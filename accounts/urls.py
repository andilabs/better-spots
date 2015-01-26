try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

# place app url patterns here

urlpatterns = patterns(
    '',
    url(r'^user/create/$', SpotUserCreate.as_view(), name='user_create'),
    url(r'^user/login/$', 'demo.views.mylogin', name='login'),
    url(r'^user/logout/$', 'demo.views.mylogout'),
    url(r'^user/email_verification/(?P<verification_key>[^/]+)/$', 'demo.views.mail_verification'),
    url(r'^auth_ex', 'demo.views.auth_ex'),
)
