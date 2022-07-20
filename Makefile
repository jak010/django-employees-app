

rundocker:
	cd ./docker && sudo docker-compose up -d

build-develop:
	python manage.py runserver 0.0.0.0:8000 --settings=config.settings.develop