import collections

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView, BaseDetailView
from django.views.generic.list import ListView

from django_filters.views import BaseFilterView
from faker.utils.text import slugify

from accounts.models import UserFavouritesSpotList
from api.spots.filtersets import SpotFilterSet
from core.models.spots import Spot
from utils.pdfs import render_to_pdf
from utils.qrcodes import make_qrcode
from .forms import AddSpotForm

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


class BaseSpotListView(BaseFilterView, UserFavouritesSpotsSmugglerMixin, ListView):
    template_name = 'www/spot_list.html'
    model = Spot
    paginate_by = 6
    context_object_name = 'spots'
    ui_context = SpotListUIConfig(site_title='browse spots', icon_type='th-large')
    filterset_class = SpotFilterSet
    strict = False

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
        context.update({'GOOGLE_MAPS_JS_API_KEY': settings.GOOGLE_MAPS_JS_API_KEY})
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


class SpotCreateView(CreateView):
    template_name = 'www/add_spot.html'
    form_class = AddSpotForm

    def get_success_url(self):
        return reverse('www:spot', args=(self.object.id,))


class PDFStickerView(DetailView):
    model = Spot
    template_name = 'www/pdf_sticker.html'

    def get(self, request, *args, **kwargs):
        spot = get_object_or_404(Spot, pk=self.kwargs.get('pk'), is_certificated=True)
        pdf, result = render_to_pdf(
            self.template_name,
            {
                'BASE_HOST': request.get_host(),
                'MEDIA_ROOT': settings.MEDIA_ROOT,
                'STATIC_ROOT': settings.STATICFILES_DIRS[0],
                'SPOT_PROJECT_NAME': settings.SPOT_PROJECT_NAME,
                'pagesize': 'A6',
                'spot': spot,
            }
        )
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return HttpResponse('We had some errors')


class QRCodeViewMixin(object):
    size = 4

    def get_source_data(self, request):
        raise NotImplementedError

    def render_to_response(self, *args, **kwargs):
        img = make_qrcode(
            self.get_source_data(self.request),
            box_size=self.kwargs.get('size', self.size)
        )
        response = HttpResponse(content_type="image/png")
        img.save(response, "png")
        return response


class QRCodeLinkView(BaseDetailView, QRCodeViewMixin):
    model = Spot

    def get_source_data(self, request):
        spot = self.get_object()
        data = "http://{}{}".format(
            request.get_host(),
            spot.www_url
        )
        return data


class QRCodeVCardView(BaseDetailView, QRCodeViewMixin):
    model = Spot

    def get_source_data(self, request):
        spot = self.get_object()
        return spot.prepare_vcard


class VCardDownloadView(DetailView):
    model = Spot
    template_name = 'www/pdf_sticker.html'

    def get(self, request, *args, **kwargs):
        spot = self.get_object()
        response = HttpResponse(spot.prepare_vcard, content_type="text/x-vcard")
        response['Content-Disposition'] = (
                'filename=vcard_from_{project_name}-{spot_name}.vcf'.format(
                    project_name=settings.SPOT_PROJECT_NAME,
                    spot_name=slugify(spot.name)
                ))
        return response
