from django.conf.urls import patterns, url
from views import SpotUserCreate

urlpatterns = patterns(
    '',
    url(r'^user/create/$', SpotUserCreate.as_view(), name='user_create'),
    url(r'^user/login/$', 'accounts.views.mylogin', name='login'),
    url(r'^user/logout/$', 'accounts.views.mylogout'),
    url(r'^user/email_verification/(?P<verification_key>[^/]+)/$', 'accounts.views.mail_verification'),
)
