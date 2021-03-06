default:
	make build
	make run

run:
	docker network create api-backend || true
	docker-compose up

build:
	docker-compose build

enter:
	docker-compose exec web bash

test:
	docker-compose exec web bash -c "python manage.py test"

production:
	docker-compose -f docker-compose-production.yml build
	docker-compose -f docker-compose-production.yml up

down:
	docker-compose down