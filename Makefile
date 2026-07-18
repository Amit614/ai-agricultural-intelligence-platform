bootstrap:
	pip install -r requirements-dev.txt

test:
	pytest

lint:
	ruff check .

format:
	black .
