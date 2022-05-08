install:
	poetry install

gendiff:
	poetry run gendiff

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest tests/test_gendiff.py

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

check:
	make lint
	make test

build:
	make check
	poetry build