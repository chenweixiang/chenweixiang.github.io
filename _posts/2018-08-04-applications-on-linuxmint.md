---
layout: post
title: "Applications on LinuxMint"
tag: Tools
toc: true
---

This article introduces the applications I used on LinuxMint system.

<!--more-->

# Applications

## Desktop Environment

* Cinnamon (Recommended)
* MATE (Second Choice)

## Chinese Input Methods

* 搜狗输入法 for Linux
* Google PinYin

## Web Browsers

* Firefox / FreeGate
* Chrome / FreeGate

## Editor

* [Gedit](https://wiki.gnome.org/Apps/Gedit)
* [Atom](https://atom.io/)

* [LibreOffice](http://www.libreoffice.org/)
* [WPS Office](https://www.wps.com/linux)

```
$ sudo apt install wps-office
```

* Microsoft Office Online, access via outlook.com
* Google Docs

## Email Clients

* Mutt, fetchmail, procmail, msmtp

## Comparison

* [Beyond Compare](http://www.scootersoftware.com/)
* [Meld](http://meldmerge.org/)

## IDE (Integrated Development Environment)

* [Source Insight](http://www.sourceinsight.com/)

# Usage of LinuxMint

## Change User Directory

Update items in configure file ```~/.config/user-dirs.dirs``` to specify directory you want to use, for instance:

```
chenwx@chenwx ~ $ cat ~/.config/user-dirs.dirs
# This file is written by xdg-user-dirs-update
# If you want to change or add directories, just edit the line you're
# interested in. All local changes will be retained on the next run
# Format is XDG_xxx_DIR="$HOME/yyy", where yyy is a shell-escaped
# homedir-relative path, or XDG_xxx_DIR="/yyy", where /yyy is an
# absolute path. No other format is supported.
#
XDG_DESKTOP_DIR="$HOME/Desktop"
XDG_DOWNLOAD_DIR="$HOME/Downloads"
XDG_TEMPLATES_DIR="$HOME/Templates"
XDG_PUBLICSHARE_DIR="$HOME/Public"
XDG_DOCUMENTS_DIR="$HOME/Documents"
XDG_MUSIC_DIR="$HOME/Music"
XDG_PICTURES_DIR="$HOME/Pictures"
XDG_VIDEOS_DIR="$HOME/Videos"
```

# References

* <a href="{{ site.base-url }}/2016/06/05/tool-list.html">Tool List</a>
