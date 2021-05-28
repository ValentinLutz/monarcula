import org.jetbrains.changelog.closure

plugins {
    id("org.jetbrains.intellij") version "0.7.3"
    id("org.jetbrains.changelog") version "1.1.2"
    java
}

group = "net.bounceme.monkee"
version = "1.0.1"

repositories {
    mavenCentral()
}

// See https://github.com/JetBrains/gradle-intellij-plugin/
intellij {
    version = "2021.1"
}
configure<JavaPluginConvention> {
    sourceCompatibility = JavaVersion.VERSION_11
}

tasks {
    patchPluginXml {
        changeNotes(closure { changelog.getUnreleased().toHTML() })
    }
}
