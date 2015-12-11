---
layout: post
title: "Unix System Overview"
tags: [Linux]
toc: true
---

This article introduces the Unix system.

<!--more-->

## Portable Operating System Interface (POSIX)

[Portable Operating System Interface (POSIX)](http://standards.ieee.org/develop/wg/POSIX.html) is a family of standards specified by the IEEE Computer Society for maintaining compatibility between operating systems. POSIX defines the application programming interface (API), along with command line shells and utility interfaces, for software compatibility with variants of Unix and other operating systems.

Originally, the name **POSIX** referred to **IEEE Std 1003.1-1988**, released in 1988. The family of POSIX standards is formally designated as **IEEE 1003** and the international standard name is **ISO/IEC 9945**.

### POSIX Standards

Before 1997, POSIX comprised several standards:

* **POSIX.1 (IEEE Std 1003.1-1988)**: Core Services (incorporates Standard ANSI C)
* **POSIX.1b (IEEE Std 1003.1b-1993)**: Real-time extensions
* **POSIX.1c (IEEE Std 1003.1c-1995)**: Threads extensions
* **POSIX.2 (IEEE Std 1003.2-1992)**: Shell and Utilities

After 1997, the [Austin Group](http://www.opengroup.org/austin/) developed the POSIX revisions. The specifications are known under the name **Single UNIX Specification (SUS)**, before they become a POSIX standard when formally approved by the ISO.

* **POSIX.1-2001 (IEEE Std 1003.1-2001)**: equates to the **Single UNIX Specification version 3 (SUSv3)**, see [The Open Group announces completion of the joint revision to POSIX® and the Single UNIX® Specification](http://www.unix.org/version3/pr.html)
* **POSIX.1-2004 (IEEE Std 1003.1-2004)**: involves a minor update of POSIX.1-2001 (IEEE Std 1003.1-2001). It incorporated two TCs (Technical Corrigenda).
* **POSIX.1-2008 (IEEE Std 1003.1-2008)**: Current active version, see [here](http://standards.ieee.org/findstds/standard/1003.1-2008.html).
* **POSIX.1-2008 with TC1 (IEEE Std 1003.1-2008/Cor 1-2013)**: Current active version, see [here](http://standards.ieee.org/findstds/standard/1003.1-2008-Cor_1-2013.html).

### POSIX-certified Systems

Some versions of the following operating systems have been certified to conform to one or more of the various POSIX standards. This means that they passed the automated conformance tests:

* IBM AIX
* HP-UX
* IRIX
* OS X (since 10.5 Leopard)
* Solaris
* Tru64
* UnixWare
* QNX Neutrino

## Single UNIX Specification (SUS)

[Single UNIX Specification (SUS)](http://www.unix.org/version4/) is the collective name of a family of standards for computer operating systems, compliance with which is required to qualify for the name **Unix**. The core specifications of the SUS are developed and maintained by the [Austin Group](http://www.opengroup.org/austin/), which is a joint working group of IEEE, [ISO JTC 1 SC22](http://www.open-std.org/JTC1/SC22/) and [The Open Group](http://www.opengroup.org/).

### SUS Standards

* **Single UNIX Specification version 1 (SUSv1)**: known as **Spec 1170**, the core of the **UNIX 95 brand**.
* **Single UNIX Specification version 2 (SUSv2)**: released in 1997, the core of the **UNIX 98 brand**.
* **Single UNIX Specification version 3 (SUSv3)**: released on January 30, 2002, the core of the **UNIX 03 brand**. Equates to the **POSIX:2001 (IEEE Std 1003.1-2001)**.
* **Single UNIX Specification version 4 (SUSv4)**: released in 2008.

### SUS-certified Systems

Currently, some versions of the following operating systems have been certified UNIX system:

* IBM AIX
* HP-UX
* Inspur K-UX
* Apple's OS X
* Solaris
* z/OS

## History of Unix system

1969: Unix was developed on Summer 1969.

1971: **Unix 1st edition** released on Nov 3, 1971.

1972: **Unix 2nd edition** released on Dec 6, 1972.

1973: **Unix 3rd edition** released in February 1973. **Unix 4th edition** released in November 1973.

1974: **Unix 5th edition** released in June 1974.

1975: **Unix 6th edition** released in May 1975. And Bourne shell is introduced begins being added onto.

1979: **Unix 7th edition** released in January 1979.

1985: **Unix 8th edition** released in February 1985.

1989: **Unix 10th edition** released in October 1989.

![Unix history](/assets/unix-history.png)

![Unix history](/assets/unix-history.svg)

## Reference

[Unix, Linux, and variant history](http://www.computerhope.com/history/unix.htm)
