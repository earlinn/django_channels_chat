startapp:
	cd src; python3 manage.py startapp <name>

run:
	cd src; python3 manage.py runserver

uvicorn:
	cd src; uvicorn config.asgi:application --reload

makemig:
	cd src; python3 manage.py makemigrations

migrate:
	cd src; python3 manage.py migrate

superuser:
	cd src; python3 manage.py createsuperuser --username admin --email test@test.com -v 3

superuser-empty:
	cd src; python3 manage.py createsuperuser

shell:
	cd src; python3 manage.py shell

celery-worker:
	cd src; python3 -m celery -A config.celery.app worker -l info

redis-server:
	sudo docker run --name redis-server -d -p 6379:6379 redis:latest

redis-server-start:
	sudo docker start redis-server

redis-server-stop:
	sudo docker stop redis-server

redis-server-exec:
	sudo docker exec -it redis-server redis-cli
