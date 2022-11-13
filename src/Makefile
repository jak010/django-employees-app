PYTHON=../venv/bin/python3

#  local에서 실행할 때
run.local:
	$(PYTHON) manage.py runserver 0.0.0.0:8000 --settings=config.settings.develop

# Test Application

run.test.employees:
	$(PYTHON) manage.py test employees.tests