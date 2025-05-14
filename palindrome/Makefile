.PHONY: all install test

all: install test

.installed:
	python -m pip install --upgrade pip && \
	pip install poetry && \
	poetry install && \
	touch .installed

install: .installed

test:
	poetry run invoke test-all
