# -*- coding: utf-8 -*-
import json
import uuid
import base64
import quopri
import vobject
import qrcode
from datetime import datetime, timedelta

from django.core.urlresolvers import reverse
from django.http import QueryDict
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
# from django.contrib.sites.models import Site
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
from django.http import Http404

from django.contrib.gis.measure import D 
from django.contrib.gis.geos import (Point, fromstr, fromfile, GEOSGeometry, MultiPoint, MultiPolygon, Polygon)

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
from rest_framework import generics

from .models import (
    Spot, DogspotUser, Dog, EmailVerification,
    Raiting, Opinion, OpinionUsefulnessRating, OtoFoto, SPOT_TYPE)

from .serializers import (
    SpotDetailSerializer,
    SpotWithDistanceSerializer, SpotListSerializer, RaitingSerializer,
    OpinionSerializer, OpinionUsefulnessRatingSerializer,
    DogspotUserSerializer, OtoFotoSerializer)

from .authentication import ExpiringTokenAuthentication

from .forms import (
    ContactForm,
    UserCreationForm)


import cStringIO as StringIO
import ho.pisa as pisa
from django.template.loader import get_template
from django.template import Context
from cgi import escape


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(
        StringIO.StringIO(html.encode('utf-8')),
        result,
        encoding='UTF-8')

    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')

    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


def pdf_sticker(request, pk):

    if Spot.objects.get(pk=pk).friendly_rate > 4.5:
        # current_site = Site.objects.get_current()

        return render_to_pdf(
            'mytemplatePDF.html',
            {
                'BASE_HOST': settings.DOGSPOT_DOMAIN,
                'MEDIA_ROOT': settings.MEDIA_ROOT,
                # 'BASE_HOST': current_site.domain,
                'pagesize': 'A6',
                'spot': Spot.objects.get(pk=pk),
            }
        )
    else:
        raise Http404


def ajax_search(request):

    query = request.GET.get('q', '')

    result = [
        {
            'name': s.name,
            'category': SPOT_TYPE[s.spot_type-1][1],
            'url': '/spots/%s' % str(s.id)
        }
        for s in Spot.objects.filter(
            name__icontains=query).order_by('spot_type')
    ]

    return HttpResponse(
        json.dumps(result, ensure_ascii=False),
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

    user_location = fromstr("POINT(%s %s)" % (lng, lat))

    desired_radius = {'m':radius}

    nearby_spots = Spot.objects.filter(mpoint__distance_lte=(user_location, D(**desired_radius))).distance(user_location).order_by('distance')[:limit]

    serializer = SpotWithDistanceSerializer(nearby_spots, many=True)
    return JSONResponse(serializer.data)


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
                    "Account was activated! Log in and enjoy dogspot!")
                return redirect('login')

            else:
                email_verification = EmailVerification(
                    verification_key=base64.urlsafe_b64encode(uuid.uuid4().bytes)[:21],
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


def map(request):
    if request.method == 'GET':
        response = TemplateResponse(request, 'map.html', {})
        return response


def map_two(request):
    if request.method == 'GET':
        response = TemplateResponse(request, 'map_two.html', {})
        return response

def mobile(request):
    if request.method == 'GET':
        response = TemplateResponse(request, 'mobile.html', {})
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

            link = '/qrcode/%d/2' % int(pk)
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
            if user.mail_verified:
                login(request, user)
                messages.add_message(
                    request,
                    messages.SUCCESS, 'You were sucessfully logged in!')
                return redirect('glowna')
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
    success_url = '/'

    def form_valid(self, form):
        content = form.cleaned_data.get('message')
        to = str(form.cleaned_data.get('mail'))
        msg = EmailMessage("contact form", content, settings.EMAIL_HOST_USER, [to, ])
        msg.send()

        messages.add_message(
            self.request,
            messages.SUCCESS, 'Your message was sucessfully sent!'
            )
        return super(ContactView, self).form_valid(form)


class DogspotUserCreate(CreateView):
    template_name = 'demo/dogspotuser_form.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.WARNING,
            'Your account was created, but it is not active.' +
            ' We sent you e-mail with confrimation link'
            )
        return super(DogspotUserCreate, self).form_valid(form)


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

    spot = Spot.objects.get(pk=pk)
    dane = prepare_vcard(spot)

    response = HttpResponse(dane, content_type="text/x-vcard")
    response['Content-Disposition'] = 'filename=%s via dogspot.vcf' % spot.name

    return response


def make_qrcode(data, version=1, box_size=3, border=4):

    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=int(box_size),
        border=border,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()

    return img


def qrencode_vcard(request, pk, size=3):

    spot = Spot.objects.get(pk=pk)
    dane = prepare_vcard(spot)

    img = make_qrcode(dane, box_size=size)

    response = HttpResponse(content_type="image/png")
    img.save(response, "png")
    # below line because of encoding issues can cause strange 500's errors - handle encoding to be url/file name safe!
    #response['Content-Disposition'] = 'filename=%s by dogspot.png' % spot.name
    return response


def qrencode_link(request, pk, size=3):

    dane = "http://%s%s" %(settings.DOGSPOT_DOMAIN, reverse('spot-detail', kwargs={'pk': pk}))
    img = make_qrcode(dane, box_size=size)

    response = HttpResponse(content_type="image/png")
    img.save(response, "png")
    # response['Content-Disposition'] = 'filename=%s by dogspot.png' % spot.name
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
        user = authenticate(email=email, password=password)
        time_now = datetime.now()

        if user and user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                if not created and token.created < time_now - timedelta(
                        hours=settings.TOKEN_EXPIRES_AFTER):
                    # for comparing dates USE_TZ = False in settings
                    token.delete()
                    token = Token.objects.create(user=user)
                    token.created = datetime.now()
                    token.save()

                return HttpResponse(
                    json.dumps({'token': token.key}),
                    content_type="application/json; charset=UTF-8")

        else:
            return HttpResponse('Unauthorized', status=401)


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
