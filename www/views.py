import json
import cStringIO as StringIO
import ho.pisa as pisa
from cgi import escape

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import Context
from django.template.loader import get_template
from django.template.response import TemplateResponse
from django.views.generic import FormView, CreateView

from core.models import Spot, SPOT_TYPE
from utils.qrcodes import make_qrcode
from accounts.forms import UserCreationForm
from .forms import ContactForm


def main(request):
    if request.method == 'GET':
        response = TemplateResponse(request, 'mission.html', {})
        return response


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
        response = TemplateResponse(request, 'mobile.html', {
            'DEBUG_PLEASE': settings.PROJECT_ROOT_PATH})
        return response


def favourites(request):
    if request.method == 'GET':
        response = TemplateResponse(request, 'favourites.html', {'my_debug': settings.PROJECT_ROOT_PATH})
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
        return render_to_pdf(
            'mytemplatePDF.html',
            {
                'BASE_HOST': settings.INSTANCE_DOMAIN,
                'MEDIA_ROOT': settings.MEDIA_ROOT,
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


def qrencode_link(request, pk, size=3, for_view='spot-detail'):

    dane = "http://%s%s" % (
        settings.INSTANCE_DOMAIN,
        reverse(for_view, kwargs={'pk': pk}))
    img = make_qrcode(dane, box_size=size)
    response = HttpResponse(content_type="image/png")
    img.save(response, "png")
    return response


def qrencode_vcard(request, pk, size=3):

    spot = Spot.objects.get(pk=pk)
    img = make_qrcode(spot.prepare_vcard, box_size=size)
    response = HttpResponse(content_type="image/png")
    img.save(response, "png")
    return response


def download_vcard(request, pk):

    spot = Spot.objects.get(pk=pk)
    response = HttpResponse(spot.prepare_vcard, content_type="text/x-vcard")
    response['Content-Disposition'] = (
        'filename=vcard_from_%s.vcf' % settings.SPOT_PROJECT_NAME)
    return response


def spots(request):
    spots_list = Spot.objects.all()
    paginator = Paginator(spots_list, 6)
    page = request.GET.get('page')
    try:
        spots = paginator.page(page)
    except PageNotAnInteger:
        spots = paginator.page(1)
    except EmptyPage:
        spots = paginator.page(paginator.num_pages)
    return render(request, 'spot_list.html', {'spots': spots})


def spot(request, pk, slug):
    spot = get_object_or_404(Spot, pk=pk)
    return render(request, 'spot_detail.html', {'spot': spot})


class SpotUserCreate(CreateView):
    template_name = 'spotuser_form.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.WARNING,
            'Your account was created, but it is not active.' +
            ' We sent you e-mail with confrimation link')

        return super(SpotUserCreate, self).form_valid(form)


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        content = form.cleaned_data.get('message')
        to = str(form.cleaned_data.get('mail'))
        msg = EmailMessage(
            "contact form",
            content,
            settings.EMAIL_HOST_USER,
            [to, ]
        )
        msg.send()

        messages.add_message(
            self.request,
            messages.SUCCESS, 'Your message was sucessfully sent!'
            )
        return super(ContactView, self).form_valid(form)
