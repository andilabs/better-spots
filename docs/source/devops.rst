My little DevOps
================

Scripts
^^^^^^^

[pull_migrate_and_restart.sh] - Pull repo, collectstatic, restart apache
----------------------------------------------------------------

.. sourcecode:: bash

	branch_name=$1
	echo "Using branch" + "$branch_name"
	declare -a instances=("dogspot.eu" "momspot.eu" "enabledspot.eu" "veganspot.org")

	for instance in "${instances[@]}"
	do
	   cd "/home/ubuntu/$instance/mbf"
	   git fetch
	   git checkout "$branch_name"
	   git pull --no-edit origin "$branch_name"
	   python manage.py collectstatic --noinput
	   python manage.py migrate
	   sudo apachectl restart
	done



[create_instance.sh] - create new instance
------------------------------------------

.. sourcecode:: bash

	# run with two arguments first is domain, second name for database and dir location, e.g: vagnspot.org veganspot
	instance_name=$1
	base_name=$2
	echo "I gonna create instance for:" $instance_name
	mkdir $instance_name
	mkdir "$instance_name"/logs
	mkdir "$instance_name"/static_assets
	cd "$instance_name"
	git clone git@github.com:andilabs/mbf.git
	cd mbf
	git checkout production
	git pull origin production
	i=`ls -l /etc/apache2/sites-available | grep ".conf" | wc -l`
	i=$((i-2))
	echo $i
	sed "s/INSTANCE_NAME_PLACEHOLDER/$instance_name/g" /etc/apache2/sites-available/xxx-base.conf > /etc/apache2/sites-available/00"$i"-"$instance_name".conf
	ln -s /etc/apache2/sites-available/00"$i"-"$instance_name".conf /etc/apache2/sites-enabled/00"$i"-"$instance_name".conf
	sudo -u postgres bash /home/ubuntu/create_db.sh "$base_name"
	bash migrator.sh "$base_name"
	apachectl restart


[create_db.sh] - create new instance postgres db with all extensions
--------------------------------------------------------------------

.. sourcecode:: bash

	base_name=$1
	psql << EOF
	CREATE USER $base_name WITH PASSWORD $DB_PASSWORD;
	create database $base_name;
	GRANT ALL PRIVILEGES ON DATABASE $base_name to $base_name;
	\connect $base_name
	-- Enable HSTORE
	create extension hstore;
	-- Enable PostGIS (includes raster)
	CREATE EXTENSION postgis;
	-- Enable Topology
	CREATE EXTENSION postgis_topology;
	-- fuzzy matching needed for Tiger
	CREATE EXTENSION fuzzystrmatch;
	-- Enable US Tiger Geocoder
	CREATE EXTENSION postgis_tiger_geocoder;
	EOF


[migrator.sh] - performs all migraitons and loads initial data for new instance
-------------------------------------------------------------------------------

.. sourcecode:: bash

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
	# cp -r data/"$instance_name"/initial_img/. media/img
	python manage.py loaddata data/"$instance_name"/spots.json
	python manage.py create_slugs
	python manage.py collectstatic


Apache
^^^^^^

xxx-base.conf
-------------

.. sourcecode:: bash

	<VirtualHost *:80>

	        ServerName INSTANCE_NAME_PLACEHOLDER
	        ServerAlias www.INSTANCE_NAME_PLACEHOLDER
	        ServerAdmin     andi@INSTANCE_NAME_PLACEHOLDER

	        LogLevel info
	        ErrorLog "/home/ubuntu/INSTANCE_NAME_PLACEHOLDER/logs/INSTANCE_NAME_PLACEHOLDER-error_log"
	        CustomLog "/home/ubuntu/INSTANCE_NAME_PLACEHOLDER/logs/INSTANCE_NAME_PLACEHOLDER-access_log" common

	        DocumentRoot "/home/ubuntu/INSTANCE_NAME_PLACEHOLDER"

	        Alias /static/ /home/ubuntu/INSTANCE_NAME_PLACEHOLDER/static_assets/

	        <Directory "/home/ubuntu/INSTANCE_NAME_PLACEHOLDER/static">
	                Order deny,allow
	                Allow from all
	        </Directory>


	        WSGIDaemonProcess INSTANCE_NAME_PLACEHOLDER python-path=/home/ubuntu/INSTANCE_NAME_PLACEHOLDER/mbf:/home/ubuntu/.virtualenvs/dogspot/lib/python2.7/site-packages
	        WSGIProcessGroup INSTANCE_NAME_PLACEHOLDER
	        WSGIScriptAlias / /home/ubuntu/INSTANCE_NAME_PLACEHOLDER/mbf/mbf/wsgi.py
	        WSGIPassAuthorization On

	        <Directory "/home/ubuntu/INSTANCE_NAME_PLACEHOLDER/mbf/mbf">
	                <Files wsgi.py>
	                        Order deny,allow
	                        Allow from all
	                </Files>
	        </Directory>
	</VirtualHost>