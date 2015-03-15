from django.conf.urls import *
from www.views import ContactView, SpotUserCreate

# place app url patterns here
urlpatterns = patterns(
    '',
    url(r'^$', 'www.views.main', name='main'),
    url(r'^ajax_search/$', 'www.views.ajax_search'),

    url(r'^mobile/', 'www.views.mobile', name='mobile'),
    url(r'^user/create/$', SpotUserCreate.as_view(), name='user_create'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^map/$', 'www.views.map', name='map'),

    url(r'^certificated/$', 'www.views.certificated_list', name='certificated_list'),
    url(r'^certificated/(?P<pk>\d+)(?:/(?P<slug>[\w\d-]+))?/$', 'www.views.certificated', name='certificated_detail'),

    url(r'^favourites/$', 'www.views.favourites_list', name='favourites_list'),

    url(r'^spots/$', 'www.views.spots_list', name='spots_list'),
    url(r'^spots/(?P<pk>\d+)(?:/(?P<slug>[\w\d-]+))?/$', 'www.views.spot', name='spot'),

    url(r'^qrcode/(?P<pk>\d+)/(?P<size>\d*)/?$', 'www.views.qrencode_vcard', name='qrcode_scaled'),

    url(r'^qrcode_link/(?P<pk>\d+)/(?P<size>\d*)/?$', 'www.views.qrencode_link', name='qrencode_link'),
    url(r'^qrcode_link/(?P<pk>\d+)/(?P<size>\d*)/(?P<for_view>.+)?$', 'www.views.qrencode_link', name='qrencode_link'),

    url(r'^qrcode_vcard/(?P<pk>\d+)/(?P<size>\d*)/?$', 'www.views.qrencode_vcard', name='qrcode_vcard'),

    url(r'^vcard/(?P<pk>\d+)/$', 'www.views.download_vcard', name='vcard'),
    url(r'^pdf/(?P<pk>\d+)/$', 'www.views.pdf_sticker', name='pdf_sticker'),

)