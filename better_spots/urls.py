from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

admin.autodiscover()

urlpatterns = [

    url(r'', include(('www.urls', 'www'), namespace='www')),
    url(r'accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    url(r'api/', include(('api.urls', 'api'), namespace='api')),
    url(r'blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('admin/', admin.site.urls),

    url(r'^favicon\.ico$', RedirectView.as_view(url='static/{}/favicon.ico'.format(settings.SPOT_PROJECT_NAME))),
    url(r'^apple-touch-icon-120x120\.png$', RedirectView.as_view(url='static/%s/apple-touch-icon-120x120.png' % (settings.SPOT_PROJECT_NAME))),
    url(r'^api/docs/', include_docs_urls(title='{} API'.format(settings.SPOT_PROJECT_NAME))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
