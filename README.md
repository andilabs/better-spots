Up and running
---------------

What is needed to be installed on your system:
==============================================

* install [vagrant](https://www.vagrantup.com/downloads.html)
* install [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
* install [pip](https://pip.pypa.io/en/stable/installing/) if you don't have it already
* required version of `pip install ansible>=2.3.1.0`


All the secret variables (db passwords, access tokens, etc.) are stored in encrypted file secrets_vars.yml


In main directory you should create file `.vault_pass.txt` containing password needed for decryption.

To get decrypted values:

    `ansible-vault decrypt secrets_vars.yml --vault-password-file .vault_pass.txt`

Modify it (e.g add new variables) and encrypt it back (before pushing to repo):

    `ansible-vault encrypt secrets_vars.yml --vault-password-file .vault_pass.txt`

Then just vagrant up !

after vagrant ssh:

    `manage.py runserver runserver 0:9000`

    access from web browser: `http://127.0.0.1:9000/`
