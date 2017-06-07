import base64
import uuid
from datetime import timedelta

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils import timezone
from django.views.generic import CreateView

from .models import EmailVerification
from .forms import UserCreationForm


class UserCreate(CreateView):
    template_name = 'accounts/user_form.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.WARNING,
            'Your account was created, but it is not active.' +
            ' We sent you e-mail with confrimation link')

        return super(UserCreate, self).form_valid(form)


# TODO: DO IT BETTER WITHOUT DB PERSISTANCE
def mail_verification(request, verification_key):

    try:
        existing_account = EmailVerification.objects.get(
            verification_key=verification_key)
        user = existing_account.user

        if user.mail_verified is True:

                messages.add_message(
                    request, messages.SUCCESS,
                    "Your account is arleady active! Just log in!")
                return redirect('accounts:login')

        else:

            if timezone.now() - existing_account.key_timestamp < timedelta(
                    hours=settings.EMAIL_VERIFY_KEY_EXPIREATION_PERIOD_HOURS):

                user.mail_verified = True
                user.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    ("Account was activated! Log in and enjoy %s!" %
                     settings.SPOT_PROJECT_NAME)
                )
                return redirect('accounts:login')

            else:

                email_verification = EmailVerification(
                    verification_key=base64.urlsafe_b64encode(
                        uuid.uuid4().bytes)[:21],
                    user=user)
                email_verification.save()
                messages.add_message(
                    request, messages.WARNING,
                    "The E-mail verification link has expired. We"
                    + " will send you the new one activation link"
                    + " to the e-mail: %s" % existing_account.user.email)
                return redirect('accounts:login')

    except EmailVerification.DoesNotExist:

        messages.add_message(
            request, messages.ERROR,
            "Account does not exist")
        return redirect('accounts:user_create')


# TODO use django.contrib.auth.views.LoginView
# https://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.views.LoginView


def mylogin(request):

    if request.method == 'GET':
        response = TemplateResponse(request, 'www/login.html', {})
        return response

    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)

        if user:

            if user.mail_verified or 1==1:
                login(request, user)
                messages.add_message(
                    request,
                    messages.SUCCESS, 'You were sucessfully logged in!')
                return redirect('www:main')
            else:
                messages.add_message(
                    request,
                    messages.WARNING,
                    'Your account is not active. Check your mailbox and verify'
                    + ' E-mail by clicking the link we sent you.')
                return redirect('accounts:login')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Your provided invalid credentials')

            return redirect('accounts:login')


def mylogout(request):

    if request.method == 'GET':

        if request.user.is_authenticated():
            logout(request)

        messages.add_message(
            request, messages.SUCCESS,
            'You sucessfully log out!')

        return redirect('www:main')


# TODO password reset
# https://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.views.PasswordResetView
# https://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.views.PasswordResetConfirmView
# https://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.views.PasswordResetDoneView
# https://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.views.PasswordResetCompleteView
