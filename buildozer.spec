[app]
title = Samrat Empire
package.name = samratapp
package.domain = org.shyam
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.1.0,pillow
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.api = 31
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
