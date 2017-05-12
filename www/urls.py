

from django.conf.urls import *
from www import views
from www.views import ContactView, SpotUserCreate

# place app url patterns here
urlpatterns = [

    url(r'^$', views.main, name='main'),

    url(r'^ajax_search/$', views.ajax_search, name='ajax_search'),

    url(r'^certificated/$', views.CertificatedSpotListView.as_view(), name='certificated_list'),

    url(r'^certificated/(?P<pk>\d+)(?:/(?P<slug>[\w\d-]+))?/$', views.CertificatedSpotDetailView.as_view(), name='certificated_detail'),

    url(r'^contact/$', ContactView.as_view(), name='contact'),

    url(r'^favourites/$', views.FavouritesSpotListView.as_view(), name='favourites_list'),

    url(r'^map/$', views.map, name='map'),

    url(r'^mobile/', views.mobile, name='mobile'),

    url(r'^pdf/(?P<pk>\d+)/$', views.pdf_sticker, name='pdf_sticker'),

    url(r'^qrcode/(?P<pk>\d+)/(?P<size>\d*)/?$', views.qrencode_vcard, name='qrcode_scaled'),

    url(r'^qrcode_link/(?P<pk>\d+)/(?P<size>\d*)/?$', views.qrencode_link, name='qrencode_link'),

    url(r'^qrcode_link/(?P<pk>\d+)/(?P<size>\d*)/(?P<for_view>.+)?$', views.qrencode_link, name='qrencode_link'),

    url(r'^qrcode_vcard/(?P<pk>\d+)/(?P<size>\d*)/?$', views.qrencode_vcard, name='qrcode_vcard'),

    url(r'^spots/$', views.SpotListView.as_view(), name='spots_list'),

    url(r'^spots/add/$', views.add_spot, name='add_spot'),

    url(r'^spots/(?P<pk>\d+)(?:/(?P<slug>[\w\d-]+))?/$', views.SpotDetailView.as_view(), name='spot'),

    url(r'^edit_photo/(?P<pk>\d+)/$', views.edit_photo, name='edit_photo'),

    url(r'^user/create/$', SpotUserCreate.as_view(), name='user_create'),

    url(r'^vcard/(?P<pk>\d+)/$', views.download_vcard, name='vcard'),
]
