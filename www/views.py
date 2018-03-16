import collections

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.http.response import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


from accounts.models import UserFavouritesSpotList
from core.models.spots import Spot, SPOT_TYPE_CHOICES
from utils.pdfs import render_to_pdf
from utils.qrcodes import make_qrcode
from utils.search import spots_full_text_search
from .forms import AddSpotForm, EditSpotPhotoForm

SpotListUIConfig = collections.namedtuple('SpotListUIConfig', ['site_title', 'icon_type'])


class UserFavouritesSpotsSmugglerMixin(object):

    def get_context_data(self, **kwargs):
        context = super(UserFavouritesSpotsSmugglerMixin, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
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

    def get_context_data(self, **kwargs):
        context = super(BaseSpotDetailView, self).get_context_data(**kwargs)
        context.update({'GOOGLE_API_KEY': settings.GOOGLE_API_KEY})
        return context


class SpotDetailView(UserFavouritesSpotsSmugglerMixin, BaseSpotDetailView):
    template_name = 'www/spot_detail.html'


class CertificatedSpotDetailView(SpotDetailView):

    def get_queryset(self):
        return super(CertificatedSpotDetailView, self).get_queryset().filter(is_certificated=True)


class MapView(TemplateView):
    template_name = 'www/map.html'

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context.update({'SPOT_PROJECT_NAME': settings.SPOT_PROJECT_NAME})
        return context


def add_spot(request):
    if request.method == 'GET':
        form = AddSpotForm()
        if not request.user.is_authenticated:
            messages.add_message(
                request,
                messages.WARNING,
                (
                    'The spots added by not-registred accounts'
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

            if request.user.is_authenticated:
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
                        'www:edit_photo',
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
                    'www:spot',
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
        csrf_token = get_token(request)
        if csrf_token == spot.anonymous_creator_cookie or request.user == spot.creator:
            form = EditSpotPhotoForm(instance=spot)
            return render(
                request,
                get_template('www/edit_spot_photo.html'),
                {'form': form, 'spot': spot}
            )
        else:
            return HttpResponse(
                'You have not acces to this resource',
                status=403
            )

    if request.method == 'POST':
        form = EditSpotPhotoForm(request.POST, request.FILES, instance=spot)
        if form.is_valid():
            spot = form.save()
            memo = (' The spot will be visible when'
                    ' it is reviewed by our moderators'
                    ) if not request.user.is_authenticated else ''
            messages.add_message(
                request,
                messages.SUCCESS, 'Spot added!' + memo
            )
            return redirect(
                reverse('spot', kwargs={"pk": spot.pk})
            )


def pdf_sticker(request, pk):
    spot = get_object_or_404(Spot, pk=pk)
    if spot.is_certificated:
        pdf, result = render_to_pdf(
            'www/pdf_sticker.html',
            {
                'BASE_HOST': request.get_host(),
                'MEDIA_ROOT': settings.MEDIA_ROOT,
                'STATIC_ROOT': settings.STATICFILES_DIRS[0],
                'SPOT_PROJECT_NAME': settings.SPOT_PROJECT_NAME,
                'pagesize': 'A6',
                'spot': Spot.objects.get(pk=pk),
            }
        )
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return HttpResponse('We had some errors')
    else:
        raise Http404


def ajax_search(request):
    query = request.GET.get('q', '')
    fts_resulted_spots = spots_full_text_search(query)
    result = [
        {
            'name': spot.name,
            'category': SPOT_TYPE_CHOICES[spot.spot_type-1][1],
            'url': spot.www_url,
            'thumb': spot.thumbnail_venue_photo,
            'tags': [tag.text for tag in spot.tags.all()],
            'address': spot.address,
            'rank': spot.rank,
        }
        for spot in fts_resulted_spots
    ]
    return JsonResponse(result, safe=False)


def qrencode_link(request, pk, size=3, for_view='www:spot'):
    spot = get_object_or_404(Spot, pk=pk)
    data = "http://%s%s" % (
        request.get_host(),
        reverse(for_view, kwargs={'pk': spot.pk}))
    img = make_qrcode(data, box_size=size)
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
