import json

from django.db.models import Q
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from django.template.response import TemplateResponse
from django.views.generic import FormView, CreateView

from core.models import Spot, SPOT_TYPE
from utils.qrcodes import make_qrcode
from accounts.forms import UserCreationForm
from .forms import ContactForm, AddSpotForm, EditSpotPhotoForm


def main(request):
    if request.method == 'GET':
        response = TemplateResponse(request, 'www/mission.html', {})
        return response


def map(request):
    if request.method == 'GET':
        response = TemplateResponse(request, 'www/map.html', {})
        return response


def mobile(request):
    if request.method == 'GET':
        response = TemplateResponse(request, 'www/mobile.html', {})
        return response


def construct_facilities_filter(raw_get_data):
    return {
        facility: raw_get_data[facility]
        for facility in raw_get_data if facility in settings.SPOT_FACILITIES}


def spots_list(request, spot_type=None):

    spots = Spot.objects.filter(is_accepted=True).order_by('name')

    facilities = construct_facilities_filter(request.GET)
    spots = spots.filter(
        facilities__contains=facilities,
    )
    spot_types_dict = dict(SPOT_TYPE)
    if spot_type and spot_type in spot_types_dict.values():
        spot_type_index = spot_types_dict.keys()[spot_types_dict.values().index(spot_type)]
        spots = spots.filter(spot_type=spot_type_index)

    cities = None
    if request.GET.getlist('city'):
        cities = request.GET.getlist('city')
        spots = spots.filter(
            address_city__in=cities
        )

    if request.GET.getlist('is_enabled'):
        enable_status = [int(i) for i in request.GET.getlist('is_enabled')]
        spots = spots.filter(
            is_enabled__in=enable_status
        )

    return generic_spots_list(
        request,
        spots,
        site_title='browse %s %s %s' % (
            '%ss ' % spot_type if spot_type else 'spots ',
            'in %s' % ' '.join(cities) if cities else '',
            'having facilities: %s' % (' '.join(facilities.keys()).replace('_', ' ')) if facilities.keys() else '',
        ),
        icon_type='th-large')


def spot(request, pk, slug):
    spot = get_object_or_404(Spot, pk=pk)
    if not spot.is_accepted:
        messages.add_message(
            request,
            messages.WARNING,
            (
                'The spots was added by not-registred user'
                ' and it is awaiting moderation.'
            )
        )
    return render(request, 'www/spot_detail.html', {'spot': spot})


def add_spot(request):
    if request.method == 'GET':
        form = AddSpotForm()
        if not request.user.is_authenticated():
            messages.add_message(
                request,
                messages.WARNING,
                (
                    'The spots added by not-registred users'
                    ' are not visible until being peer-reviewed'
                    ' <br> If you wish to register go '
                    '<a href="%s">HERE</a> it takes just few seconds.'
                ) % reverse('user_create')
            )
        return render(
            request,
            'www/add_spot.html',
            {'form': form}
        )
    if request.method == 'POST':
        form = AddSpotForm(request.POST, request.FILES)
        if form.is_valid():
            spot = form.save()

            if request.user.is_authenticated():
                spot.creator = request.user
                spot.is_accepted = True
                spot.save()
                memo = ''
            else:
                spot.anonymous_creator_cookie = request._cookies['csrftoken']
                spot.save()
                memo = (' The spot will be visible when'
                        ' it is reviewed by our moderators')

            if spot.venue_photo:
                return redirect(
                    reverse(
                        'edit_photo',
                        kwargs={
                            "pk": spot.pk
                        }
                    )
                )
            messages.add_message(
                request,
                messages.SUCCESS, 'Spot added!' + memo
            )
            return redirect(
                reverse(
                    'spot',
                    kwargs={
                        "pk": spot.pk
                    }
                )
            )
        else:
            return render(
                request,
                'www/add_spot.html',
                {'form': form}
            )


def edit_photo(request, pk):
    spot = get_object_or_404(Spot, pk=pk)

    if request.method == 'GET':
        identify = request._cookies['csrftoken']
        if (identify == spot.anonymous_creator_cookie or request.user == spot.creator):
            form = EditSpotPhotoForm(instance=spot)
            return render(
                request,
                'www/edit_spot_photo.html',
                {'form': form, 'spot': spot}
            )
        else:
            return HttpResponse(
                'You have not acces to this resource',
                status=403)

    if request.method == 'POST':
        form = EditSpotPhotoForm(instance=spot)
        form = EditSpotPhotoForm(request.POST, request.FILES, instance=spot)
        if form.is_valid():
            spot = form.save()
            memo = (' The spot will be visible when'
                    ' it is reviewed by our moderators'
                    ) if not request.user.is_authenticated() else ''
            messages.add_message(
                request,
                messages.SUCCESS, 'Spot added!' + memo
            )
            return redirect(
                reverse(
                    'spot',
                    kwargs={
                        "pk": spot.pk
                    }
                )
            )


def favourites_list(request):
    if request.user.is_authenticated():
        spots = request.user.favourites
        return generic_spots_list(
            request,
            spots,
            site_title='your favourites spots',
            icon_type='heart')
    else:
        response = TemplateResponse(request, 'www/favourites.html')
        return response


def certificated_list(request):
    spots = Spot.objects.filter(is_certificated=True).order_by('name')
    return generic_spots_list(
        request,
        spots,
        site_title='certificated spots',
        icon_type='certificate')


def certificated(request, pk, slug=None):
    spot = get_object_or_404(Spot, pk=pk, is_certificated=True)
    return render(request, 'www/spot_detail.html', {'spot': spot})


def generic_spots_list(request, spots, site_title='Spots',
                       template='www/spot_list.html', icon_type='th'):

    paginator = Paginator(spots, 12)
    page = request.GET.get('page')
    try:
        spots = paginator.page(page)
    except PageNotAnInteger:
        spots = paginator.page(1)
    except EmptyPage:
        spots = paginator.page(paginator.num_pages)
    return render(request, template, {
        'spots': spots,
        'site_title': site_title,
        'icon_type': icon_type,
        'all_cities': Spot.objects.order_by().values_list('address_city', flat=True).distinct(),
    })


def render_to_pdf(template_src, context_dict):
    # template = get_template(template_src)
    # context = Context(context_dict)
    # html = template.render(context)
    # result = StringIO.StringIO()
    #
    # pdf = pisa.pisaDocument(
    #     StringIO.StringIO(html.encode('utf-8')),
    #     result,
    #     encoding='UTF-8')
    #
    # if not pdf.err:
    #     return HttpResponse(result.getvalue(), mimetype='application/pdf')

    return HttpResponse('We had some errors')#<pre>%s</pre>' % escape(html))


def pdf_sticker(request, pk):
    spot = get_object_or_404(Spot, pk=pk)

    if spot.is_certificated:
        return render_to_pdf(
            'www/pdf_sticker.html',
            {
                'BASE_HOST': settings.INSTANCE_DOMAIN,
                'MEDIA_ROOT': settings.MEDIA_ROOT,
                'pagesize': 'A6',
                'spot': Spot.objects.get(pk=pk),
            }
        )
    else:
        raise Http404


def ajax_search(request):
    query = request.GET.get('q', '')
    result = [
        {
            'name': spot.name,
            'category': SPOT_TYPE[spot.spot_type-1][1],
            'url': spot.www_url,
            'thumb': spot.thumbnail_venue_photo,
            'address': spot.address,
        }
        for spot in Spot.objects.filter(
            Q(name__icontains=query) | Q(address_city__icontains=query),
            is_accepted=True).order_by('spot_type')[:7]
    ]

    return HttpResponse(
        json.dumps(result, ensure_ascii=False),
        content_type="application/json")


def qrencode_link(request, pk, size=3, for_view='spot-detail'):
    spot = get_object_or_404(Spot, pk=pk)
    dane = "http://%s%s" % (
        settings.INSTANCE_DOMAIN,
        reverse(for_view, kwargs={'pk': spot.pk}))
    img = make_qrcode(dane, box_size=size)
    response = HttpResponse(content_type="image/png")
    img.save(response, "png")
    return response


def qrencode_vcard(request, pk, size=3):
    spot = get_object_or_404(Spot, pk=pk)
    img = make_qrcode(spot.prepare_vcard, box_size=size)
    response = HttpResponse(content_type="image/png")
    img.save(response, "png")
    return response


def download_vcard(request, pk):
    spot = get_object_or_404(Spot, pk=pk)
    response = HttpResponse(spot.prepare_vcard, content_type="text/x-vcard")
    response['Content-Disposition'] = (
        'filename=vcard_from_%s.vcf' % settings.SPOT_PROJECT_NAME)
    return response


class SpotUserCreate(CreateView):
    template_name = 'www/spotuser_form.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.WARNING,
            'Your account was created, but it is not active.' +
            ' We sent you e-mail with confrimation link')

        return super(SpotUserCreate, self).form_valid(form)


class ContactView(FormView):
    template_name = 'www/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        content = form.cleaned_data.get('message')
        to = str(form.cleaned_data.get('mail'))
        msg = EmailMessage(
            "contact form",
            content,
            settings.EMAIL_HOST_USER,
            [to, ]
        )
        msg.send()

        messages.add_message(
            self.request,
            messages.SUCCESS, 'Your message was sucessfully sent!'
            )
        return super(ContactView, self).form_valid(form)
