from django.conf import settings
from django.conf.urls import url

from accounts.views import (
    BSLoginView,
    BSLogoutView,
    MailConfirmView,
    UserCreate,
)

urlpatterns = [
    url(r'^login/$', BSLoginView.as_view(), name='login'),
    url(r'^logout/$', BSLogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^email_verification/(?P<verification_key>[^/]+)/$', MailConfirmView.as_view(), name='email_verification'),
    url(r'^create/$', UserCreate.as_view(), name='user_create'),
]
