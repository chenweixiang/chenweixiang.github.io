---
layout: post
title: "Source Navigator NG"
tag: Tools
toc: true
---

This article introduces the Source Navigator NG.

<!--more-->

# Install Source Navigator NG 4.5 on LinuxMint

Download source code **sourcenavigator-NG4.5.tar.bz2** from [Source Navigator NG repo](https://sourceforge.net/p/sourcenav/).

Unzip it to ~/repo/sourcenavigator-NG4.5:

```
chenwx@chenwx:~/repo/sourcenavigator-NG4.5 $ ll
total 328K
-rw-r--r--  1 chenwx chenwx  14K Oct 14  2012 CHANGELOG
drwxr-xr-x  4 chenwx chenwx 4.0K Oct 16  2012 CONTRIB
-rw-r--r--  1 chenwx chenwx  143 Sep 13  2011 CONTRIBUTORS
-rw-r--r--  1 chenwx chenwx  18K Jun 26  2007 COPYING
-rw-r--r--  1 chenwx chenwx 6.1K Mar  8  2011 INSTALL
-rw-r--r--  1 chenwx chenwx  253 May  3  2007 MAINTAINERS
-rw-r--r--  1 chenwx chenwx 1.8K Aug 10  2007 Makefile.in
-rw-r--r--  1 chenwx chenwx 5.3K Feb  1  2009 README
-rw-r--r--  1 chenwx chenwx  298 Apr  5  2007 SVN_CHANGELEVELS
-rw-r--r--  1 chenwx chenwx  201 Mar  1  2011 TODO
-rwxr-xr-x  1 chenwx chenwx 3.7K Jun 26  2007 compile
drwxr-xr-x  2 chenwx chenwx 4.0K Oct 16  2012 config
-rwxr-xr-x  1 chenwx chenwx  44K Jun 26  2007 config.guess
-rwxr-xr-x  1 chenwx chenwx  32K Jun 26  2007 config.sub
-rwxr-xr-x  1 chenwx chenwx  83K Jan 21  2009 configure
-rw-r--r--  1 chenwx chenwx 1.7K Jan 21  2009 configure.in
drwxr-xr-x 74 chenwx chenwx 4.0K Oct 16  2012 db4
-rwxr-xr-x  1 chenwx chenwx  18K May  4  2008 depcomp
-rwxr-xr-x  1 chenwx chenwx 9.1K Jun 26  2007 install-sh
drwxr-xr-x  8 chenwx chenwx 4.0K Oct 16  2012 itcl
drwxr-xr-x  5 chenwx chenwx 4.0K Oct 16  2012 libgui
-rwxr-xr-x  1 chenwx chenwx  11K Jun 26  2007 missing
-rwxr-xr-x  1 chenwx chenwx 3.4K Jun 26  2007 mkinstalldirs
drwxr-xr-x 17 chenwx chenwx 4.0K Oct 16  2012 snavigator
drwxr-xr-x 14 chenwx chenwx 4.0K Oct 16  2012 tcl
drwxr-xr-x 11 chenwx chenwx 4.0K Oct 16  2012 tix
drwxr-xr-x 14 chenwx chenwx 4.0K Oct 16  2012 tk
```

Build the Source Navigator NG 4.5:

```
chenwx@chenwx:~/repo/sourcenavigator-NG4.5 $ ./configure --prefix=/opt/sourcenav

chenwx@chenwx:~/repo/sourcenavigator-NG4.5 $ make

chenwx@chenwx:~/repo/sourcenavigator-NG4.5 $ sudo make install
```

Add the Source Navigator NG 4.5 to PATH:

```
chenwx@chenwx:~/repo/sourcenavigator-NG4.5 $ ll /opt/sourcenav/bin
-rwxr-xr-x 1 root root  744 Sep  9 18:13 snavigator
-rwxr-xr-x 1 root root  877 Sep  9 18:13 snpdbg
-rwxr-xr-x 1 root root  371 Sep  9 18:13 snscenario
-rwxr-xr-x 1 root root 4.4M Sep  9 18:13 tclsh8.3
-rwxr-xr-x 1 root root 2.1K Sep  9 18:13 tixindex
-rwxr-xr-x 1 root root  13M Sep  9 18:13 tixwish4.1.8.1
-rwxr-xr-x 1 root root  13M Sep  9 18:13 wish8.3

chenwx@chenwx:~/repo/sourcenavigator-NG4.5 $ echo $PATH
/home/chenwx/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games

chenwx@chenwx:~/repo/sourcenavigator-NG4.5 $ export PATH=$PATH:/opt/sourcenav/bin 

chenwx@chenwx:~/repo/sourcenavigator-NG4.5 $ echo $PATH
/home/chenwx/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/opt/sourcenav/bin

chenwx@chenwx:~/repo/sourcenavigator-NG4.5 $ which snavigator
/opt/sourcenav/bin/snavigator
```

Start Source Navigator NG 4.5 by command:

```
chenwx@chenwx:~ $ snavigator &
```

# Source Navigator NG 4.5 Configuration

On Windows 10, set the compatibility mode of Source Navigator NG 4.5 to Windows 7:

![Source_Navigator_Compatibility_Mode](/assets/Source_Navigator_Compatibility_Mode.png)

On Windows 10, use **Run as administrator** when you're trying to create a new project, otherwise, it will pend in somewhere.

# References

* [Source Navigator NG](https://sourceforge.net/projects/sourcenav/)

