---
layout: post
title: "Das U-Boot: Universal Boot Loader"
tag: RTOS
toc: true
---

This article introduces the universal boot loader **Das U-Boot**.

<!--more-->

# Overview

**Das U-Boot** (or just **U-Boot** for short) is an open source, primary boot loader used in embedded devices to package the instructions to boot the device's operating system kernel. It is available for a number of computer architectures, including 68k, ARM, AVR32, Blackfin, MicroBlaze, MIPS, Nios, SuperH, PPC and x86.

Das U-Boot is both a first-stage and second-stage bootloader. It is loaded by the system's ROM or BIOS from a supported boot device. These vary by platform; typical examples include SD cards, SATA, NOR flash (e.g. EEPROMs, using SPI or I²C), and NAND flash. If there are size constraints, Das U-Boot may be split into stages: the platform would load a small SPL (Secondary Program Loader), and the SPL would do initial hardware configuration and load the rest of Das U-Boot.[1][2][3] Regardless of whether the SPL is used, Das U-Boot performs both first-stage (e.g., configuring memory controllers and SDRAM) and second-stage booting (performing multiple steps to load a modern operating system from a variety of devices that must be configured, presenting a menu for users to interact with and control the boot process, etc.).

## U-Boot History

* **1999-10-22**

  fadsrom - Dan Malek => **PPCBoot rev. 1.1**

* **1999-12-18**

  8xxrom-0.3.0 - Magnus Damm, Raphael Bossek => **PPCBoot rev. 1.2**

* **2000-07-07**

  Wolfgang Denk => **PPCBoot rev. 1.3**

* **2000-07-19**

  Wolfgang Denk => **PPCBoot-0.4.1**, which is the first public version of PPCBoot. Siemens PSE, Vienna: Development of a Bluetooth LAN Access Point with a MPC850 Processor that needed to be able to boot over Ethernet => first commercial sponsor

* **2000-08-08**

  **PPCBoot rev. 1.4** = **PPCBoot-0.4.2** (only PPC, only MPC8xx, 4 boards)

* **2000-10-01**

  added network support => **PPCBoot-0.4.4**

* **2000-10-01**

  Stefan Roese: add support for IBM PPC401/403/405GP processors => **PPCBoot-0.5.1**

* **2000-11-16**

  Murray Jensen: add support for MPC8260 => **PPCBoot-0.6.2**

* **2000-11-20**

  Rob Taylor: add support for MPC8240 => **PPCBoot-0.6.3**

* **End 2000**

  **PPCBoot-0.7.1** (MPC8xx, MPC8240, MPC8260, PPC401/403/405GP; 27 boards)

* **End 2001**

  **PPCBoot-1.1.3** (MPC8xx, MPC8240, MPC8260, 7xx, 74xx, IBM 4xx, 63 boards)

* **Mar 2002**

  SYSGO: split ARMBoot project, separate (incompatible) source tree

* **Jul 2002**

  begin merging with ARMBoot tree

* **Nov 2002**

  **PPCBoot-2.0.0** (last release of PPCBoot. PPC: 8xx, 824x, 826x, 7xx, 74xx, 4xx; ARM: StrongARM, ARM7, ARM9, XScale; > 106 boards). Start **U-Boot** project: **PPCBoot-2.0.0** = **U-Boot-0.1.0**. x86 support

* **Dec 2002**

  **U-Boot-0.2.0** release

* **Mar 2003**

  MIPS32 support

* **Apr 2003**

  **U-Boot-0.3.0** release. MIPS64 support

* **Jun 2003**

  **U-Boot-0.4.0** release

* **Oct 2003**

  **U-Boot-1.0.0** released. Altera NIOS-32 support

* **Dec 2003**

  Coldfire support

* **Apr 2004**

  Microblaze support

* **2004-05-31**

  **U-Boot-1.1.2** release. PPC: 5xx, 5xxx, 8xx, 824x, 826x, 85xx, 7xx, 74xx, 4xx; ARM: StrongARM, ARM720T, ARM92xT, S3C44B0, AT91RM9200, XScale; x86: SC520; m68k: Coldfire; MIPS32: 4Kc, Au1x00; MIPS64: 5Kc; NIOS32; Microblaze; more than 216 boards in public tree; many more not submitted back several board manufacturers use U-Boot as default firmware on some or all of their boards.

* **Jan 2007**

  **U-Boot-1.2.0** release

* **Nov 2007**

  **U-Boot-1.3.0** release

* **Jan 2007**

  **U-Boot-1.2.0** release

* **Oct 2008**

  v2008.10 release

  Starting with the release in October 2008, the names of the releases were changed from numerical release numbers without deeper meaning into a time stamp based numbering. Regular releases are identified by names consisting of the calendar year and month of the release date. Additional fields (if present) indicate release candidates or bug fix releases in "stable" maintenance trees.

* **Jan 2009**

  v2009.01 release

* **Mar 2009**

  v2009.03 release

# U-Boot Source Code

## Git Repository

Browse U-Boot source code [online](http://git.denx.de/u-boot.git/) or clone it to local:

```
chenwx@chenwx ~ $ git clone git://git.denx.de/u-boot.git
chenwx@chenwx ~ $ cd u-boot
chenwx@chenwx ~/u-boot $ ls
Kbuild       MAKEALL   arch    config.mk  drivers   include  scripts
Kconfig      Makefile  board   configs    dts       lib      snapshot.commit
Licenses     README    cmd     disk       examples  net      test
MAINTAINERS  api       common  doc        fs        post     tools
```

## Directory Structure

Refer to ~/u-boot/README for description of directory:

```
/arch			Architecture specific files
  /arc			Files generic to ARC architecture
  /arm			Files generic to ARM architecture
  /avr32		Files generic to AVR32 architecture
  /blackfin		Files generic to Analog Devices Blackfin architecture
  /m68k			Files generic to m68k architecture
  /microblaze		Files generic to microblaze architecture
  /mips			Files generic to MIPS architecture
  /nds32		Files generic to NDS32 architecture
  /nios2		Files generic to Altera NIOS2 architecture
  /openrisc		Files generic to OpenRISC architecture
  /powerpc		Files generic to PowerPC architecture
  /sandbox		Files generic to HW-independent "sandbox"
  /sh			Files generic to SH architecture
  /sparc		Files generic to SPARC architecture
  /x86			Files generic to x86 architecture
/api			Machine/arch independent API for external apps
/board			Board dependent files
/cmd			U-Boot commands functions
/common			Misc architecture independent functions
/configs		Board default configuration files
/disk			Code for disk drive partition handling
/doc			Documentation (don't expect too much)
/drivers		Commonly used device drivers
/dts			Contains Makefile for building internal U-Boot fdt.
/examples		Example code for standalone applications, etc.
/fs			Filesystem code (cramfs, ext2, jffs2, etc.)
/include		Header Files
/lib			Library routines generic to all architectures
/Licenses		Various license files
/net			Networking code
/post			Power On Self Test
/scripts		Various build scripts and Makefiles
/test			Various unit test files
/tools			Tools to build S-Record or U-Boot images, etc.
```

## Build U-Boot

```
chenwx@chenwx ~ $ cd u-boot
chenwx@chenwx ~/u-boot $ ls -l configs/
-rw-rw-r-- 1 chenwx chenwx  697 Jun 22 07:02 10m50_defconfig
-rw-rw-r-- 1 chenwx chenwx  733 Jun 22 07:02 3c120_defconfig
-rw-rw-r-- 1 chenwx chenwx  487 Jun 22 07:02 A10-OLinuXino-Lime_defconfig
-rw-rw-r-- 1 chenwx chenwx  466 Jun 22 07:02 A10s-OLinuXino-M_defconfig
-rw-rw-r-- 1 chenwx chenwx  599 Jun 22 07:02 A13-OLinuXinoM_defconfig
-rw-rw-r-- 1 chenwx chenwx  877 Jun 22 07:02 A13-OLinuXino_defconfig
-rw-rw-r-- 1 chenwx chenwx  559 Jun 22 07:02 A20-OLinuXino-Lime2_defconfig
-rw-rw-r-- 1 chenwx chenwx  462 Jun 22 07:02 A20-OLinuXino-Lime_defconfig
-rw-rw-r-- 1 chenwx chenwx  538 Jun 22 07:02 A20-OLinuXino_MICRO_defconfig
-rw-rw-r-- 1 chenwx chenwx  634 Jun 22 07:02 A20-Olimex-SOM-EVB_defconfig
-rw-rw-r-- 1 chenwx chenwx  619 Jun 22 07:02 Ainol_AW1_defconfig
-rw-rw-r-- 1 chenwx chenwx  687 Jun 22 07:02 Ampe_A76_defconfig
...

chenwx@chenwx ~/u-boot $ mkdir ../u-boot-build
chenwx@chenwx ~/u-boot $ make O=../u-boot-build distclean
chenwx@chenwx ~/u-boot $ make O=../u-boot-build canyonlands_config
chenwx@chenwx ~/u-boot $ make O=../u-boot-build all
```

# U-Boot Commands

Note that U-Boot is highly configurable, so not all of these commands may be available in the configuration of U-Boot installed on your hardware, or additional commands may exist. You can use the ```help``` command to print a list of all available commands for your configuration.

For most commands, you do not need to type in the full command name; instead it is sufficient to type a few characters. For instance, ```help``` can be abbreviated as ```h```.

* The behaviour of some commands depends on the configuration of U-Boot and on the definition of some variables in your U-Boot environment.
* Almost all U-Boot commands expect numbers to be entered in hexadecimal input format. (Exception: for historical reasons, the ```sleep``` command takes its argument in decimal input format.)
* Be careful not to use edit keys besides *Backspace*, as hidden characters in things like environment variables can be very difficult to find.

Refer to [DENX U-Boot and Linux Guide (DULG)](http://www.denx.de/wiki/DULG/Manual) and [U-Boot Command Line Interface](http://www.denx.de/wiki/view/DULG/UBootCommandLineInterface) for more details about U-Boot commands.

```
=> help help
help - print online help

Usage:
help [command ...]
    - show help information (for 'command')
'help' prints online help for the monitor commands.

Without arguments, it prints a short usage message for all commands.

To get detailed help information for specific commands you can type
'help' with one or more command names as arguments.
=>
```

# Port U-Boot to a New Platform

Refer to **~/u-boot/README**:

If the system board that you have is not listed, then you will need to port U-Boot to your hardware platform. To do this, follow these
steps:

1. Create a new directory to hold your board specific code. Add any files you need. In your board directory, you will need at least the **Makefile** and a **\<board\>.c**.
2. Create a new configuration file **include/configs/\<board\>.h** for your board.
3. If you're porting U-Boot to a new CPU, then also create a new directory to hold your CPU specific code. Add any files you need.
4. Run **make \<board\>_defconfig** with your new name.
5. Type **make**, and you should get a working **u-boot.srec** file to be installed on your target system.
6. Debug and solve any problems that might arise. Of course, this last step is much harder than it sounds.

# References

* [Das U-Boot Official Website](http://www.denx.de/wiki/U-Boot/)
* [Das U-Boot Git Repository](http://git.denx.de/u-boot.git/)
* [Das U-Boot FTP Server](ftp://ftp.denx.de/pub/u-boot/)
* [The U-Boot Archives](https://lists.denx.de/pipermail/u-boot/)
* [DENX U-Boot and Linux Guide (DULG)](http://www.denx.de/wiki/DULG/Manual)
* [Das U-Boot Wikipedia](https://en.wikipedia.org/wiki/Das_U-Boot)
* [Comparison of Boot Loaders](https://en.wikipedia.org/wiki/Comparison_of_boot_loaders)
* [BareBox (formerly known as U-Boot-V2)](http://www.barebox.org/)
