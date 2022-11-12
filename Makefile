

#  local에서 실행할 때
run.local:
	python manage.py runserver 0.0.0.0:8000 --settings=config.settings.develop


# docker 설정
run.dev.docker:
	cd ./.devcontainer && sudo docker-compose up -d

# Test Application

run.test.employees:
	python manage.py test employees.tests