from django.conf.urls import *
from www.views import ContactView

# place app url patterns here
urlpatterns = patterns(
    '',
    url(r'^ajax_search/$', 'www.views.ajax_search'),

    url(r'^pdf/(?P<pk>\d+)/$', 'www.views.pdf_sticker', name="pdf_sticker"),
    url(r'^$', 'www.views.main', name='main'),
    url(r'^mobile/', 'www.views.mobile', name='mobile'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^map/$', 'www.views.map', name='map'),
    url(r'^map_two/$', 'www.views.map_two', name='map_two'),
    url(r'^certificate/(?P<pk>\d+)/$', 'www.views.certificate', name='certificate'),
    url(r'^favourites/$', 'www.views.favourites', name='favourites'),
    url(r'^about/$', 'www.views.about', name='about'),

    url(r'^qrcode_link/(?P<pk>\d+)/(?P<size>\d*)/?$', 'www.views.qrencode_link', name='qrencode_link'),
    url(r'^qrcode_vcard/(?P<pk>\d+)/(?P<size>\d*)/?$', 'www.views.qrencode_vcard', name='qrcode_vcard'),
    url(r'^qrcode/(?P<pk>\d+)/(?P<size>\d*)/?$', 'www.views.qrencode_vcard', name='qrcode_scaled'),
    url(r'^vcard/(?P<pk>\d+)/$', 'www.views.download_vcard', name='vcard'),
)