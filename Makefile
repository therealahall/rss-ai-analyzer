.PHONY: test lint format

test:
    docker-compose run --rm python pytest

lint:
    docker-compose run --rm python flake8 src tests

format:
    docker-compose run --rm python black src tests
