group = "net.bounceme.monkee"
version = "1.1.1"

plugins {
    id("java")
    id("org.jetbrains.intellij") version "1.3.1"
    id("org.jetbrains.changelog") version "1.3.1"
}

repositories {
    mavenCentral()
}

java {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}

// See https://github.com/JetBrains/gradle-intellij-plugin/
intellij {
    version.set("2021.2")
    updateSinceUntilBuild.set(false)
}

// See https://github.com/JetBrains/gradle-changelog-plugin
changelog {
    version.set(project.version.toString())
}

tasks {
    patchPluginXml {
        changeNotes.set(changelog.getUnreleased().toHTML())
    }
}