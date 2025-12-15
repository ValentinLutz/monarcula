group = "net.bounceme.monkee"
version = "2.0.0"

plugins {
    id("java")
    id("org.jetbrains.intellij.platform") version "2.10.5"
    id("org.jetbrains.changelog") version "2.5.0"
}

repositories {
    mavenCentral()
    intellijPlatform {
        defaultRepositories()
    }
}

java {
    sourceCompatibility = JavaVersion.VERSION_21
    targetCompatibility = JavaVersion.VERSION_21
}

// See https://github.com/JetBrains/intellij-platform-gradle-plugin
dependencies {
    intellijPlatform {
        intellijIdea("2025.3")
        pluginVerifier()
    }
}

// See https://github.com/JetBrains/gradle-changelog-plugin
changelog {
    version = project.version.toString()
}

tasks {
    patchPluginXml {
        changeNotes = provider {
            changelog.renderItem(
                changelog.getUnreleased().withHeader(false).withEmptySections(false),
                org.jetbrains.changelog.Changelog.OutputType.HTML
            )
        }
    }
}