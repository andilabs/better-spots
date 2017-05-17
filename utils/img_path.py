#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import uuid


def get_image_path(filename):
    try:
        extension = filename.split('.')[-1]
    except IndexError:
        extension = ''
    return os.path.join(
        'img',
        '{}.{}'.format(uuid.uuid4().hex, extension)
    )
