---
layout: post
title: "Linux Series #5: C/C++ Libraries"
tags: [Linux]
toc: true
---

This article introduces C standard library and its implementations on Linux system.

<!--more-->

# C Standards

![C Language Evolution](/assets/C_Language_Evolution.png)

* **K&R C**

    First edition of ***The C Programming Language*** published by **Brian Kernighan** and **Dennis Ritchie** in 1978. This book, known to C programmers as **K&R**, served for many years as an informal specification of the language. The version of C that it describes is commonly referred to as **K&R C**.

* **ANSI X3.159-1989 (ANSI C, C89)**

    In 1983, the **American National Standards Institute (ANSI)** formed a committee, **X3J11**, to establish a standard specification of C. **X3J11** based the C standard on the Unix implementation; however, the non-portable portion of the Unix C library was handed off to the **IEEE working group 1003** to become the basis for the 1988 POSIX standard. In 1989, the C standard was ratified as **ANSI X3.159-1989** ***Programming Language C***. This version of the language is often referred to as **ANSI C**, **Standard C**, or sometimes **C89**.

* **ISO/IEC 9899:1990 (C90)**

    In 1990, the **ANSI C** standard (with formatting changes) was adopted by the International Organization for Standardization (ISO) [C Standard Committee (ISO/IEC JTC1/SC22/WG14 - C)](http://www.open-std.org/JTC1/SC22/WG14/www/standards) as **ISO/IEC 9899:1990**, which is sometimes called **C90**. Therefore, the terms **C89** and **C90** refer to the same programming language.

    It has since been amended three times by Technical Corrigenda (COR) or Amendment (AMD):

    * **ISO/IEC 9899:1990/AM1:1995** (known as **C90 AMD1** or **C95**)
    * **ISO/IEC 9899:1990/COR1:1995**
    * **ISO/IEC 9899:1990/COR2:1996**
     <br>

* **ISO/IEC9899:1999 (C99)**

    The C standard was further revised in the late 1990s, leading to the publication of **ISO/IEC 9899:1999** in 1999, which is commonly referred to as **C99**.

    It has since been amended three times by Technical Corrigenda (COR):

    * **ISO/IEC 9899:1999/COR1:2001**
    * **ISO/IEC 9899:1999/COR2:2004**
    * **ISO/IEC 9899:1999/COR3:2007**
     <br>

* **ISO/IEC 9899:2011 (C11)**

    In 2007, work began on another revision of the C standard, informally called **C1X** until its official publication on 2011-12-08. The C standards committee adopted guidelines to limit the adoption of new features that had not been tested by existing implementations. The **C11** standard adds numerous new features to C and the library, including type generic macros, anonymous structures, improved Unicode support, atomic operations, multi-threading, and bounds-checked functions. It also makes some portions of the existing **C99** library optional, and improves compatibility with C++.

    It has since been amended by Technical Corrigenda:

    * **ISO/IEC 9899:2011/COR1:2012**

# C++ Standards

![C++ Language Evolution](/assets/CPP_Language_Evolution.png)

C++ is standardized by the International Organization for Standardization (ISO) [C++ Standards Committee (JTC1/SC22/WG21 - C++)](http://www.open-std.org/jtc1/sc22/wg21/). So far, it has seen following versions of C++ released:

* **ISO/IEC 14882:1998 (C++98)**

    In 1998, the ISO working group standardized C++ for the first time as **ISO/IEC 14882:1998**, which is informally known as **C++98**.

* **ISO/IEC 14882:2003 (C++03)**

    In 2003, ISO working group published a new version of the C++ standard called **ISO/IEC 14882:2003**, which is informally known as **C++03**. This version of the C++ standard fixed problems identified in **C++98**.

* **ISO/IEC TR 19768:2007 - C++ Library Extensions (C++07/TR1)**

    In 2007, a technical report **ISO/IEC TR 19768:2007 - C++ Library Extensions** was released, which is informally known as **C++07/TR1**. While not an official part of the standard, it proposed a number of extensions to the standard library.

* **ISO/IEC TR 29124:2010 - C++ Special Math Functions**

    In 2010, a technical report **ISO/IEC TR 29124:2010 - C++ Special Math Functions** is released. The draft can be found [here](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2010/n3060.pdf).

* **ISO/IEC 14882:2011 (C++11)**

    In 2011, a major revision of the standard was informally referred to as ***C++0x***, but it was not released until 2011. The **ISO/IEC 14882:2011 (C++11)** included most of the library enhancements of **C++07/TR1**, as well as many additions to the core language.

* **ISO/IEC TR 24733:2011 - C++ decimal floating point arithmetic extensions**

    In 2011, a technical report **ISO/IEC TR 24733:2011 - C++ decimal floating point arithmetic extensions** is released. The draft can be found [here](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2009/n2849.pdf).

* **ISO/IEC 14882:2014 (C++14)**

    In 2014, **C++14** (also known as ***C++1y***) was released as a small extension to **C++11**, featuring mainly bug fixes and small improvements.

# GNU C Library

The [GNU C Library](http://www.gnu.org/software/libc/), commonly known as **glibc**, is the GNU Project's implementation of the C standard library. Despite its name, it now also directly supports C++ (and indirectly other programming languages). Was started in the early 1990s by the **Free Software Foundation (FSF)** for their GNU operating system. Released under the **GNU Lesser General Public License (LGPL)**, **glibc** is free software.

## glibc Repository

In 2009, glibc was migrated to a [Git repository on Sourceware](https://sourceware.org/glibc/wiki/GlibcGit). You can use following command to clone the git repository, and browse the glibc on [gitweb](https://sourceware.org/git/?p=glibc.git).

```
chenwx@chenwx $ git clone git://sourceware.org/git/glibc.git
```

## glibc Versions

| Versions  | Release_Date | Note |
| :-------- | :----------: | :--- |
| 1.0       | Feb 1992     |      |
| 2.0       | Jan 1997     |      |
| 2.1       | Jan 1999     |      |
| 2.1.1     | Mar 1999     |      |
| 2.2       | Nov 2000     |      |
| 2.2.1     | Jan 2001     |      |
| 2.2.2     | Feb 2001     |      |
| 2.2.3     | Mar 2001     |      |
| 2.2.4     | Jul 2001     |      |
| 2.3       | Oct 2002     |      |
| 2.3.1     | Oct 2002     |      |
| 2.3.2     | Feb 2003     |      |
| 2.3.3     | Dec 2003     |      |
| **2.3.4** | Dec 2004     | **Standard for Linux Standard Base (LSB) 3.0** |
| 2.3.5     | Apr 2005     |      |
| 2.3.6     | Nov 2005     |      |
| **2.4**   | Mar 2006     | **Standard for Linux Standard Base (LSB) 4.0**, initial inotify support |
| 2.5       | Sep 2006     | Full inotify support |
| 2.6       | May 2007     |      |
| 2.7       | Oct 2007     |      |
| 2.8       | Apr 2008     |      |
| 2.9       | Nov 2008     |      |
| 2.10      | May 2009     |      |
| 2.11      | Oct 2009     |      |
| 2.12      | May 2010     |      |
| 2.13      | Jan 2011     |      |
| 2.14      | Jun 2011     |      |
| 2.15      | Mar 2012     |      |
| 2.16      | Jun 2012     | x32 ABI support, ISO C11 compliance, SystemTap |
| 2.17      | Dec 2012     | 64-bit ARM support |
| 2.18      | Aug 2013     | Improved C++11 support. Support for Intel TSX lock elision. Support for the Xilinx MicroBlaze and IBM POWER8 microarchitectures. |
| 2.19      | Feb 2014     | SystemTap probes for malloc. GNU Indirect Function (IFUNC) support for ppc32 and ppc64. New feature test macro _DEFAULT_SOURCE to replace _SVID_SOURCE and _BSD_SOURCE. Preliminary safety documentation for all functions in the manual. ABI change in ucontext and jmp_buf for s390/s390x. |
| 2.20      | Sep 2014     | Support for file description locks |
| 2.21      | Feb 2015     | New semaphore implementation |
| 2.22      | Aug 2015     | Google Native Client (NaCl) for running on ARMv7-A, Unicode 7.0 |

# References

[ISO/IEC 9899 - Programming languages - C](http://www.open-std.org/jtc1/sc22/wg14/www/standards)
[C programming language on wiki](https://en.wikipedia.org/wiki/C_%28programming_language%29)

[JTC1/SC22/WG21 - The C++ Standards Committee](http://www.open-std.org/jtc1/sc22/wg21/)
[C++ programming language on wiki](https://en.wikipedia.org/wiki/C%2B%2B)

[GNU C Library Wikipedia](https://en.wikipedia.org/wiki/GNU_C_Library)
[GNU C Library FTP](http://ftp.gnu.org/gnu/libc/)
[GNU C Library Reporsitory](https://sourceware.org/glibc/wiki/GlibcGit)
