from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^user/login/$', 'accounts.views.mylogin', name='login'),
    url(r'^user/logout/$', 'accounts.views.mylogout'),
    url(r'^user/email_verification/(?P<verification_key>[^/]+)/$', 'accounts.views.mail_verification'),
)
