---
layout: post
title: "Applications"
tag: Tools
toc: true
---

This article introduces the applications I used on Windows and LinuxMint system.

<!--more-->

# Upgrade Thinkpad R61i

See [Upgrade Thinkpad R61i](/docs/Upgrade_Thinkpad_R61i.pdf).

# Applications on Windows

## Desktop Environment

* [Windows 10 专业版](/docs/Win10_Compare_Table.pdf)

## Chinese Input Methods

* [搜狗输入法](https://pinyin.sogou.com/)
* Google PinYin

## Web Browsers

* Chrome / FreeGate

## Editor

* [Notepad++](https://notepad-plus-plus.org/)
* [Atom](https://atom.io/)

* [LibreOffice](http://www.libreoffice.org/)
* [WPS Office](https://www.wps.com/linux)

* Microsoft Office Online, access via outlook.com
* Google Docs

## Email Clients

* Windows Outlook

## Comparison

* [Beyond Compare](http://www.scootersoftware.com/)

## IDE (Integrated Development Environment)

* [Source Insight](http://www.sourceinsight.com/)

## Dictionary

* [Lingoes 灵格斯词霸](http://www.lingoes.cn/zh/dictionary/index.html)

## Skype

* Download Skype from [here](https://www.skype.com/en/get-skype/) and see [Usage of Skype](/docs/Usage_of_Skype.pdf)

# Applications on LinuxMint

## Desktop Environment

* LinuxMint Cinnamon Edition (Recommended)
* LinuxMint MATE Edition (Second Choice)

See the following documentations:

* [Install Windows 7 via U Disk](/docs/Install_Windows7_via_U_Disk.pdf)
* [Install Windows 7 and LinuxMint 17](/docs/Install_Windows7_LinuxMint17.pdf)
* [Install LinuxMint via U Disk](/docs/Install_LinuxMint_via_U_Disk.pdf)
* [Install Xubuntu on Windows XP](/docs/Install_Xubuntu_on_Windows_XP.pdf)

## Chinese Input Methods

* [搜狗拼音输入法](https://shurufa.sogou.com/)
* Google PinYin

See [Install SogouPinYin and GooglePinYin on Linux](/docs/Install_SogouPinYin_and_GooglePinYin_on_Linux.pdf).

## Web Browsers

* Firefox / FreeGate
* Chrome / FreeGate

## Editor

* [Gedit](https://wiki.gnome.org/Apps/Gedit)
* [Atom](https://atom.io/)

* [LibreOffice](http://www.libreoffice.org/)

```
sudo add-apt-repository ppa:libreoffice/ppa
sudo apt-get update
sudo apt-get dist-upgrade
```

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

# Tips

## 开启Windows笔记本的虚拟WiFi热点

方法一：使用[WiFi共享精灵](http://www.wifigx.com/)来开启Windows笔记本的虚拟WiFi热点。

方法二：使用[开启Windows笔记本的虚拟WiFi热点](/docs/Open_Windows_Virtual_WiFi_Hotpot.pdf)和[virtual_wifi.bat](https://github.com/chenweixiang/scripts/blob/master/virtual_wifi.bat)来开启Windows笔记本的虚拟WiFi热点。

## 更改启用Bluetooth的设备的设置

参见[更改启用Bluetooth的设备的设置](/docs/Change_Bluetooth_Settings.pdf)。

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
