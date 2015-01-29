#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.

    After switch to Django VERSION 1.7 which offer JsonResponse NO MORE NEEDED
    https://docs.djangoproject.com/en/1.7/ref/request-response/#jsonresponse-objects
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
