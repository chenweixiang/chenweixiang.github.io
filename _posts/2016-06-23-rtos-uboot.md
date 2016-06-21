---
layout: post
title: "Das U-Boot: the Universal Boot Loader"
tag: RTOS
toc: true
---

This article introduces the universal boot loader **Das U-Boot**.

<!--more-->

# Overview

**Das U-Boot** (or just **U-Boot** for short) is an open source, primary boot loader used in embedded devices to package the instructions to boot the device's operating system kernel. It is available for a number of computer architectures, including 68k, ARM, AVR32, Blackfin, MicroBlaze, MIPS, Nios, SuperH, PPC and x86.

Das U-Boot is both a first-stage and second-stage bootloader. It is loaded by the system's ROM or BIOS from a supported boot device. These vary by platform; typical examples include SD cards, SATA, NOR flash (e.g. EEPROMs, using SPI or I²C), and NAND flash. If there are size constraints, Das U-Boot may be split into stages: the platform would load a small SPL (Secondary Program Loader), and the SPL would do initial hardware configuration and load the rest of Das U-Boot.[1][2][3] Regardless of whether the SPL is used, Das U-Boot performs both first-stage (e.g., configuring memory controllers and SDRAM) and second-stage booting (performing multiple steps to load a modern operating system from a variety of devices that must be configured, presenting a menu for users to interact with and control the boot process, etc.).

# Build U-Boot

```
chenwx@chenwx ~ $ git clone git://git.denx.de/u-boot.git
chenwx@chenwx ~ $ cd u-boot
chenwx@chenwx ~/u-boot $ mkdir ../u-boot-build
chenwx@chenwx ~/u-boot $ make O=../u-boot-build distclean
chenwx@chenwx ~/u-boot $ make O=../u-boot-build canyonlands_config
chenwx@chenwx ~/u-boot $ make O=../u-boot-build all
```

# Das U-Boot History

| Date | Note |
| :--- | :--- |
| Oct 22, 1999 | fadsrom - Dan Malek => PPCBoot rev. 1.1 |
| Dec 18, 1999 | 8xxrom-0.3.0 - Magnus Damm, Raphael Bossek => PPCBoot rev. 1.2 |
| Jul 07, 2000 | Wolfgang Denk => PPCBoot rev. 1.3 |
| Jul 19, 2000 | Wolfgang Denk => PPCBoot-0.4.1, which is the first public version of PPCBoot |
| | Siemens PSE, Vienna: Development of a Bluetooth LAN Access Point with a MPC850 Processor that needed to be able to boot over Ethernet => first commercial sponsor |
| Aug 08, 2000 | PPCBoot rev. 1.4 = **PPCBoot-0.4.2** (only PPC, only MPC8xx, 4 boards) |
| Oct 01, 2000 | added network support => PPCBoot-0.4.4 |
| Oct 01, 2000 | Stefan Roese: add support for IBM PPC401/403/405GP processors => PPCBoot-0.5.1 |
| Nov 16, 2000 | Murray Jensen: add support for MPC8260 => PPCBoot-0.6.2 |
| Nov 20, 2000 | Rob Taylor: add support for MPC8240 => PPCBoot-0.6.3 |
| End 2000 | PPCBoot-0.7.1 (MPC8xx, MPC8240, MPC8260, PPC401/403/405GP; 27 boards) |
| End 2001 | PPCBoot-1.1.3 (MPC8xx, MPC8240, MPC8260, 7xx, 74xx, IBM 4xx, 63 boards) |
| Mar 2002 | SYSGO: split ARMBoot project, separate (incompatible) source tree |
| Jul 2002 | begin merging with ARMBoot tree |
| Nov 2002 | PPCBoot-2.0.0 (last release of PPCBoot)<br>PPC: 8xx, 824x, 826x, 7xx, 74xx, 4xx;<br>ARM: StrongARM, ARM7, ARM9, XScale;<br>> 106 boards<br>=> Start **U-Boot** project: PPCBoot-2.0.0 = U-Boot-0.1.0 |
| Nov 2002 | x86 support |
| Mar 2003 | MIPS32 |
| Apr 2003 | MIPS64 |
| Oct 2003 | Altera NIOS-32 |
| Dec 2003 | Coldfire |
| Apr 2004 | Microblaze |
| 31 May 2004 | U-Boot-1.1.2<br>PPC: 5xx, 5xxx, 8xx, 824x, 826x, 85xx, 7xx, 74xx, 4xx;<br>ARM: StrongARM, ARM720T, ARM92xT, S3C44B0, AT91RM9200, XScale;<br>x86: SC520;<br>m68k: Coldfire;<br>MIPS32: 4Kc, Au1x00;<br>MIPS64: 5Kc;<br>NIOS32;<br>Microblaze;<br>>216 boards in public tree; many more not submitted back several board manufacturers use U-Boot as default firmware on some or all of their boards |

<p/>

# References

* [Das U-Boot Official Website](http://www.denx.de/wiki/U-Boot/)
* [Das U-Boot Git Repository](http://git.denx.de/u-boot.git/)
* [Das U-Boot FTP Server](ftp://ftp.denx.de/pub/u-boot/)
* [DENX U-Boot and Linux Guide (DULG)](http://www.denx.de/wiki/DULG/Manual)
* [Das U-Boot Wikipedia](https://en.wikipedia.org/wiki/Das_U-Boot)
* [Comparison of Boot Loaders](https://en.wikipedia.org/wiki/Comparison_of_boot_loaders)
* [BareBox (formerly known as U-Boot-V2)](http://www.barebox.org/)
