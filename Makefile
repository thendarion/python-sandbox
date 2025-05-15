MODULES := palindrome

BASE_TARGETS := install test preprocess
INSTALL_TARGETS := $(MODULES:%=%-install)
TEST_TARGETS := $(MODULES:%=%-test)
PREPROCESS_TARGETS := $(MODULES:%=%-preprocess)

.PHONY: build $(BASE_TARGETS) $(INSTALL_TARGETS) $(TEST_TARGETS) $(PREPROCESS_TARGETS)

build: $(BASE_TARGETS)

install: $(INSTALL_TARGETS)
test: $(TEST_TARGETS)
preprocess: $(PREPROCESS_TARGETS)

$(INSTALL_TARGETS): %-install:
	$(MAKE) -C $* install

$(TEST_TARGETS): %-test:
	$(MAKE) -C $* test

$(PREPROCESS_TARGETS): %-preprocess:
	$(MAKE) -C $* preprocess-test-results
