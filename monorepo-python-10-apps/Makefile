APP ?= app-01

up:
	docker compose up --build -d

down:
	docker compose down -v

logs:
	docker compose logs -f --tail=200

test:
	docker compose run --rm app-01-backend pytest -q

lint:
	docker compose run --rm app-01-backend ruff check app

format:
	docker compose run --rm app-01-backend black app

migrate:
	@for i in $(shell seq -w 1 10); do docker compose run --rm app-$$i-backend python scripts/migrate.py; done

seed:
	@for i in $(shell seq -w 1 10); do docker compose run --rm app-$$i-backend python scripts/seed.py; done

app:
	docker compose up --build $(APP)-backend $(APP)-frontend reverse-proxy postgres redis

rebuild:
	docker compose build --no-cache
