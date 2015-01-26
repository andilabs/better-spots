try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

# place app url patterns here
urlpatterns = patterns(
    '',
    url(r'^ajax_search/$', views.ajax_search),

    url(r'^pdf/(?P<pk>\d+)/$', 'demo.views.pdf_sticker', name="pdf_sticker"),
    url(r'^$', 'demo.views.main', name='main'),
    url(r'^mobile/', 'demo.views.mobile', name='mobile'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^map/$', 'demo.views.map', name='map'),
    url(r'^map_two/$', 'demo.views.map_two', name='map_two'),
    url(r'^certificate/(?P<pk>\d+)/$', 'demo.views.certificate', name='certificate'),
    url(r'^favourites/$', 'demo.views.favourites', name='favourites'),
    url(r'^about/$', 'demo.views.about', name='about'),

    url(r'^qrcode_link/(?P<pk>\d+)/(?P<size>\d*)/?$', 'demo.views.qrencode_link', name='qrencode_link'),
    url(r'^qrcode_vcard/(?P<pk>\d+)/(?P<size>\d*)/?$', 'demo.views.qrencode_vcard', name='qrcode_vcard'),
    url(r'^qrcode/(?P<pk>\d+)/(?P<size>\d*)/?$', 'demo.views.qrencode_vcard', name='qrcode_scaled'),
    url(r'^vcard/(?P<pk>\d+)/$', 'demo.views.download_vcard', name='vcard'),
    url(r'^vcard', 'demo.views.vcard'),
)