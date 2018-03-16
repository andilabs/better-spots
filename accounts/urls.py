from django.conf.urls import url

from accounts.views import (
    mail_verification,
    mylogin,
    mylogout,
    UserCreate
)

urlpatterns = [
    url(r'^login/$', mylogin, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html')),

    url(r'^logout/$', mylogout, name='logout'),
    url(r'^email_verification/(?P<verification_key>[^/]+)/$', mail_verification, name='email_verification'),
    url(r'^create/$', UserCreate.as_view(), name='user_create'),
]
