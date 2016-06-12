---
layout: post
title: "Linux: Linux kernel"
tag: Linux
toc: true
---

This article introduces the most important part of Linux system: kernel.

<!--more-->

# Linux kernel

The Linux kernel is the most important part of the Linux system. You can get Linux kernel source code from its official site [The Linux Kernel Archives](https://www.kernel.org/). Also you can browse Linux kernel source code on git repositories for the [Linux kernel mainline](https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/), [Linux kernel stable tree](https://git.kernel.org/cgit/linux/kernel/git/stable/linux-stable.git/) and [linux-next integration testing tree](linux-next integration testing tree).

## Linux kernel Releases

[Here](https://en.wikipedia.org/wiki/History_of_Linux) is a short history of Linux kernel (until December 06, 2015):

| kernel version | Release date |  Status  | Note |
| :------------: | :----------: | :------: | :--- |
| 0.01           | Sep 17, 1991 | EOL      |      |
| 0.10           | Nov 1991     | EOL      |      |
| 0.11           | Dec 1991     | EOL      | The first version to be self-hosted, as Linux kernel 0.11 could be compiled by a computer running the same kernel version. |
| 0.12           | Feb 1992     | EOL      | Adopt the GNU General Public License (GPL). |
| 0.95           | Mar 08, 1992 | EOL      | The first version to be capable of running X Window System. |
| 1.0            | Mar 14, 1994 | EOL      |      |
| 1.1            | Apr 06, 1994 | EOL      |      |
| 1.2            | Mar 07, 1995 | EOL      |      |
| pre2.0         | May 12, 1996 | EOL      |      |
| 1.3            | Jun 12, 1995 | EOL      |      |
| 2.0            | Jun 09, 1996 | EOL      |      |
| 2.2            | Jan 26, 1999 | EOL      |      |
| 2.4            | Jan 04, 2001 | EOL      |      |
| 2.6            | Dec 17, 2003 | EOL      |      |
| 2.6.11         | Mar 02, 2005 | EOL      |      |
| 2.6.12         | Jun 18, 2005 | EOL      |      |
| 2.6.13         | Aug 28, 2005 | EOL      |      |
| 2.6.14         | Oct 27, 2005 | EOL      |      |
| 2.6.15         | Jan 02, 2006 | EOL      |      |
| 2.6.16         | Mar 20, 2006 | EOL      |      |
| 2.6.17         | Jun 17, 2006 | EOL      |      |
| 2.6.18         | Sep 20, 2006 | EOL      |      |
| 2.6.19         | Nov 26, 2006 | EOL      |      |
| 2.6.20         | Feb 04, 2007 | EOL      |      |
| 2.6.21         | Apr 25, 2007 | EOL      |      |
| 2.6.22         | Jul 08, 2007 | EOL      |      |
| 2.6.23         | Oct 09, 2007 | EOL      |      |
| 2.6.24         | Jan 24, 2008 | EOL      |      |
| 2.6.25         | Apr 16, 2008 | EOL      |      |
| 2.6.26         | Jul 13, 2008 | EOL      |      |
| 2.6.27         | Oct 09, 2008 | EOL      |      |
| 2.6.28         | Dec 12, 2008 | EOL      |      |
| 2.6.29         | Mar 23, 2009 | EOL      |      |
| 2.6.30         | Jun 09, 2009 | EOL      |      |
| 2.6.31         | Sep 09, 2009 | EOL      |      |
| **2.6.32**     | Dec 02, 2009 | Longterm |      |
| 2.6.33         | Feb 24, 2010 | EOL      |      |
| 2.6.34         | May 16, 2010 | EOL      |      |
| 2.6.35         | Aug 01, 2010 | EOL      |      |
| 2.6.36         | Oct 20, 2010 | EOL      |      |
| 2.6.37         | Jan 04, 2011 | EOL      |      |
| 2.6.38         | Mar 14, 2011 | EOL      |      |
| 2.6.39         | May 18, 2011 | EOL      |      |
| 3.0            | Jul 21, 2011 | EOL      | Release kernel 3.0 to mark the kernel's 20th anniversary. |
| 3.1            | Oct 24, 2011 | EOL      |      |
| **3.2**        | Jan 04, 2012 | Longterm |      |
| 3.3            | Mar 18, 2012 | EOL      |      |
| **3.4**        | May 20, 2012 | Longterm |      |
| 3.5            | Jul 21, 2012 | EOL      |      |
| 3.6            | Sep 30, 2012 | EOL      |      |
| 3.7            | Dec 10, 2012 | EOL      |      |
| 3.8            | Feb 18, 2013 | EOL      |      |
| 3.9            | Apr 28, 2013 | EOL      |      |
| **3.10**       | Jun 30, 2013 | Longterm |      |
| 3.11           | Sep 02, 2013 | EOL      |      |
| **3.12**       | Nov 03, 2013 | Longterm |      |
| 3.13           | Jan 19, 2014 | EOL      |      |
| **3.14**       | Mar 30, 2014 | Longterm |      |
| 3.15           | Jun 08, 2014 | EOL      |      |
| 3.16           | Aug 03, 2014 | EOL      |      |
| 3.17           | Oct 05, 2014 | EOL      |      |
| **3.18**       | Dec 07, 2014 | Longterm |      |
| 3.19           | Feb 08, 2015 | EOL      |      |
| 4.0            | Apr 12, 2015 | EOL      |      |
| **4.1**        | Jun 22, 2015 | Longterm |      |
| **4.2**        | Aug 30, 2015 | Stable   |      |
| **4.3**        | Nov 01, 2015 | Stable   |      |
| **4.4**        | Dec 06, 2015 | Mainline |      |

<p/>

If we draw a picture of Linux kernel releases, it should be like this:

![Linux_Kernel_Releases](/assets/Linux_Kernel_Releases.20151218.svg)

![Linux_Kernel_Timeline](/assets/linux_kernel_timeline.png)

## Version Numbering

The Linux kernel has had [three different numbering schemes](https://en.wikipedia.org/wiki/Linux_kernel#Version_numbering):

* First numbering scheme: **kernel 0.01 ~ 1.0**

    The first scheme was used in the run-up to **1.0**. The first version of the kernel was 0.01. This was followed by 0.02, 0.03, 0.10, 0.11, 0.12 (the first GPL version), 0.95, 0.96, 0.97, 0.98, 0.99 and then 1.0. From 0.95 on there were many patch releases between versions.

* Second numbering scheme: **kernel 1.0 ~ 2.6.0**, Even-odd version numbering scheme

    After the 1.0 release and prior to version 2.6, the number was composed as ***x.y.z***, where the number ***x*** denoted the kernel version, the number ***y*** denoted the major revision of the kernel, and the number ***z*** indicated the minor revision of the kernel. The kernel version was changed only when major changes in the code and the concept of the kernel occurred (Note: version 3.0 was released in 2011, but it was not a major change in kernel concept). The major revision was assigned according to the **even-odd version numbering scheme**. The minor revision had been changed whenever security patches, bug fixes, new features or drivers were implemented in the kernel.

* Third numbering scheme: **kernel 2.6.0 ~ present**, Time-based release numbering scheme

    After version 2.6.0 was released in 2004, a **time-based** release cycle was adopted. For about seven years, the first two numbers remained **2.6**, and the third number was incremented with each new release, which rolled out after two to three months. A fourth number was sometimes added to account for bug and security fixes (only) to the kernel version. The **even-odd system** of alternation between stable and unstable was gone. Instead, development pre-releases are titled release candidates, which is indicated by appending the suffix ***-rc*** to the kernel version, followed by an ordinal number.

    The first use of the fourth number occurred when a grave error, which required immediate fixing, was encountered in **2.6.8's NFS code**. However, there were not enough other changes to legitimize the release of a new minor revision (which would have been 2.6.9). So, [2.6.8.1 was released](https://lwn.net/Articles/97898/), with the [only change](https://www.kernel.org/pub/linux/kernel/v2.6/ChangeLog-2.6.8.1) being the fix of that error. With 2.6.11, this was adopted as the new official versioning policy. Later it became customary to continuously back-port major bug-fixes and security patches to released kernels and indicate that by updating the fourth number.

    On 29 May 2011, Linus Torvalds [announced](https://lkml.org/lkml/2011/5/29/204) that the kernel version would be bumped to 3.0 for the release following 2.6.39, **due to the minor version number getting too large and to commemorate the 20th anniversary of Linux**. It continued the time-based release practice introduced with 2.6.0, but using the second number; for example, 3.1 would follow 3.0 after a few months.

    The major version number was also raised to 4 [announced on 22 Feb 2015](https://lkml.org/lkml/2015/2/22/203), for the release following version 3.19.

# References

* [The Linux Kernel Archives](https://www.kernel.org/)
* [Linux kernel Mainline Repository](https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/)
* [Linux kernel Stable Repository](https://git.kernel.org/cgit/linux/kernel/git/stable/linux-stable.git/)
* [Linux kernel Next Repository](https://git.kernel.org/cgit/linux/kernel/git/next/linux-next.git/)
* [Linux kernel version numbering](https://en.wikipedia.org/wiki/Linux_kernel#Version_numbering)
* [Linux Foundation Referenced Specifications](http://refspecs.linuxfoundation.org/)
