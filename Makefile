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

# Trick with --abort-on-container-exit brilliantly suggested by ChatGPT:

# By default, the docker-compose command returns with an exit code of 0 even
# if one of the services failed. To propagate the failure exit code
# from the container to the docker-compose command and then to the make
# command, you can add the --abort-on-container-exit flag to the docker-compose
# command. This flag will make the docker-compose command exit with a non-zero
# code if any of the containers failed.

# With this modification, if any of the containers fail during the integration test,
# the docker-compose command will exit with a non-zero code, causing the make command
# to also exit with a non-zero code and indicating that the integration-test target failed.
integration-test:
	docker compose \
         -f docker-compose.yml \
         -f docker-compose.integration-test.yml \
         up --build --abort-on-container-exit
