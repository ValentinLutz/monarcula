include .make/help.mk

clean:: ## Clean all gradle modules
	./gradlew clean

compile:: ## Build all gradle modules
	./gradlew assemble

build:: ## Build the plugin
	./gradlew buildPlugin

changelog-show:: ## Show the latest changelog
	./gradlew getChangelog

changelog-update:: ## Patch the latest changelog
	./gradlew patchChangelog

generate:: ## Generate other themes
	python3 .make/replace-colors.py

release:: build changelog-update ## Release a new version