[app]
title = CalculatorApp
package.name = calculator
package.domain = org.hosseinh

source.dir = .
source.include_exts = py,kv,png,jpg,atlas

version = 1.0

requirements = python3,kivy,hostpython3

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25c
android.accept_sdk_license = True

android.permissions =

[buildozer]
log_level = 2
warn_on_root = 0