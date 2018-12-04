---
layout: post
title: "Linux: Shell"
tag: Linux
toc: true
---

This article introduces the shells used in Unix/Linux system.

<!--more-->

As the [wikipedia](https://en.wikipedia.org/wiki/Shell_%28computing%29) says, a shell is a user interface for access to an operating system's services. In general, operating system shells use either a **command-line interface (CLI)** or **graphical user interface (GUI)**, depending on a computer's role and particular operation. Shells are actually special applications that use the kernel API in just the same way as it is used by other application programs. A shell manages the user-system interaction by prompting users for input, interpreting their input, and then handling an output from the underlying operating system.

# Terminal Emulators

According to [wikipedia](https://en.wikipedia.org/wiki/Computer_terminal), a **computer terminal** is an electronic or electromechanical hardware device that is used for entering data into, and displaying data from, a computer or a computing system. ***The function of a computer terminal is confined to display and input of data.*** A device with significant local programmable data processing capability may be called a *smart terminal* or *fat client*; A terminal that depends on the host computer for its processing power is called a *dumb terminal* or *thin client*. A personal computer can run **terminal emulator** software that replicates the function of a computer terminal, sometimes allowing concurrent use of local programs and access to a distant *terminal host* system.

According to [wikipedia](https://en.wikipedia.org/wiki/Terminal_emulator), a **terminal emulator** (*term*, or *tty* for short), ***is a program that emulates a video terminal within some other display architecture***. Though typically synonymous with a ***shell*** or ***text terminal***, the term ***terminal*** covers all remote terminals, including graphical interfaces. A terminal emulator inside a graphical user interface (GUI) is often called a [terminal window](http://www.linfo.org/terminal_window.html).

A **terminal window** allows the user access to a text terminal and all its applications such as command-line interfaces (CLI) and text user interface (TUI) applications. These may be running either on the same machine or on a different one via telnet, ssh, or dial-up. On Unix-like operating systems, it is common to have one or more terminal windows connected to the local machine.

Terminals usually support a set of ***escape sequences*** for controlling color, cursor position, etc. Examples include the family of terminal control sequence standards known as **ECMA-48**, **ANSI X3.64** or **ISO/IEC 6429**.

## Examples of terminals emulated

Many terminal emulators have been developed for terminals such as *VT100*, *VT220*, *VT320*, *IBM 3270/8/9/E*, *IBM 5250*, *IBM 3179G*, *Data General D211*, *Hewlett Packard HP700/92*, *Sperry/Unisys 2000-series UTS60*, *Burroughs/Unisys A-series T27/TD830/ET1100*, *ADDS ViewPoint*, *Sun console*, *QNX*, *AT386*, *SCO-ANSI*, *SNI 97801*, *Televideo*, and *Wyse 50/60*. Additionally, programs have been developed to emulate other terminal emulators such as **xterm** and assorted **console** terminals (e.g., for Linux). Finally, some emulations simply refer to a standard, such as **ANSI**. Such programs are available on many platforms ranging from DOS and Unix to GUI operating systems such as Microsoft Windows and OS X, to embedded operating systems found in cellphones and industrial hardware.

## List of Terminal Emulators

[Here](https://en.wikipedia.org/wiki/List_of_terminal_emulators) is a list of terminal emulators. Notable terminal emulators include **Konsole** on KDE, **Gnome-terminal** on GNOME, and **xfce4-terminal** on Xfce as well as **xterm** and **rxvt-unicode**.

Following lists are the comparison of terminal emulators:

* [Comparison of terminal emulators](https://en.wikipedia.org/wiki/Comparison_of_terminal_emulators)
* [Comprehensive Linux Terminal Performance Comparison](http://martin.ankerl.com/2007/09/01/comprehensive-linux-terminal-performance-comparison/)

# Shell

## Shell Specifications

The ```sh``` utility shall behave as specified in **POSIX 1003.1-2008 (ISO/IEC 9945-2009)**. Here is [Shell Command Language Index](http://pubs.opengroup.org/onlinepubs/7908799/xcu/shellix.html). And **Linux Standard Base (LSB)** has the extensions listed [here](http://refspecs.linuxfoundation.org/LSB_5.0.0/LSB-Core-generic/LSB-Core-generic/sh.html).

## Shell Categories

Most operating system shells fall into one of two categories: **command-line** and **graphical**. Command line shells provide a command-line interface (CLI) to the operating system, while graphical shells provide a graphical user interface (GUI). Other possibilities, although not so common, include voice user interface (VUI) and various implementations of a text-based user interface (TUI) that are not CLI. The relative merits of CLI- and GUI-based shells are often debated.

* **Command-line shells**

    Command line shells provide a command-line interface (CLI) to the operating system, which uses alphanumeric characters typed on a keyboard to provide instructions and data to the operating system, interactively. A feature of many command-line shells is the ability to save sequences of commands for re-use. The command-line shell may offer features such as **command-line completion**, where the interpreter expands commands based on a few characters input by the user.

* **Graphical shells**

    Graphical shells provide means for manipulating programs based on graphical user interface (GUI), by allowing for operations such as opening, closing, moving and resizing windows, as well as switching focus between windows. Graphical shells may be included with desktop environments or come separately, even as a set of loosely coupled utilities.

## Shell Variants

The [article](http://www.softpanorama.org/People/Shell_giants/introduction.shtml) introduces of Unix shell history, which describes the four distinct generations of Unix shells in the long history. And here is the list of the most important shells:

* **Thompson shell**, ```sh```

    The first Unix shell was the [Thompson shell](https://en.wikipedia.org/wiki/Thompson_shell) ```sh``` written by Ken Thompson at Bell Labs and distributed with versions 1 through 6 of Unix, from 1971 to 1975. Though rudimentary by modern standards, it introduced many of the basic features common to all later Unix shells, including **piping**, **simple control structures** using ```if``` and ```goto```, and **filename wildcarding**. Though not in current use, it is still available as part of some [Ancient UNIX Systems](https://en.wikipedia.org/wiki/Ancient_UNIX).

* **PWB shell** / **Mashey shell**, ```sh```

    The [PWB shell](http://www.in-ulm.de/~mascheck/bourne/PWB/) (known as Mashey shell) ```sh``` was an upward-compatible version of the **Thompson shell**, augmented by John Mashey and others and distributed with the Programmer's Workbench UNIX, circa 1975-1977. It focused on making shell programming practical, especially in large shared computing centers. It added shell variables, user-executable shell scripts, and interrupt-handling. Control structures were extended from ```if/goto``` to ```if/then/else/endif```, ```switch/breaksw/endsw```, and ```while/end/break/continue```. As shell programming became widespread, these external commands were incorporated into the shell itself for performance.

* **Almquist shell**, ```ash``` / **Debian Almquist shell**, ```dash```

    The [site](http://www.in-ulm.de/~mascheck/various/ash/) lists the family tree of Almquist Shell (ash):
    ![Almquist Shell (ash)](/assets/ash.png)

    The Almquist shell ```ash``` is also fairly popular in embedded Linux systems; its code was incorporated into the [Busybox](https://www.busybox.net/) catch-all executable often employed in this area.

    The [Debian Almquist shell](https://packages.qa.debian.org/d/dash.html) ```dash``` replaced ash and became the default ```/bin/sh``` in Debian 6 (Squeeze). Dash became the default ```/bin/sh``` in Ubuntu starting with the 6.10 release in October 2006.

* **Bourne shell**, ```sh```

    The [Bourne shell](http://www.grymoire.com/Unix/Sh.html) ```sh``` was a complete rewrite by Stephen Bourne at Bell Labs. Distributed as the shell for **UNIX Version 7** in 1979, it introduced the rest of the basic features considered common to all the Unix shells.

    Traditionally, the Bourne shell program name is ```sh``` and its path in the Unix file system hierarchy is ```/bin/sh```. But a number of compatible work-alikes are also available with various improvements and additional features. On many systems, ```sh``` may be a symbolic link or hard link to one of these alternatives: [Almquist shell (ash)](http://www.in-ulm.de/~mascheck/various/ash/), [Debian Almquist shell (dash)](http://www.in-ulm.de/~mascheck/various/ash/), [Bourne-Again shell (bash)](https://www.gnu.org/software/bash/), [Korn shell (ksh)](http://www.kornshell.org/), [Public domain Korn shell (pdksh)](http://www.cs.mun.ca/~michael/pdksh/), [MirBSD Korn shell (mksh)](https://www.mirbsd.org/mksh.htm), [Z shell (zsh)](http://www.zsh.org/) and [Busybox](http://www.busybox.net/).

* **C shell**, ```csh``` or ```tcsh```

    The [C shell](http://www.tcsh.org/Home) ```csh```, was written by Bill Joy while a graduate student at University of California, Berkeley and widely distributed with BSD Unix.

    What differentiated the C shell from others, especially in the 1980s, were its **interactive features and overall style**. Its new features made it easier and faster to use. The overall style of the language looked more like C and was seen as more readable.

    On many systems, such as Mac OS X and Red Hat Linux, ```csh``` is actually ```tcsh```, an improved version of ```csh```. Often one of the two files is either a hard link or a symbolic link to the other, so that either name refers to the same improved version of the C shell. ```tcsh``` added **filename and command completion** and **command line editing** concepts borrowed from the [Tenex system](https://en.wikipedia.org/wiki/TOPS-20#TENEX), which is the source of the ***t***. Because it only added functionality and did not change what was there, ```tcsh``` remained backward compatible with the original C shell. Though it started as a side branch from the original source tree Joy had created, ```tcsh``` is now the main branch for ongoing development.

    Here is [An in-depth interview with Steve Bourne, creator of the Bourne shell, or sh](http://www.computerworld.com.au/article/279011/a-z_programming_languages_bourne_shell_sh/).

* **Korn shell**, ```ksh```

    The [Korn shell](http://www.kornshell.org/) ```ksh``` is a Unix shell which was developed by David Korn at Bell Labs in the early 1980s and announced at USENIX on July 14, 1983. The initial development was based on **Bourne shell** source code. Korn shell is backward-compatible with the Bourne shell and includes many features of the C shell, inspired by the requests of Bell Labs users.

    There are several software products related to Korn shell: ```dtksh```, ```tksh```, ```oksh```, ```mksh```, ```SKsh```, MKS Inc.'s ```MKS Korn shell```.

* **Bourne-Again shell**, ```bash```

    The [Bourne-Again shell](https://www.gnu.org/software/bash/) ```bash``` is a Unix shell and command language written by Brian Fox for the **GNU Project** as a free software replacement for the **Bourne shell**. Released in 1989, it has been distributed widely as the shell for the GNU operating system and as a default shell on Linux and Mac OS X.

    The Bash command syntax is a superset of the Bourne shell command syntax. Bash can execute the vast majority of Bourne shell scripts without modification, with the exception of Bourne shell scripts stumbling into fringe syntax behavior interpreted differently in Bash or attempting to run a system command matching a newer Bash built-in, etc. The keywords, syntax and other basic features of the language were all copied from Bourne shell ```sh```. Other features, e.g., history, were copied from ```csh``` and ```ksh```. **Bash is a POSIX shell, but with a number of extensions**.

* **Z shell**, ```zsh```

    The [Z shell](http://www.zsh.org/) ```zsh``` can be thought of as an extended **Bourne shell** with a large number of improvements, including some features of ```bash```, ```ksh```, and ```tcsh```.

## Shell Configuration Files

|                           |   sh   |  ksh  |  csh  |  tcsh  |  bash  |  zsh  |
| :------------------------ | :----: | :---: | :---: | :----: | :----: | :---: |
| ```/etc/.login```         |        |       | login | login  |        |       |
| ```/etc/csh.cshrc```      |        |       | yes   | yes    |        |       |
| ```/etc/csh.login```      |        |       | login | login  |        |       |
| ```~/.tcshrc```           |        |       |       | yes    |        |       |
| ```~/.cshrc```            |        |       | yes   | yes    |        |       |
| ```~/etc/ksh.kshrc```     |        | int.  |       |        |        |       |
| ```/etc/sh.shrc```        | int.   |       |       |        |        |       |
| $ENV (typically ```~/.kshrc```) | int.   | int.  |       |        | int.   |       |
| ```~/.login```            |        |       | login | login  |        |       |
| ```~/.logout```           |        |       | login | login  |        |       |
| ```/etc/profile```        | login  | login |       |        | login  | login |
| ```~/.profile```          | login  | login |       |        | login  | login |
| ```~/.bash_profile```     |        |       |       |        | login  |       |
| ```~/.bash_login```       |        |       |       |        | login  |       |
| ```~/.bash_logout```      |        |       |       |        | login  |       |
| ```~/.bashrc```           |        |       |       |        | int. + n/login | |
| ```/etc/zshenv```         |        |       |       |        |        | yes   |
| ```/etc/zprofile```       |        |       |       |        |        | login |
| ```/etc/zshrc```          |        |       |       |        |        | int.  |
| ```/etc/zlogin```         |        |       |       |        |        | login |
| ```/etc/zlogout```        |        |       |       |        |        | login |
| ```~/.zshenv```           |        |       |       |        |        | yes   |
| ```~/.zprofile```         |        |       |       |        |        | login |
| ```~/.zshrc```            |        |       |       |        |        | int.  |
| ```~/.zlogin```           |        |       |       |        |        | login |

<p/>
NOTE:

* ***blank*** means a file is not read by a shell at all.
* ***yes*** means a file is always read by a shell upon startup.
* ***login*** means a file is read if the shell is a login shell.
* ***n/login*** means a file is read if the shell is not a login shell.
* ***int.*** means a file is read if the shell is interactive.

## Shell Cheat Sheet

* [Unix Commands Reference Card](/docs/Unix_Commands_Reference_Card.pdf)
* [Unix/Linux Shell Cheat Sheet](/docs/Linux_Shell_Cheat_Sheet.pdf)

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

# Tools

## apropos

[apropos](http://www.linfo.org/apropos.html) search the manual page names and descriptions. For instance:

```
chenwx@chenwx:~ $ apropos directory
alphasort (3)        - scan a directory for matching entries
basename (1)         - strip directory and suffix from filenames
bindtextdomain (3)   - set directory containing message catalogs
chacl (1)            - change the access control list of a file or directory
chdir (2)            - change working directory
chroot (2)           - change root directory
chroot (8)           - run command or interactive shell with special root directory
closedir (3)         - close a directory
cups-files.conf (5)  - file and directory configuration file for cups
dbus-cleanup-sockets (1) - clean up leftover sockets in a directory
depmod.d (5)         - Configuration directory for depmod
dir (1)              - list directory contents
dirfd (3)            - get directory stream file descriptor
dirsplit (1)         - splits directory into multiple with equal size
execveat (2)         - execute program relative to a directory file descriptor
FcCacheCreateTagFile (3) - Create CACHEDIR.TAG at cache directory.
FcCacheDir (3)       - Return directory of cache
FcCacheSubdir (3)    - Return the i'th subdirectory.
FcConfigAppFontAddDir (3) - Add fonts from directory to font database
...
```

## fish

[fish](https://fishshell.com/docs/current/tutorial.html) is a fully-equipped command line shell (like **bash** or **zsh**) that is smart and user-friendly. fish supports powerful features like syntax highlighting, autosuggestions, and tab completions that just work, with nothing to learn or configure.

If you want to make your command line more productive, more useful, and more fun, without learning a bunch of arcane syntax and configuration options, then fish might be just what you're looking for!

# References

* [Shell Wikipedia](https://en.wikipedia.org/wiki/Shell_%28computing%29)
* [Unix Shell](https://en.wikipedia.org/wiki/Unix_shell)
