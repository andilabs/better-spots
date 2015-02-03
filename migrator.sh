instance_name=$1
rm -rf accounts/migrations
rm -rf core/migrations
rm -rf www/migrations

python manage.py schemamigration accounts --initial
python manage.py schemamigration core --initial
python manage.py schemamigration www --initial

python manage.py syncdb


python manage.py migrate accounts
python manage.py migrate core
python manage.py migrate www

python manage.py migrate easy_thumbnails
python manage.py migrate rest_framework.authtoken
python manage.py migrate django_extensions

python manage.py create_andi
cp -r data/"$instance_name"/initial_img/. media/img
python manage.py loaddata data/"$instance_name"/spots.json
python manage.py create_slugs
python manage.py collectstatic

