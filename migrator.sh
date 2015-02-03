instance_name=$1
rm -rf accounts/migrations
rm -rf core/migrations
rm -rf www/migrations

python manage.py schemamigration accounts --initial --settings=mbf.settings.andi
python manage.py schemamigration core --initial --settings=mbf.settings.andi
python manage.py schemamigration www --initial --settings=mbf.settings.andi

python manage.py syncdb --settings=mbf.settings.andi


python manage.py migrate accounts --settings=mbf.settings.andi
python manage.py migrate core --settings=mbf.settings.andi
python manage.py migrate www --settings=mbf.settings.andi

python manage.py migrate easy_thumbnails --settings=mbf.settings.andi
python manage.py migrate rest_framework.authtoken --settings=mbf.settings.andi
python manage.py migrate django_extensions --settings=mbf.settings.andi

python manage.py create_andi --settings=mbf.settings.andi
cp -r data/"$instance_name"/initial_img/. media/img
python manage.py loaddata data/"$instance_name"/spots.json --settings=mbf.settings.andi
python manage.py create_slugs --settings=mbf.settings.andi
python manage.py runserver --settings=mbf.settings.andi
