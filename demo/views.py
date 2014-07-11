# -*- coding: utf-8 -*-

import json
import base64
import quopri
import vobject
from datetime import datetime, timedelta

from django.http import QueryDict
from django.http import HttpResponse
from django.conf import settings
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.views.generic import FormView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.core.mail import EmailMessage

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token


from demo.authentication import ExpiringTokenAuthentication
from demo.forms import (
    ContactForm,
    UserCreationForm,
    send_email_with_verifiaction_key
    )
from demo.models import DogspotUser, Dog, EmailVerification
from django import template
from django.utils import timezone

register = template.Library()


# @register.filter
# def in_category(things, category):
#     return things.filter(category=category)


def mail_verification(request, verification_key):

    try:

        existing_account = EmailVerification.objects.get(
            verification_key=verification_key)
        user = existing_account.user

        if user.mail_sent is True:
                messages.add_message(
                    request, messages.SUCCESS,
                    "Your account is arleady active! Just log in!")
                return redirect('login')

        else:

            if timezone.now() - existing_account.key_timestamp < timedelta(
                    hours=settings.EMAIL_VERIFY_KEY_EXPIREATION_PERIOD_HOURS):
                user.mail_sent = True
                user.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    "Account was activated! Log in and enjoy dogspot!")
                return redirect('login')

            else:
                send_email_with_verifiaction_key(user)
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


def send_email(mail_content, to, subject="contact form"):
    to = str(to)
    msg = EmailMessage(subject, mail_content, settings.EMAIL_HOST_USER, [to, ])
    msg.send()


def map(request):
    if request.method == 'GET':
        response = TemplateResponse(request, 'map.html', {})
        return response


def favorites(request):
    if request.method == 'GET':
        response = TemplateResponse(request, 'favorites.html', {})
        return response


def about(request):
    if request.method == 'GET':
        response = TemplateResponse(request, 'about.html', {})
        return response


def mylogin(request):
    if request.method == 'GET':
        response = TemplateResponse(request, 'login.html', {})
        return response
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.mail_sent:
                login(request, user)
                messages.add_message(
                    request,
                    messages.SUCCESS, 'You were sucessfully logged in!')
                return redirect('glowna')
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Your account is not active. Check your mailbox and verify'
                    + ' E-mail by clicking the link we send you.')
                return redirect('login')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Your provided invalid credentials'
                )
            return redirect('login')


def mylogout(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            logout(request)
        messages.add_message(
            request, messages.SUCCESS, 'You sucessfully log out!')
        return render_to_response(
            'login.html',
            context_instance=RequestContext(request)
            )


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        content = form.cleaned_data.get('message')
        send_email(content, form.cleaned_data.get('mail'))
        messages.add_message(
            self.request,
            messages.SUCCESS, 'Your message was sucessfully sent!'
            )
        return redirect('glowna')
        return super(ContactView, self).form_valid(form)


class DogspotUserCreate(CreateView):
    template_name = 'demo/dogspotuser_form.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Your account was created, but it is not active.' +
            ' We sent you e-mail with confrimation link'
            )
        super(DogspotUserCreate, self).form_valid(form)
        return redirect('login')


#@login_required
def dogs(request):
    dogs_list = Dog.objects.all()
    paginator = Paginator(dogs_list, 6)
    page = request.GET.get('page')
    try:
        dogs = paginator.page(page)
    except PageNotAnInteger:
        dogs = paginator.page(1)
    except EmptyPage:
        dogs = paginator.page(paginator.num_pages)
    return render(request, 'dog_list.html', {'dogs': dogs})


class DogCreate(CreateView):
    model = Dog
    fields = ('name', 'sex', 'bred', 'comment')
    success_url = '/dogs'


@csrf_exempt
def auth_ex(request):
    """
        Method is responsible to provide TOKEN
        to sucessfully authenticated user
        Following parameters should be passed in HTTP POST:
        - email
        - password

        EXAMPLE CALL:
        curl -X POST http://127.0.0.1:8000/auth_ex -d "email=andrzej.kostanski@daftcode.pl&password=andi"
        EXAMPLE RESP (without headers):
        {"token": "3a3f1cd20ee72b468a9bd7d6ab20e2e0a408ead5"}
    """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        time_now = datetime.now()  # .replace(tzinfo=utc)
        if user is not None:
            if user.is_active:
                token, created = Token.objects.get_or_create(
                    user=DogspotUser.objects.get(email=email))
                if not created and token.created < time_now - timedelta(
                        hours=settings.TOKEN_EXPIRES_AFTER):
                    token.delete()
                    token = Token.objects.create(
                        user=DogspotUser.objects.get(email=email)
                        )
                    token.created = datetime.now()
                    token.save()
                return HttpResponse(
                    json.dumps({'token': token.key}),
                    content_type="application/json; charset=UTF-8"
                )
            else:
                return HttpResponse('Unauthorized', status=401)
        else:
            return HttpResponse('Unauthorized', status=401)
    else:
        return HttpResponse("Bye others", content_type="text/plain")


@api_view(['PUT'])
@authentication_classes((ExpiringTokenAuthentication, ))
@permission_classes((IsAuthenticated,))
def vcard(request):
    """
        Method is responsible for reciving VCARDS and
        adding them to the CollectedContacts of sending exhibitor
        Method works only if provided with valid token
        in headers parameters via HTTP PUT
        method expects parameters:
        - fair_id
        - vcard in base64 format

        EXAMPLE CALL:
        curl -X PUT http://127.0.0.1:8000/vcard -v -H 'Authorization: Token 3a3f1cd20ee72b468a9bd7d6ab20e2e0a408ead5' -d "fair_id=1&vcard=<BASE_64_STRING>"
    """
    if request.method == 'PUT':
        put = QueryDict(request.body)
        fair_id = int(put.get('fair_id'))
        this_user = DogspotUser.objects.get(email=request.user)
        try:
            this_exhibitor = Exhibitor.objects.get(user=this_user, fair=fair_id)
        except Exhibitor.DoesNotExist:
            error_message = {
                "valid": False,
                "reason": "User is not exhibitor at fairs with id={0}".format(fair_id)}
            return HttpResponse(json.dumps(error_message), status=403)
        vcard = put.get('vcard')
        try:
            vcard_readable = base64.decodestring(vcard)
            quoted_printable_vcard = quopri.encodestring(vcard_readable)
            vobj = vobject.readOne(quoted_printable_vcard)
        except UnicodeEncodeError as e:  # case of bad encoding
            error_message = {
                "valid": False,
                "reason": "Invalid vCard\n{0}".format(e)}
            return HttpResponse(json.dumps(error_message), status=200)
        except vobject.base.VObjectError as e2:  # case of invalid vcard
            error_message = {
                "valid": False,
                "reason": "Invalid vCard format\n{0}".format(e2)}
            return HttpResponse(json.dumps(error_message), status=200)
        except:
            error_message = {
                "valid": False,
                "reason": "Invalid vCard."}
            return HttpResponse(json.dumps(error_message), status=200)
        cc = CollectedContact(exhibitor=this_exhibitor, vcard=vcard_readable)
        cc.save()
        return HttpResponse(status=200)
