"""
WSGI config for mbf project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
#import site

#envpath = '/home/ubuntu/.virtualenvs/dogspot/lib/python2.7/site-packages'

# we add currently directory to path and change to it
#pwd = os.path.dirname(os.path.abspath(__file__))
#os.chdir(pwd)
#sys.path = [pwd] + sys.path

# Append paths
#site.addsitedir(envpath)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mbf.settings.settings")
#sys.path.append('/home/ubuntu/dogspot.eu')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'mbf.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
