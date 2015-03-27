from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns(
    '',

    url(r'^user/login/$',
        views.mylogin,
        name='login'),

    url(r'^user/logout/$',
        views.mylogout,
        name='logout'),

    url(r'^user/email_verification/(?P<verification_key>[^/]+)/$',
        views.mail_verification,
        name='email_verification'),
)
