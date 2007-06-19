NAME=redhat-rpm-config
VERSION=$(shell awk '/Version:/ { print $$2 }' $(NAME).spec)

CVSROOT = $(shell cat CVS/Root 2>/dev/null || :)

CVSTAG = REDHAT_RPM_CONFIG_$(subst .,_,$(VERSION))

all:

tag-archive:
	git-tag -a $(CVSTAG)

create-archive:
	git-archive --format=tar --prefix=redhat-rpm-config-$(VERSION)/ HEAD | bzip2 -9v > redhat-rpm-config-$(VERSION).tar.bz2
	@echo "The final archive is in $(NAME)-$(VERSION).tar.bz2"

archive: tag-archive create-archive
dist: create-archive
