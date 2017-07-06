#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

admin.autodiscover()

urlpatterns = [

    url(r'', include('www.urls', namespace='www')),
    url(r'accounts/', include('accounts.urls', namespace='accounts')),
    url(r'api/', include('api.urls', namespace='api')),
    url(r'blog/', include('blog.urls', namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.SPOT_PROJECT_FAVICON_URL)),
    url(r'^apple-touch-icon-120x120\.png$', RedirectView.as_view(url='static/%s/apple-touch-icon-120x120.png' % (settings.SPOT_PROJECT_NAME))),
    url(r'^api/docs/', include_docs_urls(title='{} API'.format(settings.SPOT_PROJECT_NAME))),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
