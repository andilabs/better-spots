Up and running
==============

All the secret variables (db passwords, access tokens, etc.) are stored in encrypted file secrets_vars.yml


In main directory you should create file `.vault_pass.txt` containing password needed for decryption.

To get decrypted values:

    `ansible-vault decrypt secrets_vars.yml --vault-password-file .vault_pass.txt`

Modify it (e.g add new variables) and encrypt it back (before pushing to repo):

    `ansible-vault encrypt secrets_vars.yml --vault-password-file .vault_pass.txt`

Then just vagrant up !

after vagrant ssh:

    `manage.py runserver runserver 0:8000`

    access from web browser: `http://192.168.33.13:8000/`
