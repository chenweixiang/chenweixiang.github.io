---
layout: post
title: "Linux Series #6: Shell"
tags: [Linux, Programming language]
toc: true
---

This article introduces the shells used in Unix/Linux system.

<!--more-->

As the [wikipedia](https://en.wikipedia.org/wiki/Shell_%28computing%29) says, a shell is a user interface for access to an operating system's services. In general, operating system shells use either a **command-line interface (CLI)** or **graphical user interface (GUI)**, depending on a computer's role and particular operation. Shells are actually special applications that use the kernel API in just the same way as it is used by other application programs. A shell manages the user-system interaction by prompting users for input, interpreting their input, and then handling an output from the underlying operating system.

# Shell Categories

Most operating system shells fall into one of two categories: **command-line** and **graphical**. Command line shells provide a command-line interface (CLI) to the operating system, while graphical shells provide a graphical user interface (GUI). Other possibilities, although not so common, include voice user interface (VUI) and various implementations of a text-based user interface (TUI) that are not CLI. The relative merits of CLI- and GUI-based shells are often debated.

* **Command-line shells**

    Command line shells provide a command-line interface (CLI) to the operating system, which uses alphanumeric characters typed on a keyboard to provide instructions and data to the operating system, interactively. A feature of many command-line shells is the ability to save sequences of commands for re-use. The command-line shell may offer features such as **command-line completion**, where the interpreter expands commands based on a few characters input by the user.

* **Graphical shells**

    Graphical shells provide means for manipulating programs based on graphical user interface (GUI), by allowing for operations such as opening, closing, moving and resizing windows, as well as switching focus between windows. Graphical shells may be included with desktop environments or come separately, even as a set of loosely coupled utilities.

# Shell Variants

The [article](http://www.softpanorama.org/People/Shell_giants/introduction.shtml) introduces of Unix shell history, which describes the four distinct generations of Unix shells in the long history. And here is the list of the most important shells:

* **Thompson shell**, ```sh```

    The first Unix shell was the [Thompson shell](https://en.wikipedia.org/wiki/Thompson_shell) ```sh``` written by Ken Thompson at Bell Labs and distributed with Versions 1 through 6 of Unix, from 1971 to 1975. Though rudimentary by modern standards, it introduced many of the basic features common to all later Unix shells, including **piping**, **simple control structures** using ```if``` and ```goto```, and **filename wildcarding**. Though not in current use, it is still available as part of some [Ancient UNIX Systems](https://en.wikipedia.org/wiki/Ancient_UNIX).

* **PWB shell** / **Mashey shell**, ```sh```

    The [PWB shell (known as PWB shell)](http://www.in-ulm.de/~mascheck/bourne/PWB/) ```sh``` was an upward-compatible version of the **Thompson shell**, augmented by John Mashey and others and distributed with the Programmer's Workbench UNIX, circa 1975-1977. It focused on making shell programming practical, especially in large shared computing centers. It added shell variables, user-executable shell scripts, and interrupt-handling. Control structures were extended from ```if/goto``` to ```if/then/else/endif```, ```switch/breaksw/endsw```, and ```while/end/break/continue```. As shell programming became widespread, these external commands were incorporated into the shell itself for performance.

* **Almquist shell**, ```ash``` / **Debian Almquist shell**, ```dash```

    [Almquist Shell (ash)](http://www.in-ulm.de/~mascheck/various/ash/) lists the family tree of Almquist shell:
    ![Almquist Shell (ash)](/assets/ash.png)

    Almquist shell ```ash``` is also fairly popular in embedded Linux systems; its code was incorporated into the **Busybox** catch-all executable often employed in this area.

    Debian Almquist shell ```dash``` replaced ash and became the default ```/bin/sh``` in Debian 6 (Squeeze). Dash became the default ```/bin/sh``` in Ubuntu starting with the 6.10 release in October 2006.

* **Bourne shell**, ```sh```

    The [Bourne shell](http://www.grymoire.com/Unix/Sh.html) ```sh``` was a complete rewrite by Stephen Bourne at Bell Labs. Distributed as the shell for **UNIX Version 7** in 1979, it introduced the rest of the basic features considered common to all the Unix shells.

    Traditionally, the Bourne shell program name is ```sh``` and its path in the Unix file system hierarchy is ```/bin/sh```. But a number of compatible work-alikes are also available with various improvements and additional features. On many systems, ```sh``` may be a symbolic link or hard link to one of these alternatives: [Almquist shell (ash)](http://www.in-ulm.de/~mascheck/various/ash/), [Debian Almquist shell (dash)](http://www.in-ulm.de/~mascheck/various/ash/), [Bourne-Again shell (bash)](https://www.gnu.org/software/bash/), [Korn shell (ksh)](http://www.kornshell.org/), [Public domain Korn shell (pdksh)](http://www.cs.mun.ca/~michael/pdksh/), [MirBSD Korn shell (mksh)](https://www.mirbsd.org/mksh.htm), [Z shell (zsh)](http://www.zsh.org/), [Busybox](http://www.busybox.net/).

* **C shell**, ```csh``` or ```tcsh```

    The [C shell](http://www.tcsh.org/Home) ```csh```, was written by Bill Joy while a graduate student at University of California, Berkeley and widely distributed with BSD Unix.

    What differentiated the C shell from others, especially in the 1980s, were its **interactive features and overall style**. Its new features made it easier and faster to use. The overall style of the language looked more like C and was seen as more readable.

    On many systems, such as Mac OS X and Red Hat Linux, ```csh``` is actually ```tcsh```, an improved version of ```csh```. Often one of the two files is either a hard link or a symbolic link to the other, so that either name refers to the same improved version of the C shell. ```tcsh``` added **filename and command completion** and **command line editing** concepts borrowed from the [Tenex system](https://en.wikipedia.org/wiki/TOPS-20#TENEX), which is the source of the "t". Because it only added functionality and did not change what was there, ```tcsh``` remained backward compatible with the original C shell. Though it started as a side branch from the original source tree Joy had created, ```tcsh``` is now the main branch for ongoing development.

    Here is [An in-depth interview with Steve Bourne, creator of the Bourne shell, or sh](http://www.computerworld.com.au/article/279011/a-z_programming_languages_bourne_shell_sh/).

* **Korn shell**, ```ksh```

    The [Korn shell](http://www.kornshell.org/) ```ksh``` is a Unix shell which was developed by David Korn at Bell Labs in the early 1980s and announced at USENIX on July 14, 1983. The initial development was based on **Bourne shell** source code. Korn shell is backward-compatible with the Bourne shell and includes many features of the C shell, inspired by the requests of Bell Labs users.

    There are several software products related to Korn shell: ```dtksh```, ```tksh```, ```oksh```, ```mksh```, ```SKsh```, ```MKS Inc.′s MKS Korn shell```.

* **Bourne-Again shell**, ```bash```

    [Bourne-Again shell](https://www.gnu.org/software/bash/) ```bash``` is a Unix shell and command language written by Brian Fox for the **GNU Project** as a free software replacement for the **Bourne shell**. Released in 1989, it has been distributed widely as the shell for the GNU operating system and as a default shell on Linux and Mac OS X.

    The Bash command syntax is a superset of the Bourne shell command syntax. Bash can execute the vast majority of Bourne shell scripts without modification, with the exception of Bourne shell scripts stumbling into fringe syntax behavior interpreted differently in Bash or attempting to run a system command matching a newer Bash built-in, etc. The keywords, syntax and other basic features of the language were all copied from Bourne shell ```sh```. Other features, e.g., history, were copied from ```csh``` and ```ksh```. **Bash is a POSIX shell, but with a number of extensions**.

* **Z shell**, ```zsh```

    The [Z shell](http://www.zsh.org/) ```zsh``` can be thought of as an extended **Bourne shell** with a large number of improvements, including some features of ```bash```, ```ksh```, and ```tcsh```.

# Shell Configuration Files

|                           |   sh   |  ksh  |  csh  |  tcsh  |  bash  |  zsh  |
| :------------------------ | :----: | :---: | :---: | :----: | :----: | :---: |
| /etc/.login               |        |       | login | login  |        |       |
| /etc/csh.cshrc            |        |       | yes   | yes    |        |       |
| /etc/csh.login            |        |       | login | login  |        |       |
| ~/.tcshrc                 |        |       |       | yes    |        |       |
| ~/.cshrc                  |        |       | yes   | yes    |        |       |
| ~/etc/ksh.kshrc           |        | int.  |       |        |        |       |
| /etc/sh.shrc              | int.   |       |       |        |        |       |
| $ENV (typically ~/.kshrc) | int.   | int.  |       |        | int.   |       |
| ~/.login                  |        |       | login | login  |        |       |
| ~/.logout                 |        |       | login | login  |        |       |
| /etc/profile              | login  | login |       |        | login  | login |
| ~/.profile                | login  | login |       |        | login  | login |
| ~/.bash_profile           |        |       |       |        | login  |       |
| ~/.bash_login             |        |       |       |        | login  |       |
| ~/.bash_logout            |        |       |       |        | login  |       |
| ~/.bashrc                 |        |       |       |        | int. + n/login | |
| /etc/zshenv               |        |       |       |        |        | yes   |
| /etc/zprofile             |        |       |       |        |        | login |
| /etc/zshrc                |        |       |       |        |        | int.  |
| /etc/zlogin               |        |       |       |        |        | login |
| /etc/zlogout              |        |       |       |        |        | login |
| ~/.zshenv                 |        |       |       |        |        | yes   |
| ~/.zprofile               |        |       |       |        |        | login |
| ~/.zshrc                  |        |       |       |        |        | int.  |
| ~/.zlogin                 |        |       |       |        |        | login |

NOTE:
 * blank means a file is not read by a shell at all.
 * "yes" means a file is always read by a shell upon startup.
 * "login" means a file is read if the shell is a login shell.
 * "n/login" means a file is read if the shell is not a login shell.
 * "int." means a file is read if the shell is interactive.

# Shell Specifications

The ```sh``` utility shall behave as specified in **POSIX 1003.1-2008 (ISO/IEC 9945-2009)**. And **Linux Standard Base (LSB)** has the extensions listed [here](http://refspecs.linuxfoundation.org/LSB_5.0.0/LSB-Core-generic/LSB-Core-generic/sh.html). And here is [Shell Command Language Index](http://pubs.opengroup.org/onlinepubs/7908799/xcu/shellix.html).

# GNU Bash

Here is [GNU Bash official site](https://www.gnu.org/software/bash/), and here is [Bash Reference Manual](https://www.gnu.org/software/bash/manual/).

## GNU Bash Releases

| GNU Bash Version | Release Date |
| :--------------: | :----------: |
| 2.02.1           | 24 Jul 1998  |
| 2.03             | 20 Feb 1999  |
| 2.04b5           | 24 Feb 2000  |
| 2.04             | 21 Mar 2000  |
| 2.05             | 09 Apr 2001  |
| 2.05a            | 16 Nov 2001  |
| 2.05b            | 18 Jul 2002  |
| 3.0              | 30 Jul 2004  |
| 3.2              | 13 Nov 2007  |
| 4.0              | 17 Mar 2009  |
| 4.1              | 29 Jan 2010  |
| 4.2              | 10 May 2011  |
| 4.3              | 26 Feb 2014  |

## GNU Bash Repository

The GNU Bourne-Again SHell Git repository is located [here](http://savannah.gnu.org/git/?group=bash). Run following command to get a copy of the Bash source code from repository:

    $ git clone git://git.savannah.gnu.org/bash.git

or, browse sources repository online [here](http://git.savannah.gnu.org/cgit/bash.git)

# Miscellaneous

Use the following command to show the valid shells in current system:

    chenwx@chenwx ~ $ cat /etc/shells
    # /etc/shells: valid login shells
    /bin/sh
    /bin/dash
    /bin/bash
    /bin/rbash
    /bin/tcsh
    /usr/bin/tcsh
    /usr/bin/screen

Use one of the following commands to show the default shell of specified user:

    chenwx@chenwx ~ $ cat /etc/passwd | grep chenwx
    chenwx:x:1000:1000:chenwx,,,:/home/chenwx:/bin/bash

Use one of the following commands to show the default shell of current user:

    chenwx@chenwx ~ $ echo $SHELL
    /bin/bash

    chenwx@chenwx ~ $ env | grep SHELL
    SHELL=/bin/bash

    chenwx@chenwx ~ $ echo $0
    bash

Use the following command to check the current shell:

    chenwx@chenwx ~ $ echo $$
    17826
    chenwx@chenwx ~ $ ps --pid 17826
      PID TTY          TIME CMD
    17826 pts/9    00:00:00 bash

or, use just one command instead of above two:

    chenwx@chenwx ~ $ ps --pid `echo $$`
      PID TTY          TIME CMD
    17826 pts/9    00:00:00 bash

    chenwx@chenwx ~ $ ps -f --pid `echo $$`
    UID        PID  PPID  C STIME TTY          TIME CMD
    chenwx   17826  2435  0 11:44 pts/9    00:00:00 bash

# References

[Shell (computing)](https://en.wikipedia.org/wiki/Shell_%28computing%29)
[Unix shell](https://en.wikipedia.org/wiki/Unix_shell)
