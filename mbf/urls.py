#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import RedirectView
from django.contrib import admin
from demo.views import DogCreate, ContactView, DogspotUserCreate
from rest_framework import routers#,viewsets
from demo import views
from rest_framework.urlpatterns import format_suffix_patterns

admin.autodiscover()

# router = routers.DefaultRouter()
# router.register(r'spots/$', views.SpotViewSet)


urlpatterns = patterns(
    '',
    url(r'opinionusefulnessrating/(?P<pk>\d+)/$', views.OpinionUsefulness.as_view(), name="opinionusefulnessrating-detail"),
    url(r'opinions/(?P<pk>\d+)/$', views.OpinionDetail.as_view(), name="opinion-detail"),
    url(r'raitings/(?P<pk>\d+)/$', views.RaitingDetail.as_view(), name="raiting-detail"),
    url(r'spots/$', views.SpotList.as_view(), name="spot-list"),
    url(r'spots/(?P<pk>\d+)/$', views.SpotDetail.as_view(), name="spot-detail"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'demo.views.dogs', name='glowna'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^dogs/$', 'demo.views.dogs', name='dogs_list'),
    url(r'^map/$', 'demo.views.map', name='map'),
    url(r'^certificate/(?P<pk>\d+)/$', 'demo.views.certificate', name='certificate'),
    url(r'^about/$', 'demo.views.about', name='about'),
    url(r'^qrcode/(?P<pk>\d+)/$', 'demo.views.qrencode_vcard', name='qrcode'),
    url(r'^vcard/(?P<pk>\d+)/$', 'demo.views.download_vcard', name='vcard'),
    url(r'^favourites/$', 'demo.views.favourites', name='favourites'),
    url(r'^dogs/create/$', DogCreate.as_view(), name='dogs_add'),
    url(r'^user/create/$', DogspotUserCreate.as_view(), name='user_create'),
    url(r'^user/login/$', 'demo.views.mylogin', name='login'),
    url(r'^user/logout/$', 'demo.views.mylogout'),
    url(r'^user/email_verification/(?P<verification_key>[^/]+)/$', 'demo.views.mail_verification'),
    url(r'^auth_ex', 'demo.views.auth_ex'),
    url(r'^vcard', 'demo.views.vcard'),
    url(r'^nearby/(?P<lat>-?\d{2,3}.\d{5})/(?P<lng>-?\d{2,3}.\d{5})?/$', 'demo.views.nearby_spots'),
    url(r'^nearby/(?P<lat>-?\d{2,3}.\d{5})/(?P<lng>-?\d{2,3}.\d{5})/(?P<radius>\d*)$', 'demo.views.nearby_spots'),
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico')),
)
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])