---
layout: post
title: "RTOS: ThreadX"
tag: RTOS
toc: true
---

This article introduces the Real-Time Operating System **ThreadX**.

<!--more-->

# Overview

**ThreadX**, developed and marketed by *Express Logic, Inc.* of San Diego, California, USA, is a Real-Time Operating System (RTOS). Similar RTOSes are available from other vendors such as *VxWorks*, *Nucleus RTOS*, *OSE*, *QNX*, *LynxOS*, etc. The author of ThreadX (as well as Nucleus) is *William Lamie*, who is the President and CEO of *Express Logic, Inc*.

The name ThreadX is derived from the fact that threads are used as the executable modules and the letter ***X*** represents context switching, i.e., it switches threads. ThreadX can be seen as the *QThreads* of SystemC implemented in preemptive fashion.

Like most RTOSes, ThreadX uses a multitasking kernel with preemptive scheduling, fast interrupt response, memory management, interthread communication, mutual exclusion, event notification, and thread synchronization features.

Major distinguishing characteristics of ThreadX include priority inheritance, preemption-threshold, efficient timer management, picokernel design, event-chaining, fast software timers, and compact size. ThreadX is distributed using a marketing model in which source code is provided and licenses are royalty-free.

ThreadX is generally used in real-time embedded systems, especially in deeply embedded systems. Developing embedded systems using ThreadX is usually done on a host machine running Linux or Microsoft Windows, using cross-compiling target software to run on various target processor architectures. Several ThreadX-aware development tools are available, such as Wind River Workbench, ARM RealView, Green Hills Software's MULTI, Metrowerks CodeWarrior, IAR C-SPY, Lauterbach TRACE32, and visionCLICK.

Hewlett-Packard has licensed the use of ThreadX for all Inkjet, Laserjet and all-in-one devices recently[when?]. Earlier they were using LynxOS for multifunctional laserjet printers and still many printers use LynxOS. ThreadX is widely used in a variety of consumer electronics, medical devices, data networking applications, and SoC development.

# References

* [Express Logic, Inc.](http://rtos.com/products/threadx/)
