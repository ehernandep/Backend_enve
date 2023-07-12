build:
	docker-compose up --build -d
up:
	docker-compose up -d
down:
	docker-compose down
logs:
	docker-compose logs
migrate:
	docker-compose exec api python3 manage.py migrate --noinput
makemigrations:
	docker-compose exec api python3 manage.py makemigrations

superuser:
	docker-compose exec api python3 manage.py createsuperuser	

down-v:
	docker-compose down -v

shell:
	docker-compose exec api python3 manage.py shell