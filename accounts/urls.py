from django.conf.urls import url

from accounts import views

urlpatterns = [
    url(r'^user/login/$',
        views.mylogin,
        name='login'),

    url(r'^user/logout/$',
        views.mylogout,
        name='logout'),

    url(r'^user/email_verification/(?P<verification_key>[^/]+)/$',
        views.mail_verification,
        name='email_verification'),
]
