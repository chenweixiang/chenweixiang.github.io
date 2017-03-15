---
layout: post
title: "Linux: C/C++ Libraries"
tag: Linux
toc: true
---

This article introduces C standard library and its implementations on Linux system.

<!--more-->

# C Standards

Refer to <a href="{{ site.base-url }}/2016/07/08/c.html#c-standards">C Standards</a>.

# C++ Standards

Refer to <a href="{{ site.base-url }}/2016/07/10/c++.html#c-standards">C++ Standards</a>.

# Online References of C/C++ Language & Libraries

The online references of C/C++ language & libraries can be found on website:

* [CppReference.com Home Page](http://en.cppreference.com/w/c)
* [C Reference on CppReference.com](http://en.cppreference.com/w/c)
* [C++ Reference on CppReference.com](http://en.cppreference.com/w/cpp)

Also, you can download the offline archives from website:

* [Archives for offline viewing](http://en.cppreference.com/w/Cppreference:Archives)

## C Standard Library header files

The C Standard Library header files are listed in following table. It also can be found [here on CppReference.com](http://en.cppreference.com/w/c/header).

| C_Headers             | Since_Standard | Note |
| :-------------------- | :------------: | :--- |
| \<**assert.h**\>      |                | Conditionally compiled macro that compares its argument to zero |
| \<**complex.h**\>     | since **C99**  | Complex number arithmetic |
| \<**ctype.h**\>       |                | Functions to determine the type contained in character data |
| \<**errno.h**\>       |                | Macros reporting error conditions
| \<**fenv.h**\>        | since **C99**  | Floating-point environment |
| \<**float.h**\>       |                | Limits of float types |
| \<**inttypes.h**\>    | since **C99**  | Format conversion of integer types |
| \<**iso646.h**\>      | since **C95**  | Alternative operator spellings |
| \<**limits.h**\>      |                | Sizes of basic types |
| \<**locale.h**\>      |                | Localization utilities |
| \<**math.h**\>        |                | Common mathematics functions |
| \<**setjmp.h**\>      |                | Nonlocal jumps |
| \<**signal.h**\>      |                | Signal handling |
| \<**stdalign.h**\>    | since **C11**  | alignas and alignof convenience macros |
| \<**stdarg.h**\>      |                | Variable arguments |
| \<**stdatomic.h**\>   | since **C11**  | Atomic types |
| \<**stdbool.h**\>     | since **C99**  | Boolean type |
| \<**stddef.h**\>      |                | Common macro definitions |
| \<**stdint.h**\>      | since **C99**  | Fixed-width integer types |
| \<**stdio.h**\>       |                | Input/output |
| \<**stdlib.h**\>      |                | General utilities: memory management, program utilities, string conversions, random numbers |
| \<**stdnoreturn.h**\> | since **C11**  | noreturn convenience macros |
| \<**string.h**\>      |                | String handling |
| \<**tgmath.h**\>      | since **C99**  | Type-generic math (macros wrapping **math.h** and **complex.h** |
| \<**threads.h**\>     | since **C11**  | Thread library |
| \<**time.h**\>        |                | Time/date utilities |
| \<**uchar.h**\>       | since **C11**  | UTF-16 and UTF-32 character utilities |
| \<**wchar.h**\>       | since **C95**  | Extended multibyte and wide character utilities |
| \<**wctype.h**\>      | since **C95**  | Wide character classification and mapping utilities |

## C++ Standard Library header files

The C++ Standard Library header files can be found [here on CppReference.com](http://en.cppreference.com/w/cpp/header).

# GNU Compiler Collection (GCC)

## GCC Releases

Refer to [GCC Releases](https://gcc.gnu.org/releases.html) for more details.

## Content of GCC 4.8.4

The Linux From Scratch (LFS) introduces the [installation of GCC and its content](http://www.linuxfromscratch.org/lfs/view/stable/chapter06/gcc.html).

The GCC 4.8.4 installs the following programs:

| Programs         | Description |
| :--------------- | :---------- |
| ```cpp```        | The C preprocessor; it is used by the compiler to expand the ```#include```, ```#define```, and similar statements in the source files. <br>```/usr/bin/cpp -> /usr/bin/cpp-4.8``` |
| ```gcc```        | The C compiler. <br>```/usr/bin/gcc -> /usr/bin/gcc-4.8``` |
| ```cc```         | The C compiler. <br>```/usr/bin/cc -> /etc/alternatives/cc -> /usr/bin/gcc -> /usr/bin/gcc-4.8``` |
| ```g++```        | The C++ compiler. <br>```/usr/bin/g++ -> /usr/bin/g++-4.8``` |
| ```c++```        | The C++ compiler. <br>```/usr/bin/c++ -> /etc/alternatives/c++ -> /usr/bin/g++ -> /usr/bin/g++-4.8``` |
| ```gcc-ar```     | A wrapper around ```ar``` that adds a plugin to the command line. This program is only used to add ***link time optization*** and is not useful with the default build options. <br>```/usr/bin/ar```<br>```/usr/bin/gcc-ar -> /usr/bin/gcc-ar-4.8``` |
| ```gcc-nm```     | A wrapper around ```nm``` that adds a plugin to the command line. This program is only used to add ***link time optization*** and is not useful with the default build options. <br>```/usr/bin/nm```<br>```/usr/bin/gcc-nm -> /usr/bin/gcc-nm-4.8``` |
| ```gcc-ranlib``` | A wrapper around ```ranlib``` that adds a plugin to the command line. This program is only used to add ***link time optization*** and is not useful with the default build options. <br>```/usr/bin/ranlib```<br>```/usr/bin/gcc-ranlib -> /usr/bin/gcc-ranlib-4.8``` |
| ```gcov```       | A coverage testing tool; it is used to analyze programs to determine where optimizations will have the most effect. <br>```/usr/bin/gcov -> /usr/bin/gcov-4.8``` |

<p/>

The GCC 4.8.4 installs the following libraries:

| Libraries                | Description |
| :----------------------- | :---------- |
| ```libasan.{a,so}```     | The Address Sanitizer runtime library. <br><br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libasan.a```<br><br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libasan.so -> /usr/lib/x86_64-linux-gnu/libasan.so.0 -> /usr/lib/x86_64-linux-gnu/libasan.so.0.0.0``` |
| ```libatomic.{a,so}```   | ```/usr/lib/gcc/x86_64-linux-gnu/4.8/libatomic.a```<br><br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libatomic.so -> /usr/lib/x86_64-linux-gnu/libatomic.so.1 -> /usr/lib/x86_64-linux-gnu/libatomic.so.1.0.0``` |
| ```libgcc.a```           | Contains run-time support for ```gcc```. <br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libgcc.a```<br>```/usr/lib/gcc-cross/arm-linux-gnueabi/4.7/libgcc.a``` |
| ```libgcc_eh.a```        | Contains EH support routines for ```gcc```. <br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libgcc_eh.a```<br>```/usr/lib/gcc-cross/arm-linux-gnueabi/4.7/libgcc_eh.a``` |
| ```libgcc_s.so```        | Contains Support routines for ```gcc```, including EH. <br><br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libgcc_s.so -> /lib/x86_64-linux-gnu/libgcc_s.so.1```<br><br>```/usr/lib/gcc-cross/arm-linux-gnueabi/4.7/libgcc_s.so```<br><br>```/usr/lib/gcc-cross/arm-linux-gnueabi/4.7/libgcc_s.so.1 -> /usr/arm-linux-gnueabi/lib/libgcc_s.so.1``` |
| ```libgcov.a```          | This library is linked in to a program when GCC is instructed to enable profiling. <br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libgcov.a```<br>```/usr/lib/gcc-cross/arm-linux-gnueabi/4.7/libgcov.a``` |
| ```libgomp.{a,so}```     | GNU implementation of the OpenMP API for multi-platform shared-memory parallel programming in C/C++ and Fortran. <br><br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libgomp.a```<br>```/usr/lib/gcc-cross/arm-linux-gnueabi/4.7/libgomp.a```<br><br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libgomp.so -> /usr/lib/x86_64-linux-gnu/libgomp.so.1 -> /usr/lib/x86_64-linux-gnu/libgomp.so.1.0.0```<br><br>```/usr/lib/gcc-cross/arm-linux-gnueabi/4.7/libgomp.so -> /usr/arm-linux-gnueabi/lib/libgomp.so.1 -> /usr/arm-linux-gnueabi/lib/libgomp.so.1.0.0``` |
| ```libiberty.a```        | Contains routines used by various GNU programs, including ```getopt```, ```obstack```, ```strerror```, ```strtol```, and ```strtoul```. |
| ```libitm.{a,so}```      | ```/usr/lib/gcc/x86_64-linux-gnu/4.8/libitm.a```<br><br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libitm.so -> /usr/lib/x86_64-linux-gnu/libitm.so.1 -> /usr/lib/x86_64-linux-gnu/libitm.so.1.0.0``` |
| ```liblto_plugin.so```   | GCC's Link Time Optimization (LTO) plugin allows GCC to perform optimizations across compilation units. <br><br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/liblto_plugin.so -> /usr/lib/gcc/x86_64-linux-gnu/4.8/liblto_plugin.so.0.0.0```<br><br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/liblto_plugin.so.0 -> /usr/lib/gcc/x86_64-linux-gnu/4.8/liblto_plugin.so.0.0.0```<br><br>```/usr/lib/gcc-cross/arm-linux-gnueabi/4.7/liblto_plugin.so -> /usr/lib/gcc-cross/arm-linux-gnueabi/4.7/liblto_plugin.so.0.0.0```<br><br>```/usr/lib/gcc-cross/arm-linux-gnueabi/4.7/liblto_plugin.so.0 -> /usr/lib/gcc-cross/arm-linux-gnueabi/4.7/liblto_plugin.so.0.0.0``` |
| ```libquadmath.{a,so}``` | GCC Quad Precision Math Library API. <br><br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libquadmath.a```<br><br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libquadmath.so -> /usr/lib/x86_64-linux-gnu/libquadmath.so.0 -> /usr/lib/x86_64-linux-gnu/libquadmath.so.0.0.0``` |
| ```libssp.{a,so}```      | Contains routines supporting GCC's stack-smashing protection functionality. |
| ```libssp_nonshared.a``` | Contains routines supporting GCC's stack-smashing protection functionality. <br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libssp_nonshared.a```<br>```/usr/lib/gcc-cross/arm-linux-gnueabi/4.7/libssp_nonshared.a``` |
| ```libstdc++.{a,so}```   | The standard C++ library. <br><br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libstdc++.a```<br><br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libstdc++.so -> /usr/lib/x86_64-linux-gnu/libstdc++.so.6 -> /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.19```<br><br>```/usr/lib/i386-linux-gnu/libstdc++.so.6 -> /usr/lib/i386-linux-gnu/libstdc++.so.6.0.19```<br><br>```/usr/lib/i386-linux-gnu/libstdc++.so.5 -> /usr/lib/i386-linux-gnu/libstdc++.so.5.0.7``` |
| ```libsupc++.a```        | Provides supporting routines for the C++ programming language. <br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libsupc++.a``` |
| ```libtsan.{a,so}```     | The Thread Sanitizer runtime library. <br><br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libtsan.a```<br><br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libtsan.so -> /usr/lib/x86_64-linux-gnu/libtsan.so.0 -> /usr/lib/x86_64-linux-gnu/libtsan.so.0.0.0``` |

<p/>

Those following directories are created by GCC 4.8.4:

| Directories                  | Subdirectories/Headers |
| :--------------------------- | :--------------------- |
| ```/usr/include/c++```       | Subdirectories:<br>```4.8.4 -> 4.8```<br>```4.8/```<br><br>Headers:<br>```4.8/cstdio```<br>```4.8/cstdlib```<br>```4.8/cstring```<br>```...``` |
| ```/usr/lib/gcc```           | Subdirectories:<br>```x86_64-linux-gnu/```<br>```x86_64-linux-gnu/4.8.4 -> 4.8```<br>```x86_64-linux-gnu/4.8```<br><br>```i686-linux-gnu/```<br>```i686-linux-gnu/4.8.4 -> 4.8```<br>```i686-linux-gnu/4.8```<br><br>Static and shared libraries are located in following subdirectories:  <br>```x86_64-linux-gnu/4.8/```<br>```i686-linux-gnu/4.8/``` |
| ```/usr/libexec/gcc```       | ***NONE***           |
| ```/usr/share/gcc-4.8.4```   | ***NONE***           |

# GNU C Library (glibc)

The [GNU C Library](http://www.gnu.org/software/libc/), commonly known as **glibc**, is the GNU Project's implementation of the C standard library. Despite its name, it now also directly supports C++ (and indirectly other programming languages). Was started in the early 1990s by the **Free Software Foundation (FSF)** for their GNU operating system. Released under the **GNU Lesser General Public License (LGPL)**, **glibc** is free software.

## glibc Releases

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
| **2.3.4** | **Dec 2004** | **Standard for Linux Standard Base (LSB) 3.0** |
| 2.3.5     | Apr 2005     |      |
| 2.3.6     | Nov 2005     |      |
| **2.4**   | **Mar 2006** | **Standard for Linux Standard Base (LSB) 4.0**, initial ```inotify``` support |
| 2.5       | Sep 2006     | Full ```inotify``` support |
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
| **2.22**  | **Aug 2015** | Google Native Client (NaCl) for running on ARMv7-A, Unicode 7.0 |

## glibc Repository

In 2009, glibc was migrated to a [Git repository on Sourceware](https://sourceware.org/glibc/wiki/GlibcGit). You can browse the glibc source code on [gitweb](https://sourceware.org/git/?p=glibc.git). [The Community wiki for GLIBC](https://sourceware.org/glibc/wiki/HomePage) answers questions a user might have when installing and using glibc. And use following command to clone the git repository:

```
chenwx@chenwx ~ $ git clone git://sourceware.org/git/glibc.git
chenwx@chenwx ~ $ cd glibc/
chenwx@chenwx ~/glibc $ git br
* master
chenwx@chenwx ~/glibc $ git tag -l glibc-*
...
glibc-2.20
glibc-2.21
glibc-2.22
```

## Build & Install glibc from source

If you want to build the glibc from source code, you can follow the [Glibc-2.22 on Linux From Scratch (LFS)](http://www.linuxfromscratch.org/lfs/view/stable/chapter06/glibc.html). Also refer to [使用源代码将Glibc升级到2.6](http://www.ibm.com/developerworks/cn/linux/l-cn-glibc-upd/index.html).

The **glibc-2.22** installs following programs:

| Programs             | Description |
| :------------------- | :---------- |
| ```catchsegv```      | Can be used to create a stack trace when a program terminates with a segmentation fault. <br>```/usr/bin/catchsegv``` |
| ```gencat```         | Generates message catalogues. <br>```/usr/bin/gencat``` |
| ```getconf```        | Displays the system configuration values for file system specific variables. <br>```/usr/bin/getconf``` |
| ```getent```         | Gets entries from an administrative database. <br>```/usr/bin/getent``` |
| ```iconv```          | Performs character set conversion. <br>```/usr/bin/iconv``` |
| ```iconvconfig```    | Creates fastloading ```iconv``` module configuration files. <br>```/usr/sbin/iconvconfig``` |
| ```ldconfig```       | Configures the dynamic linker runtime bindings. <br>```/sbin/ldconfig``` |
| ```ldd```            | Reports which shared libraries are required by each given program or shared library. <br>```/usr/bin/ldd``` |
| ```lddlibc4```       | Assists ```ldd``` with object files. <br>```/usr/bin/lddlibc4``` |
| ```locale```         | Prints various information about the current locale. <br>```/usr/bin/locale``` |
| ```localedef```      | Compiles locale specifications. <br>```/usr/bin/localedef``` |
| ```makedb```         | Creates a simple database from textual input. <br>```/usr/bin/makedb``` |
| ```mtrace```         | Reads and interprets a memory trace file and displays a summary in human-readable format. <br>```/usr/bin/mtrace``` |
| ```nscd```           | A daemon that provides a cache for the most common name service requests. <br>```/usr/sbin/nscd``` |
| ```pcprofiledump```  | Dumps information generated by PC profiling. <br>```/usr/bin/pcprofiledump``` |
| ```pldd```           | Lists dynamic shared objects used by running processes. <br>```/usr/bin/pldd``` |
| ```rpcgen```         | Generates C code to implement the Remote Procedure Call (RPC) protocol. <br>```/usr/bin/rpcgen``` |
| ```sln```            | A statically linked ```ln``` program. <br>```/usr/bin/sln``` |
| ```sotruss```        | Traces shared library procedure calls of a specified command. <br>```/usr/bin/sotruss``` |
| ```sprof```          | Reads and displays shared object profiling data. <br>```/usr/bin/sprof``` |
| ```tzselect```       | Asks the user about the location of the system and reports the corresponding time zone description. <br>```/usr/bin/tzselect``` |
| ```xtrace```         | Traces the execution of a program by printing the currently executed function. <br>```/usr/bin/xtrace``` |
| ```zdump```          | The time zone dumper. <br>```/usr/bin/zdump``` |
| ```zic```            | The time zone compiler. <br>```/usr/sbin/zic``` |

<p/>

The **glibc-2.19** installs following libraries:

| Libraries | Description |
| :-------- | :---------- |
| ```ld-2.19.so``` | The helper program for shared library executables. Run command ```man ld.so``` for more details. <br><br>```/lib64/ld-linux-x86-64.so.2 -> /lib/x86_64-linux-gnu/ld-2.19.so```<br><br>```/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 -> /lib/x86_64-linux-gnu/ld-2.19.so```<br><br>```/lib/ld-linux.so.2 -> /lib/i386-linux-gnu/ld-2.19.so```<br><br>```/lib/i386-linux-gnu/ld-linux.so.2 -> /lib/i386-linux-gnu/ld-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/ld-linux.so.3 -> /usr/arm-linux-gnueabi/lib/ld-2.19.so``` |
| ```libBrokenLocale.{a,so}``` | Used internally by Glibc as a gross hack to get broken programs (e.g., some Motif applications) running. See comments in ```glibc-2.19/locale/broken_cur_max.c``` for more information. <br><br>```/usr/lib/x86_64-linux-gnu/libBrokenLocale.a```<br><br>```/usr/lib/x86_64-linux-gnu/libBrokenLocale.so -> /lib/x86_64-linux-gnu/libBrokenLocale.so.1 -> /lib/x86_64-linux-gnu/libBrokenLocale-2.19.so```<br><br>```/lib/i386-linux-gnu/libBrokenLocale.so.1 -> /lib/i386-linux-gnu/libBrokenLocale-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/libBrokenLocale.so.1 -> /usr/arm-linux-gnueabi/lib/libBrokenLocale-2.19.so``` |
| ```libSegFault.so``` | The segmentation fault signal handler, used by ```catchsegv```. <br>```/lib/x86_64-linux-gnu/libSegFault.so```<br>```/lib/i386-linux-gnu/libSegFault.so```<br>```/usr/arm-linux-gnueabi/lib/libSegFault.so``` |
| ```libanl.{a,so}``` | An asynchronous name lookup library. <br><br>```/usr/lib/x86_64-linux-gnu/libanl.a```<br><br>```/usr/lib/x86_64-linux-gnu/libanl.so -> /lib/x86_64-linux-gnu/libanl.so.1 -> /lib/x86_64-linux-gnu/libanl-2.19.so```<br><br>```/lib/i386-linux-gnu/libanl.so.1 -> /lib/i386-linux-gnu/libanl-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/libanl.so.1 -> /usr/arm-linux-gnueabi/lib/libanl-2.19.so``` |
| ```libc.{a,so}``` | The main C library. <br><br>```/usr/lib/x86_64-linux-gnu/libc.a```<br>```/usr/lib/x86_64-linux-gnu/libc.so```<br><br>```/lib/x86_64-linux-gnu/libc.so.6 -> /lib/x86_64-linux-gnu/libc-2.19.so```<br><br>```/lib/i386-linux-gnu/libc.so.6 -> /lib/i386-linux-gnu/libc-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/libc.so.6 -> /usr/arm-linux-gnueabi/lib/libc-2.19.so``` |
| ```libc_nonshared.a``` | ```/usr/lib/x86_64-linux-gnu/libc_nonshared.a``` |
| ```libcidn.so``` | Used internally by Glibc for handling internationalized domain names in the ```getaddrinfo()``` function. <br><br>```/usr/lib/x86_64-linux-gnu/libcidn.so -> /lib/x86_64-linux-gnu/libcidn.so.1 -> /lib/x86_64-linux-gnu/libcidn-2.19.so```<br><br>```/lib/i386-linux-gnu/libcidn.so.1 -> /lib/i386-linux-gnu/libcidn-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/libcidn.so.1 -> /usr/arm-linux-gnueabi/lib/libcidn-2.19.so``` |
| ```libcrypt.{a,so}``` | The cryptography library. <br><br>```/usr/lib/x86_64-linux-gnu/libcrypt.a```<br><br>```/usr/lib/x86_64-linux-gnu/libcrypt.so -> /lib/x86_64-linux-gnu/libcrypt.so.1 -> /lib/x86_64-linux-gnu/libcrypt-2.19.so```<br><br>```/lib/i386-linux-gnu/libcrypt.so.1 -> /lib/i386-linux-gnu/libcrypt-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/libcrypt.so.1 -> /usr/arm-linux-gnueabi/lib/libcrypt-2.19.so``` |
| ```libdl.{a,so}``` | The dynamic linking interface library. <br><br>```/usr/lib/x86_64-linux-gnu/libdl.a```<br><br>```/usr/lib/x86_64-linux-gnu/libdl.so -> /lib/x86_64-linux-gnu/libdl.so.2 -> /lib/x86_64-linux-gnu/libdl-2.19.so```<br><br>```/lib/i386-linux-gnu/libdl.so.2 -> /lib/i386-linux-gnu/libdl-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/libdl.so.2 -> /usr/arm-linux-gnueabi/lib/libdl-2.19.so``` |
| ```libg.a``` | Dummy library containing no functions. Previously was a runtime library for ```g++```. <br>```/usr/lib/x86_64-linux-gnu/libg.a``` |
| ```libieee.a``` | Linking in this module forces error handling rules for math functions as defined by the Institute of Electrical and Electronic Engineers (IEEE). The default is **POSIX.1** error handling. <br>```/usr/lib/x86_64-linux-gnu/libieee.a``` |
| ```libm.{a,so}``` | The mathematical library. <br><br>```/usr/lib/x86_64-linux-gnu/libm.a```<br><br>```/usr/lib/x86_64-linux-gnu/libm.so -> /lib/x86_64-linux-gnu/libm.so.6 -> /lib/x86_64-linux-gnu/libm-2.19.so```<br><br>```/lib/i386-linux-gnu/libm.so.6 -> /lib/i386-linux-gnu/libm-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/libm.so.6 -> /usr/arm-linux-gnueabi/lib/libm-2.19.so``` |
| ```libmcheck.a``` | Turns on memory allocation checking when linked to. <br>```/usr/lib/x86_64-linux-gnu/libmcheck.a``` |
| ```libmemusage.so``` | Used by ```memusage``` to help collect information about the memory usage of a program. <br>```/lib/x86_64-linux-gnu/libmemusage.so```<br>```/lib/i386-linux-gnu/libmemusage.so```<br>```/usr/arm-linux-gnueabi/lib/libmemusage.so``` |
| ```libnsl.{a,so}``` | The network services library. <br><br>```/usr/lib/x86_64-linux-gnu/libnsl.a```<br><br>```/usr/lib/x86_64-linux-gnu/libnsl.so -> /lib/x86_64-linux-gnu/libnsl.so.1 -> /lib/x86_64-linux-gnu/libnsl-2.19.so```<br><br>```/lib/i386-linux-gnu/libnsl.so.1 -> /lib/i386-linux-gnu/libnsl-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/libnsl.so.1 -> /usr/arm-linux-gnueabi/lib/libnsl-2.19.so``` |
| ```libnss_compat.so``` | The Name Service Switch (NSS) libraries, containing functions for resolving host names, user names, group names, aliases, services, protocols, etc. <br><br>```/usr/lib/x86_64-linux-gnu/libnss_compat.so -> /lib/x86_64-linux-gnu/libnss_compat.so.2 -> /lib/x86_64-linux-gnu/libnss_compat-2.19.so```<br><br>```/lib/i386-linux-gnu/libnss_compat.so.2 -> /lib/i386-linux-gnu/libnss_compat-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/libnss_compat.so.2 -> /usr/arm-linux-gnueabi/lib/libnss_compat-2.19.so``` |
| ```libnss_dns.so``` | The Name Service Switch (NSS) libraries, containing functions for resolving host names, user names, group names, aliases, services, protocols, etc. <br><br>```/usr/lib/x86_64-linux-gnu/libnss_dns.so -> /lib/x86_64-linux-gnu/libnss_dns.so.2 -> /lib/x86_64-linux-gnu/libnss_dns-2.19.so```<br><br>```/lib/i386-linux-gnu/libnss_dns.so.2 -> /lib/i386-linux-gnu/libnss_dns-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/libnss_dns.so.2 -> /usr/arm-linux-gnueabi/lib/libnss_dns-2.19.so``` |
| ```libnss_files.so``` | The Name Service Switch (NSS) libraries, containing functions for resolving host names, user names, group names, aliases, services, protocols, etc. <br><br>```/usr/lib/x86_64-linux-gnu/libnss_files.so -> /lib/x86_64-linux-gnu/libnss_files.so.2 -> /lib/x86_64-linux-gnu/libnss_files-2.19.so```<br><br>```/lib/i386-linux-gnu/libnss_files.so.2 -> /lib/i386-linux-gnu/libnss_files-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/libnss_files.so.2 -> /usr/arm-linux-gnueabi/lib/libnss_files-2.19.so``` |
| ```libnss_hesiod.so``` | The Name Service Switch (NSS) libraries, containing functions for resolving host names, user names, group names, aliases, services, protocols, etc. <br><br>```/usr/lib/x86_64-linux-gnu/libnss_hesiod.so -> /lib/x86_64-linux-gnu/libnss_hesiod.so.2 -> /lib/x86_64-linux-gnu/libnss_hesiod-2.19.so```<br><br>```/lib/i386-linux-gnu/libnss_hesiod.so.2 -> /lib/i386-linux-gnu/libnss_hesiod-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/libnss_hesiod.so.2 -> /usr/arm-linux-gnueabi/lib/libnss_hesiod-2.19.so``` |
| ```libnss_nis.so``` | The Name Service Switch (NSS) libraries, containing functions for resolving host names, user names, group names, aliases, services, protocols, etc. <br><br>```/usr/lib/x86_64-linux-gnu/libnss_nis.so -> /lib/x86_64-linux-gnu/libnss_nis.so.2 -> /lib/x86_64-linux-gnu/libnss_nis-2.19.so```<br><br>```/lib/i386-linux-gnu/libnss_nis.so.2 -> /lib/i386-linux-gnu/libnss_nis-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/libnss_nis.so.2 -> /usr/arm-linux-gnueabi/lib/libnss_nis-2.19.so``` |
| ```libnss_nisplus.so``` | The Name Service Switch (NSS) libraries, containing functions for resolving host names, user names, group names, aliases, services, protocols, etc. <br><br>```/usr/lib/x86_64-linux-gnu/libnss_nisplus.so -> /lib/x86_64-linux-gnu/libnss_nisplus.so.2 -> /lib/x86_64-linux-gnu/libnss_nisplus-2.19.so```<br><br>```/lib/i386-linux-gnu/libnss_nisplus.so.2 -> /lib/i386-linux-gnu/libnss_nisplus-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/libnss_nisplus.so.2 -> /usr/arm-linux-gnueabi/lib/libnss_nisplus-2.19.so``` |
| ```libpcprofile.so``` | Contains profiling functions used to track the amount of CPU time spent in specific source code lines. <br>```/lib/x86_64-linux-gnu/libpcprofile.so```<br>```/lib/i386-linux-gnu/libpcprofile.so```<br>```/usr/arm-linux-gnueabi/lib/libpcprofile.so``` |
| ```libpthread.{a,so}``` | The POSIX threads library. <br><br>```/usr/lib/x86_64-linux-gnu/libpthread.a```<br>```/usr/lib/x86_64-linux-gnu/libpthread.so```<br><br>```/lib/x86_64-linux-gnu/libpthread.so.0 -> /lib/x86_64-linux-gnu/libpthread-2.19.so```<br><br>```/lib/i386-linux-gnu/libpthread.so.0 -> /lib/i386-linux-gnu/libpthread-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/libpthread.so.0 -> /usr/arm-linux-gnueabi/lib/libpthread-2.19.so``` |
| ```libpthread_nonshared.a``` | The POSIX threads library. <br>```/usr/lib/x86_64-linux-gnu/libpthread_nonshared.a``` |
| ```libresolv.{a,so}``` | Contains functions for creating, sending, and interpreting packets to the Internet domain name servers. <br><br>```/usr/lib/x86_64-linux-gnu/libresolv.a```<br><br>```/usr/lib/x86_64-linux-gnu/libresolv.so -> /lib/x86_64-linux-gnu/libresolv.so.2 -> /lib/x86_64-linux-gnu/libresolv-2.19.so```<br><br>```/lib/i386-linux-gnu/libresolv.so.2 -> /lib/i386-linux-gnu/libresolv-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/libresolv.so.2 -> /usr/arm-linux-gnueabi/lib/libresolv-2.19.so``` |
| ```librpcsvc.a``` | Contains functions providing miscellaneous RPC services. <br>```/usr/lib/x86_64-linux-gnu/librpcsvc.a``` |
| ```librt.{a,so}``` | Contains functions providing most of the interfaces specified by the POSIX.1b Realtime Extension. <br><br>```/usr/lib/x86_64-linux-gnu/librt.a```<br><br>```/usr/lib/x86_64-linux-gnu/librt.so -> /lib/x86_64-linux-gnu/librt.so.1 -> /lib/x86_64-linux-gnu/librt-2.19.so```<br><br>```/lib/i386-linux-gnu/librt.so.1 -> /lib/i386-linux-gnu/librt-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/librt.so.1 -> /usr/arm-linux-gnueabi/lib/librt-2.19.so``` |
| ```libthread_db.so``` | Contains functions useful for building debuggers for multi-threaded programs. <br><br>```/usr/lib/x86_64-linux-gnu/libthread_db.so -> /lib/x86_64-linux-gnu/libthread_db.so.1 -> /lib/x86_64-linux-gnu/libthread_db-1.0.so```<br><br>```/lib/i386-linux-gnu/libthread_db.so.1 -> /lib/i386-linux-gnu/libthread_db-1.0.so```<br><br>```/usr/arm-linux-gnueabi/lib/libthread_db.so.1 -> /usr/arm-linux-gnueabi/lib/libthread_db-1.0.so``` |
| ```libutil.{a,so}``` | Contains code for ***standard*** functions used in many different Unix utilities. <br><br>```/usr/lib/x86_64-linux-gnu/libutil.a```<br><br>```/usr/lib/x86_64-linux-gnu/libutil.so -> /lib/x86_64-linux-gnu/libutil.so.1 -> /lib/x86_64-linux-gnu/libutil-2.19.so```<br><br>```/lib/i386-linux-gnu/libutil.so.1 -> /lib/i386-linux-gnu/libutil-2.19.so```<br><br>```/usr/arm-linux-gnueabi/lib/libutil.so.1 -> /usr/arm-linux-gnueabi/lib/libutil-2.19.so``` |

<p/>

Those following directories are created by glibc:

| Directories                  | Files/Subdirectories | Description |
| :--------------------------- | :------------------- | :---------- |
| ```/usr/include/arpa```      | ```ftp.hftp.h```<br>```inet.h```<br>```nameser.h```<br>```nameser_compat.h```<br>```telnet.h```<br>```tftp.h``` | |
| ```/usr/include/bits```      |             | |
| ```/usr/include/gnu```       |             | |
| ```/usr/include/net```       | ```ethernet.h```<br>```if.h```<br>```if_arp.h```<br>```if_packet.h```<br>```if_ppp.h```<br>```if_shaper.h```<br>```if_slip.h```<br>```ppp-comp.h```<br>```ppp_defs.h```<br>```route.h``` | |
| ```/usr/include/netash```    | ```ash.h``` | |
| ```/usr/include/netatalk```  | ```at.h```  | |
| ```/usr/include/netax25```   | ```ax25.h``` | |
| ```/usr/include/neteconet``` | ```ec.h```  | |
| ```/usr/include/netinet```   | ```ether.h```<br>```icmp6.h```<br>```if_ether.h```<br>```if_fddi.h```<br>```if_tr.h```<br>```igmp.h```<br>```in.h```<br>```in_systm.h```<br>```ip.h```<br>```ip6.h```<br>```ip_icmp.h```<br>```tcp.h```<br>```udp.h``` | |
| ```/usr/include/netipx```    | ```ipx.h``` | |
| ```/usr/include/netiucv```   | ```iucv.h``` | |
| ```/usr/include/netpacket``` | ```packet.h``` | |
| ```/usr/include/netrom```    | ```netrom.h``` | |
| ```/usr/include/netrose```   | ```rose.h``` | |
| ```/usr/include/nfs```       | ```nfs.h``` | |
| ```/usr/include/protocols``` | ```routed.h```<br>```rwhod.h```<br>```talkd.h```<br>```timed.h``` | |
| ```/usr/include/rpc```       | ```auth.h```<br>```auth_des.h```<br>```auth_unix.h```<br>```clnt.h```<br>```des_crypt.h```<br>```key_prot.h```<br>```netdb.h```<br>```pmap_clnt.h```<br>```pmap_prot.h```<br>```pmap_rmt.h```<br>```rpc.h```<br>```rpc_des.h```<br>```rpc_msg.h```<br>```svc.h```<br>```svc_auth.h```<br>```types.h```<br>```xdr.h``` | |
| ```/usr/include/rpcsvc```    | ```bootparam.h```<br>```bootparam_prot.h```<br>```bootparam_prot.x```<br>```key_prot.h```<br>```key_prot.x```<br>```klm_prot.h```<br>```klm_prot.x```<br>```mount.h```<br>```mount.x```<br>```nfs_prot.h```<br>```nfs_prot.x```<br>```nis.h```<br>```nis.x```<br>```nis_callback.h```<br>```nis_callback.x```<br>```nis_object.x```<br>```nis_tags.h```<br>```nislib.h```<br>```nlm_prot.h```<br>```nlm_prot.x```<br>```rex.h```<br>```rex.x```<br>```rquota.h```<br>```rquota.x```<br>```rstat.h```<br>```rstat.x```<br>```rusers.h```<br>```rusers.x```<br>```sm_inter.h```<br>```sm_inter.x```<br>```spray.h```<br>```spray.x```<br>```yp.h```<br>```yp.x```<br>```yp_prot.h```<br>```ypclnt.h```<br>```yppasswd.h```<br>```yppasswd.x```<br>```ypupd.h``` | |
| ```/usr/include/sys```       | ```asoundlib.h``` | |
| ```/usr/lib/audit```         |             | |
| ```/usr/lib/gconv```         |             | |
| ```/usr/lib/locale```        | ```locale-archive```<br>```C.UTF-8/``` |
| ```/usr/libexec/getconf```   |             | |
| ```/usr/share/i18n```        | ```SUPPORTED```<br>```charmaps/```<br>```locales/``` | |
| ```/usr/share/zoneinfo```    |             | |
| ```/var/cache/nscd```        |             | |
| ```/var/lib/nss_db```        |             | |

<p/>

# C Standard Library for Embedded System (newlib)

## What's newlib?

[**Newlib**](http://sourceware.org/newlib/) is a C library intended for use on embedded systems. It is a conglomeration of several library parts, all under free software licenses that make them easily usable on embedded products.

Newlib is only available in source form. It can be compiled for a wide array of processors, and will usually work on any architecture with the addition of a few low-level routines.

Newlib can be downloaded from [ftp directory](ftp://sourceware.org/pub/newlib/index.html) or accessed by [web-based GIT](https://sourceware.org/git/gitweb.cgi?p=newlib-cygwin.git).

## newlib Repository

```
chenwx@chenwx ~ $ git clone git://sourceware.org/git/newlib-cygwin.git
```

# GNU C++ Library (libstdc++)

The **GNU Standard C++ Library v3** (**libstdc++-v3**) is an ongoing project to implement the **ISO 14882 Standard C++ library** as described in clauses ***17 through 30*** and ***Annex D***. For those who want to see exactly how far the project has come, or just want the latest bleeding-edge code, the up-to-date source is available over anonymous SVN, and can be browsed over the [web](https://gcc.gnu.org/svn.html). Also refer to following websites for more details:

* [GNU C++ Library](https://gcc.gnu.org/libstdc++/)
* [GNU C++ Library Online Documentation](https://gcc.gnu.org/onlinedocs/libstdc++/)
* [GNU C++ Library API Reference](https://gcc.gnu.org/onlinedocs/libstdc++/api.html)
* [The C++ Runtime Library (libstdc++)](https://gcc.gnu.org/wiki/Libstdc%2B%2B)
* [GNU C++ Library FAQ](https://gcc.gnu.org/onlinedocs/libstdc++/faq.html)

The **glibstdc++** installs following libraries, refer to section ***Content of GCC 4.8.4*** of this article:

| Libraries | Description |
| :-------- | :---------- |
| ```libstdc++.{a,so}``` | ```/usr/lib/gcc/x86_64-linux-gnu/4.8/libstdc++.a```<br><br>```/usr/lib/gcc/x86_64-linux-gnu/4.8/libstdc++.so -> /usr/lib/x86_64-linux-gnu/libstdc++.so.6 -> /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.19```<br><br>```/usr/lib/i386-linux-gnu/libstdc++.so.6 -> /usr/lib/i386-linux-gnu/libstdc++.so.6.0.19```<br><br>```/usr/lib/i386-linux-gnu/libstdc++.so.5 -> /usr/lib/i386-linux-gnu/libstdc++.so.5.0.7``` |

# Static Library (.a)

##  What's static library?

As stated in [wikipedia](https://en.wikipedia.org/wiki/Static_library), a **static library** or **statically-linked library** is a set of routines, external functions and variables which are resolved in a caller at compile-time and copied into a target application by a compiler, linker, or binder, producing an object file and a stand-alone executable. This executable and the process of compiling it are both known as a **static build** of the program. Historically, libraries could only be ***static***. Static libraries are either merged with other static libraries and object files during building/linking to form a single executable, or they may be loaded at run-time into the address space of the loaded executable at a static memory offset determined at compile-time/link-time.

## Advantages and disadvantages

There are several advantages to statically linking libraries with an executable instead of dynamically linking them. The most significant is that the application can be certain that all its libraries are present and that they are the correct version. This avoids dependency problems, known colloquially as [DLL Hell](https://en.wikipedia.org/wiki/DLL_Hell) or more generally [dependency hell](https://en.wikipedia.org/wiki/Dependency_hell). Static linking can also allow the application to be contained in a single executable file, simplifying distribution and installation.

With static linking, it is enough to include those parts of the library that are directly and indirectly referenced by the target executable (or target library). With dynamic libraries, the entire library is loaded, as it is not known in advance which functions will be invoked by applications. Whether this advantage is significant in practice depends on the structure of the library.

In static linking, the size of the executable becomes greater than in dynamic linking, as the library code is stored ***within the executable*** rather than in separate files. But if library files are counted as part of the application then the total size will be similar, or even smaller if the compiler eliminates the unused symbols.

## Creating a Static Library

Static libraries can be easily created in C or C++. These two languages provide storage-class specifiers for indicating external or internal linkage, in addition to providing other features. To create such a library, the exported functions/procedures and other objects variables must be specified for **external linkage** (i.e. by not using the C keyword ***static***). Static library filenames usually have a ***.a*** extension on Unix-like systems and ***.lib*** on Microsoft Windows.

To create a static library, or to add additional object files to an existing static library, use a command like this:

```
chenwx@chenwx ~/helloworld $ cat helloworldlib1.c
#include <stdio.h>

void printHelloWorld()
{
    printf("Hello World!\n");
}

chenwx@chenwx ~/helloworld $ cat helloworldlib2.c
#include <stdio.h>

void printUserName(char *name)
{
    printf("Hello World! %s\n", name);
}

chenwx@chenwx ~/helloworld $ cc -Wall -c -o helloworldlib1.o helloworldlib1.c
chenwx@chenwx ~/helloworld $ cc -Wall -c -o helloworldlib2.o helloworldlib2.c

chenwx@chenwx ~/helloworld $ ar crsv libhelloworld.a helloworldlib1.o helloworldlib2.o
a - helloworldlib1.o
a - helloworldlib2.o
```

**[Historical Note]**
After creating the library it was once necessary to run the command ```ranlib libhelloworld.a``` to create a symbol table within the archive. Now, the ```ranlib``` is embedded into the ```ar``` command.

## List Information of Static Library

```
# Display a table listing the contents of archive
chenwx@chenwx ~/helloworld $ ar -t libhelloworld.a
helloworldlib1.o
helloworldlib2.o

# List symbols from object files
chenwx@chenwx ~/helloworld $ nm libhelloworld.a

helloworldlib1.o:
0000000000000000 T printHelloWorld
                 U puts

helloworldlib2.o:
0000000000000000 T printUserName
                 U printf
```

## Using Static Library

To compile a program that depends on the library ```libhelloworld.a```, one could do:

```
chenwx@chenwx ~/helloworld $ cat testhelloworld.c
int main()
{
    char *userName = "Alex";
    printHelloWorld();
    printUserName(userName);

    return 0;
}

chenwx@chenwx ~/helloworld $ cc -o testhelloworld testhelloworld.c libhelloworld.a
chenwx@chenwx ~/helloworld $ ./testhelloworld
Hello World!
Hello World! Alex
```

or, run the following command if ```libhelloworld.a``` is placed in standard library path, like ```/usr/local/lib```:

```
chenwx@chenwx ~/helloworld $ cc -lhelloworld -o testhelloworld testhelloworld.c
```

or, run the following command if ```libhelloworld.a``` is placed a directory other than standard library path:

```
chenwx@chenwx ~/helloworld $ cc -L/path/to/library-directory -lhelloworld -o testhelloworld testhelloworld.c
```

or, link the libhelloworld.a during linking stage:

```
chenwx@chenwx ~/helloworld $ cc -c -o testhelloworld.o testhelloworld.c
chenwx@chenwx ~/helloworld $ ld -lhelloworld -o testhelloworld testhelloworld.o
```

# Shared Library (.so)

##  What's shared library?

A **shared library** or **shared object** is a file that is intended to be shared by executable files and further shared object files. Modules used by a program are loaded from individual shared objects into memory at load time or run time, rather than being copied by a linker when it creates a single monolithic executable file for the program.

Shared libraries can be statically linked, meaning that references to the library modules are resolved and the modules are allocated memory when the executable file is created. But often linking of shared libraries is postponed until they are loaded.

## Naming Convention of Shared Libraries

Every shared library has a special name called the **soname**. The soname has the prefix ***lib***, the name of the library, the phrase ***.so***, followed by a period and a version number that is incremented whenever the interface changes (as a special exception, the lowest-level C libraries don't start with ***lib***), that's ***lib\<name\>.so.X***. A fully-qualified soname includes as a prefix the directory it's in; on a working system a fully-qualified soname is simply a symbolic link to the shared library's **real name**.

Every shared library also has a **real name**, which is the filename containing the actual library code. The real name adds to the soname a period, a minor number, another period, and the release number, that's ***lib\<name\>.so.X.Y[.Z]***. The last period and release number (***.Z***) are optional. The minor number and release number (***.Y***) support configuration control by letting you know exactly what version(s) of the library are installed. Note that these numbers might not be the same as the numbers used to describe the library in documentation, although that does make things easier.

In addition, there's the name that the compiler uses when requesting a library, **linker name**, which is simply the soname without any version number, that's ***lib\<name\>.so***.

| Type_of_Name | Description |
| :----------: | :---------- |
| Real name | The **real name** is the filename containing the actual shared library code. It has formats:<br>```lib<name>.so.X.Y```<br>```lib<name>.so.X.Y.Z``` |
| **soname** | The **soname** is a symbol link to **real name** of shared library. It has formats: <br>```lib<name>.so.X -> lib<name>.so.X.Y```<br>```lib<name>.so.X -> lib<name>.so.X.Y.Z```<br><br>The **soname** is used by programs depend on it at runtime. It's specified at the library's build-time to GCC's link editor ```ld``` with the ```-soname``` option. You can use following command to check the soname: <br>```objdump -p lib<name>.so.X | grep SONAME```<br>```objdump -p lib<name>.so.X.Y.Z | grep SONAME``` |
| Linker name | The linker name is used by compiler when requesting a library. It has formats:<br>```lib<name>.so```<br>```lib<name>X.so```<br>which link to the real name or **soname** of the shared library:<br>```lib<name>.so -> lib<name>.so.X```<br>```lib<name>.so -> lib<name>.so.X.Y```<br>```lib<name>.so -> lib<name>.so.X.Y.Z```<br>```lib<name>X.so -> lib<name>.so.X.Y.Z```<br><br>After the linker name ```lib<name>.so``` exist, the compiling command works:<br>```cc -l<name> -o <executable> <source>.c``` |

## Advantages and disadvantages

As [this article](http://osr507doc.sco.com/en/tools/ShLib_WhatIs.html) said, a shared library offers several benefits, like:

* **Save disk storage space**

    Shared library code is not copied into all the executable files that use that code. The executable files are smaller and use less disk space.

* **Save memory**

    By sharing library code at run time the dynamic memory needs of the processes are reduced.

* **Easier to maintain**

    Make executable files using library code easier to maintain.

    At run time shared library code is brought into the processes' address space. Therefore, updating a shared library effectively updates all executable files that use the library. If an error in shared library code is fixed, all processes automatically use the corrected code.

    Non-shared libraries cannot offer this benefit: changes to archive libraries do not affect executable files, because code from the libraries is copied to the files during link editing, not during execution.

As [this article](http://www.informit.com/guides/content.aspx?g=cplusplus&seqNum=152) said, the dynamic linking offers several advantages over static linking:

* **Code Sharing**

    With dynamic linking, programs can share identical code instead of owning individual copies of the same library. Think of the standard C or C++ libraries. They are both huge and ubiquitous. Every C or C++ program uses at least a portion of these libraries for I/O, date and time manipulation, memory allocation, string processing, and so on. If distinct copies of these libraries were statically linked into every executable file, even tiny programs would occupy dozens of megabytes.

    Worse yet, whenever a new version of the said libraries is released, every executable file would have to be replaced with a newly-linked executable in order to reflect the change. Fortunately, these libraries are usually implemented as shared dynamic libraries that are loaded into the core program at runtime.

* **Automatic Updates**

    Whenever a new version of a dynamically-linked library is installed, it automatically supercedes the previous version. When you run a program, it automatically picks the most up-to-date version without forcing the user to re-link.

* **Security**

    If you're concerned about protecting your intellectual property, splitting an application into several linkage units makes it harder for crackers to disassemble and decompile an executable file (at least in theory).

## Creating a Shared Library

Use following commands to create a shared library:

```
chenwx@chenwx ~/helloworld $ cat helloworldlib1.c
#include <stdio.h>

void printHelloWorld()
{
    printf("Hello World!\n");
}

chenwx@chenwx ~/helloworld $ cat helloworldlib2.c
#include <stdio.h>

void printUserName(char *name)
{
    printf("Hello World! %s\n", name);
}

chenwx@chenwx ~/helloworld $ cc -Wall -fPIC -c -o helloworldlib1.o helloworldlib1.c
chenwx@chenwx ~/helloworld $ cc -Wall -fPIC -c -o helloworldlib2.o helloworldlib2.c
chenwx@chenwx ~/helloworld $ cc -shared -Wl,-soname,libhelloworld.so.1 -o libhelloworld.so.1.0 helloworldlib1.o helloworldlib2.o

chenwx@chenwx ~/helloworld $ ll libhelloworld.so.1.0
-rwxrwxr-x 1 chenwx chenwx 8.0K Dec 29 20:54 libhelloworld.so.1.0

henwx@chenwx ~/helloworld $ objdump -p libhelloworld.so.1.0 | grep SONAME
  SONAME               libhelloworld.so.1
```

Compiler options:

* ```-Wall``` Include warnings. See man page for warnings specified.
* ```-fPIC``` Compiler directive to output position independent code, a characteristic required by shared libraries. The ```-fPIC``` always works, but may produce larger code than ```-fpic``` (mnenomic to remember this is that PIC is in a larger case, so it may produce larger amounts of code). Using ```-fpic``` option usually generates smaller and faster code, but will have platform-dependent limitations, such as the number of globally visible symbols or the size of the code. The linker will tell you whether it fits when you create the shared library. When in doubt, choose ```-fPIC```, because it always works.
* ```-shared``` Produce a shared object which can then be linked with other objects to form an executable.
* ```-Wl,options``` Pass options to linker.

Here are a few points worth noting:

* Don't strip the resulting library, and don't use the compiler option ```-fomit-frame-pointer``` unless you really have to. The resulting library will work, but these actions make debuggers mostly useless.

* In some cases, the call to ```gcc``` to create the object file will also need to include the option ```-Wl,-export-dynamic```. Normally, the dynamic symbol table contains only symbols which are used by a dynamic object. This option (when creating an ELF file) adds all symbols to the dynamic symbol table (see ```ld(1)``` for more information). You need to use this option when there are ***reverse dependencies***, i.e., a DL library has unresolved symbols that by convention must be defined in the programs that intend to load these libraries. For ***reverse dependencies*** to work, the master program must make its symbols dynamically available. Note that you could say ```-rdynamic``` instead of ```-Wl,export-dynamic``` if you only work with Linux systems, but according to the ELF documentation the ```-rdynamic``` flag doesn't always work for gcc on non-Linux systems.

For more detail about creating shared library, refer to [How to Write Shared Libraries](http://www.akkadia.org/drepper/dsohowto.pdf).

## Installing and Using a Shared Library

### Standard Directory

Once you've created a shared library, you'll want to install it. The simple approach is simply to copy the library into one of the standard directorie, (e.g., ```/lib```, ```/usr/lib``` or ```/usr/local/lib```) and run ```ldconfig```.

First, you need to create the shared libraries somewhere. Then, set up the necessary symbolic links, in particular a link from a **soname** to the real name (as well as from a versionless soname, that is, a soname that ends in ***.so*** for users who don't specify a version at all). The simplest approach is to run:

```
chenwx@chenwx ~/helloworld $ sudo cp libhelloworld.so.1.0 /lib/
[sudo] password for chenwx:

chenwx@chenwx ~/helloworld $ ldconfig -n /lib/
chenwx@chenwx ~/helloworld $ ll /lib/libhelloworld.so*
lrwxrwxrwx 1 root root   20 Dec 30 19:40 /lib/libhelloworld.so.1 -> libhelloworld.so.1.0
-rwxr-xr-x 1 root root 8.0K Dec 29 21:24 /lib/libhelloworld.so.1.0

chenwx@chenwx ~/helloworld $ sudo ln -s /lib/libhelloworld.so.1 /lib/libhelloworld.so
chenwx@chenwx ~/helloworld $ ll /lib/libhelloworld.so*
lrwxrwxrwx 2 root root   20 Dec 30 19:40 /lib/libhelloworld.so -> libhelloworld.so.1.0
lrwxrwxrwx 2 root root   20 Dec 30 19:40 /lib/libhelloworld.so.1 -> libhelloworld.so.1.0
-rwxr-xr-x 1 root root 8.0K Dec 29 21:24 /lib/libhelloworld.so.1.0

chenwx@chenwx ~/helloworld $ sudo ldconfig /lib
chenwx@chenwx ~/helloworld $ ldconfig -p | grep helloworld
	libhelloworld.so.1 (libc6,x86-64) => /lib/libhelloworld.so.1
	libhelloworld.so (libc6,x86-64) => /lib/libhelloworld.so
```

If the shared library is put into standard directory, then you'll need to tell the linker about shared library:

```
chenwx@chenwx ~/helloworld $ cat testhelloworld.c
int main()
{
    char *userName = "Alex";
    printHelloWorld();
    printUserName(userName);

    return 0;
}

chenwx@chenwx ~/helloworld $ cc -o testhelloworld testhelloworld.c -lhelloworld
chenwx@chenwx ~/helloworld $ ll testhelloworld
-rwxrwxr-x 1 chenwx chenwx 8.5K Dec 30 21:12 testhelloworld
chenwx@chenwx ~/Downloads/helloworld $ ./testhelloworld
Hello World!
Hello World! Alex
```

NOTE: **Libraries must be listed after the objects that use them** (more precisely, a library will be used only if it contains a symbol that satisfies an undefined reference known at the time it is encountered). So here the ```-lhelloworld``` is appended after ```cc -o testhelloworld testhelloworld.c```. Otherwise, you'll get following error:

```
chenwx@chenwx ~/helloworld $ cc -lhelloworld -o testhelloworld testhelloworld.c             
/tmp/cccQMBIY.o: In function `main':
testhelloworld.c:(.text+0x16): undefined reference to `printHelloWorld'
testhelloworld.c:(.text+0x27): undefined reference to `printUserName'
collect2: error: ld returned 1 exit status
```

### Non-standard Directory

If you can't or don't want to install a library in a standard place (e.g., you don't have the right to modify ```/lib```, ```/usr/lib``` or ```/usr/local/lib```), then you'll need to change your approach. In that case, you'll need to install it somewhere:

```
chenwx@chenwx ~/helloworld $ mkdir ~/lib
chenwx@chenwx ~/helloworld $ cp libhelloworld.so.1.0 ~/lib/
chenwx@chenwx ~/helloworld $ ln -s ~/lib/libhelloworld.so.1.0 ~/lib/libhelloworld.so.1   
chenwx@chenwx ~/helloworld $ ln -s ~/lib/libhelloworld.so.1.0 ~/lib/libhelloworld.so  
chenwx@chenwx ~/helloworld $ ll ~/lib/
lrwxrwxrwx 1 chenwx chenwx   37 Dec 30 21:29 libhelloworld.so -> /home/chenwx/lib/libhelloworld.so.1.0
lrwxrwxrwx 1 chenwx chenwx   37 Dec 30 21:29 libhelloworld.so.1 -> /home/chenwx/lib/libhelloworld.so.1.0
-rwxrwxr-x 1 chenwx chenwx 8.0K Dec 30 21:28 libhelloworld.so.1.0
```

Then give your program enough information so the program can find the library... and there are several ways to do that. You can use gcc's ```-L``` flag in simple cases:

```
chenwx@chenwx ~/helloworld $ cc -o testhelloworld testhelloworld.c -L/home/chenwx/lib -lhelloworld
chenwx@chenwx ~/helloworld $ ll testhelloworld
-rwxrwxr-x 1 chenwx chenwx 8.5K Dec 30 21:30 testhelloworld
```

Or, you can use the ```rpath``` approach, particularly if you only have a specific program to use the library being placed in a ***non-standard*** place. You can also use environment variables to control things. In particular, you can set ```LD_LIBRARY_PATH```, which is a colon-separated list of directories in which to search for shared libraries before the usual places.

NOTE: ```LD_LIBRARY_PATH``` is handy for development and testing, but shouldn't be modified by an installation process for normal use by normal users. But it's still useful for development or testing, and for working around problems that can't be worked around otherwise. If you don't want to set the ```LD_LIBRARY_PATH``` environment variable, on Linux you can even invoke the program loader directly and pass it arguments. Or use ```--library-path``` instead of it:

```
chenwx@chenwx ~/helloworld $ cc -o testhelloworld testhelloworld.c -Wl,--library-path=/home/chenwx/lib -lhelloworld
chenwx@chenwx ~/helloworld $ ll testhelloworld
-rwxrwxr-x 1 chenwx chenwx 8.5K Dec 30 22:26 testhelloworld
```

If you're using bash, you could invoke *testhelloworld* this way using:

```
chenwx@chenwx ~/helloworld $ LD_LIBRARY_PATH=/home/chenwx/lib:$LD_LIBRARY_PATH ./testhelloworld
Hello World!
Hello World! Alex
```

## Configure the Dynamic Loader

By default, the dynamic loader ```/lib/ld-linux.so.2``` searches through ```/lib``` and ```/usr/lib``` for dynamic libraries that are needed by programs as they are run. However, if there are libraries in directories other than ```/lib``` and ```/usr/lib```, these need to be added to the ```/etc/ld.so.conf``` file in order for the dynamic loader to find them. Two directories that are commonly known to contain additional libraries are ```/usr/local/lib``` and ```/opt/lib```, so add those directories to the dynamic loader's search path.

Here is the configuration of ```/etc/ld.so.conf``` in my computer:

```
chenwx@chenwx ~ $ ll /etc/ld.so.conf
-rw-r--r-- 1 root root 34 Jun 24  2014 /etc/ld.so.conf

chenwx@chenwx ~ $ cat /etc/ld.so.conf   
include /etc/ld.so.conf.d/*.conf

chenwx@chenwx ~ $ ll /etc/ld.so.conf.d/*.conf  
-rw-rw-r-- 1 root root  38 Mar 24  2014 /etc/ld.so.conf.d/fakeroot-x86_64-linux-gnu.conf
lrwxrwxrwx 1 root root  40 Oct 24  2014 /etc/ld.so.conf.d/i386-linux-gnu_GL.conf -> /etc/alternatives/i386-linux-gnu_gl_conf
-rw-r--r-- 1 root root 108 Apr 12  2014 /etc/ld.so.conf.d/i686-linux-gnu.conf
-rw-r--r-- 1 root root  44 Aug 10  2009 /etc/ld.so.conf.d/libc.conf
-rw-r--r-- 1 root root  68 Apr 12  2014 /etc/ld.so.conf.d/x86_64-linux-gnu.conf
lrwxrwxrwx 1 root root  43 Oct 24  2014 /etc/ld.so.conf.d/x86_64-linux-gnu_EGL.conf -> /etc/alternatives/x86_64-linux-gnu_egl_conf
lrwxrwxrwx 1 root root  42 Oct 24  2014 /etc/ld.so.conf.d/x86_64-linux-gnu_GL.conf -> /etc/alternatives/x86_64-linux-gnu_gl_conf

chenwx@chenwx ~ $ cat /etc/ld.so.conf.d/fakeroot-x86_64-linux-gnu.conf
/usr/lib/x86_64-linux-gnu/libfakeroot

chenwx@chenwx ~ $ cat /etc/ld.so.conf.d/libc.conf
# libc default configuration
/usr/local/lib

chenwx@chenwx ~ $ cat /etc/ld.so.conf.d/i686-linux-gnu.conf
# Multiarch support
/lib/i386-linux-gnu
/usr/lib/i386-linux-gnu
/lib/i686-linux-gnu
/usr/lib/i686-linux-gnu

chenwx@chenwx ~ $ cat /etc/ld.so.conf.d/x86_64-linux-gnu.conf
# Multiarch support
/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu

chenwx@chenwx ~ $ cat /etc/alternatives/i386-linux-gnu_gl_conf
/usr/lib/i386-linux-gnu/mesa

chenwx@chenwx ~ $ cat /etc/alternatives/x86_64-linux-gnu_gl_conf
/usr/lib/x86_64-linux-gnu/mesa

chenwx@chenwx ~ $ cat /etc/alternatives/x86_64-linux-gnu_egl_conf
/usr/lib/x86_64-linux-gnu/mesa-egl
```

## Show Shared Library Dependencies

The command ```ldd``` prints the shared libraries required by each program or shared library specified on the command line. For instance:

```
chenwx@chenwx ~ $ ldd /bin/ln
	linux-vdso.so.1 =>  (0x00007ffc51d95000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f686ee19000)
	/lib64/ld-linux-x86-64.so.2 (0x00005606eabc7000)

chenwx@chenwx ~ $ ldd -v /bin/ln
	linux-vdso.so.1 =>  (0x00007ffc68392000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fd2a4ea5000)
	/lib64/ld-linux-x86-64.so.2 (0x0000562c348c3000)

	Version information:
	/bin/ln:
		libc.so.6 (GLIBC_2.3) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.3.4) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.14) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.4) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libc.so.6
	/lib/x86_64-linux-gnu/libc.so.6:
		ld-linux-x86-64.so.2 (GLIBC_2.3) => /lib64/ld-linux-x86-64.so.2
		ld-linux-x86-64.so.2 (GLIBC_PRIVATE) => /lib64/ld-linux-x86-64.so.2
```

or, use a safer alternative when dealing with untrusted executables is:

```
chenwx@chenwx ~ $ objdump -p /bin/ln | grep NEEDED
  NEEDED               libc.so.6
```

Use the following command to list the dynamic share libraries:

```
chenwx@chenwx ~ $ ldconfig -p
1627 libs found in cache `/etc/ld.so.cache'
	libzvbi.so.0 (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/libzvbi.so.0
	libzvbi-chains.so.0 (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/libzvbi-chains.so.0
	libzip.so.2 (libc6,x86-64) => /usr/lib/libzip.so.2
	libzephyr.so.4 (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/libzephyr.so.4
	libzeitgeist-2.0.so.0 (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/libzeitgeist-2.0.so.0
	libzbar.so.0 (libc6,x86-64) => /usr/lib/libzbar.so.0
	libz.so.1 (libc6,x86-64) => /lib/x86_64-linux-gnu/libz.so.1
...

chenwx@chenwx ~ $ ldconfig -p | grep libc.so
	libc.so.6 (libc6,x86-64, OS ABI: Linux 2.6.24) => /lib/x86_64-linux-gnu/libc.so.6
	libc.so.6 (libc6, OS ABI: Linux 2.6.24) => /lib/i386-linux-gnu/libc.so.6

chenwx@chenwx ~ $ ldconfig -p | grep libstdc++.so
	libstdc++.so.6 (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/libstdc++.so.6
	libstdc++.so.6 (libc6) => /usr/lib/i386-linux-gnu/libstdc++.so.6
	libstdc++.so.5 (libc6) => /usr/lib/i386-linux-gnu/libstdc++.so.5
```

# References

* [ISO/IEC 9899 - Programming languages - C](http://www.open-std.org/jtc1/sc22/wg14/www/standards)
* [C programming language on wiki](https://en.wikipedia.org/wiki/C_%28programming_language%29)

* [JTC1/SC22/WG21 - The C++ Standards Committee](http://www.open-std.org/jtc1/sc22/wg21/)
* [C++ programming language on wiki](https://en.wikipedia.org/wiki/C%2B%2B)

* [GNU C Library Wikipedia](https://en.wikipedia.org/wiki/GNU_C_Library)
* [GNU C Library FTP](http://ftp.gnu.org/gnu/libc/)
* [GNU C Library Reporsitory](https://sourceware.org/glibc/wiki/GlibcGit)

* [动态库(.so)](http://linux-wiki.cn/wiki/%E5%8A%A8%E6%80%81%E5%BA%93%28.so%29)
* [Shared Libraries and naming conventions](https://lists.linux-foundation.org/pipermail/lsb-spec/1999-May/000251.html)
* [Static, Shared Dynamic and Loadable Linux Libraries](http://www.yolinux.com/TUTORIALS/LibraryArchives-StaticAndDynamic.html)
* [Computing Library on Wikipedia](https://en.wikipedia.org/wiki/Library_(computing))
* [Static Libraries](http://tldp.org/HOWTO/Program-Library-HOWTO/static-libraries.html)
* [Shared Libraries](http://tldp.org/HOWTO/Program-Library-HOWTO/shared-libraries.html)
