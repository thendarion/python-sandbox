.PHONY: all palindrome

all: palindrome

palindrome:
	$(MAKE) -C palindrome

install:
	$(MAKE) -C palindrome install

test:
	$(MAKE) -C palindrome test