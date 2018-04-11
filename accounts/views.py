from django.conf import settings
from django.contrib import messages
from django.contrib.auth.views import LogoutView, LoginView
from django.core.signing import SignatureExpired, BadSignature
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, TemplateView

from accounts.forms import BSAuthenticationForm
from accounts.models import User
from utils.signer import decrypt_data
from .forms import BSUserCreationForm


class UserCreate(CreateView):
    template_name = 'accounts/user_form.html'
    form_class = BSUserCreationForm
    success_url = '/'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.WARNING,
            'Your account was created, but it is not active.' +
            ' We sent you e-mail with confirmation link')

        return super(UserCreate, self).form_valid(form)


class MailConfirmView(TemplateView):
    template_name = 'www/login.html'

    def get(self, request, *args, **kwargs):
        verification_key = self.kwargs.get('verification_key')
        try:
            decrypted = decrypt_data(verification_key, max_age=settings.EMAIL_VERIFY_KEY_EXPIRATION_PERIOD_HOURS*3600)
            claimed_email = decrypted['signed_data'].split(':')[0]
            resulting_email = decrypted['result']

            if claimed_email == resulting_email:
                user = get_object_or_404(User, email=claimed_email)
                user.mail_verified = True
                user.save()
                messages.add_message(
                    self.request, messages.SUCCESS,
                    "Your account is now active you can login!")
                return redirect('accounts:login')

        except SignatureExpired:
            messages.add_message(
                self.request, messages.WARNING,
                "The E-mail verification link has expired.")
            return redirect('accounts:login')

        except BadSignature:
            messages.add_message(
                self.request, messages.WARNING,
                "The E-mail verification link is broken.")

            return redirect('accounts:login')


class BSLoginView(LoginView):
    form_class = BSAuthenticationForm
    template_name = 'www/login.html'


class BSLogoutView(LogoutView):
    template_name = 'www/base.html'

    def get_next_page(self):
        next_page = super(BSLogoutView, self).get_next_page()
        messages.add_message(
            self.request, messages.SUCCESS,
            'You successfully log out!'
        )
        return next_page


# TODO password reset
# https://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.views.PasswordResetView
# https://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.views.PasswordResetConfirmView
# https://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.views.PasswordResetDoneView
# https://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.views.PasswordResetCompleteView
