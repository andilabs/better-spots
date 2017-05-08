#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.conf import settings
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [

    url(r'', include('accounts.urls', namespace='accounts')),

    url(r'', include('www.urls', namespace='www')),

    url(r'api/', include('api.urls', namespace='api')),

    url(r'blog/', include('blog.urls', namespace='blog')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^favicon\.ico$', RedirectView.as_view(
        url=settings.SPOT_PROJECT_FAVICON_URL)),

    url(r'^apple-touch-icon-120x120\.png$', RedirectView.as_view(
        url='static/%s/apple-touch-icon-120x120.png' % (
            settings.SPOT_PROJECT_NAME))),

]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
#   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
