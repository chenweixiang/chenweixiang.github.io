---
layout: post
title: "Linux System Overview"
tags: [Linux]
toc: true
---

This article introduces Linux system overview.

<!--more-->

## Linux Standard Base (LSB)

The [Linux Standard Base (LSB)](http://refspecs.linuxfoundation.org/lsb.shtml) was created to lower the overall costs of supporting the Linux platform. By reducing the differences between individual Linux distributions, the LSB greatly reduces the costs involved with porting applications to different distributions, as well as lowers the cost and effort involved in after-market support of those applications.

The picture below represents the key LSB deliverables for application and distribution developers:
![LSB Specifications and Tools](/assets/lsb_concept_tools.png)

### LSB Specifications

The official home of the LSB specification is the [Linux Foundation's Reference Specifications Archive](http://refspecs.linuxfoundation.org/lsb.shtml). The following LSB specifications are released:

* **LSB 1.0** was released on June 29, 2001.

* **LSB 1.1** was released on January 22, 2002.

* **LSB 1.2** was released on June 28, 2002.

* **LSB 1.3** was released on December 17, 2002.

* **LSB 2.0** was released on August 31, 2004. The release omitted the PPC32 and S390 architectures.

* **LSB 2.0.1** was released on October 21, 2004.

* **LSB 2.1** was released on March 11, 2005.

* **LSB 3.0** was released on July 6, 2005.

* **LSB 3.1** Core was released on October 27, 2005; LSB 3.1 C++ and Desktop were released April 24, 2006.

    Note that the Core module specification of LSB 3.1 is the document submitted for publication by ISO/IEC as **IS 23360:1996**.

* **LSB 3.2** was released on January 25, 2008

    Note that the LSB 3.2 Core specification is an evolution of the ISO/IEC International Standard 23360, which corresponded to LSB 3.1. This edition is not to be considered an ISO standard.

* **LSB 4.0** was released on May 1, 2009

    Note that the LSB 4.0 Core specification is an evolution of the ISO/IEC International Standard 23360, which corresponded to LSB 3.1. This edition is not to be considered an ISO standard.

* **LSB 4.1** was released on February 16, 2011

    Note that the LSB 4.1 Core specification is an evolution of the ISO/IEC International Standard 23360, which corresponded to LSB 3.1. This edition is not to be considered an ISO standard.

* **LSB 5.0** was released on June 3, 2015.

    Note that the LSB 5.0 Core specification set is an evolution of the ISO/IEC International Standard 23360, which corresponded to LSB 3.1. This edition is not to be considered an ISO standard.

<br>

The Linux Standard Base (LSB) specifications are made available in two parts: **an architecture independent (generic) part** and **an architecture dependent part**. The architecture independent part is comprised of five modules: Core, C++, Desktop, Languages and Printing. The architecture dependent part is comprised of three modules: Core, C++ and Desktop.

Also, there are **mandatory** and **trial use** modules in the specification. The former impose mandatory requirements on LSB compliant distributions and applications may safely rely on the functionality described in mandatory modules. Functionality in trial use modules is not required in LSB compliant distributions and applications should take this into consideration. Meanwhile, trial use modules represent candidates for inclusion in the next versions of LSB.

### LSB Navigator

LSB Database is a central place for storing information about the LSB standard and about the surrounding Linux ecosystem. [LSB Navigator](http://www.linuxbase.org/navigator/commons/welcome.php) represents web based interface over all these information. It can be used by Linux developers, Linux distribution vendors and LSB workgroup to browse, query, analyze and submit various information.

### LSB Certification

Refer to [LSB Certification](https://www.linuxbase.org/lsb-cert/welcome_cert.php) for detail information about LSB certification. In that website, you can track the industry picture of LSB certification in **Product Directory** area. For instance, a list of Linux distributions and applications certified for compliance with the LSB standard can be found [here](https://www.linuxbase.org/lsb-cert/productdir.php?by_prod).

## Linux kernel Releases

The Linux kernel is the most important part of the Linux system. You get Linux kernel on official site [The Linux Kernel Archives](https://www.kernel.org/). [Here](https://en.wikipedia.org/wiki/History_of_Linux) is a short history of Linux kernel:

| kernel version | Release date |  Status  |
| :------------: | :----------: | :------: |
| 0.01           | Sep 17, 1991 |          |
| 0.10           | Nov 1991     |          |
| 0.95           | Mar 08, 1992 |          |
| 1.0            | Mar 14, 1994 |          |
| 1.1            | Apr 06, 1994 |          |
| 1.2            | Mar 07, 1995 |          |
| 1.3            | Jun 12, 1995 |          |
| pre2.0         | May 12, 1996 |          |
| 2.0            | Jun 09, 1996 |          |
| 2.2            | Jan 26, 1999 |          |
| 2.4            | Jan 04, 2001 |          |
| 2.6            | Dec 17, 2003 |          |
| 2.6.11         | Mar 02, 2005 |          |
| 2.6.12         | Jun 18, 2005 |          |
| 2.6.13         | Aug 28, 2005 |          |
| 2.6.14         | Oct 27, 2005 |          |
| 2.6.15         | Jan 02, 2006 |          |
| 2.6.16         | Mar 20, 2006 |          |
| 2.6.17         | Jun 17, 2006 |          |
| 2.6.18         | Sep 20, 2006 |          |
| 2.6.19         | Nov 26, 2006 |          |
| 2.6.20         | Feb 04, 2007 |          |
| 2.6.21         | Apr 25, 2007 |          |
| 2.6.22         | Jul 08, 2007 |          |
| 2.6.23         | Oct 09, 2007 |          |
| 2.6.24         | Jan 24, 2008 |          |
| 2.6.25         | Apr 16, 2008 |          |
| 2.6.26         | Jul 13, 2008 |          |
| 2.6.27         | Oct 09, 2008 |          |
| 2.6.28         | Dec 12, 2008 |          |
| 2.6.29         | Mar 23, 2009 |          |
| 2.6.30         | Jun 09, 2009 |          |
| 2.6.31         | Sep 09, 2009 |          |
| 2.6.32         | Dec 02, 2009 | longterm |
| 2.6.33         | Feb 24, 2010 |          |
| 2.6.34         | May 16, 2010 |          |
| 2.6.35         | Aug 01, 2010 |          |
| 2.6.36         | Oct 20, 2010 |          |
| 2.6.37         | Jan 04, 2011 |          |
| 2.6.38         | Mar 14, 2011 |          |
| 2.6.39         | May 18, 2011 |          |
| 3.0            | Jul 21, 2011 |          |
| 3.1            | Oct 24, 2011 |          |
| 3.2            | Jan 04, 2012 | longterm |
| 3.3            | Mar 18, 2012 |          |
| 3.4            | May 20, 2012 | longterm |
| 3.5            | Jul 21, 2012 |          |
| 3.6            | Sep 30, 2012 |          |
| 3.7            | Dec 10, 2012 |          |
| 3.8            | Feb 18, 2013 |          |
| 3.9            | Apr 28, 2013 |          |
| 3.10           | Jun 30, 2013 | longterm |
| 3.11           | Sep 02, 2013 |          |
| 3.12           | Nov 03, 2013 | longterm |
| 3.13           | Jan 19, 2014 |          |
| 3.14           | Mar 30, 2014 | longterm |
| 3.15           | Jun 08, 2014 |          |
| 3.16           | Aug 03, 2014 |          |
| 3.17           | Oct 05, 2014 |          |
| 3.18           | Dec 07, 2014 | longterm |
| 3.19           | Feb 08, 2015 |          |
| 4.0            | Apr 12, 2015 |          |
| 4.1            | Jun 22, 2015 | longterm |
| 4.2            | Aug 30, 2015 | stable   |
| 4.3            | Nov 01, 2015 | stable   |
| 4.4            | Dec 06, 2015 | mainline |

<br>

If we draw a picture of Linux kernel releases, it should be like this:

![Linux_Kernel_Releases](/assets/Linux_Kernel_Releases_20151114_without_linux-next.svg)

### Version Numbering

[Linux kernel version numbering](https://en.wikipedia.org/wiki/Linux_kernel#Version_numbering)

# Reference

[The Linux Kernel Archives](https://www.kernel.org/)
