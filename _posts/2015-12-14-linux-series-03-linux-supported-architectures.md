---
layout: post
title: "Linux: Linux Supported Architectures"
tag: Linux
toc: true
---

This article introduces Linux supported architectures, and commands to check hardware informations.

<!--more-->

# Linux Supported Architectures

According to directory ```arch/``` in Linux kernel source tree, Linux kernel supports following architectures:

* **```alpha/```**

    The [Alpha processor](https://en.wikipedia.org/wiki/DEC_Alpha) was developed by Digital Equipment Corporation (DEC). The  DEC was later bought by Compaq, which then merged with HP. Alpha always had a reputation for excellent performance and could run many different operating systems. Alpha is of great historical importance to Linux as the [first non-PC port incorporated into Linus's tree](http://www.oreilly.com/catalog/opensources/book/linus.html), as well as the first 64-bit port. [This website](http://www.alphalinux.org/wiki/index.php/Main_Page) is about the port of GNU/Linux to the Alpha architecture.

	* [Alpha: The History in Facts and Comments](http://alasir.com/articles/alpha_history/index.html)
	<p/>

* **```arc/```**

* **```arm/```**, **```arm64/```**

    The [ARM processor](http://www.arm.com/) is the most popular embedded processor, powering 80-90% of the cell phone market and most battery powered handheld devices.

	* [The ARM instruction set architecture](http://www.arm.com/products/processors/)
	* [List of ARM processors](http://www.elinux.org/ARM_Processor)
	* [The ARM Linux Project](http://www.arm.linux.org.uk/)
	<p/>

* **```avr32/```**

* **```blackfin/```**

* **```c6x/```**

* **```cris/```**

* **```frv/```**

* **```h8300/```**

* **```hexagon/```**

* **```ia64/```**

    The **Itanium** was a failed attempt to create a 64-bit successor to the 32-bit x86 processors, a role that went to AMD's x86-64 design instead. In 1994, **Intel** partnered with **Hewlett Packard (HP)** to produce a successor to both **x86** and HP's **PA-RISC**, with a new instruction set ```ia64``` fundamentally different from both. To support software written for the older processors, the designers included a complete implementation of each, because the new chip was already so big and complex that including *two* entire previous processors wasn't a significant increase to either. The result was a late, slow, inefficient chip that was difficult to manufacture, more expensive than available alternatives, difficult to write efficient compilers for, quickly nicknamed ***Itanic*** and essentially ignored by the market.

    The history of Itanium through 2003 was extensively detailed [here](http://www.catb.org/~esr/halloween/halloween9.html#itanium). A more recent obituary for the chip is zdnet's [Itanium: A cautionary tale](http://www.zdnet.com/article/itanium-a-cautionary-tale/).

* **```m32r/```**

* **```m68k/```**

* **```metag/```**

* **```microblaze/```**

* **```mips/```**

    **MIPS** (originally an acronym for **Microprocessor without Interlocked Pipeline Stages**) is a reduced instruction set computer (RISC) instruction set architecture (ISA) developed by **MIPS Technologies** (formerly **MIPS Computer Systems, Inc.**). The early MIPS architectures were 32-bit, with 64-bit versions added later. Multiple revisions of the MIPS instruction set exist, including **MIPS I** (introduced in 1985 with the R2000), **MIPS II** (introduced in 1990 with the R6000), **MIPS III** (introduced in 1992 in the R4000), **MIPS IV** (introduced in 1994 with R8000. It is a superset of MIPS III and is compatible with all existing versions of MIPS), **MIPS V**, **MIPS32** (introduced in 1999 based on MIPS II with some additional features from MIPS III, MIPS IV, and MIPS V), and **MIPS64** (introduced in 1999 based on MIPS V). The current revisions are **MIPS32** (for 32-bit implementations) and **MIPS64** (for 64-bit implementations).

    **MIPS** is probably the main competitor to **ARM**. One advantage of MIPS is its availability as a FPGA program, allowing easy prototyping of custom hardware.

* **```mn10300/```**

* **```nios2/```**

* **```openrisc/```**

* **```parisc/```**

    The **PA-RISC** is an instruction set architecture (ISA) developed by **Hewlett-Packard (HP)**. As the name implies, it is a reduced instruction set computer (RISC) architecture, where the **PA** stands for **Precision Architecture**. The design is also referred to as **HP/PA** for **Hewlett Packard Precision Architecture**. It was scheduled to be discontinued in favor of the **Itanium**, but the failure of ia64 led to a restart of PA-RISC development.

	* [PA-RISC on Wikipedia](https://en.wikipedia.org/wiki/PA-RISC)
	* [PA-RISC Linux Project History](https://parisc.wiki.kernel.org/index.php/PA-RISC_Linux_Project_History)
	* [Introduction to Linux on PA-RISC](https://parisc.wiki.kernel.org/index.php/Main_Page)
	<p/>

* **```powerpc/```**

    **PowerPC** (an acronym for **Performance Optimization With Enhanced RISC – Performance Computing**, sometimes abbreviated as **PPC**) is a RISC instruction set architecture created by the 1991 **Apple–IBM–Motorola alliance**, known as **AIM**. Apple switched to x86-64 in 2005 and Motorola spun off its processor division as Freescale. But IBM is still strongly behind PowerPC, and the various users of PowerPC formed a consortium to promote and develop it.

	* [PowerPC on Wikipedia](https://en.wikipedia.org/wiki/PowerPC)
	* [List of PowerPC Processors](https://en.wikipedia.org/wiki/List_of_PowerPC_processors)
	* [The Linux Kernel on iSeries](https://www.kernel.org/doc/ols/2001/iseries.pdf) (OLS 2001)
	* [PowerPC 64-bit Kernel Internals](https://www.kernel.org/doc/ols/2001/ppc64.pdf) (OLS 2001)
	<p/>
* **```s390/```**

* **```score/```**

* **```sh/```**

* **```sparc/```**

* **```tile/```**

* **```um/```**

    **User Mode Linux (UML)** is a port of Linux to run as a userspace program. Instead of talking to the hardware, it makes system calls to the C library. Instead of using a memory management unit it makes clever use of mmap.

	* [User-Mode Linux on Wikipedia](https://en.wikipedia.org/wiki/User-mode_Linux)
	* [User-Mode Linux](https://www.kernel.org/doc/ols/2001/uml.pdf) (OLS 2001)
	* [Making Linux Safe for Virtual Machines](https://www.kernel.org/doc/ols/2002/ols2002-pages-107-116.pdf) (OLS 2002)
	* [User Mode Linux HOWTO](http://landley.net/writing/docs/UML.html)
	* [The User-mode Linux Kernel Home Page](http://user-mode-linux.sourceforge.net/)
	<p/>

* **```unicore32/```**

* **```x86/```**

	* [Porting Linux to x86-64](https://www.kernel.org/doc/ols/2001/x86-64.pdf) (OLS 2001)
	<p/>

* **```xtensa/```**

# Commands to show Hardware Info

## General Hardware Information

### inxi

The command ```inxi``` is a 10K line mega bash script that fetches hardware details from multiple different sources and commands on the system, and generates a beautiful looking report that non technical users can read easily.

```
chenwx@chenwx ~ $ inxi -Fx
System:    Host: chenwx Kernel: 4.2.0-19-generic x86_64 (64 bit, gcc: 4.8.2)
           Desktop: Xfce 4.11.8 (Gtk 2.24.23) Distro: Linux Mint 17 Qiana
Machine:   System: LENOVO product: 77322EC version: ThinkPad R61
           Mobo: LENOVO model: 77322EC Bios: LENOVO version: 7LETC9WW (2.29 ) date: 03/18/2011
CPU:       Dual core Intel Core2 Duo CPU T9300 (-MCP-) cache: 6144 KB flags: (lm nx sse sse2 sse3 sse4_1 ssse3 vmx) bmips: 9974.9
           Clock Speeds: 1: 800.00 MHz 2: 2501.00 MHz
Graphics:  Card: Intel Mobile GM965/GL960 Integrated Graphics Controller (primary) bus-ID: 00:02.0
           X.Org: 1.15.1 drivers: intel (unloaded: fbdev,vesa) Resolution: 1280x800@60.0hz
           GLX Renderer: Mesa DRI Intel 965GM GLX Version: 2.1 Mesa 10.1.3 Direct Rendering: Yes
Audio:     Card: Intel 82801H (ICH8 Family) HD Audio Controller driver: snd_hda_intel bus-ID: 00:1b.0
           Sound: Advanced Linux Sound Architecture ver: k4.2.0-19-generic
Network:   Card-1: Qualcomm Atheros AR242x / AR542x Wireless Network Adapter (PCI-Express) driver: ath5k bus-ID: 03:00.0
           IF: wlan0 state: down mac: 00:1f:3a:77:d4:65
           Card-2: Intel 82566MM Gigabit Network Connection driver: e1000e ver: 3.2.5-k port: 1840 bus-ID: 00:19.0
           IF: eth0 state: up speed: 100 Mbps duplex: full mac: 00:1c:25:76:75:eb
Drives:    HDD Total Size: 440.1GB (67.1% used) 1: id: /dev/sda model: CSD_CAZ320S size: 320.1GB temp: 0C
           2: id: /dev/sdb model: Samsung_SSD_840 size: 120.0GB temp: 0C
Partition: ID: / size: 52G used: 39G (78%) fs: ext4
RAID:      No RAID devices detected - /proc/mdstat and md_mod kernel raid module present
Sensors:   System Temperatures: cpu: 52.0C mobo: 36.0C
           Fan Speeds (in rpm): cpu: 0
Info:      Processes: 181 Uptime: 1 day Memory: 1856.2/3879.2MB Runlevel: 2 Gcc sys: 4.8.4 Client: Shell inxi: 1.8.4
```

### hardinfo

The command ```hardinfo``` is a gtk based gui tool that generates reports about various hardware components. But it can also run from the command line only if there is no gui display available.

```
chenwx@chenwx ~ $ sudo apt-get install hardinfo
chenwx@chenwx ~ $ hardinfo &
chenwx@chenwx ~ $ hardinfo -r > ~/hardinfo.txt
```

### lshw

The command ```lshw``` is a small tool to extract detailed information on the hardware configuration of the machine. It extracts the information from different ```/proc``` and ```/sys``` files. Use the following command to show the device information in short format:

```
chenwx@chenwx ~ $ sudo lshw -short
H/W path        Device     Class       Description
==================================================
                           system      77322EC ()
/0                         bus         77322EC
/0/0                       memory      128KiB BIOS
/0/6                       processor   Intel(R) Core(TM)2 Duo CPU     T9300  @ 2.50GHz
/0/6/a                     memory      64KiB L1 cache
/0/6/c                     memory      6MiB L2 cache
/0/b                       memory      64KiB L1 cache
/0/2b                      memory      4GiB System Memory
/0/2b/0                    memory      2GiB SODIMM DDR2 Synchronous 667 MHz (1.5 ns)
/0/2b/1                    memory      2GiB SODIMM DDR2 Synchronous 667 MHz (1.5 ns)
/0/100                     bridge      Mobile PM965/GM965/GL960 Memory Controller Hub
/0/100/2                   display     Mobile GM965/GL960 Integrated Graphics Controller (primary)
/0/100/2.1                 display     Mobile GM965/GL960 Integrated Graphics Controller (secondary)
/0/100/19       eth0       network     82566MM Gigabit Network Connection
/0/100/1a                  bus         82801H (ICH8 Family) USB UHCI Controller #4
/0/100/1a.1                bus         82801H (ICH8 Family) USB UHCI Controller #5
/0/100/1a.7                bus         82801H (ICH8 Family) USB2 EHCI Controller #2
/0/100/1b                  multimedia  82801H (ICH8 Family) HD Audio Controller
/0/100/1c                  bridge      82801H (ICH8 Family) PCI Express Port 1
/0/100/1c.1                bridge      82801H (ICH8 Family) PCI Express Port 2
/0/100/1c.1/0   wlan0      network     AR242x / AR542x Wireless Network Adapter (PCI-Express)
/0/100/1c.2                bridge      82801H (ICH8 Family) PCI Express Port 3
/0/100/1c.3                bridge      82801H (ICH8 Family) PCI Express Port 4
/0/100/1c.4                bridge      82801H (ICH8 Family) PCI Express Port 5
/0/100/1d                  bus         82801H (ICH8 Family) USB UHCI Controller #1
/0/100/1d.1                bus         82801H (ICH8 Family) USB UHCI Controller #2
/0/100/1d.2                bus         82801H (ICH8 Family) USB UHCI Controller #3
/0/100/1d.7                bus         82801H (ICH8 Family) USB2 EHCI Controller #1
/0/100/1e                  bridge      82801 Mobile PCI Bridge
/0/100/1e/0                bridge      RL5c476 II
/0/100/1e/0.1              bus         R5C832 IEEE 1394 Controller
/0/100/1f                  bridge      82801HEM (ICH8M-E) LPC Interface Controller
/0/100/1f.1                storage     82801HM/HEM (ICH8M/ICH8M-E) IDE Controller
/0/100/1f.2                storage     82801HM/HEM (ICH8M/ICH8M-E) SATA Controller [AHCI mode]
/0/100/1f.3                bus         82801H (ICH8 Family) SMBus Controller
/0/1            scsi0      storage     
/0/1/0.0.0      /dev/sda   disk        320GB CSD CAZ320S
/0/1/0.0.0/1               volume      298GiB Windows FAT volume
/0/2            scsi2      storage     
/0/2/0.0.0      /dev/sdb   disk        120GB Samsung SSD 840
/0/2/0.0.0/1    /dev/sdb1  volume      100MiB Windows NTFS volume
/0/2/0.0.0/2    /dev/sdb2  volume      58GiB Windows NTFS volume
/0/2/0.0.0/3    /dev/sdb3  volume      484MiB Windows NTFS volume
/0/2/0.0.0/4    /dev/sdb4  volume      52GiB Extended partition
/0/2/0.0.0/4/5  /dev/sdb5  volume      52GiB Linux filesystem partition
/1                         power       42T4532
```

or, use the following command to show specific class information:

```
chenwx@chenwx ~ $ sudo lshw -C processor
  *-cpu                   
       description: CPU
       product: Intel(R) Core(TM)2 Duo CPU     T9300  @ 2.50GHz
       vendor: Intel Corp.
       physical id: 6
       bus info: cpu@0
       version: Intel(R) Core(TM)2 Duo CPU     T9300  @ 2.50GHz
       slot: None
       size: 2501MHz
       capacity: 2501MHz
       width: 64 bits
       clock: 200MHz
       capabilities: fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx x86-64 constant_tsc arch_perfmon pebs bts rep_good nopl aperfmperf pni dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm sse4_1 lahf_lm ida dtherm tpr_shadow vnmi flexpriority cpufreq
```

It also comes with a GUI frontend called ```lshw-gtk``` that reports the same information in a minimal graphical user interface. You maybe should install the tool first by command:

```
chenwx@chenwx ~ $ sudo apt-get install lshw-gtk
```

Then, run the command to show hardware information in GUI:

```
chenwx@chenwx ~ $ sudo lshw-gtk
```

### dmidecode

The command ```dmidecode``` is different from all other commands. It extracts hardware information by reading data from the SMBOIS data structures (also called DMI tables).

```
# display information about the processor/cpu
$ sudo dmidecode -t processor

# memory/ram information
$ sudo dmidecode -t memory

# bios details
$ sudo dmidecode -t bios
```

### hwinfo

The command ```hwinfo``` is a very handy command line tool that can be used to probe for details about hardware components. It reports information about most hardware units like cpu, hdd controllers, usb controllers, network card, graphics cards, multimedia, printers etc.

```
$ hwinfo --short
cpu:
                       Intel(R) Core(TM)2 Quad CPU    Q8400  @ 2.66GHz, 2000 MHz
                       Intel(R) Core(TM)2 Quad CPU    Q8400  @ 2.66GHz, 2000 MHz
                       Intel(R) Core(TM)2 Quad CPU    Q8400  @ 2.66GHz, 2666 MHz
                       Intel(R) Core(TM)2 Quad CPU    Q8400  @ 2.66GHz, 2666 MHz
keyboard:
  /dev/input/event2    AT Translated Set 2 keyboard
mouse:
  /dev/input/mice      Microsoft Basic Optical Mouse v2.0
graphics card:
                       Intel 965G-1
                       Intel 82G35 Express Integrated Graphics Controller
sound:
                       Intel 82801H (ICH8 Family) HD Audio Controller
storage:
                       Intel 82801H (ICH8 Family) 4 port SATA IDE Controller
                       Intel 82801H (ICH8 Family) 2 port SATA IDE Controller
                       JMicron JMB368 IDE controller
network:
  eth0                 Intel 82566DC Gigabit Network Connection
network interface:
  eth0                 Ethernet network interface
  lo                   Loopback network interface
disk:
  /dev/sda             ST3500418AS
partition:
  /dev/sda1            Partition
  /dev/sda2            Partition
  /dev/sda5            Partition
  /dev/sda6            Partition
  /dev/sda7            Partition
  /dev/sda8            Partition
cdrom:
  /dev/sr0             SONY DVD RW DRU-190A
usb controller:
                       Intel 82801H (ICH8 Family) USB UHCI Controller #4
                       Intel 82801H (ICH8 Family) USB UHCI Controller #5
                       Intel 82801H (ICH8 Family) USB2 EHCI Controller #2
                       Intel 82801H (ICH8 Family) USB UHCI Controller #1
                       Intel 82801H (ICH8 Family) USB UHCI Controller #2
                       Intel 82801H (ICH8 Family) USB UHCI Controller #3
                       Intel 82801H (ICH8 Family) USB2 EHCI Controller #1
bios:
                       BIOS
bridge:
                       Intel 82G35 Express DRAM Controller
                       Intel 82801H (ICH8 Family) PCI Express Port 1
                       Intel 82801H (ICH8 Family) PCI Express Port 2
                       Intel 82801H (ICH8 Family) PCI Express Port 3
                       Intel 82801 PCI Bridge
                       Intel 82801HB/HR (ICH8/R) LPC Interface Controller
hub:
                       Linux 3.11.0-12-generic uhci_hcd UHCI Host Controller
                       Linux 3.11.0-12-generic uhci_hcd UHCI Host Controller
                       Linux 3.11.0-12-generic uhci_hcd UHCI Host Controller
                       Linux 3.11.0-12-generic uhci_hcd UHCI Host Controller
                       Linux 3.11.0-12-generic uhci_hcd UHCI Host Controller
                       Linux 3.11.0-12-generic ehci_hcd EHCI Host Controller
                       Linux 3.11.0-12-generic ehci_hcd EHCI Host Controller
memory:
                       Main Memory
firewire controller:
                       Agere FW323
unknown:
                       FPU
                       DMA controller
                       PIC
                       Timer
                       Keyboard controller
                       Intel 82801H (ICH8 Family) SMBus Controller
                       Serial controller
```

## CPU Information

### lscpu

The command ```lscpu``` displays information on CPU architecture.

```
chenwx@chenwx ~ $ lscpu
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                2
On-line CPU(s) list:   0,1
Thread(s) per core:    1
Core(s) per socket:    2
Socket(s):             1
NUMA node(s):          1
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 23
Stepping:              6
CPU MHz:               2501.000
BogoMIPS:              4987.45
Virtualization:        VT-x
L1d cache:             32K
L1i cache:             32K
L2 cache:              6144K
NUMA node0 CPU(s):     0,1
```

### nproc

The command ```nproc``` just prints out the number of processing units available. Note that the number of processing units might not always be the same as number of cores.

```
chenwx@chenwx ~ $ nproc
2
```

### cpuid

The command ```cpuid``` fetches CPUID information about Intel and AMD x86 processors.

```
chenwx@chenwx ~ $ sudo apt-get install cpuid

chenwx@chenwx ~ $ cpuid
CPU 0:
   vendor_id = "GenuineIntel"
   version information (1/eax):
      processor type  = primary processor (0)
      family          = Intel Pentium Pro/II/III/Celeron/Core/Core 2/Atom, AMD Athlon/Duron, Cyrix M2, VIA C3 (6)
      model           = 0x7 (7)
      stepping id     = 0x6 (6)
      extended family = 0x0 (0)
      extended model  = 0x1 (1)
      (simple synth)  = Intel Core 2 Duo (Wolfdale C0/M0) / Mobile Core 2 Duo (Penryn C0/M0) / Core 2 Extreme QX9000 (Yorkfield C0) / Pentium Dual-Core
Processor E5000 (Wolfdale M0) / Xeon Processor 3100 (Wolfdale C0) / Xeon Processor 3300 (Yorkfield C0) / Xeon Processor 5200 (Wolfdale C0) / Xeon Proces
sor 5400 (Harpertown C0), 45nm
   miscellaneous (1/ebx):
      process local APIC physical ID = 0x0 (0)
      cpu count                      = 0x2 (2)
      CLFLUSH line size              = 0x8 (8)
      brand index                    = 0x0 (0)
   brand id = 0x00 (0): unknown
   feature information (1/edx):
      x87 FPU on chip                        = true
      virtual-8086 mode enhancement          = true
      debugging extensions                   = true
      page size extensions                   = true
...
```

## PCI Buses Information

### lspci

The command ```lspci``` is a utility for displaying information about PCI buses in the system and devices connected to them. Use following command to show the general information about PCI bus:

```
chenwx@chenwx ~ $ lspci    
00:00.0 Host bridge: Intel Corporation Mobile PM965/GM965/GL960 Memory Controller Hub (rev 0c)
00:02.0 VGA compatible controller: Intel Corporation Mobile GM965/GL960 Integrated Graphics Controller (primary) (rev 0c)
00:02.1 Display controller: Intel Corporation Mobile GM965/GL960 Integrated Graphics Controller (secondary) (rev 0c)
00:19.0 Ethernet controller: Intel Corporation 82566MM Gigabit Network Connection (rev 03)
00:1a.0 USB controller: Intel Corporation 82801H (ICH8 Family) USB UHCI Controller #4 (rev 03)
00:1a.1 USB controller: Intel Corporation 82801H (ICH8 Family) USB UHCI Controller #5 (rev 03)
00:1a.7 USB controller: Intel Corporation 82801H (ICH8 Family) USB2 EHCI Controller #2 (rev 03)
00:1b.0 Audio device: Intel Corporation 82801H (ICH8 Family) HD Audio Controller (rev 03)
00:1c.0 PCI bridge: Intel Corporation 82801H (ICH8 Family) PCI Express Port 1 (rev 03)
00:1c.1 PCI bridge: Intel Corporation 82801H (ICH8 Family) PCI Express Port 2 (rev 03)
00:1c.2 PCI bridge: Intel Corporation 82801H (ICH8 Family) PCI Express Port 3 (rev 03)
00:1c.3 PCI bridge: Intel Corporation 82801H (ICH8 Family) PCI Express Port 4 (rev 03)
00:1c.4 PCI bridge: Intel Corporation 82801H (ICH8 Family) PCI Express Port 5 (rev 03)
00:1d.0 USB controller: Intel Corporation 82801H (ICH8 Family) USB UHCI Controller #1 (rev 03)
00:1d.1 USB controller: Intel Corporation 82801H (ICH8 Family) USB UHCI Controller #2 (rev 03)
00:1d.2 USB controller: Intel Corporation 82801H (ICH8 Family) USB UHCI Controller #3 (rev 03)
00:1d.7 USB controller: Intel Corporation 82801H (ICH8 Family) USB2 EHCI Controller #1 (rev 03)
00:1e.0 PCI bridge: Intel Corporation 82801 Mobile PCI Bridge (rev f3)
00:1f.0 ISA bridge: Intel Corporation 82801HEM (ICH8M-E) LPC Interface Controller (rev 03)
00:1f.1 IDE interface: Intel Corporation 82801HM/HEM (ICH8M/ICH8M-E) IDE Controller (rev 03)
00:1f.2 SATA controller: Intel Corporation 82801HM/HEM (ICH8M/ICH8M-E) SATA Controller [AHCI mode] (rev 03)
00:1f.3 SMBus: Intel Corporation 82801H (ICH8 Family) SMBus Controller (rev 03)
03:00.0 Ethernet controller: Qualcomm Atheros AR242x / AR542x Wireless Network Adapter (PCI-Express) (rev 01)
15:00.0 CardBus bridge: Ricoh Co Ltd RL5c476 II (rev ba)
15:00.1 FireWire (IEEE 1394): Ricoh Co Ltd R5C832 IEEE 1394 Controller (rev 04)
```

Use option ```-k``` to show kernel drivers handling each device and also kernel modules capable of handling it. Then, use command ```modinfo``` to show details of the device driver:

```
chenwx@chenwx ~ $ lspci -k
15:00.1 FireWire (IEEE 1394): Ricoh Co Ltd R5C832 IEEE 1394 Controller (rev 04)
	Subsystem: Lenovo ThinkPad R61
	Kernel driver in use: firewire_ohci
...

chenwx@chenwx ~ $ modinfo firewire_ohci
filename:       /lib/modules/4.2.0-19-generic/kernel/drivers/firewire/firewire-ohci.ko
alias:          ohci1394
license:        GPL
description:    Driver for PCI OHCI IEEE1394 controllers
author:         Kristian Hoegsberg <krh@bitplanet.net>
srcversion:     21D3B3B5737A957C502F3CB
alias:          pci:v*d*sv*sd*bc0Csc00i10*
depends:        firewire-core
intree:         Y
vermagic:       4.2.0-19-generic SMP mod_unload modversions
signer:         Build time autogenerated kernel key
sig_key:        3B:EC:C2:05:81:AA:65:E9:FD:F9:C7:CB:D9:DA:08:DC:3A:FC:52:33
sig_hashalgo:   sha512
parm:           quirks:Chip quirks (default = 0, nonatomic cycle timer = 0x1, reset packet generation = 0x2, AR/selfID endianness = 0x4, no 1394a enhancements = 0x8, disable MSI = 0x10, TI SLLZ059 erratum = 0x20, IR wake unreliable = 0x40) (int)
parm:           debug:Verbose logging (default = 0, AT/AR events = 1, self-IDs = 2, IRQs = 4, busReset events = 8, or a combination, or all = -1) (int)
parm:           remote_dma:Enable unfiltered remote DMA (default = N) (bool)
```

It's also possible to filter out specific device information with ```grep```:

```
chenwx@chenwx ~ $ lspci -v | grep "VGA" -A 12
00:02.0 VGA compatible controller: Intel Corporation Mobile GM965/GL960 Integrated Graphics Controller (primary) (rev 0c) (prog-if 00 [VGA controller])
	Subsystem: Lenovo ThinkPad T61/R61
	Flags: bus master, fast devsel, latency 0, IRQ 31
	Memory at f8100000 (64-bit, non-prefetchable) [size=1M]
	Memory at e0000000 (64-bit, prefetchable) [size=256M]
	I/O ports at 1800 [size=8]
	Expansion ROM at <unassigned> [disabled]
	Capabilities: <access denied>
	Kernel driver in use: i915

00:02.1 Display controller: Intel Corporation Mobile GM965/GL960 Integrated Graphics Controller (secondary) (rev 0c)
	Subsystem: Lenovo ThinkPad T61/R61
	Flags: bus master, fast devsel, latency 0
```

## USB Buses Information

### lsusb

The command ```lsusb``` is a utility for displaying information about USB buses in the system and the devices connected to them.

```
chenwx@chenwx ~ $ lsusb
Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 007 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 006 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 004 Device 002: ID 046d:c050 Logitech, Inc. RX 250 Optical Mouse
Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub

chenwx@chenwx ~ $ lsusb -t
/:  Bus 07.Port 1: Dev 1, Class=root_hub, Driver=uhci_hcd/2p, 12M
/:  Bus 06.Port 1: Dev 1, Class=root_hub, Driver=uhci_hcd/2p, 12M
/:  Bus 05.Port 1: Dev 1, Class=root_hub, Driver=uhci_hcd/2p, 12M
/:  Bus 04.Port 1: Dev 1, Class=root_hub, Driver=uhci_hcd/2p, 12M
    |__ Port 1: Dev 2, If 0, Class=Human Interface Device, Driver=usbhid, 1.5M
/:  Bus 03.Port 1: Dev 1, Class=root_hub, Driver=uhci_hcd/2p, 12M
/:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=ehci-pci/6p, 480M
/:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=ehci-pci/4p, 480M
```

or, use the following command to show details of the specified device:

```
chenwx@chenwx ~ $ lsusb -v -s 002:001

Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Couldn't open device, some information will be missing
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               2.00
  bDeviceClass            9 Hub
  bDeviceSubClass         0 Unused
  bDeviceProtocol         0 Full speed (or root) hub
  bMaxPacketSize0        64
  idVendor           0x1d6b Linux Foundation
  idProduct          0x0002 2.0 root hub
  bcdDevice            4.02
  iManufacturer           3
  iProduct                2
  iSerial                 1
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength           25
    bNumInterfaces          1
    bConfigurationValue     1
    iConfiguration          0
    bmAttributes         0xe0
      Self Powered
      Remote Wakeup
    MaxPower                0mA
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           1
      bInterfaceClass         9 Hub
      bInterfaceSubClass      0 Unused
      bInterfaceProtocol      0 Full speed (or root) hub
      iInterface              0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x81  EP 1 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0004  1x 4 bytes
        bInterval              12
```

## Block Devices Information

### lsscsi

The command ```lsscsi``` uses information in sysfs (Linux kernel series 2.6 and later) to list SCSI devices (or hosts) currently attached to the system.

```
chenwx@chenwx ~ $ sudo apt-get install lsscsi

chenwx@chenwx ~ $ lsscsi --version
version: 0.27  2013/05/08 [svn: r111]

chenwx@chenwx ~ $ lsscsi
[0:0:0:0]    disk    ATA      CSD CAZ320S      n/a   /dev/sda
[2:0:0:0]    disk    ATA      Samsung SSD 840  BB6Q  /dev/sdb
```

### lsblk

The command ```lsblk``` list out information all block devices, which are the hard drive partitions and other storage devices like optical drives and flash drives.

```
chenwx@chenwx ~ $ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda      8:0    0 298.1G  0 disk
`-sda1   8:1    0 298.1G  0 part /media/chenwx/Work
sdb      8:16   0 111.8G  0 disk
|-sdb1   8:17   0   100M  0 part
|-sdb2   8:18   0  58.4G  0 part
|-sdb3   8:19   0   484M  0 part
|-sdb4   8:20   0     1K  0 part
`-sdb5   8:21   0  52.8G  0 part /
```

### hdparm

The command ```hdparm``` gets information about sata devices like hard disks.

```
chenwx@chenwx ~ $ sudo hdparm -i /dev/sda

/dev/sda:

 Model=CSD CAZ320S, FwRev=, SerialNo=
 Config={ HardSect NotMFM HdSw>15uSec Fixed DTR>10Mbs }
 RawCHS=16383/16/63, TrkSize=0, SectSize=0, ECCbytes=0
 BuffType=DualPortCache, BuffSize=8192kB, MaxMultSect=16, MultSect=16
 CurCHS=16383/16/63, CurSects=16514064, LBA=yes, LBAsects=625142448
 IORDY=on/off, tPIO={min:120,w/IORDY:120}, tDMA={min:120,rec:120}
 PIO modes:  pio0 pio1 pio2 pio3 pio4
 DMA modes:  mdma0 mdma1 mdma2
 UDMA modes: udma0 udma1 udma2 udma3 udma4 *udma5
 AdvancedPM=yes: mode=0x80 (128) WriteCache=enabled
 Drive conforms to: unknown:  ATA/ATAPI-3,4,5,6,7

 * signifies the current active mode
```

## Filesystem Information

### df

The command ```df``` reports various partitions, their mount points and the used and available space on each.

```
chenwx@chenwx ~ $ df -H
Filesystem      Size  Used Avail Use% Mounted on
udev            2.1G  4.1k  2.1G   1% /dev
tmpfs           407M  1.6M  406M   1% /run
/dev/sdb5        56G   42G   12G  78% /
none            4.1k     0  4.1k   0% /sys/fs/cgroup
none            5.3M     0  5.3M   0% /run/lock
none            2.1G   35M  2.0G   2% /run/shm
none            105M   25k  105M   1% /run/user
/dev/sda1       321G  255G   66G  80% /media/chenwx/Work
```

### pydf

The command ```pydf``` is an improved ```df``` version written in python, that displays colored output that looks better than ```df```.

```
chenwx@chenwx ~ $ sudo apt-get install pydf

chenwx@chenwx ~ $ pydf
Filesystem Size Used Avail Use%                                         Mounted on        
/dev/sdb5   52G  38G   11G 73.7 [###########################..........] /                 
/dev/sda1  298G 237G   61G 79.4 [#############################........] /media/chenwx/Work
```

### fdisk

The command ```fdisk``` is a utility to modify partitions on hard drives, and can be used to list out the partition information as well.

```
chenwx@chenwx ~ $ sudo fdisk -l

Disk /dev/sda: 320.1 GB, 320072933376 bytes
240 heads, 63 sectors/track, 41345 cylinders, total 625142448 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x9c050a53

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1              63   625140399   312570168+  42  SFS

Disk /dev/sdb: 120.0 GB, 120034123776 bytes
255 heads, 63 sectors/track, 14593 cylinders, total 234441648 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x000beffd

   Device Boot      Start         End      Blocks   Id  System
/dev/sdb1   *        2048      206847      102400    7  HPFS/NTFS/exFAT
/dev/sdb2          206848   122741313    61267233    7  HPFS/NTFS/exFAT
/dev/sdb3       122742784   123734015      495616   27  Hidden NTFS WinRE
/dev/sdb4       123736062   234440703    55352321    5  Extended
/dev/sdb5       123736064   234440703    55352320   83  Linux
```

### mount

The command ```mount``` is used to mount a filesystem.

```
chenwx@chenwx ~ $ mount | column -t
/dev/sdb5    on  /                                    type  ext4             (rw,errors=remount-ro)
proc         on  /proc                                type  proc             (rw,noexec,nosuid,nodev)
sysfs        on  /sys                                 type  sysfs            (rw,noexec,nosuid,nodev)
none         on  /sys/fs/cgroup                       type  tmpfs            (rw)
none         on  /sys/fs/fuse/connections             type  fusectl          (rw)
none         on  /sys/kernel/debug                    type  debugfs          (rw)
none         on  /sys/kernel/security                 type  securityfs       (rw)
udev         on  /dev                                 type  devtmpfs         (rw,mode=0755)
devpts       on  /dev/pts                             type  devpts           (rw,noexec,nosuid,gid=5,mode=0620)
tmpfs        on  /run                                 type  tmpfs            (rw,noexec,nosuid,size=10%,mode=0755)
none         on  /run/lock                            type  tmpfs            (rw,noexec,nosuid,nodev,size=5242880)
none         on  /run/shm                             type  tmpfs            (rw,nosuid,nodev)
none         on  /run/user                            type  tmpfs            (rw,noexec,nosuid,nodev,size=104857600,mode=0755)
none         on  /sys/fs/pstore                       type  pstore           (rw)
tracefs      on  /var/lib/ureadahead/debugfs/tracing  type  tracefs          (rw,relatime)
binfmt_misc  on  /proc/sys/fs/binfmt_misc             type  binfmt_misc      (rw,noexec,nosuid,nodev)
systemd      on  /sys/fs/cgroup/systemd               type  cgroup           (rw,noexec,nosuid,nodev,none,name=systemd)
gvfsd-fuse   on  /run/user/1000/gvfs                  type  fuse.gvfsd-fuse  (rw,nosuid,nodev,user=chenwx)
/dev/sda1    on  /media/chenwx/Work                   type  fuseblk          (rw,nosuid,nodev,allow_other,default_permissions,blksize=4096)
```

### findmnt

The command ```findmnt``` can be used to take a quick look at what is mounted where and with what options.

```
chenwx@chenwx ~ $ findmnt -l
TARGET                   SOURCE                                                 FSTYPE          OPTIONS
/sys                     sysfs                                                  sysfs           rw,nosuid,nodev,noexec,relatime
/proc                    proc                                                   proc            rw,nosuid,nodev,noexec,relatime
/dev                     udev                                                   devtmpfs        rw,relatime,size=1969892k,nr_inodes=492473,mode=755
/dev/pts                 devpts                                                 devpts          rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000
/run                     tmpfs                                                  tmpfs           rw,nosuid,noexec,relatime,size=397232k,mode=755
/                        /dev/disk/by-uuid/51ce0b57-1d7f-4da3-b46f-d6a0ea64c81d ext4            rw,relatime,errors=remount-ro,data=ordered
/sys/fs/cgroup                                                                  tmpfs           rw,relatime,size=4k,mode=755
/sys/fs/fuse/connections                                                        fusectl         rw,relatime
/sys/kernel/debug                                                               debugfs         rw,relatime
/sys/kernel/security                                                            securityfs      rw,relatime
/run/lock                                                                       tmpfs           rw,nosuid,nodev,noexec,relatime,size=5120k
/run/shm                                                                        tmpfs           rw,nosuid,nodev,relatime
/run/user                                                                       tmpfs           rw,nosuid,nodev,noexec,relatime,size=102400k,mode=755
/sys/fs/pstore                                                                  pstore          rw,relatime
/proc/sys/fs/binfmt_misc binfmt_misc                                            binfmt_misc     rw,nosuid,nodev,noexec,relatime
/sys/fs/cgroup/systemd   systemd                                                cgroup          rw,nosuid,nodev,noexec,relatime,name=systemd
/run/user/1000/gvfs      gvfsd-fuse                                             fuse.gvfsd-fuse rw,nosuid,nodev,relatime,user_id=1000,group_id=1000
/media/chenwx/Work       /dev/sda1                                              fuseblk         rw,nosuid,nodev,relatime,user_id=0,group_id=0,default_pe


# Read file systems from fstab
chenwx@chenwx ~ $ findmnt -s  
TARGET SOURCE                                    FSTYPE OPTIONS
/      UUID=51ce0b57-1d7f-4da3-b46f-d6a0ea64c81d ext4   errors=remount-ro

# Filter filesystems by type
chenwx@chenwx ~ $ findmnt -t ext4
TARGET SOURCE                                                 FSTYPE OPTIONS
/      /dev/disk/by-uuid/51ce0b57-1d7f-4da3-b46f-d6a0ea64c81d ext4   rw,relatime,errors=remount-ro,data=ordered

# Search by source device
chenwx@chenwx ~ $ findmnt -S /dev/sda1
TARGET             SOURCE    FSTYPE  OPTIONS
/media/chenwx/Work /dev/sda1 fuseblk rw,nosuid,nodev,relatime,user_id=0,group_id=0,default_permissions,allow_other,blksize=4096

# Search by mount point
chenwx@chenwx ~ $ findmnt -T /
TARGET SOURCE                                                 FSTYPE OPTIONS
/      /dev/disk/by-uuid/51ce0b57-1d7f-4da3-b46f-d6a0ea64c81d ext4   rw,relatime,errors=remount-ro,data=ordered
```

## Memory Information

### free

The command ```free``` checks the amount of used, free and total amount of RAM on system with the free command.

```
chenwx@chenwx ~ $ free -m
             total       used       free     shared    buffers     cached
Mem:          3879       3737        142        120        217       1574
-/+ buffers/cache:       1945       1934
Swap:            0          0          0
```

### vmstat

The command ```vmstat``` with the s option, lays out the memory usage statistics much like the proc command.

```
chenwx@chenwx ~ $ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0      0 194540 225156 1611012    0    0    36    97  335  448 13  2 86  0  0

chenwx@chenwx ~ $ vmstat -s
      3972284 K total memory
      3851852 K used memory
      2823888 K active memory
       751548 K inactive memory
       120432 K free memory
       225264 K buffer memory
      1627296 K swap cache
            0 K total swap
            0 K used swap
            0 K free swap
       994215 non-nice user cpu ticks
        16101 nice user cpu ticks
       131429 system cpu ticks
      6817796 idle cpu ticks
        12333 IO-wait cpu ticks
            0 IRQ cpu ticks
         3252 softirq cpu ticks
            0 stolen cpu ticks
      2872257 pages paged in
      7760196 pages paged out
            0 pages swapped in
            0 pages swapped out
     26694633 interrupts
     78835068 CPU context switches
   1450451585 boot time
        42883 forks
```

### top

The command ```top``` is generally used to check memory and cpu usage per process. However it also reports total memory usage and can be used to monitor the total RAM usage. The header on output has the required information.

```
chenwx@chenwx ~ $ top
```

### htop

Similar to the command ```top```, the command ```htop``` also shows memory usage along with various other details.

```
chenwx@chenwx ~ $ sudo apt-get install htop

chenwx@chenwx ~ $ htop
```

### dmidecode

dmidecode is a tool for dumping a computer's DMI (some say SMBIOS) table contents in a human-readable format. This table contains a description of the system's hardware components, as well as other useful pieces of information such as serial numbers and BIOS revision.  Thanks to this table, you can retrieve this information without having to probe for the actual hardware. While this is a good point in terms of report speed and safeness, this also makes the presented information possibly unreliable.

Use the following dmidecode commands to show the memory information:

```
chenwx@chenwx ~ $ sudo dmidecode | grep -P -A5 "Memory\s+Device" | grep Size | grep -v Range
	Size: 2048 MB
	Size: 2048 MB

chenwx@chenwx ~ $ sudo dmidecode | grep -P 'Maximum\s+Capacity'
	Maximum Capacity: 4 GB

chenwx@chenwx ~ $ sudo dmidecode | grep -A16 "Memory Device" | grep 'Speed'
	Speed: 667 MHz
	Speed: 667 MHz
```

## /proc Files

Many of the virtual files in the ```/proc``` directory contain information about hardware and configurations. Here are some of them:

```
# CPU information
chenwx@chenwx ~ $ cat /proc/cpuinfo
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 23
model name	: Intel(R) Core(TM)2 Duo CPU     T9300  @ 2.50GHz
stepping	: 6
microcode	: 0x60f
cpu MHz		: 800.000
cache size	: 6144 KB
physical id	: 0
siblings	: 2
core id		: 0
cpu cores	: 2
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 10
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx lm constant_tsc arch_perfmon pebs bts rep_good nopl aperfmperf pni dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm sse4_1 lahf_lm ida dtherm tpr_shadow vnmi flexpriority
bugs		:
bogomips	: 4987.45
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

# To count the number of processing units use grep with wc
chenwx@chenwx ~ $ cat /proc/cpuinfo | grep processor | wc -l
2

# Memory information
chenwx@chenwx ~ $ cat /proc/meminfo
MemTotal:        3972284 kB
MemFree:          196688 kB
MemAvailable:    2041008 kB
Buffers:          223100 kB
Cached:          1584416 kB
SwapCached:            0 kB
Active:          2738176 kB
Inactive:         764180 kB
Active(anon):    1703572 kB
Inactive(anon):   106368 kB
Active(file):    1034604 kB
Inactive(file):   657812 kB
Unevictable:          32 kB
Mlocked:              32 kB
SwapTotal:             0 kB
SwapFree:              0 kB
Dirty:               360 kB
Writeback:             0 kB
AnonPages:       1694872 kB
Mapped:           282540 kB
Shmem:            115100 kB
Slab:             208288 kB
SReclaimable:     181352 kB
SUnreclaim:        26936 kB
KernelStack:        6640 kB
PageTables:        28552 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:     1986140 kB
Committed_AS:    3804112 kB
VmallocTotal:   34359738367 kB
VmallocUsed:      344180 kB
VmallocChunk:   34358947836 kB
HardwareCorrupted:     0 kB
AnonHugePages:    595968 kB
CmaTotal:              0 kB
CmaFree:               0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:      103104 kB
DirectMap2M:     4016128 kB

# Linux/kernel information
chenwx@chenwx ~ $ cat /proc/version
Linux version 4.2.0-19-generic (buildd@lgw01-60) (gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1) ) #23~14.04.1-Ubuntu SMP Thu Nov 12 12:33:30 UTC 2015

# SCSI/Sata devices
chenwx@chenwx ~ $ cat /proc/scsi/scsi
Attached devices:
Host: scsi0 Channel: 00 Id: 00 Lun: 00
  Vendor: ATA      Model: CSD CAZ320S      Rev: n/a
  Type:   Direct-Access                    ANSI  SCSI revision: 05
Host: scsi2 Channel: 00 Id: 00 Lun: 00
  Vendor: ATA      Model: Samsung SSD 840  Rev: BB6Q
  Type:   Direct-Access                    ANSI  SCSI revision: 05

# Partitions
chenwx@chenwx ~ $ cat /proc/partitions
major minor  #blocks  name

   1        0      65536 ram0
   1        1      65536 ram1
   1        2      65536 ram2
   1        3      65536 ram3
   1        4      65536 ram4
   1        5      65536 ram5
   1        6      65536 ram6
   1        7      65536 ram7
   1        8      65536 ram8
   1        9      65536 ram9
   1       10      65536 ram10
   1       11      65536 ram11
   1       12      65536 ram12
   1       13      65536 ram13
   1       14      65536 ram14
   1       15      65536 ram15
   8        0  312571224 sda
   8        1  312568832 sda1
   8       16  117220824 sdb
   8       17     102400 sdb1
   8       18   61267233 sdb2
   8       19     495616 sdb3
   8       20          1 sdb4
   8       21   55352320 sdb5
```

## /sys Files

# References

* [16 commands to check hardware information on Linux](http://www.binarytides.com/linux-commands-hardware-info/)
* [Check hardware information on Linux with hwinfo command](http://www.binarytides.com/linux-hwinfo-command/)
* [How to install hwinfo on Fedora 19/20 and CentOS 5/6](http://www.binarytides.com/install-hwinfo-fedora-centos/)
* [8 commands to check cpu information on Linux](http://www.binarytides.com/linux-cpu-information/)
* [8 examples of findmnt command to check mounted file systems on Linux](http://www.binarytides.com/linux-findmnt-command/)
* [5 commands to check memory usage on Linux](http://www.binarytides.com/linux-command-check-memory-usage/)
