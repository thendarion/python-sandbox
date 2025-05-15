.PHONY: build install test preprocess-test-results

build: install test

.installed:
	python -m pip install --upgrade pip
	pip install poetry
	poetry install
	touch .installed

install: .installed

test: install
	poetry run invoke test-all
	sed '0,/testsuite/s//testsuites/' robot-report.xml | tac | sed '0,/testsuite/s//testsuites/' | tac > temp.xml  
	mv temp.xml robot-report.xml
