Better Spots
=============
[![Build Status](https://travis-ci.org/andilabs/better-spots.png?branch=master)](https://travis-ci.org/andilabs/better-spots)


This project aim is to build location oriented store for collecting spots, which are
 dog-, mom-, vegan- or disabled people- friendly.

Using mostly following technologies stack:

    Python 3
    Django
    Django Rest Framework
    Postgres + PostGIS
    

Up and running
===============

What is needed to be installed on your system:
----------------------------------------------

* install [vagrant](https://www.vagrantup.com/downloads.html) tested on v. 1.9.4
* install [Virtual Box](https://www.virtualbox.org/wiki/Downloads) tested on v. 5.0.26
* install [pip](https://pip.pypa.io/en/stable/installing/) if you don't have it already
* required [ansible](http://docs.ansible.com/) version >=2.3.1.0 install via  `pip install ansible>=2.3.1.0`

Secret vars
-----------

All the secret variables (db passwords, access tokens, etc.) are stored in 
encrypted file secrets_vars.yml

In main directory you should create file `.vault_pass.txt` containing 
password needed for decryption.

For demo purpose fill the values in secrets_vars.yml or ask me for right 
content of .vaul_pass.txt:

    db_password: "yourDesiredDBpass"
    email_host_user: "yourEmail@example.com"
    email_host_password: "yourEmailPass"
    django_secret_key: "YourDjangoSecretKeyYourDjangoSecretKeyYourDjangoSe"
    google_map_api_key: "YourGoogleMapsAPIkeyYourGoogleMapsAPIke"
    google_maps_js_key: "YourGoogleMapsJSApiKey"
    mailtrap_user: "YourMailtrapUser"
    mailtrap_password: "YourMailTrapPassword"
    mailtrap_token: "YourMailTrapRestAPIToken"
    recaptcha_public_key: "YourGoogleRecaptchaSiteKey"
    recaptcha_private_key: "YourGoogleRecaptchaSecretKey"

To get decrypted values:

    ansible-vault decrypt secrets_vars.yml --vault-password-file .vault_pass.txt

Modify it (e.g add new variables) and encrypt it back (before pushing to repo):

    ansible-vault encrypt secrets_vars.yml --vault-password-file .vault_pass.txt


Git hook to prevent commiting unencrypted vars (place it in `.git/hooks/pre-commit`:

    if grep -q password secrets_vars.yml; then
      echo "please encrypt the secrets, found raw word password"
      exit 1
    elif grep -q secret secrets_vars.yml; then
      echo "please encrypt the secrets, found raw word secret"
      exit 1
    elif grep -q key secrets_vars.yml; then
      echo "please encrypt the secrets, found raw word key"
      exit 1
    fi

    exit 0

Bootstrap the project
---------------------

Then just `vagrant up` !

after the whole provisioning is done without errors your machine with 
(Linux Ubuntu Xenial 16.04 LTS) is ready and you can `vagrant ssh` and
run django server:

    ./manage.py runserver 0:9000

and access from web browser: 

[http://127.0.0.1:9000/](http://127.0.0.1:9000/)

Project targets
---------------

There are four projects (labels) possible:

- dogspot
- momspot
- enabledspot
- veganspot

you pick using one of labels by setting right settings import inside the 
file `better-spots/better_spots/settings/__init__.py` e.g for 
using dogspot label the content of the file should be:

    from better_spots.settings.labels.dogspot.dev import *

    

API
===

Use swagger to browse API:
--------------------------

[http://127.0.0.1:9000/api/schema/](http://127.0.0.1:9000/api/schema/)



TESTS
======

To run these few units:
----------------------

    ./manage.py test --settings=better_spots.unittesting

