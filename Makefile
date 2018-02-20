install:
	@echo 'Download latest docker image'

build:
	@echo 'Build docker image from Dockerfile'
	docker build -q -t info_service:latest .

run: kill
	@echo 'Run docker image as a container'
	docker run --rm -d --name info_service -p 5000:5000 info_service:latest

kill:
	@echo 'Kill docker container if running'
	docker kill info_service || true

debug:
	@echo 'Build and run local container'
	docker exec -it info_service sh

tests: build kill run
	@echo 'Run tests'
	docker exec -it info_service python -m unittest

release:
	@echo 'Release new version'
	@echo 'Update changelog'
	@echo 'Release on Github'
	@echo 'Release on Dockerhub'
	docker login
	docker tag market-information-service VikashKothary/market-information-service:0.0.0
	docker push VikashKothary/market-information-service:0.0.0

clear-docker:
	@echo 'Clear all docker images'
	sh scripts/clear_docker.sh > /dev/null