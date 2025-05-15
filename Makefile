MODULES := palindrome

BASE_TARGETS := install test preprocess
INSTALL_TARGETS := $(MODULES:%=%-install)
TEST_TARGETS := $(MODULES:%=%-test)

.PHONY: build $(BASE_TARGETS) $(INSTALL_TARGETS) $(TEST_TARGETS) 

build: $(BASE_TARGETS)

install: $(INSTALL_TARGETS)
test: install $(TEST_TARGETS)

$(INSTALL_TARGETS): %-install:
	$(MAKE) -C $* install

$(TEST_TARGETS): %-test:
	$(MAKE) -C $* test

