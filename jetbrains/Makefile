include .make/help.mk

clean:: ## Clean all gradle modules
	./gradlew clean

compile:: ## Build all gradle modules
	./gradlew assemble

build:: ## Build the plugin
	./gradlew buildPlugin

generate:: ## Generate other themes
	python3 .make/replace-colors.py

release::  ## Release a new version
	./gradlew patchPluginXml buildPlugin patchChangelog