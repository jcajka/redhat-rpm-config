NAME=redhat-rpm-config
VERSION=$(shell awk '/Version:/ { print $$2 }' $(NAME).spec)

CVSROOT = $(shell cat CVS/Root 2>/dev/null || :)

CVSTAG = REDHAT_RPM_CONFIG_$(subst .,_,$(VERSION))

all:

tag-archive:
	@cvs -Q tag -F $(CVSTAG)

create-archive:
	@rm -rf /tmp/$(NAME)
	@cd /tmp ; cvs -Q -d $(CVSROOT) export -r$(CVSTAG) $(NAME) || echo "Um... export aborted."
	@mv /tmp/$(NAME) /tmp/$(NAME)-$(VERSION)
	@cd /tmp ; tar -czSpf $(NAME)-$(VERSION).tar.gz $(NAME)-$(VERSION)
	@rm -rf /tmp/$(NAME)-$(VERSION)
	@cp /tmp/$(NAME)-$(VERSION).tar.gz .
	@rm -f /tmp/$(NAME)-$(VERSION).tar.gz
	@echo ""
	@echo "The final archive is in $(NAME)-$(VERSION).tar.gz"

archive: tag-archive create-archive
