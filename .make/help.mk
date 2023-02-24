.DEFAULT_GOAL := help

help::
	@egrep -h '\s##\s' $(MAKEFILE_LIST) \
		| awk -F':.*?## | \\| ' '{printf "\033[36m%-18s \033[37m %-35s \033[35m%s \n", $$1, $$2, $$3}'