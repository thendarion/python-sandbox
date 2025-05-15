.PHONY: all palindrome install test preprocess-test-results

all: palindrome

palindrome:
	$(MAKE) -C palindrome

install:
	$(MAKE) -C palindrome install

test:
	$(MAKE) -C palindrome test

preprocess-test-results:
	$(MAKE) -C palindrome preprocess-test-results
