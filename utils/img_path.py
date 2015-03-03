#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import uuid

def get_image_path(instance=None, filename=None):
    return os.path.join('img', uuid.uuid4().hex)