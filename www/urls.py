from django.conf.urls import url
from django.views.generic import TemplateView


from www import views

# place app url patterns here
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="www/mission.html"), name='main'),
    url(r'^ajax_search/$', views.ajax_search, name='ajax_search'),
    url(r'^certificated/$', views.CertificatedSpotListView.as_view(), name='certificated_list'),
    url(r'^certificated/(?P<pk>\d+)(?:/(?P<slug>[\w\d-]+))?/$', views.CertificatedSpotDetailView.as_view(), name='certificated_detail'),
    url(r'^favourites/$', views.FavouritesSpotListView.as_view(), name='favourites_list'),
    url(r'^map/$', views.MapView.as_view(), name='map'),
    url(r'^mobile/', TemplateView.as_view(template_name="www/mobile.html"), name='mobile'),
    url(r'^pdf/(?P<pk>\d+)/$', views.pdf_sticker, name='pdf_sticker'),
    url(r'^qrcode/(?P<pk>\d+)/(?P<size>\d*)/?$', views.qrencode_vcard, name='qrcode_scaled'),
    url(r'^qrcode_link/(?P<pk>\d+)/(?P<size>\d*)/?$', views.qrencode_link, name='qrencode_link'),
    url(r'^qrcode_link/(?P<pk>\d+)/(?P<size>\d*)/(?P<for_view>.+)?$', views.qrencode_link, name='qrencode_link'),
    url(r'^qrcode_vcard/(?P<pk>\d+)/(?P<size>\d*)/?$', views.qrencode_vcard, name='qrcode_vcard'),
    url(r'^spots/$', views.SpotListView.as_view(), name='spots_list'),
    url(r'^spots/add/$', views.add_spot, name='add_spot'),
    url(r'^spots/(?P<pk>\d+)(?:/(?P<slug>[\w\d-]+))?/$', views.SpotDetailView.as_view(), name='spot'),
    url(r'^edit_photo/(?P<pk>\d+)/$', views.edit_photo, name='edit_photo'),
    url(r'^vcard/(?P<pk>\d+)/$', views.download_vcard, name='vcard'),
    url(r'^react/(?:.*)/?$', views.index),
]
