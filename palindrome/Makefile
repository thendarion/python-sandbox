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

preprocess-test-results:
    sed '0,/testsuite/s//testsuites/' robot-report.xml | tac \
	 | sed '0,/testsuite/s//testsuites/' | tac > output.xml  \
	 && mv output.xml robot-report.xml