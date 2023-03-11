.PHONY: start
start:
	docker compose up --build

COMPOSE_RUN = docker compose run --build --rm

TEST_CMD = python -m pytest .

app-bash:
	$(COMPOSE_RUN) app bash
app-build-test:
	docker build --target test -t app:test app
app-test: app-build-test
	docker run app:test $(TEST_CMD)

data-bash:
	$(COMPOSE_RUN) data bash
data-build-test:
	docker build --target test -t data:test data
data-test: data-build-test
	docker run data:test $(TEST_CMD)

.PHONY: test
test: app-test data-test
