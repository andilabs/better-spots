import collections
import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from accounts.models import UserFavouritesSpotList
from core.models.spots import Spot, SPOT_TYPE_CHOICES
from utils.qrcodes import make_qrcode
from .forms import ContactForm, AddSpotForm, EditSpotPhotoForm

SpotListUIConfig = collections.namedtuple('SpotListUIConfig', ['site_title', 'icon_type'])


class UserFavouritesSpotsSmugglerMixin(object):

    def get_context_data(self, **kwargs):
        context = super(UserFavouritesSpotsSmugglerMixin, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            user_favourites = dict(UserFavouritesSpotList.objects.filter(
                user_id=self.request.user.id).values_list('spot_id', 'pk'))
            context['user_favourites_spots_pks'] = user_favourites.keys()
            context['user_favourites_spots_lookup'] = user_favourites
        return context


class BaseSpotListView(UserFavouritesSpotsSmugglerMixin, ListView):
    template_name = 'www/spot_list.html'
    model = Spot
    paginate_by = 6
    context_object_name = 'spots'
    ui_context = SpotListUIConfig(site_title='browse spots', icon_type='th-large')

    def get_context_data(self, **kwargs):
        context = super(BaseSpotListView, self).get_context_data(**kwargs)
        context.update(self.ui_context._asdict())
        return context


class SpotListView(BaseSpotListView):
    pass


class CertificatedSpotListView(BaseSpotListView):
    queryset = Spot.objects.filter(is_certificated=True).order_by('name')
    ui_context = SpotListUIConfig(site_title='certificated spots', icon_type='certificate')


@method_decorator(login_required(), name='dispatch')
class FavouritesSpotListView(BaseSpotListView):
    ui_context = SpotListUIConfig(site_title='your favourites spots', icon_type='heart')

    def get_queryset(self):
        return super(FavouritesSpotListView, self).get_queryset().filter(
            pk__in=self.request.user.favourites.all()
        )


class BaseSpotDetailView(DetailView):
    model = Spot


class SpotDetailView(UserFavouritesSpotsSmugglerMixin, BaseSpotDetailView):
    template_name = 'www/spot_detail.html'


class CertificatedSpotDetailView(SpotDetailView):

    def get_queryset(self):
        return super(CertificatedSpotDetailView, self).get_queryset().filter(is_certificated=True)


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
                ) % reverse('accounts:user_create')
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
                get_template('www/add_spot.html'),
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
                get_template('www/edit_spot_photo.html'),
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
            get_template('www/pdf_sticker.html'),
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
            'category': SPOT_TYPE_CHOICES[spot.spot_type-1][1],
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


def main(request):
    if request.method == 'GET':
        response = TemplateResponse(request, get_template('www/mission.html'), {})
        return response


def map(request):
    if request.method == 'GET':
        response = TemplateResponse(request, get_template('www/map.html'), {})
        return response


def mobile(request):
    if request.method == 'GET':
        response = TemplateResponse(request, get_template('www/mobile.html'), {})
        return response
