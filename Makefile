install:
    python -m pip install --upgrade pip
    pip install poetry
	cd palindrome && \
	poetry install

test:
	cd palindrome && \
	poetry run invoke test-all