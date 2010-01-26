NAME=redhat-rpm-config
VERSION=9.1.0

CVSTAG = REDHAT_RPM_CONFIG_$(subst .,_,$(VERSION))

all:

clean:
	rm -f *~ 

install:
	mkdir -p $(DESTDIR)/usr/lib/rpm/redhat
	cp -pr * $(DESTDIR)/usr/lib/rpm/redhat/
	rm -f $(DESTDIR)/usr/lib/rpm/redhat/Makefile

tag-archive:
	git tag -a $(CVSTAG)

create-archive:
	git archive --format=tar --prefix=$(NAME)-$(VERSION)/ HEAD | bzip2 -9v > $(NAME)-$(VERSION).tar.bz2
	@echo "The final archive is in $(NAME)-$(VERSION).tar.bz2"

archive: tag-archive create-archive
dist: create-archive
