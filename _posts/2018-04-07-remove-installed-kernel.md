---
layout: post
title: "Linux: Remove Installed Kernel"
tag: Linux
toc: true
---

This article introduces how to remove the installed kernels.

<!--more-->

Sometime, I'll compile the Linux kernel and install it in my laptop. I try to remove the kernel image and config file from directory ```/boot``` when I don't need the kernel anymore. Then, I find those kernel comes back again later. The following steps are used to remove the kernel completely:

```
chenwx@chenwx ~ $ dpkg --get-selections | grep linux-image
linux-image-4.0.1-alex				install
linux-image-4.0.1-alex-dbg			install
linux-image-4.1.0-alex				install
linux-image-4.1.0-alex-dbg			install
linux-image-4.1.4-alex				install
linux-image-4.1.4-alex-dbg			install
linux-image-4.1.5-alex				install
linux-image-4.1.5-alex-dbg			install
linux-image-4.15.0-13-generic			install
linux-image-4.2.0-alex				install
linux-image-4.2.0-alex-dbg			install
linux-image-4.2.2-alex				install
linux-image-4.2.2-alex-dbg			install
linux-image-4.3.0-alex				install
linux-image-4.3.0-alex-dbg			install
linux-image-4.4.0-15-generic			deinstall
linux-image-4.4.0-47-generic			deinstall
linux-image-extra-4.15.0-13-generic		install
linux-image-extra-4.4.0-15-generic		deinstall
linux-image-extra-4.4.0-47-generic		deinstall

chenwx@chenwx ~ $ sudo apt-get remove linux-image-4.0.1-alex linux-image-4.0.1-alex-dbg linux-image-4.1.0-alex linux-image-4.1.0-alex-dbg linux-image-4.1.4-alex linux-image-4.1.4-alex-dbg linux-image-4.1.5-alex linux-image-4.1.5-alex-dbg linux-image-4.2.0-alex linux-image-4.2.0-alex-dbg linux-image-4.2.2-alex linux-image-4.2.2-alex-dbg linux-image-4.3.0-alex linux-image-4.3.0-alex-dbg 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages will be REMOVED:
  linux-image-4.0.1-alex linux-image-4.0.1-alex-dbg linux-image-4.1.0-alex linux-image-4.1.0-alex-dbg linux-image-4.1.4-alex
  linux-image-4.1.4-alex-dbg linux-image-4.1.5-alex linux-image-4.1.5-alex-dbg linux-image-4.2.0-alex linux-image-4.2.0-alex-dbg
  linux-image-4.2.2-alex linux-image-4.2.2-alex-dbg linux-image-4.3.0-alex linux-image-4.3.0-alex-dbg
0 upgraded, 0 newly installed, 14 to remove and 0 not upgraded.
After this operation, 15.7 GB disk space will be freed.
Do you want to continue? [Y/n] Y
(Reading database ... 527178 files and directories currently installed.)
Removing linux-image-4.0.1-alex (4.0.1-alex-5) ...
update-initramfs: Deleting /boot/initrd.img-4.0.1-alex
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-4.15.0-13-generic
Found initrd image: /boot/initrd.img-4.15.0-13-generic
Found memtest86+ image: /boot/memtest86+.elf
Found memtest86+ image: /boot/memtest86+.bin
Found Windows 10 (loader) on /dev/sdb1
done
Removing linux-image-4.0.1-alex-dbg (4.0.1-alex-5) ...
Removing linux-image-4.1.0-alex (1) ...
update-initramfs: Deleting /boot/initrd.img-4.1.0-alex
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-4.15.0-13-generic
Found initrd image: /boot/initrd.img-4.15.0-13-generic
Found memtest86+ image: /boot/memtest86+.elf
Found memtest86+ image: /boot/memtest86+.bin
Found Windows 10 (loader) on /dev/sdb1
done
Removing linux-image-4.1.0-alex-dbg (1) ...
Removing linux-image-4.1.4-alex (1) ...
update-initramfs: Deleting /boot/initrd.img-4.1.4-alex
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-4.15.0-13-generic
Found initrd image: /boot/initrd.img-4.15.0-13-generic
Found memtest86+ image: /boot/memtest86+.elf
Found memtest86+ image: /boot/memtest86+.bin
Found Windows 10 (loader) on /dev/sdb1
done
Removing linux-image-4.1.4-alex-dbg (1) ...
Removing linux-image-4.1.5-alex (1) ...
update-initramfs: Deleting /boot/initrd.img-4.1.5-alex
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-4.15.0-13-generic
Found initrd image: /boot/initrd.img-4.15.0-13-generic
Found memtest86+ image: /boot/memtest86+.elf
Found memtest86+ image: /boot/memtest86+.bin
Found Windows 10 (loader) on /dev/sdb1
done
Removing linux-image-4.1.5-alex-dbg (1) ...
Removing linux-image-4.2.0-alex (1) ...
update-initramfs: Deleting /boot/initrd.img-4.2.0-alex
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-4.15.0-13-generic
Found initrd image: /boot/initrd.img-4.15.0-13-generic
Found memtest86+ image: /boot/memtest86+.elf
Found memtest86+ image: /boot/memtest86+.bin
Found Windows 10 (loader) on /dev/sdb1
done
Removing linux-image-4.2.0-alex-dbg (1) ...
Removing linux-image-4.2.2-alex (1) ...
update-initramfs: Deleting /boot/initrd.img-4.2.2-alex
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-4.15.0-13-generic
Found initrd image: /boot/initrd.img-4.15.0-13-generic
Found memtest86+ image: /boot/memtest86+.elf
Found memtest86+ image: /boot/memtest86+.bin
Found Windows 10 (loader) on /dev/sdb1
done
Removing linux-image-4.2.2-alex-dbg (1) ...
Removing linux-image-4.3.0-alex (1) ...
update-initramfs: Deleting /boot/initrd.img-4.3.0-alex
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-4.15.0-13-generic
Found initrd image: /boot/initrd.img-4.15.0-13-generic
Found memtest86+ image: /boot/memtest86+.elf
Found memtest86+ image: /boot/memtest86+.bin
Found Windows 10 (loader) on /dev/sdb1
done
Removing linux-image-4.3.0-alex-dbg (1) ...

chenwx@chenwx ~/work/blog $ dpkg --get-selections | grep linux-image
linux-image-4.0.1-alex				deinstall
linux-image-4.1.0-alex				deinstall
linux-image-4.1.4-alex				deinstall
linux-image-4.1.5-alex				deinstall
linux-image-4.15.0-13-generic			install
linux-image-4.2.0-alex				deinstall
linux-image-4.2.2-alex				deinstall
linux-image-4.3.0-alex				deinstall
linux-image-4.4.0-15-generic			deinstall
linux-image-4.4.0-47-generic			deinstall
linux-image-extra-4.15.0-13-generic		install
linux-image-extra-4.4.0-15-generic		deinstall
linux-image-extra-4.4.0-47-generic		deinstall
```

# References

* [删除多余的内核](https://www.cnblogs.com/llwang/p/4095658.html)

