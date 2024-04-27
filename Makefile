DJANGO = python manage.py

runserver:
	$(DJANGO) runserver

makemigrations:
	$(DJANGO) makemigrations

migrate:
	$(DJANGO) migrate

test:
	$(DJANGO) test

requirements:
	pip freeze > requirements.txt

format:
	black .