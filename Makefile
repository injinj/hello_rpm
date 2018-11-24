build_dir ?= .
bind      := $(build_dir)/bin

.PHONY: everything
everything: all

-include .copr/Makefile

.PHONY: dist_bins
dist_bins: $(bind) $(bind)/hello_world

.PHONY: dist_rpm
dist_rpm: srpm
	( cd rpmbuild && rpmbuild --define "-topdir `pwd`" -ba SPECS/hello_rpm.spec )

$(bind):
	@mkdir -p $(bind)

$(bind)/hello_world: src/hello_world.c
	$(CC) -ggdb -o $@ $<

clean:
	rm -r -f $(bind)

.PHONY: all
all: $(bind) $(bind)/hello_world
