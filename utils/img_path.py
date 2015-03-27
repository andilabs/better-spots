#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import uuid

def get_image_path():
    return os.path.join('img', uuid.uuid4().hex)