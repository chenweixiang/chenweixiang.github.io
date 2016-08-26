---
layout: post
title: "Prerequisite of Building Kernel"
tag: Linux kernel
toc: true
---

This article introduces the prerequisite of building kernel.

<!--more-->

# Prerequisite

First, check out the specific version of Linux kernel:

```
chenwx@chenwx ~/linux $ git co v4.6.4
Checking out files: 100% (9725/9725), done.
Note: checking out 'v4.6.4'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at 310ca59d1f1c... Linux 4.6.4

chenwx@chenwx ~/linux $ git st
HEAD detached at v4.6.4
nothing to commit, working tree clean
```

Then, check the minimal requirements of tools in *~/Documentation/Changes*, or you can check the latest version of [Documentation/Changes on mainline](https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/tree/Documentation/Changes).

```
chenwx@chenwx ~/linux $ more Documentation/Changes
...

Current Minimal Requirements
============================

Upgrade to at *least* these software revisions before thinking you've
encountered a bug!  If you're unsure what version you're currently
running, the suggested command should tell you.

Again, keep in mind that this list assumes you are already functionally
running a Linux kernel.  Also, not all tools are necessary on all
systems; obviously, if you don't have any ISDN hardware, for example,
you probably needn't concern yourself with isdn4k-utils.

o  GNU C                  3.2                     # gcc --version
o  GNU make               3.80                    # make --version
o  binutils               2.12                    # ld -v
o  util-linux             2.10o                   # fdformat --version
o  module-init-tools      0.9.10                  # depmod -V
o  e2fsprogs              1.41.4                  # e2fsck -V
o  jfsutils               1.1.3                   # fsck.jfs -V
o  reiserfsprogs          3.6.3                   # reiserfsck -V
o  xfsprogs               2.6.0                   # xfs_db -V
o  squashfs-tools         4.0                     # mksquashfs -version
o  btrfs-progs            0.18                    # btrfsck
o  pcmciautils            004                     # pccardctl -V
o  quota-tools            3.09                    # quota -V
o  PPP                    2.4.0                   # pppd --version
o  isdn4k-utils           3.1pre1                 # isdnctrl 2>&1|grep version
o  nfs-utils              1.0.5                   # showmount --version
o  procps                 3.2.0                   # ps --version
o  oprofile               0.9                     # oprofiled --version
o  udev                   081                     # udevd --version
o  grub                   0.93                    # grub --version || grub-install --version
o  mcelog                 0.6                     # mcelog --version
o  iptables               1.4.2                   # iptables -V
o  openssl & libcrypto    1.0.0                   # openssl version
o  bc                     1.06.95                 # bc --version
```

Actually, the softwares used to build linux kernel is quiet stable. We can get it from the commit history of *Documentation/Changes*:

```
chenwx@chenwx ~/linux $ git lhg Documentation/Changes
*   5ebe0ee802c5 2015-11-05 Linus Torvalds  Merge tag 'docs-for-linus' of git://git.lwn.net/linux
|\  
| * 1c3a54e257f7 2015-09-29 Jonathan Corbet  Documentation/Changes: Add bc in "Current Minimal Requirements" section
* | 283e8ba2dfde 2015-09-25 David Howells  MODSIGN: Change from CMS to PKCS#7 signing if the openssl is too old
|/  
* 3f1d44ae6401 2015-08-27 James Morris  Documentation/Changes: Now need OpenSSL devel packages for module signing
* bf5777bcdc54 2014-12-22 Jonathan Corbet  Documentation: GNU is frequently spelled Gnu
* 5d330cddb907 2014-12-03 David S. Miller  Update old iproute2 and Xen Remus links
* 00703e0b7990 2014-09-06 Jiri Kosina  Documentation: remove obsolete pcmcia-cs from Changes
* 03ebb7d03f94 2014-09-06 Jiri Kosina  Documentation: update links in Changes
* c8c3f7d621c1 2014-07-12 Linus Torvalds  Documentation/Changes: clean up mcelog paragraph
* 221069bed0c7 2014-05-19 Jiri Kosina  doc: Note need of bc in the kernel build from 3.10 onwards
* dad337501d49 2013-11-27 Linus Torvalds  remove obsolete references to powertweak
* 5adaf851d207 2011-07-11 Linus Torvalds  Documentation/Changes: remove some really obsolete text
* e06c37440014 2011-03-22 Linus Torvalds  Documentation/Changes: minor corrections
* a65577375844 2010-07-03 Jiri Kosina  Documentation update broken web addresses
* d879e19e18eb 2010-03-22 Jan Engelhardt  netfilter: xtables: remove xt_string revision 0
* 7a9226370543 2009-12-14 Patrick McHardy  netfilter: xtables: document minimal required version
* 082196242e24 2009-06-17 Linus Torvalds  Documentation/Changes: perl is needed to build the kernel
*   45e3e1935e28 2009-06-14 Linus Torvalds  Merge branch 'master' of git://git.kernel.org/pub/scm/linux/kernel/git/sam/kbuild-next
|\  
| * 2185a5ecd98d 2009-06-14 Sam Ravnborg  documentation: make version fix
* | 172d899db4bf 2009-04-28 H. Peter Anvin  x86, mce: document new 32bit mcelog requirement in Documentation/Changes
|/  
* 242f45da5b7b 2009-01-29 Linus Torvalds  Documentation/Changes: add required versions for new filesystems
* c3887cd72532 2007-08-02 H. Peter Anvin  [x86 setup] Document grub < 0.93 as broken
* 03a67a46af86 2006-11-30 Adrian Bunk  Fix typos in doc and comments
* e41217129c66 2006-09-11 Sam Ravnborg  Documentaion: update Documentation/Changes with minimum versions
* 890fbae2818a 2005-06-20 Greg Kroah-Hartman  [PATCH] devfs: Last little devfs cleanups throughout the kernel tree.
* 44fc355db7c2 2006-03-20 Adrian Bunk  Documentation/Changes: remove outdated translation references
* a1365647022e 2006-01-08 Linus Torvalds  [PATCH] remove gcc-2 checks
* 62a07e6e9e93 2005-11-07 Linus Torvalds  [PATCH] ksymoops related docs update
* ad7e14a55ed7 2005-10-27 Greg Kroah-Hartman  [PATCH] update required version of udev
* 909021ea7a8f 2005-09-27 Linus Torvalds  [PATCH] fuse: add required version info
* ec0344a2c93c 2005-07-27 Linus Torvalds  [PATCH] Documentation/Changes: document the required udev version
* eb05bfe4fbf0 2005-06-30 Linus Torvalds  [PATCH] pcmcia: update Documentation
* 5085cb26503a 2005-06-27 Linus Torvalds  [PATCH] pcmcia: add some Documentation
* 0c0a400d1deb 2005-06-23 Linus Torvalds  [PATCH] oprofile: report anonymous region samples
* 8b0c2d989cc6 2005-05-01 Linus Torvalds  [PATCH] DocBook: Use xmlto to process the DocBook files.
* 1da177e4c3f4 2005-04-16 Linus Torvalds  (tag: v2.6.12-rc2) Linux-2.6.12-rc2
```

# References

* [Documentation/Changes on mainline](https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/tree/Documentation/Changes)
