#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf.urls.static import static


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'', include('accounts.urls')),
    url(r'api/', include('api.urls')),
    # url(r'', include('core.urls')),
    url(r'', include('www.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon\.ico$', RedirectView.as_view(
        url=settings.SPOT_PROJECT_FAVICON_URL)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
