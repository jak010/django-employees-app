

build-db:
	sudo docker-compose -f ./deployment/docker-compose.yml up -d

build-db-with-log:
	sudo docker-compose -f ./deployment/docker-compose.yml up


build-develop:
	python manage.py runserver 0.0.0.0:8000 --settings=config.settings.develop