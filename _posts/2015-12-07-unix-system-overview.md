---
layout: post
title: "Unix: Overview"
tag: Linux
toc: true
---

This article introduces the standards and history of Unix system briefly.

<!--more-->

# Portable Operating System Interface (POSIX)

The [Portable Operating System Interface (POSIX)](http://standards.ieee.org/develop/wg/POSIX.html) is a family of standards specified by the **IEEE Computer Society** for maintaining compatibility between operating systems. **POSIX** defines the application programming interface (API), along with command line shells and utility interfaces, for software compatibility with variants of Unix and other operating systems.

Originally, the name **POSIX** referred to **IEEE Std 1003.1-1988**, released in 1988. The family of **POSIX** standards is formally designated as **IEEE 1003** and the international standard name is **ISO/IEC 9945**.

## POSIX Standards

Before 1997, POSIX comprised several standards:

| POSIX_standards | IEEE_standards | Note |
| :-------------- | :------------- | :--- |
| **POSIX.1**     | **IEEE Std 1003.1-1988**  | Core Services (incorporates standard ANSI C) |
| **POSIX.1b**    | **IEEE Std 1003.1b-1993** | Real-time extensions |
| **POSIX.1c**    | **IEEE Std 1003.1c-1995** | Threads extensions |
| **POSIX.2**     | **IEEE Std 1003.2-1992**  | Shell and Utilities |

<p/>

After 1997, the [Austin Group](http://www.opengroup.org/austin/) developed the POSIX revisions. The specifications are known under the name **Single UNIX Specification (SUS)**, before they become a POSIX standard when formally approved by the ISO.

| POSIX_standards | IEEE_standards | ISO/IEC_standards | POSIX_Note |
| :-------------- | :------------- | :---------------- | :--------- |
| **POSIX.1-2001** | **IEEE Std 1003.1-2001** | **ISO/IEC 9945-2003** | The **POSIX.1-2001** equates to the **Single UNIX Specification, version 3** (**SUSv3**), see [The Open Group announces completion of the joint revision to POSIX® and the Single UNIX® Specification](http://www.unix.org/version3/pr.html). |
| **POSIX.1-2004** | **IEEE Std 1003.1-2004** | | The **POSIX.1-2004** involves a minor update of **POSIX.1-2001** (**IEEE Std 1003.1-2001**). It incorporated two TCs (Technical Corrigenda):<br>- **IEEE Std 1003.1-2001/Cor 1-2002**<br>- **IEEE Std 1003.1-2001/Cor 2-2004**<br>Here is the online [IEEE Std 1003.1-2004 specification](http://pubs.opengroup.org/onlinepubs/000095399/). |
| **POSIX.1-2008** | **IEEE Std 1003.1-2008** | **ISO/IEC 9945-2009** | Current active version, see [here](http://standards.ieee.org/findstds/standard/1003.1-2008.html). The **POSIX.1-2008** is the core of the **Single UNIX Specification, version 4** (**SUSv4**). |
| **POSIX.1-2008/TC1** | **IEEE Std 1003.1-2008 /Cor 1-2013** | | Current active version, see [here](http://standards.ieee.org/findstds/standard/1003.1-2008-Cor_1-2013.html). Here is the online [IEEE Std 1003.1-2008 specification](http://pubs.opengroup.org/onlinepubs/9699919799/nframe.html). |

# Single UNIX Specification (SUS)

Beginning in 1998, a joint working group known as the [Austin Group](http://www.opengroup.org/austin/) began to develop the combined standard that would be known as the **Single UNIX Specification, version 3** (**SUSv3**) and as **POSIX.1-2001** (formally **IEEE Std 1003.1-2001**). It was released on January 30, 2002.

The [Single UNIX Specification (SUS)](http://www.unix.org/version4/) is the collective name of a family of standards for computer operating systems, compliance with which is required to qualify for the name **Unix**. The core specifications of the **Single UNIX Specification (SUS)** are developed and maintained by the [Austin Group](http://www.opengroup.org/austin/), which is a joint working Group of members of the [IEEE Portable Applications Standards Committee]((https://www.ieee.org/index.html)), [members of The Open Group](http://www.opengroup.org/), and [members of ISO/IEC Joint Technical Committee 1 (JTC1)](http://www.open-std.org/JTC1/SC22/). The Austin Group continues as the maintenance body for the specification, that's **ISO/IEC 9945**, **IEEE Std 1003.1**, and **The Open Group Base Specifications**.

## SUS Standards

| The_Single_UNIX_Specification_standards | Note |
| :---------------------------------------- | :--- |
| **Single UNIX Specification, version 1** (**SUSv1**) | Known as **Spec 1170**. It's the core of the **UNIX 95 brand**. |
| **Single UNIX Specification, version 2** (**SUSv2**) | Released in 1997. It's the core of the **UNIX 98 brand**. |
| **Single UNIX Specification, version 3** (**SUSv3**) | Released on January 30, 2002. It's the core of the **UNIX 03 brand** and equates to the **POSIX.1-2001 (IEEE Std 1003.1-2001)**. |
| **Single UNIX Specification, version 4** (**SUSv4**) | Released in 2008. It equates to the **POSIX.1-2008** (**IEEE Std 1003.1-2008**). Here is the online [IEEE Std 1003.1-2008 specification](http://pubs.opengroup.org/onlinepubs/9699919799/nframe.html). |

## Content of SUSv4

### Composition of SUSv4

The **Single UNIX Specification, Version 4 (SUSv4)** is made up of two documents: the **Base Specifications, Issue 7** and **X/Open Curses, Issue 7 (XCURSES)**. And the **Base Specifications, Issue 7** comprise four volumes:

* **Base Definitions, Issue 7** (**XBD7**)
* **System Interfaces, Issue 7** (**XSH7**)
* **Shell and Utilities, Issue 7** (**XCU7**)
* **Rationale, Issue 7** (**XRAT7**) (Informative)

### Interfaces of SUSv4

There are now **1833** interfaces defined in the **Single UNIX Specification, version 4** (**SUSv4**):

|  XBD  |  XSH  |  XCU  | XCURSES | Total |
| :---: | :---: | :---: | :-----: | :---: |
|   82  |  1191 |  174  |   386   | 1833  |

### Shell and Utilities, Issue 7 (XCU7)

According to chapter ***4.2 Functional Over view*** of ***Single UNIX Specification, version 4***, the Single UNIX Specification supports a robust tool environment of **174 utilities** (that's **160 external utilities** and **14 required built-in utilities**), described in XCU. The following table contains the 160 external utilities. Also refer to chapter ***8 Utility Interface Table*** and chapter ***12 Utilities Migration*** of ***Single UNIX Specification, version 4*** for more details, and there are more information can be found on the online [IEEE Std 1003.1-2008 specification](http://pubs.opengroup.org/onlinepubs/9699919799/nframe.html).

```
admin           df              lex             pwd             time
alias           diff            link            qalter          touch
ar              dirname         ln              qdel            tput
asa             du              locale          qhold           tr
at              echo            localedef       qmove           true
awk             ed              logger          qmsg            tsort
basename        env             logname         qrerun          tty
batch           ex              lp              qrls            type
bc              expand          ls              qselect         ulimit
bg              expr            m4              qsig            umask
c99             false           mailx           qstat           unalias
cal             fc              make            qsub            uname
cat             fg              man             read            uncompress
cd              file            mesg            renice          unexpand
cflow           find            mkdir           rm              unget
chgrp           fold            mkfifo          rmdel           uniq
chmod           fort77          more            rmdir           unlink
chown           fuser           mv              sact            uucp
cksum           gencat          newgrp          sccs            uudecode
cmp             get             nice            sed             uuencode
comm            getconf         nl              sh              uustat
command         getopts         nm              sleep           uux
compress        grep            nohup           sort            val
cp              hash            od              split           vi
crontab         head            paste           strings         wait
csplit          iconv           patch           strip           wc
ctags           id              pathchk         stty            what
cut             ipcrm           pax             tabs            who
cxref           ipcs            pr              tail            write
date            jobs            printf          talk            xargs
dd              join            prs             tee             yacc
delta           kill            ps              test            zcat
```

A certified UNIX system will provide all the tools in **XCU**, with the following provisions:

* The DEVELOPMENT utilities need not be provided. These consist of:

    ```admin``` ```cflow``` ```cflow``` ```ctags``` ```cxref``` ```delta``` ```get``` ```lex``` ```make```
    ```nm``` ```prs``` ```rmdel``` ```sact``` ```sccs``` ```strip``` ```unget``` ```val``` ```what``` ```yacc```

    **[NOTE1]** If the implementation claims to provide the DEVELOPMENT option, then all the tools in the group must be provided.

    **[NOTE2]** It should be noted that the C compiler, ```c99```, is not considered part of the DEVELOPMENT group. All certified UNIX systems must provide a way of compiling C-language programs.

* The FORTRAN development utilities need not be provided. These consist of the compiler, ```fort77```, and the ```ctags``` utility (which is also a DEVELOPMENT utility).

* The UUCP utilities need not be provided. These consist of:

    ```uucp``` ```uustat``` ```uux```

* The obsolescent Batch Environment Services and Utilities need not be provided. These consist of:

    ```qalter``` ```qdel``` ```qhold``` ```qmove``` ```qmsg``` ```qrerun``` ```qrls``` ```qselect``` ```qsig``` ```qstat``` ```qsub```

The following table contains the **special built-in utilities** of shell (see [IEEE Std 1003.1-2008 specification](http://pubs.opengroup.org/onlinepubs/9699919799/nframe.html)):

```
break           dot (.)         exit            return          times
colon (:)       eval            export          set             trap
continue        exec            readonly        shift           unset
```

# UNIX Certification

Here is the [POSIX Certification website](http://get.posixcertified.ieee.org/). The **POSIX®** Certified by ***IEEE*** and ***The Open Group*** certification program is a voluntary program, but is required of suppliers who wish to use the **POSIX®** trademark. Certification is open to any product meeting the ***conformance requirements***. Once a supplier has achieved certification for a product, they are permitted to use the trademark in connection with that product.

Here is some resources related to UNIX Certification:

* [The Open Group's UNIX Certification Program](http://www.opengroup.org/certification/idx/unix.html)
* [The UNIX 03 Certification Guide](http://www.opengroup.org/openbrand/docs/UNIX03_Certification_Guide.html)
* [The Practical Guide to the Open Brand](http://www.opengroup.org/openbrand/Certification_Guide/)
* [The register of Certified Products](http://www.opengroup.org/openbrand/register/) - Registered Products by major product standards.

# History of Unix system

This is a short description of Unix releases:

| Date  | Unix Releases |
| :---: | :--------------- |
| 1969  | Unix was developed on Summer 1969. |
| 1971  | **Unix 1st edition** released on Nov 3, 1971. |
| 1972  | **Unix 2nd edition** released on Dec 6, 1972. |
| 1973  | **Unix 3rd edition** released in February 1973.<br>**Unix 4th edition** released in November 1973. |
| 1974  | **Unix 5th edition** released in June 1974. |
| 1975  | **Unix 6th edition** released in May 1975. And Bourne shell is introduced begins being added onto. |
| 1979  | **Unix 7th edition** released in January 1979. |
| 1985  | **Unix 8th edition** released in February 1985. |
| 1989  | **Unix 10th edition** released in October 1989. |

## Unix Timeline

Besides, you can see the preview of the Unix timeline on website [Unix History](http://www.levenez.com/unix/). And following two figures from wikipedia is also very useful to understand the evolution of Unix distributions:

![Unix history](/assets/unix-history.png)

![Unix history](/assets/unix-history.svg)

# References

* [Unix, Linux, and variant history](http://www.computerhope.com/history/unix.htm)
* [Unix Tree](http://minnie.tuhs.org/cgi-bin/utree.pl)
