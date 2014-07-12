#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import RedirectView
from django.contrib import admin
from demo.views import DogCreate, ContactView, DogspotUserCreate
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'demo.views.dogs', name='glowna'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^dogs/$', 'demo.views.dogs', name='dogs_list'),
    url(r'^map/$', 'demo.views.map', name='map'),
    url(r'^certificate/$', 'demo.views.certificate', name='certificate'),
    url(r'^about/$', 'demo.views.about', name='about'),
    url(r'^favorites/$', 'demo.views.favorites', name='favorites'),
    url(r'^dogs/create/$', DogCreate.as_view(), name='dogs_add'),
    url(r'^user/create/$',
        DogspotUserCreate.as_view(),
        name='user_create'),
    url(r'^user/login/$', 'demo.views.mylogin', name='login'),
    url(r'^user/logout/$', 'demo.views.mylogout'),
    url(r'^user/email_verification/(?P<verification_key>[^/]+)/$',
        'demo.views.mail_verification'),
    url(r'^auth_ex', 'demo.views.auth_ex'),
    url(r'^vcard', 'demo.views.vcard'),
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico')),
)
