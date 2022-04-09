include .make/help.mk

clean:: ## Clean all gradle modules
	./gradlew clean

compile:: ## Build all gradle modules
	./gradlew assemble

build:: ## Build the plugin
	./gradlew patchPluginXml buildPlugin patchChangelog

generate:: ## Generate other themes
	python3 .make/replace-colors.py

release:: build changelog-update ## Release a new version