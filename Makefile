install:
	@echo 'download latest docker image'

build:
	@echo 'build local dockerfile'
	docker build -t info_service:0.0.0 .

run: kill
	@echo 'run dockerfile'
	docker run --rm --name info_service -p 5000:5000 info_service:0.0.0

kill:
	@echo 'kill service if running'
	docker kill info_service || true

debug: build kill run
	@echo: 'Build and run local service'
	docker exec -it info_service sh

test: build kill run
	@echo 'run tests'
	docker exec -it info_service python -m unittest

release:
	@echo 'Release new version'
	@echo 'Update changelog'
	@echo 'Release on Github'
	@echo 'Release on Dockerhub'

clear-docker:
	@echo 'clear all docker images'
	sh scripts/clear_docker.sh