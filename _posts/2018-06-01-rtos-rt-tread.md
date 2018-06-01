---
layout: post
title: "RTOS: RT-Thread"
tag: RTOS
toc: true
---

This article introduces the open source IoT operating system **RT-Thread**.

<!--more-->

# Overview

[RT-Thread](https://www.rt-thread.org/) is an open source IoT operating system from China, which has strong scalability: from a tiny kernel running on a tiny core, for example ARM Cortex-M0, or Cortex-M3/4/7, to a rich feature system running on MIPS32, ARM Cortex-A8, ARM Cortex-A9 DualCore etc.

RT-Thread RTOS like a traditional real-time operating system. The kernel has real-time multi-task scheduling, semaphore, mutex, mail box, message queue, signal etc. However, it has three different things:

* Device Driver;
* Component;
* Application Module

The device driver is more like a driver framework, UART, IIC, SPI, SDIO, USB device/host, EMAC, MTD NAND etc. The developer can easily add low level driver and board configuration, then combined with the upper framework, he/she can use lots of features.

The Component is a software concept upon RT-Thread kernel, for example a shell (finsh/msh shell), virtual file system (FAT, YAFFS, UFFS, ROM/RAM file system etc), TCP/IP protocol stack (lwIP), POSIX (thread) interface etc. One component must be a directory under RT-Thread/Components and one component can be descripted by a SConscript file (then be compiled and linked into the system).

The Appliation Module, or User Applicaion (UA) is a dyanmic loaded module, it can be compiled standalone without Kernel. Each UA has its own object container to manage thread/semaphore/kernel object which was created or initialized inside this UA. More information about UA, please visit another [git repo](https://github.com/RT-Thread/rtthread-apps).

# References

* [RT-Thread](https://www.rt-thread.org/)
* [RT-Thread Git Repo](https://github.com/RT-Thread/rt-thread)
