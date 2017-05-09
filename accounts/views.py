import base64
import uuid
from datetime import timedelta

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.utils import timezone
from django.views.generic import CreateView

from .models import EmailVerification
from .forms import UserCreationForm


def mail_verification(request, verification_key):

    try:
        existing_account = EmailVerification.objects.get(
            verification_key=verification_key)
        user = existing_account.user

        if user.mail_verified is True:

                messages.add_message(
                    request, messages.SUCCESS,
                    "Your account is arleady active! Just log in!")
                return redirect('login')

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
                return redirect('login')

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
                return redirect('login')

    except EmailVerification.DoesNotExist:

        messages.add_message(
            request, messages.ERROR,
            "Account does not exist")
        return redirect('user_create')


class SpotUserCreate(CreateView):
    template_name = 'www/spotuser_form.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.WARNING,
            'Your account was created, but it is not active.' +
            ' We sent you e-mail with confrimation link')

        return super(SpotUserCreate, self).form_valid(form)


def mylogin(request):

    if request.method == 'GET':
        response = TemplateResponse(request, 'www/login.html', {})
        return response

    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)

        if user:

            if user.mail_verified:
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
                return redirect('login')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Your provided invalid credentials')

            return redirect('login')


def mylogout(request):

    if request.method == 'GET':

        if request.user.is_authenticated():
            logout(request)

        messages.add_message(
            request, messages.SUCCESS,
            'You sucessfully log out!')

        return redirect('www:main')
