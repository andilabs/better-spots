# -*- coding: utf-8 -*-

import json
import base64
import quopri
import vobject
import qrcode
from datetime import datetime, timedelta

from django.http import QueryDict
from django.http import HttpResponse
from django.conf import settings
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
from django.utils import timezone

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
from rest_framework import generics

from demo.models import (
    Spot, DogspotUser, Dog, EmailVerification,
    Raiting, Opinion, OpinionUsefulnessRating, OtoFoto, SPOT_TYPE)
from demo.serializers import (
    SpotDetailSerializer,
    SpotWithDistanceSerializer, SpotListSerializer, RaitingSerializer,
    OpinionSerializer, OpinionUsefulnessRatingSerializer,
    DogspotUserSerializer, OtoFotoSerializer)
from demo.authentication import ExpiringTokenAuthentication
from demo.forms import (
    ContactForm,
    UserCreationForm,
    send_email_with_verifiaction_key)


def ajax_search(request):
    query = request.GET.get('q', '')
    result = [{'name': s.name,
               'category': SPOT_TYPE[s.spot_type-1][1],
               'url': '/spots/%s' % str(s.id)} for s in Spot.objects.filter(
        name__icontains=query).order_by('spot_type')]

    return HttpResponse(json.dumps(result, ensure_ascii=False),
                        content_type="application/json")


class OtoFotoDetail(generics.RetrieveUpdateDestroyAPIView):
    model = OtoFoto
    serializer_class = OtoFotoSerializer


class OtoFotoList(generics.ListCreateAPIView):
    serializer_class = OtoFotoSerializer

    def get_queryset(self):
        queryset = OtoFoto.objects.all()
        return queryset


class DogspotUserList(generics.ListCreateAPIView):
    serializer_class = DogspotUserSerializer

    def get_queryset(self):
        queryset = DogspotUser.objects.all()
        return queryset


class DogspotUserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = DogspotUser
    serializer_class = DogspotUserSerializer


class SpotList(generics.ListCreateAPIView):
    serializer_class = SpotListSerializer

    def get_queryset(self):
        queryset = Spot.objects.all()
        return queryset


class OpinionUsefulness(generics.RetrieveUpdateDestroyAPIView):
    model = OpinionUsefulnessRating
    serializer = OpinionUsefulnessRatingSerializer


class OpinionDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Opinion
    serializer_class = OpinionSerializer


class RaitingList(generics.ListCreateAPIView):
    serializer_class = RaitingSerializer

    def get_queryset(self):
        queryset = Raiting.objects.all()
        return queryset


class RaitingDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Raiting
    serializer_class = RaitingSerializer


class SpotDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Spot
    serializer_class = SpotDetailSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def nearby_spots(request, lat, lng, radius=5000, limit=50):

    radius = float(radius) / 1000.0

    kwerenda = """SELECT id, (6367*acos(cos(radians(%2f))
               *cos(radians(latitude))*cos(radians(longitude)-radians(%2f))
               +sin(radians(%2f))*sin(radians(latitude))))
               AS distance FROM demo_spot HAVING
               distance < %d ORDER BY distance LIMIT 0, %d""" % (
        float(lat),
        float(lng),
        float(lat),
        radius,
        limit
    )

    queryset = Spot.objects.raw(kwerenda)

    serializer = SpotWithDistanceSerializer(queryset, many=True)

    return JSONResponse(serializer.data)


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


def favourites(request):
    if request.method == 'GET':
        response = TemplateResponse(request, 'favourites.html', {})
        return response


def about(request):
    if request.method == 'GET':
        response = TemplateResponse(request, 'about.html', {})
        return response


def certificate(request, pk):

    try:
        spot = Spot.objects.get(pk=pk)
        if request.method == 'GET':

            link = '/qrcode/%d' % int(pk)
            return render(
                request,
                'certificate.html',
                {'spot': spot, 'qrcode_link': link})

    except:
        return render(
            request,
            'certificate.html',
            {'spot': None,
             'qrcode_link': 'holder.js/200x200/text:qrcode not avaliable'})


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


def prepare_vcard(spot):

    dane = "BEGIN:VCARD\r\n"
    dane += "VERSION:3.0\r\n"
    dane += "N:;%s\r\n" % spot.name
    dane += "item1.ADR;type=HOME;type=pref:;;%s %s;%s;;;%s\r\n" % (
        spot.address_street,
        spot.address_number,
        spot.address_city,
        spot.address_country)
    dane += "EMAIL;INTERNET;PREF:%s\r\n" % spot.email if spot.email else ""
    dane += "TEL;WORK;VOICE;PREF:%s\r\n" % spot.phone_number if spot.phone_number else ""
    dane += "URL;WORK;PREF:%s\r\n" % spot.www if spot.www else ""
    dane += "X-SOCIALPROFILE;type=facebook:%s\r\n"  % spot.facebook if spot.facebook else ""
    dane += "END:VCARD\r\n"

    return dane


def download_vcard(request, pk):
    # moze fajnie by zrobic oddzielna funkce do robieni vcardki z zalaczaniem obrazka
    spot = Spot.objects.get(pk=pk)
    dane = prepare_vcard(spot) #.encode('utf-8-sig')  # base64.b64encode()

    response = HttpResponse(dane, content_type="text/x-vcard")
    # response['Content-Transfer-Encoding'] = 'base64'
    response['Content-Disposition'] = 'filename=%s vcard from dogspot.vcf' % spot.name

    return response


def qrencode_vcard(request, pk):

    spot = Spot.objects.get(pk=pk)
    dane = prepare_vcard(spot)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=3,
        border=4,
    )

    qr.add_data(dane)
    qr.make(fit=True)

    img = qr.make_image()

    response = HttpResponse(content_type="image/png")
    img.save(response, "png")
    response['Content-Disposition'] = 'filename=%s qrcode from dogspot.png' % spot.name
    return response





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
