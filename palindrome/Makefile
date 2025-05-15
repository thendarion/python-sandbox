.PHONY: build install test run-tests preprocess-test-results

build: install test

.installed:
	python -m pip install --upgrade pip
	pip install poetry
	poetry install
	touch .installed

install: .installed

run-tests:
	poetry run invoke test-all

preprocess-test-results:
	sed -e '0,/testsuite/s//testsuites/' -e '$$s/testsuite/testsuites/' -i robot-report.xml 

test: install run-tests preprocess-test-results
