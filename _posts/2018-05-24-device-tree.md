---
layout: post
title: "Device Tree"
tag: Linux
toc: true
---

This article introduces device tree under Linux environment.

<!--more-->

# Overview

In computing, a **device tree** (also written **devicetree**) is a data structure describing the hardware components of a particular computer so that the operating system's kernel can use and manage those components, including the CPU or CPUs, the memory, the buses and the peripherals.

The device tree was derived from SPARC-based workstations and servers via the [Open Firmware project](https://web.archive.org/web/20110610141437/http://playground.sun.com/1275/home.html). The current Devicetree specification[1] is targeted at smaller systems, but is still used with some server-class systems (for instance, those described by the Power Architecture Platform Reference (PAPR) including some Apple Macintoshes).

Personal computers with the x86 architecture generally do not use device trees, relying instead on various auto configuration protocols to discover hardware. Systems which use device trees usually pass a static device tree (perhaps stored in ROM) to the operating system, but can also generate a device tree in the early stages of booting. As an example, Das U-Boot and kexec can pass a device tree when launching a new operating system. On systems with a boot loader that does not support device trees, a static device tree may be installed along with the operating system; the Linux kernel supports this approach.

# Device Tree Specification

The Devicetree specification is currently managed by a community named [devicetree.org](https://www.devicetree.org/), which is associated with, among others, [Linaro](https://www.linaro.org/) and [Arm](https://www.arm.com/).

* [DeviceTree Specification Release v0.1](/docs/devicetree-specification-v0.1-20160524.pdf)
* [DeviceTree Specification Release v0.2](/docs/devicetree-specification-changebars-v0.2.pdf)

# Device Tree Formats

A device tree can hold any kind of data as internally it is a **tree** of named **nodes** and **properties**. Nodes contain properties and child nodes, while properties are *name-value* pairs.

Device trees have both a **binary format** (DTC) for operating systems to use and a **textual format** (DTS) for convenient editing and management.

* [About The Device Tree](/docs/About_The_Device_Tree.pdf)
* [Device Tree Usage](http://www.devicetree.org/Device_Tree_Usage)

# References

* [Device Tree on Wikipedia](https://en.wikipedia.org/wiki/Device_tree)
* [Open Firmware Quick Reference](http://www.firmworks.com/QuickRef.html)
* [devicetree.org](https://www.devicetree.org/)
* [Device Tree Usage](http://www.devicetree.org/Device_Tree_Usage)
* [Device Tree Reference](https://elinux.org/Device_Tree_Reference)
* [Device Tree on OMAPpedia](http://omappedia.org/wiki/Device_Tree)
* [Linux and the Device Tree](https://www.kernel.org/doc/Documentation/devicetree/usage-model.txt)
* [Device Tree Tutorial (ARM)](https://saurabhsengarblog.wordpress.com/2015/11/28/device-tree-tutorial-arm/)
