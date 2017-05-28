---
layout: post
title: "RTOS: Overview"
tag: RTOS
toc: true
---

This article introduces the basic knowledge of Real-Time Operating System (RTOS).

<!--more-->

# What's RTOS?

A real-time operating system (RTOS) is an operating system (OS) intended to serve real-time application process data as it comes in, typically without buffering delays. Processing time requirements (including any OS delay) are measured in tenths of seconds or shorter.

A key characteristic of a RTOS is the level of its consistency concerning the amount of time it takes to accept and complete an application's task; the variability is *jitter*. A *hard* real-time operating system has less jitter than a *soft* real-time operating system. The chief design goal is not high throughput, but rather a guarantee of a soft or hard performance category. A RTOS that can usually or *generally* meet a *deadline* is a *soft real-time OS*, but if it can meet a deadline *deterministically* it is a *hard real-time OS*.

A RTOS has an advanced algorithm for scheduling. Scheduler flexibility enables a wider, computer-system orchestration of process priorities, but a real-time operating system is more frequently dedicated to a narrow set of applications. Key factors in a real-time operating system are minimal interrupt latency and minimal thread switching latency; a real-time operating system is valued more for how quickly or how predictably it can respond than for the amount of work it can perform in a given period of time.

# List of RTOS

The RTOS is developed and supplied by multiple suppliers in an open market. See the [comparison of real-time operating systems](https://en.wikipedia.org/wiki/Comparison_of_real-time_operating_systems) for a comprehensive list. Here is a list of RTOS, which are used during my work.

| Name | License | Source Model | Target | Status | Platforms |
| :--- | :------ | :----------- | :----- | :----- | :-------- |
| [**OSE**](http://www.enea.com/ose) | Proprietary | Closed | General purpose | Active | ARM, PowerPC, MIPS, IXP2400, TI OMAP, ... |
| [**ThreadX**](http://rtos.com/products/threadx) | Proprietary | Available to customers | ? | Active | ARC, ARM/Thumb, AVR32, BlackFin, 680x0-ColdFire, H8-300H, Luminary Micro Stellaris, M-CORE, MicroBlaze, PIC24-dsPIC, PIC32, MIPS, V8xx, Nios II, PowerPC, Renesas RX100, RX200, RX600, RX700, Synergy, SH, SHARC, StarCore, STM32, StrongARM, TMS320C54x, TMS320C6x, x86/x386, XScale, Xtensa/Diamond, ZSP |
| [**Micrium µC/OS-II**](http://micrium.com/rtos/ucosii/overview) | Proprietary | Available under license | Embedded | Active | ARM7-9-11/Cortex-M1-3-4-A8/9, AVR, HC11/12/S12, ColdFire, Blackfin, MicroBlaze, NIOS, 8051, x86, Win32, H8S, M16C, M32C, MIPS, 68000, PIC24-dsPIC33-PIC32, MSP430, PowerPC, SH, StarCore, Renesas RX100-200-600-700, RL; STM32, ... |
| [**Micrium µC/OS-III**](http://micrium.com/rtos/ucosiii/overview) | Proprietary | Available under license | Embedded | Active | ARM7-9-11/Cortex-M1-3-4-A8/9, AVR, HC11/12/S12, ColdFire, Blackfin, MicroBlaze, NIOS, 8051, x86, Win32, H8S, M16C, M32C, MIPS, 68000, PIC24/dsPIC33/PIC32, MSP430, PowerPC, SH, StarCore, Renesas RX100-200-600-700, RL; STM32, ... |

<p/>

Here is a list of RTOS, which is open source:

* [RT-Thread](http://www.rt-thread.org/)
* [eCos](http://ecos.com/)
* [Fiasco]()
* [FreeRTOS](http://www.freertos.org/)
* [Phoenix-RTOS](http://www.phoesys.com/)
* [Nut/OS](http://www.ethernut.de/en/firmware/nutos.html)
* [Prex](https://www.prexcard.com/)
* [RTAI](https://www.rtai.org/)
* [RTEMS](https://www.rtems.org/)
* [Real-Time Linux](https://rt.wiki.kernel.org/index.php/Main_Page)
* SHaRK
* [TRON Project](http://www.tron.org/index-e.html)
* [Xenomai](https://xenomai.org)
* [CoOS](http://www.brc-electronics.nl/coos)

Here is a list of RTOS, which is not open source:

* [Ardence RTX](http://www.intervalzero.com/)
* [BeOS](http://toastytech.com/guis/b5pe.html)
* [ChorusOS](http://docs.oracle.com/cd/E19048-01/chorus5/806-6893/auto1/index.html)
* [DNIX](https://dflund.se/~triad/diab/dnix.html)
* [DMERT](https://en.wikipedia.org/wiki/Multi-Environment_Real-Time)
* [e-Tkernel](https://china.xilinx.com/products/intellectual-property/1-25wc4j.html)
* HOPEN OS
* [embOS](https://www.segger.com/embos.html)
* [INTEGRITY](www.ghs.com/products/rtos/integrity.html)
* ITRON
* LynxOS
* MERT
* MicroC/OS-II
* MQX RTOS
* Nucleus
* OS-9
* OSE
* OSEK/VDX
* OSEKtime
* PDOS
* Phar Lap ETS
* PikeOS
* Portos
* pSOS
* QNX
* RMX
* RSX-11
* RT-11
* RTOS-UH
* RTXC
* Salvo RTOS
* SINTRAN III
* Symbian OS
* ThreadX
* VRTX
* VxWorks
* Windows CE
* µnOS
* UNIX-RTR
* REX
* HP-1000/RTE

# References

* [RTOS Wikipedia](https://en.wikipedia.org/wiki/Real-time_operating_system)
* [Comparison of Real-Time Operating Systems (RTOS) at Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_real-time_operating_systems)
* [Comparison of Real-Time Operating Systems (RTOS) at DMOZ](https://www.dmoz.org/Computers/Software/Operating_Systems/Realtime)
* [2014 Embedded Market Study](http://bd.eduweb.hhs.nl/es/2014-embedded-market-study-then-now-whats-next.pdf)
