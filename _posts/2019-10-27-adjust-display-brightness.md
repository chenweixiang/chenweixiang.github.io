---
layout: post
title: "Adjust Display Brightness"
tag: Linux
toc: true
---

This article introduces how to adjust display brightness on LinuxMint.

<!--more-->

# Adjust display brightness on LinuxMint

Adjust display brightness on LinuxMint:

```
root@chenwx:~# ll /sys/class/backlight/
lrwxrwxrwx  1 root root 0 Oct 27 15:10 acpi_video0 -> ../../devices/pci0000:00/0000:00:02.0/backlight/acpi_video0/
lrwxrwxrwx  1 root root 0 Oct 27 15:10 intel_backlight -> ../../devices/pci0000:00/0000:00:02.0/drm/card0/card0-LVDS-1/intel_backlight/

root@chenwx:~# ll /sys/class/backlight/intel_backlight/
-r--r--r-- 1 root root 4096 Oct 27 15:14 actual_brightness
-rw-r--r-- 1 root root 4096 Oct 27 15:14 bl_power
-rw-r--r-- 1 root root 4096 Oct 27 15:15 brightness
lrwxrwxrwx 1 root root    0 Oct 27 15:14 device -> ../../card0-LVDS-1/
 -r--r--r-- 1 root root 4096 Oct 27 15:14 max_brightness
drwxr-xr-x 2 root root    0 Oct 27 15:14 power/
lrwxrwxrwx 1 root root    0 Oct 27 15:14 subsystem -> ../../../../../../../class/backlight/
-r--r--r-- 1 root root 4096 Oct 27 15:14 type
-rw-r--r-- 1 root root 4096 Oct 27 15:14 uevent

root@chenwx:~# cat /sys/class/backlight/intel_backlight/max_brightness 
12056655

root@chenwx:~# cat /sys/class/backlight/intel_backlight/brightness
6304856

root@chenwx:~# echo 12056655 > /sys/class/backlight/intel_backlight/brightness
root@chenwx:~# cat /sys/class/backlight/intel_backlight/brightness
12056655
```

# Solution

首选项 > 电源管理 > 亮度 > 屏幕亮度 > 100%

# References

None.

