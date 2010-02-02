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
	@git tag -a $(CVSTAG) -m "$(NAME)-$(VERSION) release"

create-archive:
	@git archive --format=tar --prefix=$(NAME)-$(VERSION)/ HEAD | tar xf -
	@git log > $(NAME)-$(VERSION)/ChangeLog
	@tar cjf $(NAME)-$(VERSION).tar.bz2 $(NAME)-$(VERSION)
	@rm -rf $(NAME)-$(VERSION)
	@echo "Created $(NAME)-$(VERSION).tar.bz2"

archive: tag-archive create-archive
