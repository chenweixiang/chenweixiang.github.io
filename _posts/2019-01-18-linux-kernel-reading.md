---
layout: post
title: "[Kernel] Linux Kernel Reading"
tag: Linux
toc: true
---

This article records my reading of Linux kernel based on Linux v3.2.

<!--more-->

# 1 Linux Kernel Brief Introduction

## 1.1 Linux Cross Reference

* [Linux Cross Reference (LXR)](http://lxr.linux.no/)
* [Cross-Referenced Linux and Device Driver Code](http://www.cs.fsu.edu/~baker/devices/)
* [Linux Syscall Reference](http://syscalls.kernelgrok.com/)
* [FreeBSD and Linux Kernel Cross-Reference](http://fxr.watson.org/)

## 1.2 Linux Kernel Git Repository

Git repositories hosted at [kernel.org](https://git.kernel.org/cgit/).

Refer to chapter 6.1.3 of **Pro Git** for the Git workflow of Linux kernel:

> 1) Regular developers work on their topic branch and rebase their work on top of master. The master branch is that of the dictator.
>
> 2) Lieutenants merge the developers' topic branches into their master branch.
>
> 3) The dictator merges the lieutenants' master branches into the dictator's master branch.
>
> 4) The dictator pushes their master to the reference repository so the other developers can rebase on it.

[**NOTE**] For Linux kernel developers, maybe it’s better for them to rebase their work on top of **linux-next** branch, refer to [1.2.2 linux-next tree](#1-2-2-linux-next-tree).

Git workflow:

![git_workflow](/assets/git_workflow.jpg)

Linux kernel code flow:

![linux_kernel_code_flow](/assets/linux_kernel_code_flow.jpg)

### 1.2.1 Git client repository

Git client:

* [http://git-scm.com/](http://git-scm.com/)
* [http://ndpsoftware.com/git-cheatsheet.html](http://ndpsoftware.com/git-cheatsheet.html)

Git client repository:

* [https://github.com/git/git](https://github.com/git/git)
* [https://git.kernel.org/cgit/git/git.git](https://git.kernel.org/cgit/git/git.git)
* [git://git.kernel.org/pub/scm/git/git.git](git://git.kernel.org/pub/scm/git/git.git)
* [https://git.kernel.org/pub/scm/git/git.git](https://git.kernel.org/pub/scm/git/git.git)
* [https://kernel.googlesource.com/pub/scm/git/git.git](https://kernel.googlesource.com/pub/scm/git/git.git)

After Git is installed, you can also get Git via Git itself for updates:

```
chenwx@chenwx:~ $ git clone https://github.com/git/git

chenwx@chenwx:~ $ cd git/
chenwx@chenwx:~/git $ git checkout master
chenwx@chenwx:~/git $ git pull

chenwx@chenwx:~/git $ git tag -l --sort="v:refname" | tail
  v2.3.3
  v2.3.4
  v2.3.5
  v2.4.0-rc0
chenwx@chenwx:~/git $ git checkout v2.3.5

chenwx@chenwx:~/git $ sudo make prefix=/usr install install-doc install-html install-info
chenwx@chenwx:~/git $ git --version

chenwx@chenwx:~/git $ make distclean
chenwx@chenwx:~/git $ git checkout master
```

### 1.2.2 linux-next tree

**linux-next** tree:

* [git://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git](git://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git)
* [https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git](https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git)
* [https://kernel.googlesource.com/pub/scm/linux/kernel/git/next/linux-next.git](https://kernel.googlesource.com/pub/scm/linux/kernel/git/next/linux-next.git)

Materials related to **linux-next** tree:

* [http://lwn.net/Articles/268881/](http://lwn.net/Articles/268881/)
* [http://lwn.net/Articles/269120/](http://lwn.net/Articles/269120/)
* [http://lwn.net/Articles/289013/](http://lwn.net/Articles/289013/)
* [http://lwn.net/Articles/289245/](http://lwn.net/Articles/289245/)

This tree, to be maintained by *Stephen Rothwell*, is intended to be a gathering point for the patches which are planned to be merged in the next development cycle.

[**NOTE1**] As a kernel developer, you should send patches against **linux-next** tree, not the **mainline** tree.

[**NOTE2**] You can see which trees have been included by looking in the [*linux/Next/Trees*](https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/tree/Next/Trees) file in the source. There are also [*quilt-import.log*](https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/tree/Next/quilt-import.log) and [*merge.log*](https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/tree/Next/merge.log) files in the [*linux/Next*](https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/tree/Next) directory:

```
chenwx@chenwx ~/linux/Next $ ll
-rw-r--r-- 1 chenwx chenwx 11K Feb 24 12:47 SHA1s
-rw-r--r-- 1 chenwx chenwx 17K Feb 24 12:47 Trees
-rw-r--r-- 1 chenwx chenwx 92K Feb 24 12:47 merge.log
-rw-r--r-- 1 chenwx chenwx  81 Feb 24 12:47 quilt-import.log
```

The **linux-next** tree has following branches:

* **stable** branch, trackes the master branch of linux **mainline** tree.
* **akpm** and **akpm-base** branches, track [http://www.ozlabs.org/~akpm/mmotm/](http://www.ozlabs.org/~akpm/mmotm/).
* **master** branch, the tags such as *next-20150324* are on this branch.

```
chenwx@chenwx ~/linux $ git br -r | grep linux-next
  linux-next/akpm
  linux-next/akpm-base
  linux-next/master
  linux-next/stable
```

#### 1.2.2.1 How to track linux-next tree

Tracking **linux-next** tree is a little bit different from usual trees. In particular, since *Stephen Rothwell* rebases it quite frequently, you shouldn't do a *git pull* on **linux-next**.

Note that **linux-next** tree isn't an *evolving* tree like mainline tree, it's best to see it as being a list of individual kernels released as tags, i.e. you shouldn't be merging one into another.

Use following commands to track **linux-next** tree:

```
# (1) Change directory to ~/linux
chenwx@chenwx ~ $ cd linux

# (2) Fetch linux-next plus tags.
#     Note that all tags be fetched from the remote in addition to
#     whatever else is being fetched by command "git fetch --tags".
chenwx@chenwx ~/linux $ git fetch
chenwx@chenwx ~/linux $ git fetch --tags

# (3) Update linux-next tree
chenwx@chenwx ~/linux $ git checkout master
chenwx@chenwx ~/linux $ git remote update
Fetching origin

# (4) List recent linux-next tags
chenwx@chenwx ~/linux $ git tag -l "next-*" | tail
...
next-20141015
next-20141016
next-20141017

# (5) Choose the linux-next version that you will work from, and
#     create a local branch ec-task10-v1 based on that version
chenwx@chenwx ~/linux $ git checkout next-20141017 -b ec-task10-v1
Switched to a new branch 'ec-task10'
```

#### 1.2.2.2 Subsystem trees

[**NOTE**] Refer to file [*linux/Next/Trees*](https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/tree/Next/Trees) in **linux-next** tree for subsystem trees.

##### 1.2.2.2.1 linux-staging tree

**linux-staging** tree:

* [git://git.kernel.org/pub/scm/linux/kernel/git/gregkh/staging.git](git://git.kernel.org/pub/scm/linux/kernel/git/gregkh/staging.git)
* [https://git.kernel.org/pub/scm/linux/kernel/git/gregkh/staging.git](https://git.kernel.org/pub/scm/linux/kernel/git/gregkh/staging.git)
* [https://kernel.googlesource.com/pub/scm/linux/kernel/git/gregkh/staging.git](https://kernel.googlesource.com/pub/scm/linux/kernel/git/gregkh/staging.git)

Materials related to **linux-staging** tree:

* [http://lwn.net/Articles/285599/](http://lwn.net/Articles/285599/)

The **linux-staging** tree was created to hold drivers and filesystems and other semi-major additions to the Linux kernel that are not ready to be merged at this point in time. It is here for companies and authors to get a wider range of testing, and to allow for other members of the community to help with the development of these features for the eventual inclusion into the main kernel tree.

##### 1.2.2.2.2 linux-security tree

**linux-security** tree:

* [https://git.kernel.org/cgit/linux/kernel/git/jmorris/linux-security.git](https://git.kernel.org/cgit/linux/kernel/git/jmorris/linux-security.git)
* [git://git.kernel.org/pub/scm/linux/kernel/git/jmorris/linux-security.git](git://git.kernel.org/pub/scm/linux/kernel/git/jmorris/linux-security.git)
* [https://git.kernel.org/pub/scm/linux/kernel/git/jmorris/linux-security.git](https://git.kernel.org/pub/scm/linux/kernel/git/jmorris/linux-security.git)
* [https://kernel.googlesource.com/pub/scm/linux/kernel/git/jmorris/linux-security.git](https://kernel.googlesource.com/pub/scm/linux/kernel/git/jmorris/linux-security.git)

### 1.2.3 mainline tree

Linux **mainline** tree:

* [git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git](git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git)
* [https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git)
* [https://kernel.googlesource.com/pub/scm/linux/kernel/git/torvalds/linux.git](https://kernel.googlesource.com/pub/scm/linux/kernel/git/torvalds/linux.git)

This is *Linux Torvalds*' git tree. There is only one branch, that's **master** branch, on the mainline tree.

[**NOTE1**] As a kernel developer, you should send patches against **linux-staging** or **linux-next** tree, not the mainline tree.

[**NOTE2**] Linux Torvalds负责维护mainline tree，在每个开发周期的merge window，新功能补丁会被合入mainline tree.

### 1.2.4 linux-stable tree

Refer to [Documentataion/translations/zh_CN/stable_kernel_rules.txt](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/Documentation/translations/zh_CN/stable_kernel_rules.txt).

Linux kernel stable tree:

* [https://git.kernel.org/cgit/linux/kernel/git/stable/linux-stable.git](https://git.kernel.org/cgit/linux/kernel/git/stable/linux-stable.git)
* [git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git](git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git)
* [http://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git](http://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git)
* [https://kernel.googlesource.com/pub/scm/linux/kernel/git/stable/linux-stable.git](https://kernel.googlesource.com/pub/scm/linux/kernel/git/stable/linux-stable.git)

Linux kernel stable patch queue:

* [https://git.kernel.org/cgit/linux/kernel/git/stable/stable-queue.git](https://git.kernel.org/cgit/linux/kernel/git/stable/stable-queue.git)
* [git://git.kernel.org/pub/scm/linux/kernel/git/stable/stable-queue.git](git://git.kernel.org/pub/scm/linux/kernel/git/stable/stable-queue.git)
* [https://git.kernel.org/pub/scm/linux/kernel/git/stable/stable-queue.git](git://git.kernel.org/pub/scm/linux/kernel/git/stable/stable-queue.git)
* [https://kernel.googlesource.com/pub/scm/linux/kernel/git/stable/stable-queue.git](git://git.kernel.org/pub/scm/linux/kernel/git/stable/stable-queue.git)

Each stable release has a corresponding branch on stable tree, such as *linux-3.2.y*. And its latest commits/maintainers can be found at [here](https://git.kernel.org/cgit/linux/kernel/git/stable/linux-stable.git/refs/heads).

Check the longterm branches on [https://www.kernel.org](https://www.kernel.org) and use following commands to track those branches:

```
chenwx@chenwx ~/linux $ git co linux-2.6.32.y
Checking out files: 100% (32771/32771), done.
Branch linux-2.6.32.y set up to track remote branch linux-2.6.32.y from origin.
Switched to a new branch 'linux-2.6.32.y'

chenwx@chenwx ~/linux $ git co linux-3.2.y
Checking out files: 100% (16874/16874), done.
Branch linux-3.2.y set up to track remote branch linux-3.2.y from origin.
Switched to a new branch 'linux-3.2.y'

chenwx@chenwx ~/linux $ git co linux-3.4.y
Checking out files: 100% (32682/32682), done.
Branch linux-3.4.y set up to track remote branch linux-3.4.y from origin.
Switched to a new branch 'linux-3.4.y'

chenwx@chenwx ~/linux $ git co linux-3.10.y
Checking out files: 100% (22201/22201), done.
Branch linux-3.10.y set up to track remote branch linux-3.10.y from origin.
Switched to a new branch 'linux-3.10.y'

chenwx@chenwx ~/linux $ git co linux-3.12.y
Checking out files: 100% (31307/31307), done.
Branch linux-3.12.y set up to track remote branch linux-3.12.y from origin.
Switched to a new branch 'linux-3.12.y'

chenwx@chenwx ~/linux $ git co linux-3.14.y
Checking out files: 100% (15876/15876), done.
Branch linux-3.14.y set up to track remote branch linux-3.14.y from origin.
Switched to a new branch 'linux-3.14.y'

chenwx@chenwx ~/linux $ git br
  linux-2.6.32.y
  linux-3.10.y
  linux-3.12.y
* linux-3.14.y
  linux-3.2.y
  linux-3.4.y
  master
```

[**NOTE**] **linux-stable** tree是对已发布的正式版本的后续维护，只包括一些bugfix或安全补丁，但不包括功能补丁。

### 1.2.5 Setup Linux Kernel Workarea

Run the following commands to clone all Linux kernel repositories into the same directory:

```
#
# (1) Clone mainline tree linux.git to ~/linux
#     git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
#     https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
#
chenwx@chenwx ~ $ git clone https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
Cloning into 'linux'...
remote: Counting objects: 3841355, done.
remote: Compressing objects: 100% (75674/75674), done.
remote: Total 3841355 (delta 56478), reused 0 (delta 0)
Receiving objects: 100% (3841355/3841355), 892.40 MiB | 2.47 MiB/s, done.
Resolving deltas: 100% (3147072/3147072), done.
Checking connectivity... done.
Checking out files: 100% (47936/47936), done.

#
# (2) Add next tree linux-next.git to ~/linux
#     git://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git
#     https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git
#
chenwx@chenwx ~/linux $ git remote add linux-next https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git

#
# (2.1) Download source code from linux-next tree
#
chenwx@chenwx ~/linux $ git fetch linux-next
chenwx@chenwx ~/linux $ git fetch --tags linux-next

#
# (2.2) Create local branch to track master branch of linux-next tree
#
chenwx@chenwx ~/linux $ git branch --track next-master linux-next/master

#
# (3) Add stable tree linux-stable.git to ~/linux
#     git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git
#     https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git
#
chenwx@chenwx ~/linux $ git remote add linux-stable https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git

#
# (3.1) Download source code from linux-stable tree
#
chenwx@chenwx ~/linux $ git fetch linux-stable
chenwx@chenwx ~/linux $ git fetch --tags linux-stable

#
# (3.2) Create local branches to track longterm stable branches
#       Check the stable branches on website https://www.kernel.org/
#
chenwx@chenwx ~/linux $ git co linux-3.2.y
chenwx@chenwx ~/linux $ git co linux-3.4.y
chenwx@chenwx ~/linux $ git co linux-3.10.y
chenwx@chenwx ~/linux $ git co linux-3.12.y
chenwx@chenwx ~/linux $ git co linux-3.14.y
chenwx@chenwx ~/linux $ git co linux-3.16.y
chenwx@chenwx ~/linux $ git co linux-3.18.y
chenwx@chenwx ~/linux $ git co linux-4.1.y
chenwx@chenwx ~/linux $ git co linux-4.4.y
chenwx@chenwx ~/linux $ git co linux-4.5.y
chenwx@chenwx ~/linux $ git co linux-4.6.y

#
# (4) Show local branches
#
chenwx@chenwx ~/linux $ git br
  linux-3.10.y
  linux-3.12.y
  linux-3.14.y
  linux-3.16.y
  linux-3.18.y
  linux-3.2.y
  linux-3.4.y
  linux-4.1.y
  linux-4.4.y
  linux-4.5.y
  linux-4.6.y
* master
  next-master

#
# (5) Use the following commands to fetch objects from all remotes
#
chenwx@chenwx ~/linux $ git remote -v
linux-next	https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git (fetch)
linux-next	https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git (push)
linux-stable	https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git (fetch)
linux-stable	https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git (push)
origin	https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git (fetch)
origin	https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git (push)

chenwx@chenwx ~/linux $ git remote update
Fetching origin
Fetching linux-stable
Fetching linux-next

chenwx@chenwx ~/linux $ git fetch --all
Fetching origin
Fetching linux-stable
Fetching linux-next
```

## 1.3 Linux Kernel Mailing lists

订阅和取消订阅邮件列表

* [http://vger.kernel.org/vger-lists.html](http://vger.kernel.org/vger-lists.html)

### 1.3.1 lkml.org

lkml.org

* [https://lkml.org/](https://lkml.org/)

在下列页面中列出了每年的邮件统计数字：

* [https://lkml.org/lkml](https://lkml.org/lkml)

可通过下列方式查看某天的邮件：

https://lkml.org/lkml/\<Year\>/\<Month\>/\<Day\>

例如：[https://lkml.org/lkml/2014/3/31](https://lkml.org/lkml/2014/3/31)

[**NOTE**] 可以通过左侧的"Get diff 1"提取邮件中的Patch.

### 1.3.2 lkml.iu.edu

The Linux-Kernel Archive:

* [http://lkml.iu.edu//hypermail/linux/kernel/index.html](http://lkml.iu.edu//hypermail/linux/kernel/index.html)

### 1.3.3 marc.info

marc.info

* [http://marc.info/?l=linux-kernel](http://marc.info/?l=linux-kernel)

[**NOTE**] 采用Courier New字体，视觉效果好。

## 1.4 Linux Kernel Releases

通过下列命令查看某 Linux kernel release 的信息，以v3.2为例：

```
chenwx@chenwx ~/linux $ git tag -l v3.2
v3.2
chenwx@chenwx ~/linux $ git lc v3.2
commit 805a6af8dba5dfdd35ec35dc52ec0122400b2610 (HEAD, tag: v3.2)
Author:     Linus Torvalds <torvalds@linux-foundation.org>
AuthorDate: Wed Jan 4 15:55:44 2012 -0800
Commit:     Linus Torvalds <torvalds@linux-foundation.org>
CommitDate: Wed Jan 4 15:55:44 2012 -0800

    Linux 3.2

 Makefile | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Refer to <a href="{{ site.base-url }}/2018/05/15/linux-kernel-releases.html">Linux Kernel Releases</a>.

### 1.4.1 Linux Versions

参见 **Understanding the Linux Kernel, 3rd Edition** 第 1. Introduction章第Linux Versions 节：

Up to kernel version 2.5, Linux identified kernels through a simple numbering scheme. Each version was characterized by three numbers, separated by periods. The first two numbers were used to identify the version; the third number identified the release. *The second version number identified the type of kernel: if it was even, it denoted a stable version; otherwise, it denoted a development version.*

During development of Linux kernel version 2.6, however, a significant change in the version numbering scheme has taken place. *Basically, the second number no longer identifies stable or development versions;* thus, nowadays kernel developers introduce large and significant changes in the current kernel version 2.6. A new kernel 2.7 branch will be created only when kernel developers will have to test a really disruptive change; this 2.7 branch will lead to a new current kernel version, or it will be backported to the 2.6 version, or finally it will simply be dropped as a dead end.

On 29 May 2011, *Linus Torvalds* announced that the kernel version would be bumped to 3.0 for the release following 2.6.39, *due to the minor version number getting too large and to commemorate the 20th anniversary of Linux.* It continued the time-based release practice introduced with 2.6.0, but using the second number - e.g. 3.1 would follow 3.0 after a few months. An additional number (now the third number) would be added on when necessary to designate security and bug fixes, as for example with 3.0.18. The major version number might be raised to 4 at some future date. Refer to [https://lkml.org/lkml/2011/5/29/204](https://lkml.org/lkml/2011/5/29/204).

### 1.4.2 Relationship of Tags

Linux kernel releases are marked by tags, such as v4.16. Run the following command to show the tags:

```
chenwx@chenwx ~/linux $ git tag -l v[0-9]* --sort=v:refname
v2.6.11
v2.6.11-tree
v2.6.12
v2.6.12-rc2
v2.6.12-rc3
v2.6.12-rc4
v2.6.12-rc5
v2.6.12-rc6
v2.6.12.1
v2.6.12.2
v2.6.12.3
v2.6.12.4
v2.6.12.5
v2.6.12.6
...
v4.16
v4.16-rc1
v4.16-rc2
v4.16-rc3
v4.16-rc4
v4.16-rc5
v4.16-rc6
v4.16-rc7
v4.16.1
v4.16.2
v4.16.3
v4.16.4
v4.16.5
v4.16.6
v4.16.7
v4.16.8
v4.17-rc1
v4.17-rc2
v4.17-rc3
v4.17-rc4
v4.17-rc5
```

If you want to know the relationship of Linux kernel tags, the Python script [linux_kernel_releases.py
](https://github.com/chenweixiang/scripts/blob/master/linux_kernel_releases.py) can be used to draw a figure about it. For instance:

```
chenwx@chenwx ~/linux $ ~/scripts/linux_kernel_releases.py -l "v3.2 v3.16 v3.18 v4.1 v4.4 v4.9 v4.14" -s "v4.15 v4.16" -o ~/Downloads/
Begin tag        : v2.6.12
End tag          : v4.16.8
Longterm branch  : v3.2 v3.16 v3.18 v4.1 v4.4 v4.9 v4.14
Stable branch    : v4.15 v4.16
Output directory : /home/chenwx/Downloads
```

The output is below figure:

![Linux_Kernel_Releases_20180512.svg](/assets/Linux_Kernel_Releases_20180512.svg)

### 1.4.3 Linux Kernel Release Note

The Linux kernel release notes are collected on website [Linux Kernel Newbies](https://kernelnewbies.org/):

* [Linux v4.0](https://kernelnewbies.org/Linux_4.0)
* [Linux v4.1](https://kernelnewbies.org/Linux_4.1)
* [Linux v4.2](https://kernelnewbies.org/Linux_4.2)
* [Linux v4.3](https://kernelnewbies.org/Linux_4.3)
* [Linux v4.4](https://kernelnewbies.org/Linux_4.4)
* [Linux v4.5](https://kernelnewbies.org/Linux_4.5)
* [Linux v4.6](https://kernelnewbies.org/Linux_4.6)
* [Linux v4.7](https://kernelnewbies.org/Linux_4.7)
* [Linux v4.8](https://kernelnewbies.org/Linux_4.8)
* [Linux v4.9](https://kernelnewbies.org/Linux_4.9)
* [Linux v4.10](https://kernelnewbies.org/Linux_4.10)
* [Linux v4.11](https://kernelnewbies.org/Linux_4.11)
* [Linux v4.12](https://kernelnewbies.org/Linux_4.12)
* [Linux v4.13](https://kernelnewbies.org/Linux_4.13)
* [Linux v4.14](https://kernelnewbies.org/Linux_4.14)
* [Linux v4.15](https://kernelnewbies.org/Linux_4.15)
* [Linux v4.16](https://kernelnewbies.org/Linux_4.16)
* [Linux v4.17](https://kernelnewbies.org/Linux_4.17)

## 1.5 Linux Kernel Bug Reporting

Linux内核开发者用于追踪内核Bug的网站

* [https://bugzilla.kernel.org/](https://bugzilla.kernel.org/)

## 1.6 Linux Kernel Development Process

参见下列文档：

* [Documentation/process/](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/process)
* [How to Participate in the Linux Community](/docs/How_to_Participate_in_the_Linux_Community.pdf) from Linux Foundation

Linux kernel development cycle:

![linux_kernel_develop_process](/assets/linux_kernel_develop_process.jpg)

Linux kernel code flow:

![linux_kernel_code_flow](/assets/linux_kernel_code_flow.jpg)

## 1.7 Linux Kernel Related Books

* **Linux Kernel Development, 3rd Edition**. *Robert Love* Done on 2014-01-12
* **Understanding the Linux Kernel, 3rd Edition**. *Daniel P. Bovet & Marco Cesati* Done on 2014-03-13
* **Understanding the Linux Virtual Memory Manager**, July 9 2007, *Mel Gorman* Done on 2014-03-17
* **Linux Device Drivers, 3rd Edition**. *Jonathan Corbet, Alessandro Rubini, Greg Kroah-Hartman*
* **Understanding Linux Network Internals**. *Christian Benvenuti*
* [Linux Memory Management](http://linux-mm.org)

## 1.8 Linux Distributions

GNU/Linux Distribution Timeline:

* [http://futurist.se/gldt/](http://futurist.se/gldt/)

The LWN.net Linux Distribution List:

* [http://lwn.net/Distributions/](http://lwn.net/Distributions/)

### 1.8.1 Git trees for linux distributions

Git trees for linux distributions:

| Linux distributions | Git trees |
| :------------------ | :-------- |
| Ubuntu              | [https://wiki.ubuntu.com/Kernel/Dev/KernelGitGuide](https://wiki.ubuntu.com/Kernel/Dev/KernelGitGuide) |
| LinuxMint           | [https://github.com/linuxmint](https://github.com/linuxmint) |

<p/>

### 1.8.2 How to check version of linux distributions

#### 1.8.2.1 lsb_release -a

```
chenwx@chenwx:~ $ lsb_release -a
No LSB modules are available.
Distributor ID:	LinuxMint
Description:	Linux Mint 19 Tara
Release:	19
Codename:	tara
```

#### 1.8.2.2 /etc/\*-release

```
chenwx@chenwx:~ $ cat /etc/issue
Linux Mint 19 Tara \n \l

chenwx@chenwx:~ $ cat /etc/issue.net
Linux Mint 19 Tara

chenwx@chenwx:~ $ cat /etc/lsb-release
DISTRIB_ID=LinuxMint
DISTRIB_RELEASE=19
DISTRIB_CODENAME=tara
DISTRIB_DESCRIPTION="Linux Mint 19 Tara"

chenwx@chenwx:~ $ cat /etc/os-release
NAME="Linux Mint"
VERSION="19 (Tara)"
ID=linuxmint
ID_LIKE=ubuntu
PRETTY_NAME="Linux Mint 19"
VERSION_ID="19"
HOME_URL="https://www.linuxmint.com/"
SUPPORT_URL="https://forums.ubuntu.com/"
BUG_REPORT_URL="http://linuxmint-troubleshooting-guide.readthedocs.io/en/latest/"
PRIVACY_POLICY_URL="https://www.linuxmint.com/"
VERSION_CODENAME=tara
UBUNTU_CODENAME=bionic

chenwx@chenwx:~ $ cat /etc/debian_version
buster/sid
```

#### 1.8.2.3 uname -a

```
chenwx@chenwx:~ $ uname -a
Linux chenwx 4.15.0-39-generic #42-Ubuntu SMP Tue Oct 23 15:48:01 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```

#### 1.8.2.4 /proc/version

```
chenwx@chenwx:~ $ cat /proc/version
Linux version 4.15.0-39-generic (buildd@lgw01-amd64-054) (gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)) #42-Ubuntu SMP Tue Oct 23 15:48:01 UTC 2018
```

#### 1.8.2.5 dmesg

```
chenwx@chenwx:~ $ dmesg | grep "Linux"
[    0.000000] Linux version 4.15.0-39-generic (buildd@lgw01-amd64-054) (gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)) #42-Ubuntu SMP Tue Oct 23 15:48:01 UTC 2018 (Ubuntu 4.15.0-39.42-generic 4.15.18)
[    0.044097] ACPI: Added _OSI(Linux-Dell-Video)
[    0.044098] ACPI: Added _OSI(Linux-Lenovo-NV-HDMI-Audio)
[    0.050972] ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored
[    1.099636] Linux agpgart interface v0.103
[    2.044123] usb usb1: Manufacturer: Linux 4.15.0-39-generic ehci_hcd
[    2.064119] usb usb2: Manufacturer: Linux 4.15.0-39-generic ehci_hcd
[    2.064730] usb usb3: Manufacturer: Linux 4.15.0-39-generic uhci_hcd
[    2.065177] usb usb4: Manufacturer: Linux 4.15.0-39-generic uhci_hcd
[    2.065640] usb usb5: Manufacturer: Linux 4.15.0-39-generic uhci_hcd
[    2.066097] usb usb6: Manufacturer: Linux 4.15.0-39-generic uhci_hcd
[    2.066567] usb usb7: Manufacturer: Linux 4.15.0-39-generic uhci_hcd
[    2.455143] pps_core: LinuxPPS API ver. 1 registered
[   18.436173] VBoxPciLinuxInit
```

#### 1.8.2.6 yum / dnf

```
$ yum info nano
Loaded plugins: fastestmirror, ovl
Loading mirror speeds from cached hostfile
* base: centos.zswap.net
* extras: mirror2.evolution-host.com
* updates: centos.zswap.net
Available Packages
Name : nano
Arch : x86_64
Version : 2.3.1
Release : 10.el7
Size : 440 k
Repo : base/7/x86_64
Summary : A small text editor
URL : http://www.nano-editor.org
License : GPLv3+
Description : GNU nano is a small and friendly text editor.

$ yum repolist
Loaded plugins: fastestmirror, ovl
Loading mirror speeds from cached hostfile
* base: centos.zswap.net
* extras: mirror2.evolution-host.com
* updates: centos.zswap.net
repo id repo name status
base/7/x86_64 CentOS-7 - Base 9591
extras/7/x86_64 CentOS-7 - Extras 388
updates/7/x86_64 CentOS-7 - Updates 1929
repolist: 11908

$ dnf info nano
Last metadata expiration check: 0:01:25 ago on Thu Feb 15 01:59:31 2018.
Installed Packages
Name : nano
Version : 2.8.7
Release : 1.fc27
Arch : x86_64
Size : 2.1 M
Source : nano-2.8.7-1.fc27.src.rpm
Repo : <a href="http://www.jobbole.com/members/system">@System</a>
From repo : fedora
Summary : A small text editor
URL : https://www.nano-editor.org
License : GPLv3+
Description : GNU nano is a small and friendly text editor.
```

#### 1.8.2.7 rpm

```
$ rpm -q nano
nano-2.8.7-1.fc27.x86_64
```

#### 1.8.2.8 apt-get

```
chenwx@chenwx:~ $ apt-cache policy nano
nano:
  Installed: (none)
  Candidate: 2.9.3-2
  Version table:
     2.9.3-2 500
        500 http://mirrors.aliyun.com/ubuntu bionic/main amd64 Packages
```

# 2 Linux Kernel源代码结构

本文中的目录和文件均相对于目录```~/linux/```，参见[1.2.5 Setup Linux Kernel Workarea](#1-2-5-setup-linux-kernel-workarea)节。

## 2.1 说明文件

linux/目录下的文件：

| Files | Description |
| :---- | :---------- |
| README | Linux内核说明文档，简要介绍了Linux内核的背景，描述了配置和build内核需要什么。 |
| COPYING | 版权声明 |
| CREDITS | Linux内核贡献人员列表 |
| MAINTAINERS | Linux维护人员信息 |
| REPORTING-BUGS | 报告Bug的流程及模板 |

<p/>

Documentation/目录下的文件：

| Documentation/ | Description |
| :------------- | :---------- |
| 00-INDEX | Documentation/下各目录的内容 |
| email-clients.txt | 使用邮件发送patch时， 需要对邮件客户端进行特殊配置。 |
| Changes | 列出了成功编译和运行内核所需的各种软件包的最小集合。 |
| CodingStyle | 描述了Linux内核编码风格， 和一些隐藏在背后的基本原理。 所有的想加入内核的新代码应当遵循这篇文档的指导。 绝大数的内核代码维护者只愿意接受那些符合这篇文档描述的风格的补丁， 许多内核开发者也只愿意审查那些符合Linux内核编码风格的代码。 |
| development-process | Linux kernel development process. |
| SubmittingPatches<br>SubmittingDrivers<br>SubmitChecklist | 描述了如何成功的创建和向社区递交一个补丁， 包括：邮件内容、邮件格式、发送者和接收者。 遵循文档里提倡的规则并不一定保证你提交补丁成功 (因为所有的补丁遭受详细而严格的内容和风格的审查)， 但是不遵循它们， 提交补丁肯定不成功。 |
| stable_api_nonsense.txt | 这篇文档描述了有意决定在内核里没有固定内核API的基本原因， 这对于理解Linux的开发哲学非常关键， 也对于从其他操作系统转移到Linux上的开发人员非常重要。 |
| SecurityBugs | 如果你确知在Linux Kernel里发现了security problem， 请遵循这篇文档描述的步骤， 帮助通知内核的开发者们并解决这类问题。 |
| ManagementStyle | 这篇文档描述了Linux内核开发者们如何进行管理运作， 以及运作方法背后的分享精神(shared ethos)。 这篇文档对于那些内核开发新手们(或者那些好奇者)值得一读， 因为它解决或解释了很多对于内核维护者独特行为的误解。 |
| stable_kernel_rules.txt | 这篇文档描述了一个稳定的内核版本如何发布的规则， 以及需要做些什么如果你想把一个修改加入到其中的一个版本。 |
| kernel-docs.txt | 关于内核开发的外部文档列表。 |
| applying-patches.txt | 描述了什么是补丁(patch)， 以及如何将它应用到内核的不同开发分支(branch)上。 |
| kbuild/kconfig.txt | Information on using the Linux kernel config tools. |
| DocBook/ | 内核里有大量的由内核源码自动生成的文档。 其中包括了内核内部API的全面描述， 和如何处理好锁的规则。 文档格式包括 PDF, Postscritpt, HTML 和 man pages， 可在内核源码主目录下运行下列命令自动生成， 见下文。 |

<p/>

检查内核代码风格：

```
step 1) 运行脚本scripts/Lindent使源代码符合Linux Kernel的代码风格：
# scripts/Lindent <file>

或者，运行下列命令来格式化源代码：
# indent -kr -i8 -ts8 -sob -l80 -ss -bs -psl <file>

step 2) 运行下列脚本来检查代码格式的合法性：
# scripts/checkpatch.pl --terse --file <file>
```

[**NOTE**] The style checker ```scripts/chechpatch.pl``` should be viewed as a guide not as the final word. If your code looks better with a violation then its probably best left alone.

[**NOTE**] The pre-condition of running ```scripts/Lindent``` and ```indent``` is that the source files use unix format, use below command to transfer source file format:

```
# dos2unix <file>
# unix2dos <file>
```

在内核源码根目录下执行下列命令会在DocBook/目录下生成不同格式的文档：

```
/*
 * (1) 顶层Makefile中有关内核文档的目标
 */
chenwx@chenwx ~/linux $ ll Documentation/DocBook/
total 1.1M
-rw-r--r-- 1 chenwx chenwx  21K Aug 11 09:12 80211.tmpl
-rw-r--r-- 1 chenwx chenwx 7.1K Aug 11 09:12 Makefile
-rw-r--r-- 1 chenwx chenwx 4.0K Aug 11 09:12 alsa-driver-api.tmpl
-rw-r--r-- 1 chenwx chenwx  69K Aug 12 08:25 crypto-API.tmpl
-rw-r--r-- 1 chenwx chenwx  16K Aug 11 09:10 debugobjects.tmpl
-rw-r--r-- 1 chenwx chenwx  15K Aug 11 09:12 device-drivers.tmpl
-rw-r--r-- 1 chenwx chenwx  12K Aug 11 09:10 deviceiobook.tmpl
-rw-r--r-- 1 chenwx chenwx 174K Aug 12 08:25 drm.tmpl
...

chenwx@chenwx ~/linux $ make help
...
Documentation targets:
 Linux kernel internal documentation in different formats:
  htmldocs        - HTML
  pdfdocs         - PDF
  psdocs          - Postscript
  xmldocs         - XML DocBook
  mandocs         - man pages
  installmandocs  - install man pages generated by mandocs
  cleandocs       - clean all generated DocBook files
...

/*
 * (2) 编译HTML格式的内核文档
 */
chenwx@chenwx ~/linux $ make O=../linux-build/ htmldocs
...
  HTML    Documentation/DocBook/z8530book.html
rm -rf Documentation/DocBook/index.html; echo '<h1>Linux Kernel HTML Documentation</h1>' >> Documentation/DocBook/index.html && echo '<h2>Kernel Version: 4.1.6</h2>' >> Documentation/DocBook/index.html && cat Documentation/DocBook/80211.html Documentation/DocBook/alsa-driver-api.html Documentation/DocBook/crypto-API.html Documentation/DocBook/debugobjects.html Documentation/DocBook/device-drivers.html Documentation/DocBook/deviceiobook.html Documentation/DocBook/drm.html Documentation/DocBook/filesystems.html Documentation/DocBook/gadget.html Documentation/DocBook/genericirq.html Documentation/DocBook/kernel-api.html Documentation/DocBook/kernel-hacking.html Documentation/DocBook/kernel-locking.html Documentation/DocBook/kgdb.html Documentation/DocBook/libata.html Documentation/DocBook/librs.html Documentation/DocBook/lsm.html Documentation/DocBook/media_api.html Documentation/DocBook/mtdnand.html Documentation/DocBook/networking.html Documentation/DocBook/rapidio.html Documentation/DocBook/regulator.html Documentation/DocBook/s390-drivers.html Documentation/DocBook/scsi.html Documentation/DocBook/sh.html Documentation/DocBook/tracepoint.html Documentation/DocBook/uio-howto.html Documentation/DocBook/usb.html Documentation/DocBook/w1.html Documentation/DocBook/writing-an-alsa-driver.html Documentation/DocBook/writing_musb_glue_layer.html Documentation/DocBook/writing_usb_driver.html Documentation/DocBook/z8530book.html >> Documentation/DocBook/index.html

/*
 * (3) 查看编译后的HTML格式的内核文档
 */
chenwx@chenwx ~/linux $ firefox ../linux-build/Documentation/DocBook/index.html &
```

## 2.2 配置文件

| Files | Description |
| :---- | :---------- |
| Kconfig, */Kconfig | 内核配置选项文件Kconfig |
| Kbuild, */Kbuild | 内核编译系统Kbuild的Makefile文件 |
| Makefile | 顶层Makefile文件 |

<p/>

## 2.3 代码文件

| Directory | Description |
| :-------- | :---------- |
| arch/ | 包含所有与特定硬件结构相关的内核代码。arch目录下处理器体系架构介绍，参见arch目录下处理器体系架构介绍节。 |
| block/ | block层的实现。最初block层的代码一部分位于drivers/目录，一部分位于fs/目录，从2.6.15开始，block 层的核心代码被提取出来放在了顶层的block/目录。 |
| certs/ | Since Linux kernel version 3.7 onwards, support has been added for signed kernel modules. When enabled, the Linux kernel will only load kernel modules that are digitally signed with the proper key. This allows further hardening of the system by disallowing unsigned kernel modules, or kernel modules signed with the wrong key, to be loaded. Malicious kernel modules are a common method for loading rootkits on a Linux system. Refer to [Signed Kernel Module Support](/docs/signed_kernel_module_support.pdf). |
| crypto/ | 内核本身所用的加密API，实现了常用的加密和散列算法，还有一些压缩和CRC校验算法。 |
| drivers/ | 包含内核中所有的设备驱动程序，每种驱动程序占用一个子目录，如块设备，scsi设备驱动程序等。 |
| firmware/ | 使用某些驱动程序而需要的设备固件。 |
| fs/ | 包含所有文件系统的代码，每种文件系统占用一个子目录，如ext2、ext3、ext4等。 |
| include/ | 包含编译内核代码时所需的大部分头文件。与体系架构无关的头文件包含在include/linux目录下。 |
| init/ | 包含内核的初始化代码，这是内核开始工作的起点。 |
| ipc/ | 包含进程间通信的代码。 |
| kernel/ | 包含主要的核心代码。与体系架构有关的核心代码包含在arch/$(ARCH)/kernel/目录下。 |
| lib/ | 核心的库代码。与arch/$(ARCH)/lib下的代码不同，这里的库代码都是用C编写的，在内核新的移植版本中可以直接使用。 |
| mm/ | 包含所有与体系架构无关的内存管理代码。与体系架构有关的内存管理代码包含在arch/$(ARCH)/mm/目录下。 |
| net/ | 包含内核的网络代码。 |
| samples/ | Linux内核的示范代码。 |
| scripts/ | 包含编译内核所用的脚本等文件。 |
| security/ | 包括了不同的Linux安全模型的代码，例如: NSA Security-Enhanced Linux. |
| sound/ | 声卡驱动以及其他声音相关的代码。 |
| tools/ | Tools helpful for developing Linux. |
| perf/ | 由内核维护人员Ingo Molnar等人开发的Linux内核综合性能概要分析工具。 |
| usr/ | Early user-space code (called initramfs). |
| virt/ | Virtualization infrastructure. |

<p/>

脚本```scripts/get_maintainer.pl```用于检测指定内核子系统的维护者，例如：

```
chenwx@chenwx ~/linux $ scripts/get_maintainer.pl -f fs
Alexander Viro <viro@zeniv.linux.org.uk> (maintainer:FILESYSTEMS (VFS...)
linux-fsdevel@vger.kernel.org (open list:FILESYSTEMS (VFS...)
linux-kernel@vger.kernel.org (open list)
```

# 3 Linux Kernel配置、编译与升级

Linux kernel的编译流程：

![Linux_Kernel_Compiling](/assets/Linux_Kernel_Compiling.jpg)

## 3.1 概述

参见目录[Documentation/kbuild/](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/kbuild)中的下列文档：

| 00-INDEX | info on the kernel build process |
| kbuild.txt | developer information on kbuild |
| kconfig.txt | usage help for make *config |
| kconfig-language.txt | specification of Config Language, the language in Kconfig files |
| makefiles.txt | developer information for linux kernel makefiles |
| modules.txt | how to build modules and to install them |

<p/>

[**NOTE**] 编译系统前，需要先检查系统中相关工具的版本是否满足文件Documentation/Changes所列出的最小要求，参见[3.1A Prerequisite of Building Kernel](#3-1a-prerequisite-of-building-kernel)节。

## 3.1A Prerequisite of Building Kernel

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

## 3.2 Kbuild编译系统

参见下列说明文档：

* [Documentation/kbuild/kbuild.txt](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/kbuild/kbuild.txt)
* [Documentation/kbuild/makefiles.txt](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/kbuild/makefiles.txt)
* [Documentation/kbuild/modules.txt](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/kbuild/modules.txt)

### 3.2.0 Kbuild和Makefile的关系

由[Documentation/kbuild/makefiles.txt](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/kbuild/modules.txt)中的描述:

> The preferred name for the kbuild files are 'Makefile' but 'Kbuild' can be used and if both a 'Makefile' and a 'Kbuild' file exists, then the 'Kbuild' file will be used.

可知，Kbuild编译系统的配置文件名为Makefile或Kbuild，若在同一个目录中同时存在Makefile和Kbuild，则优先采用Kbuild，参见scripts/Makefile.build：

```
# The filename Kbuild has precedence over Makefile
kbuild-dir := $(if $(filter /%,$(src)),$(src),$(srctree)/$(src))
kbuild-file := $(if $(wildcard $(kbuild-dir)/Kbuild),$(kbuild-dir)/Kbuild,$(kbuild-dir)/Makefile)
include $(kbuild-file)
```

运行下列命令查找同时包含Kbuild和Makefile的目录：

```
chenwx@chenwx ~/linux $ find . -name Makefile | xargs dirname | sort > dir_Makefile.txt
chenwx@chenwx ~/linux $ find . -name Kbuild | xargs dirname | sort > dir_Kbuild.txt

chenwx@chenwx ~/linux $ comm -12 dir_Makefile.txt dir_Kbuild.txt
.
./arch/arc
./arch/mips
./arch/s390
./arch/sparc
./arch/tile
./arch/x86
./tools/testing/nvdimm
```

由此可知，同时包含Makefile和Kbuild的目录仅有：

```
~/linux/
~/linux/arch/arc/
~/linux/arch/mips/
~/linux/arch/s390/
~/linux/arch/sparc/
~/linux/arch/tile/
~/linux/arch/x86/
```

其中，顶层Makefile是make直接调用的，其他的linux/$(SRCARCH)/Makefile则是通过顶层Makefile引入的：

```
linux/Makefile
+- include scripts/Kbuild.include
|  +- build := -f $(srctree)/scripts/Makefile.build obj
+- include arch/$(SRCARCH)/Makefile
```

此外，还可以通过下列命令统计内核中Makefile和Kbuild文件数目(v4.9-rc1)：

```
chenwx@chenwx ~/linux $ find . -name Makefile | wc -l
2260
chenwx@chenwx ~/linux $ find . -name Kbuild | wc -l
173
```

### 3.2.1 采用Kbuild编译系统的Linux Kernel版本

从Linux Kernel v2.6起，Linux内核的编译采用Kbuild系统。和过去的编译系统有很大的不同，尤其对于Linux内核模块的编译。在新的系统下，Linux编译系统会两次扫描Linux的Makefile:

* 首先，编译系统会读取Linux内核顶层的Makefile (通过在linux的顶层目录执行make命令来读取Makefiles);
* 然后，根据读到的内容第二次读取Kbuild的Makefile来编译Linux内核 (参见[3.2.0 Kbuild和Makefile的关系](#3-2-0-kbuild-makefile-)节)。

### 3.2.1A Components of Kbuild System

The documents related to kbuild system of Linux kernel are located in directory *~/Documentation/kbuild/*:

```
chenwx@chenwx ~/linux $ ll Documentation/kbuild/
-rw-rw-r-- 1 chenwx chenwx  427 Jul 22 20:39 00-INDEX
-rw-rw-r-- 1 chenwx chenwx 2.3K Aug  2 22:12 Kconfig.recursion-issue-01
-rw-rw-r-- 1 chenwx chenwx 2.8K Aug  2 22:12 Kconfig.recursion-issue-02
-rw-rw-r-- 1 chenwx chenwx 1.1K Aug  2 22:12 Kconfig.select-break
-rw-rw-r-- 1 chenwx chenwx 2.4K Aug  2 22:12 headers_install.txt
-rw-rw-r-- 1 chenwx chenwx 8.3K Aug  2 22:12 kbuild.txt
-rw-rw-r-- 1 chenwx chenwx  22K Aug  2 22:12 kconfig-language.txt
-rw-rw-r-- 1 chenwx chenwx 8.7K Jul 22 20:39 kconfig.txt
-rw-rw-r-- 1 chenwx chenwx  47K Aug  2 22:12 makefiles.txt
-rw-rw-r-- 1 chenwx chenwx  17K Jul 22 20:39 modules.txt
```

The kbuild system of Linux kernel includes the following items:

#### 3.2.1A.1 Top Makefile

The top Makefile is included in the root directory of Linux kernel repository:

```
chenwx@chenwx ~/linux $ ll Makefile
-rw-rw-r-- 1 chenwx chenwx 57K Jul 22 20:40 Makefile
```

We alway input make commands in the root directory of Linux kernel repository, that's the top Makefile is the main entry point of kbuild system.

##### 3.2.1A.1.1 Makefile Tree

The top Makefile includes the following Makefiles:

```
linux-3.2/Makefile
+- include scripts/Kbuild.include
|  +- build := -f $(srctree)/scripts/Makefile.build obj
+- include arch/$(SRCARCH)/Makefile
|  |  >> for x86, includes linux-3.2/arch/x86/Makefile
|  +- include $(srctree)/arch/x86/Makefile_32.cpu
```

and where, the ```linux-3.2/scripts/Makefile.build``` includes the following scripts:

```
linux-3.2/scripts/Makefile.build
+- -include include/config/auto.conf
+- include scripts/Kbuild.include
+- include $(kbuild-file)
|  >> 包含指定目录下的Kbuild，或者Makefile(若不存在Kbuild的话)
+- include scripts/Makefile.lib
+- include scripts/Makefile.host
+- include $(cmd_files)
```

Run the following commands to check the relationships between Makefile and Kbuild:

```
chenwx@chenwx ~/linux $ make -d O=../linux-build bzImage > ../linux-build/build.log

chenwx@chenwx ~/linux $ grep "Reading makefile" ../linux-build/build.log
Reading makefiles...
Reading makefile 'Makefile'...
Reading makefiles...
Reading makefile '/home/chenwx/linux/Makefile'...
Reading makefile 'scripts/Kbuild.include' (search path) (no ~ expansion)...
Reading makefile 'include/config/auto.conf' (search path) (don't care) (no ~ expansion)...
Reading makefile 'include/config/auto.conf.cmd' (search path) (don't care) (no ~ expansion)...
Reading makefile 'arch/x86/Makefile' (search path) (no ~ expansion)...
Reading makefile 'arch/x86/Makefile_32.cpu' (search path) (no ~ expansion)...
Reading makefile 'scripts/Makefile.gcc-plugins' (search path) (no ~ expansion)...
Reading makefile 'scripts/Makefile.kasan' (search path) (no ~ expansion)...
Reading makefile 'scripts/Makefile.extrawarn' (search path) (no ~ expansion)...
Reading makefile 'scripts/Makefile.ubsan' (search path) (no ~ expansion)...
Reading makefile '.vmlinux.cmd' (search path) (no ~ expansion)...
Reading makefiles...
Reading makefile '/home/chenwx/linux/scripts/Makefile.build'...
Reading makefile 'include/config/auto.conf' (search path) (don't care) (no ~ expansion)...
Reading makefile 'scripts/Kbuild.include' (search path) (no ~ expansion)...
Reading makefile '/home/chenwx/linux/arch/x86/entry/syscalls/Makefile' (search path) (no ~ expansion)...
Reading makefile 'scripts/Makefile.lib' (search path) (no ~ expansion)...
...
```

#### 3.2.1A.2 Sub-Makefile

There is one Makefile in each sub-directory of *~/linux*. Currently, the number is 2211 in kernel v4.7.2:

```
chenwx@chenwx ~/linux $ find . -name Makefile | wc -l
2211
```

And there maybe one Kbuild file in some sub-directories:

```
chenwx@chenwx ~/linux $ find . -name Kbuild | wc -l
173
```

#### 3.2.1A.3 Makefile Scripts

Some support scripts of kbuild system are located in directory *scripts/*:

```
chenwx@chenwx ~/linux $ ll scripts/Kbuild.include
-rw-rw-r-- 1 chenwx chenwx 15K Aug 14 09:20 scripts/Kbuild.include

chenwx@chenwx ~/linux $ ll scripts/Makefile*
-rw-rw-r-- 1 chenwx chenwx 1.8K Jul 22 20:39 scripts/Makefile
-rw-rw-r-- 1 chenwx chenwx  683 Jul 22 20:39 scripts/Makefile.asm-generic
-rw-rw-r-- 1 chenwx chenwx  15K Jul 22 20:40 scripts/Makefile.build
-rw-rw-r-- 1 chenwx chenwx 2.9K Jul 22 20:39 scripts/Makefile.clean
-rw-rw-r-- 1 chenwx chenwx 1.3K Jul 22 20:39 scripts/Makefile.dtbinst
-rw-rw-r-- 1 chenwx chenwx 2.6K Jul 22 20:39 scripts/Makefile.extrawarn
-rw-rw-r-- 1 chenwx chenwx 2.1K Jul 22 20:39 scripts/Makefile.fwinst
-rw-rw-r-- 1 chenwx chenwx 4.7K Jul 22 20:39 scripts/Makefile.headersinst
-rwxrwxrwx 1 chenwx chenwx   68 Jul 22 04:32 scripts/Makefile.help
-rw-rw-r-- 1 chenwx chenwx 4.6K Jul 22 20:39 scripts/Makefile.host
-rw-rw-r-- 1 chenwx chenwx  934 Jul 22 20:39 scripts/Makefile.kasan
-rw-rw-r-- 1 chenwx chenwx  15K Jul 22 20:40 scripts/Makefile.lib
-rwxrwxrwx 1 chenwx chenwx 1.8K Jul 22 04:32 scripts/Makefile.modbuiltin
-rw-rw-r-- 1 chenwx chenwx 1.3K Jul 22 20:39 scripts/Makefile.modinst
-rw-rw-r-- 1 chenwx chenwx 5.3K Jul 22 20:39 scripts/Makefile.modpost
-rw-rw-r-- 1 chenwx chenwx 1005 Jul 22 20:39 scripts/Makefile.modsign
-rw-rw-r-- 1 chenwx chenwx 1.1K Jul 22 20:39 scripts/Makefile.ubsan
```

Those Makefile scripts are included in the top Makefile, and come into being a tree with Makefile, refer to [3.2.1A.1.1 Makefile Tree](#3-2-1a-1-1-makefile-tree).

### 3.2.2 Kbuild编译系统概述

#### 3.2.2.1 编译进内核/$(obj-y)

Kbuild Makefile规定所有编译进内核的目标文件都保存在$(obj-y)列表中，而该列表依赖于内核的配置。Kbuild编译$(obj-y)列表中的所有文件。然后，调用"$(LD) -r"将它们连接到*/build-in.o，该类文件会被顶层Makefile链接进vmlinux中。

注意：在Documentation/kbuild/makefiles.txt中，包含下列描述：

> The order of files in $(obj-y) is significant. Duplicates in the lists are allowed: the first instance will be linked into built-in.o and succeeding instances will be ignored.

由此可知，$(obj-y)中文件的顺序是重要的！

**如何确定$(obj-y)中文件的顺序?**

可以根据下列几个方面来确定$(obj-y)中文件的顺序:

1) 确定目录及其子目录的编译顺序，参见[3.2.2.4 递归访问下级目录](#3-2-2-4-)节和[Appendix A: make -f scripts/Makefile.build obj=列表](#appendix-a-make-f-scripts-makefile-build-obj-)节;

2) 根据该目录中的Makefile及配置文件.config来确定该目录下文件的编译顺序。例如linux/fs/ext2/Makefile，根据宏CONFIG_EXT2_*的取值就可以确定文件的编译顺序了:

```
obj-$(CONFIG_EXT2_FS)            += ext2.o
ext2-y                           := balloc.o dir.o file.o ialloc.o inode.o \
                                    ioctl.o namei.o super.o symlink.o
ext2-$(CONFIG_EXT2_FS_XATTR)     += xattr.o xattr_user.o xattr_trusted.o
ext2-$(CONFIG_EXT2_FS_POSIX_ACL) += acl.o
ext2-$(CONFIG_EXT2_FS_SECURITY)  += xattr_security.o
```

#### 3.2.2.2 编译成模块/$(obj-m)

模块可以通过insmod命令加载。$(obj-m)列举出了哪些文件要编译成可加载模块。一个模块可以由一个或多个文件编译而成。如果是一个源文件，Kbuild Makefile只需简单的将其加到$(obj-m)中去就可以了。如果内核模块是由多个源文件编译而成，那就要采用下列方法声明所要编译的模块：

```
#drivers/isdn/i4l/Makefile
obj-$(CONFIG_FOO) += isdn.o
isdn-objs := isdn_net_lib.o isdn_v110.o isdn_common.o
```

Kbuild需要知道所编译的模块是基于哪些源文件，所以需要通过变量$(<module_name>-objs)来告诉它。在本例中，isdn是模块名，Kbuild将编译在$(isdn-objs)中列出的所有文件，然后使用"$(LD) -r"生成isdn.o。

注：上述语法同样适用于将源文件编译进内核。

#### 3.2.2.3 编译成库文件/$(lib-y)/$(lib-m)

在$(lib-y)中列出的文件用来编译成该目录下的一个库文件lib.a，例如lib/lib.a和arch/x86/lib/lib.a。通常，$(lib-y)用于lib/和arch/\*/lib目录。

在$(obj-y)与$(lib-y)中同时列出的文件，因为该文件在内核和库文件中都是可以访问的，所以该文件是不会被包含在库文件中的。在，$(lib-m)中的文件就要包含在lib.a库文件中。参见scripts/Makefile.lib:

```
# Figure out what we need to build from the various variables
# ===========================================================================

# When an object is listed to be built compiled-in and modular,
# only build the compiled-in version

obj-m := $(filter-out $(obj-y),$(obj-m))

# Libraries are always collected in one lib file.
# Filter out objects already built-in

lib-y := $(filter-out $(obj-y), $(sort $(lib-y) $(lib-m)))
```

注：Kbuild Makefile可以同时列出要编译进内核的文件和要编译成库的文件。所以，在一个目录里可以同时存在built-in.o和lib.a两个文件，例如由checksum.o和delay.o两个文件创建一个库文件lib.a：

```
#arch/x86/lib/Makefile
lib-y := chechsum.o delay.o
```

为了让Kbuild真正认识到这里要有一个库文件lib.a要创建，其所在的目录要加到$(libs-y)列表中，参见顶层Makefile:

```
libs-y	:= lib/

libs-y1	:= $(patsubst %/, %/lib.a, $(libs-y))
libs-y2	:= $(patsubst %/, %/built-in.o, $(libs-y))
libs-y	:= $(libs-y1) $(libs-y2)

vmlinux-main := $(core-y) $(libs-y) $(drivers-y) $(net-y)
```

此外，可以使用下列命令查看lib.a中包含的目标文件：

```
chenwx@chenwx ～/linux $ objdump -a lib/lib.a
In archive lib/lib.a:

argv_split.o:     file format elf32-i386
rw-r--r-- 0/0   1708 Jan  1 02:00 1970 argv_split.o

bug.o:     file format elf32-i386
rw-r--r-- 0/0   2256 Jan  1 02:00 1970 bug.o

cmdline.o:     file format elf32-i386
rw-r--r-- 0/0   1936 Jan  1 02:00 1970 cmdline.o

...
chenwx@chenwx ～/linux $ readelf -A lib/lib.a

File: lib/lib.a(argv_split.o)

File: lib/lib.a(bug.o)

File: lib/lib.a(cmdline.o)

...
```

#### 3.2.2.4 递归访问下级目录

一个Kbuild Makefile只对编译所在目录的对象负责。在子目录中文件的编译要由其所在子目录中的Makefile来管理。只要让Kbuild知道它应该递归操作，那么该系统就会在其子目录中自动的调用make递归操作，这就是$(obj-y)和$(obj-m)的作用。例如，ext2被放的一个单独的目录下，在fs目录下的Makefile会告诉Kbuild使用下面的赋值进行向下递归操作：

```
# fs/Makefile
obj-$(CONFIG_EXT2_FS) += ext2/
```

如果CONFIG_EXT2_FS被设置为'y'(编译进内核)或是'm'(编译成模块)，相应的obj-变量就会被设置，故Kbuild就会递归向下访问ext2目录。Kbuild只是用这些信息来决定是否需要访问该目录，而具体怎么编译由该目录中的Makefile来决定，参见编译$(obj)下的子目录节。

[**NOTE**] 将CONFIG_变量设置成目录名是一个好的编程习惯，这让Kbuild在完全忽略那些相应的CONFIG_值不是'y'和'm'的目录。

#### 3.2.2.5 编译标志

Kbuild编译系统中用到的编译标志包括：

```
EXTRA_CFLAGS		// 用$(CC)编译C源文件时的选项
EXTRA_AFLAGS		// 针对每个目录的选项，只不过它是用来编译汇编源代码的
EXTRA_LDFLAGS
EXTRA_ARFLAGS
CFLAGS_$@		// 是$(CC)针对每个文件的选项，而不是目录。$@ 表明了具体操作的文件
AFLAGS_$@
```

这些EXTRA_开头的大写字母变量都是编译标志，所有的EXTRA_变量只在所定义的Kbuild Makefile中起作用。EXTRA_变量可以在Kbuild Makefile中所有命令中使用。

参见[Documentation/kbuild/makefiles.txt](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/kbuild/makefiles.txt)第3.7 Compilation flags节。

### 3.2.3 Make命令

make命令：

```
# make help   // 帮助信息，参见下表
# make V=1    // 输出详细命令，默认V=0
# make -n     // 仅打印出要执行的命令，并不进行实际编译
# make -j4    // 可加快编译速度
```

对于kernel v3.18而言，make help打印下列帮助信息：

```
chenwx@chenwx ~/linux $ make help
Cleaning targets:
  clean			- Remove most generated files but keep the config and
			  enough build support to build external modules
  mrproper		- Remove all generated files + config + various backup files
  distclean		- mrproper + remove editor backup and patch files

Configuration targets:
  config		- Update current config utilising a line-oriented program
  nconfig		- Update current config utilising a ncurses menu based program
  menuconfig		- Update current config utilising a menu based program
  xconfig		- Update current config utilising a QT based front-end
  gconfig		- Update current config utilising a GTK based front-end
  oldconfig		- Update current config utilising a provided .config as base
  localmodconfig	- Update current config disabling modules not loaded
  localyesconfig	- Update current config converting local mods to core
  silentoldconfig	- Same as oldconfig, but quietly, additionally update deps
  defconfig		- New config with default from ARCH supplied defconfig
  savedefconfig		- Save current config as ./defconfig (minimal config)
  allnoconfig		- New config where all options are answered with no
  allyesconfig		- New config where all options are accepted with yes
  allmodconfig		- New config selecting modules when possible
  alldefconfig		- New config with all symbols set to default
  randconfig		- New config with random answer to all options
  listnewconfig		- List new options
  olddefconfig		- Same as silentoldconfig but sets new symbols to their default value
  kvmconfig		- Enable additional options for guest kernel support
  tinyconfig		- Configure the tiniest possible kernel

Other generic targets:
  all			- Build all targets marked with [*]
* vmlinux		- Build the bare kernel
* modules		- Build all modules
  modules_install	- Install all modules to INSTALL_MOD_PATH (default: /)
  firmware_install	- Install all firmware to INSTALL_FW_PATH
			  (default: $(INSTALL_MOD_PATH)/lib/firmware)
  dir/			- Build all files in dir and below
  dir/file.[oisS]	- Build specified target only
  dir/file.lst		- Build specified mixed source/assembly target only
			  (requires a recent binutils and recent build (System.map))
  dir/file.ko		- Build module including final link
  modules_prepare	- Set up for building external modules
  tags/TAGS		- Generate tags file for editors
  cscope		- Generate cscope index
  gtags			- Generate GNU GLOBAL index
  kernelrelease		- Output the release version string (use with make -s)
  kernelversion		- Output the version stored in Makefile (use with make -s)
  image_name		- Output the image name (use with make -s)
  headers_install	- Install sanitised kernel headers to INSTALL_HDR_PATH
			  (default: ./usr)

Static analysers
  checkstack		- Generate a list of stack hogs
  namespacecheck	- Name space analysis on compiled kernel
  versioncheck		- Sanity check on version.h usage
  includecheck		- Check for duplicate included header files
  export_report		- List the usages of all exported symbols
  headers_check		- Sanity check on exported headers
  headerdep		- Detect inclusion cycles in headers
  coccicheck		- Check with Coccinelle.

Kernel selftest
  kselftest		- Build and run kernel selftest (run as root)
			  Build, install, and boot kernel before
			  running kselftest on it

Kernel packaging:
  rpm-pkg		- Build both source and binary RPM kernel packages
  binrpm-pkg		- Build only the binary kernel package
  deb-pkg		- Build the kernel as a deb package
  tar-pkg		- Build the kernel as an uncompressed tarball
  targz-pkg		- Build the kernel as a gzip compressed tarball
  tarbz2-pkg		- Build the kernel as a bzip2 compressed tarball
  tarxz-pkg		- Build the kernel as a xz compressed tarball
  perf-tar-src-pkg	- Build perf-3.18.0.tar source tarball
  perf-targz-src-pkg	- Build perf-3.18.0.tar.gz source tarball
  perf-tarbz2-src-pkg	- Build perf-3.18.0.tar.bz2 source tarball
  perf-tarxz-src-pkg	- Build perf-3.18.0.tar.xz source tarball

Documentation targets:
 Linux kernel internal documentation in different formats:
  htmldocs		- HTML
  pdfdocs		- PDF
  psdocs		- Postscript
  xmldocs		- XML DocBook
  mandocs		- man pages
  installmandocs	- install man pages generated by mandocs
  cleandocs		- clean all generated DocBook files

Architecture specific targets (x86):
* bzImage		- Compressed kernel image (arch/x86/boot/bzImage)
  install		- Install kernel using
			  (your) ~/bin/installkernel or
			  (distribution) /sbin/installkernel or
			  install to $(INSTALL_PATH) and run lilo
  fdimage		- Create 1.4MB boot floppy image (arch/x86/boot/fdimage)
  fdimage144		- Create 1.4MB boot floppy image (arch/x86/boot/fdimage)
  fdimage288		- Create 2.8MB boot floppy image (arch/x86/boot/fdimage)
  isoimage		- Create a boot CD-ROM image (arch/x86/boot/image.iso)
			  bzdisk/fdimage*/isoimage also accept:
			  FDARGS="..."  arguments for the booted kernel
			  FDINITRD=file initrd for the booted kernel

  i386_defconfig	- Build for i386
  x86_64_defconfig	- Build for x86_64

  make V=0|1 [targets]   0 => quiet build (default), 1 => verbose build
  make V=2   [targets]   2 => give reason for rebuild of target
  make O=dir [targets]   Locate all output files in "dir", including .config
  make C=1   [targets]   Check all c source with $CHECK (sparse by default)
  make C=2   [targets]   Force check of all c source with $CHECK
  make RECORDMCOUNT_WARN=1 [targets]   Warn about ignored mcount sections
  make W=n   [targets]   Enable extra gcc checks, n=1,2,3 where
		1: warnings which may be relevant and do not occur too often
		2: warnings which occur quite often but may still be relevant
		3: more obscure warnings, can most likely be ignored
		Multiple levels can be combined with W=12 or W=123

Execute "make" or "make all" to build all targets marked with [*]
For further info see the ./README file
```

## 3.3 内核配置

内核版本号由顶层Makefile中的下列变量决定的：

```
VERSION = 3
PATCHLEVEL = 2
SUBLEVEL = 0
EXTRAVERSION =

# Read KERNELRELEASE from include/config/kernel.release (if it exists)
KERNELRELEASE = $(shell cat include/config/kernel.release 2> /dev/null)
KERNELVERSION = $(VERSION)$(if $(PATCHLEVEL),.$(PATCHLEVEL)$(if $(SUBLEVEL),.$(SUBLEVEL)))$(EXTRAVERSION)
```

可以更改EXTRAVERSION的取值来定义自己的版本号。例如，EXTRAVERSION = -chenwx，则新内核的版本号为3.2.0-chenwx，可通过下列命令查看：

```
chenwx@chenwx ~/linux $ make kernelrelease
scripts/kconfig/conf --silentoldconfig Kconfig
3.2.1-chenwx
```

### 3.3.0 Create Output Directory

It's better to build Linux kernel on a directory outside of local kernel repository, such as *~/linux-build*. In order to use another directory to build Linux kernel, the repository should be clean up:

```
chenwx@chenwx ~/linux $ make distclean
chenwx@chenwx ~/linux $ mkdir ../linux-build
```

And then, use parameter ```O=../linux-build/``` in each make command later, such as configure Linux kernel:

```
chenwx@chenwx ~/linux $ make O=../linux-build/ menuconfig
```

### 3.3.1 make config

执行make config的流程：

![make_config_1](/assets/make_config_1.jpg)

执行make config命令，会调用顶层Makefile中的config目标：

```
// 定义$(build)变量
include $(srctree)/scripts/Kbuild.include

// 目标config参见config节
config: scripts_basic outputmakefile FORCE
	// 创建目录
	$(Q)mkdir -p include/linux include/config
	/*
	 * $(build)定义于scripts/Kbuild.include
	 * 扩展为 $(MAKE) -f scripts/Makefile.build obj=scripts/kconfig config
	 */
	$(Q)$(MAKE) $(build)=scripts/kconfig $@			

// 编译script/basic/fixdep，参见scripts_basic节
scripts_basic:
	// 扩展为 $(MAKE) -f scripts/Makefile.build obj=scripts/basic
	$(Q)$(MAKE) $(build)=scripts/basic
	$(Q)rm -f .tmp_quiet_recordmcount

// 参见outputmakefile节
outputmakefile:
ifneq ($(KBUILD_SRC),)
	$(Q)ln -fsn $(srctree) source
	// 执行脚本scripts/mkmakefile，用于在$(objtree)指定的目录中生成Makefile
	$(Q)$(CONFIG_SHELL) $(srctree)/scripts/mkmakefile \
	    $(srctree) $(objtree) $(VERSION) $(PATCHLEVEL)
endif

// 因为本规则没有依赖，目标FORCE总会被认为是最新的，所以规则中定义的命令总会被执行
FORCE:
```

#### 3.3.1.1 scripts_basic

在顶层Makefile中，包含下列规则：

```
// 定义$(build)变量
include $(srctree)/scripts/Kbuild.include

// 编译scripts/basic/fixdep
scripts_basic:
	$(Q)$(MAKE) $(build)=scripts/basic
	$(Q)rm -f .tmp_quiet_recordmcount	// 参见scripts/recordmcount.pl
```

$(build)定义于scripts/Kbuild.include:

```
build := -f $(if $(KBUILD_SRC),$(srctree)/)scripts/Makefile.build obj
```

因此，$(Q)$(MAKE) $(build)=scripts/basic被扩展为：

```
$(Q)$(MAKE) -f scripts/Makefile.build obj=scripts/basic
```

该命令用于编译scripts/basic目录。由于未指定编译目标，故编译scripts/Makefile.build中的默认目标__build：

```
PHONY := __build
__build:

...
__build: $(if $(KBUILD_BUILTIN),$(builtin-target) $(lib-target) $(extra-y))	\
		   $(if $(KBUILD_MODULES),$(obj-m) $(modorder-target))		\
		   $(subdir-ym) $(always)
	@:
```

而其中的$(always)则是由scripts/basic/Makefile引入的。

首先，scripts/Makefile.build中的下列语句将scripts/basic/Makefile包含进来：

```
// 扩展为kbuild-dir := script/basic
kbuild-dir := $(if $(filter /%,$(src)),$(src),$(srctree)/$(src))
// 扩展为kbuild-file := script/basic/Makefile
kbuild-file := $(if $(wildcard $(kbuild-dir)/Kbuild),$(kbuild-dir)/Kbuild,$(kbuild-dir)/Makefile)
// 此处将script/basic/Makefile包含进来
include $(kbuild-file)
```

其次，根据scripts/basic/Makefile中的规则：

```
hostprogs-y	:= fixdep
always		:= $(hostprogs-y)

# fixdep is needed to compile other host programs
$(addprefix $(obj)/,$(filter-out fixdep,$(always))): $(obj)/fixdep
```

可知，$(always)的取值为fixdep。

那么，fixdep是如何被编译出来的呢？

1) scripts/Makefile.build中的下列语句将scripts/Makefile.host包含进来：

```
# Do not include host rules unless needed
// 由scripts/basic/Makefile可知，$(hostprogs-y)=fixdep
ifneq ($(hostprogs-y)$(hostprogs-m),)
include scripts/Makefile.host
endif
```

2) 在scripts/Makefile.host中，包含下列编译fixdep的规则：

```
// 扩展为__hostprogs := fixdep
__hostprogs := $(sort $(hostprogs-y) $(hostprogs-m))

# C code
# Executables compiled from a single .c file
// 扩展为host-csingle := fixdep
host-csingle	:= $(foreach m,$(__hostprogs),$(if $($(m)-objs),,$(m)))

// 扩展为host-csingle := scripts/basic/fixdep
host-csingle	:= $(addprefix $(obj)/,$(host-csingle))

# Create executable from a single .c file
# host-csingle -> Executable
quiet_cmd_host-csingle 	= HOSTCC  $@
      cmd_host-csingle	= $(HOSTCC) $(hostc_flags) -o $@ $< \
	  	$(HOST_LOADLIBES) $(HOSTLOADLIBES_$(@F))

// 此处的%为fixdep，故fixdep由fixdep.c编译而来的
$(host-csingle): $(obj)/%: $(src)/%.c FORCE
	// 调用cmd_host-csingle来实际编译fixdep
	$(call if_changed_dep,host-csingle)
```

注：在linux-2.6.18中，script/basic目录中包含两个程序：fixdep, docproc

#### 3.3.1.2 outputmakefile

在顶层Makefile中，包含下列规则：

```
outputmakefile:
// 由命令行中传入该参数，如make -f ../linux/Makefile KBUILD_SRC=../linux/ config
ifneq ($(KBUILD_SRC),)
	$(Q)ln -fsn $(srctree) source				// source链接到KBUILD_SRC所代表的目录
	$(Q)$(CONFIG_SHELL) $(srctree)/scripts/mkmakefile \
	    $(srctree) $(objtree) $(VERSION) $(PATCHLEVEL)	// $(objtree)为执行make命令时的当前目录
endif
```

该规则执行脚本scripts/mkmakefile，在输出目录$(objtree)中生成Makefile文件，以便于在目录$(objtree)中直接执行make命令即可编译内核。

举例，假设目录结构如下：

```
~/
 +- linux/			// 包含linux 3.2版本的内核源代码
 +- linux-build/		// 输出目录
```

在～/linux/目录执行下列命令：

```
chenwx@chenwx ~/linux $ mkdir ../linux-build
chenwx@chenwx ~/linux $ make O=../linux-build/ outputmakefile
  HOSTCC  scripts/basic/fixdep
  GEN     /home/chenwx/linux-build/Makefile
  HOSTCC  scripts/kconfig/conf.o
  SHIPPED scripts/kconfig/zconf.tab.c
  SHIPPED scripts/kconfig/zconf.lex.c
  SHIPPED scripts/kconfig/zconf.hash.c
  HOSTCC  scripts/kconfig/zconf.tab.o
  HOSTLD  scripts/kconfig/conf
scripts/kconfig/conf --silentoldconfig Kconfig
***
*** Configuration file ".config" not found!
***
*** Please run some configurator (e.g. "make oldconfig" or
*** "make menuconfig" or "make xconfig").
***
/home/chenwx/linux/scripts/kconfig/Makefile:33: recipe for target 'silentoldconfig' failed
make[3]: *** [silentoldconfig] Error 1
/home/chenwx/linux/Makefile:492: recipe for target 'silentoldconfig' failed
make[2]: *** [silentoldconfig] Error 2
  GEN     /home/chenwx/linux-build/Makefile
```

则会在~/linux-build/目录中生成Makefile文件，以后直接在~/linux-build/目录执行make命令就可编译内核了。生成的Makefile如下：

```
# Automatically generated by /home/chenwx/linux/scripts/mkmakefile: don't edit

VERSION = 3
PATCHLEVEL = 2

lastword = $(word $(words $(1)),$(1))
makedir := $(dir $(call lastword,$(MAKEFILE_LIST)))

ifeq ("$(origin V)", "command line")
VERBOSE := $(V)
endif
ifneq ($(VERBOSE),1)
Q := @
endif

MAKEARGS := -C /home/chenwx/linux
MAKEARGS += O=$(if $(patsubst /%,,$(makedir)),$(CURDIR)/)$(patsubst %/,%,$(makedir))

MAKEFLAGS += --no-print-directory

.PHONY: all $(MAKECMDGOALS)

all	:= $(filter-out all Makefile,$(MAKECMDGOALS))

all:
	$(Q)$(MAKE) $(MAKEARGS) $(all)

Makefile:;

$(all): all
	@:

%/: all
	@:
```

那么，在～/linux-build/目录执行make config命令时，其执行过程是怎样的呢？

1) 根据～/linux-build/Makefile中的规则，执行make config命令时，实际执行下列规则：

```
all:
	$(Q)$(MAKE) $(MAKEARGS) $(all)
```

该规则被扩展为：

```
make -C /home/chenwx/linux O=/home/chenwx/linux-build/ config
```

2) 根据顶层Makefile中的下列规则，继而执行其中的sub-make规则：

```
ifneq ($(KBUILD_OUTPUT),)
# Invoke a second make in the output directory, passing relevant variables
# check that the output directory actually exists
saved-output := $(KBUILD_OUTPUT)
KBUILD_OUTPUT := $(shell cd $(KBUILD_OUTPUT) && /bin/pwd)
$(if $(KBUILD_OUTPUT),, \
     $(error output directory "$(saved-output)" does not exist))

PHONY += $(MAKECMDGOALS) sub-make

$(filter-out _all sub-make $(CURDIR)/Makefile, $(MAKECMDGOALS)) _all: sub-make
	$(Q)@:

sub-make: FORCE
	$(if $(KBUILD_VERBOSE:1=),@)$(MAKE) -C $(KBUILD_OUTPUT) \
	KBUILD_SRC=$(CURDIR) \
	KBUILD_EXTMOD="$(KBUILD_EXTMOD)" -f $(CURDIR)/Makefile \
	$(filter-out _all sub-make,$(MAKECMDGOALS))

# Leave processing to above invocation of make
skip-makefile := 1
endif # ifneq ($(KBUILD_OUTPUT),)
```

该规则被扩展为：

```
make -C /home/chenwx/linux-build/ \
	KBUILD_SRC=/home/chenwx/linux \
	KBUILD_EXTMOD="" -f /home/chenwx/linux-build/Makefile \
	config
```

此后，make config的编译过程与[3.3.1 make config](#3-3-1-make-config)节完全相同。

#### 3.3.1.3 config

在顶层Makefile中，包含下列有关config的规则：

```
config: scripts_basic outputmakefile FORCE
	$(Q)mkdir -p include/linux include/config
	$(Q)$(MAKE) $(build)=scripts/kconfig $@
```

首先，创建两个目录：include/linux和include/config。

其次，根据scripts/Kbuild.include中对$(build)的定义：

```
build := -f $(if $(KBUILD_SRC),$(srctree)/)scripts/Makefile.build obj
```

$(Q)$(MAKE) $(build)=scripts/kconfig $@ 被扩展为：

```
$(Q)$(MAKE) -f scripts/Makefile.build obj=scripts/kconfig config
```

而scripts/Makefile.build中的下列语句将scripts/kconfig/Makefile包含进来：

```
// 扩展为kbuild-dir := script/kconfig
kbuild-dir := $(if $(filter /%,$(src)),$(src),$(srctree)/$(src))
// 扩展为kbuild-file := script/kconfig/Makefile
kbuild-file := $(if $(wildcard $(kbuild-dir)/Kbuild),$(kbuild-dir)/Kbuild,$(kbuild-dir)/Makefile)
// 此处将script/kconfig/Makefile包含进来
include $(kbuild-file)

因而，make config的最终目标为scripts/kconfig/Makefile中的config：
ifdef KBUILD_KCONFIG			// 此处，变量KBUILD_KCONFIG未定义
	Kconfig := $(KBUILD_KCONFIG)
else
	Kconfig := Kconfig		// 故进入本分支
endif
...
config: $(obj)/conf
	$< --oldaskconfig $(Kconfig)
...
conf-objs	:= conf.o  zconf.tab.o	// conf-objs用于scripts/Makefile.host中的host-cobjs变量
...
hostprogs-y := conf
...
$(obj)/zconf.tab.o: $(obj)/zconf.lex.c $(obj)/zconf.hash.c
```

而config又依赖于$(obj)/conf，因此需要先编译$(obj)/conf。

那么，$(obj)/conf是如何编译链接的呢？

1) 由scripts/Makefile.host中的下列规则：

```
__hostprogs := $(sort $(hostprogs-y) $(hostprogs-m))			// __hostprogs := conf
...
# Object (.o) files compiled from .c files
host-cobjs	:= $(sort $(foreach m,$(__hostprogs),$($(m)-objs)))	// host-cobjs := conf-objs
...
# Create .o file from a single .c file
# host-cobjs -> .o
quiet_cmd_host-cobjs	= HOSTCC  $@
      cmd_host-cobjs	= $(HOSTCC) $(hostc_flags) -c -o $@ $<
$(host-cobjs): $(obj)/%.o: $(src)/%.c FORCE
	$(call if_changed_dep,host-cobjs)				// 调用cmd_host-cobjs编译
```

可知，conf.o由conf.c编译而来，zconf.tab.o由zconf.lex.c和zconf.hash.c编译而来。

2) 然后再根据scripts/Makefile.host中的下列规则：

```
# C executables linked based on several .o files
host-cmulti	:= $(foreach m,$(__hostprogs),\			// host-cmulti := conf
		   $(if $($(m)-cxxobjs),,$(if $($(m)-objs),$(m))))
...
host-cmulti	:= $(addprefix $(obj)/,$(host-cmulti))		// host-cmulti := scripts/Kconfig/conf
...
# Link an executable based on list of .o files, all plain c
# host-cmulti -> executable
quiet_cmd_host-cmulti	= HOSTLD  $@
      cmd_host-cmulti	= $(HOSTCC) $(HOSTLDFLAGS) -o $@	\
			  $(addprefix $(obj)/,$($(@F)-objs)) 	\
			  $(HOST_LOADLIBES) $(HOSTLOADLIBES_$(@F))
$(host-cmulti): $(obj)/%: $(host-cobjs) $(host-cshlib) FORCE
	$(call if_changed,host-cmulti)				// 调用cmd_host-cmulti链接各.o文件生成conf
```

将conf.o和zconf.tab.o链接生成conf可执行文件。

在scripts/kconfig/Makefile中，目标config下的规则 $< --oldaskconfig $(Kconfig) 被扩展为：
scripts/kconfig/conf --oldaskconfig Kconfig

即调用conf程序解析顶层内核配置文件Kconfig(注：顶层配置文件中又引入与体系结构有关的配置文件，参见下文)，并将用户的配置结果输出到.config文件中(通过scripts\kconfig\confdata.c中的函数conf_write())。

```
config SRCARCH
	string
	option env="SRCARCH"
source "arch/$SRCARCH/Kconfig"
```

### 3.3.2 make \*config

执行make \*config的流程:

![make_config.all](/assets/make_config.all.jpg)

参见linux/README中的下列命令：

```
make menuconfig		// Text based color menus, radiolists & dialogs
make nconfig		// Enhanced text based color menus
make xconfig		// X windows (Qt) based configuration tool
make gconfig		// X windows (Gtk) based configuration tool
make oldconfig		// Default all questions based on the contents of
			// your existing ./.config file and asking about new config symbols
make localmodconfig	// Update current config disabling modules not loaded
make localyesconfig	// Update current config converting local mods to core
make silentoldconfig	// Like “make oldconfig”, but avoids cluttering the screen
			// with questions already answered. Additionally updates dependencies
make oldnoconfig	// Same as silentoldconfig but sets new symbols to their default value
make defconfig		// Create file .config by using the default symbol values from either
			// arch/$ARCH/defconfig or arch/$ARCH/configs/${PLATFORM}_defconfig,
			// depending on the architecture
Make savedefconfig	// Save current config as ./defconfig (minimal config)
make ${PLATFORM}_defconfig
			// Create a ./.config file by using the default symbol values from
			// arch/$ARCH/configs/${PLATFORM}_defconfig. Use "make help" to get
			// a list of all available platforms of your architecture
make allyesconfig	// Create a ./.config file by setting symbol values to 'y' as much as possible
make allnoconfig	// Create a ./.config file by setting symbol values to 'n' as much as possible
make allmodconfig	// Create a ./.config file by setting symbol values to 'm' as much as possible
make alldefconfig	// New config with all symbols set to default
make randconfig		// Create a ./.config file by setting symbol values to random values
make listnewconfig	// List new options
```

注：可通过执行命令make help，查看系统支持的Configuration Targets.

执行make \*config命令，会调用顶层Makefile中的目标：

```
// 定义$(build)变量
include $(srctree)/scripts/Kbuild.include

// 下列两行与config相同，参见config节
%config: scripts_basic outputmakefile FORCE
	$(Q)mkdir -p include/linux include/config
	/*
	 * $(build)定义参见scripts/Kbuild.include
	 * $(MAKE) -f scripts/Makefile.build obj=scripts/kconfig *config
	 */
	$(Q)$(MAKE) $(build)=scripts/kconfig $@

// To build script/basic/fixdep，参见scripts_basic节
scripts_basic:
	// $(Q)$(MAKE) -f scripts/Makefile.build obj=scripts/basic
	$(Q)$(MAKE) $(build)=scripts/basic
	$(Q)rm -f .tmp_quiet_recordmcount

// 参见outputmakefile节
outputmakefile:
ifneq ($(KBUILD_SRC),)
	$(Q)ln -fsn $(srctree) source
	// 执行scripts/mkmakefile，该脚本在$(objtree)指定的目录中生成Makefile
	$(Q)$(CONFIG_SHELL) $(srctree)/scripts/mkmakefile \
	    $(srctree) $(objtree) $(VERSION) $(PATCHLEVEL)
endif

// 因为本规则没有依赖，目标FORCE总会被认为是最新的，所以规则中定义的命令总会被执行
FORCE:
```

%config: scripts_basic outputmakefile FORCE的下列语句：

```
$(Q)$(MAKE) $(build)=scripts/kconfig $@			// $(build)定义于scripts/Kbuild.include
```

被扩展后，变为：

```
$(Q)$(MAKE) -f scripts/Makefile.build obj=scripts/kconfig *config
```

而scripts/Makefile.build中的下列语句将scripts/kconfig/Makefile包含进来：

```
// 扩展为kbuild-dir := script/kconfig
kbuild-dir := $(if $(filter /%,$(src)),$(src),$(srctree)/$(src))
// 扩展为kbuild-file := script/kconfig/Makefile
kbuild-file := $(if $(wildcard $(kbuild-dir)/Kbuild),$(kbuild-dir)/Kbuild,$(kbuild-dir)/Makefile)
// 此处将script/kconfig/Makefile包含进来
include $(kbuild-file)
```

因而，make config的最终目标为scripts/kconfig/Makefile中的*config：

```
xconfig: $(obj)/qconf
	$< $(Kconfig)			// 扩展为scripts/kconfig/qconf Kconfig

gconfig: $(obj)/gconf
	$< $(Kconfig)			// 扩展为scripts/kconfig/gconf Kconfig

menuconfig: $(obj)/mconf
	$< $(Kconfig)			// 扩展为scripts/kconfig/mconf Kconfig

nconfig: $(obj)/nconf
	$< $(Kconfig)			// 扩展为scripts/kconfig/nconf Kconfig

oldconfig: $(obj)/conf
	$< --$@ $(Kconfig)		// 扩展为scripts/kconfig/conf --oldconfig Kconfig

silentoldconfig: $(obj)/conf
	$(Q)mkdir -p include/generated
	$< --$@ $(Kconfig)		// 扩展为scripts/kconfig/conf --silentoldconfig Kconfig

allnoconfig allyesconfig allmodconfig alldefconfig randconfig: $(obj)/conf
	$< --$@ $(Kconfig)		// 扩展为scripts/kconfig/conf --$@ Kconfig

defconfig: $(obj)/conf
ifeq ($(KBUILD_DEFCONFIG),)
	$< --defconfig $(Kconfig)	// 扩展为scripts/kconfig/conf –defconfig Kconfig
else
	@echo "*** Default configuration is based on '$(KBUILD_DEFCONFIG)'"
	// 扩展为scripts/kconfig/conf --defconfig=arch/$(SRCARCH)/config/$(KBUILD_DEFCONFIG) Kconfig
	$(Q)$< --defconfig=arch/$(SRCARCH)/configs/$(KBUILD_DEFCONFIG) $(Kconfig)
endif

%_defconfig: $(obj)/conf
	// 扩展为scripts/kconfig/conf --defconfig=arch/$(SRCARCH)/configs/$@ Kconfig
	$(Q)$< --defconfig=arch/$(SRCARCH)/configs/$@ $(Kconfig)
```

make \*config的具体编译链接过程与[3.3.1 make config](#3-3-1-make-config)节类似。

[**NOTE1**] It's entirely possible that that existing .config you used as the basis for your configuration isn't quite up to date; that is, it may have no entries representing extremely new features that have been added to the kernel. If that's the case, the "make oldconfig" will stop at each one of those choices and ask you what to do. And if you're new to building a kernel, you may not know the right answer. One solution is to just keep hitting ENTER and take the default, but that can get tedious. A faster solution is:

```
// two single quotes, no space between
chenwx ~/linux # yes '' | make oldconfig
```

[**NOTE2**] Perhaps the most useful target for beginners is defconfig (short for "default config") which simply sets your .config to an established set of defaults for your system and architecture. And how can you see these defaults? Simple -- from the top of the kernel source tree, just run following command, and you'll see dozens of default config files for all of the kernel's supported architectures.

```
chenwx ~/linux # find arch -name "*defconfig"
```

#### 3.3.2.1 Use Old Existed Configure

In order to build Linux kernel, build it based on the old existed configure */boot/config-4.4.0-15-generic*:

```
chenwx@chenwx ~/linux $ cp /boot/config-4.4.0-15-generic ../linux-build/.config

chenwx@chenwx ~/linux $ make O=../linux-build/ olddefconfig
make[1]: Entering directory '/home/chenwx/linux-build'
  HOSTCC  scripts/basic/fixdep
  GEN     ./Makefile
  HOSTCC  scripts/kconfig/conf.o
  SHIPPED scripts/kconfig/zconf.tab.c
  SHIPPED scripts/kconfig/zconf.lex.c
  SHIPPED scripts/kconfig/zconf.hash.c
  HOSTCC  scripts/kconfig/zconf.tab.o
  HOSTLD  scripts/kconfig/conf
scripts/kconfig/conf  --olddefconfig Kconfig
.config:1631:warning: symbol value 'm' invalid for RXKAD
.config:3586:warning: symbol value 'm' invalid for SERIAL_8250_FINTEK
#
# configuration written to .config
#
make[1]: Leaving directory '/home/chenwx/linux-build'
```

I like to use the command ```make menuconfig``` to configure linux kernel because it much more easier to use it.

### 3.3.3 Kconfig/内核配置选项文件

内核配置文件包括：

* Kconfig
* arch/$(SRCARCH)/Kconfig
* ...

其说明参见：

* [Documentation/kbuild/kconfig.txt](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/kbuild/kconfig.txt)
* [Documentation/kbuild/kconfig-language.txt](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/kbuild/kconfig-language.txt)

Linux Kernel中的所有Kconfig文件形成了一棵树，参见[Appendix C: Kconfig tree](#appendix-c-kconfig-tree)。

### 3.3.4 .config/内核配置结果文件

#### 3.3.4.1 .config的格式

在[3.3.1 make config](#3-3-1-make-config)节和[3.3.2 make \*config](#3-3-2-make-config)节中生成的conf等配置程序读取内核配置选项文件Kconfig中的内核配置信息，并根据用户的选择，生成内核配置结果文件.config，以供后续编译内核时使用(顶层Makefile会读取该文件，参见[3.3.4.2 .config如何被顶层Makefile调用](#3-3-4-2-config-makefile-)节)。内核配置结果文件.config中包含下列内容：

```
# CONFIG_64BIT is not set
CONFIG_X86_32=y
# CONFIG_X86_64 is not set
CONFIG_X86=y
CONFIG_INSTRUCTION_DECODER=y
CONFIG_OUTPUT_FORMAT="elf32-i386"
CONFIG_ARCH_DEFCONFIG="arch/x86/configs/i386_defconfig"
CONFIG_LOCKDEP_SUPPORT=y
CONFIG_STACKTRACE_SUPPORT=y
...
```

#### 3.3.4.2 .config如何被顶层Makefile调用

由[3.4.2 编译bzImage/$(obj-y)](#3-4-2-bzimage-obj-y-)节和[3.4.3 编译modules/$(obj-m)](#3-4-3-modules-obj-m-)节可知，在编译内核和模块时，其目标都要依赖于$(vmlinux-dirs)。而由[3.4.2.1.3 $(vmlinux-dirs)](#3-4-2-1-3-vmlinux-dirs-)节和[3.4.2.1.1 prepare](#3-4-2-1-1-prepare)节可知，存在下列依赖关系：

```
$(vmlinux-dirs) <= prepare <= prepare0 <= archprepare <= prepare1 <= include/config/auto.conf
```

而由[3.4.2.1.1.1 include/config/auto.conf](#3-4-2-1-1-1-include-config-auto-conf)节可知，include/config/auto.conf是由.config生成的。需要理解下列两点：

1) 执行make \*config命令，将会生成配置文件.config，参见[3.3.1 make config](#3-3-1-make-config)节和[3.3.2 make \*config](#3-3-2-make-config)节；

2) 执行make silentoldconfig命令(执行本命令的前提条件是，系统中必须已存在配置文件.config)，将会同时生成下列三个文件:

**include/config/auto.conf**

与.config文件中的配置完全相同 (注意：这两个文件中行的顺序可能不同，可通过执行下列命令来比较这两个文件的差异):

```
chenwx@chenwx ~/linux $ cd ../linux-build
chenwx@chenwx ~/linux-build $ sort .config > config.sort
chenwx@chenwx ~/linux-build $ sort .config > .config.sort
chenwx@chenwx ~/linux-build $ sed '/#/d' .config.sort > .config.sort.sed
chenwx@chenwx ~/linux-build $ sort include/config/auto.conf > auto.conf.sort
chenwx@chenwx ~/linux-build $ sed '/#/d' auto.conf.sort > auto.conf.sort.sed
chenwx@chenwx ~/linux-build $ diff -B .config.sort.sed auto.conf.sort.sed
chenwx@chenwx ~/linux-build $
```

**include/config/auto.conf.cmd**

本文件包含了生成配置文件include/config/auto.conf时所用到的Kconfig文件。

**include/config/tristate.conf**

本文件包含了include/config/auto.conf中的部分配置信息，且全为大写字母。

由于include/config/auto.conf与.config完全相同，因此顶层Makefile通过下列语句将.config包含进编译系统中(注意：当include/config/auto.conf生成后，make会重新读取Makefile文件，因而可以通过该语句读取最新的include/config/auto.conf)：

```
# Read in config
-include include/config/auto.conf;
```

当满足下列条件之一时：

* 不存在include/config/auto.conf时，
* .config比include/config/auto.conf要新时，
* include/config/auto.conf.cmd中包含的任意Kconfig文件比include/config/auto.conf要新时，

将调用顶层Makefile中的下列规则，创建或更新include/config/auto.conf和include/config/auto.conf.cmd文件，此时更新后的include/config/auto.conf与系统中已存在的.config文件完全相同，因而可以自动包含最新的配置：

```
# If .config is newer than include/config/auto.conf, someone tinkered
# with it and forgot to run make oldconfig.
# if auto.conf.cmd is missing then we are probably in a cleaned tree so
# we execute the config step to be sure to catch updated Kconfig files
include/config/%.conf: $(KCONFIG_CONFIG) include/config/auto.conf.cmd
	// 扩展为make scripts/kconfig/conf --silentoldconfig
	$(Q)$(MAKE) -f $(srctree)/Makefile silentoldconfig
```

## 3.4 内核编译

Linux内核的Makefile分为下列5个部分：

```
Makefile			- 顶层Makefile
.config				- 内核配置结果文件，参见.config/内核配置结果文件节
arch/$(ARCH)/Makefile		- 具体架构的Makefile
scripts/Makefile.*		- 通用的规则等，面向所有的Kbuild Makefiles
Kbuild Makefiles		- 内核源代码中大约有500个这样的文件(文件名为Kbuild)
```

**Makefile**

The top Makefile reads the .config file, which comes from the kernel configuration process. The top Makefile is responsible for building two major products: vmlinux (the resident kernel image) and modules (any module files). It builds these goals by recursively descending into the subdirectories of the kernel source tree.

**\*/Kbuild**

每一个子目录都有一个Kbuild Makefile文件，用来执行从其上层目录传递下来的命令。Kbuild Makefile从.config文件中提取信息，生成Kbuild完成内核编译所需的文件列表。

**scripts/Makefile.***

包含了所有的定义、规则等信息。这些文件被用来编译基于Kbuild Makefile的内核。这些文件包括：

```
Makefile.asm-generic
Makefile.build
Makefile.clean
Makefile.fwinst
Makefile.headersinst
Makefile.help
Makefile.host
Makefile.lib
Makefile.modbuiltin
Makefile.modinst
Makefile.modpost
```

各Makefile之间存在调用关系，这形成了一棵树，参见[Appendix B: Makefile Tree](#appendix-b-makefile-tree)节。

### 3.4.1 Makefile的Default Target

【**GNU Make知识点**】

根据《GNU make v3.8.2》第4.10节可知：

> One file can be the target of several rules. All the prerequisites mentioned in all the rules are merged into one list of prerequisites for the target. If the target is older than any prerequisite from any rule, the recipe is executed.
>
> There can only be one recipe to be executed for a file. If more than one rule gives a recipe for the same file, make uses the last one given and prints an error message. (As a special case, if the file’s name begins with a dot, no error message is printed. This odd behavior is only for compatibility with other implementations of make - you should avoid using it). Occasionally it is useful to have the same target invoke multiple recipes which are defined in different parts of your makefile; you can use double-colon rules for this.

顶层Makefile及其包含的Makefile，包含如下规则：

1) 来自顶层Makefile

```
# That's our default target when none is given on the command line
PHONY := _all
_all:

# If building an external module we do not care about the all: rule
# but instead _all depend on modules
PHONY += all
/*
 * 若仅执行make命令，则$(KBUILD_EXTMOD)为空
 * 若执行make M=dir或make ... SUBDIRS=$PWD命令，则$(KBUILD_EXTMOD)不为空
 */
ifeq ($(KBUILD_EXTMOD),)
_all: all			// 若仅执行make命令，则进入本分支
else
_all: modules			// 若执行make M=dir或make ... SUBDIRS=$PWD命令，则进入本分支
endif

// 以x86体系为例，此处为include arch/x86/Makefile，其中包含all: bzImage，如下
include $(srctree)/arch/$(SRCARCH)/Makefile
```

2) 来自arch/x86/Makfile

```
# Default kernel to build
all: bzImage
```

3) 来自顶层Makefile

```
// 该目标被arch/x86/Makefile中的目标all: bzImage覆盖
all: vmlinux

ifdef CONFIG_MODULES

# By default, build modules as well
all: modules

else # CONFIG_MODULES
...
endif # CONFIG_MODULES
```

由上述规则可知：

* 执行make命令时，调用顶层Makefile中的目标_all，目标_all依赖于目标all，而目标all又依次依赖于目标bzImage、vmlinux和modules。即执行make命令时，将依次执行目标bzImage、vmlinux和modules，因而生成下列文件：

```
vmlinux
System.map
arch/x86/boot/bzImage
arch/i386/boot/bzImage		(link to ./arch/x86/boot/bzImage)
oneDir/twoDir/*.ko		(modules)
./arch/x86/lib/lib.a		(library)
./lib/lib.a			(library)
```

* 执行make vmlinux命令，编译顶层Makefile中的目标vmlinux，参见[3.4.2 编译bzImage/$(obj-y)](#3-4-2-bzimage-obj-y-)节。生成下列文件：

```
vmlinux
```

* 执行make modules命令，编译顶层Makefile中的目标modules，参见[3.4.3 编译modules/$(obj-m)](#3-4-3-modules-obj-m-)节。生成下列文件：

```
oneDir/twoDir/*.ko (modules)
```

* 执行下列命令之一来编译外部模块，参见[3.4.4 编译external modules](#3-4-4-external-modules)节：

```
# make -C <kernel_src_dir> M=<ext_module_dir> modules
# make -C <kernel_src_dir> SUBDIRS=$PWD modules
```

注：KBUILD_EXTMOD称为Kbuild扩展模式，若执行命令make M=dir，则变量KBUILD_EXTMOD被置为dir，继而执行下列规则：

```
# That's our default target when none is given on the command line
PHONY := _all
_all:

# If building an external module we do not care about the all: rule
# but instead _all depend on modules
PHONY += all
ifeq ($(KBUILD_EXTMOD),)	// 此时，$(KBUILD_EXTMOD)=dir
_all: all
else
_all: modules			// 进入此分支
endif
```

执行依赖于modules的代码，就相当于执行make modules。这个make方法也是用来提高驱动开发效率，如果只想编译某个具体的驱动，只要指定对应的子目录，就可以只编译这个驱动而不去编译其他的内核代码了。

执行make命令时，各目标的依赖关系:

![Targets_Tree](/assets/Targets_Tree.jpg)

其中的数字表示对应目标的生成顺序。

### 3.4.2 编译bzImage/$(obj-y)

在arch/x86/Makefile中，包含下列规则：

```
boot := arch/x86/boot

# Default kernel to build
all: bzImage

# KBUILD_IMAGE specify target image being built
KBUILD_IMAGE := $(boot)/bzImage

bzImage: vmlinux
ifeq ($(CONFIG_X86_DECODER_SELFTEST),y)
	$(Q)$(MAKE) $(build)=arch/x86/tools posttest
endif
	$(Q)$(MAKE) $(build)=$(boot) $(KBUILD_IMAGE)
	$(Q)mkdir -p $(objtree)/arch/$(UTS_MACHINE)/boot
	$(Q)ln -fsn ../../x86/boot/bzImage $(objtree)/arch/$(UTS_MACHINE)/boot/$@
```

在顶层Makefile中，包含下列规则：

```
vmlinux: $(vmlinux-lds) $(vmlinux-init) $(vmlinux-main) vmlinux.o $(kallsyms.o) FORCE
ifdef CONFIG_HEADERS_CHECK
	$(Q)$(MAKE) -f $(srctree)/Makefile headers_check
endif
ifdef CONFIG_SAMPLES
	$(Q)$(MAKE) $(build)=samples
endif
ifdef CONFIG_BUILD_DOCSRC
	$(Q)$(MAKE) $(build)=Documentation
endif
	$(call vmlinux-modpost)
	$(call if_changed_rule,vmlinux__)
	$(Q)rm -f .old_version

...
vmlinux-lds	:= arch/$(SRCARCH)/kernel/vmlinux.lds
vmlinux-init	:= $(head-y) $(init-y)
vmlinux-main	:= $(core-y) $(libs-y) $(drivers-y) $(net-y)
vmlinux-all	:= $(vmlinux-init) $(vmlinux-main)
...
vmlinux.o	: $(modpost-init) $(vmlinux-main) FORCE
modpost-init	:= $(filter-out init/built-in.o, $(vmlinux-init))
...
kallsyms.o	:= .tmp_kallsyms$(last_kallsyms).o	// last_kallsyms := 2 or 3

...
# The actual objects are generated when descending,
# make sure no implicit rule kicks in
$(sort $(vmlinux-init) $(vmlinux-main)) $(vmlinux-lds): $(vmlinux-dirs) ;

...
PHONY += $(vmlinux-dirs)
$(vmlinux-dirs): prepare scripts
	$(Q)$(MAKE) $(build)=$@
```

#### 3.4.2.1 $(vmlinux-dirs)

在顶层Makefile中，包含下列规则：

```
vmlinux-dirs	:=	$(patsubst %/,%,$(filter %/, $(init-y) $(init-m)	\
			$(core-y) $(core-m) $(drivers-y) $(drivers-m)		\
			$(net-y) $(net-m) $(libs-y) $(libs-m)))

# The actual objects are generated when descending,
# make sure no implicit rule kicks in
$(sort $(vmlinux-init) $(vmlinux-main)) $(vmlinux-lds): $(vmlinux-dirs) ;

PHONY += $(vmlinux-dirs)
$(vmlinux-dirs): prepare scripts
	$(Q)$(MAKE) $(build)=$@
```

由此可知，编译vmlinux时，vmlinux所依赖的目标$(vmlinux-init)、$(vmlinux-main)和$(vmlinux-lds)均依赖于$(vmlinux-dirs)。而$(vmlinux-dirs)又依赖于目标prepare和scripts。

##### 3.4.2.1.1 prepare

在顶层Makefile中，包含下列规则：

```
scripts_basic:
	$(Q)$(MAKE) $(build)=scripts/basic
	$(Q)rm -f .tmp_quiet_recordmcount

# prepare3 is used to check if we are building in a separate output directory,
# and if so do:
# 1) Check that make has not been executed in the kernel src $(srctree)
prepare3: include/config/kernel.release
ifneq ($(KBUILD_SRC),)	// 当不在linux源代码目录编译(参见outputmakefile节)时，执行下列命令
	@$(kecho) '  Using $(srctree) as source for kernel'
	$(Q)if [ -f $(srctree)/.config -o -d $(srctree)/include/config ]; then \
		echo "  $(srctree) is not clean, please run 'make mrproper'"; \
		echo "  in the '$(srctree)' directory."; \
		/bin/false; \
	fi;
endif

# prepare2 creates a makefile if using a separate output directory
prepare2: prepare3 outputmakefile asm-generic

prepare1: prepare2 include/linux/version.h include/generated/utsrelease.h \
                       include/config/auto.conf
	$(cmd_crmodverdir)

archprepare: prepare1 scripts_basic

prepare0: archprepare FORCE
	// 扩展为make -f scripts/Makefile.build obj=.
	$(Q)$(MAKE) $(build)=.

# All the preparing..
prepare: prepare0
```

###### 3.4.2.1.1.1 include/config/auto.conf

在Documentation/kbuild/kconfig.txt中，包含下列描述：

```
KCONFIG_AUTOCONFIG
--------------------------------------------------
This environment variable can be set to specify the path & name of the
"auto.conf" file.  Its default value is "include/config/auto.conf".
```

在顶层Makefile中，包含下列规则：

```
KCONFIG_CONFIG	?= .config

...
no-dot-config-targets := clean mrproper distclean \
                         cscope gtags TAGS tags help %docs check% coccicheck \
                         include/linux/version.h headers_% \
                         kernelversion %src-pkg

config-targets	:= 0
mixed-targets	:= 0
dot-config	:= 1

// 执行make命令，$(MAKECMDGOALS)为空，不进入本分支
ifneq ($(filter $(no-dot-config-targets), $(MAKECMDGOALS)),)
	ifeq ($(filter-out $(no-dot-config-targets), $(MAKECMDGOALS)),)
		dot-config := 0
	endif
endif

ifeq ($(KBUILD_EXTMOD),)
    ifneq ($(filter config %config,$(MAKECMDGOALS)),)
        config-targets := 1
        ifneq ($(filter-out config %config,$(MAKECMDGOALS)),)
            mixed-targets := 1
        endif
    endif
endif

...
// 由上述规则可知，dot-config取值为1
ifeq ($(dot-config),1)
# Read in config
/*
 * 2) 由下文1)处的规则生成include/config/auto.conf后，
 * make会重新读取Makefile文件，在此处读取该文件的内容
 */
-include include/config/auto.conf

// 执行make命令时，$(KBUILD_EXTMOD)为空，进入本分支
ifeq ($(KBUILD_EXTMOD),)

# Read in dependencies to all Kconfig* files, make sure to run
# oldconfig if changes are detected.
-include include/config/auto.conf.cmd

# To avoid any implicit rule to kick in, define an empty command
$(KCONFIG_CONFIG) include/config/auto.conf.cmd: ;

# If .config is newer than include/config/auto.conf, someone tinkered
# with it and forgot to run make oldconfig.
# if auto.conf.cmd is missing then we are probably in a cleaned tree so
# we execute the config step to be sure to catch updated Kconfig files
/*
 * 1) 执行下列规则，由.config生成include/config/*.conf文件，
 * 此后在上文2)处读取该文件的内容
 */
include/config/%.conf: $(KCONFIG_CONFIG) include/config/auto.conf.cmd
	$(Q)$(MAKE) -f $(srctree)/Makefile silentoldconfig

else # KBUILD_EXTMOD

# external modules needs include/generated/autoconf.h and include/config/auto.conf
# but do not care if they are up-to-date. Use auto.conf to trigger the test
PHONY += include/config/auto.conf

include/config/auto.conf:
	$(Q)test -e include/generated/autoconf.h -a -e $@ || (		\
	echo;								\
	echo "  ERROR: Kernel configuration is invalid.";		\
	echo "         include/generated/autoconf.h or $@ are missing.";\
	echo "         Run 'make oldconfig && make prepare' on kernel src to fix it.";	\
	echo;								\
	/bin/false)

endif # KBUILD_EXTMOD

else
# Dummy target needed, because used as prerequisite
include/config/auto.conf: ;
endif # $(dot-config)
```

由上述规则可知，若.config比include/config/auto.conf要新，则执行下列命令更新include/config/auto.conf文件，将最新的配置包含进来，参见[3.3.4.1 .config的格式](#3-3-4-1-config-)节和[3.3.4.2 .config如何被顶层Makefile调用](#3-3-4-2-config-makefile-)节：

```
$(Q)$(MAKE) -f $(srctree)/Makefile silentoldconfig
```

###### 3.4.2.1.1.2 include/config/kernel.release

在顶层Makefile中，包含下列规则：

```
# Store (new) KERNELRELASE string in include/config/kernel.release
include/config/kernel.release: include/config/auto.conf FORCE
	$(Q)rm -f $@
	$(Q)echo "$(KERNELVERSION)$$($(CONFIG_SHELL) $(srctree)/scripts/setlocalversion $(srctree))" > $@
```

生成的include/config/kernel.release包含下列内容：

```
3.2.0-chenwx
```

###### 3.4.2.1.1.3 outputmakefile

参见[3.3.1.2 outputmakefile](#3-3-1-2-outputmakefile)节。

###### 3.4.2.1.1.4 asm-generic

在顶层Makefile中，包含下列规则：

```
# Support for using generic headers in asm-generic
PHONY += asm-generic
asm-generic:
	$(Q)$(MAKE) -f $(srctree)/scripts/Makefile.asm-generic \
	            obj=arch/$(SRCARCH)/include/generated/asm
```

该命令被扩展为(以x86体系为例)：

```
make -f scripts/Makefile.asm-generic obj=arch/x86/include/generated/asm
```

在scripts/Makefile.asm-generic中，包含下列规则：

```
// 扩展为arch/x86/include/asm/Kbuild
kbuild-file := $(srctree)/arch/$(SRCARCH)/include/asm/Kbuild
-include $(kbuild-file)

include scripts/Kbuild.include

// 创建目录arch/x86/include/generated/asm
# Create output directory if not already present
_dummy := $(shell [ -d $(obj) ] || mkdir -p $(obj))

quiet_cmd_wrap = WRAP    $@
cmd_wrap = echo "\#include <asm-generic/$*.h>" >$@

/*
 * 在x86体系中，$(generic-y)为空，故本目标不产生任何文件
 * 在其他体系中，该目标用于生成指定的头文件，例如:
 * arch/blackfin/include/asm/Kbuild
 */
all: $(patsubst %, $(obj)/%, $(generic-y))
	@:

$(obj)/%.h:
	$(call cmd,wrap)	// 调用cmd_wrap命令
```

###### 3.4.2.1.1.5 include/linux/version.h

在顶层Makefile中，包含下列规则：

```
define filechk_version.h
	(echo \#define LINUX_VERSION_CODE $(shell				\
	expr $(VERSION) \* 65536 + 0$(PATCHLEVEL) \* 256 + 0$(SUBLEVEL));    	\
	echo '#define KERNEL_VERSION(a,b,c) (((a) << 16) + ((b) << 8) + (c))';)
endef

...
include/linux/version.h: $(srctree)/Makefile FORCE
	/*
	 * 参见scripts/Kbuild.include，调用filechk_version.h
	 * 生成include/linux/version.h
	 */
	$(call filechk,version.h)
```

生成的include/linux/version.h包含下列内容：

```
#define LINUX_VERSION_CODE 197120
#define KERNEL_VERSION(a,b,c) (((a) << 16) + ((b) << 8) + (c))
```

###### 3.4.2.1.1.6 include/generated/utsrelease.h

在顶层Makefile中，包含下列规则：

```
uts_len := 64
define filechk_utsrelease.h
	if [ `echo -n "$(KERNELRELEASE)" | wc -c ` -gt $(uts_len) ]; then \
	  echo '"$(KERNELRELEASE)" exceeds $(uts_len) characters' >&2;    \
	  exit 1;                                                         \
	fi;                                                               \
	(echo \#define UTS_RELEASE \"$(KERNELRELEASE)\";)
endef

// 依赖于kernel.release，参见include/config/kernel.release节
include/generated/utsrelease.h: include/config/kernel.release FORCE
	/*
	 * 参见scripts/Kbuild.include，调用filechk_utsrelease.h
	 * 生成include/linux/utsrelease.h
	 */
	$(call filechk,utsrelease.h)
```

生成的include/generated/utsrelease.h包含下列内容：

```
#define UTS_RELEASE "3.2.0-chenwx"
```

###### 3.4.2.1.1.7 prepare1

在顶层Makefile中，包含下列规则：

```
# When compiling out-of-tree modules, put MODVERDIR in the module
# tree rather than in the kernel tree. The kernel tree might
# even be read-only.
// 扩展为.tmp_versions
export MODVERDIR := $(if $(KBUILD_EXTMOD),$(firstword $(KBUILD_EXTMOD))/).tmp_versions

ifeq ($(KBUILD_EXTMOD),)

prepare1: prepare2 include/linux/version.h include/generated/utsrelease.h \
                   include/config/auto.conf
	// 执行命令cmd_crmodverdir，生成空目录.tmp_versions/
	$(cmd_crmodverdir)

...
else # KBUILD_EXTMOD
...
endif # KBUILD_EXTMOD

...
# Create temporary dir for module support files
# clean it up only when building all modules
// 扩展mkdir -p .tmp_versions ; rm -f .tmp_versions/*
cmd_crmodverdir = $(Q)mkdir -p $(MODVERDIR) \
                  $(if $(KBUILD_MODULES),; rm -f $(MODVERDIR)/*)
```

###### 3.4.2.1.1.8 scripts_basic

参见[3.3.1.1 scripts_basic](#3-3-1-1-scripts-basic)节。

###### 3.4.2.1.1.9 prepare0

在顶层Makefile中，包含下列规则：

```
prepare0: archprepare FORCE
	$(Q)$(MAKE) $(build)=.
```

其中，命令 $(Q)$(MAKE) $(build)=. 被扩展为：

```
make -f scripts/Makefile.build obj=.
```

该命令将编译scripts/Makefile.build中的默认规则__build：

```
PHONY := __build
__build:

# The filename Kbuild has precedence over Makefile
kbuild-dir := $(if $(filter /%,$(src)),$(src),$(srctree)/$(src))
kbuild-file := $(if $(wildcard $(kbuild-dir)/Kbuild),$(kbuild-dir)/Kbuild,$(kbuild-dir)/Makefile)
include $(kbuild-file)				// 将linux/Kbuild包含进来

__build: $(if $(KBUILD_BUILTIN),$(builtin-target) $(lib-target) $(extra-y))	\
	 $(if $(KBUILD_MODULES),$(obj-m) $(modorder-target))			\
	 $(subdir-ym) $(always)			// 变量$(always)由linux/Kbuild引入
	@:
```

由$(always)可知，该目标会生成下列文件：

```
include/generated/bounds.h
include/generated/asm-offsets.h
```

##### 3.4.2.1.2 scripts

在顶层Makefile中，包含下列规则：

```
ifeq ($(KBUILD_EXTMOD),)
# Additional helpers built in scripts/
# Carefully list dependencies so we do not try to build scripts twice
# in parallel
PHONY += scripts
scripts: scripts_basic include/config/auto.conf include/config/tristate.conf
	$(Q)$(MAKE) $(build)=$(@)

...
endif # KBUILD_EXTMOD
```

###### 3.4.2.1.2.1 scripts_basic

参见[3.3.1.1 scripts_basic](#3-3-1-1-scripts-basic)节。

###### 3.4.2.1.2.2 include/config/auto.conf

参见[3.4.2.1.1.1 include/config/auto.conf](#3-4-2-1-1-1-include-config-auto-conf)节。

###### 3.4.2.1.2.3 include/config/tristate.conf

参见Documentation/kbuild/kconfig.txt:

```
KCONFIG_TRISTATE
--------------------------------------------------
This environment variable can be set to specify the path & name of the
"tristate.conf" file.  Its default value is "include/config/tristate.conf".
```

在顶层Makefile中，包含下列规则：

```
include/config/%.conf: $(KCONFIG_CONFIG) include/config/auto.conf.cmd
	$(Q)$(MAKE) -f $(srctree)/Makefile silentoldconfig
```

由此可知，include/config/tristate.conf是由下列命令生成的：

```
$(Q)$(MAKE) -f $(srctree)/Makefile silentoldconfig
```

该命令与生成include/config/auto.conf所用命令是相同的，这两个文件也是同时生成的，参见[3.3.4.2 .config如何被顶层Makefile调用](#3-3-4-2-config-makefile-)节。

在scripts/Makefile.modbuiltin中，通过下列规则将include/config/tristate.conf引入，参见[3.4.3.3.1 make -f scripts/Makefile.modbuiltin obj=$*](#3-4-3-3-1-make-f-scripts-makefile-modbuiltin-obj-)节：

```
# tristate.conf sets tristate variables to uppercase 'Y' or 'M'
# That way, we get the list of built-in modules in obj-Y
-include include/config/tristate.conf
```

###### 3.4.2.1.2.4 scripts

在顶层Makefile中，包含下列规则：

```
ifeq ($(KBUILD_EXTMOD),)
# Additional helpers built in scripts/
# Carefully list dependencies so we do not try to build scripts twice
# in parallel
PHONY += scripts
scripts: scripts_basic include/config/auto.conf include/config/tristate.conf
	$(Q)$(MAKE) $(build)=$(@)

endif # KBUILD_EXTMOD
```

当[3.3.1.1 scripts_basic](#3-3-1-1-scripts-basic)节至[3.4.2.1.2.3 include/config/tristate.conf](#3-4-2-1-2-3-include-config-tristate-conf)节中的目标完成后，执行下列命令编译scripts目录及其子目录：

```
make -f scripts/Makefile.build obj=scripts
```

该编译过程与scripts_basic节类似，只不过变量$(always)是由scripts/Makefile引入的，如下：

```
hostprogs-$(CONFIG_KALLSYMS)		+= kallsyms
hostprogs-$(CONFIG_LOGO)		+= pnmtologo
hostprogs-$(CONFIG_VT)			+= conmakehash
hostprogs-$(CONFIG_IKCONFIG)		+= bin2c
hostprogs-$(BUILD_C_RECORDMCOUNT)	+= recordmcount

always	:= $(hostprogs-y) $(hostprogs-m)

subdir-y				+= mod
```

该目标生成下列可执行文件：

```
scripts/kallsyms
scripts/pnmtologo
scripts/conmakehash
scripts/bin2c
scripts/recordmcount
scripts/mod/modpost
scripts/mod/mk_elfconfig
```

##### 3.4.2.1.3 $(vmlinux-dirs)

在顶层Makefile中，包含下列规则：

```
init-y		:= init/
drivers-y	:= drivers/ sound/ firmware/
net-y		:= net/
libs-y		:= lib/
core-y		:= usr/

// 此处以x86体系为例，将arch/x86/Makefile引入
include $(srctree)/arch/$(SRCARCH)/Makefile

core-y		+= kernel/ mm/ fs/ ipc/ security/ crypto/ block/

vmlinux-dirs	:= $(patsubst %/,%,$(filter %/, $(init-y) $(init-m)	\
		   $(core-y) $(core-m) $(drivers-y) $(drivers-m)	\
		   $(net-y) $(net-m) $(libs-y) $(libs-m)))

PHONY += $(vmlinux-dirs)
$(vmlinux-dirs): prepare scripts
	$(Q)$(MAKE) $(build)=$@
```

在arch/x86/Makefile中，包含下列规则：

```
libs-y += arch/x86/lib/

# See arch/x86/Kbuild for content of core part of the kernel
core-y += arch/x86/

# drivers-y are linked after core-y
drivers-$(CONFIG_MATH_EMULATION)	+= arch/x86/math-emu/
drivers-$(CONFIG_PCI)			+= arch/x86/pci/

# must be linked after kernel/
drivers-$(CONFIG_OPROFILE)		+= arch/x86/oprofile/

# suspend and hibernation support
drivers-$(CONFIG_PM)			+= arch/x86/power/

drivers-$(CONFIG_FB)			+= arch/x86/video/
```

由此可知，vmlinux-dirs被扩展为：

```
vmlinux-dirs :=	\
	init \							// $(init-y)
	usr arch/x86 kernel mm fs ipc security crypto block \	// $(core-y)
	drivers sound firmware \				// $(drivers-y)
	arch/x86/math-emu \					// 与CONFIG_MATH_EMULATION有关
	arch/x86/pci \						// 与CONFIG_PCI有关
	arch/x86/oprofile \					// 与CONFIG_OPROFILE有关
	arch/x86/power \					// 与CONFIG_PM有关
	arch/x86/video \					// 与CONFIG_FB有关
	net \							// $(net-y)
	lib arch/x86/lib					// $(libs-y)
```

当$(vmlinux-dirs)所依赖的目标prepare和scripts完成后，将会执行下列命令编译$(vmlinux-dirs):

```
$(Q)$(MAKE) $(build)=$@
```

根据scripts/Makefile.build中对build的定义，该命令依次被扩展为：

```
make -f scripts/Makefile.build obj=init
make -f scripts/Makefile.build obj=usr
make -f scripts/Makefile.build obj=arch/x86		// 此处以x86体系为例，由arch/x86/Makefile中的core-y引入
make -f scripts/Makefile.build obj=kernel
make -f scripts/Makefile.build obj=mm
make -f scripts/Makefile.build obj=fs
make -f scripts/Makefile.build obj=ipc
make -f scripts/Makefile.build obj=security
make -f scripts/Makefile.build obj=crypto
make -f scripts/Makefile.build obj=block
make -f scripts/Makefile.build obj=drivers
make -f scripts/Makefile.build obj=sound
make -f scripts/Makefile.build obj=firmware
make -f scripts/Makefile.build obj=arch/x86/math-emu	// 与CONFIG_MATH_EMULATION有关
make -f scripts/Makefile.build obj=arch/x86/pci		// 与CONFIG_PCI有关
make -f scripts/Makefile.build obj=arch/x86/oprofile	// 与CONFIG_OPROFILE有关
make -f scripts/Makefile.build obj=arch/x86/power	// 与CONFIG_PM有关
make -f scripts/Makefile.build obj=arch/x86/video	// 与CONFIG_FB有关
make -f scripts/Makefile.build obj=net
make -f scripts/Makefile.build obj=lib
make -f scripts/Makefile.build obj=arch/x86/lib/	// 以x86体系为例，由arch/x86/Makefile中的libs-y引入
```

当执行这些命令时，如果这些目录下存在子目录，则make会递归调用其子目录下的Kbuild或Makefile(若不存在Kbuild文件)，详细的命令调用列表参见[Appendix A: make -f scripts/Makefile.build obj=列表](#appendix-a-make-f-scripts-makefile-build-obj-)节。

###### 3.4.2.1.3.1 make -f scripts/Makefile.build obj=XXX命令的执行过程

因为命令make -f scripts/Makefile.build obj=XXX中没有指定目标，故编译scripts/Makefile.build中的默认目标__build：

```
src := $(obj)
PHONY := __build
__build:

// kbuild-dir被扩展为obj指定的目录
kbuild-dir := $(if $(filter /%,$(src)),$(src),$(srctree)/$(src))
// kbuild-file被扩展为obj指定目录下的Kbuild或Makefile，其中Kbuild的优先级高于Makefile
kbuild-file := $(if $(wildcard $(kbuild-dir)/Kbuild),$(kbuild-dir)/Kbuild,$(kbuild-dir)/Makefile)
// 此处将obj指定目录下的Kbuild或Makefile包含进来
include $(kbuild-file)

__build: $(if $(KBUILD_BUILTIN),$(builtin-target) $(lib-target) $(extra-y))	\
	 $(if $(KBUILD_MODULES),$(obj-m) $(modorder-target))			\
	 $(subdir-ym) $(always)
	@:
```

根据顶层Makefile中对$(KBUILD_BUILTIN)和$(KBUILD_MODULES)的定义可知，上述规则被扩展为：

```
__build: $(builtin-target) $(lib-target) $(extra-y) $(obj-m) $(modorder-target) $(subdir-ym) $(always)
	@:
```

\_\_build所依赖的各目标参见下列几节：

###### 3.4.2.1.3.1.1 $(builtin-target)

在scripts/Makefile.build中，包含下列规则：

```
ifneq ($(strip $(obj-y) $(obj-m) $(obj-n) $(obj-) $(subdir-m) $(lib-target)),)
builtin-target := $(obj)/built-in.o
endif

#
# Rule to compile a set of .o files into one .o file
#
ifdef builtin-target
quiet_cmd_link_o_target = LD      $@
# If the list of objects to link is empty, just create an empty built-in.o
cmd_link_o_target = $(if $(strip $(obj-y)),				\
		    $(LD) $(ld_flags) -r -o $@ $(filter $(obj-y), $^)	\
		    $(cmd_secanalysis),					\
		    rm -f $@; $(AR) rcs$(KBUILD_ARFLAGS) $@)

$(builtin-target): $(obj-y) FORCE		// $(obj-y)参见$(obj-y)节
	$(call if_changed,link_o_target)	// 调用cmd_link_o_target，参见cmd_link_o_target节

targets += $(builtin-target)
endif # builtin-target
```

###### 3.4.2.1.3.1.1.1 $(obj-y)

$(obj)指定目录下的Makefile为$(obj-y)赋值。以fs/Makefile为例，其中包含如下规则：

```
/*
 * 此处使用":="为obj-y重新赋值，冲掉obj-y之前的取值。
 * 其他Makefile也使用类似方法为obj-y赋值
 */
obj-y :=	open.o read_write.o file_table.o super.o		\
		char_dev.o stat.o exec.o pipe.o namei.o fcntl.o		\
		ioctl.o readdir.o select.o fifo.o dcache.o inode.o	\
		attr.o bad_inode.o file.o filesystems.o namespace.o	\
		seq_file.o xattr.o libfs.o fs-writeback.o		\
		pnode.o drop_caches.o splice.o sync.o utimes.o		\
		stack.o fs_struct.o statfs.o

ifeq ($(CONFIG_BLOCK),y)
obj-y += buffer.o bio.o block_dev.o direct-io.o mpage.o ioprio.o
else
obj-y += no-block.o
endif

obj-$(CONFIG_BLK_DEV_INTEGRITY)	+= bio-integrity.o
obj-y				+= notify/
obj-$(CONFIG_EPOLL)		+= eventpoll.o
obj-$(CONFIG_ANON_INODES)	+= anon_inodes.o
obj-$(CONFIG_SIGNALFD)		+= signalfd.o
...
```

由此可知，$(obj-y)的取值与某些配置项的取值有关。$(obj)包含两类取值：

* $(obj)目录下需要编译的目标文件，如open.o。其编译过程参见[3.4.2.1.3.1.1.1.1 编译$(obj)目录下的目标文件](#3-4-2-1-3-1-1-1-1-obj-)节；
* $(obj)下的子目录，如notify/，其编译为notify/built-in.o，参见[3.4.2.1.3.1.1.1.2 编译$(obj)下的子目录](#3-4-2-1-3-1-1-1-2-obj-)节。

###### 3.4.2.1.3.1.1.1.1 编译$(obj)目录下的目标文件

在scripts/Makefile.build中，包含下列规则：

```
// $(CHECK), $(CHECKFLAGS)定义于顶层Makefile
# Linus' kernel sanity checking tool
ifneq ($(KBUILD_CHECKSRC),0)
  ifeq ($(KBUILD_CHECKSRC),2)
    quiet_cmd_force_checksrc	= CHECK   $<
          cmd_force_checksrc	= $(CHECK) $(CHECKFLAGS) $(c_flags) $< ;
  else
      quiet_cmd_checksrc	= CHECK   $<
            cmd_checksrc	= $(CHECK) $(CHECKFLAGS) $(c_flags) $< ;
  endif
endif

ifndef CONFIG_MODVERSIONS
// $(c_flags)定义于scripts/Makefile.lib。cmd_cc_o_c的扩展结果见下文
cmd_cc_o_c = $(CC) $(c_flags) -c -o $@ $<

else
# When module versioning is enabled the following steps are executed:
# o compile a .tmp_<file>.o from <file>.c
# o if .tmp_<file>.o doesn't contain a __ksymtab version, i.e. does
#   not export symbols, we just rename .tmp_<file>.o to <file>.o and
#   are done.
# o otherwise, we calculate symbol versions using the good old
#   genksyms on the preprocessed source and postprocess them in a way
#   that they are usable as a linker script
# o generate <file>.o from .tmp_<file>.o using the linker to
#   replace the unresolved symbols __crc_exported_symbol with
#   the actual value of the checksum generated by genksyms

cmd_cc_o_c = $(CC) $(c_flags) -c -o $(@D)/.tmp_$(@F) $<
cmd_modversions =									\
	/*
	 * $(OBJDUMP)定义于顶层Makefile，取值为objdump
	 * 该语句用于在目标文件中查找是否存在名为__ksymtab的段，
	 * 参见include/linux/export.h
	 */
	if $(OBJDUMP) -h $(@D)/.tmp_$(@F) | grep -q __ksymtab; then			\
		$(call cmd_gensymtypes,$(KBUILD_SYMTYPES),$(@:.o=.symtypes))		\
		    > $(@D)/.tmp_$(@F:.o=.ver);						\
											\
		$(LD) $(LDFLAGS) -r -o $@ $(@D)/.tmp_$(@F) 				\
			-T $(@D)/.tmp_$(@F:.o=.ver);					\
		rm -f $(@D)/.tmp_$(@F) $(@D)/.tmp_$(@F:.o=.ver);			\
	else										\
		mv -f $(@D)/.tmp_$(@F) $@;						\
	fi;
endif

ifdef CONFIG_FTRACE_MCOUNT_RECORD
ifdef BUILD_C_RECORDMCOUNT
sub_cmd_record_mcount =									\
	if [ $(@) != "scripts/mod/empty.o" ]; then					\
		$(objtree)/scripts/recordmcount $(RECORDMCOUNT_FLAGS) "$(@)";		\
	fi;
recordmcount_source := $(srctree)/scripts/recordmcount.c 				\
				 $(srctree)/scripts/recordmcount.h
else
sub_cmd_record_mcount = set -e ; perl $(srctree)/scripts/recordmcount.pl "$(ARCH)"	\
	"$(if $(CONFIG_CPU_BIG_ENDIAN),big,little)"					\
	"$(if $(CONFIG_64BIT),64,32)"							\
	"$(OBJDUMP)" "$(OBJCOPY)" "$(CC) $(KBUILD_CFLAGS)"				\
	"$(LD)" "$(NM)" "$(RM)" "$(MV)"							\
	"$(if $(part-of-module),1,0)" "$(@)";
recordmcount_source := $(srctree)/scripts/recordmcount.pl
endif
cmd_record_mcount = 									\
	if [ "$(findstring -pg,$(_c_flags))" = "-pg" ]; then				\
		$(sub_cmd_record_mcount)						\
	fi;
endif

// 将源文件*.c编译成目标文件*.o，并生成命令文件.*.o.cmd
define rule_cc_o_c
	/*
	 * echo-cmd定义于scripts/Kbuild.include，
	 * 此处用于显示命令cmd_checksrc，下同
	 */
	$(call echo-cmd,checksrc) $(cmd_checksrc)					\
	// 调用cmd_cc_o_c将源文件*.c编译成目标文件*.o
	$(call echo-cmd,cc_o_c) $(cmd_cc_o_c);						\
	// 若定义了CONFIG_MODVERSIONS，则命令cmd_modversions有效
	$(cmd_modversions)								\
	$(call echo-cmd,record_mcount)							\
	$(cmd_record_mcount)								\
	scripts/basic/fixdep $(depfile) $@ '$(call make-cmd,cc_o_c)' >			\
	                                            $(dot-target).tmp;			\
	// 删除依赖文件，如fs/.open.o.d，该文件是在命令cmd_cc_o_c中生成的
	rm -f $(depfile);								\
	// 生成命令文件，如fs/.open.o.cmd
	mv -f $(dot-target).tmp $(dot-target).cmd
endef

# Built-in and composite module parts
$(obj)/%.o: $(src)/%.c $(recordmcount_source) FORCE
	$(call cmd,force_checksrc)		// 调用cmd_force_checksrc
	$(call if_changed_rule,cc_o_c)		// 调用rule_cc_o_c

/*
 * 后面还有由源代码.S编译成目标文件.o的规则，与.c编译成.o的规则类似
 */
```

如果未定义CONFIG_MODVERSIONS，则命令cmd_cc_o_c扩展后的结果如下(以fs/open.o为例)：

```
gcc -Wp,-MD,fs/.open.o.d  -nostdinc -isystem /usr/lib/gcc/i686-linux-gnu/4.7/include -I/usr/src/linux-3.2/arch/x86/include -Iarch/x86/include/generated -Iinclude  -include /usr/src/linux-3.2/include/linux/kconfig.h -D__KERNEL__ -Wall -Wundef -Wstrict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -Werror-implicit-function-declaration -Wno-format-security -fno-delete-null-pointer-checks -O2 -m32 -msoft-float -mregparm=3 -freg-struct-return -mpreferred-stack-boundary=2 -march=i686 -Wa,-mtune=generic32 -ffreestanding -DCONFIG_AS_CFI=1 -DCONFIG_AS_CFI_SIGNAL_FRAME=1 -DCONFIG_AS_CFI_SECTIONS=1 -pipe -Wno-sign-compare -fno-asynchronous-unwind-tables -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -Wframe-larger-than=1024 -fno-stack-protector -Wno-unused-but-set-variable -fomit-frame-pointer -Wdeclaration-after-statement -Wno-pointer-sign -fno-strict-overflow -fconserve-stack -DCC_HAVE_ASM_GOTO    -D"KBUILD_STR(s)=#s" -D"KBUILD_BASENAME=KBUILD_STR(open)"  -D"KBUILD_MODNAME=KBUILD_STR(open)" -c -o fs/open.o fs/open.c
```

**假设内核中多个目录下存在同名头文件xxx.h，那么某.c文件包含的是哪个目录下的头文件xxx.h呢？**

命令cmd_cc_o_c中的变量c_flags定义于scripts/Makefile.lib:

```
C_flags = -Wp,-MD,$(depfile) $(NOSTDINC_FLAGS) $(LINUXINCLUDE)		\
		$(__c_flags) $(modkern_cflags)				\
		-D"KBUILD_STR(s)=\#s" $(basename_flags) $(modname_flags)
```

其中，变量LINUXINCLUDE定义于顶层Makefile中:

```
LINUXINCLUDE :=	-I$(srctree)/arch/$(hdr-arch)/include			\
			-Iarch/$(hdr-arch)/include/generated –Iinclude	\
			$(if $(KBUILD_SRC), -I$(srctree)/include)	\
			-include $(srctree)/include/linux/kconfig.h
```
由此可知，编译.c文件时查找头文件的目录顺序。以fs/open.o为例，LINUXINCLUDE被扩展为：

```
-I/usr/src/linux-3.2/arch/x86/include -Iarch/x86/include/generated -Iinclude -include /usr/src/linux-3.2/include/linux/kconfig.h
```

即查找头文件的目录顺序依次为：

```
arch/x86/include/			// 与体系架构有关
arch/x86/include/generated/		// 与体系架构有关
include/
include/linux/kconfig.h
```

###### 3.4.2.1.3.1.1.1.2 编译$(obj)下的子目录

在scripts/Makefile.build中，包含下列规则：

```
// 引入$(obj)指定目录下的Makefile，从中得到$(obj-y)的取值
# The filename Kbuild has precedence over Makefile
kbuild-dir  := $(if $(filter /%,$(src)),$(src),$(srctree)/$(src))
kbuild-file := $(if $(wildcard $(kbuild-dir)/Kbuild),$(kbuild-dir)/Kbuild,$(kbuild-dir)/Makefile)
include $(kbuild-file)

// 定义变量$(subdir-obj-y)和$(subdir-ym)，见下文
include scripts/Makefile.lib

# To build objects in subdirs, we need to descend into the directories
$(sort $(subdir-obj-y)): $(subdir-ym) ;

$(subdir-ym):
	/*
	 * 编译$(obj-y)和$(obj-m)中的子目录，
	 * 参见[make -f scripts/Makefile.build obj=XXX命令的执行过程](#)节;
	 * 以fs/notify为例，该命令扩展为： make -f scripts/Makefile.build obj=fs/notify
	 */
	$(Q)$(MAKE) $(build)=$@
```

**$(subdir-ym)**

$(obj-y)定义于scripts/Makefile.lib:

```
// 获取$(obj-y)和$(obj-m)中的子目录列表
__subdir-y	:= $(patsubst %/,%,$(filter %/, $(obj-y)))
subdir-y	+= $(__subdir-y)
__subdir-m	:= $(patsubst %/,%,$(filter %/, $(obj-m)))
subdir-m	+= $(__subdir-m)

/*
 * $(subdir-ym)为$(obj)的子目录名:
 * 以$(obj)=fs为例，则$(subdir-ym)取值为notify等
 */
# Subdirectories we need to descend into
subdir-ym	:= $(sort $(subdir-y) $(subdir-m))

// Add subdir path
subdir-ym	:= $(addprefix $(obj)/,$(subdir-ym))
```

**$(subdir-obj-y)**

$(subdir-obj-y)定义于scripts/Makefile.lib：

```
// 若$(obj-y)中包含子目录，则将子目录下的文件编译为built-in.o，如notify/built-in.o
obj-y		  := $(patsubst %/, %/built-in.o, $(obj-y))

# $(subdir-obj-y) is the list of objects in $(obj-y) which uses dir/ to
# tell kbuild to descend
subdir-obj-y := $(filter %/built-in.o, $(obj-y))

/*
 * $(subdir-obj-y)的取值，如 fs/notify/built-in.o fs/proc/built-in.o ...
 * 而这些目标文件的编译参见[$(builtin-target)节](#)
 */
subdir-obj-y := $(addprefix $(obj)/,$(subdir-obj-y))
```

如果$(obj-y)中包含子目录，则将子目录下的源文件编译成一个目标文件built-in.o。

###### 3.4.2.1.3.1.1.2 cmd_link_o_target

在scripts/Makefile.build中，包含下列规则：

```
#
# Rule to compile a set of .o files into one .o file
#
ifdef builtin-target

quiet_cmd_link_o_target = LD      $@
# If the list of objects to link is empty, just create an empty built-in.o
cmd_link_o_target = $(if $(strip $(obj-y)),				\
		    $(LD) $(ld_flags) -r -o $@ $(filter $(obj-y), $^)	\
		    $(cmd_secanalysis),					\
		    rm -f $@; $(AR) rcs$(KBUILD_ARFLAGS) $@)

endif # builtin-target
```

命令cmd_link_o_target将$(obj)指定目录及其子目录下的目标文件连接成built-in.o。以obj=fs为例，该命令扩展为：

```
ld -m elf_i386   -r -o fs/built-in.o fs/open.o fs/read_write.o fs/file_table.o fs/super.o fs/char_dev.o fs/stat.o fs/exec.o fs/pipe.o fs/namei.o fs/fcntl.o fs/ioctl.o fs/readdir.o fs/select.o fs/fifo.o fs/dcache.o fs/inode.o fs/attr.o fs/bad_inode.o fs/file.o fs/filesystems.o fs/namespace.o fs/seq_file.o fs/xattr.o fs/libfs.o fs/fs-writeback.o fs/pnode.o fs/drop_caches.o fs/splice.o fs/sync.o fs/utimes.o fs/stack.o fs/fs_struct.o fs/statfs.o fs/buffer.o fs/bio.o fs/block_dev.o fs/direct-io.o fs/mpage.o fs/ioprio.o fs/notify/built-in.o fs/eventpoll.o fs/anon_inodes.o fs/signalfd.o fs/timerfd.o fs/eventfd.o fs/aio.o fs/locks.o fs/binfmt_script.o fs/quota/built-in.o fs/proc/built-in.o fs/partitions/built-in.o fs/sysfs/built-in.o fs/devpts/built-in.o fs/ramfs/built-in.o fs/nls/built-in.o fs/exofs/built-in.o
```

###### 3.4.2.1.3.1.2 $(lib-target)

在scripts/Makefile.build中，包含下列规则：

```
// 将$(obj)指定目录下的库文件编译成$(obj)/lib.a
ifneq ($(strip $(lib-y) $(lib-m) $(lib-n) $(lib-)),)
lib-target := $(obj)/lib.a
endif

ifneq ($(strip $(obj-y) $(obj-m) $(obj-n) $(obj-) $(subdir-m) $(lib-target)),)
builtin-target := $(obj)/built-in.o
endif

#
# Rule to compile a set of .o files into one .a file
#
ifdef lib-target
quiet_cmd_link_l_target = AR      $@
cmd_link_l_target = rm -f $@; $(AR) rcs$(KBUILD_ARFLAGS) $@ $(lib-y)

/*
 * $(lib-y)定义于$(obj)指定目录下的Kbuild或Makefile，
 * 并经过scripts/Makefile.lib的进一步处理，参见[$(lib-y)](#)节
 */
$(lib-target): $(lib-y) FORCE
	// 调用cmd_link_l_target编译$(lib-target)
	$(call if_changed,link_l_target)

targets += $(lib-target)
endif
```

###### 3.4.2.1.3.1.2.1 $(lib-y)

$(lib-y)或$(lib-m)定义于$(obj)指定目录下的Kbuild或Makefile，以lib/Makefile为例，其中包含下列规则：

```
lib-y := ctype.o string.o vsprintf.o cmdline.o			\
	 rbtree.o radix-tree.o dump_stack.o timerqueue.o	\
	 idr.o int_sqrt.o extable.o prio_tree.o			\
	 sha1.o md5.o irq_regs.o reciprocal_div.o argv_split.o	\
	 proportions.o prio_heap.o ratelimit.o show_mem.o	\
	 is_single_threaded.o plist.o decompress.o

lib-$(CONFIG_MMU) += ioremap.o
lib-$(CONFIG_SMP) += cpumask.o

lib-y	+= kobject.o kref.o klist.o
...
```

在scripts/Makefile.lib中，对$(lib-y)或$(lib-m)进一步处理，如下所示：

```
# Libraries are always collected in one lib file.
# Filter out objects already built-in
lib-y := $(filter-out $(obj-y), $(sort $(lib-y) $(lib-m)))

/*
 * 此时，$(lib-y)中包含了要编译进库文件中的目标文件列表，如lib/ctype.o lib/string.o ...
 * 编译$(lib-y)时，符合规则"$(obj)/%.o: $(src)/%.c $(recordmcount_source) FORCE"
 */ 参见[编译$(obj)目录下的目标文件](#)节
lib-y := $(addprefix $(obj)/,$(lib-y))
```

###### 3.4.2.1.3.1.3 $(extra-y)

$(extra-y)的取值参见$(obj)指定目录下的Kbuild或Makefile。在scripts/Makefile.lib中，对其做进一步处理：

```
/*
 * 此时，$(extra-y)为目标文件列表
 * 编译$(lib-y)时，符合规则"$(obj)/%.o: $(src)/%.c $(recordmcount_source) FORCE"
 * 参见编译$(obj)目录下的目标文件节
 */
extra-y := $(addprefix $(obj)/,$(extra-y))
```

###### 3.4.2.1.3.1.4 $(obj-m)

$(obj-m)的取值参见$(obj)指定目录下的Kbuild或Makefile。在scripts/Makefile.lib中，对其做进一步处理：

```
# When an object is listed to be built compiled-in and modular,
# only build the compiled-in version
obj-m			:= $(filter-out $(obj-y),$(obj-m))

__subdir-m		:= $(patsubst %/,%,$(filter %/, $(obj-m)))
/*
 * $(subdir-m)中包含$(obj-m)中的子目录名，
 * 其将在$(builtin-target)中编译，参见[编译$(obj)下的子目录](#)节
 */
subdir-m		+= $(__subdir-m)
obj-m			:= $(filter-out %/, $(obj-m))

/*
 * 此时，$(obj-m)中仅包含$(obj)指定目录下的目标文件列表，不包含子目录
 * 编译$(obj-m)时，符合规则"$(obj)/%.o: $(src)/%.c $(recordmcount_source) FORCE"，
 * 参见[编译$(obj)目录下的目标文件](#)节
 */
obj-m			:= $(addprefix $(obj)/,$(obj-m))
```

###### 3.4.2.1.3.1.5 $(modorder-target)

在scripts/Makefile.build中，包含下列规则：

```
modorder-target := $(obj)/modules.order

#
# Rule to create modules.order file
#
# Create commands to either record .ko file or cat modules.order from
# a subdirectory
modorder-cmds =						\
	// $(modorder)定义于scripts/Makefile.lib，见下文
	$(foreach m, $(modorder),			\
		$(if $(filter %/modules.order, $m),	\
			cat $m;, echo kernel/$m;))

// $(subdir-ym)的编译参见[编译$(obj)下的子目录](#)节
$(modorder-target): $(subdir-ym) FORCE
	/*
	 * 调用modorder-cmds生成$(obj)/modules.order文件，
	 * 以fs/notify为例，该语句展开为：
 * (cat /dev/null;   cat fs/notify/dnotify/modules.order;
 *  cat fs/notify/inotify/modules.order;
 *  cat fs/notify/fanotify/modules.order;) > fs/notify/modules.order
 */
	$(Q)(cat /dev/null; $(modorder-cmds)) > $@
```

$(modorder)定义于scripts/Makefile.lib：

```
# Determine modorder.
# Unfortunately, we don't have information about ordering between -y
# and -m subdirs.  Just put -y's first.
modorder	:= $(patsubst %/,%/modules.order, $(filter %/, $(obj-y)) $(obj-m:.o=.ko))

...
modorder	:= $(addprefix $(obj)/,$(modorder))
```

###### 3.4.2.1.3.1.6 $(always)

$(always)的取值参见$(obj)指定目录下的Kbuild或Makefile。在scripts/Makefile.lib中，对其做进一步处理：

```
/*
 * 此时，$(always)中仅包含$(obj)指定目录下的目标文件列表
 * 编译$(always)时，符合规则"$(obj)/%.o: $(src)/%.c $(recordmcount_source) FORCE"，
 * 参见[编译$(obj)目录下的目标文件](#)节
 */
always		:= $(addprefix $(obj)/,$(always))
```

#### 3.4.2.2 $(vmlinux-lds)

##### 3.4.2.2.1 vmlinux.lds的作用

编译内核的过程分两步：一是"编译"，二是"链接"。vmlinux.lds就是告诉编译器如何链接编译好的各个.o文件，即如何组织内核的每个函数存放在内核镜像文件的位置，参见[Appendix F: vmlinux.lds.S](#appendix-f-vmlinux-lds-s)。

![Vmlinux_Image](/assets/Vmlinux_Image.png)

##### 3.4.2.2.2 vmlinux.lds如何生成

在顶层Makefile中，包含下列规则：

```
vmlinux-lds  := arch/$(SRCARCH)/kernel/vmlinux.lds

...
# The actual objects are generated when descending,
# make sure no implicit rule kicks in
$(sort $(vmlinux-init) $(vmlinux-main)) $(vmlinux-lds): $(vmlinux-dirs) ;
```

由$(vmlinux-dirs)节可知，当编译arch/x86目录时，将执行下列命令：

```
// 此处以x86体系为例，由arch/x86/Makefile中的core-y引入
make -f scripts/Makefile.build obj=arch/x86
```

其中，arch/x86/Kbuild包含下列规则：

```
obj-y += kernel/
```

即编译子目录arch/x86/kernel，并调用arch/x86/kernel/Makefile，其包含下列规则：

```
extra-y := head_$(BITS).o head$(BITS).o head.o init_task.o vmlinux.lds
```

根据$(extra-y)节的规则编译$(extra-y)，即根据scripts/Makefile.build中的下列规则来生成vmlinux.lds：

```
# Linker scripts preprocessor (.lds.S -> .lds)
# ---------------------------------------------------------------------------
quiet_cmd_cpp_lds_S = LDS     $@
       cmd_cpp_lds_S = $(CPP) $(cpp_flags) -P -C -U$(ARCH) \
	               -D__ASSEMBLY__ -DLINKER_SCRIPT -o $@ $<

$(obj)/%.lds: $(src)/%.lds.S FORCE		// vmlinux.lds是由vmlinux.lds.S预编译得来的
	$(call if_changed_dep,cpp_lds_S)	// 调用cmd_cpp_lds_S生成vmlinux.lds
```

由此可知，vmlinux.lds是由arch/x86/kernel/vmlinux.lds.S预处理而来，所用命令为cmd_cpp_lds_S。该命令被扩展为(参见编译后产生的命令文件arch/x86/kernel/.vmlinux.lds.cmd)：

```
gcc -E -Wp,-MD,arch/x86/kernel/.vmlinux.lds.d  -nostdinc -isystem /usr/lib/gcc/i686-linux-gnu/4.7/include -I/usr/src/linux-3.2/arch/x86/include -Iarch/x86/include/generated -Iinclude  -include /usr/src/linux-3.2/include/linux/kconfig.h -D__KERNEL__   -Ui386 -P -C -Ui386 -D__ASSEMBLY__ -DLINKER_SCRIPT -o arch/x86/kernel/vmlinux.lds arch/x86/kernel/vmlinux.lds.S
```

预处理后的vmlinux.lds是链接器GNU ld的link script文件，它是由Linker Command Language写成的，用于链接.o文件，参见[3.4.2.6.1.2 cmd_vmlinux__](#3-4-2-6-1-2-cmd-vmlinux-)节。关于link script语法，参见[Using ld](/docs/Using_ld_v2.17.pdf)。

#### 3.4.2.3 $(vmlinux-init)

在顶层Makefile中，包含下列规则：

```
vmlinux-init := $(head-y) $(init-y)
```

##### 3.4.2.3.1 $(head-y)

$(head-y)与体系结构有关，其定义于arch/$(ARCH)/Makefile。以x86为例，参见arch/x86/Makefile:

```
head-y := arch/x86/kernel/head_$(BITS).o	// $(BITS) = 32 or 64, 由head_32.S或head_64.S编译而来
head-y += arch/x86/kernel/head$(BITS).o		// $(BITS) = 32 or 64, 由head32.S或head64.S编译而来
head-y += arch/x86/kernel/head.o		// 由head.c编译而来
head-y += arch/x86/kernel/init_task.o		// 由init_task.c编译而来
```

根据$(vmlinux-dirs)节，在执行命令：

```
make -f scripts/Makefile.build obj=arch/x86/kernel
```

编译arch/x86/kernel/目录时，调用arch/x86/kernel/Makefile，其中包含：

```
extra-y := head_$(BITS).o head$(BITS).o head.o init_task.o vmlinux.lds
```

因此，$(head-y)中定义的目标文件是在编译$(extra-y)时编译的，参见[3.4.2.1.3.1.3 $(extra-y)](#3-4-2-1-3-1-3-extra-y-)节。

##### 3.4.2.3.2 $(init-y)

在顶层Makefile中，包含下列规则：

```
init-y	:= init/
init-y	:= $(patsubst %/, %/built-in.o, $(init-y))
```

根据$(vmlinux-dirs)节，在执行命令：

```
make -f scripts/Makefile.build obj=init
```

编译init/目录时，由于没有指定目标，故编译scripts/Makefile.build中的默认目标__build：

```
// 扩展为kbuild-dir := init
kbuild-dir := $(if $(filter /%,$(src)),$(src),$(srctree)/$(src))
// 扩展为kbuild-file := init/Makefile
kbuild-file := $(if $(wildcard $(kbuild-dir)/Kbuild),$(kbuild-dir)/Kbuild,$(kbuild-dir)/Makefile)
// 此处将init/Makefile包含进来，其中包括$(obj-y)变量
include $(kbuild-file)

...
__build: $(if $(KBUILD_BUILTIN),$(builtin-target) $(lib-target) $(extra-y))	\
	 $(if $(KBUILD_MODULES),$(obj-m) $(modorder-target))			\
	 $(subdir-ym) $(always)
	@:
```

\_\_build依赖于$(builtin-target)，在scripts/Makefile.build中，包含如下规则：

```
// 由init/Makefile可知，$(obj-y)不为空，故此条件成立
ifneq ($(strip $(obj-y) $(obj-m) $(obj-n) $(obj-) $(subdir-m) $(lib-target)),)
builtin-target := $(obj)/built-in.o		// init/built-in.o
endif

...
ifdef builtin-target
...
/*
 * 扩展为init/built-in.o: $(obj-y) FORCE，
 * 其中$(obj-y)定义于init/Makefile
 */
$(builtin-target): $(obj-y) FORCE
	/*
	 * if_changed定义于scripts/Kbuild.include，
	 * 若为真，则调用cmd_link_o_target
	 */
	$(call if_changed,link_o_target)
...
endif # builtin-target
```

由上述规则可知，先编译init/Makefile中$(obj-y)定义的目标文件，然后调用cmd_link_o_target函数链接$(obj-y)中的.o文件生成init/built-in.o。

```
$(obj-y)定义于init/Makefile中，且与.config中的配置有关：
obj-y						:= main.o version.o mounts.o
ifneq ($(CONFIG_BLK_DEV_INITRD),y)
obj-y						+= noinitramfs.o
else
obj-$(CONFIG_BLK_DEV_INITRD)			+= initramfs.o
endif
obj-$(CONFIG_GENERIC_CALIBRATE_DELAY)		+= calibrate.o
```

**$(obj-y)中main.o和version.o的编译**

main.o和version.o分别由main.c和version.c编译而来，其编译过程满足scripts/ Makefile.build中的规则"$(obj)/%.o: $(src)/%.c $(recordmcount_source) FORCE"，参见[3.4.2.1.3.1.1.1.1 编译$(obj)目录下的目标文件](#3-4-2-1-3-1-1-1-1-obj-)节。

**$(obj-y)中mounts.o的编译、链接**

mounts.o的编译有些复杂。首先，mounts.o不是由mounts.c编译而来，它由多个.c文件编译而来。由init/Makefile中的规则：

```
mounts-y				:= do_mounts.o
mounts-$(CONFIG_BLK_DEV_RAM)		+= do_mounts_rd.o
mounts-$(CONFIG_BLK_DEV_INITRD)		+= do_mounts_initrd.o
mounts-$(CONFIG_BLK_DEV_MD)		+= do_mounts_md.o
```

如果配置项取值如下：

```
CONFIG_BLK_DEV_RAM = y
CONFIG_BLK_DEV_INITRD = y
CONFIG_BLK_DEV_MD = y
```

则，mounts-y = do_mounts.o do_mounts_rd.o do_mounts_initrd.o do_mounts_md.o

由scripts/Makefile.lib中的如下规则：

```
// 扩展为multi-used-y := mounts.o
multi-used-y := $(sort $(foreach m,$(obj-y), $(if $(strip $($(m:.o=-objs)) $($(m:.o=-y))), $(m))))

...
/*
 * 扩展为multi-objs-y := $(mounts-y)，即：
 * multi-objs-y := do_mounts.o do_mounts_rd.o do_mounts_initrd.o do_mounts_md.o
 */
multi-objs-y := $(foreach m, $(multi-used-y), $($(m:.o=-objs)) $($(m:.o=-y)))
```

再根据scritps/Makefile.build中的如下规则：

```
$(multi-used-y) : %.o: $(multi-objs-y) FORCE
	$(call if_changed,link_multi-y)
...
# Built-in and composite module parts
$(obj)/%.o: $(src)/%.c $(recordmcount_source) FORCE
	$(call cmd,force_checksrc)
	$(call if_changed_rule,cc_o_c)
```

可知，首先执行rule_cc_o_c命令，分别将do_mounts.c、do_mounts_rd.c、do_mounts_initrd.c、do_mounts_md.c编译成do_mounts.o、do_mounts_rd.o、do_mounts_initrd.o、do_mounts_md.o；然后执行cmd_multi-y命令，将这些.o文件链接成mounts.o文件。

#### 3.4.2.4 $(vmlinux-main)

在顶层Makefile中，包含如下规则：

```
vmlinux-main := $(core-y) $(libs-y) $(drivers-y) $(net-y)
...
# The actual objects are generated when descending,
# make sure no implicit rule kicks in
$(sort $(vmlinux-init) $(vmlinux-main)) $(vmlinux-lds): $(vmlinux-dirs) ;
```

$(vmlinux-main)依赖于$(vmlinux-dirs)，其编译过程参见$(vmlinux-dirs)节，即通过下列命令编译：

```
// 编译$(core-y)
make -f scripts/Makefile.build obj=usr
make -f scripts/Makefile.build obj=arch/x86		// 此处以x86体系为例，由arch/x86/Makefile中的core-y引入
make -f scripts/Makefile.build obj=kernel
make -f scripts/Makefile.build obj=mm
make -f scripts/Makefile.build obj=fs
make -f scripts/Makefile.build obj=ipc
make -f scripts/Makefile.build obj=security
make -f scripts/Makefile.build obj=crypto
make -f scripts/Makefile.build obj=block
// 编译$(drivers-y)
make -f scripts/Makefile.build obj=drivers
make -f scripts/Makefile.build obj=sound
make -f scripts/Makefile.build obj=firmware
make -f scripts/Makefile.build obj=arch/x86/math-emu	// 与CONFIG_MATH_EMULATION有关
make -f scripts/Makefile.build obj=arch/x86/pci		// 与CONFIG_PCI有关
make -f scripts/Makefile.build obj=arch/x86/oprofile	// 与CONFIG_OPROFILE有关
make -f scripts/Makefile.build obj=arch/x86/power	// 与CONFIG_PM有关
make -f scripts/Makefile.build obj=arch/x86/video	// 与CONFIG_FB有关
// 编译$(net-y)
make -f scripts/Makefile.build obj=net
// 编译$(libs-y)
make -f scripts/Makefile.build obj=lib
make -f scripts/Makefile.build obj=arch/x86/lib/	// 以x86为例，由arch/x86/Makefile中的lib-y引入
```

#### 3.4.2.5 vmlinux.o

在顶层Makefile中，包含如下规则：

```
/*
 * 由$(vmlinux-init)节可知，modpost-init被扩展
 * 为$(head-y)，而$(head-y)的编译参见$(head-y)节
 */
modpost-init := $(filter-out init/built-in.o, $(vmlinux-init))

// $(vmlinux-main)的编译参见$(vmlinux-main)节
vmlinux.o: $(modpost-init) $(vmlinux-main) FORCE
	// 调用rule_vmlinux-modpost生成vmlinux.o
	$(call if_changed_rule,vmlinux-modpost)

...
// 参见cmd_vmlinux-modpost节
quiet_cmd_vmlinux-modpost = LD      $@
     cmd_vmlinux-modpost   = $(LD) $(LDFLAGS) -r -o $@			\
	 $(vmlinux-init) --start-group $(vmlinux-main) --end-group	\
	 $(filter-out $(vmlinux-init) $(vmlinux-main) FORCE ,$^)

// 参见rule_vmlinux-modpost节
define rule_vmlinux-modpost
	:
	// 调用cmd_vmlinux-modpost编译vmlinux.o
	+$(call cmd,vmlinux-modpost)
	// 根据vmlinux.o生成Module.symvers
	$(Q)$(MAKE) -f $(srctree)/scripts/Makefile.modpost $@
	// 生成命令文件.vmlinux.o.cmd
	$(Q)echo 'cmd_$@ := $(cmd_vmlinux-modpost)' > $(dot-target).cmd
endef
```

##### 3.4.2.5.1 cmd_vmlinux-modpost

调用下列命令链接vmlinux.o：

```
cmd_vmlinux-modpost = $(LD) $(LDFLAGS) -r -o $@					\
		      $(vmlinux-init) --start-group $(vmlinux-main) --end-group	\
		      $(filter-out $(vmlinux-init) $(vmlinux-main) FORCE ,$^)
```

其中，$^ is a list of all the prerequisites of the rule，此处取值为$(modpost-init) $(vmlinux-main)。

该命令被扩展为：

```
ld -m elf_i386 -r -o vmlinux.o arch/x86/kernel/head_32.o arch/x86/kernel/head32.o arch/x86/kernel/head.o arch/x86/kernel/init_task.o  init/built-in.o --start-group  usr/built-in.o  arch/x86/built-in.o  kernel/built-in.o  mm/built-in.o  fs/built-in.o  ipc/built-in.o  security/built-in.o  crypto/built-in.o  block/built-in.o  lib/lib.a  arch/x86/lib/lib.a  lib/built-in.o  arch/x86/lib/built-in.o  drivers/built-in.o  sound/built-in.o  firmware/built-in.o  arch/x86/math-emu/built-in.o  arch/x86/power/built-in.o  net/built-in.o –end-group
```

##### 3.4.2.5.2 rule_vmlinux-modpost

调用cmd_vmlinux-modpost链接vmlinux.o完成后，将执行下列命令：

```
$(Q)$(MAKE) -f $(srctree)/scripts/Makefile.modpost $@
```

该命令被扩展为：

```
make -f scripts/Makefile.modpost vmlinux.o
```

即执行scripts/Makefile.modpost中的vmlinux.o目标：

```
modpost	= scripts/mod/modpost						\
	  $(if $(CONFIG_MODVERSIONS),-m)				\
	  $(if $(CONFIG_MODULE_SRCVERSION_ALL),-a,)			\
	  // kernelsymfile := $(objtree)/Module.symvers
	  $(if $(KBUILD_EXTMOD),-i,-o) $(kernelsymfile)			\
	  $(if $(KBUILD_EXTMOD),-I $(modulesymfile))			\
	  $(if $(KBUILD_EXTRA_SYMBOLS), $(patsubst %, -e %,$(KBUILD_EXTRA_SYMBOLS)))	\
	  $(if $(KBUILD_EXTMOD),-o $(modulesymfile))			\
	  $(if $(CONFIG_DEBUG_SECTION_MISMATCH),,-S)			\
	  $(if $(KBUILD_EXTMOD)$(KBUILD_MODPOST_WARN),-w)		\
	  $(if $(cross_build),-c)

...
quiet_cmd_kernel-mod = MODPOST $@
	cmd_kernel-mod = $(modpost) $@

vmlinux.o: FORCE
	// 调用cmd_kernel-mod
	$(call cmd,kernel-mod)
```

调用cmd_kernel-mod执行下列命令：

```
scripts/mod/modpost -m -o /usr/src/linux-3.2/Module.symvers  vmlinux.o
```

输出Module.symvers文件，其中包含基本内核导出的、供模块使用的符号以及CRC校验和。

上述命令执行完成后，继续执行下列命令：

```
$(Q)echo 'cmd_$@ := $(cmd_vmlinux-modpost)' > $(dot-target).cmd
```

根据scripts/Kbuild.include中对dot-target的定义：

```
# Name of target with a '.' as filename prefix. foo/bar.o => foo/.bar.o
dot-target = $(dir $@).$(notdir $@)
```

可知，该命令被扩展为：

```
echo 'cmd_vmlinux.o := ld -m elf_i386 -r -o vmlinux.o arch/x86/kernel/head_32.o arch/x86/kernel/head32.o arch/x86/kernel/head.o arch/x86/kernel/init_task.o  init/built-in.o --start-group  usr/built-in.o  arch/x86/built-in.o  kernel/built-in.o  mm/built-in.o  fs/built-in.o  ipc/built-in.o  security/built-in.o  crypto/built-in.o  block/built-in.o  lib/lib.a  arch/x86/lib/lib.a  lib/built-in.o  arch/x86/lib/built-in.o  drivers/built-in.o  sound/built-in.o  firmware/built-in.o  arch/x86/math-emu/built-in.o  arch/x86/power/built-in.o  net/built-in.o --end-group ' > ./.vmlinux.o.cmd
```

其输出为./.vmlinux.o.cmd，该文件包含编译vmlinux.o时所用的命令。

#### 3.4.2.6 $(kallsyms.o)

在顶层Makefile中，包含如下规则：

```
// kallsyms.o的取值与.config中的配置项CONFIG_KALLSYMS有关
ifdef CONFIG_KALLSYMS
    last_kallsyms := 2
    ifdef KALLSYMS_EXTRA_PASS
        ifneq ($(KALLSYMS_EXTRA_PASS),0)
            last_kallsyms := 3
        endif
    endif

// kallsymb.o := .tmp_kallsyms2.o或.tmp_kallsyms3.o
kallsyms.o := .tmp_kallsyms$(last_kallsyms).o

...
endif

.tmp_kallsyms1.o .tmp_kallsyms2.o .tmp_kallsyms3.o: %.o: %.S scripts FORCE
	// 调用cmd_as_o_S生成.tmp_kallsym%.o
	$(call if_changed_dep,as_o_S)

// KALLSYMS = scripts/kallsyms
.tmp_kallsyms%.S: .tmp_vmlinux% $(KALLSYMS)
	// 调用cmd_kallsyms生成.tmp_kallsym%.S
	$(call cmd,kallsyms)

# .tmp_vmlinux1 must be complete except kallsyms, so update vmlinux version
.tmp_vmlinux1: $(vmlinux-lds) $(vmlinux-all) FORCE
	// 调用rule_ksym_ld链接生成.tmp_vmlinux1
	$(call if_changed_rule,ksym_ld)

.tmp_vmlinux2: $(vmlinux-lds) $(vmlinux-all) .tmp_kallsyms1.o FORCE
	// 调用cmd_vmlinux__链接生成.tmp_vmlinux2
	$(call if_changed,vmlinux__)

.tmp_vmlinux3: $(vmlinux-lds) $(vmlinux-all) .tmp_kallsyms2.o FORCE
	// 调用cmd_vmlinux__链接生成.tmp_vmlinux3
	$(call if_changed,vmlinux__)
```

编译链接$(kallsyms.o)的流程：

![Compiling_kallsyms.o](/assets/Compiling_kallsyms.o.jpg)

##### 3.4.2.6.1 rule_ksym_ld

在顶层Makefile中，包含如下规则：

```
# Rule to link vmlinux - also used during CONFIG_KALLSYMS
# May be overridden by arch/$(ARCH)/Makefile
quiet_cmd_vmlinux__ ?= LD      $@
      cmd_vmlinux__ ?= $(LD) $(LDFLAGS) $(LDFLAGS_vmlinux) -o $@		\
      -T $(vmlinux-lds) $(vmlinux-init)						\
      --start-group $(vmlinux-main) --end-group					\
      $(filter-out $(vmlinux-lds) $(vmlinux-init) $(vmlinux-main) vmlinux.o FORCE ,$^)

# Generate new vmlinux version
quiet_cmd_vmlinux_version = GEN     .version
      cmd_vmlinux_version = set -e;						\
	  if [ ! -r .version ]; then						\
	    rm -f .version;							\
	    echo 1 >.version;							\
	  else									\
	    mv .version .old_version;						\
	    expr 0$$(cat .old_version) + 1 >.version;				\
	  fi;									\
	  $(MAKE) $(build)=init

...
define rule_ksym_ld
	:
	// 调用cmd_vmlinux_version
	+$(call cmd,vmlinux_version)
	// 调用cmd_vmlinux__
	$(call cmd,vmlinux__)
	// 生成命令文件..tmp_vmlinux1.cmd
	$(Q)echo 'cmd_$@ := $(cmd_vmlinux__)' > $(@D)/.$(@F).cmd
endef
```

###### 3.4.2.6.1.1 cmd_vmlinux_version

该命令的输出.version文件。

###### 3.4.2.6.1.2 cmd_vmlinux__

链接.tmp_vmlinux1时，该命令被扩展为：

```
cmd_.tmp_vmlinux1 := ld -m elf_i386 --build-id -o .tmp_vmlinux1 -T arch/x86/kernel/vmlinux.lds arch/x86/kernel/head_32.o arch/x86/kernel/head32.o arch/x86/kernel/head.o arch/x86/kernel/init_task.o  init/built-in.o --start-group  usr/built-in.o  arch/x86/built-in.o  kernel/built-in.o  mm/built-in.o  fs/built-in.o  ipc/built-in.o  security/built-in.o  crypto/built-in.o  block/built-in.o  lib/lib.a  arch/x86/lib/lib.a  lib/built-in.o  arch/x86/lib/built-in.o  drivers/built-in.o  sound/built-in.o  firmware/built-in.o  arch/x86/math-emu/built-in.o  arch/x86/power/built-in.o  net/built-in.o --end-group
```

链接.tmp_vmlinux2时，该命令被扩展为：

```
cmd_.tmp_vmlinux2 := ld -m elf_i386 --build-id -o .tmp_vmlinux2 -T arch/x86/kernel/vmlinux.lds arch/x86/kernel/head_32.o arch/x86/kernel/head32.o arch/x86/kernel/head.o arch/x86/kernel/init_task.o  init/built-in.o --start-group  usr/built-in.o  arch/x86/built-in.o  kernel/built-in.o  mm/built-in.o  fs/built-in.o  ipc/built-in.o  security/built-in.o  crypto/built-in.o  block/built-in.o  lib/lib.a  arch/x86/lib/lib.a  lib/built-in.o  arch/x86/lib/built-in.o  drivers/built-in.o  sound/built-in.o  firmware/built-in.o  arch/x86/math-emu/built-in.o  arch/x86/power/built-in.o  net/built-in.o --end-group .tmp_kallsyms1.o
```

链接.tmp_vmlinux3时，该命令被扩展为：

```
cmd_.tmp_vmlinux3 := ld -m elf_i386 --build-id -o .tmp_vmlinux3 -T arch/x86/kernel/vmlinux.lds arch/x86/kernel/head_32.o arch/x86/kernel/head32.o arch/x86/kernel/head.o arch/x86/kernel/init_task.o  init/built-in.o --start-group  usr/built-in.o  arch/x86/built-in.o  kernel/built-in.o  mm/built-in.o  fs/built-in.o  ipc/built-in.o  security/built-in.o  crypto/built-in.o  block/built-in.o  lib/lib.a  arch/x86/lib/lib.a  lib/built-in.o  arch/x86/lib/built-in.o  drivers/built-in.o  sound/built-in.o  firmware/built-in.o  arch/x86/math-emu/built-in.o  arch/x86/power/built-in.o  net/built-in.o --end-group .tmp_kallsyms2.o
```

该命令的输出为.tmp_vmlinux1, .tmp_vmlinux2, 或.tmp_vmlinux3。

链接vmlinux时(参见rule_vmlinux__节)，该命令被扩展为：

```
cmd_vmlinux := ld -m elf_i386 --build-id -o vmlinux -T arch/x86/kernel/vmlinux.lds arch/x86/kernel/head_32.o arch/x86/kernel/head32.o arch/x86/kernel/head.o arch/x86/kernel/init_task.o  init/built-in.o --start-group  usr/built-in.o  arch/x86/built-in.o  kernel/built-in.o  mm/built-in.o  fs/built-in.o  ipc/built-in.o  security/built-in.o  crypto/built-in.o  block/built-in.o  lib/lib.a  arch/x86/lib/lib.a  lib/built-in.o  arch/x86/lib/built-in.o  drivers/built-in.o  sound/built-in.o  firmware/built-in.o  arch/x86/math-emu/built-in.o  arch/x86/power/built-in.o  net/built-in.o --end-group .tmp_kallsyms2.o
```

注：本命令中最后一个参数为.tmp_kallsyms2.o，也可能为.tmp_kallsyms3.o，具体取值与配置有关，参见[3.4.2.6 $(kallsyms.o)](#3-4-2-6-kallsyms-o-)节。

##### 3.4.2.6.2 cmd_kallsyms

在顶层Makefile中，包含如下规则：

```
# Generate .S file with all kernel symbols
quiet_cmd_kallsyms = KSYM    $@
      cmd_kallsyms = $(NM) -n $< | $(KALLSYMS) \
                     $(if $(CONFIG_KALLSYMS_ALL),--all-symbols) > $@
```

在编译.tmp_kallsyms1.S时，该命令被扩展为：

```
nm -n .tmp_vmlinux1 | scripts/kallsyms --all-symbols > .tmp_kallsyms1.S
```

在编译.tmp_kallsyms2.S时，该命令被扩展为：

```
nm -n .tmp_vmlinux2 | scripts/kallsyms --all-symbols > .tmp_kallsyms2.S
```

在编译.tmp_kallsyms3.S时，该命令被扩展为：

```
nm -n .tmp_vmlinux3 | scripts/kallsyms --all-symbols > .tmp_kallsyms3.S
```

##### 3.4.2.6.3 cmd_as_o_S

在顶层Makefile中，包含如下规则：

```
quiet_cmd_as_o_S = AS      $@
cmd_as_o_S       = $(CC) $(a_flags) -c -o $@ $<
```

在编译.tmp_kallsyms1.o时，该命令被扩展为：

```
cmd_.tmp_kallsyms1.o := gcc -Wp,-MD,./..tmp_kallsyms1.o.d -D__ASSEMBLY__ -m32 -DCONFIG_AS_CFI=1 -DCONFIG_AS_CFI_SIGNAL_FRAME=1 -DCONFIG_AS_CFI_SECTIONS=1   -gdwarf-2    -nostdinc -isystem /usr/lib/gcc/i686-linux-gnu/4.7/include -I/usr/src/linux-3.2/arch/x86/include -Iarch/x86/include/generated -Iinclude  -include /usr/src/linux-3.2/include/linux/kconfig.h -D__KERNEL__    -c -o .tmp_kallsyms1.o .tmp_kallsyms1.S
```

在编译.tmp_kallsyms2.o时，该命令被扩展为：

```
cmd_.tmp_kallsyms2.o := gcc -Wp,-MD,./..tmp_kallsyms1.o.d -D__ASSEMBLY__ -m32 -DCONFIG_AS_CFI=1 -DCONFIG_AS_CFI_SIGNAL_FRAME=1 -DCONFIG_AS_CFI_SECTIONS=1   -gdwarf-2    -nostdinc -isystem /usr/lib/gcc/i686-linux-gnu/4.7/include -I/usr/src/linux-3.2/arch/x86/include -Iarch/x86/include/generated -Iinclude  -include /usr/src/linux-3.2/include/linux/kconfig.h -D__KERNEL__    -c -o .tmp_kallsyms2.o .tmp_kallsyms2.S
```

在编译.tmp_kallsyms3.o时，该命令被扩展为：

```
cmd_.tmp_kallsyms3.o := gcc -Wp,-MD,./..tmp_kallsyms1.o.d -D__ASSEMBLY__ -m32 -DCONFIG_AS_CFI=1 -DCONFIG_AS_CFI_SIGNAL_FRAME=1 -DCONFIG_AS_CFI_SECTIONS=1   -gdwarf-2    -nostdinc -isystem /usr/lib/gcc/i686-linux-gnu/4.7/include -I/usr/src/linux-3.2/arch/x86/include -Iarch/x86/include/generated -Iinclude  -include /usr/src/linux-3.2/include/linux/kconfig.h -D__KERNEL__    -c -o .tmp_kallsyms3.o .tmp_kallsyms3.S
```

#### 3.4.2.7 vmlinux

在顶层Makefile中，包含如下规则：

```
vmlinux: $(vmlinux-lds) $(vmlinux-init) $(vmlinux-main) vmlinux.o $(kallsyms.o) FORCE

/* 参见make -f Makefile headers_check节 */
ifdef CONFIG_HEADERS_CHECK
	$(Q)$(MAKE) -f $(srctree)/Makefile headers_check
endif

/*
 * 参见make -f scripts/Makefile.build obj=samples节，
 * 编译samples目录，内核编程示例
 */
ifdef CONFIG_SAMPLES
	$(Q)$(MAKE) $(build)=samples
endif

/*
 * 参见make -f scripts/Makefile.build obj=Documentation节，
 * 编译Documentation目录
 */
ifdef CONFIG_BUILD_DOCSRC
	$(Q)$(MAKE) $(build)=Documentation
endif
	// 未定义函数vmlinux-modpost，忽略
	$(call vmlinux-modpost)
	/*
	 * 调用rule_vmlinux__链接vmlinux，并
	 * 生成System.map，参见rule_vmlinux__节
	 */
	$(call if_changed_rule,vmlinux__)
	$(Q)rm -f .old_version
```

##### 3.4.2.7.1 make -f Makefile headers_check

在顶层Makefile中，包含如下规则：

```
# Where to locate arch specific headers
hdr-arch	:= $(SRCARCH)		// 此处以x86体系为例

hdr-inst	:= -rR -f $(srctree)/scripts/Makefile.headersinst obj

# If we do an all arch process set dst to asm-$(hdr-arch)
hdr-dst	= $(if $(KBUILD_HEADERS), dst=include/asm-$(hdr-arch), dst=include/asm)

PHONY += __headers
// 参见include/linux/version.h，scripts_basic和asm-generic节
__headers: include/linux/version.h scripts_basic asm-generic FORCE
	// 编译scripts/unifdef
	$(Q)$(MAKE) $(build)=scripts build_unifdef

PHONY += headers_install
headers_install: __headers
	$(if $(wildcard $(srctree)/arch/$(hdr-arch)/include/asm/Kbuild),, \
	$(error Headers not exportable for the $(SRCARCH) architecture))
	// 扩展为make -rR -f $(srctree)/scripts/Makefile.headersinst obj=include
	$(Q)$(MAKE) $(hdr-inst)=include
	// 扩展为make -rR -f $(srctree)/scripts/Makefile.headersinst obj=arch/x86/include/asm $(hdr-dst)
	$(Q)$(MAKE) $(hdr-inst)=arch/$(hdr-arch)/include/asm $(hdr-dst)

PHONY += headers_check
headers_check: headers_install
	// 扩展为make -rR -f $(srctree)/scripts/Makefile.headersinst obj=include  HDRCHECK=1
	$(Q)$(MAKE) $(hdr-inst)=include HDRCHECK=1
	// 扩展为make -rR -f $(srctree)/scripts/Makefile.headersinst obj=arch/x86/include/asm $(hdr-dst) HDRCHECK=1
	$(Q)$(MAKE) $(hdr-inst)=arch/$(hdr-arch)/include/asm $(hdr-dst) HDRCHECK=1
```

##### 3.4.2.7.2 make -f scripts/Makefile.build obj=samples

参见[3.4.2.1.3.1 make -f scripts/Makefile.build obj=XXX命令的执行过程](#3-4-2-1-3-1-make-f-scripts-makefile-build-obj-xxx-)节。samples目录包含内核编程的示例。

##### 3.4.2.7.3 make -f scripts/Makefile.build obj=Documentation

参见[3.4.2.1.3.1 make -f scripts/Makefile.build obj=XXX命令的执行过程](#3-4-2-1-3-1-make-f-scripts-makefile-build-obj-xxx-)节。

##### 3.4.2.7.4 rule_vmlinux__

在顶层Makefile中，包含如下规则：

```
# Generate System.map
quiet_cmd_sysmap = SYSMAP
      cmd_sysmap = $(CONFIG_SHELL) $(srctree)/scripts/mksysmap

# Link of vmlinux
# If CONFIG_KALLSYMS is set .version is already updated
# Generate System.map and verify that the content is consistent
# Use + in front of the vmlinux_version rule to silent warning with make -j2
# First command is ':' to allow us to use + in front of the rule
define rule_vmlinux__
	:
	// 调用cmd_vmlinux_version，参见cmd_vmlinux_version节
	$(if $(CONFIG_KALLSYMS),,+$(call cmd,vmlinux_version))
	// 调用cmd_vmlinux__链接vmlinux，参见cmd_vmlinux__节
	$(call cmd,vmlinux__)
	// 生成命令文件./.vmlinux.cmd
	$(Q)echo 'cmd_$@ := $(cmd_vmlinux__)' > $(@D)/.$(@F).cmd
	$(Q)$(if $($(quiet)cmd_sysmap),						\
	  echo '  $($(quiet)cmd_sysmap)  System.map' &&)			\
	// 用于提取vmlinux中的符号，并保存于System.map
	$(cmd_sysmap) $@ System.map;						\
	if [ $$? -ne 0 ]; then							\
		rm -f $@;							\
		/bin/false;							\
	fi;
	$(verify_kallsyms)
endef

...
define verify_kallsyms
	$(Q)$(if $($(quiet)cmd_sysmap),						\
	  echo '  $($(quiet)cmd_sysmap)  .tmp_System.map' &&)			\
	  /*
	   * 提取.tmp_vmlinux2或.tmp_vmlinux3中的符号
	   * (参见$(kallsyms.o)节和cmd_vmlinux__节)，
	   * 并保存于.tmp_System.map
	   */
	  $(cmd_sysmap) .tmp_vmlinux$(last_kallsyms) .tmp_System.map
	/*
	 * 比较System.map和.tmp_System.map，
	 * 应该相同；若不同，则打印错误信息
	 */
	$(Q)cmp -s System.map .tmp_System.map ||				\
		(echo Inconsistent kallsyms data;				\
		 echo This is a bug - please report about it;			\
		 echo Try "make KALLSYMS_EXTRA_PASS=1" as a workaround;		\
		 rm .tmp_kallsyms* ; /bin/false )
endef
```

本命令的输出为vmlinux和System.map，其中：

* vmlinux用来生成bzImage，参见[3.4.2.8.5.1 $(obj)/piggy.o](#3-4-2-8-5-1-obj-piggy-o)节；
* System.map被安装到/boot/System.map-3.2.0(通过执行命令make install)，参见[编译内核](#)节。

查看vmlinux的文件属性：

```
chenwx@chenwx /usr/src/linux $ file vmlinux
vmlinux: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, BuildID[sha1]=0xb14c81a12cca7144a29770565166fe7f8b1748d7, not stripped
```

#### 3.4.2.8 bzImage

在arch/x86/Makefile中，包含如下规则：

```
boot := arch/x86/boot

# Default kernel to build
all: bzImage

# KBUILD_IMAGE specify target image being built
KBUILD_IMAGE := $(boot)/bzImage

bzImage: vmlinux
ifeq ($(CONFIG_X86_DECODER_SELFTEST),y)
	// 扩展为make -f scripts/Makefile.build obj=arch/x86/tools posttest
	$(Q)$(MAKE) $(build)=arch/x86/tools posttest
endif
	// 扩展为make -f scripts/Makefile.build obj=arch/x86/boot arch/x86/boot/bzImage
	$(Q)$(MAKE) $(build)=$(boot) $(KBUILD_IMAGE)
	// 扩展为mkdir -p /usr/src/linux-3.2/arch/i386/boot
	$(Q)mkdir -p $(objtree)/arch/$(UTS_MACHINE)/boot
	/*
	 * 扩展为ln -fsn ../../x86/boot/bzImage /usr/src/linux-3.2/arch/i386/boot/bzImage
	 * 即arch/i386/boot/目录中的bzImage为符号链接，指向arch/x86/boot/bzImage
	 */
	$(Q)ln -fsn ../../x86/boot/bzImage $(objtree)/arch/$(UTS_MACHINE)/boot/$@
```

编译bzImage的命令为：

```
$(Q)$(MAKE) $(build)=$(boot) $(KBUILD_IMAGE)
```

该命令被扩展为：

```
make -f scripts/Makefile.build obj=arch/x86/boot arch/x86/boot/bzImage
```

该命令调用arch/x86/boot/Makefile，并编译目标arch/x86/boot/bzImage。在arch/x86/boot/Makefile中，包含如下规则：

```
/*
 * (1) 参见3.4.2.8.1 $(src)/setup.ld节，
 *     3.4.2.8.2 $(SETUP_OBJS)节，3.4.2.8.3 $(obj)/setup.elf节
 */
LDFLAGS_setup.elf	:= -T
$(obj)/setup.elf: $(src)/setup.ld $(SETUP_OBJS) FORCE
	$(call if_changed,ld)

// (2) 参见3.4.2.8.4 $(obj)/setup.bin节
OBJCOPYFLAGS_setup.bin	:= -O binary
$(obj)/setup.bin: $(obj)/setup.elf FORCE
	$(call if_changed,objcopy)

// (3) 参见3.4.2.8.5 $(obj)/compressed/vmlinux节
$(obj)/compressed/vmlinux: FORCE
	$(Q)$(MAKE) $(build)=$(obj)/compressed $@

// (4) 参见3.4.2.8.6 $(obj)/vmlinux.bin节
OBJCOPYFLAGS_vmlinux.bin := -O binary -R .note -R .comment -S
$(obj)/vmlinux.bin: $(obj)/compressed/vmlinux FORCE
	$(call if_changed,objcopy)

// (5) 参见3.4.2.8.8 arch/x86/boot/bzImage节
$(obj)/bzImage: $(obj)/setup.bin $(obj)/vmlinux.bin $(obj)/tools/build FORCE
	$(call if_changed,image)
	@echo 'Kernel: $@ is ready' ' (#'`cat .version`')'
```

各目标之间的依赖关系，参见[Appendix I: Targets Tree](#appendix-i-targets-tree)。

bzImage的生成过程：

![bzImage](/assets/bzImage.jpg)

![bzImage_1](/assets/bzImage_1.png)

##### 3.4.2.8.1 $(src)/setup.ld

arch/x86/boot/setup.ld是GNU ld的Linker script文件，与$(vmlinux.lds)类似，参见[3.4.2.2 $(vmlinux-lds)](#3-4-2-2-vmlinux-lds-)节。

##### 3.4.2.8.2 $(SETUP_OBJS)

该变量定义于arch/x86/boot/Makefile:

```
setup-y		+= a20.o bioscall.o cmdline.o copy.o cpu.o cpucheck.o
setup-y		+= early_serial_console.o edd.o header.o main.o mca.o memory.o
setup-y		+= pm.o pmjump.o printf.o regs.o string.o tty.o video.o
setup-y		+= video-mode.o version.o
setup-$(CONFIG_X86_APM_BOOT) += apm.o

# The link order of the video-*.o modules can matter.  In particular,
# video-vga.o *must* be listed first, followed by video-vesa.o.
# Hardware-specific drivers should follow in the order they should be
# probed, and video-bios.o should typically be last.
setup-y		+= video-vga.o
setup-y		+= video-vesa.o
setup-y		+= video-bios.o

...
SETUP_OBJS = $(addprefix $(obj)/,$(setup-y))
```

##### 3.4.2.8.3 $(obj)/setup.elf

在arch/x86/boot/Makefile中，包含如下规则：

```
LDFLAGS_setup.elf	:= -T
$(obj)/setup.elf: $(src)/setup.ld $(SETUP_OBJS) FORCE
	$(call if_changed,ld)
```

调用命令cmd_ld将$(SETUP_OBJS)中的文件连接生成arch/x86/boot/setup.elf。命令cmd_ld定义于scripts/Makefile.lib，被扩展为：

```
ld -m elf_i386   -T arch/x86/boot/setup.ld arch/x86/boot/a20.o arch/x86/boot/bioscall.o arch/x86/boot/cmdline.o arch/x86/boot/copy.o arch/x86/boot/cpu.o arch/x86/boot/cpucheck.o arch/x86/boot/early_serial_console.o arch/x86/boot/edd.o arch/x86/boot/header.o arch/x86/boot/main.o arch/x86/boot/mca.o arch/x86/boot/memory.o arch/x86/boot/pm.o arch/x86/boot/pmjump.o arch/x86/boot/printf.o arch/x86/boot/regs.o arch/x86/boot/string.o arch/x86/boot/tty.o arch/x86/boot/video.o arch/x86/boot/video-mode.o arch/x86/boot/version.o arch/x86/boot/apm.o arch/x86/boot/video-vga.o arch/x86/boot/video-vesa.o arch/x86/boot/video-bios.o -o arch/x86/boot/setup.elf
```

##### 3.4.2.8.4 $(obj)/setup.bin

在arch/x86/boot/Makefile中，包含如下规则：

```
OBJCOPYFLAGS_setup.bin	:= -O binary
$(obj)/setup.bin: $(obj)/setup.elf FORCE
	$(call if_changed,objcopy)
```

调用命令cmd_objcopy由arch/x86/boot/setup.elf生成arch/x86/boot/setup.bin。命令cmd_objcopy定义于scripts/Makefile.lib，被扩展为：

```
objcopy  -O binary arch/x86/boot/setup.elf arch/x86/boot/setup.bin
```

That's write the output file **setup.bin** from input file **setup.elf** using the object format binary.

##### 3.4.2.8.5 $(obj)/compressed/vmlinux

在arch/x86/boot/Makefile中，包含如下规则：

```
$(obj)/compressed/vmlinux: FORCE
	$(Q)$(MAKE) $(build)=$(obj)/compressed $@
```

执行下列命令编译arch/x86/boot/compressed目录：

```
$(Q)$(MAKE) $(build)=$(obj)/compressed $@
```

该命令被扩展为：

```
make -f scripts/Makefile.build obj=arch/x86/boot/compressed arch/x86/boot/compressed/vmlinux
```

该命令调用arch/x86/boot/compressed/Makefile，其中包含如下规则：

```
$(obj)/vmlinux: $(obj)/vmlinux.lds $(obj)/head_$(BITS).o $(obj)/misc.o $(obj)/string.o $(obj)/cmdline.o $(obj)/early_serial_console.o $(obj)/piggy.o FORCE
	$(call if_changed,ld)
	@:
```

调用命令cmd_ld生成arch/x86/boot/compressed/vmlinux。命令cmd_ld定义于scripts/Makefile.lib，被扩展为：

```
ld -m elf_i386   -T arch/x86/boot/compressed/vmlinux.lds arch/x86/boot/compressed/head_32.o arch/x86/boot/compressed/misc.o arch/x86/boot/compressed/string.o arch/x86/boot/compressed/cmdline.o arch/x86/boot/compressed/early_serial_console.o arch/x86/boot/compressed/piggy.o -o arch/x86/boot/compressed/vmlinux
```

输出为arch/x86/boot/compressed/vmlinux，该压缩内核文件大小约为1.6M，要比/usr/src/linux-3.2/vmlinux (参见rule_vmlinux__节，其大小约46M) 小很多。

查看arch/x86/boot/compressed/vmlinux的文件属性：

```
chenwx@chenwx /usr/src/linux $ file arch/x86/boot/compressed/vmlinux
arch/x86/boot/compressed/vmlinux: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, not stripped
```

arch/x86/boot/compressed/vmlinux所依赖的各目标文件分别由如下文件生成：

```
arch/x86/boot/compressed/vmlinux.lds			<= arch/x86/boot/compressed/vmlinux.lds.S
arch/x86/boot/compressed/head_32.o			<= arch/x86/boot/compressed/head_32.S
arch/x86/boot/compressed/head_64.o			<= arch/x86/boot/compressed/head_64.S
arch/x86/boot/compressed/misc.o				<= arch/x86/boot/compressed/misc.c, misc.h
arch/x86/boot/compressed/string.o			<= arch/x86/boot/compressed/string.c
arch/x86/boot/compressed/cmdline.o			<= arch/x86/boot/compressed/cmdline.c
arch/x86/boot/compressed/early_serial_console.o		<= arch/x86/boot/compressed/early_serial_console.c
arch/x86/boot/compressed/piggy.o			<= arch/x86/boot/compressed/piggy.S，参见$(obj)/piggy.o节
```

###### 3.4.2.8.5.1 $(obj)/piggy.o

在arch/x86/boot/compressed/Makefile中，包含如下规则：

```
// (1) 参见3.4.2.8.5.1.1 $(obj)/vmlinux.bin节
OBJCOPYFLAGS_vmlinux.bin :=  -R .comment -S
$(obj)/vmlinux.bin: vmlinux FORCE
	$(call if_changed,objcopy)

// (2) 参见3.4.2.8.5.1.2 $(obj)/vmlinux.bin.gz节
vmlinux.bin.all-y := $(obj)/vmlinux.bin
$(obj)/vmlinux.bin.gz: $(vmlinux.bin.all-y) FORCE
	$(call if_changed,gzip)

/*
 * (3) 参见3.4.2.8.5.1.3 $(obj)/mkpiggy节，
 *     3.4.2.8.5.1.4 $(obj)/piggy.S节，
 *     3.4.2.8.5.1.5 $(obj)/piggy.o节
 */
suffix-$(CONFIG_KERNEL_GZIP)	:= gz

quiet_cmd_mkpiggy = MKPIGGY $@
      cmd_mkpiggy = $(obj)/mkpiggy $< > $@ || ( rm -f $@ ; false )

$(obj)/piggy.S: $(obj)/vmlinux.bin.$(suffix-y) $(obj)/mkpiggy FORCE
	$(call if_changed,mkpiggy)
```

arch/x86/boot/compressed/piggy.o是由arch/x86/boot/compressed/piggy.S编译而来的，各目标之间的依赖关系参见[Appendix I: Targets Tree](#appendix-i-targets-tree)。

###### 3.4.2.8.5.1.1 $(obj)/vmlinux.bin

在arch/x86/boot/compressed/Makefile中，包含如下规则：

```
OBJCOPYFLAGS_vmlinux.bin :=  -R .comment -S
$(obj)/vmlinux.bin: vmlinux FORCE
	$(call if_changed,objcopy)
```

调用命令cmd_objcopy生成arch/x86/boot/compressed/vmlinux.bin。命令cmd_objcopy定义于scripts/Makefile.lib，被扩展为：

```
objcopy  -R .comment -S vmlinux arch/x86/boot/compressed/vmlinux.bin
```

其中，参数的含义如下：

```
-R sectionname: Remove any section named sectionname from the output file.
-S/--strip-all: Do not copy relocation and symbol information from the source file.
```

vmlinux为linux-3.2/vmlinux，参见[3.4.2.7 vmlinux](#3-4-2-7-vmlinux)节。

###### 3.4.2.8.5.1.2 $(obj)/vmlinux.bin.gz

在arch/x86/boot/compressed/Makefile中，包含如下规则：

```
// 扩展为arch/x86/boot/compressed/vmlinux.bin
vmlinux.bin.all-y := $(obj)/vmlinux.bin

$(obj)/vmlinux.bin.gz: $(vmlinux.bin.all-y) FORCE
	$(call if_changed,gzip)
```

调用命令cmd_gzip将arch/x86/boot/compressed/vmlinux.bin压缩成arch/x86/boot/compressed/vmlinux.bin.gz。命令cmd_gzip定义于scripts/Makefile.lib，被扩展为：

```
(cat arch/x86/boot/compressed/vmlinux.bin | gzip -n -f -9 > arch/x86/boot/compressed/vmlinux.bin.gz) || (rm -f arch/x86/boot/compressed/vmlinux.bin.gz ; false)
```

###### 3.4.2.8.5.1.3 $(obj)/mkpiggy

```
arch/x86/boot/compressed/mkpiggy		<= arch/x86/boot/compressed/mkpiggy.c
```

where, the executable mkpiggy is used when creating arch/x86/boot/compressed/piggy.S, see [3.4.2.8.5.1.4 $(obj)/piggy.S](#3-4-2-8-5-1-4-obj-piggy-s).

###### 3.4.2.8.5.1.4 $(obj)/piggy.S

在arch/x86/boot/compressed/Makefile中，包含如下规则：

```
suffix-$(CONFIG_KERNEL_GZIP)	:= gz

...
quiet_cmd_mkpiggy = MKPIGGY $@
      cmd_mkpiggy = $(obj)/mkpiggy $< > $@ || ( rm -f $@ ; false )

$(obj)/piggy.S: $(obj)/vmlinux.bin.$(suffix-y) $(obj)/mkpiggy FORCE
	$(call if_changed,mkpiggy)
```

调用命令cmd_mkpiggy生成arch/x86/boot/compressed/piggy.S，该命令被扩展为：

```
arch/x86/boot/compressed/mkpiggy arch/x86/boot/compressed/vmlinux.bin.gz > arch/x86/boot/compressed/piggy.S || ( rm -f arch/x86/boot/compressed/piggy.S ; false )
```

由arch/x86/boot/compressed/mkpiggy.c可知，上述命令将arch/x86/boot/compressed/vmlinux.bin.gz添加到 arch/x86/boot/compressed/piggy.S中：

```
/*
 * 此代码被放到.rodata..compressed段中，对该段的连接参见:
 * 3.4.2.8.5.2 arch/x86/boot/compressed/vmlinux.lds
 * 下列变量用于解压二进制文件vmlinux.bin.gz:
 * z_input_len, z_extract_offset, input_data
 * 参见4.3.4.1.3 arch/x86/boot/compressed/head_32.S节
 */
.section .rodata..compressed,"a",@progbits
.globl z_input_len
z_input_len = <ilen>
.globl z_output_len
z_output_len = <olen>
.globl z_extract_offset
z_extract_offset = <offs>
/* z_extract_offset_negative allows simplification of head_32.S */
.globl z_extract_offset_negative
z_extract_offset_negative = <offs>
.globl z_run_size
z_run_size = <run_size>

.globl input_data, input_data_end
input_data:
// 将二进制文件vmlinux.bin.gz包含到这里
.incbin arch/x86/boot/compressed/vmlinux.bin.gz
input_data_end:

NOTE: How to embed a binary in your executable?
Method #1: Covert the binary to the "hex" text, and #include
(binary_file.hex)
0xeb, 0xfe, 0x90, 0x90, ...

(C file)
unsigned char binary[] = {
    #include "binary_file.hex"
};

Method #2: Use ".incbin" mnemonic in the assembler
.section .rodata
.global input_data, input_data_end
input_data:
    .incbin "binary_file.bin"
input_data_end:
```

Obviously, mkpiggy uses the Method #2 to generate arch/x86/boot/compressed/piggy.S

###### 3.4.2.8.5.1.5 $(obj)/piggy.o

在scripts/Makefile.build中，包含如下规则：

```
quiet_cmd_as_o_S = AS $(quiet_modtag)  $@
cmd_as_o_S       = $(CC) $(a_flags) -c -o $@ $<

$(obj)/%.o: $(src)/%.S FORCE
	$(call if_changed_dep,as_o_S)
```

调用命令cmd_as_o_S将arch/x86/boot/compressed/piggy.S编译成arch/x86/boot/compressed/piggy.o。命令cmd_as_o_S被扩展为：

```
gcc -Wp,-MD,arch/x86/boot/compressed/.piggy.o.d  -nostdinc -isystem /usr/lib/gcc/i686-linux-gnu/4.7/include -I/usr/src/linux-3.2/arch/x86/include -Iarch/x86/include/generated -Iinclude  -include /usr/src/linux-3.2/include/linux/kconfig.h -D__KERNEL__ -m32 -D__KERNEL__  -O2 -fno-strict-aliasing -fPIC -DDISABLE_BRANCH_PROFILING -march=i386 -ffreestanding -fno-stack-protector -D__ASSEMBLY__         -c -o arch/x86/boot/compressed/piggy.o arch/x86/boot/compressed/piggy.S
```

That's, make an object (arch/x86/boot/compressed/piggy.o) that contains the compressed image (arch/x86/boot/compressed/vmlinux.bin.gz ), see 3.4.2.8.5.1.4 $(obj)/piggy.S.

###### 3.4.2.8.5.2 arch/x86/boot/compressed/vmlinux.lds

该文件包含如下内容:

```
#include <asm-generic/vmlinux.lds.h>

OUTPUT_FORMAT(CONFIG_OUTPUT_FORMAT, CONFIG_OUTPUT_FORMAT, CONFIG_OUTPUT_FORMAT)

#undef i386

#include <asm/cache.h>
#include <asm/page_types.h>

#ifdef CONFIG_X86_64
OUTPUT_ARCH(i386:x86-64)
ENTRY(startup_64)
#else
OUTPUT_ARCH(i386)
ENTRY(startup_32)
#endif

SECTIONS
{
	/* Be careful parts of head_64.S assume startup_32 is at
	 * address 0.
	 */
	. = 0;
	.head.text : {
		_head = . ;
		// 包含arch/x86/boot/compressed/head_32.S中的代码
		HEAD_TEXT
		_ehead = . ;
	}
	.rodata..compressed : {
		/*
		 * 包含arch/x86/boot/compressed/piggy.S中的代码，
		 * 参见3.4.2.8.5.1.4 $(obj)/piggy.S节
		 */
		*(.rodata..compressed)
	}
	.text :	{
		_text = .; 	/* Text */
		*(.text)
		*(.text.*)
		_etext = . ;
	}
	.rodata : {
		_rodata = . ;
		*(.rodata)	 /* read-only data */
		*(.rodata.*)
		_erodata = . ;
	}
	.got : {
		_got = .;
		KEEP(*(.got.plt))
		KEEP(*(.got))
		_egot = .;
	}
	.data :	{
		_data = . ;
		*(.data)
		*(.data.*)
		_edata = . ;
	}
	. = ALIGN(L1_CACHE_BYTES);
	.bss : {
		_bss = . ;
		*(.bss)
		*(.bss.*)
		*(COMMON)
		. = ALIGN(8);	/* For convenience during zeroing */
		_ebss = .;
	}
#ifdef CONFIG_X86_64
       . = ALIGN(PAGE_SIZE);
       .pgtable : {
		_pgtable = . ;
		*(.pgtable)
		_epgtable = . ;
	}
#endif
	_end = .;
}
```

##### 3.4.2.8.6 $(obj)/vmlinux.bin

在arch/x86/boot/Makefile中，包含如下规则：

```
OBJCOPYFLAGS_vmlinux.bin := -O binary -R .note -R .comment -S
$(obj)/vmlinux.bin: $(obj)/compressed/vmlinux FORCE
	$(call if_changed,objcopy)
```

调用命令cmd_objcopy由arch/x86/boot/compressed/vmlinux 生成arch/x86/boot/vmlinux.bin。命令cmd_objcopy定义于scripts/Makefile.lib，被扩展为：

```
objcopy  -O binary -R .note -R .comment -S arch/x86/boot/compressed/vmlinux arch/x86/boot/vmlinux.bin
```

其中，参数的含义如下：

```
-R sectionname: Remove any section named sectionname from the output file.
-S/--strip-all: Do not copy relocation and symbol information from the source file.
```

##### 3.4.2.8.7 $(obj)/tools/build

```
arch/x86/boot/tools/build  <=  arch/x86/boot/tools/build.c
```

arch/x86/boot/tools/build的用法参见[3.4.2.8.8 arch/x86/boot/bzImage](#3-4-2-8-8-arch-x86-boot-bzimage)节。

##### 3.4.2.8.8 arch/x86/boot/bzImage

在arch/x86/boot/Makefile中，包含如下规则：

```
$(obj)/bzImage: $(obj)/setup.bin $(obj)/vmlinux.bin $(obj)/tools/build FORCE
	/*
	 * 调用cmd_image，由arch/x86/boot/setup.bin和
	 * arch/x86/boot/vmlinux.bin生成arch/x86/boot/bzImage
	 */
	$(call if_changed,image)
	// 打印 Kernel: arch/x86/boot/bzImage is ready  (#1)
	@echo 'Kernel: $@ is ready' ' (#'`cat .version`')'

...
quiet_cmd_image = BUILD   $@
cmd_image = $(obj)/tools/build $(obj)/setup.bin $(obj)/vmlinux.bin > $@
```

调用命令cmd_image由arch/x86/boot/setup.bin和arch/x86/boot/vmlinux.bin生成arch/x86/boot/bzImage，该命令被扩展为：

```
arch/x86/boot/tools/build arch/x86/boot/setup.bin arch/x86/boot/vmlinux.bin > arch/x86/boot/bzImage
```

查看arch/x86/boot/bzImage的文件属性：

```
chenwx@chenwx /usr/src/linux $ file arch/x86/boot/bzImage
arch/x86/boot/bzImage: Linux kernel x86 boot executable bzImage, version 3.2.0 (chenwx@chenwx) #1 SMP Tue Feb 19 23:35:53 EET 2013, RO-rootFS, swap_dev 0x2, Normal VGA
```

### 3.4.3 编译modules/$(obj-m)

运行make modules命令(或者make命令)，执行顶层Makefile中的modules目标：

```
KBUILD_AFLAGS_MODULE  := -DMODULE
KBUILD_CFLAGS_MODULE  := -DMODULE
KBUILD_LDFLAGS_MODULE := -T $(srctree)/scripts/module-common.lds

...
export KBUILD_AFLAGS_MODULE KBUILD_CFLAGS_MODULE KBUILD_LDFLAGS_MODULE

...
/*
 * 由此可知，必须满足CONFIG_MODULES=y才能编译modules；
 * 而CONFIG_MODULES根据init/Kconfig中的如下配置项生成:
 * 		menuconfig MODULES
 *  			bool "Enable loadable module support"
 */
ifdef CONFIG_MODULES

all: modules

PHONY += modules
modules: $(vmlinux-dirs) $(if $(KBUILD_BUILTIN),vmlinux) modules.builtin
	$(Q)$(AWK) '!x[$$0]++' $(vmlinux-dirs:%=$(objtree)/%/modules.order) > $(objtree)/modules.order
	@$(kecho) '  Building modules, stage 2.';
	$(Q)$(MAKE) -f $(srctree)/scripts/Makefile.modpost
	$(Q)$(MAKE) -f $(srctree)/scripts/Makefile.fwinst obj=firmware __fw_modbuild

modules.builtin: $(vmlinux-dirs:%=%/modules.builtin)
	$(Q)$(AWK) '!x[$$0]++' $^ > $(objtree)/modules.builtin

%/modules.builtin: include/config/auto.conf
	$(Q)$(MAKE) $(modbuiltin)=$*

...
else # CONFIG_MODULES

# Modules not configured
# ---------------------------------------------------------------------------

modules modules_install: FORCE
	@echo
	@echo "The present kernel configuration has modules disabled."
	@echo "Type 'make config' and enable loadable module support."
	@echo "Then build a kernel with module support enabled."
	@echo
	@exit 1

endif # CONFIG_MODULES
```

#### 3.4.3.1 $(vmlinux-dirs)

参见[3.4.2.1 $(vmlinux-dirs)](#3-4-2-1-vmlinux-dirs-)节。

#### 3.4.3.2 vmlinux

在顶层Makefile中，包含如下规则：

```
KBUILD_BUILTIN := 1

#	If we have only "make modules", don't compile built-in objects.
#	When we're building modules with modversions, we need to consider
#	the built-in objects during the descend as well, in order to
#	make sure the checksums are up to date before we record them.

// 执行make modules时，满足条件，进入本分支；仅执行make时，不进入本分支
ifeq ($(MAKECMDGOALS),modules)
  // 参见linux-3.2/Documentation/kbuild/modules.txt第6节
  KBUILD_BUILTIN := $(if $(CONFIG_MODVERSIONS),1)
endif
```

若配置了CONFIG_MODVERSIONS，则modules依赖于vmlinux，其执行过程参见[3.4.2.7 vmlinux](#3-4-2-7-vmlinux)节；否则，modules不依赖于vmlinux。

#### 3.4.3.3 modules.builtin

modules.builtin的含义：

> This file lists all modules that are built into the kernel. This is used by modprobe to not fail when trying to load something builtin.

在顶层Makefile中，包含如下规则：

```
ifdef CONFIG_MODULES

...
modules.builtin: $(vmlinux-dirs:%=%/modules.builtin)
	$(Q)$(AWK) '!x[$$0]++' $^ > $(objtree)/modules.builtin

%/modules.builtin: include/config/auto.conf
	$(Q)$(MAKE) $(modbuiltin)=$*

...
else # CONFIG_MODULES
...
endif # CONFIG_MODULES
```

由$(vmlinux-dirs)节可知，$(vmlinux-dirs:%=%/modules.builtin)被扩展为：

```
init/modules.builtin usr/modules.builtin arch/x86/modules.builtin kernel/modules.builtin mm/modules.builtin fs/modules.builtin ipc/modules.builtin security/modules.builtin crypto/modules.builtin block/modules.builtin drivers/modules.builtin sound/modules.builtin firmware/modules.builtin net/modules.builtin lib/modules.builtin arch/x86/lib/modules.builtin
```

该列表匹配规则：

```
// include/config/auto.conf参见.config如何被顶层Makefile调用节和include/config/auto.conf节
%/modules.builtin: include/config/auto.conf
	$(Q)$(MAKE) $(modbuiltin)=$*
```

因而执行下列命令：

```
$(Q)$(MAKE) $(modbuiltin)=$*
```

其中，$(modbuiltin)定义于scripts/Kbuild.include：

```
modbuiltin := -f $(if $(KBUILD_SRC),$(srctree)/)scripts/Makefile.modbuiltin obj
```

故该命令分别被扩展为：

```
make -f scripts/Makefile.modbuiltin obj=$*
```

其执行过程参见[3.4.3.3.1 make -f scripts/Makefile.modbuiltin obj=$*](#3-4-3-3-1-make-f-scripts-makefile-modbuiltin-obj-)节。

##### 3.4.3.3.1 make -f scripts/Makefile.modbuiltin obj=$*

由modules.builtin节可知，make -f scripts/Makefile.modbuiltin obj=$* 被扩展为：

```
make -f scripts/Makefile.modbuiltin obj=init
make -f scripts/Makefile.modbuiltin obj=usr
make -f scripts/Makefile.modbuiltin obj=arch/x86
make -f scripts/Makefile.modbuiltin obj=kernel
make -f scripts/Makefile.modbuiltin obj=mm
make -f scripts/Makefile.modbuiltin obj=fs
make -f scripts/Makefile.modbuiltin obj=ipc
make -f scripts/Makefile.modbuiltin obj=security
make -f scripts/Makefile.modbuiltin obj=crypto
make -f scripts/Makefile.modbuiltin obj=block
make -f scripts/Makefile.modbuiltin obj=drivers
make -f scripts/Makefile.modbuiltin obj=sound
make -f scripts/Makefile.modbuiltin obj=firmware
make -f scripts/Makefile.modbuiltin obj=net
make -f scripts/Makefile.modbuiltin obj=lib
make -f scripts/Makefile.modbuiltin obj=arch/x86/lib/
```

当执行这些命令时，如果这些目录下存在子目录，则make会递归调用其子目录下的Kbuild或Makefile(若不存在Kbuild文件)，详细的命令调用列表参见[Appendix D: make -f scripts/Makefile.modbuiltin obj=列表](#appendix-d-make-f-scripts-makefile-modbuiltin-obj-)节。

由于这些命令未指明编译目标，故编译scripts/Makefile.modbuiltin的默认目标__modbuiltin:

```
src := $(obj)

PHONY := __modbuiltin
__modbuiltin:

modbuiltin-target  := $(obj)/modules.builtin

__modbuiltin: $(modbuiltin-target) $(subdir-ym)
	@:

$(modbuiltin-target): $(subdir-ym) FORCE
	$(Q)(for m in $(modbuiltin-mods); do echo kernel/$$m; done;	\
	cat /dev/null $(modbuiltin-subdirs)) > $@

...
$(subdir-ym):
	$(Q)$(MAKE) $(modbuiltin)=$@
```

###### 3.4.3.3.1.1 $(subdir-ym)

在scripts/Makefile.modbuiltin中，包含如下规则：

```
// auto.conf中的所有配置项格式为CONFIG_xxx=y或m，均为小写，故可得到obj-y和obj-m列表
-include include/config/auto.conf
# tristate.conf sets tristate variables to uppercase 'Y' or 'M'
# That way, we get the list of built-in modules in obj-Y
// tristate.conf中的所有配置项格式为CONFIG_xxx=Y或M，均为大写，故可得到obj-Y或obj-M列表
-include include/config/tristate.conf

...
include scripts/Makefile.lib
__subdir-Y	:= $(patsubst %/,%,$(filter %/, $(obj-Y)))
subdir-Y	+= $(__subdir-Y)
subdir-ym	:= $(sort $(subdir-y) $(subdir-Y) $(subdir-m))
subdir-ym	:= $(addprefix $(obj)/,$(subdir-ym))

...
$(subdir-ym):
	$(Q)$(MAKE) $(modbuiltin)=$@
```

$(subdir-ym)的取值与如下三部分有关：

* $(subdir-y)，参见scripts/Makefile.lib
* $(subdir-m)，参见scripts/Makefile.lib
* $(subdir-Y)，与配置文件include/config/tristate.conf有关

调用命令 $(Q)$(MAKE) $(modbuiltin)=$@ 递归编译$(obj)指定目录的子目录，该命令被扩展为:

```
make -f scripts/Makefile.modbuiltin obj=$@
```

详细命令列表参见[Appendix D: make -f scripts/Makefile.modbuiltin obj=列表](#appendix-d-make-f-scripts-makefile-modbuiltin-obj-)节。

###### 3.4.3.3.1.2 $(modbuiltin-target)

在scripts/Makefile.modbuiltin中，包含如下规则：

```
modbuiltin-subdirs	:= $(patsubst %,%/modules.builtin, $(subdir-ym))
modbuiltin-mods		:= $(filter %.ko, $(obj-Y:.o=.ko))
modbuiltin-target	:= $(obj)/modules.builtin

...
$(modbuiltin-target): $(subdir-ym) FORCE
	$(Q)(for m in $(modbuiltin-mods); do echo kernel/$$m; done;	\
	cat /dev/null $(modbuiltin-subdirs)) > $@
```

该目标执行下列命令：

```
	$(Q)(for m in $(modbuiltin-mods); do echo kernel/$$m; done;	\
	cat /dev/null $(modbuiltin-subdirs)) > $@
```

以drivers/input/目录为例，该命令被扩展为：

```
(for m in drivers/input/input-core.ko drivers/input/mousedev.ko; do echo kernel/$m; done;	\
	cat /dev/null drivers/input/joystick/modules.builtin drivers/input/keyboard/modules.builtin drivers/input/misc/modules.builtin) > drivers/input/modules.builtin
```

该命令输出文件modules.builtin，用于保存对应目录及其子目录下的*.ko文件列表。

##### 3.4.3.3.2 modules.builtin

在顶层Makefile中，包含如下规则：

```
ifdef CONFIG_MODULES

...
modules.builtin: $(vmlinux-dirs:%=%/modules.builtin)
	$(Q)$(AWK) '!x[$$0]++' $^ > $(objtree)/modules.builtin

...
else # CONFIG_MODULES
...
endif # CONFIG_MODULES
```

命令：

```
$(Q)$(AWK) '!x[$$0]++' $^ > $(objtree)/modules.builtin
```

被扩展为：

```
awk '!x[$0]++' init/modules.builtin usr/modules.builtin arch/x86/modules.builtin kernel/modules.builtin mm/modules.builtin fs/modules.builtin ipc/modules.builtin security/modules.builtin crypto/modules.builtin block/modules.builtin drivers/modules.builtin sound/modules.builtin firmware/modules.builtin arch/x86/pci/modules.builtin arch/x86/power/modules.builtin arch/x86/video/modules.builtin net/modules.builtin lib/modules.builtin arch/x86/lib/modules.builtin > /usr/src/linux-3.2/modules.builtin
```

该命令将所有子目录下的modules.builtin文件(参见[3.4.3.3.1.2 $(modbuiltin-target)](#3-4-3-3-1-2-modbuiltin-target-)节)内容输出到文件linux-3.2/modules.builtin中。该文件包含make modules命令生成的所有*.ko文件列表。执行make modules_install时，将linux-3.2/modules.builtin拷贝到/lib/modules/3.2.0/modules.builtin，参见[安装内核](#3-5-5-)节。

#### 3.4.3.4 modules

在顶层Makefile中，包含如下规则：

```
ifdef CONFIG_MODULES

...
modules: $(vmlinux-dirs) $(if $(KBUILD_BUILTIN),vmlinux) modules.builtin
	// 生成linux-3.2/modules.order，参见modules.order节
	$(Q)$(AWK) '!x[$$0]++' $(vmlinux-dirs:%=$(objtree)/%/modules.order) > $(objtree)/modules.order
	@$(kecho) '  Building modules, stage 2.';
	// 参见make -f scripts/Makefile.modpost节
	$(Q)$(MAKE) -f $(srctree)/scripts/Makefile.modpost
	// 参见make -f scripts/Makefile.fwinst obj=firmware __fw_modbuild节
	$(Q)$(MAKE) -f $(srctree)/scripts/Makefile.fwinst obj=firmware __fw_modbuild

...
else # CONFIG_MODULES
...
endif # CONFIG_MODULES
```

##### 3.4.3.4.1 modules.order

命令 $(Q)$(AWK) '!x[$$0]++' $(vmlinux-dirs:%=$(objtree)/%/modules.order) > $(objtree)/modules.order 被扩展为：

```
awk '!x[$0]++' /usr/src/linux-3.2/init/modules.order /usr/src/linux-3.2/usr/modules.order /usr/src/linux-3.2/arch/x86/modules.order /usr/src/linux-3.2/kernel/modules.order /usr/src/linux-3.2/mm/modules.order /usr/src/linux-3.2/fs/modules.order /usr/src/linux-3.2/ipc/modules.order /usr/src/linux-3.2/security/modules.order /usr/src/linux-3.2/crypto/modules.order /usr/src/linux-3.2/block/modules.order /usr/src/linux-3.2/drivers/modules.order /usr/src/linux-3.2/sound/modules.order /usr/src/linux-3.2/firmware/modules.order /usr/src/linux-3.2/arch/x86/video/modules.order /usr/src/linux-3.2/net/modules.order /usr/src/linux-3.2/lib/modules.order /usr/src/linux-3.2/arch/x86/lib/modules.order > /usr/src/linux-3.2/modules.order
```

该命令将所有子目录下的modules.order文件(参见$(modorder-target)节)内容输出到文件linux-3.2/modules.order中，该文件列出了构建系统内部模块的次序。执行make modules_install时，将linux-3.2/modules.order拷贝到/lib/modules/3.2.0/modules.order，参见[安装内核](#3-5-5-)节。

##### 3.4.3.4.2 make -f scripts/Makefile.modpost

命令 $(Q)$(MAKE) -f $(srctree)/scripts/Makefile.modpost 被扩展为：

```
make -f /usr/src/linux-3.2/scripts/Makefile.modpost
```

因为该命令未指定编译目标，故编译scripts/Makefile.modpost中的默认目标_modpost：

```
PHONY := _modpost
_modpost: __modpost

/*
 * 在顶层Makefile中，MODVERDIR := $(if $(KBUILD_EXTMOD),$(firstword $(KBUILD_EXTMOD))/).tmp_versions
 * .tmp_versions目录是在目标prepare1中创建的，参见prepare1节
 * __modules用于保存.tmp_versions/*.mod文件中以dir/subdir/*.ko结尾的所有行，并按字母顺序进行排序
 */
__modules	:= $(sort $(shell grep -h '\.ko' /dev/null $(wildcard $(MODVERDIR)/*.mod)))
// modules的取值与__modules相同，均为dir/subdir/*.ko列表
modules	:= $(patsubst %.o,%.ko, $(wildcard $(__modules:.ko=.o)))

...
_modpost: $(if $(KBUILD_MODPOST_NOFINAL), $(modules:.ko:.o),$(modules))

__modpost: $(modules:.ko=.o) FORCE
	$(call cmd,modpost) $(wildcard vmlinux) $(filter-out FORCE,$^)

$(modules): %.ko :%.o %.mod.o FORCE
	$(call if_changed,ld_ko_o)

$(modules:.ko=.mod.o): %.mod.o: %.mod.c FORCE
	$(call if_changed_dep,cc_o_c)

$(modules:.ko=.mod.c): __modpost ;
```

各目标之间的依赖关系如下：

![target_modpost](/assets/target_modpost.png)

###### 3.4.3.4.2.1 \_\_modpost

在scripts/Makefile.modpost中，包含如下规则：

```
modpost = scripts/mod/modpost                    \
 $(if $(CONFIG_MODVERSIONS),-m)                  \
 $(if $(CONFIG_MODULE_SRCVERSION_ALL),-a,)       \
 $(if $(KBUILD_EXTMOD),-i,-o) $(kernelsymfile)   \
 $(if $(KBUILD_EXTMOD),-I $(modulesymfile))      \
 $(if $(KBUILD_EXTRA_SYMBOLS), $(patsubst %, -e %,$(KBUILD_EXTRA_SYMBOLS))) \
 $(if $(KBUILD_EXTMOD),-o $(modulesymfile))      \
 $(if $(CONFIG_DEBUG_SECTION_MISMATCH),,-S)      \
 $(if $(KBUILD_EXTMOD)$(KBUILD_MODPOST_WARN),-w) \
 $(if $(cross_build),-c)

quiet_cmd_modpost = MODPOST $(words $(filter-out vmlinux FORCE, $^)) modules
      cmd_modpost = $(modpost) -s

__modpost: $(modules:.ko=.o) FORCE
	$(call cmd,modpost) $(wildcard vmlinux) $(filter-out FORCE,$^)
```

$(modules:.ko=.o)是在目标$(vmlinux-dirs)中编译完成的，参见[3.4.3.1 $(vmlinux-dirs)](#3-4-3-1-vmlinux-dirs-)节。

之后，目标__modpost调用命令：

```
$(call cmd,modpost) $(wildcard vmlinux) $(filter-out FORCE,$^)
```

该命令被扩展为：

```
$(modpost) –s $(wildcard vmlinux) $(filter-out FORCE,$^)
```

继而被扩展为：

```
scripts/mod/modpost -a -o /usr/src/linux-3.2/Module.symvers -s $(modules:.ko=.o)
```

该命令会生成如下文件：

**1) /usr/src/linux-3.2/Module.symvers**

See Documentation/kbuild/modules.txt:

> Module.symvers contains a list of all exported symbols from a kernel build.

**2) *.mod.c**

以hello.c为例，生成的hello.mod.c文件如下，另参见[mod->init/mod->exit与init_module()/cleanup_module()的关联](#)节:

```
#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);

struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0x35ec255d, "module_layout" },
	{ 0x50eedeb8, "printk" },
	{ 0xb4390f9a, "mcount" },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=";


MODULE_INFO(srcversion, "C8EB943C79F42BA9921FE81");
```

以drivers/net/ethernet/intel/e1000e/e1000e.c为例，编译过程中生成的e1000e.mod.c文件如下:

```
#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);

__visible struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

MODULE_INFO(intree, "Y");

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0x420178e0, __VMLINUX_SYMBOL_STR(module_layout) },
	{ 0x6860880e, __VMLINUX_SYMBOL_STR(alloc_pages_current) },
	{ 0x3ce4ca6f, __VMLINUX_SYMBOL_STR(disable_irq) },
	{ 0x2d3385d3, __VMLINUX_SYMBOL_STR(system_wq) },
	{ 0xf744ad48, __VMLINUX_SYMBOL_STR(netdev_info) },
	{ 0x8728198a, __VMLINUX_SYMBOL_STR(kmalloc_caches) },
	{ 0xd2b09ce5, __VMLINUX_SYMBOL_STR(__kmalloc) },
	{ 0x20fcaa16, __VMLINUX_SYMBOL_STR(ethtool_op_get_ts_info) },
	{ 0xe4689576, __VMLINUX_SYMBOL_STR(ktime_get_with_offset) },
	{ 0xf9a482f9, __VMLINUX_SYMBOL_STR(msleep) },
	{ 0x99840d00, __VMLINUX_SYMBOL_STR(timecounter_init) },
	{  0xeec2d, __VMLINUX_SYMBOL_STR(__pm_runtime_idle) },
	{ 0xd6ee688f, __VMLINUX_SYMBOL_STR(vmalloc) },
	{ 0x65b5fe49, __VMLINUX_SYMBOL_STR(param_ops_int) },
	{ 0x91eb9b4, __VMLINUX_SYMBOL_STR(round_jiffies) },
	{ 0xaf34e5b8, __VMLINUX_SYMBOL_STR(napi_disable) },
	{ 0x754d539c, __VMLINUX_SYMBOL_STR(strlen) },
	{ 0xdd2baf66, __VMLINUX_SYMBOL_STR(skb_pad) },
	{ 0xee2f9e23, __VMLINUX_SYMBOL_STR(dma_set_mask) },
	{ 0x30ad4c2e, __VMLINUX_SYMBOL_STR(pci_disable_device) },
	{ 0xf33ff0e, __VMLINUX_SYMBOL_STR(pci_disable_msix) },
	{ 0x4ea25709, __VMLINUX_SYMBOL_STR(dql_reset) },
	{ 0xb0d99f0c, __VMLINUX_SYMBOL_STR(netif_carrier_on) },
	{ 0xea41f64, __VMLINUX_SYMBOL_STR(pm_qos_add_request) },
	{ 0x7f13d491, __VMLINUX_SYMBOL_STR(pm_qos_remove_request) },
	{ 0xc0a3d105, __VMLINUX_SYMBOL_STR(find_next_bit) },
	{ 0x6b06fdce, __VMLINUX_SYMBOL_STR(delayed_work_timer_fn) },
	{ 0xab51580, __VMLINUX_SYMBOL_STR(netif_carrier_off) },
	{ 0x88bfa7e, __VMLINUX_SYMBOL_STR(cancel_work_sync) },
	{ 0xbd8afbb8, __VMLINUX_SYMBOL_STR(__dev_kfree_skb_any) },
	{ 0xeae3dfd6, __VMLINUX_SYMBOL_STR(__const_udelay) },
	{ 0x9580deb, __VMLINUX_SYMBOL_STR(init_timer_key) },
	{ 0xd3000832, __VMLINUX_SYMBOL_STR(pcie_capability_clear_and_set_word) },
	{ 0xa57863e, __VMLINUX_SYMBOL_STR(cancel_delayed_work_sync) },
	{ 0xe6048175, __VMLINUX_SYMBOL_STR(mutex_unlock) },
	{ 0xed21bd02, __VMLINUX_SYMBOL_STR(__pm_runtime_resume) },
	{ 0x999e8297, __VMLINUX_SYMBOL_STR(vfree) },
	{ 0x83472897, __VMLINUX_SYMBOL_STR(dma_free_attrs) },
	{ 0xbfe2cb70, __VMLINUX_SYMBOL_STR(pci_bus_write_config_word) },
	{ 0x893a01a6, __VMLINUX_SYMBOL_STR(pci_disable_link_state_locked) },
	{ 0xf4c91ed, __VMLINUX_SYMBOL_STR(ns_to_timespec) },
	{ 0xc499ae1e, __VMLINUX_SYMBOL_STR(kstrdup) },
	{ 0x7d11c268, __VMLINUX_SYMBOL_STR(jiffies) },
	{ 0x91ba0d02, __VMLINUX_SYMBOL_STR(__dynamic_netdev_dbg) },
	{ 0x3ce3bc30, __VMLINUX_SYMBOL_STR(skb_trim) },
	{ 0x1b3b6da3, __VMLINUX_SYMBOL_STR(__netdev_alloc_skb) },
	{ 0x27c33efe, __VMLINUX_SYMBOL_STR(csum_ipv6_magic) },
	{ 0xcaaacf2e, __VMLINUX_SYMBOL_STR(__pskb_pull_tail) },
	{ 0xb0e16c7, __VMLINUX_SYMBOL_STR(ptp_clock_unregister) },
	{ 0x4f8b5ddb, __VMLINUX_SYMBOL_STR(_copy_to_user) },
	{ 0x76f5966a, __VMLINUX_SYMBOL_STR(pci_set_master) },
	{ 0xee7cdf54, __VMLINUX_SYMBOL_STR(netif_schedule_queue) },
	{ 0x706d051c, __VMLINUX_SYMBOL_STR(del_timer_sync) },
	{ 0xfb578fc5, __VMLINUX_SYMBOL_STR(memset) },
	{ 0xf0df2a5f, __VMLINUX_SYMBOL_STR(pci_enable_pcie_error_reporting) },
	{ 0xe0e4f728, __VMLINUX_SYMBOL_STR(netif_tx_wake_queue) },
	{ 0x36c1f2ce, __VMLINUX_SYMBOL_STR(pci_restore_state) },
	{ 0x9c9c66a4, __VMLINUX_SYMBOL_STR(dev_err) },
	{ 0x1916e38c, __VMLINUX_SYMBOL_STR(_raw_spin_unlock_irqrestore) },
	{ 0x85467e31, __VMLINUX_SYMBOL_STR(current_task) },
	{ 0xeb784c5f, __VMLINUX_SYMBOL_STR(ethtool_op_get_link) },
	{ 0x27e1a049, __VMLINUX_SYMBOL_STR(printk) },
	{ 0xa00aca2a, __VMLINUX_SYMBOL_STR(dql_completed) },
	{ 0x4c9d28b0, __VMLINUX_SYMBOL_STR(phys_base) },
	{ 0xc39a30e2, __VMLINUX_SYMBOL_STR(free_netdev) },
	{ 0xa1c76e0a, __VMLINUX_SYMBOL_STR(_cond_resched) },
	{ 0xc7c5ae39, __VMLINUX_SYMBOL_STR(register_netdev) },
	{ 0x5792f848, __VMLINUX_SYMBOL_STR(strlcpy) },
	{ 0xe6a1061c, __VMLINUX_SYMBOL_STR(dma_alloc_attrs) },
	{ 0x16305289, __VMLINUX_SYMBOL_STR(warn_slowpath_null) },
	{ 0xfbd63449, __VMLINUX_SYMBOL_STR(__pci_enable_wake) },
	{ 0xa5bba893, __VMLINUX_SYMBOL_STR(mutex_lock) },
	{ 0x393d4de9, __VMLINUX_SYMBOL_STR(crc32_le) },
	{ 0x6d8b0e69, __VMLINUX_SYMBOL_STR(dev_close) },
	{ 0x20e7f58, __VMLINUX_SYMBOL_STR(__dev_kfree_skb_irq) },
	{ 0x16e5c2a, __VMLINUX_SYMBOL_STR(mod_timer) },
	{ 0x660735f6, __VMLINUX_SYMBOL_STR(netif_napi_add) },
	{ 0x71b0e23f, __VMLINUX_SYMBOL_STR(ptp_clock_register) },
	{ 0x2072ee9b, __VMLINUX_SYMBOL_STR(request_threaded_irq) },
	{ 0x3b803f6d, __VMLINUX_SYMBOL_STR(device_wakeup_enable) },
	{ 0xf6fd855f, __VMLINUX_SYMBOL_STR(pci_clear_master) },
	{ 0x1be08d7c, __VMLINUX_SYMBOL_STR(dev_open) },
	{ 0xe523ad75, __VMLINUX_SYMBOL_STR(synchronize_irq) },
	{ 0xc542933a, __VMLINUX_SYMBOL_STR(timecounter_read) },
	{ 0x69653fc1, __VMLINUX_SYMBOL_STR(dev_notice) },
	{ 0x167c5967, __VMLINUX_SYMBOL_STR(print_hex_dump) },
	{ 0xfef0a6f1, __VMLINUX_SYMBOL_STR(pci_select_bars) },
	{ 0xa8b76a68, __VMLINUX_SYMBOL_STR(timecounter_cyc2time) },
	{ 0xa916ca8d, __VMLINUX_SYMBOL_STR(netif_device_attach) },
	{ 0xe3c8a6d7, __VMLINUX_SYMBOL_STR(napi_gro_receive) },
	{ 0x50e8877f, __VMLINUX_SYMBOL_STR(_dev_info) },
	{ 0x40a9b349, __VMLINUX_SYMBOL_STR(vzalloc) },
	{ 0xeeb1eb27, __VMLINUX_SYMBOL_STR(pci_disable_link_state) },
	{ 0xee2754a8, __VMLINUX_SYMBOL_STR(netif_device_detach) },
	{ 0x6839ed62, __VMLINUX_SYMBOL_STR(__alloc_skb) },
	{ 0x42c8de35, __VMLINUX_SYMBOL_STR(ioremap_nocache) },
	{ 0x12a38747, __VMLINUX_SYMBOL_STR(usleep_range) },
	{ 0x7e03c231, __VMLINUX_SYMBOL_STR(pci_enable_msix_range) },
	{ 0x927a02a0, __VMLINUX_SYMBOL_STR(pci_bus_read_config_word) },
	{ 0x6c4d5fb, __VMLINUX_SYMBOL_STR(__napi_schedule) },
	{ 0x70cd1f, __VMLINUX_SYMBOL_STR(queue_delayed_work_on) },
	{ 0xb81c3712, __VMLINUX_SYMBOL_STR(pci_cleanup_aer_uncorrect_error_status) },
	{ 0x46258b48, __VMLINUX_SYMBOL_STR(pm_schedule_suspend) },
	{ 0xa89987e1, __VMLINUX_SYMBOL_STR(napi_complete_done) },
	{ 0x7478f512, __VMLINUX_SYMBOL_STR(eth_type_trans) },
	{ 0x14496b8c, __VMLINUX_SYMBOL_STR(pskb_expand_head) },
	{ 0xbdfb6dbb, __VMLINUX_SYMBOL_STR(__fentry__) },
	{ 0x5bbb85a1, __VMLINUX_SYMBOL_STR(netdev_err) },
	{ 0x467df16d, __VMLINUX_SYMBOL_STR(netdev_rss_key_fill) },
	{ 0x855db502, __VMLINUX_SYMBOL_STR(pci_enable_msi_range) },
	{ 0x7f243c4d, __VMLINUX_SYMBOL_STR(pci_unregister_driver) },
	{ 0xcc5005fe, __VMLINUX_SYMBOL_STR(msleep_interruptible) },
	{ 0x9b5c5d69, __VMLINUX_SYMBOL_STR(kmem_cache_alloc_trace) },
	{ 0xe259ae9e, __VMLINUX_SYMBOL_STR(_raw_spin_lock) },
	{ 0x680ec266, __VMLINUX_SYMBOL_STR(_raw_spin_lock_irqsave) },
	{ 0xf6ebc03b, __VMLINUX_SYMBOL_STR(net_ratelimit) },
	{ 0x7bf58702, __VMLINUX_SYMBOL_STR(netdev_warn) },
	{ 0xf7de5d93, __VMLINUX_SYMBOL_STR(eth_validate_addr) },
	{ 0xabab7c3a, __VMLINUX_SYMBOL_STR(pci_disable_pcie_error_reporting) },
	{ 0xfcec0987, __VMLINUX_SYMBOL_STR(enable_irq) },
	{ 0x37a0cba, __VMLINUX_SYMBOL_STR(kfree) },
	{ 0x69acdf38, __VMLINUX_SYMBOL_STR(memcpy) },
	{ 0x93f11a07, __VMLINUX_SYMBOL_STR(___pskb_trim) },
	{ 0x75e1fdc7, __VMLINUX_SYMBOL_STR(param_array_ops) },
	{ 0x55f9b4c, __VMLINUX_SYMBOL_STR(ptp_clock_index) },
	{ 0x53c47218, __VMLINUX_SYMBOL_STR(pci_disable_msi) },
	{ 0xf2f2267b, __VMLINUX_SYMBOL_STR(dma_supported) },
	{ 0xedc03953, __VMLINUX_SYMBOL_STR(iounmap) },
	{ 0x38db821d, __VMLINUX_SYMBOL_STR(pci_prepare_to_sleep) },
	{ 0x78dd04c6, __VMLINUX_SYMBOL_STR(pci_dev_run_wake) },
	{ 0x880670bd, __VMLINUX_SYMBOL_STR(__pci_register_driver) },
	{ 0xc357923c, __VMLINUX_SYMBOL_STR(pm_qos_update_request) },
	{ 0x58a2b881, __VMLINUX_SYMBOL_STR(put_page) },
	{ 0xb352177e, __VMLINUX_SYMBOL_STR(find_first_bit) },
	{ 0xf2c69a59, __VMLINUX_SYMBOL_STR(dev_warn) },
	{ 0x3590fefe, __VMLINUX_SYMBOL_STR(unregister_netdev) },
	{ 0x2e0d2f7f, __VMLINUX_SYMBOL_STR(queue_work_on) },
	{ 0x28318305, __VMLINUX_SYMBOL_STR(snprintf) },
	{ 0xbdcf9640, __VMLINUX_SYMBOL_STR(consume_skb) },
	{ 0x32b060f5, __VMLINUX_SYMBOL_STR(pci_enable_device_mem) },
	{ 0xb99003f0, __VMLINUX_SYMBOL_STR(__napi_alloc_skb) },
	{ 0xb651ecb0, __VMLINUX_SYMBOL_STR(skb_tstamp_tx) },
	{ 0xfd33aebd, __VMLINUX_SYMBOL_STR(skb_put) },
	{ 0xcce7db0, __VMLINUX_SYMBOL_STR(pci_release_selected_regions) },
	{ 0x4f6b400b, __VMLINUX_SYMBOL_STR(_copy_from_user) },
	{ 0x11a87f43, __VMLINUX_SYMBOL_STR(param_ops_uint) },
	{ 0xdf59da8e, __VMLINUX_SYMBOL_STR(pcie_capability_write_word) },
	{ 0x9e7d6bd0, __VMLINUX_SYMBOL_STR(__udelay) },
	{ 0x68ce7ed9, __VMLINUX_SYMBOL_STR(dma_ops) },
	{ 0xd619a163, __VMLINUX_SYMBOL_STR(pci_request_selected_regions_exclusive) },
	{ 0xd9f6c399, __VMLINUX_SYMBOL_STR(device_set_wakeup_enable) },
	{ 0x7a29ada4, __VMLINUX_SYMBOL_STR(pcie_capability_read_word) },
	{ 0xf20dabd8, __VMLINUX_SYMBOL_STR(free_irq) },
	{ 0xd8d8f7a7, __VMLINUX_SYMBOL_STR(pci_save_state) },
	{ 0xd831efc6, __VMLINUX_SYMBOL_STR(alloc_etherdev_mqs) },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=ptp";

/*
 * 宏MODULE_ALIAS参见13.1.2.1 MODULE_INFO()/__MODULE_INFO()节;
 * 通过下列命令查看编译后的e1000e.ko中的alias:
 *   # objdump -s --section=.modinfo ./drivers/net/ethernet/intel/e1000e/e1000e.ko
 */
MODULE_ALIAS("pci:v00008086d0000105Esv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d0000105Fsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010A4sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010BCsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010A5sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d00001060sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010D9sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010DAsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010D5sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010B9sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d0000107Dsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d0000107Esv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d0000107Fsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d0000108Bsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d0000108Csv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d0000109Asv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010D3sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010F6sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d0000150Csv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d00001096sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010BAsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d00001098sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010BBsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d0000104Csv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010C5sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010C4sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d0000104Asv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d0000104Bsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d0000104Dsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d00001049sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d00001501sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010C0sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010C2sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010C3sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010BDsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d0000294Csv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010E5sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010BFsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010F5sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010CBsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010CCsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010CDsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010CEsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010DEsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010DFsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d00001525sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010EAsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010EBsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010EFsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000010F0sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d00001502sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d00001503sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d0000153Asv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d0000153Bsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d0000155Asv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d00001559sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000015A0sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000015A1sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000015A2sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000015A3sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d0000156Fsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d00001570sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000015B7sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00008086d000015B8sv*sd*bc*sc*i*");

MODULE_INFO(srcversion, "224852E6236A925EFB3CC8C");
```

###### 3.4.3.4.2.2 %.mod.c=>%.mod.o

\*.mod.c是在目标$(builtin-target)执行命令cmd_link_o_target时生成的，参见[3.4.2.1.3.1.1.2 cmd_link_o_target](#3-4-2-1-3-1-1-2-cmd-link-o-target)节。

在scripts/Makefile.modpost中，包含如下规则：

```
quiet_cmd_cc_o_c = CC      $@
      cmd_cc_o_c = $(CC) $(c_flags) $(KBUILD_CFLAGS_MODULE) $(CFLAGS_MODULE) \
		   -c -o $@ $<

$(modules:.ko=.mod.o): %.mod.o: %.mod.c FORCE
	$(call if_changed_dep,cc_o_c)
```

调用命令cmd_cc_o_c将*.mod.c编译成*.mod.o。以arch/x86/crypto/aes-i586.mod.c为例，该命令被扩展为：

```
gcc -Wp,-MD,arch/x86/crypto/.aes-i586.mod.o.d  -nostdinc -isystem /usr/lib/gcc/i686-linux-gnu/4.7/include -I/usr/src/linux-3.2/arch/x86/include -Iarch/x86/include/generated -Iinclude  -include /usr/src/linux-3.2/include/linux/kconfig.h -D__KERNEL__ -Wall -Wundef -Wstrict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -Werror-implicit-function-declaration -Wno-format-security -fno-delete-null-pointer-checks -Os -m32 -msoft-float -mregparm=3 -freg-struct-return -mpreferred-stack-boundary=2 -march=i686 -maccumulate-outgoing-args -Wa,-mtune=generic32 -ffreestanding -fstack-protector -DCONFIG_AS_CFI=1 -DCONFIG_AS_CFI_SIGNAL_FRAME=1 -DCONFIG_AS_CFI_SECTIONS=1 -pipe -Wno-sign-compare -fno-asynchronous-unwind-tables -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -Wframe-larger-than=1024 -Wno-unused-but-set-variable -fno-omit-frame-pointer -fno-optimize-sibling-calls -fno-inline-functions-called-once -Wdeclaration-after-statement -Wno-pointer-sign -fno-strict-overflow -fconserve-stack -DCC_HAVE_ASM_GOTO   -D"KBUILD_STR(s)=#s" -D"KBUILD_BASENAME=KBUILD_STR(aes_i586.mod)"  -D"KBUILD_MODNAME=KBUILD_STR(aes_i586)" -DMODULE  -c -o arch/x86/crypto/aes-i586.mod.o arch/x86/crypto/aes-i586.mod.c
```

###### 3.4.3.4.2.3 $(modules)

在scripts/Makefile.modpost中，包含如下规则：

```
quiet_cmd_ld_ko_o = LD [M]  $@
      cmd_ld_ko_o = $(LD) -r $(LDFLAGS)							\
                             $(KBUILD_LDFLAGS_MODULE) $(LDFLAGS_MODULE)	\
                             -o $@ $(filter-out FORCE,$^)

$(modules): %.ko : %.o %.mod.o FORCE
	$(call if_changed,ld_ko_o)
```

调用命令cmd_ld_ko_o将*.mod.o和*.o连接成*.ko。以arch/x86/crypto/aes-i586.mod.c为例，该命令被扩展为：

```
ld -r -m elf_i386 -T /usr/src/linux-3.2/scripts/module-common.lds --build-id  -o arch/x86/crypto/aes-i586.ko arch/x86/crypto/aes-i586.o arch/x86/crypto/aes-i586.mod.o
```

[**NOTE1**] 执行make modules_install命令时，这些*.ko文件会被安装到/lib/modules/3.2.0/kernel/目录，参见[安装内核](#3-5-5-)节；

[**NOTE2**] script/module-common.lds是生成*.ko文件的链接脚本文件，参见[Appendix H: scripts/module-common.lds](#appendix-h-scripts-module-common-lds)节。

##### 3.4.3.4.3 make -f scripts/Makefile.fwinst obj=firmware \_\_fw_modbuild

在scripts/Makefile.fwinst中，包含如下规则：

```
/*
 * 引入firmware/Makefile，其中包含$(fw-shipped-m)和$(fw-shipped-y)
 * $(fw-shipped-m)和$(fw-shipped-y)中包含*.fw, *.bin, *.dsp列表
 */
include $(srctree)/$(obj)/Makefile

...
mod-fw := $(fw-shipped-m)
# If CONFIG_FIRMWARE_IN_KERNEL isn't set, then install the
# firmware for in-kernel drivers too.
ifndef CONFIG_FIRMWARE_IN_KERNEL
mod-fw += $(fw-shipped-y)
endif

...
__fw_modbuild: $(addprefix $(obj)/,$(mod-fw))
	@:
```

###### 3.4.3.4.3.1 $(mod-fw)

在firmware/Makefile中，包含如下规则：

```
...
// $(fw-shipped-m)和$(fw-shipped-y)中包含*.fw, *.bin, *.dsp列表
fw-shipped-$(CONFIG_3C359) += 3com/3C359.bin
fw-shipped-$(CONFIG_ACENIC) += $(acenic-objs)
fw-shipped-$(CONFIG_ADAPTEC_STARFIRE) += adaptec/starfire_rx.bin \
				 adaptec/starfire_tx.bin
fw-shipped-$(CONFIG_ATARI_DSP56K) += dsp56k/bootstrap.bin
fw-shipped-$(CONFIG_ATM_AMBASSADOR) += atmsar11.fw
fw-shipped-$(CONFIG_BNX2X) += bnx2x/bnx2x-e1-6.2.9.0.fw \
			     bnx2x/bnx2x-e1h-6.2.9.0.fw \
			     bnx2x/bnx2x-e2-6.2.9.0.fw
fw-shipped-$(CONFIG_BNX2) += bnx2/bnx2-mips-09-6.2.1a.fw \
			     bnx2/bnx2-rv2p-09-6.0.17.fw \
			     bnx2/bnx2-rv2p-09ax-6.0.17.fw \
			     bnx2/bnx2-mips-06-6.2.1.fw \
			     bnx2/bnx2-rv2p-06-6.0.15.fw
fw-shipped-$(CONFIG_CASSINI) += sun/cassini.bin
fw-shipped-$(CONFIG_COMPUTONE) += intelliport2.bin
...

quiet_cmd_ihex	= IHEX    $@
      cmd_ihex		= $(OBJCOPY) -Iihex -Obinary $< $@

...
// firmware/目录中已存在*.ihex文件
$(obj)/%: $(obj)/%.ihex | $(objtree)/$(obj)/$$(dir %)
	$(call cmd,ihex)
```

调用cmd_ihex命令，以firmware/bnx2/bnx2-mips-09-6.2.1a.fw为例，该命令被扩展为：

```
objcopy -Iihex -Obinary firmware/bnx2/bnx2-mips-09-6.2.1a.fw.ihex firmware/bnx2/bnx2-mips-09-6.2.1a.fw
```

该命令输出如下文件：

```
firmware/oneSubdir/twoSubdir/.../*.fw
firmware/oneSubdir/twoSubdir/.../*.bin
firmware/oneSubdir/twoSubdir/.../*.dsp
```

### 3.4.4 编译external modules

执行下列命令之一来编译外部模块:

```
# make -C <kernel_src_dir> M=<ext_module_dir> modules
# make -C <kernel_src_dir> SUBDIRS=$PWD modules
```

在顶层Makefile中，包含如下规则：

```
# Use make M=dir to specify directory of external module to build
# Old syntax make ... SUBDIRS=$PWD is still supported
# Setting the environment variable KBUILD_EXTMOD take precedence
ifdef SUBDIRS
  KBUILD_EXTMOD ?= $(SUBDIRS)
endif

ifeq ("$(origin M)", "command line")
  KBUILD_EXTMOD := $(M)
endif

...

# That's our default target when none is given on the command line
PHONY := _all
_all:

# If building an external module we do not care about the all: rule
# but instead _all depend on modules
PHONY += all
ifeq ($(KBUILD_EXTMOD),)
_all: all
else
_all: modules	// 此时定义了KBUILD_EXTMOD，故进入本分支
endif

# When compiling out-of-tree modules, put MODVERDIR in the module
# tree rather than in the kernel tree. The kernel tree might
# even be read-only.
// 在命令cmd_crmodverdir中使用
export MODVERDIR := $(if $(KBUILD_EXTMOD),$(firstword $(KBUILD_EXTMOD))/).tmp_versions

ifeq ($(KBUILD_EXTMOD),)
...
else # KBUILD_EXTMOD

###
# External module support.
# When building external modules the kernel used as basis is considered
# read-only, and no consistency checks are made and the make
# system is not used on the basis kernel. If updates are required
# in the basis kernel ordinary make commands (without M=...) must
# be used.
#
# The following are the only valid targets when building external
# modules.
# make M=dir clean	Delete all automatically generated files
# make M=dir modules	Make all modules in specified dir
# make M=dir		Same as 'make M=dir modules'
# make M=dir modules_install
#				Install the modules built in the module directory
#				Assumes install directory is already created

# We are always building modules
KBUILD_MODULES := 1
PHONY += crmodverdir

/*
 * (1) 该目标执行命令cmd_crmodverdir，用于在外部模块源代码
 *     目录中创建临时目录.tmp_versions/，用于保存*.mod文件
 */
crmodverdir:
	$(cmd_crmodverdir)

/*
 * (2) 检查$(objtree)/Module.symvers是否存在
 */
PHONY += $(objtree)/Module.symvers
$(objtree)/Module.symvers:
	@test -e $(objtree)/Module.symvers || ( \
	echo; \
	echo "  WARNING: Symbol version dump $(objtree)/Module.symvers"; \
	echo "           is missing; modules will have no dependencies and modversions."; \
	echo )

/*
 * (3) 编译外部模块源代码目录
 *     示例：若外部模块源代码所在目录为/ext/module/src，
 *     则module-dirs被扩展为_module_/ext/module/src
 */
module-dirs := $(addprefix _module_,$(KBUILD_EXTMOD))
PHONY += $(module-dirs) modules
$(module-dirs): crmodverdir $(objtree)/Module.symvers
	/*
	 * 示例：扩展为make –f scripts/Makefile.build obj=/ext/module/src
	 * 编译外部模块源代码目录，参见make -f scripts/Makefile.build obj=XXX命令的执行过程节，
	 * 其中，$(obj-m)由外部模块源代码目录中的Makefile配置
	 */
	$(Q)$(MAKE) $(build)=$(patsubst _module_%,%,$@)

/*
 * (4) Stage 2 of building external modules
 */
modules: $(module-dirs)
	@$(kecho) '  Building modules, stage 2.';
	/*
	 * 扩展为make –f scripts/Makefile.modpost，
	 * 其执行过程参见make -f scripts/Makefile.modpost节
	 */
	$(Q)$(MAKE) -f $(srctree)/scripts/Makefile.modpost

endif # KBUILD_EXTMOD

...
# Create temporary dir for module support files
# clean it up only when building all modules
cmd_crmodverdir = $(Q)mkdir -p $(MODVERDIR) \
                      $(if $(KBUILD_MODULES),; rm -f $(MODVERDIR)/*)
```

各目标之间的依赖关系如下：

![target_modules](/assets/target_modules.png)

### 3.4.4A 只编译内核中的某个驱动程序

以驱动程序drivers/net/ethernet/intel/e1000e为例，按照如下步骤编译该驱动程序:

```
# 切换到和当前内核版本匹配的内核版本
chenwx@chenwx ~/linux $ uname -r
4.2.2-alex
chenwx@chenwx ~/linux $ git co v4.2.2
Previous HEAD position was 64291f7db5bd... Linux 4.2
HEAD is now at 7659db320e01... Linux 4.2.2

# 为编译内核做准备
chenwx@chenwx ~/linux $ make O=../linux-build/ modules_prepare
make[1]: Entering directory `/home/chenwx/linux-build'
  SYSTBL  arch/x86/entry/syscalls/../../include/generated/asm/syscalls_32.h
  SYSHDR  arch/x86/entry/syscalls/../../include/generated/asm/unistd_32_ia32.h
  SYSHDR  arch/x86/entry/syscalls/../../include/generated/asm/unistd_64_x32.h
  SYSTBL  arch/x86/entry/syscalls/../../include/generated/asm/syscalls_64.h
  SYSHDR  arch/x86/entry/syscalls/../../include/generated/uapi/asm/unistd_32.h
  SYSHDR  arch/x86/entry/syscalls/../../include/generated/uapi/asm/unistd_64.h
  SYSHDR  arch/x86/entry/syscalls/../../include/generated/uapi/asm/unistd_x32.h
  HOSTCC  scripts/basic/bin2c
  HOSTCC  arch/x86/tools/relocs_32.o
  HOSTCC  arch/x86/tools/relocs_64.o
  HOSTCC  arch/x86/tools/relocs_common.o
  HOSTLD  arch/x86/tools/relocs
  CHK     include/config/kernel.release
  UPD     include/config/kernel.release
  Using /home/chenwx/linux as source for kernel
  GEN     ./Makefile
  WRAP    arch/x86/include/generated/asm/clkdev.h
  WRAP    arch/x86/include/generated/asm/cputime.h
  WRAP    arch/x86/include/generated/asm/dma-contiguous.h
  WRAP    arch/x86/include/generated/asm/early_ioremap.h
  WRAP    arch/x86/include/generated/asm/mcs_spinlock.h
  WRAP    arch/x86/include/generated/asm/mm-arch-hooks.h
  CHK     include/generated/uapi/linux/version.h
  UPD     include/generated/uapi/linux/version.h
  CHK     include/generated/utsrelease.h
  UPD     include/generated/utsrelease.h
  CC      kernel/bounds.s
  CHK     include/generated/bounds.h
  UPD     include/generated/bounds.h
  CHK     include/generated/timeconst.h
  UPD     include/generated/timeconst.h
  CC      arch/x86/kernel/asm-offsets.s
  CHK     include/generated/asm-offsets.h
  UPD     include/generated/asm-offsets.h
  CALL    /home/chenwx/linux/scripts/checksyscalls.sh
  HOSTCC  scripts/genksyms/genksyms.o
  SHIPPED scripts/genksyms/parse.tab.c
  HOSTCC  scripts/genksyms/parse.tab.o
  SHIPPED scripts/genksyms/lex.lex.c
  SHIPPED scripts/genksyms/keywords.hash.c
  SHIPPED scripts/genksyms/parse.tab.h
  HOSTCC  scripts/genksyms/lex.lex.o
  HOSTLD  scripts/genksyms/genksyms
  CC      scripts/mod/empty.o
  HOSTCC  scripts/mod/mk_elfconfig
  MKELF   scripts/mod/elfconfig.h
  HOSTCC  scripts/mod/modpost.o
  CC      scripts/mod/devicetable-offsets.s
  GEN     scripts/mod/devicetable-offsets.h
  HOSTCC  scripts/mod/file2alias.o
  HOSTCC  scripts/mod/sumversion.o
  HOSTLD  scripts/mod/modpost
  HOSTCC  scripts/selinux/genheaders/genheaders
  HOSTCC  scripts/selinux/mdp/mdp
  HOSTCC  scripts/kallsyms
  HOSTCC  scripts/conmakehash
  HOSTCC  scripts/recordmcount
  HOSTCC  scripts/sortextable
make[1]: Leaving directory `/home/chenwx/linux-build'

# 编译驱动程序drivers/net/ethernet/intel/e1000e
chenwx@chenwx ~/linux $ make O=../linux-build/ M=drivers/net/ethernet/intel/e1000e
make[1]: Entering directory `/home/chenwx/linux-build'

  WARNING: Symbol version dump ./Module.symvers
           is missing; modules will have no dependencies and modversions.

  CC [M]  drivers/net/ethernet/intel/e1000e/82571.o
  CC [M]  drivers/net/ethernet/intel/e1000e/ich8lan.o
  CC [M]  drivers/net/ethernet/intel/e1000e/80003es2lan.o
  CC [M]  drivers/net/ethernet/intel/e1000e/mac.o
  CC [M]  drivers/net/ethernet/intel/e1000e/manage.o
  CC [M]  drivers/net/ethernet/intel/e1000e/nvm.o
  CC [M]  drivers/net/ethernet/intel/e1000e/phy.o
  CC [M]  drivers/net/ethernet/intel/e1000e/param.o
  CC [M]  drivers/net/ethernet/intel/e1000e/ethtool.o
  CC [M]  drivers/net/ethernet/intel/e1000e/netdev.o
  CC [M]  drivers/net/ethernet/intel/e1000e/ptp.o
  LD [M]  drivers/net/ethernet/intel/e1000e/e1000e.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC      drivers/net/ethernet/intel/e1000e/e1000e.mod.o
  LD [M]  drivers/net/ethernet/intel/e1000e/e1000e.ko
make[1]: Leaving directory `/home/chenwx/linux-build'

# 查看编译后的驱动程序drivers/net/ethernet/intel/e1000e
chenwx@chenwx ~/linux $ ll ../linux-build/drivers/net/ethernet/intel/e1000e
total 13M
-rw-r--r-- 1 chenwx chenwx 314K Oct  7 21:39 80003es2lan.o
-rw-r--r-- 1 chenwx chenwx 334K Oct  7 21:39 82571.o
-rw-r--r-- 1 chenwx chenwx    0 Oct  7 21:39 Module.symvers
-rw-r--r-- 1 chenwx chenwx    8 Oct  7 21:39 built-in.o
-rw-r--r-- 1 chenwx chenwx 4.2M Oct  7 21:39 e1000e.ko
-rw-r--r-- 1 chenwx chenwx  13K Oct  7 21:39 e1000e.mod.c
-rw-r--r-- 1 chenwx chenwx  70K Oct  7 21:39 e1000e.mod.o
-rw-r--r-- 1 chenwx chenwx 4.1M Oct  7 21:39 e1000e.o
-rw-r--r-- 1 chenwx chenwx 410K Oct  7 21:39 ethtool.o
-rw-r--r-- 1 chenwx chenwx 476K Oct  7 21:39 ich8lan.o
-rw-r--r-- 1 chenwx chenwx 337K Oct  7 21:39 mac.o
-rw-r--r-- 1 chenwx chenwx 263K Oct  7 21:39 manage.o
-rw-r--r-- 1 chenwx chenwx   51 Oct  7 21:39 modules.order
-rw-r--r-- 1 chenwx chenwx 855K Oct  7 21:39 netdev.o
-rw-r--r-- 1 chenwx chenwx 284K Oct  7 21:39 nvm.o
-rw-r--r-- 1 chenwx chenwx 287K Oct  7 21:39 param.o
-rw-r--r-- 1 chenwx chenwx 386K Oct  7 21:39 phy.o
-rw-r--r-- 1 chenwx chenwx 266K Oct  7 21:39 ptp.o

chenwx@chenwx ~/linux $ modinfo ../linux-build/drivers/net/ethernet/intel/e1000e/e1000e.ko
filename:       /home/chenwx/linux/../linux-build/drivers/net/ethernet/intel/e1000e/e1000e.ko
version:        3.2.5-k
license:        GPL
description:    Intel(R) PRO/1000 Network Driver
author:         Intel Corporation, <linux.nics@intel.com>
srcversion:     224852E6236A925EFB3CC8C
alias:          pci:v00008086d000015B8sv*sd*bc*sc*i*
alias:          pci:v00008086d000015B7sv*sd*bc*sc*i*
alias:          pci:v00008086d00001570sv*sd*bc*sc*i*
alias:          pci:v00008086d0000156Fsv*sd*bc*sc*i*
alias:          pci:v00008086d000015A3sv*sd*bc*sc*i*
alias:          pci:v00008086d000015A2sv*sd*bc*sc*i*
alias:          pci:v00008086d000015A1sv*sd*bc*sc*i*
alias:          pci:v00008086d000015A0sv*sd*bc*sc*i*
alias:          pci:v00008086d00001559sv*sd*bc*sc*i*
alias:          pci:v00008086d0000155Asv*sd*bc*sc*i*
alias:          pci:v00008086d0000153Bsv*sd*bc*sc*i*
alias:          pci:v00008086d0000153Asv*sd*bc*sc*i*
alias:          pci:v00008086d00001503sv*sd*bc*sc*i*
alias:          pci:v00008086d00001502sv*sd*bc*sc*i*
alias:          pci:v00008086d000010F0sv*sd*bc*sc*i*
alias:          pci:v00008086d000010EFsv*sd*bc*sc*i*
alias:          pci:v00008086d000010EBsv*sd*bc*sc*i*
alias:          pci:v00008086d000010EAsv*sd*bc*sc*i*
alias:          pci:v00008086d00001525sv*sd*bc*sc*i*
alias:          pci:v00008086d000010DFsv*sd*bc*sc*i*
alias:          pci:v00008086d000010DEsv*sd*bc*sc*i*
alias:          pci:v00008086d000010CEsv*sd*bc*sc*i*
alias:          pci:v00008086d000010CDsv*sd*bc*sc*i*
alias:          pci:v00008086d000010CCsv*sd*bc*sc*i*
alias:          pci:v00008086d000010CBsv*sd*bc*sc*i*
alias:          pci:v00008086d000010F5sv*sd*bc*sc*i*
alias:          pci:v00008086d000010BFsv*sd*bc*sc*i*
alias:          pci:v00008086d000010E5sv*sd*bc*sc*i*
alias:          pci:v00008086d0000294Csv*sd*bc*sc*i*
alias:          pci:v00008086d000010BDsv*sd*bc*sc*i*
alias:          pci:v00008086d000010C3sv*sd*bc*sc*i*
alias:          pci:v00008086d000010C2sv*sd*bc*sc*i*
alias:          pci:v00008086d000010C0sv*sd*bc*sc*i*
alias:          pci:v00008086d00001501sv*sd*bc*sc*i*
alias:          pci:v00008086d00001049sv*sd*bc*sc*i*
alias:          pci:v00008086d0000104Dsv*sd*bc*sc*i*
alias:          pci:v00008086d0000104Bsv*sd*bc*sc*i*
alias:          pci:v00008086d0000104Asv*sd*bc*sc*i*
alias:          pci:v00008086d000010C4sv*sd*bc*sc*i*
alias:          pci:v00008086d000010C5sv*sd*bc*sc*i*
alias:          pci:v00008086d0000104Csv*sd*bc*sc*i*
alias:          pci:v00008086d000010BBsv*sd*bc*sc*i*
alias:          pci:v00008086d00001098sv*sd*bc*sc*i*
alias:          pci:v00008086d000010BAsv*sd*bc*sc*i*
alias:          pci:v00008086d00001096sv*sd*bc*sc*i*
alias:          pci:v00008086d0000150Csv*sd*bc*sc*i*
alias:          pci:v00008086d000010F6sv*sd*bc*sc*i*
alias:          pci:v00008086d000010D3sv*sd*bc*sc*i*
alias:          pci:v00008086d0000109Asv*sd*bc*sc*i*
alias:          pci:v00008086d0000108Csv*sd*bc*sc*i*
alias:          pci:v00008086d0000108Bsv*sd*bc*sc*i*
alias:          pci:v00008086d0000107Fsv*sd*bc*sc*i*
alias:          pci:v00008086d0000107Esv*sd*bc*sc*i*
alias:          pci:v00008086d0000107Dsv*sd*bc*sc*i*
alias:          pci:v00008086d000010B9sv*sd*bc*sc*i*
alias:          pci:v00008086d000010D5sv*sd*bc*sc*i*
alias:          pci:v00008086d000010DAsv*sd*bc*sc*i*
alias:          pci:v00008086d000010D9sv*sd*bc*sc*i*
alias:          pci:v00008086d00001060sv*sd*bc*sc*i*
alias:          pci:v00008086d000010A5sv*sd*bc*sc*i*
alias:          pci:v00008086d000010BCsv*sd*bc*sc*i*
alias:          pci:v00008086d000010A4sv*sd*bc*sc*i*
alias:          pci:v00008086d0000105Fsv*sd*bc*sc*i*
alias:          pci:v00008086d0000105Esv*sd*bc*sc*i*
depends:        
vermagic:       4.2.2 SMP mod_unload modversions
parm:           debug:Debug level (0=none,...,16=all) (int)
parm:           copybreak:Maximum size of packet that is copied to a new buffer on receive (uint)
parm:           TxIntDelay:Transmit Interrupt Delay (array of int)
parm:           TxAbsIntDelay:Transmit Absolute Interrupt Delay (array of int)
parm:           RxIntDelay:Receive Interrupt Delay (array of int)
parm:           RxAbsIntDelay:Receive Absolute Interrupt Delay (array of int)
parm:           InterruptThrottleRate:Interrupt Throttling Rate (array of int)
parm:           IntMode:Interrupt Mode (array of int)
parm:           SmartPowerDownEnable:Enable PHY smart power down (array of int)
parm:           KumeranLockLoss:Enable Kumeran lock loss workaround (array of int)
parm:           WriteProtectNVM:Write-protect NVM [WARNING: disabling this can lead to corrupted NVM] (array of int)
parm:           CrcStripping:Enable CRC Stripping, disable if your BMC needs the CRC (array of int)
```

### 3.4.5 交叉编译ARM

交叉编译内核需要安装交叉编译器，参见[Cross compiling Linux kernel on x86_64](/docs/Cross_Compile_Linux.pdf)。

根据顶层Makefile中的如下定义可知，Makefile的Default Target节至编译external modules节的编译与当前环境的体系架构有关：

```
# SUBARCH tells the usermode build what the underlying arch is.  That is set
# first, and if a usermode build is happening, the "ARCH=um" on the command
# line overrides the setting of ARCH below.  If a native build is happening,
# then ARCH is assigned, getting whatever value it gets normally, and
# SUBARCH is subsequently ignored.
SUBARCH := $(shell uname -m | sed -e s/i.86/i386/ -e s/sun4u/sparc64/				\
						  -e s/arm.*/arm/ -e s/sa110/arm/		\
						  -e s/s390x/s390/ -e s/parisc64/parisc/		\
						  -e s/ppc.*/powerpc/ -e s/mips.*/mips/		\
						  -e s/sh[234].*/sh/ )

# Cross compiling and selecting different set of gcc/bin-utils
# ---------------------------------------------------------------------------
#
# When performing cross compilation for other architectures ARCH shall be set
# to the target architecture. (See arch/* for the possibilities).
# ARCH can be set during invocation of make:
# make ARCH=ia64
# Another way is to have ARCH set in the environment.
# The default ARCH is the host where make is executed.

# CROSS_COMPILE specify the prefix used for all executables used
# during compilation. Only gcc and related bin-utils executables
# are prefixed with $(CROSS_COMPILE).
# CROSS_COMPILE can be set on the command line
# make CROSS_COMPILE=ia64-linux-
# Alternatively CROSS_COMPILE can be set in the environment.
# A third alternative is to store a setting in .config so that plain
# "make" in the configured kernel build directory always uses that.
# Default value for CROSS_COMPILE is not to prefix executables
# Note: Some architectures assign CROSS_COMPILE in their arch/*/Makefile
export KBUILD_BUILDHOST := $(SUBARCH)
ARCH			?= $(SUBARCH)
CROSS_COMPILE	?= $(CONFIG_CROSS_COMPILE:"%"=%)

# Architecture as present in compile.h
UTS_MACHINE 	:= $(ARCH)
SRCARCH 		:= $(ARCH)

...
```

如果为其他体系架构编译内核，则需要进行交叉编译。下面以ARM为例，讲解Linux Kernel的交叉编译。

#### 3.4.5.1 安装交叉编译器

以ARM为例，运行下列命令安装交叉编译器:

```
chenwx@chenwx ~/linux $ sudo apt-get install gcc-arm-linux-gnueabi
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following extra packages will be installed:
  binutils-arm-linux-gnueabi cpp-4.7-arm-linux-gnueabi cpp-arm-linux-gnueabi gcc-4.7-arm-linux-gnueabi gcc-4.7-arm-linux-gnueabi-base libc6-armel-cross
  libc6-dev-armel-cross libgcc1-armel-cross libgomp1-armel-cross linux-libc-dev-armel-cross
Suggested packages:
  binutils-doc gcc-4.7-locales cpp-doc gcc-4.7-multilib-arm-linux-gnueabi libmudflap0-4.7-dev-armel-cross gcc-4.7-doc libgcc1-dbg-armel-cross
  libgomp1-dbg-armel-cross libitm1-dbg-armel-cross libquadmath-dbg-armel-cross libmudflap0-dbg-armel-cross binutils-gold automake1.9 flex bison
  gdb-arm-linux-gnueabi gcc-doc
The following NEW packages will be installed:
  binutils-arm-linux-gnueabi cpp-4.7-arm-linux-gnueabi cpp-arm-linux-gnueabi gcc-4.7-arm-linux-gnueabi gcc-4.7-arm-linux-gnueabi-base gcc-arm-linux-gnueabi
  libc6-armel-cross libc6-dev-armel-cross libgcc1-armel-cross libgomp1-armel-cross linux-libc-dev-armel-cross
0 upgraded, 11 newly installed, 0 to remove and 417 not upgraded.
Need to get 20.6 MB of archives.
After this operation, 41.0 MB of additional disk space will be used.
...

chenwx@chenwx ~/linux $ ll /usr/bin | grep arm
-rwxr-xr-x  1 root   root        9648 Jul  9  2012 arm2hpdl
-rwxr-xr-x  1 root   root       26524 Sep 21  2012 arm-linux-gnueabi-addr2line
-rwxr-xr-x  2 root   root       55228 Sep 21  2012 arm-linux-gnueabi-ar
-rwxr-xr-x  2 root   root      569784 Sep 21  2012 arm-linux-gnueabi-as
-rwxr-xr-x  1 root   root       22164 Sep 21  2012 arm-linux-gnueabi-c++filt
lrwxrwxrwx  1 root   root          25 Oct  6  2012 arm-linux-gnueabi-cpp -> arm-linux-gnueabi-cpp-4.7
-rwxr-xr-x  1 root   root      515328 Sep 21  2012 arm-linux-gnueabi-cpp-4.7
-rwxr-xr-x  1 root   root       26384 Sep 21  2012 arm-linux-gnueabi-elfedit
lrwxrwxrwx  1 root   root          25 Oct  6  2012 arm-linux-gnueabi-gcc -> arm-linux-gnueabi-gcc-4.7
-rwxr-xr-x  1 root   root      515328 Sep 21  2012 arm-linux-gnueabi-gcc-4.7
-rwxr-xr-x  1 root   root       22088 Sep 21  2012 arm-linux-gnueabi-gcc-ar-4.7
-rwxr-xr-x  1 root   root       22088 Sep 21  2012 arm-linux-gnueabi-gcc-nm-4.7
-rwxr-xr-x  1 root   root       22092 Sep 21  2012 arm-linux-gnueabi-gcc-ranlib-4.7
lrwxrwxrwx  1 root   root          26 Oct  6  2012 arm-linux-gnueabi-gcov -> arm-linux-gnueabi-gcov-4.7
-rwxr-xr-x  1 root   root      210704 Sep 21  2012 arm-linux-gnueabi-gcov-4.7
-rwxr-xr-x  1 root   root       92728 Sep 21  2012 arm-linux-gnueabi-gprof
-rwxr-xr-x  4 root   root      494592 Sep 21  2012 arm-linux-gnueabi-ld
-rwxr-xr-x  4 root   root      494592 Sep 21  2012 arm-linux-gnueabi-ld.bfd
-rwxr-xr-x  2 root   root     2886436 Sep 21  2012 arm-linux-gnueabi-ld.gold
-rwxr-xr-x  2 root   root       35092 Sep 21  2012 arm-linux-gnueabi-nm
-rwxr-xr-x  2 root   root      204668 Sep 21  2012 arm-linux-gnueabi-objcopy
-rwxr-xr-x  2 root   root      307456 Sep 21  2012 arm-linux-gnueabi-objdump
-rwxr-xr-x  2 root   root       55240 Sep 21  2012 arm-linux-gnueabi-ranlib
-rwxr-xr-x  1 root   root      369540 Sep 21  2012 arm-linux-gnueabi-readelf
-rwxr-xr-x  1 root   root       26488 Sep 21  2012 arm-linux-gnueabi-size
-rwxr-xr-x  1 root   root       26476 Sep 21  2012 arm-linux-gnueabi-strings
-rwxr-xr-x  2 root   root      204668 Sep 21  2012 arm-linux-gnueabi-strip
lrwxrwxrwx  1 root   root           9 Jan 22  2013 charmap -> gucharmap
lrwxrwxrwx  1 root   root           9 Jan 22  2013 gnome-character-map -> gucharmap
-rwxr-xr-x  1 root   root       68276 Sep 28  2012 gucharmap
lrwxrwxrwx  1 root   root          26 Jan 22  2013 testparm -> /etc/alternatives/testparm
-rwxr-xr-x  1 root   root     1427132 Oct  5  2012 testparm.samba3

chenwx@chenwx ~/linux $ arm-linux-gnueabi-gcc --version
arm-linux-gnueabi-gcc (Ubuntu/Linaro 4.7.2-1ubuntu1) 4.7.2
Copyright (C) 2012 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

#### 3.4.5.2 配置内核ARM

可采用如下两种方式之一配置内核：

**1) 运行下列命令配置内核，配置结果保存在~/linux-build/.config中**

```
# make O=../linux-build/ ARCH=arm CROSS_COMPILE=arm-linux-gnueabi- menuconfig
```

**2) 运行下列命令使用arch/arm/configs/目录中的默认配置文件，以acs5k_defconfig为例(参见[3.3.2 make *config](#3-3-2-make-config)节)**

```
# make O=../linux-build/ ARCH=arm CROSS_COMPILE=arm-linux-gnueabi- acs5k_defconfig
```

```
chenwx@chenwx ~/linux $ ll arch/arm/configs/
-rw-r--r-- 1 chenwx chenwx  1998 Jul  8 20:53 acs5k_defconfig
-rw-r--r-- 1 chenwx chenwx  2011 Jul  8 20:53 acs5k_tiny_defconfig
-rw-r--r-- 1 chenwx chenwx  2617 Jul  8 20:53 am200epdkit_defconfig
-rw-r--r-- 1 chenwx chenwx  2289 Jul  8 20:53 ape6evm_defconfig
-rw-r--r-- 1 chenwx chenwx  4068 Jul  8 20:53 armadillo800eva_defconfig
-rw-r--r-- 1 chenwx chenwx  1315 Jul  8 20:53 assabet_defconfig
-rw-r--r-- 1 chenwx chenwx  5249 Jul  8 20:53 at91_dt_defconfig
...

chenwx@chenwx ~/linux $ make O=../linux-build/ ARCH=arm CROSS_COMPILE=arm-linux-gnueabi- help
...
Architecture specific targets (arm):
* zImage        - Compressed kernel image (arch/arm/boot/zImage)
  Image         - Uncompressed kernel image (arch/arm/boot/Image)
* xipImage      - XIP kernel image, if configured (arch/arm/boot/xipImage)
  uImage        - U-Boot wrapped zImage
  bootpImage    - Combined zImage and initial RAM disk
                  (supply initrd image via make variable INITRD=<path>)
* dtbs          - Build device tree blobs for enabled boards
  dtbs_install  - Install dtbs to /boot/dtbs/3.15.0
  install       - Install uncompressed kernel
  zinstall      - Install compressed kernel
  uinstall      - Install U-Boot wrapped compressed kernel
                  Install using (your) ~/bin/installkernel or
                  (distribution) /sbin/installkernel or
                  install to $(INSTALL_PATH) and run lilo

  acs5k_defconfig            - Build for acs5k
  acs5k_tiny_defconfig       - Build for acs5k_tiny
  am200epdkit_defconfig      - Build for am200epdkit
  ape6evm_defconfig          - Build for ape6evm
  armadillo800eva_defconfig  - Build for armadillo800eva
  assabet_defconfig          - Build for assabet
  at91_dt_defconfig          - Build for at91_dt
  at91rm9200_defconfig       - Build for at91rm9200
  at91sam9260_9g20_defconfig - Build for at91sam9260_9g20
  at91sam9261_9g10_defconfig - Build for at91sam9261_9g10
  at91sam9263_defconfig      - Build for at91sam9263
  at91sam9g45_defconfig      - Build for at91sam9g45
  at91sam9rl_defconfig       - Build for at91sam9rl
...

chenwx@chenwx ~/linux $ make O=../linux-build/ ARCH=arm CROSS_COMPILE=arm-linux-gnueabi- acs5k_defconfig
#
# configuration written to .config
#
```

#### 3.4.5.3 内核的交叉编译

运行下列命令为ARM架构交叉编译内核：

```
chenwx@chenwx ～/linux $ make O=../linux-build/ ARCH=arm CROSS_COMPILE=arm-linux-gnueabi-
...
  LD      vmlinux
  SORTEX  vmlinux
  SYSMAP  System.map
  OBJCOPY arch/arm/boot/Image
  Kernel: arch/arm/boot/Image is ready
  AS      arch/arm/boot/compressed/head.o
  GZIP    arch/arm/boot/compressed/piggy.gzip
  AS      arch/arm/boot/compressed/piggy.gzip.o
  CC      arch/arm/boot/compressed/misc.o
  CC      arch/arm/boot/compressed/decompress.o
  CC      arch/arm/boot/compressed/string.o
  SHIPPED arch/arm/boot/compressed/hyp-stub.S
  AS      arch/arm/boot/compressed/hyp-stub.o
  SHIPPED arch/arm/boot/compressed/lib1funcs.S
  AS      arch/arm/boot/compressed/lib1funcs.o
  SHIPPED arch/arm/boot/compressed/ashldi3.S
  AS      arch/arm/boot/compressed/ashldi3.o
  LD      arch/arm/boot/compressed/vmlinux
  OBJCOPY arch/arm/boot/zImage
  Kernel: arch/arm/boot/zImage is ready
  MODPOST 42 modules
  CC      arch/arm/crypto/aes-arm.mod.o
  LD [M]  arch/arm/crypto/aes-arm.ko
  CC      arch/arm/crypto/sha1-arm.mod.o
  LD [M]  arch/arm/crypto/sha1-arm.ko
  CC      crypto/ansi_cprng.mod.o
  LD [M]  crypto/ansi_cprng.ko
...

chenwx@chenwx ～/linux-build $ ll vmlinux System.map arch/arm/boot/compressed/vmlinux arch/arm/boot/zImage
-rwxr-xr-x 1 chenwx chenwx  985956 Dec  9 11:56 arch/arm/boot/compressed/vmlinux
-rwxr-xr-x 1 chenwx chenwx  947208 Dec  9 11:56 arch/arm/boot/zImage
-rw-r--r-- 1 chenwx chenwx  316549 Dec  9 11:56 System.map
-rwxr-xr-x 1 chenwx chenwx 2435755 Dec  9 11:56 vmlinux

chenwx@chenwx ～/linux-build $ file vmlinux
vmlinux: ELF 32-bit LSB executable, ARM, version 1, statically linked, BuildID[sha1]=0xf2e0153fb842be3137df94af05c48f27dfd510b9, not stripped

chenwx@chenwx ～/linux-build $ file arch/arm/boot/compressed/vmlinux
arch/arm/boot/compressed/vmlinux: ELF 32-bit LSB executable, ARM, version 1, statically linked, not stripped

chenwx@chenwx ～/linux-build $ file arch/arm/boot/zImage
arch/arm/boot/zImage: Linux kernel ARM boot executable zImage (little-endian)
```

#### 3.4.5.4 安装编译的内核模块

运行下列命令安装编译的内核模块：

```
# make O=../linux-build/ ARCH=arm CROSS_COMPILE=arm-linux-gnueabi- INSTALL_MOD_PATH=/path/install/modules/ modules_install
```

```
chenwx@chenwx ～/linux $ make O=../linux-build/ ARCH=arm CROSS_COMPILE=arm-linux-gnueabi- INSTALL_MOD_PATH=~/arm_mod modules_install
  INSTALL arch/arm/crypto/aes-arm.ko
  INSTALL arch/arm/crypto/sha1-arm.ko
  INSTALL crypto/ansi_cprng.ko
  INSTALL crypto/anubis.ko
  INSTALL crypto/arc4.ko
  INSTALL crypto/blowfish_common.ko
  INSTALL crypto/blowfish_generic.ko
  INSTALL crypto/camellia_generic.ko
  INSTALL crypto/cast5_generic.ko
  INSTALL crypto/cast6_generic.ko
  INSTALL crypto/cast_common.ko
  INSTALL crypto/ccm.ko
  INSTALL crypto/cmac.ko
  INSTALL crypto/crc32.ko
  INSTALL crypto/crc32c.ko
  INSTALL crypto/crct10dif_common.ko
  INSTALL crypto/crct10dif_generic.ko
  INSTALL crypto/ctr.ko
  INSTALL crypto/cts.ko
  INSTALL crypto/des_generic.ko
  INSTALL crypto/fcrypt.ko
  INSTALL crypto/gcm.ko
  INSTALL crypto/ghash-generic.ko
  INSTALL crypto/lrw.ko
  INSTALL crypto/md4.ko
  INSTALL crypto/michael_mic.ko
  INSTALL crypto/pcbc.ko
  INSTALL crypto/rmd128.ko
  INSTALL crypto/rmd160.ko
  INSTALL crypto/rmd256.ko
  INSTALL crypto/rmd320.ko
  INSTALL crypto/seqiv.ko
  INSTALL crypto/sha512_generic.ko
  INSTALL crypto/tcrypt.ko
  INSTALL crypto/tgr192.ko
  INSTALL crypto/vmac.ko
  INSTALL crypto/wp512.ko
  INSTALL crypto/xcbc.ko
  INSTALL crypto/xts.ko
  INSTALL fs/ext3/ext3.ko
  INSTALL fs/jbd/jbd.ko
  INSTALL fs/mbcache.ko
  DEPMOD  3.13.0-rc1-00001-g83836a9

chenwx@chenwx ～/linux $ ll ~/arm_mod/
total 12
drwxr-xr-x  3 chenwx chenwx 4096 Dec 10 03:52 .
drwxr-xr-x 36 chenwx chenwx 4096 Dec  9 12:30 ..
drwxr-xr-x  3 chenwx chenwx 4096 Dec 10 03:52 lib

chenwx@chenwx ～/linux $ ll ~/arm_mod/lib/
total 12
drwxr-xr-x 3 chenwx chenwx 4096 Dec 10 03:52 .
drwxr-xr-x 3 chenwx chenwx 4096 Dec 10 03:52 ..
drwxr-xr-x 3 chenwx chenwx 4096 Dec 10 03:52 modules

chenwx@chenwx ～/linux $ ll ~/arm_mod/lib/modules/
total 12
drwxr-xr-x 3 chenwx chenwx 4096 Dec 10 03:52 .
drwxr-xr-x 3 chenwx chenwx 4096 Dec 10 03:52 ..
drwxr-xr-x 3 chenwx chenwx 4096 Dec 10 03:53 3.13.0-rc1-00001-g83836a9

chenwx@chenwx ～/linux $ ll ~/arm_mod/lib/modules/3.13.0-rc1-00001-g83836a9/
total 88
drwxr-xr-x 3 chenwx chenwx 4096 Dec 10 03:53 .
drwxr-xr-x 3 chenwx chenwx 4096 Dec 10 03:52 ..
lrwxrwxrwx 1 chenwx chenwx   33 Dec 10 03:52 build -> /usr/src/linuxkernel/linux-stable
drwxr-xr-x 5 chenwx chenwx 4096 Dec 10 03:53 kernel
-rw-r--r-- 1 chenwx chenwx  615 Dec 10 03:53 modules.alias
-rw-r--r-- 1 chenwx chenwx  946 Dec 10 03:53 modules.alias.bin
-rw-r--r-- 1 chenwx chenwx 1929 Dec 10 03:52 modules.builtin
-rw-r--r-- 1 chenwx chenwx 2526 Dec 10 03:53 modules.builtin.bin
-rw-r--r-- 1 chenwx chenwx   69 Dec 10 03:53 modules.ccwmap
-rw-r--r-- 1 chenwx chenwx 1295 Dec 10 03:53 modules.dep
-rw-r--r-- 1 chenwx chenwx 2892 Dec 10 03:53 modules.dep.bin
-rw-r--r-- 1 chenwx chenwx   52 Dec 10 03:53 modules.devname
-rw-r--r-- 1 chenwx chenwx   73 Dec 10 03:53 modules.ieee1394map
-rw-r--r-- 1 chenwx chenwx  141 Dec 10 03:53 modules.inputmap
-rw-r--r-- 1 chenwx chenwx   81 Dec 10 03:53 modules.isapnpmap
-rw-r--r-- 1 chenwx chenwx   74 Dec 10 03:53 modules.ofmap
-rw-r--r-- 1 chenwx chenwx 1086 Dec 10 03:52 modules.order
-rw-r--r-- 1 chenwx chenwx   99 Dec 10 03:53 modules.pcimap
-rw-r--r-- 1 chenwx chenwx   43 Dec 10 03:53 modules.seriomap
-rw-r--r-- 1 chenwx chenwx  131 Dec 10 03:53 modules.softdep
-rw-r--r-- 1 chenwx chenwx 2755 Dec 10 03:53 modules.symbols
-rw-r--r-- 1 chenwx chenwx 3571 Dec 10 03:53 modules.symbols.bin
-rw-r--r-- 1 chenwx chenwx  189 Dec 10 03:53 modules.usbmap
lrwxrwxrwx 1 chenwx chenwx   33 Dec 10 03:52 source -> /usr/src/linuxkernel/linux-stable

chenwx@chenwx ～/linux $ ll ~/arm_mod/lib/modules/3.13.0-rc1-00001-g83836a9/kernel/
total 20
drwxr-xr-x 5 chenwx chenwx 4096 Dec 10 03:53 .
drwxr-xr-x 3 chenwx chenwx 4096 Dec 10 03:53 ..
drwxr-xr-x 3 chenwx chenwx 4096 Dec 10 03:52 arch
drwxr-xr-x 2 chenwx chenwx 4096 Dec 10 03:53 crypto
drwxr-xr-x 4 chenwx chenwx 4096 Dec 10 03:53 fs
```

### 3.4.6 Export Header Files

Refer to following documentations:

* http://crashcourse.ca/introduction-linux-kernel-programming/intermission-lets-talk-about-header-files-free-lesson
* [Kernel Headers](/docs/Kernel_Headers.pdf)
* [Header Files](/docs/Header_files.pdf)

If you want to do kernel programming, there is a package corresponding to each running kernel that you can install that provides the kernel space header files against which you can compile your loadable modules so that you don't even need a full kernel source tree.

There are times when you're programming for user space but you need header files that define kernel space structures since you're going to be defining a structure that you want to pass into kernel space, almost certainly via a system call, and you need to get a declaration for that structure somewhere, which leads us to introduce a third type of header file -- the kind that are relevant for both kernel and user space.

Such header files are carefully selected from the header files in the kernel source tree, they're "cleaned" (using a process that will be explained shortly), and they're bundled into yet another package that you'll see in a minute. So ... where do these header files come from? At the top of your kernel source tree, simply run:

```
chenwx@chenwx ~/linux $ make distclean       [optional]
chenwx@chenwx ~/linux $ make headers_install
```

at which point a carefully selected subset of the kernel header files scattered around the tree are collected, sanitized and placed carefully under the kernel source tree directory usr/include/, where you can examine them with:

```
chenwx@chenwx ~/linux $ find usr/include/ | more
usr/include/
usr/include/asm
usr/include/asm/ptrace-abi.h
usr/include/asm/types.h
usr/include/asm/auxvec.h
usr/include/asm/siginfo.h
usr/include/asm/bootparam.h
usr/include/asm/unistd_64.h
usr/include/asm/mman.h
usr/include/asm/hyperv.h
usr/include/asm/perf_regs.h
usr/include/asm/svm.h
usr/include/asm/shmbuf.h
usr/include/asm/fcntl.h
usr/include/asm/unistd.h
usr/include/asm/swab.h
usr/include/asm/stat.h
...
```

What you're looking at in the output above is the collection of kernel header files that are also deemed to be appropriate for user space programmers who want to, perhaps, define structures that they will be passing to kernel code. More to the point, these header files have already been packaged for you and are almost certainly already on your system. In the case of Ubuntu 10.04, this would be the linux-libc-dev package:

```
chenwx@chenwx ~/linux $ dpkg -L linux-libc-dev | more
/.
/usr
/usr/include
/usr/include/asm
/usr/include/asm/ptrace-abi.h
/usr/include/asm/types.h
/usr/include/asm/auxvec.h
/usr/include/asm/siginfo.h
/usr/include/asm/bootparam.h
/usr/include/asm/unistd_64.h
/usr/include/asm/mman.h
/usr/include/asm/hyperv.h
/usr/include/asm/perf_regs.h
/usr/include/asm/svm.h
/usr/include/asm/shmbuf.h
/usr/include/asm/fcntl.h
/usr/include/asm/unistd.h
/usr/include/asm/swab.h
...
```

#### 3.4.6.1 Who decides which kernel header files are exported?

When you run "make headers_install" from the top of your kernel source tree, who or what decides precisely which kernel header files will get bundled up and stashed under the kernel source directory usr/include/ for later "exporting" to user space? That's easy.

The header files to be exported are defined by the Kbuild files scattered throughout the kernel source tree. The one at the very top level is the engine, while elsewhere throughout the tree, you'll find Kbuild files like, say, this one:

```
chenwx@chenwx ~/linux $ cat include/uapi/Kbuild
# UAPI Header export list
# Top-level Makefile calls into asm-$(ARCH)
# List only non-arch directories below

header-y += asm-generic/
header-y += linux/
header-y += sound/
header-y += mtd/
header-y += rdma/
header-y += video/
header-y += drm/
header-y += xen/
header-y += scsi/
header-y += misc/
```

That file simply defines that the export process should recursively continue into those subdirectories and keep checking for more Kbuild files. If we check further, we'll start to see Kbuild files like:

```
chenwx@chenwx ~/linux $ cat include/uapi/linux/Kbuild
# UAPI Header export list
header-y += android/
header-y += byteorder/
header-y += can/
header-y += caif/
header-y += dvb/
header-y += hdlc/
header-y += hsi/
header-y += iio/
header-y += isdn/
...
header-y += acct.h
header-y += adb.h
header-y += adfs_fs.h
header-y += affs_hardblocks.h
header-y += agpgart.h
header-y += aio_abi.h
header-y += am437x-vpfe.h
header-y += apm_bios.h
header-y += arcfb.h
header-y += atalk.h
header-y += atmapi.h
...
```

which clearly represents a combination of more recursive directories, plus immediate header files. Quite simply, all kernel Kbuild files have that general structure and, collectively (throughout the entire kernel source tree), they define all of the kernel header files to be exported to user space.

#### 3.4.6.2 What does it mean to "sanitize" one of those header files?

In many cases, the header files to be exported contain some content that is meaningful only in kernel space, and it's only a subset of the header file that needs to be exported. Kernel-only code is normally surrounded by a preprocessor conditional that checks the value of the ```__KERNEL__``` macro, and part of the the job of the export process (when you run make headers_install) is to examine each file that is being exported, identify the code that is relevant only in kernel space, and remove it. Quite simple, really.

That's why (for example) the kernel version of the header file include/video/edid.h looks like this:

```
#ifndef __linux_video_edid_h__
#define __linux_video_edid_h__

#if !defined(__KERNEL__) || defined(CONFIG_X86)

struct edid_info {
        unsigned char dummy[128];
};

#ifdef __KERNEL__
extern struct edid_info edid_info;
#endif /* __KERNEL__ */

#endif

#endif /* __linux_video_edid_h__ */
```

but by the time it ends up in user space and is placed at /usr/include/video/edid.h, it looks like this:

```
#ifndef __linux_video_edid_h__
#define __linux_video_edid_h__

struct edid_info {
	unsigned char dummy[128];
};

#endif /* __linux_video_edid_h__ */
```

Technically, there's no actual harm in leaving in that kernel-only content since, when you're compiling in user space, you're guaranteed that the preprocessor macro ```__KERNEL__``` will never be set, but it's cleaner to just strip out that irrelevant content during the export process.

NOTE: If you look carefully, you'll notice that many of the Kbuild files contain both the variables header-y and unifdef-y to identify the header files to be sanitized and exported. The latter is now deprecated and Kbuild files should now contain only the first form, but the older form is still supported.

#### 3.4.6.3 Installation of Linux API Headers in LFS

参见[Linux-4.18.5 API Headers (online)](http://www.linuxfromscratch.org/lfs/view/stable-systemd/chapter06/linux-headers.html) and [Linux-4.18.5 API Headers (local pdf)](/docs/Linux-4.18.5_API_Headers.pdf)。

The following steps show the installation of Linux API headers in Linux From Scratch (LFS):

```
chenwx@chenwx ~/linux $ mkdir ../linux-header
chenwx@chenwx ~/linux $ make INSTALL_HDR_PATH=../linux-header/ headers_install
  CHK     include/generated/uapi/linux/version.h
  INSTALL include/asm-generic (35 files)
  INSTALL include/drm (21 files)
  INSTALL include/linux/android (1 file)
  INSTALL include/linux/byteorder (2 files)
  INSTALL include/linux/caif (2 files)
  INSTALL include/linux/can (5 files)
  INSTALL include/linux/dvb (8 files)
  INSTALL include/linux/hdlc (1 file)
  INSTALL include/linux/hsi (2 files)
  INSTALL include/linux/iio (2 files)
  INSTALL include/linux/isdn (1 file)
  INSTALL include/linux/mmc (1 file)
  INSTALL include/linux/netfilter/ipset (4 files)
  INSTALL include/linux/netfilter (86 files)
  INSTALL include/linux/netfilter_arp (2 files)
  INSTALL include/linux/netfilter_bridge (17 files)
  INSTALL include/linux/netfilter_ipv4 (9 files)
  INSTALL include/linux/netfilter_ipv6 (12 files)
  INSTALL include/linux/nfsd (5 files)
  INSTALL include/linux/raid (2 files)
  INSTALL include/linux/spi (1 file)
  INSTALL include/linux/sunrpc (1 file)
  INSTALL include/linux/tc_act (12 files)
  INSTALL include/linux/tc_ematch (4 files)
  INSTALL include/linux/usb (11 files)
  INSTALL include/linux/wimax (1 file)
  INSTALL include/linux (436 files)
  INSTALL include/misc (1 file)
  INSTALL include/mtd (5 files)
  INSTALL include/rdma/hfi (1 file)
  INSTALL include/rdma (14 files)
  INSTALL include/scsi/fc (4 files)
  INSTALL include/scsi (4 files)
  INSTALL include/sound (15 files)
  INSTALL include/video (3 files)
  INSTALL include/xen (4 files)
  INSTALL include/uapi (0 file)
  INSTALL include/asm (65 files)

// Remove .install and ..install.cmd files
chenwx@chenwx ~/linux $ find ../linux-header/include \( -name .install -o -name ..install.cmd \) -delete

// Install the linux headers to /usr/include directory
chenwx@chenwx ~/linux $ cp -rv ../linux-header/include/* /usr/include

// Check the generated linux headers
chenwx@chenwx ~/linux $ ll ../linux-header/
drwxrwxr-x 14 chenwx chenwx 4.0K Oct 23 17:23 include
chenwx@chenwx ~/linux $ ll ../linux-header/include/
drwxrwxr-x  2 chenwx chenwx 4.0K Oct 23 17:24 asm
drwxrwxr-x  2 chenwx chenwx 4.0K Oct 23 17:24 asm-generic
drwxrwxr-x  2 chenwx chenwx 4.0K Oct 23 17:24 drm
drwxrwxr-x 25 chenwx chenwx  20K Oct 23 17:24 linux
drwxrwxr-x  2 chenwx chenwx 4.0K Oct 23 17:24 misc
drwxrwxr-x  2 chenwx chenwx 4.0K Oct 23 17:24 mtd
drwxrwxr-x  3 chenwx chenwx 4.0K Oct 23 17:24 rdma
drwxrwxr-x  3 chenwx chenwx 4.0K Oct 23 17:24 scsi
drwxrwxr-x  2 chenwx chenwx 4.0K Oct 23 17:24 sound
drwxrwxr-x  2 chenwx chenwx 4.0K Oct 23 17:24 uapi
drwxrwxr-x  2 chenwx chenwx 4.0K Oct 23 17:24 video
drwxrwxr-x  2 chenwx chenwx 4.0K Oct 23 17:24 xen
chenwx@chenwx ~/linux $ find ../linux-header/include/ -type f | wc -l
797
```

## 3.5 内核升级

### 3.5.1 内核升级准备

#### 3.5.1.1 查看当前系统内核版本

It is easy to tell if you are running a distribution kernel. Unless you downloaded, compiled and installed your own version of kernel from [kernel.org](https://www.kernel.org/), you are running a distribution kernel. To find out the version of your kernel, run ```uname -r```:

```
chenwx ～ $ uname -r
3.5.0-17-generic
```

[**NOTE**] If you see anything at all after the dash, you are running a distribution kernel. Please use the support channels offered by your distribution vendor to obtain kernel support.

也可通过下列命令查看内核版本:

```
chenwx ～ $ cat /proc/version
Linux version 3.15.0-eudyptula-00054-g783e9e8-dirty (chenwx@chenwx) (gcc version 4.8.1 (Ubuntu/Linaro 4.8.1-10ubuntu8) ) #3 SMP Fri May 9 07:56:01 CST 2014
```

### 3.5.2 获取新版本内核源代码

#### 3.5.2.1 通过Git Repository下载源代码

1) Download source code from linux.git to directory ~/linux

```
$ cd ~
$ git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
```

2) Checkout source code of specific git tree

```
$ git branch -a
$ git checkout master
$ git tag -l next-*
$ git checkout next-20150224
```

参见[1.2.5 Setup Linux Kernel Workarea](#1-2-5-setup-linux-kernel-workarea)节。

#### 3.5.2.2 通过源代码压缩包和补丁下载源代码

1) Download source code from [http://www.kernel.org/pub/linux/kernel](http://www.kernel.org/pub/linux/kernel):

```
linux-3.2.tar.bz2        05-Jan-2012 00:40   75M  
linux-3.2.tar.gz         05-Jan-2012 00:40   94M  
linux-3.2.tar.sign       05-Jan-2012 00:40  490
linux-3.2.tar.xz         05-Jan-2012 00:40   62M
```

2) Unzip source code to directory ~/linux:

```
$ cd ~
$ rm -rf linux-3.2				// 删除源代码目录
$ rm -rf linux					// 删除链接目录

$ gzip -cd linux-3.2.tar.gz | tar xvf -		// 生成linux-3.2目录
or,
$ bzip2 -dc linux-3.2.tar.bz2 | tar xvf –	// 生成linux-3.2目录

$ ln -s linux-3.2 linux				// 重新生成linux链接目录
```

Refer to linux/README:

> Do NOT use the /usr/src/linux area! This area has a (usually incomplete) set of kernel headers that are used by the library header files. They should match the library, and not get messed up by whatever the kernel-du-jour happens to be.

3) Apply patches

参见[内核补丁/Patch](#)节。

### 3.5.3 配置内核

执行如下命令配置内核：

```
$ cd ~/linux

// 该命令可确保源代码目录下没有不正确的.o文件
$ make mrproper
$ make clean
$ make distclean

// 参见make config节和make *config节，产生配置输出文件~/linux-build/.config
$ make config O=../linux-build
$ make *config O=../linux-build
or,
$ cp /boot/config-3.15.9-generic ../linux-build/.config
$ make olddefconfig O=../linux-build
$ make menuconfig O=../linux-build

$ make kernelrelease O=../linux-build
3.2.0-chenwx
```

[**NOTE**] It's more convenient to preserve the kernel source untouched and have all the configuration output and compilation results generated in a remote directory.

1) it leaves the source unpolluted by all of those output files, which makes it easier if you want to search the tree using something like grep.

2) it allows you to work with a directory of kernel source for which you have no write access. Perhaps it's a system directory, or in some other user's home directory. As long as you can cd to the top of the source tree and have read access to all of the source, you can generate all of the output elsewhere.

3) it lets you work with multiple configurations and builds simultaneously, since you can simply switch from one output directory to another on the fly, using the same kernel source directory as the basis for all of those builds.

There is only one caution, though. Once you initially select an output directory, you must specify that output directory on every subsequent make invocation, but that should simply be obvious. In fact, the last time I checked, you can't use the remote directory feature if your kernel source tree already shows signs of internal configuration. In short, this feature is meant to be used with a pristine kernel source tree.

在本文中，内核源代码位于```~/linux```目录下，而编译的输出目录位于```～/linux-build```目录下。

### 3.5.4 编译内核

执行如下命令编译内核：

```
# cd ~/linux
# make menuconfig O=../linux-build

// 建立编译时所需的从属文件。
// 注：在linux-3.2中，已经不需要执行该命令了，执行make dep的输出为：
// *** Warning: make dep is unnecessary now.
# make dep

# make O=../linux-build
# make O=../linux-build –j4
```

编译内核，具体过程参见[3.4.1 Makefile的Default Target](#3-4-1-makefile-default-target)节：

* linux-2.6之前版本使用make bzImage命令；
* linux-2.6之后版本可仅使用make命令，相当于之前的make bzImage和make modules命令。

本命令的产生如下输出文件：

```
~/linux-build/vmlinux
~/linux-build/System.map
~/linux-build/arch/x86/boot/bzImage
~/linux-build/arch/i386/boot/bzImage (linked to ~/linux-build/arch/x86/boot/bzImage)
~/linux-build/oneSubDir/twoSubDir/*.ko (modules)
```

### 3.5.5 安装内核

执行如下命令安装内核模块：

```
# sudo make modules_install O=../linux-build
```

可加载模块被安装到/lib/modules/3.2.0/目录下：

```
/lib/modules/3.2.0/source		==链接==>	~/linux-build
/lib/modules/3.2.0/build		==链接==>	~/linux-build
~/linux-build/modules.order		==安装==>	/lib/modules/3.2.0/modules.order
~/linux-build/modules.builtin		==安装==>	/lib/modules/3.2.0/modules.builtin
$(modules)节的输出文件(*.ko)		==安装==>	/lib/modules/3.2.0/kernel/目录
$(mod-fw)节的输出文件(*.fw/*.bin/*.dsp)	==安装==>	/lib/firmware/目录
```

执行如下命令安装新内核：

```
# sudo make install O=../linux-build
```

规则install参见arch/x86/Makefile，其实际执行下列命令：

```
make -f scripts/Makefile.build obj=arch/x86/boot install
sh /home/linux-3.2/arch/x86/boot/install.sh 3.2.0 arch/x86/boot/bzImage System.map "/boot"
```

其中，/home/linux-3.2/arch/x86/boot/install.sh调用下列命令安装内核：

```
/sbin/installkernel 3.2.0 arch/x86/boot/bzImage System.map "/boot"
```

本命令进行如下操作：

```
~/linux-build/arch/x86/boot/bzImage (参见bzImage节)	==安装==>	/boot/vmlinuz-3.2.0-chenwx
~/linux-build/System.map (参见rule_vmlinux__节)		==安装==>	/boot/System.map-3.2.0-chenwx
~/linux-build/.config (参见.config/内核配置结果文件节)	==安装==>	/boot/config-3.2.0-chenwx
```

生成文件：

```
/boot/initrd.img-3.11.0-12-generic
```

#### 3.5.5.1 modules_install

运行```make modules_install```命令，执行顶层Makefile中的modules_install目标：

```
#
# INSTALL_PATH specifies where to place the updated kernel and system map
# images. Default is /boot, but you can set it to other values
export	INSTALL_PATH ?= /boot

#
# INSTALL_DTBS_PATH specifies a prefix for relocations required by build roots.
# Like INSTALL_MOD_PATH, it isn't defined in the Makefile, but can be passed as
# an argument if needed. Otherwise it defaults to the kernel install path
#
export INSTALL_DTBS_PATH ?= $(INSTALL_PATH)/dtbs/$(KERNELRELEASE)

#
# INSTALL_MOD_PATH specifies a prefix to MODLIB for module directory
# relocations required by build roots.  This is not defined in the
# makefile but the argument can be passed to make if needed.
#
MODLIB	= $(INSTALL_MOD_PATH)/lib/modules/$(KERNELRELEASE)
export MODLIB

ifdef CONFIG_MODULES

# Target to install modules
PHONY += modules_install
modules_install: _modinst_ _modinst_post

PHONY += _modinst_
_modinst_:
	@rm -rf $(MODLIB)/kernel
	@rm -f $(MODLIB)/source
	@mkdir -p $(MODLIB)/kernel
	// 创建链接文件/lib/modules/3.2.0/source	至~/linux-build
	@ln -s `cd $(srctree) && /bin/pwd` $(MODLIB)/source
	// 创建链接文件/lib/modules/3.2.0/build至~/linux-build
	@if [ ! $(objtree) -ef  $(MODLIB)/build ]; then \
		rm -f $(MODLIB)/build ; \
		ln -s $(CURDIR) $(MODLIB)/build ; \
	fi
	// 安装文件~/linux-build/modules.order至/lib/modules/3.2.0/modules.order
	@cp -f $(objtree)/modules.order $(MODLIB)/
	// 安装文件~/linux-build/modules.builtin至/lib/modules/3.2.0/modules.builtin
	@cp -f $(objtree)/modules.builtin $(MODLIB)/
	// 执行scripts/Makefile.modinst中的目标__modinst以安装编译好的modules
	$(Q)$(MAKE) -f $(srctree)/scripts/Makefile.modinst

# This depmod is only for convenience to give the initial
# boot a modules.dep even before / is mounted read-write.  However the
# boot script depmod is the master version.
PHONY += _modinst_post
_modinst_post: _modinst_
	// 执行scripts/Makefile.fwinst中的目标__fw_modinst
	$(Q)$(MAKE) -f $(srctree)/scripts/Makefile.fwinst obj=firmware __fw_modinst
	// 参见3.5.5.1.1 cmd_depmod节
	$(call cmd,depmod)

else # CONFIG_MODULES

# Modules not configured
# ---------------------------------------------------------------------------

modules modules_install: FORCE
	@echo >&2
	@echo >&2 "The present kernel configuration has modules disabled."
	@echo >&2 "Type 'make config' and enable loadable module support."
	@echo >&2 "Then build a kernel with module support enabled."
	@echo >&2
	@exit 1

endif # CONFIG_MODULES
```

##### 3.5.5.1.1 cmd_depmod

在顶层Makefile中，包含如下规则：

```
# SHELL used by kbuild
CONFIG_SHELL		:= $(shell if [ -x "$$BASH" ]; then echo $$BASH; \
			     else if [ -x /bin/bash ]; then echo /bin/bash; \
			     else echo sh; fi ; fi)

// 该命令来自module-init-tools或kmod，参见13.3.1 加载/卸载模块的命令节
DEPMOD			= /sbin/depmod

// 获取当前编译的内核版本号，例如: 4.2.0-alex
KERNELRELEASE	= $(shell cat include/config/kernel.release 2> /dev/null)

# Run depmod only if we have System.map and depmod is executable
quiet_cmd_depmod = DEPMOD  $(KERNELRELEASE)
      cmd_depmod = $(CONFIG_SHELL) $(srctree)/scripts/depmod.sh $(DEPMOD) \
                   $(KERNELRELEASE) "$(patsubst y,_,$(CONFIG_HAVE_UNDERSCORE_SYMBOL_PREFIX))"
```

命令cmd_depmod被扩展为:

```
/bin/bash /home/chenwx/linux/scripts/depmod.sh /sbin/depmod 4.2.0-alex
```

其中，命令/sbin/depmod需要首先存在下列目录和文件:

```
/lib/modules/4.2.0-alex/
/lib/modules/4.2.0-alex/modules.builtin
/lib/modules/4.2.0-alex/modules.order
```

然后，命令/sbin/depmod生成下列文件:

```
/lib/modules/4.2.0-alex/modules.alias
/lib/modules/4.2.0-alex/modules.alias.bin
/lib/modules/4.2.0-alex/modules.builtin.bin
/lib/modules/4.2.0-alex/modules.dep
/lib/modules/4.2.0-alex/modules.dep.bin
/lib/modules/4.2.0-alex/modules.devname
/lib/modules/4.2.0-alex/modules.softdep
/lib/modules/4.2.0-alex/modules.symbols
/lib/modules/4.2.0-alex/modules.symbols.bin
```

### 3.5.6 配置引导加载程序GRUB(或LILO)

#### 3.5.6.0 LILO与GRUB的比较

所有引导加载程序都以类似的方式工作，满足共同的目的。不过，LILO和GRUB之间有很多不同之处：

* LILO没有交互式命令界面，而GRUB拥有；
* LILO不支持网络引导，而GRUB支持；
* LILO将关于可以引导的操作系统位置的信息物理上存储在MBR中。如果修改了LILO配置文件，必须将LILO第一阶段引导加载程序重写到MBR。相对于GRUB，这是一个更为危险的选择，因为错误配置的MBR可能会让系统无法引导。使用GRUB，如果配置文件配置错误，则只是默认转到GRUB命令行界面。

#### 3.5.6.1 LILO

编辑LILO的引导配置文件/etc/lilo.conf，添加新内核的启动选项，例如：

```
#
# 主要小节
#
boot=/dev/hda                 # 告诉LILO在哪里安装引导加载程序
map=/boot/map                 # 指向引导期间LILO内部使用的映射文件
install=/boot/boot.b          # 是LILO在引导过程中内部使用的文件之一
message=/boot/message
# 默认启动新内核
default="Linux-3.2"
# 显示启动菜单...
prompt                        # 告诉LILO使用用户界面
# ... 并等候5秒
timeout=50                    # 是引导提示在自动引导默认OS之前的等待时间(以十分之一秒为单位)
#
# 新内核：默认映像
#
image=/boot/vmlinuz-3.2
      label="Linux-3.2"
      root=/dev/hda1
      read-only
      append="devfs=mount resume=/dev/hda5"
#
# 旧内核
# 最好保留旧内核的配置选项，这样不会因升级失败而导致机器无法启动，至少还可用旧内核引导计算机启动
#
image=/boot/vmlinuz
      label="linux"
      root=/dev/hda1
      read-only
      append="devfs=mount resume=/dev/hda5"
#
# 软盘启动
#
other=/dev/floppy
      label="floppy"
      unsafe
```

保存后退出，然后运行命令：

```
# lilo
```

来更新系统引导映象，这样对lilo.conf的修改才会生效。重启操作系统后，在LILO的提示符下按Tab键，可以看到加入的新内核选项。

#### 3.5.6.2 GRUB Legacy

GRUB引导加载程序：

* [http://www.gnu.org/software/grub/grub-legacy.html](http://www.gnu.org/software/grub/grub-legacy.html)
* [ftp://alpha.gnu.org/gnu/grub/](ftp://alpha.gnu.org/gnu/grub/)

GRUB的配置文件保存在/boot/grub中，其目录结构如下：

```
/boot/grub
|-- device.map
|-- menu.lst -> ./grub.conf
|-- grub.conf
|-- grub.conf.201108031656
|-- grub.conf.201210281219
|-- grub.conf.201210281220
|-- grub.conf.ORG_SC
|-- splash.xpm.gz
|-- stage1
|-- e2fs_stage1_5
|-- fat_stage1_5
|-- ffs_stage1_5
|-- iso9660_stage1_5
|-- jfs_stage1_5
|-- minix_stage1_5
|-- reiserfs_stage1_5
|-- ufs2_stage1_5
|-- vstafs_stage1_5
|-- xfs_stage1_5
`-- stage2
```

GRUB有几个重要的文件：stage1、stage1.5、stage2。引导顺序为stage1 -> stage1.5 -> stage2，其中：

* stage1：大小只有512字节，通常放在MBR中，它的作用很简单，就是在系统启动时用于装载stage2并将控制权交给它。
* stage2：GRUB的核心，所有的功能都是由它实现的。
* stage1.5：介于stage1和stage2之间，起桥梁作用，因为stage2较大，通常是放在一个文件系统中的，但是stage1并不能识别文件系统格式，所以需要stage1.5来引导位于某个文件系统中的stage2。根据文件系统格式的不同，stage1.5也需要相应的文件，它们存放于1-63的柱面之间，如：

	* e2fs_stage1_5用于识别ext文件系统格式
	* fat_stage1_5用于识别fat文件系统格式
	* ...

GRUB的引导配置文件为/boot/grub/menu.lst，其链接到./grub.conf，如下所示：

```
# grub.conf generated by anaconda
#
# Note that you do not have to rerun grub after making changes to this file
# NOTICE:  You do not have a /boot partition.  This means that
#          all kernel and initrd paths are relative to /, eg.
#          root (hd0,0)
#          kernel /boot/vmlinuz-version ro root=/dev/cciss/c0d0p1
#          initrd /boot/initrd-version.img
#boot=/dev/cciss/c0d0
default=0
timeout=5
#console.${METH_SUFFIX}#splashimage=(hd0,0)/boot/grub/splash.xpm.gz
hiddenmenu
password  --md5 $1$uQ/fD0$DZpAM1mla6Vauzr2l4rfa0
title Red Hat Enterprise Linux Server (2.6.18-274.18.1.el5)
	root (hd0,0)
	kernel /boot/vmlinuz-2.6.18-274.18.1.el5 ro root=LABEL=/ rhgb quiet apm=off nomce
	initrd /boot/initrd-2.6.18-274.18.1.el5.img
title Red Hat Enterprise Linux Server (2.6.18-194.26.1.el5)
	password  --md5 $1$uQ/fD0$DZpAM1mla6Vauzr2l4rfa0
	root (hd0,0)
	kernel /boot/vmlinuz-2.6.18-194.26.1.el5 ro root=LABEL=/ rhgb quiet apm=off nomce
	initrd /boot/initrd-2.6.18-194.26.1.el5.img
title Infineon Gold Image (2.6.18-164.el5)
	password  --md5 $1$uQ/fD0$DZpAM1mla6Vauzr2l4rfa0
	root (hd0,0)
	kernel /boot/vmlinuz-2.6.18-164.el5 ro root=LABEL=/ rhgb quiet apm=off nomce
	initrd /boot/initrd-2.6.18-164.el5.img
# s+c Service Images start
title Red Hat Enterprise Linux Server (2.6.18-274.18.1.el5) Single User
	password  --md5 $1$uQ/fD0$DZpAM1mla6Vauzr2l4rfa0
	root (hd0,0)
	kernel /boot/vmlinuz-2.6.18-274.18.1.el5 single ro root=LABEL=/ rhgb quiet apm=off nomce
	initrd /boot/initrd-2.6.18-274.18.1.el5.img
title Red Hat E5.0 Rescue System (Network Boot)
	password  --md5 $1$uQ/fD0$DZpAM1mla6Vauzr2l4rfa0
	root (hd0,0)
	kernel /boot/vmlinuz.rhEL5 initrd=/boot/initrd.img rescue root=/dev/nfs ks=nfs:10.216.60.23:/kickstart/rules/netboot.redhatel5 ksdevice=eth0 devfs=nomount ramdisk_size=8192 vga=788 nomce
	initrd /boot/initrd.rhEL5
title Red Hat E5.0 Installer
	password  --md5 $1$uQ/fD0$DZpAM1mla6Vauzr2l4rfa0
	root (hd0,0)
	kernel /boot/vmlinuz.rhEL5 initrd=/boot/initrd.img ks root=/dev/nfs ks=nfs:10.216.60.23:/kickstart/rules/kickstart.redhatel5-x86_64 ksdevice=eth0 devfs=nomount ramdisk_size=8192 vga=788 nomce
	initrd /boot/initrd.rhEL5
# s+c Service Images end
```

其中，

* title表示引导一个操作系统的配置项，可以使多个title项。
* root (hd0,0)用来设置kernel与initrd两项内容的根地址。root指示所需文件存在于哪个磁盘哪个分区上，(hd0,0)表示第一个硬盘，第一个分区，参考/boot/grub/device.map。
* kernel表示内核文件的名字，并且包含一些加载内核时的参数，or代表以只读方式加载。
* initrd是用在内核启动时能够访问的硬盘文件系统，包含一些附加的驱动程序。

编辑/boot/grub/menu.lst并重新启动计算机，就可以看到新添加的内核条目了。

#### 3.5.6.3 GNU GRUB 2

GNU GRUB引导加载程序：

* [http://www.gnu.org/software/grub/grub.html](http://www.gnu.org/software/grub/grub.html)
* [ftp://ftp.gnu.org/gnu/grub/](ftp://ftp.gnu.org/gnu/grub/)
* [ftp://alpha.gnu.org/gnu/grub/](ftp://alpha.gnu.org/gnu/grub/)

**GNU GRUB** is a Multiboot boot loader. It was derived from GRUB, the GRand Unified Bootloader, which was originally designed and implemented by Erich Stefan Boleyn.

**GRUB 2** has replaced what was formerly known as GRUB (i.e. version 0.9x), which has, in turn, become GRUB Legacy. Enhancements to GRUB are still being made, but the current released versions are quite usable for normal operation.

**GRUB Legacy** is no longer being developed.

系统中存在如下有关GRUB 2的命令：

```
chenwx ~ # ll /usr/bin/grub-* /usr/sbin/grub-*
-rwxr-xr-x 1 root root  63456 10月 11  2013 /usr/bin/grub-editenv
-rwxr-xr-x 1 root root 695084 10月 11  2013 /usr/bin/grub-fstest
-rwxr-xr-x 1 root root   1737 10月 11  2013 /usr/bin/grub-kbdcomp
-rwxr-xr-x 1 root root  43216 10月 11  2013 /usr/bin/grub-menulst2cfg
-rwxr-xr-x 1 root root  83552 10月 11  2013 /usr/bin/grub-mkfont
-rwxr-xr-x 1 root root 131380 10月 11  2013 /usr/bin/grub-mkimage
-rwxr-xr-x 1 root root  63488 10月 11  2013 /usr/bin/grub-mklayout
-rwxr-xr-x 1 root root  71844 10月 11  2013 /usr/bin/grub-mkpasswd-pbkdf2
-rwxr-xr-x 1 root root 207120 10月 11  2013 /usr/bin/grub-mkrelpath
-rwxr-xr-x 1 root root  13510 10月 11  2013 /usr/bin/grub-mkrescue
-rwxr-xr-x 1 root root   6387 10月 11  2013 /usr/bin/grub-mkstandalone
-rwxr-xr-x 1 root root 515820 10月 11  2013 /usr/bin/grub-mount
lrwxrwxrwx 1 root root     34  4月 28 20:14 /usr/bin/grub-ntldr-img -> ../lib/grub/i386-pc/grub-ntldr-img
-rwxr-xr-x 1 root root  83744 10月 11  2013 /usr/bin/grub-script-check
lrwxrwxrwx 1 root root     35  4月 28 20:20 /usr/sbin/grub-bios-setup -> ../lib/grub/i386-pc/grub-bios-setup
-rwxr-xr-x 1 root root   1248  5月 14  2013 /usr/sbin/grub-install
-rwxr-xr-x 1 root root  35079 10月 11  2013 /usr/sbin/grub-install.real
-rwxr-xr-x 1 root root   7689 10月 11  2013 /usr/sbin/grub-mkconfig
-rwxr-xr-x 1 root root  38612 10月 11  2013 /usr/sbin/grub-mkdevicemap
-rwxr-xr-x 1 root root   7530 10月 11  2013 /usr/sbin/grub-mknetdir
-rwxr-xr-x 1 root root 780684 10月 11  2013 /usr/sbin/grub-probe
-rwxr-xr-x 1 root root   3933 10月 11  2013 /usr/sbin/grub-reboot
-rwxr-xr-x 1 root root   3442 10月 11  2013 /usr/sbin/grub-set-default

chenwx ~ # ll /usr/bin/update-grub* /usr/sbin/update-grub*
-rwxr-xr-x 1 root root  64 10月  5  2012 /usr/sbin/update-grub
lrwxrwxrwx 1 root root  11  4月 28 20:20 /usr/sbin/update-grub2 -> update-grub
-rwxr-xr-x 1 root root 241  8月 16  2011 /usr/sbin/update-grub-gfxpayload
```

修改配置文件/etc/default/grub:

* 设置内核启动选项earlyprink=vga，把系统早期启动的信息打印到显示屏上
* 注释掉GRUB_HIDDEN_TIMEOUT和GRUB_HIDDEN_TIMEOUT_QUIET
* 设置启动菜单超时时间为10：GRUB_TIMEOUT=10，或者，设置为等待用户选择：GRUB_TIMEOUT=-1

```
#GRUB_HIDDEN_TIMEOUT=0
#GRUB_HIDDEN_TIMEOUT_QUIET=true
GRUB_TIMEOUT=10
GRUB_CMDLINE_LINUX="earlyprink=vga"
```

执行下列命令更新配置文件/boot/grub/grub.cfg:

```
# method (1) to upldate /boot/grub/grub.cfg
chenwx@chenwx /boot $ sudo update-grub
[sudo] password for chenwx:
Generating grub.cfg ...
Found linux image: /boot/vmlinuz-3.11.0-12-generic
Found initrd image: /boot/initrd.img-3.11.0-12-generic
Found memtest86+ image: /boot/memtest86+.bin
  No volume groups found
done

# method (2) to upldate /boot/grub/grub.cfg
chenwx@chenwx /boot $ su
Password:
chenwx boot # grub-mkconfig > /boot/grub/grub.cfg
Generating grub.cfg ...
Found linux image: /boot/vmlinuz-3.15.9-031509-generic
Found initrd image: /boot/initrd.img-3.15.9-031509-generic
Found linux image: /boot/vmlinuz-3.11.0-12-generic
Found initrd image: /boot/initrd.img-3.11.0-12-generic
Found linux image: /boot/vmlinuz-3.2.0
Found initrd image: /boot/initrd.img-3.2.0
Found memtest86+ image: /boot/memtest86+.bin
  No volume groups found
done
```

### 3.5.7 重新启动系统前的准备工作

运行脚本[dmesg_msg_diff.sh](https://github.com/chenweixiang/scripts/blob/master/dmesg_msg_diff.sh)来保存编译内核产生的日志，用于比较和查找错误：

```
$ dmesg -t -l emerg > `uname -r`.dmesg_current_emerg
$ dmesg -t -l alert > `uname -r`.dmesg_current_alert
$ dmesg -t -l crit > `uname -r`.dmesg_current_alert
$ dmesg -t -l err > `uname -r`.dmesg_current_err
$ dmesg -t -l warn > `uname -r`.dmesg_current_warn
$ dmesg -t -k > `uname -r`.dmesg_kernel
$ dmesg -t > `uname -r`.dmesg_current
```

运行脚本[dmesg_msg_save.sh](https://github.com/chenweixiang/scripts/blob/master/dmesg_msg_save.sh)输出日志文件：

```
#!/bin/bash
#
# Copyright(c) Chen Weixiang <weixiang.chen@gmail.com>
#
# License: GPLv2

release=`uname -r`

echo "dmesg -t -l emerg > $release.dmesg_emerg"
dmesg -t -l emerg > $release.dmesg_emerg

echo "dmesg -t -l crit > $release.dmesg_crit"
dmesg -t -l crit > $release.dmesg_crit

echo "dmesg -t -l alert > $release.dmesg_alert"
dmesg -t -l alert > $release.dmesg_alert

echo "dmesg -t -l err > $release.dmesg_err"
dmesg -t -l err > $release.dmesg_err

echo "dmesg -t -l warn > $release.dmesg_warn"
dmesg -t -l warn > $release.dmesg_warn

echo "dmesg -t -k > $release.dmesg_kern"
dmesg -t -k > $release.dmesg_kern

echo "dmesg -t > $release.dmesg"
dmesg -t > $release.dmesg
```

### 3.5.8 重启系统，并验证新内核

重新启动内核后，首先查看新内核的版本信息：

```
/*
 * (1) 查看内核版本信息
 */
chenwx@chenwx ~/linux $ uname -a
Linux chenwx 4.1.5-alex #2 SMP Wed Aug 12 22:53:34 CST 2015 x86_64 x86_64 x86_64 GNU/Linux

chenwx@chenwx ~/linux $ cat /proc/version
Linux version 4.1.5-alex (chenwx@chenwx) (gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04) ) #2 SMP Wed Aug 12 22:53:34 CST 2015

/*
 * (2) 查看头文件信息
 */
chenwx@chenwx ~/linux $ dpkg -L linux-headers-4.1.5-alex
/.
/usr
/usr/src
/usr/src/linux-headers-4.1.5-alex
/usr/src/linux-headers-4.1.5-alex/.config
/usr/src/linux-headers-4.1.5-alex/Module.symvers
/usr/src/linux-headers-4.1.5-alex/init
/usr/src/linux-headers-4.1.5-alex/init/Makefile
/usr/src/linux-headers-4.1.5-alex/init/Kconfig
/usr/src/linux-headers-4.1.5-alex/samples
/usr/src/linux-headers-4.1.5-alex/samples/kdb
/usr/src/linux-headers-4.1.5-alex/samples/kdb/Makefile
/usr/src/linux-headers-4.1.5-alex/samples/hw_breakpoint
...
/usr/src/linux-headers-4.1.5-alex/Kconfig
/usr/share
/usr/share/doc
/usr/share/doc/linux-headers-4.1.5-alex
/usr/share/doc/linux-headers-4.1.5-alex/changelog.Debian.gz
/usr/share/doc/linux-headers-4.1.5-alex/copyright
/lib
/lib/modules
/lib/modules/4.1.5-alex
/lib/modules/4.1.5-alex/build
```

然后，比较新老内核的dmesg信息，看看新的内核有没有编译错误。

使用dmesg查看隐藏的问题，对于定位新代码带来的bug是一个好方法。一般来说，dmesg不会输出新的crit, alert, emerg级别的错误信息，也不应该出现新的err级别的信息。要注意的是那些warn级别的日志信息。注意：warn级别的信息并不是坏消息，新代码带来新的警告信息，不会给内核带去严重的影响。

运行脚本[dmesg_msg_save.sh](https://github.com/chenweixiang/scripts/blob/master/dmesg_msg_save.sh)输出日志文件：

```
#!/bin/bash
#
# Copyright(c) Chen Weixiang <weixiang.chen@gmail.com>
#
# License: GPLv2

if [ "$1" == "" ]; then
        echo "$0 <old uname -r>"
        exit -1
fi

release=`uname -r`

echo "Start dmesg regression check for $release" > dmesg_checks_results

echo "--------------------------" >> dmesg_checks_results

dmesg -t -l emerg > $release.dmesg_emerg
echo "dmesg emergency regressions"
echo "--------------------------" >> dmesg_checks_results
diff $1.dmesg_emerg $release.dmesg_emerg >> dmesg_checks_results
echo "--------------------------" >> dmesg_checks_results

dmesg -t -l crit > $release.dmesg_crit
echo "dmesg critical regressions"
echo "--------------------------" >> dmesg_checks_results
diff $1.dmesg_crit $release.dmesg_crit >> dmesg_checks_results
echo "--------------------------" >> dmesg_checks_results

dmesg -t -l alert > $release.dmesg_alert
echo "dmesg alert regressions" >> dmesg_checks_results
echo "--------------------------" >> dmesg_checks_results
diff $1.dmesg_alert $release.dmesg_alert >> dmesg_checks_results
echo "--------------------------" >> dmesg_checks_results

dmesg -t -l err > $release.dmesg_err
echo "dmesg err regressions" >> dmesg_checks_results
echo "--------------------------" >> dmesg_checks_results
diff $1.dmesg_err $release.dmesg_err >> dmesg_checks_results
echo "--------------------------" >> dmesg_checks_results

dmesg -t -l warn > $release.dmesg_warn
echo "dmesg warn regressions" >> dmesg_checks_results
echo "--------------------------" >> dmesg_checks_results
diff $1.dmesg_warn $release.dmesg_warn >> dmesg_checks_results
echo "--------------------------" >> dmesg_checks_results

dmesg -t -k > $release.dmesg_kern
echo "dmesg_kern regressions" >> dmesg_checks_results
echo "--------------------------" >> dmesg_checks_results
diff $1.dmesg_kern $release.dmesg_kern >> dmesg_checks_results
echo "--------------------------" >> dmesg_checks_results

dmesg -t > $release.dmesg
echo "dmesg regressions" >> dmesg_checks_results
echo "dmesg regressions" >> dmesg_checks_results
echo "--------------------------" >> dmesg_checks_results
diff $1.dmesg $release.dmesg >> dmesg_checks_results
echo "--------------------------" >> dmesg_checks_results

echo "--------------------------" >> dmesg_checks_results

echo "End dmesg regression check for $release" >> dmesg_checks_results
```

运行脚本[dmesg_msg_diff.sh](https://github.com/chenweixiang/scripts/blob/master/dmesg_msg_diff.sh)来对比两者的差别：

```
dmesg -t -l emerg > `uname -r`.dmesg_current_emerg
dmesg -t -l alert > `uname -r`.dmesg_current_alert
dmesg -t -l crit > `uname -r`.dmesg_current_alert
dmesg -t -l err > `uname -r`.dmesg_current_err
dmesg -t -l warn > `uname -r`.dmesg_current_warn
dmesg -t -k > `uname -r`.dmesg_kernel
dmesg -t > `uname -r`.dmesg_current
```

## 3.5A 采用make deb-pkg为Debian系统升级内核

[**NOTE**] Thinkpad R61i采用LinuxMint系统，故使用此方法升级内核更方便，简单！

除了采用[3.5 内核升级](#)节所述的方法升级内核外，也可以采用```make deb-pkg```命令编译内核并为Debian系统升级内核：

```
# 安装必要工具包(仅需执行一次)
chenwx@chenwx ~/linux $ sudo apt-get install kernel-package

# 选择内核版本
chenwx@chenwx ~/linux $ git checkout v4.0.1

# 清空内核目录
chenwx@chenwx ~/linux $ make mrproper
chenwx@chenwx ~/linux $ make mrproper O=../linux-build
chenwx@chenwx ~/linux $ make-kpkg clean
chenwx@chenwx ~/linux $ make-kpkg clean O=../linux-build

# 配置内核
chenwx@chenwx ~/linux $ cp /boot/config-3.13.0-24-generic ../linux-build/.config
chenwx@chenwx ~/linux $ make olddefconfig O=../linux-build

# 清空内核目录，并将内核编译成deb包，其中:
# LOCALVERSION:    等价于顶层Makefile中的EXTRAVERSION
# KDEB_PKGVERSION: 用于命名软件包；若未设置该变量，则采用../linux-build/.version中的取值(该值会递增)
chenwx@chenwx ~/linux $ make deb-pkg O=../linux-build LOCALVERSION=-alex KDEB_PKGVERSION=1
  CHK     include/config/kernel.release
  UPD     include/config/kernel.release
make KBUILD_SRC=
  HOSTCC  scripts/basic/fixdep
  HOSTCC  arch/x86/tools/relocs_32.o
  HOSTCC  arch/x86/tools/relocs_64.o
  HOSTCC  arch/x86/tools/relocs_common.o
  HOSTLD  arch/x86/tools/relocs
  ...

# 编译后的deb包位与上级目录，其命名格式为:
# linux-<PACKAGETYPE>-<VERSION.PATCHLEVEL.SUBLEVEL><LOCALVERSION>_<KDEB_PKGVERSION>_<CPUTYPE>.deb
chenwx@chenwx ~/linux $ ll ../linux-*
-rw-r--r--  1 chenwx chenwx 945K Jun 11 21:03 linux-firmware-image-4.0.1-alex_1_amd64.deb
-rw-r--r--  1 chenwx chenwx 6.7M Jun 11 21:04 linux-headers-4.0.1-alex_1_amd64.deb
-rw-r--r--  1 chenwx chenwx 355M Jun 11 21:43 linux-image-4.0.1-alex-dbg_1_amd64.deb
-rw-r--r--  1 chenwx chenwx  38M Jun 11 21:06 linux-image-4.0.1-alex_1_amd64.deb
-rw-r--r--  1 chenwx chenwx 781K Jun 11 21:04 linux-libc-dev_1_amd64.deb

# 安装新内核
chenwx@chenwx ~/linux $ sudo dpkg -i ../*.deb

# 重启系统，并验证新内核
chenwx@chenwx ~/linux $ uname -a
Linux chenwx 4.0.1-alex #5 SMP Tue May 5 07:01:44 CST 2015 x86_64 x86_64 x86_64 GNU/Linux
```

## 3.5B 采用make-kpkg编译并升级内核

```
NAME
       make-kpkg - build Debian kernel packages from Linux kernel sources

SYNOPSIS
       make-kpkg [options] [target [target ...]]

DESCRIPTION
       This manual page explains the Debian make-kpkg utility, which is used to create the kernel
       related Debian packages. This utility needs to be run from a top level Linux kernel source
       directory, which has been previously configured (unless you are using the configure target).
       Normally, if kernel-package does not find a .config file in the current directory, it tries
       very hard to get an appropriate one (usually a config file already tailored for Debian
       kernels for that architecture), and then calls make oldconfig to let the user answer any new
       questions. However, this might still result in an inappropriate configuration, you are
       encouraged to configure the kernel by the usual means before invoking make-kpkg.

       Typically, make-kpkg should be run under fakeroot,

            make-kpkg --rootcmd fakeroot kernel_image

       but instead you run this command as root (this is not recommended), or under fakeroot, or
       tell make-kpkg how to become root (not recommended either, fakeroot is perhaps the safest
       option), like so:

            make-kpkg --rootcmd sudo kernel_image

       The Debian package file is created in the parent directory of the kernel source directory
       where this command is run.

Refer to the following commands:
chenwx@chenwx ~/linux $ sudo apt-get install kernel-package
chenwx@chenwx ~/linux $ which make-kpkg
/usr/bin/make-kpkg

chenwx@chenwx ~/linux $ make-kpkg --help
This program should be run in a linux kernel source top level directory.
/usr/share/doc/kernel-package/Problems.gz contains a list of known problems.

usage: make-kpkg [options] target [target ...]
  where options are:
 --help                This message.
 --revision number     The debian revision number. ([a-zA-Z.~+0-9]) (Must
                         have digit)
 --append-to-version foo
 --append_to_version foo an additional kernel sub-version. ([-a-z.+0-9])
                         Does not require editing the kernel Makefile
                         over rides env var APPEND_TO_VERSION.
                         requires a make-kpkg clean
 --added-modules foo
 --added_modules foo   Comma/space separated list of add on modules
                       affected by the modules_<blah> targets
 --arch     foo        architecture
 --cross-compile
 --cross_compile       target string
 --subarch  bar        Set the subarch for the image being compiled
                        (have to be on a compatible machine).
 --arch-in-name
 --arch_in_name        Embed the subarch in the image package name
 --stem     foo        Call the packages foo-* instead of kernel-*
 --initrd              Create a image package suitable for initrd.
 -j         jobs       Sec CONCURRENCY_LEVEL to -I<jobs> for this action.
 --jobs     jobs       Set CONCURRENCY_LEVEL to -I<jobs> for this action.
 --pgpsign  name       An ID used to sign the changes file using pgp.
 --config target       Change the type of configure done from the  default
                       oldconfig.
 --targets             Lists the known targets.
 --noexec              Pass a -n option to the make process
 --overlay dir         An overlay directory to (re))place file in ./debian
 --verbose             Pass a V=1 option to the make process
 --zimage              Create a kernel using zImage rather than bzImage
 --bzimage             Create a kernel using bzImage (in case the site
                       wide default is zimage, as set in
                       /etc/kernel-pkg.conf)
 --rootcmd method      A command that provides a means of gaining
                       superuser access (for example, `sudo' or
                       `fakeroot') as needed by dpkg-buildpackages'
                       -r option. Does not work for targets binary,
                        binary-indep,  and  binary-arch.
 --us                  This option is passed to dpkg-buildpackage, and
                       directs that package not to sign the
                       source. This is only relevant for the
                       buildpackage target.
 --uc                  This option is passed to dpkg-buildpackage, and
                       directs that package not to sign the
                       changelog. This is only relevant for the
                       buildpackage target.

Use one of --zimage or --bzimage, or none, but not both.

Option Format: The options may be shortened to the smallest unique
string, and may be entered with either a - or a -- prefix, and you may
use a space between an option string and a value. Please refer to man
Getopt::Long for details on how the options may be entered.

Version: 12.036+nmu3
Manoj Srivastava <srivasta@debian.org>

chenwx@chenwx ~/linux $ make-kpkg --targets
 Known Targets are:
===============================================================================
|     Targets                      |   Automatically builds                   |
===============================================================================
|  clean                           |                                          |
|  buildpackage                    | Builds the whole package                 |
|* binary                          | Builds kernel_{source,headers,image,doc} |
|*      binary-indep               |                                          |
|            kernel_source         |                                          |
|            kernel_doc            |                                          |
|            kernel_manual         |                                          |
|*      binary-arch                |                                          |
|            kernel_headers        |                                          |
|            kernel_debug          |                                          |
|            kernel_image          | Builds build                             |
|                           build  |                                          |
| modules                          |                                          |
| modules_image                    |                                          |
| modules_config                   |                                          |
| modules_clean                    |                                          |
| configure                        | If you wish to edit files                |
|                           debian | generated by make config                 |
| debian                           | Creates ./debian dir                     |
===============================================================================
 *: make-kpkg needs to be run as root (or fakeroot), --rootcmd will not work
See /usr/share/kernel-package/rules for details.

chenwx@chenwx ~/linux $ fakeroot make-kpkg --initrd --append-to-version -alex kernel_image kernel_headers
```

## 3.6 内核补丁/Patch

参见Documentation/applying-patches.txt关于内核补丁的描述：

> A patch is a small text document containing a delta of changes between two different versions of a source tree. Patches are created with the 'diff' program.
>
> To correctly apply a patch you need to know what base it was generated from and what new version the patch will change the source tree into. These should both be present in the patch file metadata or be possible to deduce from the filename.

### 3.6.1 内核补丁的下载地址

The patches are available at:
* [http://kernel.org/](http://kernel.org/)
* [ftp://www.kernel.org/pub/linux/kernel/v3.x/](ftp://www.kernel.org/pub/linux/kernel/v3.x/)

Most recent patches are linked from the front page, but they also have specific homes:

**The v2.6 and v3.x patches live at**

* [ftp://ftp.kernel.org/pub/linux/kernel/v2.6/](ftp://ftp.kernel.org/pub/linux/kernel/v2.6/)
* [ftp://ftp.kernel.org/pub/linux/kernel/v3.x/](ftp://ftp.kernel.org/pub/linux/kernel/v3.x/)

**The v2.6 and v3.x -rc patches live at**

* [ftp://ftp.kernel.org/pub/linux/kernel/v2.6/testing/](ftp://ftp.kernel.org/pub/linux/kernel/v2.6/testing/)
* [ftp://ftp.kernel.org/pub/linux/kernel/v3.x/testing/](ftp://ftp.kernel.org/pub/linux/kernel/v3.x/testing/)

**The v2.6 and v3.x -git patches live at**

* [ftp://ftp.kernel.org/pub/linux/kernel/v2.6/snapshots/](ftp://ftp.kernel.org/pub/linux/kernel/v2.6/snapshots/)
* [ftp://ftp.kernel.org/pub/linux/kernel/v3.x/incr/](ftp://ftp.kernel.org/pub/linux/kernel/v3.x/incr/)

**The v2.6 and v3.x -mm kernels live at**

* [ftp://ftp.kernel.org/pub/linux/kernel/people/akpm/patches/2.6/](ftp://ftp.kernel.org/pub/linux/kernel/people/akpm/patches/2.6/)

### 3.6.2 如何应用内核补丁

注意：安装内核补丁前，需要先进入老版本的内核源代码目录，以linux-3.2为例：

```
# cd ~/linux-3.2
```

Uncompress and apply the patch:

```
# zcat path/to/patch-x.y.z.gz | patch -p1
# bzcat path/to/patch-x.y.z.bz2 | patch -p1
# xzcat path/to/patch-x.y.z.xz | patch -p1
```

Uncompress the patch:

```
# gunzip patch-x.y.z.gz		// 解压后的patch为patch-x.y.z
# bunzip2 patch-x.y.z.bz2	// 解压后的patch为patch-x.y.z
# unxz patch-x.y.z.xz		// 解压后的patch为patch-x.y.z
```

Apply a uncompressed patch:

```
# patch -p1 < path/to/patch-x.y.z
```

Revert (undo) a patch:

```
# patch -p1 -R < path/to/patch-x.y.z
```

Patch can get the name of the file to use via the -i argument:

```
# patch -p1 -i path/to/patch-x.y.z
```

Just print a listing of what would happen, but doesn't actually make any changes:

```
# patch -p1 --dry-run path/to/patch-x.y.z
```

Make patch to be silent except for errors:

```
# patch -p1 -s path/to/patch-x.y.z
```

Print more information about the work being done:

```
# patch -p1 --verbose path/to/patch-x.y.z
```

#### 3.6.2.1 The 2.6.x.y kernels

Kernels with 4-digit versions are -stable kernels.

These patches are not incremental, meaning that, for example the 2.6.12.3 patch does not apply on top of the 2.6.12.2 kernel source, but rather on top of the base 2.6.12 kernel source. So, in order to apply the 2.6.12.3 patch to your existing 2.6.12.2 kernel source, you have to first back out the 2.6.12.2 patch (so you are left with a base 2.6.12 kernel source) and then apply the new 2.6.12.3 patch. For example:


```
$ cd ~/linux-2.6.12.2					# change into the kernel source dir
$ patch -p1 -R < ../patch-2.6.12.2		# revert the 2.6.12.2 patch
$ patch -p1 < ../patch-2.6.12.3			# apply the new 2.6.12.3 patch
$ cd ..
$ mv linux-2.6.12.2 linux-2.6.12.3		# rename the kernel source dir
```

#### 3.6.2.2 The -rc kernels

These are release-candidate kernels (not stable). The -rc patches are not incremental, they apply to a base 2.6.x kernel, just like the 2.6.x.y patches described above (See section The 2.6.x.y kernels).

The kernel version before the –rcN suffix denotes the version of the kernel that this -rc kernel will eventually turn into. So, 2.6.13-rc5 means that this is the fifth release candidate for the 2.6.13 kernel and the patch should be applied on top of the 2.6.12 kernel source.

Here are 3 examples of how to apply these patches:

```
# First an example of moving from 2.6.12 to 2.6.13-rc3
$ cd ~/linux-2.6.12					# change into the 2.6.12 source dir
$ patch -p1 < ../patch-2.6.13-rc3		# apply the 2.6.13-rc3 patch
$ cd ..
$ mv linux-2.6.12 linux-2.6.13-rc3		# rename the source dir

# Now let's move from 2.6.13-rc3 to 2.6.13-rc5
$ cd ~/linux-2.6.13-rc3				# change into the 2.6.13-rc3 dir
$ patch -p1 -R < ../patch-2.6.13-rc3		# revert the 2.6.13-rc3 patch
$ patch -p1 < ../patch-2.6.13-rc5		# apply the new 2.6.13-rc5 patch
$ cd ..
$ mv linux-2.6.13-rc3 linux-2.6.13-rc5	# rename the source dir

# Finally let's try and move from 2.6.12.3 to 2.6.13-rc5
$ cd ~/linux-2.6.12.3					# change to the kernel source dir
$ patch -p1 -R < ../patch-2.6.12.3		# revert the 2.6.12.3 patch
$ patch -p1 < ../patch-2.6.13-rc5		# apply new 2.6.13-rc5 patch
$ cd ..
$ mv linux-2.6.12.3 linux-2.6.13-rc5		# rename the kernel source dir
```

#### 3.6.2.3 The -git kernels

These are daily snapshots of Linus' kernel tree. These patches are usually released daily and represent the current state of Linus's tree. They are more experimental than -rc kernels since they are generated automatically without even a cursory glance to see if they are sane.

-git patches are not incremental and apply either to a base 2.6.x kernel or a base 2.6.x-rc kernel -- you can see which from their name. A patch named 2.6.12-git1 applies to the 2.6.12 kernel source and a patch named 2.6.13-rc3-git2 applies to the source of the 2.6.13-rc3 kernel.

Here are some examples of how to apply these patches:

```
# moving from 2.6.12 to 2.6.12-git1
$ cd ~/linux-2.6.12						# change to the kernel source dir
$ patch -p1 < ../patch-2.6.12-git1			# apply the 2.6.12-git1 patch
$ cd ..
$ mv linux-2.6.12 linux-2.6.12-git1			# rename the kernel source dir

// moving from 2.6.12-git1 to 2.6.13-rc2-git3
$ cd ~/linux-2.6.12-git1					# change to the kernel source dir
// revert the 2.6.12-git1 patch. we now have a 2.6.12 kernel
$ patch -p1 -R < ../patch-2.6.12-git1
// apply the 2.6.13-rc2 patch. the kernel is now 2.6.13-rc2
$ patch -p1 < ../patch-2.6.13-rc2

// apply the 2.6.13-rc2-git3 patch. the kernel is now 2.6.13-rc2-git3
$ patch -p1 < ../patch-2.6.13-rc2-git3
$ cd ..
$ mv linux-2.6.12-git1 linux-2.6.13-rc2-git3	# rename source dir
```

#### 3.6.2.4 The -mm kernels

These are experimental kernels released by Andrew Morton.

Here are some examples of applying the -mm patches:

```
# moving from 2.6.12 to 2.6.12-mm1
$ cd ~/linux-2.6.12				# change to the 2.6.12 source dir
$ patch -p1 < ../2.6.12-mm1			# apply the 2.6.12-mm1 patch
$ cd ..
$ mv linux-2.6.12 linux-2.6.12-mm1	# rename the source appropriately

# moving from 2.6.12-mm1 to 2.6.13-rc3-mm3
$ cd ~/linux-2.6.12-mm1
$ patch -p1 -R < ../2.6.12-mm1		# revert the 2.6.12-mm1 patch. we now have a 2.6.12 source
$ patch -p1 < ../patch-2.6.13-rc3	# apply the 2.6.13-rc3 patch. we now have a 2.6.13-rc3 source
$ patch -p1 < ../2.6.13-rc3-mm3		# apply the 2.6.13-rc3-mm3 patch
$ cd ..
$ mv linux-2.6.12-mm1 linux-2.6.13-rc3-mm3	# rename the source dir
```

### 3.6.3 如何生成内核补丁

#### 3.6.3.1 通过diff生成内核补丁

The simplest way to generate a patch is to have two source trees, one that is the vanilla stock kernel (such as linux-3.2-vanilla) and another that is the stock tree with your modifications (such as linux-3.2). To generate a patch of the two trees, issue the following command from one directory above the standard kernel source tree:

```
# cd /home/
# tar xvf linux-3.2.tar.bz2				// unzip source code to /home/linux-3.2
# mv linux-3.2 linux-3.2-vanilla			// source tree without change
# tar xvf linux-3.2.tar.bz2				// unzip source code to /home/linux-3.2
# vi linux-3.2/some/files				// make your changes
# diff -uprN -X linux-3.2-vanilla/Documentation/dontdiff linux-3.2-vanilla/ linux-3.2/ > my-patch
```

Alternatively, if you need to diff only a single file, you can do

```
# cp linux-3.2/mm/memory.c linux-3.2/mm/memory.c.orig
# vi linux-3.2/mm/memory.c				// make your change
# diff -up linux-3.2/mm/memory.c{.orig,} > my-patch
```

A useful utility is diffstat, which generates a histogram of a patch’s changes (line additions and removals). To generate the output on one of your patches, do

```
# diffstat -p 1 -w 70 my-patch
```

[**NOTE1**] Patches generated with diff should always be unified diff, include the C function that the change affects and be generated from one directory above the kernel source root. A unified diff include more information that just the differences between two lines. It begins with a two line header with the names and creation date of the two files that diff is comparing.

[**NOTE2**] "dontdiff" is a list of files which are generated by the kernel during the build process, and should be ignored in any diff(1)-generated patch. The "dontdiff" file is included in the kernel tree in 2.6.12 and later. For earlier kernel versions, you can get it from <http://www.xenotime.net/linux/doc/dontdiff>.

#### 3.6.3.2 通过git生成内核补丁

When you have a commit (or two) in your tree, you can generate a patch for each commit, which you can treat as you do the patches described in the previous section:

```
# git format-patch -s origin
```

This generates patches for all commits in your repository and not in the original tree. Git creates the patches in the root of your kernel source tree. To generate patches for only the last N commits, you can execute the following:

```
# git format-patch -s -N
```

Use below command to generate the diffstat:

```
# git diff -M --stat –summary <commit-1> <commit-2>
```

where, the ```-M``` enables rename detection, and the ```--summary``` enables a summary of new/deleted or renamed files.

# 4 Linux系统的启动过程

阅读下列文档：

* linux-3.2/Documentation/x86/boot.txt
* [计算机是如何启动的](/docs/How_to_Start_Computer.pdf)
* [Linux的启动流程](/docs/Linux_Startup_Process.pdf)

## 4.1 内核映像的内存布局

在linux-3.2/Documentation/x86/boot.txt中，包含有关内核映像(参见[bzImage](#)节和[安装内核](#3-5-5-)节)的内存布局的描述。根据内核版本的不同，内核映像的内存布局也存在差异，分别参见[4.1.1 Image/zImage (old kernels)](#4-1-1-image-zimage-old-kernels-)节和[4.1.2 bzImage (modern kernel)](#4-1-2-bzimage-modern-kernel-)节，以及下图：

![bzImage_2](/assets/bzImage_2.png)

![bzImage_3](/assets/bzImage_3.png)

![bzImage_4](/assets/bzImage_4.png)

内核映像的内存布局包含如下几个重要部分：

| 内核组成部分 | 模式  | 源代码出处 |
| :--------- | :--- | :------- |
| Kernel boot sector | 实模式 | v2.6.23及其之前版本的内核:<br>arch/i386/boot/bootsect.S<br>arch/x86_64/boot/bootsect.S<br><br>v2.6.24及其之后版本的内核:<br>arch/i386/boot/header.S<br>arch/i386/boot/main.c |
| Kernel setup | 实模式 | v2.6.23及其之前版本的内核:<br>arch/i386/boot/setup.S<br>arch/x86_64/boot/setup.S<br><br>v2.6.24及其之后版本的内核:<br>arch/i386/boot/header.S<br>arch/i386/boot/main.c |
| Protected-mode kernel | 保护模式 | |

<p/>

**实模式**

实模式是指寻址采用和8086相同的16位段和偏移量，最大寻址空间1MB，最大分段64KB。

![real-mode-protocol](/assets/real-mode-protocol.png)

**保护模式**

保护模式是指寻址采用32位段和偏移量，最大寻址空间4GB，最大分段4GB(Pentium Pre及以后为64GB)。在保护模式下，CPU可以进入虚拟8086方式，这是在保护模式下的实模式程序运行环境。

由[4.1.1 Image/zImage (old kernels)](#4-1-1-image-zimage-old-kernels-)节和[4.1.2 bzImage (modern kernel)](#4-1-2-bzimage-modern-kernel-)节可知：

* real-mode code: boot sector and setup code
* real-mode code can total up to 32KB, although the boot loader may choose to load only the first two sectors (1K)

### 4.1.1 Image/zImage (old kernels)

The traditional memory map for the kernel loader, used for Image or zImage kernels, typically looks like:

![Memery_Layout_03](/assets/Memery_Layout_03.jpg)

### 4.1.2 bzImage (modern kernel)

For a modern bzImage kernel with boot protocol version >= 2.02, a memory layout is suggested like:

![Memery_Layout_02](/assets/Memery_Layout_02.jpg)

where, the address X is as low as the design of the boot loader permits.

## 4.2 主引导记录MBR(Master Boot Record)

### 4.2.1 硬盘结构

硬盘有很多盘片组成，每个盘片的每个面都有一个读写磁头。如果有N个盘片，就有2N个面，对应着2N个磁头(Heads)，从0、1、2...开始编号。每个盘片的半径为固定值R的同心圆在逻辑上形成了一个以电机主轴为轴的柱面(Cylinders)，由外至里编号为0、1、2...。每个盘片上的每个磁道又被划分为几十个扇区(Sector)，通常每个扇区的容量是512字节，并按照一定规则编号1、2、3...，形成Cylinders × Heads × Sector个扇区。

![HardDisk](/assets/HardDisk.png)

对于硬盘而言，一个扇区可能的字节数为128 x 2^n (n=0,1,2,3)。大多情况下，取n=2，即一个扇区(sector)大小为512字节。

### 4.2.2 主引导扇区

主引导扇区位于整个硬盘的0柱面0磁头1扇区```{(柱面，磁头，扇区)|(0，0，1)}```，BIOS在执行完自己固有的程序以后就会jump到MBR中的第一条指令，将系统的控制权交由MBR来执行。主引导扇区主要由三部分组成：

* 主引导记录 MBR (Master Boot Record)
* 硬盘分区表 DPT (Disk Partition Table)
* 结束标志字

![MBR_Components](/assets/MBR_Components.png)

![MBR_Sections](/assets/MBR_Sections.png)

#### 4.2.2.1 主引导记录MBR

主引导记录中包含了硬盘的一系列参数和一段引导程序。其中，硬盘引导程序的主要作用是检查硬盘分区表是否正确并且在系统硬件完成自检后将控制权交给硬盘上的引导程序(如GNU GRUB)。MBR是由分区程序(如Fdisk)所产生的，它是低级格式化的产物，和操作系统没有任何关系，即它不依赖任何操作系统；而且硬盘引导程序也是可以改变的，从而能够实现多系统引导。

#### 4.2.2.2 硬盘分区表DPT

硬盘分区表占据主引导扇区的64个字节(01BE-01FD)，可以对四个分区信息进行描述，其中每个分区信息占16个字节。具体每个字节的定义可以参见硬盘分区结构信息。

| 偏移(十六进制) | 长度(字节) | 含义  |
| :----------: | :-------: | :--- |
| 00 | 1 | 分区状态：<br>00->非活动分区<br>80->活动分区，表示系统可引导<br>其他数值无意义 |
| 01 | 1 | 分区起始磁头号(Head)，使用全部8位 |
| 02 | 2 | 分区起始扇区号(Sector)，占据02字节的Bit #0-#5；<br>分区起始柱面号(Cylinder)，占据02字节的Bit #6-#7和03字节的全部8位 |
| 04 | 1 | 文件系统标志位：<br>0B表示分区的文件系统是FAT32<br>04表示分区的文件系统是FAT16<br>07表示分区的文件系统是NTFS |
| 05 | 1 | 分区结束磁头号(Head)，使用全部8位 |
| 06 | 2 | 分区结束扇区号(Sector)，占据06字节的Bit #0-#5；<br>分区结束柱面号(Cylinder)，占据06字节的Bit #6-#7和07字节的全部8位 |
| 08 | 4 | 分区起始相对扇区 |
| 0C | 4 | 分区总的扇区数 |

<p/>

#### 4.2.2.3 结束标志字

结束标志字55AA(偏移1FE-1FF)是主引导扇区的最后两个字节，用于检验主引导记录是否有效的标志。

## 4.3 Linux引导过程

![Linux_Boot](/assets/Linux_Boot.png)

当系统首次引导或系统被重置时，处理器会执行一个位于已知位置处的代码。在PC中，这个位置在基本输入/输出系统(BIOS)中，它保存在主板上的闪存中。嵌入式系统中的中央处理单元(CPU)会调用这个重置向量来启动一个位于闪存/ROM中的已知地址处的程序。在这两种情况下，结果都是相同的。因为PC提供了很多灵活性，BIOS必须确定要使用哪个设备来引导系统。

当找到一个引导设备之后，第一阶段的引导加载程序就被装入RAM并执行。这个引导加载程序的大小小于512字节(一个扇区)，其作用是加载第二阶段引导加载程序。

当第二阶段引导加载程序被装入RAM并执行时，通常会显示一个动画界面，并将Linux和一个可选的初始RAM磁盘(临时根文件系统)加载到内存中。在加载内核映像时，第二阶段引导加载程序会将控制权交给内核映像，然后内核就可以进行解压和初始化了。在这个阶段中，第二阶段引导加载程序会检测系统硬件、枚举系统连接的硬件设备、安装根设备，然后加载必要的内核模块。完成这些操作之后启动第一个用户空间程序(init，参见4.3.5 init节)，并执行高级系统初始化工作。

这就是 Linux 引导的整个过程。

### 4.3.1 系统启动 (System startup)

系统启动阶段依赖于引导Linux系统上的硬件。

在嵌入式平台中，当系统加电或重置时，会使用一个启动环境。这方面的例子包括U-Boot、RedBoot和Lucent的MicroMonitor。嵌入式平台通常都是与引导监视器搭配销售的。这些程序位于目标硬件上的闪存中的某一段特殊区域，它们提供了将Linux内核映像下载到闪存并继续执行的方法。除了可以存储并引导Linux映像之外，这些引导监视器还执行一定级别的系统测试和硬件初始化过程。在嵌入式平台中，这些引导监视器通常会涉及第一阶段和第二阶段的引导加载程序。

在PC中，引导Linux系统是从BIOS中的地址0xFFFF0处(即接近于1M内存处)开始的。BIOS的第一个步骤是加电自检(POST, Power On Self Test)。POST的工作是对硬件进行检测。BIOS的第二个步骤是进行本地设备的枚举和初始化。给定BIOS功能的不同用法之后，BIOS由两部分组成：POST代码和运行时服务。当POST完成之后，它被从内存中清理了出来，但是BIOS运行时服务依然保留在内存中，目标操作系统可以使用这些服务。要引导一个操作系统，BIOS运行时会按照CMOS的设置中定义的顺序来搜索处于活动状态且可以引导的设备。引导设备可以是软盘、CD-ROM、硬盘上的某个分区、网络上的某个设备，甚至是USB闪存。通常Linux是从硬盘引导的，其中主引导记录(MBR)中包含主引导加载程序(即第一阶段引导加载程序)。MBR是一个512字节大小的扇区，位于磁盘的第一个扇区中(0柱面0磁头1扇区，参见[主引导扇区](#)节)。当MBR被加载到RAM中后，BIOS就会将控制权交给MBR。

**提取MBR的信息**

要查看MBR的内容，使用下面的命令：

```
# dd if=/dev/hda of=mbr.bin bs=512 count=1
# od -xa mbr.bin
```

这个dd命令要以root用户的身份运行，它从/dev/hda(第一个IDE盘)上读取前512个字节的内容，并将其写入mbr.bin文件中。od命令会以十六进制和ASCII码格式打印这个二进制文件的内容。

### 4.3.2 第一阶段引导加载程序 (Stage 1 Bootloader)

MBR中的主引导加载程序(第一阶段引导加载程序)是一个512字节大小的映像，其中包含程序代码和硬盘分区表(参见[主引导扇区](#)节)。前446字节是主引导加载程序，其中包含可执行代码和错误消息文本。接下来的64字节是硬盘分区表，其中包含4个分区的记录(每个记录的大小是16字节)。MBR以两个特殊字节(0x55AA)结束，该数字会用来检查MBR的有效性。

主引导加载程序用于查找并加载次引导加载程序(第二阶段引导加载程序)。它是通过在硬盘分区表中查找一个活动分区来实现这种功能的。当找到一个活动分区时，它会扫描分区表中的其他分区，以确保它们都不是活动的。当这个过程验证完成之后，就将该活动分区的引导记录从这个设备中读入RAM中并执行它。

### 4.3.3 第二阶段引导加载程序 (Stage 2 Bootloader)

次引导加载程序(第二阶段引导加载程序)被形象地称为内核加载程序。这个阶段的任务是加载Linux内核和可选的初始RAM磁盘。

在x86 PC环境中，第一阶段引导加载程序和第二阶段引导加载程序一起被称为GRand Unified Bootloader (GRUB，参见[GRUB Legacy](#)节和[GNU GRUB](#)节)或者Linux Loader (LILO，参见[LILO](#)节)。由于LILO有一些缺点，而GRUB克服了这些缺点(参见[LILO与GRUB的比较](#)节)，因此下面重点关注GRUB。

GRUB包含了有关Linux文件系统的知识。GRUB不像LILO一样使用裸扇区，而是可以从ext2或ext3文件系统中加载Linux内核。它是通过将两阶段的引导加载程序转换成三阶段的引导加载程序来实现这项功能的。阶段1 (MBR)引导阶段1.5的引导加载程序，它可以理解包含Linux内核映像的特殊文件系统。这方面的例子包括reiserfs_stage1_5 (要从Reiser日志文件系统上进行加载)或者e2fs_stage1_5 (要从ext2或ext3文件系统上进行加载)。当阶段1.5的引导加载程序被加载并运行时，阶段2的引导加载程序就可以被加载了。

当阶段2加载之后，GRUB就可以在请求时显示可用内核列表(在/etc/grub.conf中定义，同时还有几个软符号链接/etc/grub/menu.lst和/etc/grub.conf)。我们可以选择内核甚至修改附加内核参数。另外，还可以使用一个命令行的shell对引导过程进行高级手工控制。

将第二阶段引导加载程序加载到内存中之后，就可以对文件系统进行查询了，并将默认的内核映像和initrd映像加载到内存中。当这些映像文件准备好之后，阶段2的引导加载程序就可以调用内核映像了。

**GRUB 阶段引导加载程序**

/boot/grub目录中包含了stage1、stage1.5和stage2引导加载程序，以及很多其他加载程序(例如，CR-ROM使用的是iso9660_stage_1_5)。

### 4.3.4 Kernel v3.2.0

当内核映像被加载到内存中，且第二阶段引导加载程序释放控制权之后，内核阶段就开始了。内核映像并不是一个可执行的内核，而是一个压缩过的内核映像。通常它是一个zImage (压缩映像，小于512KB)或一个bzImage (较大的压缩映像，大于512KB)，它是用gzip压缩的(参见[$(obj)/piggy.o](#)节)。在这个内核映像之前是一个例程，它实现少量硬件设置，并对内核映像中包含的内核进行解压，然后将其放入高端内存中，如果有初始RAM磁盘映像，就会将它移动到内存中，并标明以后使用。然后该例程会调用内核，并开始启动内核引导的过程。

#### 4.3.4.1 内核启动过程中的函数调用关系

由arch/x86/boot/setup.ld中的如下代码：

```
ENTRY(_start)
```

可知，setup.bin (参见[bzImage](#)节)的入口点是_start。GRUB会执行jmp_far(0x20, 0)跳过/boot/vmlinuz-3.2.0-chenwx的前0x200个字节，即跳到vmlinuz实模式代码_start处执行，即arch/x86/boot/header.S中的_start，参见[arch/x86/boot/header.S](#)节。

##### 4.3.4.1.1 arch/x86/boot/header.S

注：几乎header.S中所有的代码都是在准备实模式下的C语言环境。

```
/*
 * header.S从开始到此处(# offset 512, entry point)代码实现的功能和
 * 以前内核中arch/i386/boot/bootsect.S的功能是一样的。
 * header.S中(# offset 512, entry point)之后代码所实现的功能和以前
 * 内核中arch/i386/boot/setup.S的一部分类似，包括：
 *  - 设置setup header参数；
 *  - 设置堆栈；
 *  - 检查setup中的标签；
 *  - 清除BSS段；
 *  - 调用入口函数main()
 */
	# offset 512, entry point

	.globl	_start
_start:
	# Explicitly enter this as bytes, or the assembler
	# tries to generate a 3-byte jump here, which causes
	# everything else to push off to the wrong offset.
	.byte	0xeb		# short (2-byte) jump		// #0200处的第一个字节代表短跳转指令，其中0xeb是该指令代码
	.byte	start_of_setup-1f				// #0201处的一个字节表示跳转距离，从标号1到start_of_setup

/*
 * CAN_USE_HEAP表示本体系架构是否支持堆，其定义于arch/x86/include/asm/bootparam.h:
 * #define CAN_USE_HEAP (1<<7)
 */
CAN_USE_HEAP	= 0x80		# If set, the loader also has set

/*
 * STACK_SIZE定义于arch/x86/boot/boot.h中，取值为512，故堆的大小为512字节
 * _end来自arch/x86/boot/setup.ld，表示整个setup.bin的结尾，
 * 参见Image/zImage (old kernels)节(0x00098000处)和bzImage (modern kernel)节(X+08000)
 */
heap_end_ptr:	.word	_end+STACK_SIZE-512

...
	.section ".entrytext", "ax"
start_of_setup:
#ifdef SAFE_RESET_DISK_CONTROLLER
# Reset the disk controller.
	movw	$0x0000, %ax		# Reset disk controller
	movb	$0x80, %dl			# All disks
	int	$0x13				// 用13号中断重设系统盘的磁盘控制器ax=0x0，dl=0x80
#endif

# Force %es = %ds			// 先强制让附加数据段es的内容等于数据段ds的内容
	movw	%ds, %ax
	movw	%ax, %es
	cld

# Apparently some ancient versions of LILO invoked the kernel with %ss != %ds,
# which happened to work by accident for the old code.  Recalculate the stack
# pointer if %ss is invalid.  Otherwise leave it alone, LOADLIN sets up the
# stack behind its own code, so we can't blindly put it directly past the heap.

	movw	%ss, %dx
	cmpw	%ax, %dx	# %ds == %ss?
	movw	%sp, %dx
	je	2f		# -> assume %sp is reasonably set

	# Invalid %ss, make up a new stack	// 设置实模式下的堆栈，参见bzImage (modern kernel)节
	movw	$_end, %dx					// _end来自arch/x86/boot/setup.ld，表示整个setup.bin的结尾
	testb	$CAN_USE_HEAP, loadflags
	jz	1f
	movw	heap_end_ptr, %dx
1:	addw	$STACK_SIZE, %dx
	jnc	2f
	xorw	%dx, %dx	# Prevent wraparound

// 标号2处的代码将dx中的栈顶地址按双字对齐，即将最低两位清零
2:	# Now %dx should point to the end of our stack space
	andw	$~3, %dx	# dword align (might as well...)
	jnz	3f
	movw	$0xfffc, %dx	# Make sure we're not zero
3:	movw	%ax, %ss
	movzwl	%dx, %esp	# Clear upper half of %esp
	sti			# Now we should have a working stack

# We will have entered with %cs = %ds+0x20, normalize %cs so
# it is on par with the other segments.
	pushw	%ds
	pushw	$6f
	lretw
6:

# Check signature at end of setup
	cmpl	$0x5a5aaa55, setup_sig
	jne	setup_bad

/*
 * 清空setup的bss段(非初始化数据段)，注意bss段和数据段(data段)的区别：
 * bss段存放未初始化的全局变量和静态变量，data段存放初始化后的全局变量和静态变量
 */
# Zero the bss
	movw	$__bss_start, %di
	movw	$_end+3, %cx
	xorl	%eax, %eax
	subw	%di, %cx
	shrw	$2, %cx
	rep; stosl

# Jump to C code (should not return)
	calll	main		// 跳转到arch/x86/boot/main.c中的main()，参见arch/x86/boot/main.c节
```

##### 4.3.4.1.2 arch/x86/boot/main.c

arch/x86/boot/header.S最终调用arch/x86/boot/main.c中的main()函数。在执行main()函数时，系统还处于实模式下，其主要功能是为进入保护模式做准备，涉及初始化计算机中的硬件设备，并为内核程序的执行建立环境。虽然之前BIOS已经初始化了大部分硬件设备，但是Linux并不依赖于BIOS，而是以自己的方式重新初始化硬件设备以增强可移植性和健壮性。

```
void main(void)
{
	/* First, copy the boot header into the "zeropage" */
	copy_boot_params();					// 参见copy_boot_params()节

	/* Initialize the early-boot console */
	console_init();						// 解析内核参数earlyprintk
	if (cmdline_find_option_bool("debug"))
		puts("early console in setup code\n");

	/* End of heap check */
	init_heap();						// 参见init_heap()节

	/* Make sure we have all the proper CPU support */
	if (validate_cpu()) {					// 参见validate_cpu()节
		puts("Unable to boot - please use a kernel appropriate for your CPU.\n");
		die();
	}

	/* Tell the BIOS what CPU mode we intend to run in. */
	set_bios_mode();						// 参见set_bios_mode()节

	/* Detect memory layout */
	// 参见detect_memory()节和检测内存段及其大小/boot_params.e820_map节
	detect_memory();

	/* Set keyboard repeat rate (why?) */
	keyboard_set_repeat();				// 参见keyboard_set_repeat()节

	/* Query MCA information */
	query_mca();						// 参见query_mca()节

	/* Query Intel SpeedStep (IST) information */
	query_ist();						// 参见query_ist()节

	/* Query APM information */
#if defined(CONFIG_APM) || defined(CONFIG_APM_MODULE)
	// 填充boot_params.apm_bios_info，其执行过程与query_ist()类似，参见query_ist()节
	query_apm_bios();
#endif

	/* Query EDD information */
#if defined(CONFIG_EDD) || defined(CONFIG_EDD_MODULE)
	/*
	 * 填充boot_params.eddbuf_entries, boot_params.edd_mbr_sig_buf_entries,
	 * boot_params.eddbuf，其执行过程与query_ist()类似，参见query_edd()节
	 */
	query_edd();
#endif

	/* Set the video mode */
	set_video();						// 参见set_video()节

	/* Do the last things and invoke protected mode */
	go_to_protected_mode();				// 参见go_to_protected_mode()节
}
```

###### 4.3.4.1.2.1 copy_boot_params()

该函数定义于arch/x86/boot/main.c:

```
/*
 * struct boot_params定义于arch/x86/include/asm/bootparam.h
 * 变量boot_params是main.c的全局变量，且未被初始化，故位于bss段。
 * GRUB把vmlinuz加载到内存后，boot_params就位于_bss_start的开始位置。
 * 此后，当启动保护模式的分页功能后，第一个页面就是从它开始的(注：不是从0x0开始)。
 * 故内核注释它为zeropage，即所谓的0号页面，足见变量boot_params的重要性。
 */
struct boot_params boot_params __attribute__((aligned(16)));

static void copy_boot_params(void)
{
	struct old_cmdline {
		u16 cl_magic;
		u16 cl_offset;
	};

	// arch/x86/include/asm/setup.h中OLD_CL_ADDRESS取值为0x020
	const struct old_cmdline * const oldcmd = (const struct old_cmdline *)OLD_CL_ADDRESS;

	// 变量boot_params的大小刚好是一个页面的大小，即4KB
	BUILD_BUG_ON(sizeof boot_params != 4096);
	/*
	 * 将hdr的内容拷贝到全局变量boot_params.hdr中。其中，
	 * hdr是arch/x86/boot/header.S中定义的数据段中的内容
	 * 而boot_params.hdr的类型为struct setup_header
	 * (参见arch/x86/include/asm/bootparam.h)，其定义与
	 * arch/x86/boot/header.S中hdr段的定义相同，故可以使用memcpy()拷贝
	 */
	memcpy(&boot_params.hdr, &hdr, sizeof hdr);

	// arch/x86/include/asm/setup.h中OLD_CL_MAGIC取值为0xA33F
	if (!boot_params.hdr.cmd_line_ptr && oldcmd->cl_magic == OLD_CL_MAGIC) {
		/* Old-style command line protocol. */
		u16 cmdline_seg;

		/* Figure out if the command line falls in the region
		   of memory that an old kernel would have copied up
		   to 0x90000... */
		if (oldcmd->cl_offset < boot_params.hdr.setup_move_size)
			cmdline_seg = ds();
		else
			cmdline_seg = 0x9000;

		// 针对旧内核，调整boot_params.hdr.cmd_line_ptr字段的取值
		boot_params.hdr.cmd_line_ptr = (cmdline_seg << 4) + oldcmd->cl_offset;
	}
}
```

###### 4.3.4.1.2.2 init_heap()

该函数用来检查内核初始化阶段使用的堆，其定义于arch/x86/boot/main.c:

```
static void init_heap(void)
{
	char *stack_end;

	if (boot_params.hdr.loadflags & CAN_USE_HEAP) {
		asm("leal %P1(%%esp),%0" : "=r" (stack_end) : "i" (-STACK_SIZE));

		// heap_end_ptr参见arch/x86/boot/header.S节，堆栈大小为512字节
		heap_end = (char *) ((size_t)boot_params.hdr.heap_end_ptr + 0x200);
		// 检查堆的大小，不能溢出，否则就调整到stack_end
		if (heap_end > stack_end)
			heap_end = stack_end;
	} else {
		/* Boot protocol 2.00 only, no heap available */
		puts("WARNING: Ancient bootloader, some functionality may be limited!\n");
	}
}

4.3.4.1.2.3 validate_cpu()

该函数定义于arch/x86/boot/cpu.c:
int validate_cpu(void)
{
	u32 *err_flags;
	int cpu_level, req_level;
	const unsigned char *msg_strs;

	/*
	 * 通过调用arch/x86/boot/cpucheck.c中的check_cpu()函数读取CPU信息，
	 * 并将其存放在如下变量中：
	 *   cpu_level - 表示系统实际的CPU版本
	 *   req_level - 表示运行本内核所需要的CPU最低版本
	 * 若cpu_level < req_level，则报错
	 */
	check_cpu(&cpu_level, &req_level, &err_flags);

	if (cpu_level < req_level) {
		printf("This kernel requires an %s CPU, ", cpu_name(req_level));
		printf("but only detected an %s CPU.\n", cpu_name(cpu_level));
		return -1;
	}

	if (err_flags) {
		int i, j;
		puts("This kernel requires the following features not present on the CPU:\n");

		msg_strs = (const unsigned char *)x86_cap_strs;

		for (i = 0; i < NCAPINTS; i++) {
			u32 e = err_flags[i];

			for (j = 0; j < 32; j++) {
				if (msg_strs[0] < i || (msg_strs[0] == i && msg_strs[1] < j)) {
					/* Skip to the next string */
					msg_strs += 2;
					while (*msg_strs++)
						;
				}
				if (e & 1) {
					if (msg_strs[0] == i && msg_strs[1] == j && msg_strs[2])
						printf("%s ", msg_strs+2);
					else
						printf("%d:%d ", i, j);
				}
				e >>= 1;
			}
		}
		putchar('\n');
		return -1;
	} else {
		return 0;
	}
}
```

###### 4.3.4.1.2.4 set_bios_mode()

该函数定义于arch/x86/boot/main.c:

```
/*
 * Tell the BIOS what CPU mode we intend to run in.
 */
static void set_bios_mode(void)
{
#ifdef CONFIG_X86_64
	struct biosregs ireg;

	initregs(&ireg);
	ireg.ax = 0xec00;
	ireg.bx = 2;
	/*
	 * intcall是初始化阶段的中断处理函数，此处调用0x15中断，并将BIOS的寄存器设置成ireg变量的值。
	 * 注：初始化阶段至此，仍处于实模式阶段，Linux内核的中断系统还没有被初始化，该函数是内核编译后临时
	 * 生成的一个BIOS服务程序，跟arch/x86/boot/header.S中的那些int指令的效果是一样的
	 */
	intcall(0x15, &ireg, NULL);
#endif
}
```

###### 4.3.4.1.2.5 detect_memory()

该函数根据物理内存的类型探测内存布局，其定义于arch/x86/boot/memory.c:

```
int detect_memory(void)
{
	int err = -1;

	// 填充boot_params.e820_entries和boot_params.e820_map，参见detect_memory_e820()节
	if (detect_memory_e820() > 0)
		err = 0;

	// 填充boot_params.alt_mem_k
	if (!detect_memory_e801())
		err = 0;

	// 填充boot_params.screen_info.ext_mem_k
	if (!detect_memory_88())
		err = 0;

	return err;
}
```

###### 4.3.4.1.2.5.1 detect_memory_e820()

该函数定义于arch/x86/boot/memory.c，另参见检测内存段及其大小/boot_params.e820_map节：

```
static int detect_memory_e820(void)
{
	int count = 0;
	struct biosregs ireg, oreg;
	// 此时，boot_params.e820_map是一个空数组，本函数用于初始化该数组
	struct e820entry *desc = boot_params.e820_map;
	static struct e820entry buf; /* static so it is zeroed */

	initregs(&ireg);
	ireg.ax  = 0xe820;
	ireg.cx  = sizeof buf;
	ireg.edx = SMAP;
	ireg.di  = (size_t)&buf;

	do {
		/*
		 * int 0x15中断查询物理内存时，每次返回一个内存段的信息，
		 * 因此要想返回系统中所有的物理内存信息，必须以循环的方式查询
		 */
		intcall(0x15, &ireg, &oreg);
		ireg.ebx = oreg.ebx; /* for next iteration... */

		/* BIOSes which terminate the chain with CF = 1 as opposed
		   to %ebx = 0 don't always report the SMAP signature on
		   the final, failing, probe. */
		if (oreg.eflags & X86_EFLAGS_CF)
			break;

		/* Some BIOSes stop returning SMAP in the middle of
		   the search loop.  We don't know exactly how the BIOS
		   screwed up the map at that point, we might have a
		   partial map, the full map, or complete garbage, so
		   just return failure. */
		if (oreg.eax != SMAP) {
			count = 0;
			break;
		}

		*desc++ = buf;
		count++;
	/*
	 * boot_params.e820_map数组的最大下标为E820MAX，取值为128，
	 * 参见arch/x86/include/asm/e820.h
	 */
	} while (ireg.ebx && count < ARRAY_SIZE(boot_params.e820_map));

	// 返回检测到的物理内存段的个数
	return boot_params.e820_entries = count;
}
```

###### 4.3.4.1.2.6 keyboard_set_repeat()

该函数定义于arch/x86/boot/main.c:

```
/*
 * Set the keyboard repeat rate to maximum.  Unclear why this
 * is done here; this might be possible to kill off as stale code.
 */
static void keyboard_set_repeat(void)
{
	struct biosregs ireg;
	initregs(&ireg);
	ireg.ax = 0x0305;
	// 调用int 0x16中断，设置键盘的重复延时和速率
	intcall(0x16, &ireg, NULL);
}
```

###### 4.3.4.1.2.7 query_mca()

该函数定义于arch/x86/boot/mca.c:

```
int query_mca(void)
{
	struct biosregs ireg, oreg;
	u16 len;

	initregs(&ireg);
	ireg.ah = 0xc0;
	// 调用BIOS的int 0x15中断，读取系统环境配置表信息
	intcall(0x15, &ireg, &oreg);

	if (oreg.eflags & X86_EFLAGS_CF)
		return -1;	/* No MCA present */

	set_fs(oreg.es);
	len = rdfs16(oreg.bx);

	if (len > sizeof(boot_params.sys_desc_table))
		len = sizeof(boot_params.sys_desc_table);

	// 将系统环境配置表信息保存到boot_params.sys_desc_table中
	copy_from_fs(&boot_params.sys_desc_table, oreg.bx, len);
	return 0;
}
```

###### 4.3.4.1.2.8 query_ist()

该函数定义于arch/x86/boot/main.c:

```
/*
 * Get Intel SpeedStep (IST) information.
 */
static void query_ist(void)
{
	struct biosregs ireg, oreg;

	/* Some older BIOSes apparently crash on this call, so filter
	   it from machines too old to have SpeedStep at all. */
	if (cpu.level < 6)
		return;

	initregs(&ireg);
	ireg.ax  = 0xe980;		/* IST Support */
	ireg.edx = 0x47534943;	/* Request value */
	// 调用BIOS的int 0x15中断，查询IST信息，并将其保存到boot_params.ist_info中
	intcall(0x15, &ireg, &oreg);

	boot_params.ist_info.signature  = oreg.eax;
	boot_params.ist_info.command    = oreg.ebx;
	boot_params.ist_info.event      = oreg.ecx;
	boot_params.ist_info.perf_level = oreg.edx;
}
```

###### 4.3.4.1.2.9 query_edd()

该函数定义于arch/x86/boot/edd.c:

```
void query_edd(void)
{
	char eddarg[8];
	int do_mbr = 1;
#ifdef CONFIG_EDD_OFF
	int do_edd = 0;
#else
	int do_edd = 1;
#endif
	int be_quiet;
	int devno;
	struct edd_info ei, *edp;
	u32 *mbrptr;

	if (cmdline_find_option("edd", eddarg, sizeof eddarg) > 0) {
		if (!strcmp(eddarg, "skipmbr") || !strcmp(eddarg, "skip")) {
			do_edd = 1;
			do_mbr = 0;
		}
		else if (!strcmp(eddarg, "off"))
			do_edd = 0;
		else if (!strcmp(eddarg, "on"))
			do_edd = 1;
	}

	be_quiet = cmdline_find_option_bool("quiet");

	edp     = boot_params.eddbuf;
	mbrptr = boot_params.edd_mbr_sig_buffer;

	if (!do_edd)
		return;

	/* Bugs in OnBoard or AddOnCards Bios may hang the EDD probe,
	 * so give a hint if this happens.
	 */

	if (!be_quiet)
		printf("Probing EDD (edd=off to disable)... ");

	for (devno = 0x80; devno < 0x80+EDD_MBR_SIG_MAX; devno++) {
		/*
		 * Scan the BIOS-supported hard disks and query EDD
		 * information...
		 */
		if (!get_edd_info(devno, &ei) && boot_params.eddbuf_entries < EDDMAXNR) {
			memcpy(edp, &ei, sizeof ei);
			edp++;
			boot_params.eddbuf_entries++;
		}

		if (do_mbr && !read_mbr_sig(devno, &ei, mbrptr++))
			boot_params.edd_mbr_sig_buf_entries = devno-0x80+1;
	}

	if (!be_quiet)
		printf("ok\n");
}
```

###### 4.3.4.1.2.10 set_video()

该函数定义于arch/x86/boot/video.c:

```
void set_video(void)
{
	// vid_mode定义于arch/x86/boot/header.S，其取值为SVGA_MODE
	u16 mode = boot_params.hdr.vid_mode;

	// 重新设置堆的位置，把它设定到_end处，参见arch/x86/boot/header.S节
	RESET_HEAP();

	store_mode_params();	// 利用BIOS的显示服务程序对视频显示进行设置，保存到boot_params.screen_info
	save_screen();		// 将当前屏幕的内容存储到指定的内存空间中
	probe_cards(0);		// 扫描显卡

	for (;;) {
		if (mode == ASK_VGA)
			mode = mode_menu();

		if (!set_mode(mode))
			break;

		printf("Undefined video mode number: %x\n", mode);
		mode = ASK_VGA;
	}
	boot_params.hdr.vid_mode = mode;
	vesa_store_edid();
	/*
	 * 设置EDID。EDID是一种VESA标准数据格式，其中包含有关监视器及其性能的参数，
	 * 包括供应商信息、最大图像大小、颜色设置、厂商预设置、频率范围的限制以及显示器
	 * 名和序列号的字符串
	 */
	store_mode_params();

	/*
	 * 根据是否进入mode_menu()设置了do_restore来恢复刚刚被保存的screen_info信息，
	 * 它与save_screen()正好相反
	 */
	if (do_restore)
		restore_screen();
}
```

###### 4.3.4.1.2.11 go_to_protected_mode()

当main()函数执行到go_to_protected_mode()时，系统就即将告别实模式环境，进入保护模式了。保护模式(Protected Mode，或简写为pmode)是一种80286系列及之后的x86兼容CPU操作模式。保护模式有一些新的特色，设计用来增强多功能和系统稳定度，像是内存保护，分页系统，以及硬件支持的虚拟内存。现今大部分的x86操作系统都在保护模式下运行，包含Linux、FreeBSD、微软Windows 2.0及之后版本。

注意：在执行go_to_protected_mode()时，系统还处于实模式下，只不过是进入与保护模式相关的代码。

该函数定义于arch/x86/boot/pm.c:

```
/*
 * Actual invocation sequence
 */
void go_to_protected_mode(void)
{
	/* Hook before leaving real mode, also disables interrupts.
	 * 若boot_params.hdr.realmode_swtch被设置，则执行该函数，否则，关中断(NMI)
	 * 由arch/x86/boot/header.S可知，该字段未被设置：
	 * realmode_swtch:	.word	0, 0
	 */
	realmode_switch_hook();

	/* Enable the A20 gate */
	if (enable_a20()) {			// 参见enable_a20()节
		puts("A20 gate not responding, unable to boot...\n");
		die();
	}

	/* Reset coprocessor (IGNNE#) */
	reset_coprocessor();

	/* Mask all interrupts in the PIC */
	mask_all_interrupts();

	/* Actual transition to protected mode... */
	setup_idt();
	setup_gdt();
	/*
	 * 函数protected_mode_jump()参见protected_mode_jump()节，该函数需要两个入参：
	 * 1) 第一个入参：boot_params.hdr.code32_start，定义于arch/x86/boot/header.S，
	 *    取值为0x100000，由bzImage (modern kernel)节的图可知，该参数表示进入保护模式后
	 *    执行的第一条内核代码(Protected-mode kernel)；
	 * 2) 第二个入参：&boot_params+(ds()<<4)是传递给内核的参数，为0号页面的地址，
	 *    即变量boot_params，参见copy_boot_params()节
	 */
	protected_mode_jump(boot_params.hdr.code32_start, (u32)&boot_params + (ds() << 4));
}
```

###### 4.3.4.1.2.11.1 enable_a20()

PC及其兼容机的第21根地址线(A20)较特殊，PC中安排了一个“门”来控制该地址线是否有效。到了80286，系统的地址总线有原来的20根发展到24根，这样能够访问的内存可以达到224=16MB。Intel在设计80286时提出的目标是向下兼容，所以在实模式下，系统所表现的行为应该和8086/8088所表现的行为完全一样，也就是说，在实模式下，80286及其后续系列，应该和8086/8088完全兼容。但80286芯片却存在一个BUG：因为80286有了A20线，如果程序员访问100000H-10FFEFH之间的内存，系统将实际访问这块内存，而不是像8086/8088那样从0开始。如下图所示：

为了解决上述兼容性问题，IBM使用键盘控制器上剩余的一些输出线来管理第21根地址线(从0开始数是第20根)的有效性，被称为A20 Gate：

1) 如果A20 Gate被打开，则当程序员给出100000H-10FFEFH之间的地址时，系统将真正访问这块内存区域；

2) 如果A20 Gate被关闭，则当程序员给出100000H-10FFEFH之间的地址时，系统仍然使用8086/8088的方式，即取模方式(8086仿真)。绝大多数IBM PC兼容机默认A20 Gate是被关闭的。现在许多新型PC上存在直接通过BIOS功能调用来控制A20 Gate的功能。

上述的内存访问模式都是实模式，在80286以及更高系列的PC中，即使A20 Gate被打开，在实模式下所能够访问的内存最大也只能为10FFEFH，尽管它们的地址总线所能够访问的能力都大大超过这个限制。为了能够访问10FFEFH以上的内存，则必须进入保护模式。

enable_a20()就是用来打开A20 Gate的，参见arch/x86/boot/a20.c。

###### 4.3.4.1.2.11.2 protected_mode_jump()

该函数定义于arch/x86/boot/pmjump.S:

```
	.text
	.code16

/*
 * void protected_mode_jump(u32 entrypoint, u32 bootparams);
 */
GLOBAL(protected_mode_jump)
	movl	%edx, %esi		# Pointer to boot_params table

	xorl	%ebx, %ebx
	movw	%cs, %bx
	shll	$4, %ebx
	addl	%ebx, 2f
	jmp	1f				# Short jump to serialize on 386/486
1:

	movw	$__BOOT_DS, %cx
	movw	$__BOOT_TSS, %di

	movl	%cr0, %edx
	// 执行完本行代码后，内核从此告别实模式，开始了内核的保护模式
	orb	$X86_CR0_PE, %dl		# Protected mode
	movl	%edx, %cr0

	# Transition to 32-bit mode
	.byte	0x66, 0xea		# ljmpl opcode
2:	.long	in_pm32			# offset		// 开始执行in_pm32函数
	.word	__BOOT_CS			# segment
ENDPROC(protected_mode_jump)


	.code32
	.section ".text32","ax"
GLOBAL(in_pm32)
	# Set up data segments for flat 32-bit mode
	movl	%ecx, %ds
	movl	%ecx, %es
	movl	%ecx, %fs
	movl	%ecx, %gs
	movl	%ecx, %ss
	# The 32-bit code sets up its own stack, but this way we do have
	# a valid stack if some debugging hack wants to use it.
	addl	%ebx, %esp

	# Set up TR to make Intel VT happy
	ltr	%di

	# Clear registers to allow for future extensions to the
	# 32-bit boot protocol
	xorl	%ecx, %ecx
	xorl	%edx, %edx
	xorl	%ebx, %ebx
	xorl	%ebp, %ebp
	xorl	%edi, %edi

	# Set up LDTR to make Intel VT happy
	lldt	%cx

	/*
	 * 开始执行由入参传来的boot_params.hdr.code32_start，
	 * 即0x100000处的代码(Protected-mode Kernel)，
	 * 参见bzImage (modern kernel)节；
	 * 在解压vmlinuz之前，这段代码为arch/x86/boot/compressed/head_32.S
	 * 中的函数startup_32，参见arch/x86/boot/compressed/head_32.S节
	 */
	jmpl	*%eax			# Jump to the 32-bit entrypoint
ENDPROC(in_pm32)
```

注意：从系统启动到函数protected_mode_jump()，并不是第一次进入保护模式，在bootloader阶段，GRUB已经执行过一次保护模式的命令了，即把vmlinuz第三部分的代码拷贝到内存0x100000之后。参见[第二阶段引导加载程序 (Stage 2 Bootloader](#)节。

##### 4.3.4.1.3 arch/x86/boot/compressed/head_32.S

由protected_mode_jump()节可知，进入保护模式后执行的第一个函数为arch/x86/boot/compressed/head_32.S中的函数startup_32：

```
	__HEAD
ENTRY(startup_32)
	cld
	/*
	 * Test KEEP_SEGMENTS flag to see if the bootloader is asking
	 * us to not reload segments
	 */
	/*
	 * 参见arch/x86/kernel/asm-offsets.c，BP_loadflags是字段hdr.loadflags相对于
	 * 结构体boot_params首地址的偏移量，因而，BP_loadflags+%esi就是hdr.loadflags的地址
	 */
	testb	$(1<<6), BP_loadflags(%esi)
	jnz	1f

	cli
	// 参见arch/x86/include/asm/segment.h，__BOOT_DS的取值为24
	movl	$__BOOT_DS, %eax
	movl	%eax, %ds
	movl	%eax, %es
	movl	%eax, %fs
	movl	%eax, %gs
	movl	%eax, %ss
1:

/*
 * Calculate the delta between where we were compiled to run
 * at and where we were actually loaded at.  This can only be done
 * with a short local call on x86.  Nothing  else will tell us what
 * address we are running at.  The reserved chunk of the real-mode
 * data at 0x1e4 (defined as a scratch field) are used as the stack
 * for this calculation. Only 4 bytes are needed.
 */
	/*
	 * BP_scratch是字段scratch相对于结构体boot_params首地址的偏移量，
	 * 即让栈顶指向(BP_scratch+4)(%esi)地址lea指令得到boot_params.scratch
	 * 的32位物理地址，并将其存放到esp寄存器中
	 */
	leal	(BP_scratch+4)(%esi), %esp
	call	1f
1:	popl	%ebp
	subl	$1b, %ebp

/*
 * %ebp contains the address we are loaded at by the boot loader and %ebx
 * contains the address where we should move the kernel image temporarily
 * for safe in-place decompression.
 */

#ifdef CONFIG_RELOCATABLE
	movl	%ebp, %ebx
	/*
	 * BP_kernel_alignment是字段hdr.kernel_alignment相对于结构体boot_params首地址的偏移量
	 * 在arch/x86/boot/header.S中，kernel_alignment:  .long CONFIG_PHYSICAL_ALIGN
	 * 又在.config中，CONFIG_PHYSICAL_ALIGN=0x1000000
	 */
	movl	BP_kernel_alignment(%esi), %eax
	decl	%eax
	addl    %eax, %ebx
	notl	%eax
	andl    %eax, %ebx
#else
	// 根据arch/x86/include/asm/boot.h和.config中配置可知，LOAD_PHYSICAL_ADDR取值为0x1000000
	movl	$LOAD_PHYSICAL_ADDR, %ebx
#endif

	/* Target address to relocate to for decompression */
	addl	$z_extract_offset, %ebx

	/* Set up the stack */
	leal	boot_stack_end(%ebx), %esp

	/* Zero EFLAGS */
	pushl	$0
	popfl

/*
 * Copy the compressed kernel to the end of our buffer
 * where decompression in place becomes safe.
 */
	pushl	%esi
	leal	(_bss-4)(%ebp), %esi
	leal	(_bss-4)(%ebx), %edi
	// _bss是解压缩程序的BSS段
	/*
	 * _bss – startup_32涵盖了vmlinuz从startup_32以后的代码长度，
	 * 包括整个待解压内核，然后再右移2位，即除以4
	 */
	movl	$(_bss - startup_32), %ecx
	shrl	$2, %ecx
	// 设置方向标志置位，下一行中的rep是由高地址向低地址进行，
	// 即_bss到当前正在执行的startup_32
	std
	// 把内核映像拷贝到0x1000000以后的内存单元中
	rep	movsl
	cld
	popl	%esi

/*
 * Jump to the relocated address.
 */
	leal	relocated(%ebx), %eax
	/*
	 * 本行之前的代码将原GRUB加载的内核映像(位于0x100000处)拷贝到0x1000000
	 * 之后新的内存单元中。本行代码跳转到拷贝后的内核映像(位于0x1000000之后)中
	 * 的relocated处执行，即离开原GRUB加载的内核映像(位于0x100000处)
	 */
	jmp	*%eax
ENDPROC(startup_32)


.text
relocated:

/*
 * Clear BSS (stack is currently empty)
 */
	xorl	%eax, %eax
	leal	_bss(%ebx), %edi
	leal	_ebss(%ebx), %ecx
	subl	%edi, %ecx
	shrl	$2, %ecx
	rep	stosl

/*
 * Adjust our own GOT
 */
	leal	_got(%ebx), %edx
	leal	_egot(%ebx), %ecx
1:
	cmpl	%ecx, %edx
	jae	2f
	addl	%ebx, (%edx)
	addl	$4, %edx
	jmp	1b
2:

/*
 * Do the decompression, and jump to the new kernel..
 */
	/*
	 * 此段中的下列变量均来自于arch/x86/boot/compressed/mkpiggy.c:
	 * z_extract_offset_negative, z_input_len, input_data
	 * 参见3.4.2.8.5.1.4 $(obj)/piggy.S节
	 */
	leal	z_extract_offset_negative(%ebx), %ebp
						/* push arguments for decompress_kernel: */
	pushl	%ebp				/* output address */		// 解压缩的缓存首地址
	pushl	$z_input_len		/* input_len */			// 待解压缩内核的大小
	leal	input_data(%ebx), %eax
	pushl	%eax				/* input_data */			// 待解压缩内核的开始地址
	leal	boot_heap(%ebx), %eax
	pushl	%eax				/* heap area */			// 解压缩内核所用的堆
	pushl	%esi				/* real mode pointer */	// 表示拷贝内核映像之前的内核映像地址
	/*
	 * 调用arch/x86/boot/compressed/misc.c中的decompress_kernel()解压内核，
	 * 参见decompress_kernel()节
	 */
	call	decompress_kernel
	addl	$20, %esp

#if CONFIG_RELOCATABLE
/*
 * Find the address of the relocations.
 */
	leal	z_output_len(%ebp), %edi

/*
 * Calculate the delta between where vmlinux was compiled to run
 * and where it was actually loaded.
 */
	movl	%ebp, %ebx
	subl	$LOAD_PHYSICAL_ADDR, %ebx
	jz	2f	/* Nothing to be done if loaded at compiled addr. */
/*
 * Process relocations.
 */

1:	subl	$4, %edi
	movl	(%edi), %ecx
	testl	%ecx, %ecx
	jz	2f
	addl	%ebx, -__PAGE_OFFSET(%ebx, %ecx)
	jmp	1b
2:
#endif

/*
 * Jump to the decompressed kernel.
 */
	xorl	%ebx, %ebx
	/*
	 * 开始执行解压后的内核，即第二个startup_32()函数，
	 * 该函数定义于arch/x86/kernel/head_32.S，
	 * 参见arch/x86/kernel/head_32.S节
	 */
	jmp	*%ebp
```

###### 4.3.4.1.3.1 decompress_kernel()

该函数定义于arch/x86/boot/compressed/misc.c:

```
asmlinkage void decompress_kernel(void *rmode, memptr heap, unsigned char *input_data,
						 unsigned long input_len, unsigned char *output)
{
	real_mode = rmode;

	if (cmdline_find_option_bool("quiet"))
		quiet = 1;
	if (cmdline_find_option_bool("debug"))
		debug = 1;

	if (real_mode->screen_info.orig_video_mode == 7) {
		vidmem = (char *) 0xb0000;
		vidport = 0x3b4;
	} else {
		vidmem = (char *) 0xb8000;
		vidport = 0x3d4;
	}

	lines = real_mode->screen_info.orig_video_lines;
	cols = real_mode->screen_info.orig_video_cols;

	console_init();
	if (debug)
		putstr("early console in decompress_kernel\n");

	free_mem_ptr     = heap;	/* Heap */
	free_mem_end_ptr = heap + BOOT_HEAP_SIZE;

	if ((unsigned long)output & (MIN_KERNEL_ALIGN - 1))
		error("Destination address inappropriately aligned");
#ifdef CONFIG_X86_64
	if (heap > 0x3fffffffffffUL)
		error("Destination address too large");
#else
	if (heap > ((-__PAGE_OFFSET-(128<<20)-1) & 0x7fffffff))
		error("Destination address too large");
#endif
#ifndef CONFIG_RELOCATABLE
	if ((unsigned long)output != LOAD_PHYSICAL_ADDR)
		error("Wrong destination address");
#endif

	if (!quiet)
		putstr("\nDecompressing Linux... ");
	// 调用lib/decompress_xxx.c中的同名函数
	decompress(input_data, input_len, NULL, NULL, output, NULL, error);
	parse_elf(output);
	if (!quiet)
		putstr("done.\nBooting the kernel.\n");
	return;
}
```

##### 4.3.4.1.4 arch/x86/kernel/head_32.S

由arch/x86/boot/compressed/head_32.S节可知，解压内核后，执行的第一个函数是arch/x86/kernel/head_32.S中的startup_32()函数。该函数主要是为第一个Linux进程(进程0)建立执行环境，主要执行以下操作：

* 把段寄存器初始化为最终值
* 把内核的bss段填充为0
* 初始化包含在swapper_pg_dir的临时内核页表，并初始化pg0，以使线性地址一致地映射同一物理地址
* 把页全局目录的地址存放在cr3寄存器中，并通过设置cr0寄存器的PG位启用分页
* 把从BIOS中获得的系统参数和传递给操作系统的参数boot_params放入第一个页框中
* 为进程0建立内核态堆栈
* 该函数再一次清零eflags寄存器的所有位
* 调用setup_idt用空的中断处理程序填充中断描述符表IDT
* 识别处理器的型号
* 用编译好的GDT和IDT表的地址来填充gdtr和idtr寄存器
* 初始化虚拟机监视器xen
* 调用start_kernel()函数

函数startup_32()定义于arch/x86/kernel/head_32.S:

```
...
__HEAD
ENTRY(startup_32)
	movl pa(stack_start),%ecx

...
	movl $(__KERNEL_STACK_CANARY),%eax
	movl %eax,%gs

	xorl %eax,%eax			# Clear LDT
	lldt %ax

	cld					# gcc2 wants the direction flag cleared at all times
	pushl $0				# fake return address for unwinder
	movb $1, ready
	jmp *(initial_code)

...
	__REFDATA
.align 4
ENTRY(initial_code)
	.long i386_start_kernel			// 参见386_start_kernel()节

...
.data
.balign 4
ENTRY(stack_start)
	.long init_thread_union+THREAD_SIZE	// 为进程0建立内核态堆栈，参见init_thread_union节
```

###### 4.3.4.1.4.1 init_thread_union

该变量定义于include/linux/sched.h:

```
union thread_union {
	struct thread_info thread_info;				// 0号进程的thread_info
	unsigned long stack[THREAD_SIZE/sizeof(long)];	// THREAD_SIZE的取值为8kB
};

extern union thread_union init_thread_union;

init_thread_union实际定义于arch/x86/kernel/init_task.c中：
union thread_union init_thread_union __init_task_data =
	{ INIT_THREAD_INFO(init_task) };				// 参见arch/x86/include/asm/thread_info.h

struct task_struct init_task = INIT_TASK(init_task);	// 0号进程的task_struct
```

其中的__init_task_data定义于include/linux/init_task.h中：

```
/* Attach to the init_task data structure for proper alignment */
#define __init_task_data __attribute__((__section__(".data..init_task")))
```

###### 4.3.4.1.4.2 i386_start_kernel()

该函数定义于arch/x86/kernel/head32.c:

```
void __init i386_start_kernel(void)
{
	memblock_init();

	memblock_x86_reserve_range(__pa_symbol(&_text), __pa_symbol(&__bss_stop), "TEXT DATA BSS");

#ifdef CONFIG_BLK_DEV_INITRD
	/* Reserve INITRD */
	if (boot_params.hdr.type_of_loader && boot_params.hdr.ramdisk_image) {
		/* Assume only end is not page aligned */
		u64 ramdisk_image = boot_params.hdr.ramdisk_image;
		u64 ramdisk_size  = boot_params.hdr.ramdisk_size;
		u64 ramdisk_end   = PAGE_ALIGN(ramdisk_image + ramdisk_size);
		memblock_x86_reserve_range(ramdisk_image, ramdisk_end, "RAMDISK");
	}
#endif

	/* Call the subarch specific early setup function */
	switch (boot_params.hdr.hardware_subarch) {
	case X86_SUBARCH_MRST:
		x86_mrst_early_setup();
		break;
	case X86_SUBARCH_CE4100:
		x86_ce4100_early_setup();
		break;
	default:
		i386_default_early_setup();
		break;
	}

	/*
	 * At this point everything still needed from the boot loader
	 * or BIOS or kernel text should be early reserved or marked not
	 * RAM in e820. All other memory is free game.
	 */
	start_kernel();		// 参见start_kernel()节
}
```

###### 4.3.4.1.4.3 start_kernel()

As specified in chapter 16 of **Linux Device Drivers, 2nd Edition**:

> The architecture-independent starting point is start_kernel() in init/main.c. This function is invoked from architecture-specific code, to which it never returns.

由[386_start_kernel()](#)节可知，i386_start_kernel()将调用start_kernel()，其定义于init/main.c:

```
asmlinkage void __init start_kernel(void)
{
	char * command_line;
	/*
	 * 在arch/x86/kernel/vmlinux.lds中包含该变量的定义；
	 * 与__initcall_start[], __initcall_end[], __early_initcall_end[]类似，
	 * 参见__initcall_start[], __early_initcall_end[]节
	 */
	extern const struct kernel_param __start___param[], __stop___param[];

	smp_setup_processor_id();

	/*
	 * Need to run as early as possible, to initialize the
	 * lockdep hash:
	 */
	lockdep_init();					// 参见lockdep_init()节
	debug_objects_early_init();			// 参见debug_objects_early_init()节

	/*
	 * Set up the the initial canary ASAP:
	 */
	boot_init_stack_canary();

	cgroup_init_early();

	local_irq_disable();				// 关闭可屏蔽中断，与下文中的local_irq_enable()对应
	early_boot_irqs_disabled = true; 	// 在下文调用local_irq_enable()前将该变量置为false

/*
 * Interrupts are still disabled. Do necessary setups, then
 * enable them
 */

	// 参见Architecture-dependent routine / tick_handle_periodic()节
	tick_init();
	boot_cpu_init();
	page_address_init();
	printk(KERN_NOTICE "%s", linux_banner);
	/*
	 * 该函数与体系架构有关。内核启动命令行参见内核启动命令行节，
	 * 内存初始化参见boot_params.e820_map[]=>e820 / e820_saved节
	 */
	setup_arch(&command_line);
	mm_init_owner(&init_mm, &init_task);	// 与配置项CONFIG_MM_OWNER的取值有关
	mm_init_cpumask(&init_mm);			// 与配置项CONFIG_CPUMASK_OFFSTACK的取值有关
	setup_command_line(command_line);	// 保存命令行参数，以备后续使用，参见内核启动命令行节
	setup_nr_cpu_ids();
	setup_per_cpu_areas();			// 参见Per-CPU Variables的初始化节
	smp_prepare_boot_cpu();	/* arch-specific boot-cpu hooks */

	build_all_zonelists(NULL);
	page_alloc_init();

	// 解析boot_command_line中的内核选项，参见parse_early_param() / parse_args()节
	printk(KERN_NOTICE "Kernel command line: %s\n", boot_command_line);
	parse_early_param();
	parse_args("Booting kernel", static_command_line, __start___param,
				 __stop___param - __start___param, &unknown_bootoption);

	jump_label_init();

	/*
	 * These use large bootmem allocations and must precede
	 * kmem_cache_init(). 参见19.2.1.1.1 默认分配的log_buf节
	 */
	setup_log_buf(0);
	// 初始化PID哈希链表头，参见PID散列表和链表节
	pidhash_init();
	/*
	 * 初始化VFS的两个重要数据结构dcache和inode的缓存，
	 * 参见vfs_caches_init_early()节
	 */
	vfs_caches_init_early();
	/*
	 * sort_main_extable()用于把编译期间kbuild设置的异常表
	 * __start___ex_table和__stop___ex_table中的所有元素排序
	 * 参见include/asm-generic/vmlinux.lds.h和
	 * arch/x86/kernel/vmlinux.lds.S中的宏EXCEPTION_TABLE，
	 * 以及arch/x86/kernel/entry_32.S中的__ex_table
	 */
	sort_main_extable();
	// 初始化中断描述符表idt_table[NR_VECTORS]，参见trap_init()节
	trap_init();
	// 初始化内存管理，参见mm_init()节
	mm_init();

	/*
	 * Set up the scheduler prior starting any interrupts (such as the
	 * timer interrupt). Full topology setup happens at smp_init()
	 * time - but meanwhile we still have a functioning scheduler.
	 */
	sched_init();			// 初始化调度程序，参见sched_init()节
	/*
	 * Disable preemption - early bootup scheduling is extremely
	 * fragile until we cpu_idle() for the first time.
	 */
	preempt_disable();		// 与配置项CONFIG_PREEMPT_COUNT的取值有关，参见preempt_disable()节
	if (!irqs_disabled()) {
		printk(KERN_WARNING "start_kernel(): bug: interrupts were "
				"enabled *very* early, fixing it\n");
		local_irq_disable();
	}
	idr_init_cache();		// 参见idr_init_cache()节
	perf_event_init();		// 与配置项CONFIG_PERF_EVENTS的取值有关
	rcu_init();			// 参见RCU的初始化节
	radix_tree_init();
	/* init some links before init_ISA_irqs() */
	early_irq_init();		// 参见early_irq_init()节
	init_IRQ();			// 参见init_IRQ()节
	prio_tree_init();
	init_timers();			// 参见定时器模块的编译及初始化节
	hrtimers_init();			// 参见hrtimer的编译及初始化节
	softirq_init();			// 初始化软中断的TASKLET_SOFTIRQ和HI_SOFTIRQ，参见softirq_init()节
	timekeeping_init();
	// 初始化系统日期和时间，参见Architecture-dependent routine / tick_handle_periodic()节
	time_init();
	profile_init();			// 与配置项CONFIG_PROFILING的取值有关
	call_function_init();
	if (!irqs_disabled())
		printk(KERN_CRIT "start_kernel(): bug: interrupts were "
				 "enabled early\n");
	early_boot_irqs_disabled = false;
	local_irq_enable();		// 打开可屏蔽中断，与上文中的local_irq_disable()对应

	/* Interrupts are enabled now so all GFP allocations are safe. */
	gfp_allowed_mask = __GFP_BITS_MASK;

	kmem_cache_init_late();

	/*
	 * HACK ALERT! This is early. We're enabling the console before
	 * we've done PCI setups etc, and console_init() must be aware of
	 * this. But we do want output early, in case something goes wrong.
	 */
	/*
	 * 初始化系统控制台结构，该函数执行后可调用printk()函数
	 * 将log_buf中符合打印级别要求的系统信息打印到控制台上
	 */
	console_init();
	if (panic_later)
		/*
		 * 当系统出现无法继续运行下去的故障时才调用函数panic()，
		 * 该函数会导致系统中止，然后显示系统错误号
		 */
		panic(panic_later, panic_param);

	lockdep_info();

	/*
	 * Need to run this when irqs are enabled, because it wants
	 * to self-test [hard/soft]-irqs on/off lock inversion bugs
	 * too:
	 */
	locking_selftest();

#ifdef CONFIG_BLK_DEV_INITRD
	if (initrd_start && !initrd_below_start_ok &&
	    page_to_pfn(virt_to_page((void *)initrd_start)) < min_low_pfn) {
		 printk(KERN_CRIT "initrd overwritten (0x%08lx < 0x%08lx) - disabling it.\n",
		    page_to_pfn(virt_to_page((void *)initrd_start)), min_low_pfn);
		initrd_start = 0;
	}
#endif
	page_cgroup_init();
	enable_debug_pagealloc();
	debug_objects_mem_init();		// 与配置项CONFIG_DEBUG_OBJECTS的取值有关
	kmemleak_init();
	setup_per_cpu_pageset();
	numa_policy_init();
	if (late_time_init)			// 参见Architecture-dependent routine / tick_handle_periodic()节
		late_time_init();
	sched_clock_init();
	calibrate_delay();			// 确定CPU时钟的速度
	pidmap_init();				// 初始化pid_namespace结构的全局变量init_pid_ns
	anon_vma_init();
#ifdef CONFIG_X86
	if (efi_enabled)
		efi_enter_virtual_mode();
#endif
	thread_info_cache_init();
	cred_init();
	fork_init(totalram_pages);
	proc_caches_init();
	buffer_init();				// 初始化页高速缓存
	key_init();
	security_init();				// 初始化LSM，参见LSM的初始化节
	dbg_late_init();
	// 用于初始化VFS数据结构的slab缓存，参见vfs_caches_init()节
	vfs_caches_init(totalram_pages);
	signals_init();				// 建立数据结构sigqueue的slab缓存，参见信号的初始化节
	/* rootfs populating might need page-writeback */
	page_writeback_init();
#ifdef CONFIG_PROC_FS
	proc_root_init();			// 初始化proc文件系统，参见proc_root_init()节
#endif
	cgroup_init();
	cpuset_init();
	taskstats_init_early();
	delayacct_init();

	check_bugs();

	// 初始化高级配置和电源管理接口ACPI(Advanced Configuration and Power Interface)
	acpi_early_init(); /* before LAPIC and SMP init */
	sfi_init_late();

	ftrace_init();				// 与配置项CONFIG_FTRACE_MCOUNT_RECORD的取值有关

	/* Do the rest non-__init'ed, we're now alive */
	rest_init();				// 参见rest_init()节
}
```

###### 4.3.4.1.4.3.1 lockdep_init()

该函数定义于kernel/lockdep.c：

```
void lockdep_init(void)
{
	int i;

	/*
	 * Some architectures have their own start_kernel()
	 * code which calls lockdep_init(), while we also
	 * call lockdep_init() from the start_kernel() itself,
	 * and we want to initialize the hashes only once:
	 */
	if (lockdep_initialized)
		return;

	for (i = 0; i < CLASSHASH_SIZE; i++)		// CLASSHASH_SIZE取值为4096
		INIT_LIST_HEAD(classhash_table + i);	// 初始化散列表classhash_table[CLASSHASH_SIZE]

	for (i = 0; i < CHAINHASH_SIZE; i++)		// CHAINHASH_SIZE取值为16384
		INIT_LIST_HEAD(chainhash_table + i);	// 初始化散列表chainhash_table[CHAINHASH_SIZE]

	lockdep_initialized = 1;
}
```

###### 4.3.4.1.4.3.2 debug_objects_early_init()

由lib/Makefile中的如下规则：

```
obj-$(CONFIG_DEBUG_OBJECTS) += debugobjects.o
```

可知，debugobjects.c的编译与.config中的配置项CONFIG_DEBUG_OBJECTS有关。

如果CONFIG_DEBUG_OBJECTS=y，则在lib/debugobjects.c中，包含如下有关debug_object_early_init()的代码：

```
void __init debug_objects_early_init(void)
{
	int i;

	for (i = 0; i < ODEBUG_HASH_SIZE; i++)       // ODEBUG_HASH_SIZE的取值为16384
		raw_spin_lock_init(&obj_hash[i].lock);

	for (i = 0; i < ODEBUG_POOL_SIZE; i++)       // ODEBUG_POOL_SIZE的取值为512
		hlist_add_head(&obj_static_pool[i].node, &obj_pool);
}
```

如果CONFIG_DEBUG_OBJECTS=n，则在include/linux/debugobjects.h中，debug_object_early_init()被定义为空函数：

```
static inline void debug_objects_early_init(void) { }
```

###### 4.3.4.1.4.3.3 parse_early_param() / parse_args()

###### 4.3.4.1.4.3.3.1 内核启动命令行

在启动内核时，可以传递一个命令行字符串(即内核参数及其取值)，来控制内核启动的过程，例如：

```
BOOT_IMAGE=/boot/vmlinuz-3.5.0-17-generic root=UUID=61b86fe4-41d9-4de3-a204-f64bf26eb02d ro quiet splash vt.handoff=7
```

可通过下列命令查看内核启动命令行：

```
chenwx proc # cat /proc/cmdline
BOOT_IMAGE=/boot/vmlinuz-3.15.0-eudyptula-00054-g783e9e8-dirty root=UUID=fe67c2d0-9b0f-4fd6-8e97-463ce95a7e0c ro quiet splash
```

在内核启动过程中，涉及到如下几个命令行字符串变量：

* builtin_cmdline
* boot_command_line
* saved_command_line
* command_line
* static_command_line

最初，在引导内核启动时，boot_command_line是由boot_loader传递给内核的，参见arch/x86/kernel/head_32.S中的函数ENTRY(startup_32)。此后，在如下函数调用中：

```
start_kernel()
-> setup_arch(&command_line)			// 参见init/main.c
-> setup_command_line(command_line)		// 参见init/main.c
```

根据编译条件的不同，boot_command_line的取值可能会发生变化，并将boot_command_line赋值给其他变量，参见:

![boot_command_line](/assets/boot_command_line.jpg)

###### 4.3.4.1.4.3.3.1.1 boot_command_line的配置方式

上文中的变量boot_command_line可以由如下两种方式配置：

1) 通过LILO或GRUB等引导加载程序进行配置(参见[配置引导加载程序GRUB(或LILO](#)节)。例如/boot/grub/grub.cfg中包含如下内容：

```
...
menuentry 'Linux Mint 14 MATE 32-bit, 3.5.0-17-generic (/dev/sda1)' --class linuxmint --class gnu-linux --class gnu --class os {
	recordfail
	gfxmode $linux_gfx_mode
	insmod gzio
	insmod part_msdos
	insmod ext2
	set root='hd0,msdos1'
	if [ x$feature_platform_search_hint = xy ]; then
	  search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1  61b86fe4-41d9-4de3-a204-f64bf26eb02d
	else
	  search --no-floppy --fs-uuid --set=root 61b86fe4-41d9-4de3-a204-f64bf26eb02d
	fi
	linux	/boot/vmlinuz-3.5.0-17-generic root=UUID=61b86fe4-41d9-4de3-a204-f64bf26eb02d ro   quiet splash $vt_handoff
	initrd	/boot/initrd.img-3.5.0-17-generic
}
menuentry 'Linux Mint 14 MATE 32-bit, 3.5.0-17-generic (/dev/sda1) -- recovery mode' --class linuxmint --class gnu-linux --class gnu --class os {
	recordfail
	insmod gzio
	insmod part_msdos
	insmod ext2
	set root='hd0,msdos1'
	if [ x$feature_platform_search_hint = xy ]; then
	  search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1  61b86fe4-41d9-4de3-a204-f64bf26eb02d
	else
	  search --no-floppy --fs-uuid --set=root 61b86fe4-41d9-4de3-a204-f64bf26eb02d
	fi
	echo	'Loading Linux 3.5.0-17-generic ...'
	linux	/boot/vmlinuz-3.5.0-17-generic root=UUID=61b86fe4-41d9-4de3-a204-f64bf26eb02d ro recovery nomodeset
	echo	'Loading initial ramdisk ...'
	initrd	/boot/initrd.img-3.5.0-17-generic
}
...
```

2) 在配置内核(make \*config)时，通过如下选项配置内核参数。这些内核参数被静态的编译进内核，此后通过变量builtin_cmdline访问，参见arch/x86/kernel/setup.c中的setup_arch()函数：

```
Processor type and features
[*] Built-in kernel command line							=> CONFIG_CMDLINE_BOOL
()    Built-in kernel command string						=> CONFIG_CMDLINE
[ ]   Built-in command line overrides boot loader arguments		=> CONFIG_CMDLINE_OVERRIDE
```

###### 4.3.4.1.4.3.3.2 注册内核参数的处理函数

内核参数的处理函数被放置到.init.setup段或__param段，分别由宏early_param()/\_\_setup()和\_\_module_param_call()来完成。参见如下文档：

* Documentation/kernel-parameters.txt
* Documentation/sysctl/kernel.txt

###### 4.3.4.1.4.3.3.2.1 early_param()/\_\_setup()

宏early_param()和__setup()用于注册内核参数的处理函数，这些处理函数被放置到.init.setup段，参见include/linux/init.h:

```
struct obs_kernel_param {
	const char *str;				// 内核参数名
	int (*setup_func)(char *);		// 内核参数的处理函数
	int early;					// 是否为宏early_param注册的
};

#define __setup(str, fn)								\
	__setup_param(str, fn, fn, 0)

#define early_param(str, fn)							\
	__setup_param(str, fn, fn, 1)

#define __setup_param(str, unique_id, fn, early)				\
	static const char __setup_str_##unique_id[] __initconst	\
		__aligned(1) = str; 							\
	static struct obs_kernel_param __setup_##unique_id		\
		__used __section(.init.setup)					\
		__attribute__((aligned((sizeof(long)))))			\
		= { __setup_str_##unique_id, fn, early }
```

这两个宏定义并初始化了类型为struct obs_kernel_param的对象，它被编译到.init.setup段。根据vmlinux.lds如何生成节，arch/x86/kernel/vmlinux.lds.S被扩展为vmliux.lds(详见错误：引用源未找到)，其中，.init.setup段包含如下内容：

```
.init.data : AT(ADDR(.init.data) - 0xC0000000) { *(.init.data) *(.cpuinit.data) *(.meminit.data) . = ALIGN(8); __ctors_start = .; *(.ctors) __ctors_end = .; *(.init.rodata) . = ALIGN(8); __start_ftrace_events = .; *(_ftrace_events) __stop_ftrace_events = .; *(.cpuinit.rodata) *(.meminit.rodata) . = ALIGN(32); __dtb_start = .; *(.dtb.init.rodata) __dtb_end = .; . = ALIGN(16); __setup_start = .; *(.init.setup) __setup_end = .; __initcall_start = .; *(.initcallearly.init) __early_initcall_end = .; *(.initcall0.init) *(.initcall0s.init) *(.initcall1.init) *(.initcall1s.init) *(.initcall2.init) *(.initcall2s.init) *(.initcall3.init) *(.initcall3s.init) *(.initcall4.init) *(.initcall4s.init) *(.initcall5.init) *(.initcall5s.init) *(.initcallrootfs.init) *(.initcall6.init) *(.initcall6s.init) *(.initcall7.init) *(.initcall7s.init) __initcall_end = .; __con_initcall_start = .; *(.con_initcall.init) __con_initcall_end = .; __security_initcall_start = .; *(.security_initcall.init) __security_initcall_end = .; }
```

因而，可通过__setup_start和__setup_end查询内核参数并调用其处理函数。

注：early_param()与__setup()的不同之处在于，early_param()注册的内核参数必须在其他内核参数之前被处理。以参数foo及处理函数foo_func()为例，这两个宏的扩展结果如下：

* early_param("foo", foo_func)

```
static const char __setup_str_foo_func[] __initconst __aligned(1) = "foo";
static struct obs_kernel_param __setup_foo_func
	__used __section(.init.setup) __attribute__((aligned((sizeof(long)))))
	= { __setup_str_foo_func, foo_func, 1 }
```

* \_\_setup("foo", foo_func)

```
static const char __setup_str_foo_func[] __initconst __aligned(1) = "foo";
static struct obs_kernel_param __setup_foo_func
	__used __section(.init.setup) __attribute__((aligned((sizeof(long)))))
	= { __setup_str_foo_func, foo_func, 0 }
```

在init/main.c中，包含如下定义：

```
early_param("debug", debug_kernel);
early_param("quiet", quiet_kernel);
early_param("loglevel", loglevel);

__setup("reset_devices", set_reset_devices);
__setup("init=", init_setup);
__setup("rdinit=", rdinit_setup);
```

###### 4.3.4.1.4.3.3.2.2 \_\_module_param_call()

宏__module_param_call()用于注册内核参数的处理函数，这些处理函数被放置到__param段，其定义于include/linux/moduleparam.h:

```
struct kernel_param {
	const char *name;
	const struct kernel_param_ops *ops;
	u16 perm;
	u16 flags;
	union {
		void *arg;
		const struct kparam_string *str;
		const struct kparam_array *arr;
	};
};

/* This is the fundamental function for registering boot/module parameters. */
#define __module_param_call(prefix, name, ops, arg, isbool, perm)				\
	/* Default value instead of permissions? */							\
	static int __param_perm_check_##name __attribute__((unused)) =			\
	BUILD_BUG_ON_ZERO((perm) < 0 || (perm) > 0777 || ((perm) & 2))			\
	+ BUILD_BUG_ON_ZERO(sizeof(""prefix) > MAX_PARAM_PREFIX_LEN);			\
	static const char __param_str_##name[] = prefix #name;					\
	static struct kernel_param __moduleparam_const __param_##name			\
	__used													\
	__attribute__ ((unused,__section__ ("__param"),aligned(sizeof(void *))))	\
	= { __param_str_##name, ops, perm, isbool ? KPARAM_ISBOOL : 0,	{ arg } }
```

该宏定义并初始化了类型为struct kernel_param的对象，它被编译到__param段。根据vmlinux.lds如何生成节，arch/x86/kernel/vmlinux.lds.S被扩展为vmliux.lds(详见错误：引用源未找到)，其中包含如下内容：

```
__param : AT(ADDR(__param) - 0xC0000000) { __start___param = .; *(__param) __stop___param = .; }
```

因而可以通过__start___param和__stop___param查询内核参数并调用其处理函数。

使用__module_param_call()的宏，参见[13.1.3.1 与模块参数有关的宏](#)节。

###### 4.3.4.1.4.3.3.3 内核参数处理函数的调用过程

函数start_kernel()调用parse_early_param()和parse_args()来分别处理early_param()和__setup()注册的内核参数处理函数：

```
asmlinkage void __init start_kernel(void)
{
	...
	printk(KERN_NOTICE "Kernel command line: %s\n", boot_command_line);
	/*
	 * 解析命令行boot_command_line中的内核参数，并在.init.setup段
	 * 查找其处理函数，参见parse_early_param()节
	 */
	parse_early_param();
	/*
	 * 解析命令行static_command_line中的内核参数，并在__param段或
	 * .init.setup段查找其处理函数，参见parse_args()节
	 */
	parse_args("Booting kernel", static_command_line, __start___param,
			__stop___param - __start___param, &unknown_bootoption);
	...
}
```

###### 4.3.4.1.4.3.3.3.1 parse_early_param()

该函数定义于init/main.c:

```
/* Arch code calls this early on, or if not, just before other parsing. */
void __init parse_early_param(void)
{
	static __initdata int done = 0;
	static __initdata char tmp_cmdline[COMMAND_LINE_SIZE];

	if (done)
		return;

	// 解析命令行boot_command_line中的内核参数
	/* All fall through to do_early_param. */
	strlcpy(tmp_cmdline, boot_command_line, COMMAND_LINE_SIZE);
	parse_early_options(tmp_cmdline);
	done = 1;
}

void __init parse_early_options(char *cmdline)
{
	// 函数do_early_param()参见下文
	parse_args("early options", cmdline, NULL, 0, do_early_param);
}
```

其中，函数parse_args()定义于kernel/params.c:

```
/* Args looks like "foo=bar,bar2 baz=fuz wiz". */
int parse_args(const char *name, char *args,
	       const struct kernel_param *params, unsigned num,
	       int (*unknown)(char *param, char *val))
{
	char *param, *val;

	DEBUGP("Parsing ARGS: %s\n", args);

	/* Chew leading spaces */
	args = skip_spaces(args);

	while (*args) {
		int ret;
		int irq_was_disabled;

		args = next_arg(args, &param, &val);				// 获取下一个参数param及其取值val
		irq_was_disabled = irqs_disabled();
		ret = parse_one(param, val, params, num, unknown);	// 解析这个参数
		if (irq_was_disabled && !irqs_disabled()) {
			printk(KERN_WARNING "parse_args(): option '%s' enabled irq's!\n", param);
		}
		switch (ret) {
		case -ENOENT:
			printk(KERN_ERR "%s: Unknown parameter `%s'\n", name, param);
			return ret;
		case -ENOSPC:
			printk(KERN_ERR "%s: `%s' too large for parameter `%s'\n", name, val ?: "", param);
			return ret;
		case 0:
			break;
		default:
			printk(KERN_ERR "%s: `%s' invalid for parameter `%s'\n", name, val ?: "", param);
			return ret;
		}
	}

	/* All parsed OK. */
	return 0;
}
```

其中，函数parse_one()定义于kernel/params.c:

```
static int parse_one(char *param, char *val,
		     const struct kernel_param *params, unsigned num_params,
		     int (*handle_unknown)(char *param, char *val))
{
	unsigned int i;
	int err;

	/*
	 * 在params中查找同名参数param，若存在，则调用其处理函数；
	 * start_kernel() -> parse_early_param() -> parse_early_options() -> parse_args(...) 不进入此循环；而
	 * start_kernel() -> parse_args("Booting kernel", ..., &unknown_bootoption) 要进入此循环，
	 * 其中，params为__start___param，num_params为__stop___param - __start___param，即__param段的内容，
	 * 参见__module_param_call()节
	 */
	/* Find parameter */
	for (i = 0; i < num_params; i++) {
		if (parameq(param, params[i].name)) {
			/* No one handled NULL, so do it here. */
			if (!val && params[i].ops->set != param_set_bool)
				return -EINVAL;
			DEBUGP("They are equal!  Calling %p\n", params[i].ops->set);
			mutex_lock(&param_lock);
			err = params[i].ops->set(val, &params[i]);
			mutex_unlock(&param_lock);
			return err;
		}
	}

	/*
	 * start_kernel() -> parse_early_param() -> parse_early_options() -> parse_args() 要进入此分支，
	 * 此时，handle_unknown取值为do_early_param，即调用do_early_param()，参见下文；
	 * start_kernel() -> parse_args("Booting kernel", ..., &unknown_bootoption) 可能会进入此分支，
	 * 此时，handle_unknown取值为unknown_bootoption，即调用unknown_bootoption()，参见parse_args()节
	 */
	if (handle_unknown) {
		DEBUGP("Unknown argument: calling %p\n", handle_unknown);
		return handle_unknown(param, val);
	}

	DEBUGP("Unknown argument `%s'\n", param);
	return -ENOENT;
}
```

函数do_early_param()定义于init/main.c:

```
/* Check for early params. */
static int __init do_early_param(char *param, char *val)
{
	const struct obs_kernel_param *p;

	/*
	 * 查找指定内核参数的处理函数，并调用之；
	 * 变量__setup_start和__setup_end参见early_param()/__setup()节
	 */
	for (p = __setup_start; p < __setup_end; p++) {
		if ((p->early && parameq(param, p->str)) ||
		     (strcmp(param, "console") == 0 && strcmp(p->str, "earlycon") == 0) ) {
			if (p->setup_func(val) != 0)
				printk(KERN_WARNING "Malformed early option '%s'\n", param);
		}
	}
	/* We accept everything at this stage. */
	return 0;
}
```

###### 4.3.4.1.4.3.3.3.2 parse_args()

当start_kernel()调用完parse_early_param()后，将调用如下函数解析命令行static_command_line中的内核参数：

```
parse_args("Booting kernel", static_command_line, __start___param,
		__stop___param - __start___param, &unknown_bootoption);
```

其执行过程与[parse_early_param()](#)节类似，不同之处在于，函数parse_one()调用handle_unknown()时，实际调用的是函数unknown_bootoption()而不是do_early_param()。

函数unknown_bootoption()定义于init/main.c:

```
/*
 * Unknown boot options get handed to init, unless they look like
 * unused parameters (modprobe will find them in /proc/cmdline).
 */
static int __init unknown_bootoption(char *param, char *val)
{
	/* Change NUL term back to "=", to make "param" the whole string. */
	if (val) {
		/* param=val or param="val"? */
		if (val == param+strlen(param)+1)
			val[-1] = '=';
		else if (val == param+strlen(param)+2) {
			val[-2] = '=';
			memmove(val-1, val, strlen(val)+1);
			val--;
		} else
			BUG();
	}

	/* Handle obsolete-style parameters */
	// 若parse_one()在__param段找不到对应参数的处理函数，则在.init.setup段重新查找
	if (obsolete_checksetup(param))
		return 0;

	/* Unused module parameter. */
	if (strchr(param, '.') && (!val || strchr(param, '.') < val))
		return 0;

	if (panic_later)
		return 0;

	if (val) {
		/* Environment option */
		unsigned int i;
		for (i = 0; envp_init[i]; i++) {
			if (i == MAX_INIT_ENVS) {
				panic_later = "Too many boot env vars at `%s'";
				panic_param = param;
			}
			if (!strncmp(param, envp_init[i], val - param))
				break;
		}
		envp_init[i] = param;
	} else {
		/* Command line option */
		unsigned int i;
		for (i = 0; argv_init[i]; i++) {
			if (i == MAX_INIT_ARGS) {
				panic_later = "Too many boot init vars at `%s'";
				panic_param = param;
			}
		}
		argv_init[i] = param;
	}
	return 0;
}

static int __init obsolete_checksetup(char *line)
{
	const struct obs_kernel_param *p;
	int had_early_param = 0;

	/*
	 * 查找指定内核参数的处理函数，并调用之；
	 * 其处理过程与函数do_early_param()类似，参见parse_early_param()节
	 */
	p = __setup_start;
	do {
		int n = strlen(p->str);
		if (parameqn(line, p->str, n)) {
			if (p->early) {
				/* Already done in parse_early_param?
				 * (Needs exact match on param part).
				 * Keep iterating, as we can have early
				 * params and __setups of same names 8( */
				if (line[n] == '\0' || line[n] == '=')
					had_early_param = 1;
			} else if (!p->setup_func) {
				printk(KERN_WARNING "Parameter %s is obsolete," ignored\n", p->str);
				return 1;
			} else if (p->setup_func(line + n))	// 调用内核参数的处理函数
				return 1;
		}
		p++;
	} while (p < __setup_end);

	return had_early_param;
}
```

###### 4.3.4.1.4.3.4 vfs_caches_init_early()

该函数用于初始化目录项哈希表(dentry_hashtable)和索引节点哈希表(inode_hashtable)，其定义于fs/dcache.c:

```
void __init vfs_caches_init_early(void)
{
	dcache_init_early();		// 参见dcache_init_early()节
	inode_init_early();		// 参见inode_init_early()节
}
```

###### 4.3.4.1.4.3.4.1 dcache_init_early()

该函数定义于fs/dcache.c:

```
static unsigned int d_hash_mask __read_mostly;
static unsigned int d_hash_shift __read_mostly;

static struct hlist_bl_head *dentry_hashtable __read_mostly;
static __initdata unsigned long dhash_entries;

static void __init dcache_init_early(void)
{
	int loop;

	// 如果本函数没有创建目录项哈希表，则在dcache_init()中创建，参见dcache_init()节
	/* If hashes are distributed across NUMA nodes, defer
	 * hash allocation until vmalloc space is available.
	 */
	if (hashdist)
		return;

	dentry_hashtable = alloc_large_system_hash("Dentry cache",
					sizeof(struct hlist_bl_head),
					dhash_entries,
					13,
					HASH_EARLY,
					&d_hash_shift,
					&d_hash_mask,
					0);

	for (loop = 0; loop < (1 << d_hash_shift); loop++)
		INIT_HLIST_BL_HEAD(dentry_hashtable + loop);
}
```

其中，变量hashdist定义于mm/page_alloc.c:

```
int hashdist = HASHDIST_DEFAULT;
```

而HASHDIST_DEFAULT与配置项CONFIG_NUMA和CONFIG_64BIT有关，其定义于include/linux/bootmem.h:

```
/* Only NUMA needs hash distribution. 64bit NUMA architectures have
 * sufficient vmalloc space.
 */
#if defined(CONFIG_NUMA) && defined(CONFIG_64BIT)
#define HASHDIST_DEFAULT 1
#else
#define HASHDIST_DEFAULT 0
#endif
```

###### 4.3.4.1.4.3.4.2 inode_init_early()

该函数定义于fs/inode.c:

```
static unsigned int i_hash_mask __read_mostly;
static unsigned int i_hash_shift __read_mostly;
static struct hlist_head *inode_hashtable __read_mostly;

static __initdata unsigned long ihash_entries;

/*
 * Initialize the waitqueues and inode hash table.
 */
void __init inode_init_early(void)
{
	int loop;

	/* If hashes are distributed across NUMA nodes, defer
	 * hash allocation until vmalloc space is available.
	 */
	if (hashdist)
		return;

	inode_hashtable = alloc_large_system_hash("Inode-cache",
					sizeof(struct hlist_head),
					ihash_entries,
					14,
					HASH_EARLY,
					&i_hash_shift,
					&i_hash_mask,
					0);

	for (loop = 0; loop < (1 << i_hash_shift); loop++)
		INIT_HLIST_HEAD(&inode_hashtable[loop]);
}
```

###### 4.3.4.1.4.3.5 trap_init()

该函数用于设置中断描述符表中前19个陷阱门所对应的处理程序(这些中断向量都是CPU保留用于异常处理的，参见[中断处理简介](#)节)，其定义于arch/x86/kernel/trap.c:

```
void __init trap_init(void)
{
	int i;

#ifdef CONFIG_EISA
	void __iomem *p = early_ioremap(0x0FFFD9, 4);

	if (readl(p) == 'E' + ('I'<<8) + ('S'<<16) + ('A'<<24))
		EISA_bus = 1;
	early_iounmap(p, 4);
#endif

	/*
	 * 数组idt_table[]定义于arch/x86/kernel/traps.c，其中，NR_VECTORS=256
	 *    gate_desc idt_table[NR_VECTORS];
	 */
	set_intr_gate(0, &divide_error); 					// 填充idt_table[0]
	set_intr_gate_ist(2, &nmi, NMI_STACK); 				// 填充idt_table[2]
	/* int4 can be called from all */
	set_system_intr_gate(4, &overflow); 					// 填充idt_table[4]
	set_intr_gate(5, &bounds); 							// 填充idt_table[5]
	set_intr_gate(6, &invalid_op); 						// 填充idt_table[6]
	set_intr_gate(7, &device_not_available); 				// 填充idt_table[7]
#ifdef CONFIG_X86_32
	set_task_gate(8, GDT_ENTRY_DOUBLEFAULT_TSS); 			// 填充idt_table[8]
#else
	set_intr_gate_ist(8, &double_fault, DOUBLEFAULT_STACK);
#endif
	set_intr_gate(9, &coprocessor_segment_overrun); 			// 填充idt_table[9]
	set_intr_gate(10, &invalid_TSS); 					// 填充idt_table[10]
	set_intr_gate(11, &segment_not_present);				// 填充idt_table[11]
	set_intr_gate_ist(12, &stack_segment, STACKFAULT_STACK); 	// 填充idt_table[12]
	set_intr_gate(13, &general_protection); 				// 填充idt_table[13]
	set_intr_gate(15, &spurious_interrupt_bug); 			// 填充idt_table[15]
	set_intr_gate(16, &coprocessor_error); 				// 填充idt_table[16]
	set_intr_gate(17, &alignment_check); 					// 填充idt_table[17]
#ifdef CONFIG_X86_MCE
	set_intr_gate_ist(18, &machine_check, MCE_STACK); 		// 填充idt_table[18]
#endif
	set_intr_gate(19, &simd_coprocessor_error); 			// 填充idt_table[19]

	/*
	 * FIRST_EXTERNAL_VECTOR定义于arch/x86/include/asm/irq_vectors.h，取值为0x20
	 * 即设置位图used_vectors的前32比特为1，表示中断向量表idt_table的占用情况
	 */
	/* Reserve all the builtin and the syscall vector: */
	for (i = 0; i < FIRST_EXTERNAL_VECTOR; i++)
		set_bit(i, used_vectors);

// CONFIG_IA32_EMULATION是否和下面的CONFIG_X86_32冲突？
#ifdef CONFIG_IA32_EMULATION
	set_system_intr_gate(IA32_SYSCALL_VECTOR, ia32_syscall); 	// 填充idt_table[128]
	// IA32_SYSCALL_VECTOR定义于arch/x86/include/asm/irq_vectors.h，取值为0x80
	set_bit(IA32_SYSCALL_VECTOR, used_vectors);
#endif

#ifdef CONFIG_X86_32
	/*
	 * SYSCALL_VECTOR定义于arch/x86/include/asm/irq_vectors.h，其取值为0x80
	 * system_call为系统调用总控程序，定义于arch/x86/kernel/entry_32.S，参见系统调用节
	 * 系统调用使用int 0x80中断，system_call根据系统调用号(保存于eax)查询sys_call_table，
	 * 找到对应的处理程序并执行
	 */
	set_system_trap_gate(SYSCALL_VECTOR, &system_call); 		// 填充idt_table[128]
	/*
	 * SYSCALL_VECTOR定义于arch/x86/include/asm/irq_vectors.h，其取值为0x80
	 * 在arch/x86/kernel/traps.c中，used_vectors通过宏DECLARE_BITMAP定义：
	 *     DECLARE_BITMAP(used_vectors, NR_VECTORS);
	 *     扩展后：unsigned long used_vectors[256];
	 */
	set_bit(SYSCALL_VECTOR, used_vectors);
#endif

	/*
	 * Should be a barrier for any external CPU state:
	 */
	cpu_init();				// 该函数定义于arch/x86/kernel/cpu/common.c

	x86_init.irqs.trap_init();		// x86_init定义于arch/x86/kernel/x86_init.c
}
```

idt_table[]示意图，参见Subjects/Chapter04_Boot/Figures/idt_table[].jpg

###### 4.3.4.1.4.3.5.1 设置idt_table表项

函数trap_init()调用如下函数设置idt_table表项，其定义于arch/x86/include/asm/desc.h：

* set_intr_gate()

```
static inline void set_intr_gate(unsigned int n, void *addr)
{
	BUG_ON((unsigned)n > 0xFF);
	_set_gate(n, GATE_INTERRUPT, addr, 0, 0, __KERNEL_CS);
}
```

* set_intr_gate_ist()

```
static inline void set_intr_gate_ist(int n, void *addr, unsigned ist)
{
	BUG_ON((unsigned)n > 0xFF);
	_set_gate(n, GATE_INTERRUPT, addr, 0, ist, __KERNEL_CS);
}

- set_system_intr_gate()
static inline void set_system_intr_gate(unsigned int n, void *addr)
{
	BUG_ON((unsigned)n > 0xFF);
	_set_gate(n, GATE_INTERRUPT, addr, 0x3, 0, __KERNEL_CS);
}
```

* set_task_gate()

```
static inline void set_intr_gate(unsigned int n, void *addr)
{
	BUG_ON((unsigned)n > 0xFF);
	_set_gate(n, GATE_INTERRUPT, addr, 0, 0, __KERNEL_CS);
}
```

* set_system_trap_gate()

```
static inline void set_system_trap_gate(unsigned int n, void *addr)
{
	BUG_ON((unsigned)n > 0xFF);
	_set_gate(n, GATE_TRAP, addr, 0x3, 0, __KERNEL_CS);
}
```

上述函数均通过调用_set_gate()来实现，其定义于arch/x86/include/asm/desc.h:

```
static inline void _set_gate(int gate, unsigned type, void *addr, unsigned dpl,
									unsigned ist, unsigned seg)
{
	gate_desc s;

	// 参见pack_gate()节
	pack_gate(&s, type, (unsigned long)addr, dpl, ist, seg);

	/*
	 * does not need to be atomic because it is only done once at
	 * setup time
	 */
	// 将描述符s拷贝到idt_table[gate]项中，参见write_idt_entry()节
	write_idt_entry(idt_table, gate, &s);
}
```

###### 4.3.4.1.4.3.5.1.1 pack_gate()

pack_gate()定义于arch/x86/include/asm/desc.h：

```
#ifdef CONFIG_X86_64

static inline void pack_gate(gate_desc *gate, unsigned type, unsigned long func,
					  unsigned dpl, unsigned ist, unsigned seg)
{
	gate->offset_low		= PTR_LOW(func);
	gate->segment		= __KERNEL_CS;
	gate->ist			= ist;
	gate->p			= 1;
	gate->dpl			= dpl;
	gate->zero0		= 0;
	gate->zero1		= 0;
	gate->type			= type;
	gate->offset_middle	= PTR_MIDDLE(func);
	gate->offset_high	= PTR_HIGH(func);
}

#else

/*
 * 给指定的描述符赋值，参见段描述符节
 * 注意：没有定义宏CONFIG_X86_64的情况下，入参flags是无效的
 */
static inline void pack_gate(gate_desc *gate, unsigned char type, unsigned long base,
					  unsigned dpl, unsigned flags, unsigned short seg)
{
	gate->a = (seg << 16) | (base & 0xffff);
	gate->b = (base & 0xffff0000) | (((0x80 | type | (dpl << 5)) & 0xff) << 8);
}

#endif
```

###### 4.3.4.1.4.3.5.1.2 write_idt_entry()

该函数定义于arch/x86/include/asm/desc.h：

```
#ifdef CONFIG_PARAVIRT
#include <asm/paravirt.h>
#else
#define write_idt_entry(dt, entry, g)		native_write_idt_entry(dt, entry, g)
#endif	/* CONFIG_PARAVIRT */

static inline void native_write_idt_entry(gate_desc *idt, int entry, const gate_desc *gate)
{
	memcpy(&idt[entry], gate, sizeof(*gate));
}
```

###### 4.3.4.1.4.3.6 mm_init()

该函数定义于init/main.c:

```
static void __init mm_init(void)
{
	/*
	 * page_cgroup requires countinous pages as memmap
	 * and it's bigger than MAX_ORDER unless SPARSEMEM.
	 */
	page_cgroup_init_flatmem();
	mem_init();				// 参见mem_init()节
	kmem_cache_init();			// 参见 General Cache/kmem_cache_init()节
	percpu_init_late();
	pgtable_cache_init();
	vmalloc_init();
}

4.3.4.1.4.3.6.1 mem_init()

该函数定义于arch/x86/mm/init_32.c:
void __init mem_init(void)
{
	int codesize, reservedpages, datasize, initsize;
	int tmp;

	pci_iommu_alloc();

#ifdef CONFIG_FLATMEM
	BUG_ON(!mem_map);
#endif
	/* this will put all low memory onto the freelists */
	// 参见free_all_bootmem()/free_all_bootmem_core()节
	totalram_pages += free_all_bootmem();

	reservedpages = 0;
	/*
	 * max_low_pfn的含义参见错误：引用源未找到，其取值被如下函数更新：
	 * start_kernel() -> setup_arch() -> find_low_pfn_range()
	 */
	for (tmp = 0; tmp < max_low_pfn; tmp++)
		/*
		 * Only count reserved RAM pages:
		 */
		if (page_is_ram(tmp) && PageReserved(pfn_to_page(tmp)))
			reservedpages++;

	// 将高端内存转入Buddy Allocator System中管理，参见set_highmem_pages_init()节
	set_highmem_pages_init();

	// 各变量的含义参见错误：引用源未找到
	codesize =  (unsigned long) &_etext - (unsigned long) &_text;
	datasize =  (unsigned long) &_edata - (unsigned long) &_etext;
	initsize =  (unsigned long) &__init_end - (unsigned long) &__init_begin;

	// 打印输出参见early_node_map[]=>node_data[]->node_zones[]节NOTE 13
	printk(KERN_INFO "Memory: %luk/%luk available "
		"(%dk kernel code, %dk reserved, %dk data, %dk init, %ldk highmem)\n",
		nr_free_pages() << (PAGE_SHIFT-10), num_physpages << (PAGE_SHIFT-10),
		codesize >> 10, reservedpages << (PAGE_SHIFT-10),
		datasize >> 10, initsize >> 10, totalhigh_pages << (PAGE_SHIFT-10));

	// 打印输出参见early_node_map[]=>node_data[]->node_zones[]节NOTE 13
	printk(KERN_INFO "virtual kernel memory layout:\n"
		"    fixmap  : 0x%08lx - 0x%08lx   (%4ld kB)\n"
#ifdef CONFIG_HIGHMEM
		"    pkmap   : 0x%08lx - 0x%08lx   (%4ld kB)\n"
#endif
		"    vmalloc : 0x%08lx - 0x%08lx   (%4ld MB)\n"
		"    lowmem  : 0x%08lx - 0x%08lx   (%4ld MB)\n"
		"      .init : 0x%08lx - 0x%08lx   (%4ld kB)\n"
		"      .data : 0x%08lx - 0x%08lx   (%4ld kB)\n"
		"      .text : 0x%08lx - 0x%08lx   (%4ld kB)\n",

		FIXADDR_START, FIXADDR_TOP,
		(FIXADDR_TOP - FIXADDR_START) >> 10,

#ifdef CONFIG_HIGHMEM
		PKMAP_BASE, PKMAP_BASE+LAST_PKMAP*PAGE_SIZE,
		(LAST_PKMAP*PAGE_SIZE) >> 10,
#endif

		VMALLOC_START, VMALLOC_END,
		(VMALLOC_END - VMALLOC_START) >> 20,

		(unsigned long)__va(0), (unsigned long)high_memory,
		((unsigned long)high_memory - (unsigned long)__va(0)) >> 20,

		(unsigned long)&__init_begin, (unsigned long)&__init_end,
		((unsigned long)&__init_end - (unsigned long)&__init_begin) >> 10,

		(unsigned long)&_etext, (unsigned long)&_edata,
		((unsigned long)&_edata - (unsigned long)&_etext) >> 10,

		(unsigned long)&_text, (unsigned long)&_etext,
		((unsigned long)&_etext - (unsigned long)&_text) >> 10);

	/*
	 * Check boundaries twice: Some fundamental inconsistencies can
	 * be detected at build time already.
	 */
#define __FIXADDR_TOP (-PAGE_SIZE)
#ifdef CONFIG_HIGHMEM
	BUILD_BUG_ON(PKMAP_BASE + LAST_PKMAP*PAGE_SIZE	> FIXADDR_START);
	BUILD_BUG_ON(VMALLOC_END > PKMAP_BASE);
#endif
#define high_memory (-128UL << 20)
	BUILD_BUG_ON(VMALLOC_START >= VMALLOC_END);
#undef high_memory
#undef __FIXADDR_TOP

#ifdef CONFIG_HIGHMEM
	BUG_ON(PKMAP_BASE + LAST_PKMAP*PAGE_SIZE > FIXADDR_START);
	BUG_ON(VMALLOC_END > PKMAP_BASE);
#endif
	BUG_ON(VMALLOC_START >= VMALLOC_END);
	BUG_ON((unsigned long)high_memory > VMALLOC_START);

	if (boot_cpu_data.wp_works_ok < 0)
		test_wp_bit();
}
```

###### 4.3.4.1.4.3.6.1.1 free_all_bootmem()/free_all_bootmem_core()

Once free_all_bootmem() returns, all the pages in ZONE_NORMAL have been given to the buddy allocator. See section early_node_map[]=>node_data[]->node_zones[].

函数free_all_bootmem()定义于mm/bootmem.c:

```
static struct list_head bdata_list __initdata = LIST_HEAD_INIT(bdata_list);

/**
 * free_all_bootmem - release free pages to the buddy allocator
* Returns the number of pages actually released.
 */
unsigned long __init free_all_bootmem(void)
{
	unsigned long total_pages = 0;
	bootmem_data_t *bdata;

	/*
	 * 类型bootmem_data_t参见Boot Memory Allocator/bootmem_data_t节，
	 * 变量bdata_list参见链表，函数free_all_bootmem_core()参见下文
	 */
	list_for_each_entry(bdata, &bdata_list, list)
		total_pages += free_all_bootmem_core(bdata);

	return total_pages;
}
```

其中，函数free_all_bootmem_core()定义于mm/bootmem.c:

```
static unsigned long __init free_all_bootmem_core(bootmem_data_t *bdata)
{
	int aligned;
	struct page *page;
	unsigned long start, end, pages, count = 0;

	if (!bdata->node_bootmem_map)
		return 0;

	start = bdata->node_min_pfn;
	end = bdata->node_low_pfn;

	/*
	 * If the start is aligned to the machines wordsize, we might
	 * be able to free pages in bulks of that order.
	 */
	aligned = !(start & (BITS_PER_LONG - 1));

	bdebug("nid=%td start=%lx end=%lx aligned=%d\n", bdata - bootmem_node_data, start, end, aligned);

	while (start < end) {
		unsigned long *map, idx, vec;

		map = bdata->node_bootmem_map;
		idx = start - bdata->node_min_pfn;
		vec = ~map[idx / BITS_PER_LONG];

		/*
		 * 根据起始页框号是否对齐、空闲页面的多少等因素释放页面到Buddy Allocator Sytem：
		 * 或者一次释放32个页面，或者一次释放一个页面
		 */
		if (aligned && vec == ~0UL && start + BITS_PER_LONG < end) {
			int order = ilog2(BITS_PER_LONG);
			__free_pages_bootmem(pfn_to_page(start), order);	// 每次释放32个页面，参见下文
			count += BITS_PER_LONG;
		} else {
			unsigned long off = 0;
			while (vec && off < BITS_PER_LONG) {
				if (vec & 1) {
					page = pfn_to_page(start + off);
					__free_pages_bootmem(page, 0);		// 每次释放1个页面，参见下文
					count++;
				}
				vec >>= 1;
				off++;
			}
		}
		start += BITS_PER_LONG;
	}

	/*
	 * 释放位图(bdata->node_bootmem_map)所占用的内存空间：
	 * 位图用来指示一个页面是否空闲，现在所有内存都归Buddy Allocator System管理，
	 * 该位图就没有存在的必要了
	 */
	page = virt_to_page(bdata->node_bootmem_map);
	pages = bdata->node_low_pfn - bdata->node_min_pfn;
	pages = bootmem_bootmap_pages(pages);
	count += pages;
	while (pages--)
		__free_pages_bootmem(page++, 0);					// 参见下文

	bdebug("nid=%td released=%lx\n", bdata - bootmem_node_data, count);

	return count;
}
```

其中，函数__free_pages_bootmem()定义于mm/page_alloc.c:

```
void __meminit __free_pages_bootmem(struct page *page, unsigned int order)
{
	if (order == 0) {				// 释放单个页面
		__ClearPageReserved(page);		// 复位page->flags中的标志位PG_reserved
		set_page_count(page, 0);		// page->_count = 0
		set_page_refcounted(page);		// page->_count = 1
		__free_page(page);			// 参见__free_page()/free_page()节
	} else {						// 释放2order个页面
		int loop;

		prefetchw(page);
		for (loop = 0; loop < BITS_PER_LONG; loop++) {
			struct page *p = &page[loop];

			if (loop + 1 < BITS_PER_LONG)
				prefetchw(p + 1);
			__ClearPageReserved(p); 	// 复位page->flags中的标志位PG_reserved
			set_page_count(p, 0);		// page->_count = 0
		}

		set_page_refcounted(page);		// page->_count = 1
		__free_pages(page, order);		// 参见free_pages()/__free_pages()节
	}
}
```

###### 4.3.4.1.4.3.6.1.2 set_highmem_pages_init()

函数set_highmem_pages_init()定义于arch/x86/mm/init_32.c:

```
void __init set_highmem_pages_init(void)
{
	struct zone *zone;
	int nid;

	for_each_zone(zone) {
		unsigned long zone_start_pfn, zone_end_pfn;

		if (!is_highmem(zone))
			continue;

		zone_start_pfn = zone->zone_start_pfn;
		zone_end_pfn = zone_start_pfn + zone->spanned_pages;

		nid = zone_to_nid(zone);
		printk(KERN_INFO "Initializing %s for node %d (%08lx:%08lx)\n",
				zone->name, nid, zone_start_pfn, zone_end_pfn);

		add_highpages_with_active_regions(nid, zone_start_pfn, zone_end_pfn);
	}
	totalram_pages += totalhigh_pages;
}
```

函数add_highpages_with_active_regions()定义于arch/x86/mm/init_32.c:

```
void __init add_highpages_with_active_regions(int nid, unsigned long start_pfn, unsigned long end_pfn)
{
	struct range *range;
	int nr_range;
	int i;

	// 获取页框数
	nr_range = __get_free_all_memory_range(&range, nid, start_pfn, end_pfn);

	for (i = 0; i < nr_range; i++) {
		struct page *page;
		int node_pfn;

		for (node_pfn = range[i].start; node_pfn < range[i].end; node_pfn++) {
			if (!pfn_valid(node_pfn))
				continue;
			page = pfn_to_page(node_pfn);
			/*
			 * 调用__free_page()将该页加入到Buddy Allocator System中
			 * 参见early_node_map[]=>node_data[]->node_zones[]节
			 * 和__free_page()/free_page()节
			 */
			add_one_highpage_init(page);
		}
	}
}
```

###### 4.3.4.1.4.3.7 sched_init()

该函数定义参见kernel/sched.c:

```
void __init sched_init(void)
{
	...

	/*
	 * Make us the idle thread. Technically, schedule() should not be
	 * called from this thread, however somewhere below it might be,
	 * but because we are the idle thread, we just pick up running again
	 * when this runqueue becomes "idle".
	 */
	/*
	 * 将当前进程作为idle进程，放置到当然CPU运行队列的rq->idle域，
	 * 参见运行队列结构/struct rq节
	 */
	init_idle(current, smp_processor_id());

	calc_load_update = jiffies + LOAD_FREQ;

	/*
	 * During early bootup we pretend to be a normal task:
	 */
	// 各调度类组成的链表参见pick_next_task()节和错误：引用源未找到节
	current->sched_class = &fair_sched_class;

	...
}
```

###### 4.3.4.1.4.3.8 early_irq_init()

该函数用于初始化数组irq_desc[](参见[struct irq_desc](#)节)，其定义于kernel/irq/irqdesc.c:

```
#ifdef CONFIG_SPARSE_IRQ
...
#else /* !CONFIG_SPARSE_IRQ */

int __init early_irq_init(void)
{
	int count, i, node = first_online_node;
	struct irq_desc *desc;

	init_irq_default_affinity();

	printk(KERN_INFO "NR_IRQS:%d\n", NR_IRQS);

	desc = irq_desc;
	count = ARRAY_SIZE(irq_desc);

	// 依次为数组irq_desc[]元素赋予默认值
	for (i = 0; i < count; i++) {
		desc[i].kstat_irqs = alloc_percpu(unsigned int);
		alloc_masks(&desc[i], GFP_KERNEL, node);
		raw_spin_lock_init(&desc[i].lock);
		lockdep_set_class(&desc[i].lock, &irq_desc_lock_class);
		desc_set_defaults(i, &desc[i], node, NULL);
	}
	return arch_early_irq_init();
}

#endif

static void desc_set_defaults(unsigned int irq, struct irq_desc *desc,
		int node, struct module *owner)
{
	int cpu;

	desc->irq_data.irq = irq;
	desc->irq_data.chip = &no_irq_chip;
	desc->irq_data.chip_data = NULL;
	desc->irq_data.handler_data = NULL;
	desc->irq_data.msi_desc = NULL;
	irq_settings_clr_and_set(desc, ~0, _IRQ_DEFAULT_INIT_FLAGS);
	irqd_set(&desc->irq_data, IRQD_IRQ_DISABLED);
	desc->handle_irq = handle_bad_irq;
	desc->depth = 1;
	desc->irq_count = 0;
	desc->irqs_unhandled = 0;
	desc->name = NULL;
	desc->owner = owner;
	for_each_possible_cpu(cpu)
		*per_cpu_ptr(desc->kstat_irqs, cpu) = 0;
	desc_smp_init(desc, node);
}
```

###### 4.3.4.1.4.3.9 init_IRQ()

该函数用于设置可屏蔽中断，其定义于arch/x86/kernel/irqinit.c:

```
void __init init_IRQ(void)
{
	int i;

	/*
	 * We probably need a better place for this, but it works for
	 * now ...
	 */
	x86_add_irq_domains();

	/*
	 * On cpu 0, Assign IRQ0_VECTOR..IRQ15_VECTOR's to IRQ 0..15.
	 * If these IRQ's are handled by legacy interrupt-controllers like PIC,
	 * then this configuration will likely be static after the boot. If
	 * these IRQ's are handled by more mordern controllers like IO-APIC,
	 * then this vector space can be freed and re-used dynamically as the
	 * irq's migrate etc.
	 */
	/*
	 * legacy_pic参见legacy_pic / x86_init节，其中legacy_pic->nr_legacy_irqs
	 * 取值为NR_IRQS_LEGACY，即16。因而，此处设置IRQ 0x30..0x3F，参见vector_irq节
	 * IRQ0_VECTOR定义于arch/x86/include/asm/irq_vectors.h，取值为48，参见中断处理简介节
	 */
	for (i = 0; i < legacy_pic->nr_legacy_irqs; i++)
		per_cpu(vector_irq, 0)[IRQ0_VECTOR + i] = i;

	/*
	 * x86_init参见legacy_pic / x86_init节，其中x86_init.irqs.intr_init
	 * 取值为native_init_IRQ。因而，如下语句调用函数native_init_IRQ()，
	 * 参见native_init_IRQ()节
	 */
	x86_init.irqs.intr_init();
}
```

###### 4.3.4.1.4.3.9.1 legacy_pic / x86_init

变量legacy_pic定义于arch/x86/kernel/i8259.c:

```
struct irq_chip i8259A_chip = {
	.name			= "XT-PIC",
	.irq_mask		= disable_8259A_irq,
	.irq_disable	= disable_8259A_irq,
	.irq_unmask	= enable_8259A_irq,
	.irq_mask_ack	= mask_and_ack_8259A,
};

struct legacy_pic default_legacy_pic = {
	// 取值为16，定义于arch/x86/include/asm/irq_vectors.h
	.nr_legacy_irqs	= NR_IRQS_LEGACY,
	.chip  		= &i8259A_chip,
	.mask 		= mask_8259A_irq,
	.unmask		= unmask_8259A_irq,
	.mask_all 		= mask_8259A,
	.restore_mask 	= unmask_8259A,
	.init 		= init_8259A,
	.irq_pending 	= i8259A_irq_pending,
	.make_irq 		= make_8259A_irq,
};

struct legacy_pic *legacy_pic = &default_legacy_pic;
```

变量x86_init定义于arch/x86/kernel/x86_init.c:

```
/*
 * The platform setup functions are preset with the default functions
 * for standard PC hardware.
 */
struct x86_init_ops x86_init __initdata = {

	.resources = {
		.probe_roms		= probe_roms,
		.reserve_resources	= reserve_standard_io_resources,
		.memory_setup		= default_machine_specific_memory_setup,
	},

	.mpparse = {
		.mpc_record		= x86_init_uint_noop,
		.setup_ioapic_ids	= x86_init_noop,
		.mpc_apic_id		= default_mpc_apic_id,
		.smp_read_mpc_oem	= default_smp_read_mpc_oem,
		.mpc_oem_bus_info	= default_mpc_oem_bus_info,
		.find_smp_config		= default_find_smp_config,
		.get_smp_config		= default_get_smp_config,
	},

	.irqs = {
		.pre_vector_init		= init_ISA_irqs,
		.intr_init			= native_init_IRQ,
		.trap_init			= x86_init_noop,
	},

	.oem = {
		.arch_setup		= x86_init_noop,
		.banner			= default_banner,
	},

	.mapping = {
		.pagetable_reserve	= native_pagetable_reserve,
	},

	.paging = {
		.pagetable_setup_start= native_pagetable_setup_start,
		.pagetable_setup_done	= native_pagetable_setup_done,
	},

	.timers = {
		.setup_percpu_clockev	= setup_boot_APIC_clock,
		.tsc_pre_init		= x86_init_noop,
		.timer_init		= hpet_time_init,
		.wallclock_init		= x86_init_noop,
	},

	.iommu = {
		.iommu_init		= iommu_init_noop,
	},

	.pci = {
		.init				= x86_default_pci_init,
		.init_irq			= x86_default_pci_init_irq,
		.fixup_irqs		= x86_default_pci_fixup_irqs,
	},
};
```

###### 4.3.4.1.4.3.9.2 native_init_IRQ()

该函数定义于arch/x86/kernel/irqinit.c:

```
void __init native_init_IRQ(void)
{
	int i;

	/*
	 * x86_init参见legacy_pic / x86_init节，其中x86_init.irqs.pre_vector_init
	 * 取值为init_ISA_irqs，因而如下语句调用函数init_ISA_irqs()，参见init_ISA_irqs()节
	 */
	/* Execute any quirks before the call gates are initialised: */
	x86_init.irqs.pre_vector_init();

	// 参见apic_intr_init()节
	apic_intr_init();

	/*
	 * Cover the whole vector space, no vector can escape
	 * us. (some of these will be overridden and become
	 * 'special' SMP interrupts)
	 */
	for (i = FIRST_EXTERNAL_VECTOR; i < NR_VECTORS; i++) {
		/*
		 * IA32_SYSCALL_VECTOR could be used in trap_init already.
		 * used_vectors定义于arch/x86/kernel/traps.c
		 * used_vectors is BITMAP for irq which is not managed by percpu vector_irq
		 * used_vectors中的前32个比特位在trap_init()中被赋值，参见trap_init()节
		 */
		if (!test_bit(i, used_vectors))
			// 数组interrupt[]参见interrupt[]节
			set_intr_gate(i, interrupt[i-FIRST_EXTERNAL_VECTOR]);
	}

	// IRQ2 is cascade interrupt to second interrupt controller
	if (!acpi_ioapic && !of_ioapic)
		setup_irq(2, &irq2);

#ifdef CONFIG_X86_32
	/*
	 * External FPU? Set up irq13 if so, for
	 * original braindamaged IBM FERR coupling.
	 */
	if (boot_cpu_data.hard_math && !cpu_has_fpu)
		setup_irq(FPU_IRQ, &fpu_irq); 		// FPU_IRQ取值为13

	irq_ctx_init(smp_processor_id());
#endif
}
```

###### 4.3.4.1.4.3.9.2.1 init_ISA_irqs()

该函数用于设置ISA中断(IRQ 0x30-0x3F，参见中断处理简介节)所对应的中断处理程序，其定义于arch/x86/kernel/irqinit.c:

```
void __init init_ISA_irqs(void)
{
	// 外部可屏蔽中断采用8259A中断控制器，参见legacy_pic / x86_init节和节
	struct irq_chip *chip = legacy_pic->chip;
	const char *name = chip->name;
	int i;

#if defined(CONFIG_X86_64) || defined(CONFIG_X86_LOCAL_APIC)
	init_bsp_APIC();
#endif
	// 调用init_8259A()初始化8259A中断控制器，参见legacy_pic / x86_init节
	legacy_pic->init(0);

	// 依次设置8259A控制的16个中断向量对应的中断处理函数，即handle_level_irq()
	for (i = 0; i < legacy_pic->nr_legacy_irqs; i++)
		irq_set_chip_and_handler_name(i, chip, handle_level_irq, name);
}
```

其中，irq_set_chip_and_handler_name()设置中断控制器芯片及中断处理函数，其定义于kernel/irq/chip.c:

```
void irq_set_chip_and_handler_name(unsigned int irq, struct irq_chip *chip,
			      irq_flow_handler_t handle, const char *name)
{
	irq_set_chip(irq, chip);
	__irq_set_handler(irq, handle, 0, name);
}

/**
 *	irq_set_chip - set the irq chip for an irq
 *	@irq:	irq number
 *	@chip:	pointer to irq chip description structure
 */
int irq_set_chip(unsigned int irq, struct irq_chip *chip)
{
	unsigned long flags;
	struct irq_desc *desc = irq_get_desc_lock(irq, &flags, 0);

	if (!desc)
		return -EINVAL;

	if (!chip)
		chip = &no_irq_chip;

	desc->irq_data.chip = chip;
	irq_put_desc_unlock(desc, flags);
	/*
	 * For !CONFIG_SPARSE_IRQ make the irq show up in
	 * allocated_irqs. For the CONFIG_SPARSE_IRQ case, it is
	 * already marked, and this call is harmless.
	 */
	irq_reserve_irq(irq);
	return 0;
}

void __irq_set_handler(unsigned int irq, irq_flow_handler_t handle, int is_chained, const char *name)
{
	unsigned long flags;
	struct irq_desc *desc = irq_get_desc_buslock(irq, &flags, 0);

	if (!desc)
		return;

	if (!handle) {
		handle = handle_bad_irq;
	} else {
		if (WARN_ON(desc->irq_data.chip == &no_irq_chip))
			goto out;
	}

	/* Uninstall? */
	if (handle == handle_bad_irq) {
		if (desc->irq_data.chip != &no_irq_chip)
			mask_ack_irq(desc);
		irq_state_set_disabled(desc);
		desc->depth = 1;
	}
	// 设置中断处理函数为handle_level_irq()，参见desc->handle_irq()/handle_level_irq()节
	desc->handle_irq = handle;
	desc->name = name;

	if (handle != handle_bad_irq && is_chained) {
		irq_settings_set_noprobe(desc);
		irq_settings_set_norequest(desc);
		irq_settings_set_nothread(desc);
		irq_startup(desc);
	}
out:
	irq_put_desc_busunlock(desc, flags);
}
```

###### 4.3.4.1.4.3.9.2.2 apic_intr_init()

该函数设置APIC可屏蔽中断所对应的中断处理程序，其定义于arch/x86/kernel/irqinit.c:

```
static void __init apic_intr_init(void)
{
	smp_intr_init();

#ifdef CONFIG_X86_THERMAL_VECTOR
	alloc_intr_gate(THERMAL_APIC_VECTOR, thermal_interrupt); 		// IRQ 0xFA
#endif
#ifdef CONFIG_X86_MCE_THRESHOLD
	alloc_intr_gate(THRESHOLD_APIC_VECTOR, threshold_interrupt); 	// IRQ 0xF9
#endif

#if defined(CONFIG_X86_64) || defined(CONFIG_X86_LOCAL_APIC)
	/* self generated IPI for local APIC timer */
	alloc_intr_gate(LOCAL_TIMER_VECTOR, apic_timer_interrupt); 		// IRQ 0xEF

	/* IPI for X86 platform specific use */
	alloc_intr_gate(X86_PLATFORM_IPI_VECTOR, x86_platform_ipi); 	// IRQ 0xF7

	/* IPI vectors for APIC spurious and error interrupts */
	alloc_intr_gate(SPURIOUS_APIC_VECTOR, spurious_interrupt); 		// IRQ 0xFF
	alloc_intr_gate(ERROR_APIC_VECTOR, error_interrupt); 			// IRQ 0xFE

	/* IRQ work interrupts: */
# ifdef CONFIG_IRQ_WORK
	alloc_intr_gate(IRQ_WORK_VECTOR, irq_work_interrupt); 			// IRQ 0xF6
# endif

#endif
}
```

###### 4.3.4.1.4.3.9.2.3 interrupt[]

数组interrupt[]定义于arch/x86/kernel/entry_32.S:

```
/*
 * Build the entry stubs and pointer table with some assembler magic.
 * We pack 7 stubs into a single 32-byte chunk, which will fit in a
 * single cache line on all modern x86 implementations.
 */
.section .init.rodata,"a"
ENTRY(interrupt)
.section .entry.text, "ax"
	.p2align 5
	.p2align CONFIG_X86_L1_CACHE_SHIFT
ENTRY(irq_entries_start)
	RING0_INT_FRAME
vector=FIRST_EXTERNAL_VECTOR					// FIRST_EXTERNAL_VECTOR取值为0x20
.rept (NR_VECTORS-FIRST_EXTERNAL_VECTOR+6)/7		// 外层循环，共32次
	.balign 32								// 32字节对齐
	.rept	7								// 内层循环，共7次
		.if vector < NR_VECTORS
			.if vector <> FIRST_EXTERNAL_VECTOR
				CFI_ADJUST_CFA_OFFSET -4		// 按照CFA规则修改前一个offset，以达到4字节对齐
			.endif
1: 			pushl_cfi $(~vector+0x80) 	/* Note: always in signed byte range */ // 占2字节
			.if ((vector-FIRST_EXTERNAL_VECTOR)%7) <> 6
				jmp 2f					// 跳转到2处，即long jmp，占5字节
			.endif
			.previous
			.long 1b						// 跳转到1处，即short jmp，占2字节
			.section .entry.text, "ax"
			vector=vector+1
		.endif
	.endr
2: 	jmp common_interrupt						// 跳转到common_interrupt执行
.endr
END(irq_entries_start)

.previous
END(interrupt)
.previous

/*
 * the CPU automatically disables interrupts when executing an IRQ vector,
 * so IRQ-flags tracing has to follow that:
 */
	.p2align CONFIG_X86_L1_CACHE_SHIFT
common_interrupt:
	addl $-0x80,(%esp)	/* Adjust vector into the [-256,-1] range */
	SAVE_ALL			// 保存中断处理程序可能用到的寄存器
	TRACE_IRQS_OFF
	movl %esp,%eax		// 把栈顶指针传给eax寄存器，该寄存器的内容将作为do_IRQ()函数的入参
	call do_IRQ		// 调用do_IRQ()处理中断，参见do_IRQ()节
	jmp ret_from_intr	// 参见ret_from_intr节
ENDPROC(common_interrupt)
	CFI_ENDPROC
```

ENTRY(interrupt)通过伪指令.rept和.endr，在代码段产生(NR_VECTORS - FIRST_EXTERNAL_VECTOR)个跳转到common_interrupt的汇编代码片段，起始地址为irq_entries_start；在数据段产生一个中断数组的符号interrupt，用于记录产生代码段中每个中断向量处理的汇编代码片段地址，在C语言中将interrupt符号作为中断数组变量导入(参见arch/x86/include/asm/hw_irq.h):

```
extern void (*__initconst interrupt[NR_VECTORS-FIRST_EXTERNAL_VECTOR])(void);
```

ENTRY(interrupt)编译之后，所生成的代码段和数据段内存布局如下：


ENTRIY(interrupt)汇编代码段主要由两个.rept构成，外层.rept循环(NR_VECTORS-FIRST_EXTERNAL_VECTOR+6)/7次，而其中每次内层.rept循环7次，内层循环所产生的代码以32字节对齐，内层.rept循环产生的代码如上图irq_entries_start中的粗黑方框所示。

以两层.rept循环生成jmp common_interrupt的目的在于：在内循环中，前6次循环产生的代码指令为push和short jmp，而第7次产生的代码指令为push和long jmp。push占2字节，short jmp占2字节，long jmp占5字节，故采取这种方式内层.rept循环7次产生的代码大小为：6 * (2 + 2) + 2 + 5 = 31 字节，而外层循环以32字节对齐。老版本每次都为push和long jmp，相对而言，这种新方法利用short jmp节省了内存开销。

每个中断门描述符将$(~vector+0x80)压栈后都会跳转到common_interrupt处执行。common_interrupt在保存中断现场之后，跳转到do_IRQ()进行中断处理，最后调用iret_from_intr进行中断返回、恢复中断上下文。

common_interrupt在调用do_IRQ()前，中断栈内存布局如下：


###### 4.3.4.1.4.3.10 softirq_init()

该函数用于初始化软中断相关数据结构，其定义于kernel/softirq.c:

```
void __init softirq_init(void)
{
	int cpu;

	for_each_possible_cpu(cpu) {
		int i;

		// 参见struct tasklet_节
		per_cpu(tasklet_vec, cpu).tail = &per_cpu(tasklet_vec, cpu).head;
		// 参见struct tasklet_节
		per_cpu(tasklet_hi_vec, cpu).tail = &per_cpu(tasklet_hi_vec, cpu).head;
		for (i = 0; i < NR_SOFTIRQS; i++)
			INIT_LIST_HEAD(&per_cpu(softirq_work_list[i], cpu));	// 参见softirq_work_list[]节
	}

	register_hotcpu_notifier(&remote_softirq_cpu_notifier);

	/*
	 * 设置软中断TASKLET_SOFTIRQ的服务程序为tasklet_action()，
	 * 参见struct softirq_节和tasklet_action()节
	 */
	open_softirq(TASKLET_SOFTIRQ, tasklet_action);
	/*
	 * 设置软中断HI_SOFTIRQ的服务程序为tasklet_hi_action()，
	 * 参见struct softirq_节和tasklet_hi_action()节
	 */
	open_softirq(HI_SOFTIRQ, tasklet_hi_action);
}

static struct notifier_block __cpuinitdata remote_softirq_cpu_notifier = {
	.notifier_call = remote_softirq_cpu_notify,
};
```

###### 4.3.4.1.4.3.10.1 tasklet_action()

该函数定义于kernel/softirq.c:

```
static void tasklet_action(struct softirq_action *a)
{
	struct tasklet_struct *list;

	// 从tasklet_vec中获取列表，参见struct tasklet_节
	local_irq_disable();
	list = __this_cpu_read(tasklet_vec.head);
	__this_cpu_write(tasklet_vec.head, NULL);
	__this_cpu_write(tasklet_vec.tail, &__get_cpu_var(tasklet_vec).head);
	local_irq_enable();

	while (list) {
		struct tasklet_struct *t = list;

		list = list->next;

		if (tasklet_trylock(t)) {
			if (!atomic_read(&t->count)) {
				if (!test_and_clear_bit(TASKLET_STATE_SCHED, &t->state))
					BUG();
				t->func(t->data); 	// 调用该tasklet的处理函数
				tasklet_unlock(t);
				continue;
			}
			tasklet_unlock(t);
		}

		local_irq_disable();
		t->next = NULL;
		*__this_cpu_read(tasklet_vec.tail) = t;
		__this_cpu_write(tasklet_vec.tail, &(t->next));
		// 将当前CPU对应的irq_stat变量中的域__softirq_pending中的标志位TASKLET_SOFTIRQ置位
		__raise_softirq_irqoff(TASKLET_SOFTIRQ);
		local_irq_enable();
	}
}
```

###### 4.3.4.1.4.3.10.2 tasklet_hi_action()

该函数定义于kernel/softirq.c:

```
static void tasklet_hi_action(struct softirq_action *a)
{
	struct tasklet_struct *list;

	local_irq_disable();
	list = __this_cpu_read(tasklet_hi_vec.head);
	__this_cpu_write(tasklet_hi_vec.head, NULL);
	__this_cpu_write(tasklet_hi_vec.tail, &__get_cpu_var(tasklet_hi_vec).head);
	local_irq_enable();

	while (list) {
		struct tasklet_struct *t = list;

		list = list->next;

		if (tasklet_trylock(t)) {
			if (!atomic_read(&t->count)) {
				if (!test_and_clear_bit(TASKLET_STATE_SCHED, &t->state))
					BUG();
				t->func(t->data); 	// 调用该tasklet的处理函数
				tasklet_unlock(t);
				continue;
			}
			tasklet_unlock(t);
		}

		local_irq_disable();
		t->next = NULL;
		*__this_cpu_read(tasklet_hi_vec.tail) = t;
		__this_cpu_write(tasklet_hi_vec.tail, &(t->next));
		__raise_softirq_irqoff(HI_SOFTIRQ);
		local_irq_enable();
	}
}
```

###### 4.3.4.1.4.3.11 vfs_caches_init()

该函数定义于fs/dcache.c:

```
struct kmem_cache *names_cachep __read_mostly;

void __init vfs_caches_init(unsigned long mempages)
{
	unsigned long reserve;

	/* Base hash sizes on available memory, with a reserve equal to
        150% of current kernel size */
	reserve = min((mempages - nr_free_pages()) * 3/2, mempages - 1);
	mempages -= reserve;

	// 参见Create a Specific Cache/kmem_cache_create()节
	names_cachep = kmem_cache_create("names_cache", PATH_MAX, 0,
			SLAB_HWCACHE_ALIGN|SLAB_PANIC, NULL);

	dcache_init();			// 参见dcache_init()节
	inode_init();			// 参见inode_init()节
	files_init(mempages); 	// 参见files_init()节
	mnt_init();			// 参见mnt_init()节
	bdev_cache_init();		// 参见bdev_cache_init()节
	chrdev_init();			// 参见chrdev_init()节
}
```

###### 4.3.4.1.4.3.11.1 dcache_init()

该函数与dcache_init_early()类似，如果在dache_init_early()已经创建了目录项哈希表，则dcache_init()不再创建；否则，创建目录项哈希表。因此，调用了本函数后，目录项哈希表(dentry_hashtable)一定存在了。其定义于fs/dcache.c:

```
static unsigned int d_hash_mask __read_mostly;
static unsigned int d_hash_shift __read_mostly;

static struct hlist_bl_head *dentry_hashtable __read_mostly;
static __initdata unsigned long dhash_entries;

static void __init dcache_init(void)
{
	int loop;

	/*
	 * A constructor could be added for stable state like the lists,
	 * but it is probably not worth it because of the cache nature
	 * of the dcache.
	 */
	dentry_cache = KMEM_CACHE(dentry, SLAB_RECLAIM_ACCOUNT|SLAB_PANIC|SLAB_MEM_SPREAD);

	// 参见dcache_init_early()节
	/* Hash may have been set up in dcache_init_early */
	if (!hashdist)
		return;

	dentry_hashtable = alloc_large_system_hash("Dentry cache",
					sizeof(struct hlist_bl_head),
					dhash_entries,
					13,
					0,
					&d_hash_shift,
					&d_hash_mask,
					0);

	for (loop = 0; loop < (1 << d_hash_shift); loop++)
		INIT_HLIST_BL_HEAD(dentry_hashtable + loop);
}
```

###### 4.3.4.1.4.3.11.2 inode_init()

该函数与inode_init_early()类似，如果在inode_init_early()已经创建了索引节点哈希表，则inode_init()不再创建；否则，创建索引节点哈希表。因此，调用了本函数后，索引节点哈希表(inode_hashtable)一定存在了。其定义于fs/inode.c:

```
static unsigned int i_hash_mask __read_mostly;
static unsigned int i_hash_shift __read_mostly;
static struct hlist_head *inode_hashtable __read_mostly;

static __initdata unsigned long ihash_entries;

void __init inode_init(void)
{
	int loop;

	/* inode slab cache */
	// 参见Create a Specific Cache/kmem_cache_create()节
	inode_cachep = kmem_cache_create("inode_cache",
					 sizeof(struct inode),
					 0,
					 (SLAB_RECLAIM_ACCOUNT|SLAB_PANIC|
					 SLAB_MEM_SPREAD),
					 init_once);

	// 参见inode_init_early()节
	/* Hash may have been set up in inode_init_early */
	if (!hashdist)
		return;

	inode_hashtable = alloc_large_system_hash("Inode-cache",
					sizeof(struct hlist_head),
					ihash_entries,
					14,
					0,
					&i_hash_shift,
					&i_hash_mask,
					0);

	for (loop = 0; loop < (1 << i_hash_shift); loop++)
		INIT_HLIST_HEAD(&inode_hashtable[loop]);
}
```

###### 4.3.4.1.4.3.11.3 files_init()

该函数定义于fs/fs_table.c:

```
/* sysctl tunables... */
struct files_stat_struct files_stat = {
	.max_files = NR_FILE
};

DECLARE_LGLOCK(files_lglock);
DEFINE_LGLOCK(files_lglock);

static struct percpu_counter nr_files __cacheline_aligned_in_smp;

void __init files_init(unsigned long mempages)
{
	unsigned long n;

	// 参见Create a Specific Cache/kmem_cache_create()节
	filp_cachep = kmem_cache_create("filp", sizeof(struct file), 0,
			SLAB_HWCACHE_ALIGN | SLAB_PANIC, NULL);

	/*
	 * One file with associated inode and dcache is very roughly 1K.
	 * Per default don't use more than 10% of our memory for files.
	 */
	n = (mempages * (PAGE_SIZE / 1024)) / 10;
	/*
	 * NR_FILE定义于include/linux/fs.h，取值为8192
	 * max_t()取n和NR_FILE中的最大值
	 */
	files_stat.max_files = max_t(unsigned long, n, NR_FILE);
	files_defer_init();				// 参见files_defer_init()节
	lg_lock_init(files_lglock);			// 实际调用函数files_lglock_lock_init()
	percpu_counter_init(&nr_files, 0);	// 将nr_files.count设置为0
}
```

###### 4.3.4.1.4.3.11.3.1 files_defer_init()

该函数定义于fs/file.c:

```
int sysctl_nr_open_max = 1024 * 1024; /* raised later */

void __init files_defer_init(void)
{
	int i;
	for_each_possible_cpu(i)
		fdtable_defer_list_init(i);
	sysctl_nr_open_max = min((size_t)INT_MAX, ~(size_t)0/sizeof(void *)) & -BITS_PER_LONG;
}
```

其中，fdtable_defer_list_init()用于初始化指定CPU的变量fdtable_defer_list，参见fs/file.c:

```
/*
 * We use this list to defer free fdtables that have vmalloced
 * sets/arrays. By keeping a per-cpu list, we avoid having to embed
 * the work_struct in fdtable itself which avoids a 64 byte (i386) increase in
 * this per-task structure.
 */
static DEFINE_PER_CPU(struct fdtable_defer, fdtable_defer_list);

static void __devinit fdtable_defer_list_init(int cpu)
{
	struct fdtable_defer *fddef = &per_cpu(fdtable_defer_list, cpu);
	spin_lock_init(&fddef->lock);
	// 将fddef->wq.func赋值为free_fdtable_work，用于释放该wq
	INIT_WORK(&fddef->wq, free_fdtable_work);
	fddef->next = NULL;	// 初始化fdtable链表
}
```

变量fdtable_defer_list的结构，参见Subjects/Chapter04_Boot/Figures/fdtable_defer_list.jpg

###### 4.3.4.1.4.3.11.4 mnt_init()

该函数定义于fs/namespace.c:

```
static struct list_head *mount_hashtable __read_mostly;
static struct kmem_cache *mnt_cache __read_mostly;
static struct rw_semaphore namespace_sem;

/* /sys/fs */
struct kobject *fs_kobj;

DEFINE_BRLOCK(vfsmount_lock);

void __init mnt_init(void)
{
	unsigned u;
	int err;

	init_rwsem(&namespace_sem);

	// 参见Create a Specific Cache/kmem_cache_create()节
	mnt_cache = kmem_cache_create("mnt_cache", sizeof(struct vfsmount),
						   0, SLAB_HWCACHE_ALIGN | SLAB_PANIC, NULL);

	mount_hashtable = (struct list_head *)__get_free_page(GFP_ATOMIC);

	if (!mount_hashtable)
		panic("Failed to allocate mount hash table\n");

	printk(KERN_INFO "Mount-cache hash table entries: %lu\n", HASH_SIZE);

	for (u = 0; u < HASH_SIZE; u++)
		INIT_LIST_HEAD(&mount_hashtable[u]);

	br_lock_init(vfsmount_lock);

	/*
	 * 注册并安装sysfs文件系统，参见sysfs_init()节:
	 * - 注册sysfs文件系统后，file_systems链表中添加了一个新元素sysfs_fs_type；
	 * - 安装sysfs文件系统后，生成了sysfs_mnt。通常，sysfs文件系统被安装在/sys下，
	 *   可通过 # mount 命令查看
	 */
	err = sysfs_init();
	if (err)
		printk(KERN_WARNING "%s: sysfs_init error: %d\n", __func__, err);

	// 创建sysfs文件系统的fs子目录，参见kobject_create_and_add()节
	fs_kobj = kobject_create_and_add("fs", NULL);
	if (!fs_kobj)
		printk(KERN_WARNING "%s: kobj create error\n", __func__);

	// 注册rootfs文件系统，参见init_rootfs()节
	init_rootfs();

	// 安装rootfs文件系统，生成系统根目录/，参见init_mount_tree()节和[NOTE]
	init_mount_tree();
}
```

**为什么不直接把真实的文件系统设置为根文件系统?**

答案很简单，因为内核中没有根文件系统的设备驱动，如USB等存放根文件系统的设备驱动，而且即便将根文件系统的设备驱动编译到内核中，此时这些设备驱动还尚未加载，其实所有的设备驱动都是由后面的kernel_init线程加载的，所以需要CPIO initrd, initrd和RAMDisk initrd。另外，root设备都是以设备文件的方式指定的，如果没有根文件系统，设备文件怎么可能存在呢?

```
start_kernel()
-> vfs_caches_init()
   -> mnt_init()
      -> init_mount_tree()			// 设置根文件系统
-> rest_init()
   -> kernel_init()
      -> do_pre_smp_initcalls()		// 加载设备驱动
      -> do_basic_setup()			// 加载设备驱动
```

###### 4.3.4.1.4.3.11.4.1 sysfs_init()

该函数定义于fs/sysfs/mount.c:

```
static struct vfsmount *sysfs_mnt;
struct kmem_cache *sysfs_dir_cachep;

int __init sysfs_init(void)
{
	int err = -ENOMEM;

	// 参见Create a Specific Cache/kmem_cache_create()节
	sysfs_dir_cachep = kmem_cache_create("sysfs_dir_cache", sizeof(struct sysfs_dirent), 0, 0, NULL);
	if (!sysfs_dir_cachep)
		goto out;

	// 调用bdi_init(&sysfs_backing_dev_info)初始化变量sysfs_backing_dev_info，其定义于fs/sysfs/inode.c
	err = sysfs_inode_init();
	if (err)
		goto out_err;

	// 将sysfs文件系统注册到file_systems中，参见注册/注销文件系统节和11.3.5.2 Sysfs的编译及初始化节
	err = register_filesystem(&sysfs_fs_type);
	if (!err) {
		// 安装sysfs文件系统，参见安装文件系统节
		sysfs_mnt = kern_mount(&sysfs_fs_type);
		if (IS_ERR(sysfs_mnt)) {
			printk(KERN_ERR "sysfs: could not mount!\n");
			err = PTR_ERR(sysfs_mnt);
			sysfs_mnt = NULL;
			// 若出错，则从file_systems中注销文件系统sysfs_fs_type，参见注册/注销文件系统节
			unregister_filesystem(&sysfs_fs_type);
			goto out_err;
		}
	} else
		goto out_err;
out:
	return err;
out_err:
	kmem_cache_destroy(sysfs_dir_cachep);
	sysfs_dir_cachep = NULL;
	goto out;
}
```

###### 4.3.4.1.4.3.11.4.2 init_rootfs()

关于rootfs的介绍，参见Documentation/filesystems/ramfs-rootfs-initramfs.txt:

> What is rootfs?
>
> Rootfs is a special instance of ramfs (or tmpfs, if that's enabled), which is always present in 2.6 systems. You can't unmount rootfs for approximately the same reason you can't kill the init process; rather than having special code to check for and handle an empty list, it's smaller and simpler for the kernel to just make sure certain lists can't become empty.
>
> Most systems just mount another filesystem over rootfs and ignore it. The amount of space an empty instance of ramfs takes up is tiny.

一般文件系统的注册都是通过宏module_init以及函数do_initcalls()来完成的，但是rootfs的注册却是通过函数init_rootfs()来完成的，这意味着rootfs的注册过程是Linux内核初始化阶段不可分割的一部分！

函数init_rootfs()定义于fs/ramfs/inode.c:

```
int __init init_rootfs(void)
{
	int err;

	// 初始化变量ramfs_backing_dev_info
	err = bdi_init(&ramfs_backing_dev_info);
	if (err)
		return err;

	/*
	 * 将rootfs文件系统注册到file_systems中，
	 * 参见注册/注销文件系统节和11.3.2.2 Rootfs编译与初始化及安装过程节
	 */
	err = register_filesystem(&rootfs_fs_type);
	if (err)
		bdi_destroy(&ramfs_backing_dev_info);

	return err;
}
```

###### 4.3.4.1.4.3.11.4.3 init_mount_tree()

该函数定义于fs/namespace.c:

```
static void __init init_mount_tree(void)
{
	struct vfsmount *mnt;
	struct mnt_namespace *ns;
	struct path root;

	/*
	 * 文件系统rootfs的注册，参见do_kern_mount()节；
	 * 此过程中调用了rootfs_mount()，参见rootfs_mount()节
	 */
	mnt = do_kern_mount("rootfs", 0, "rootfs", NULL);
	if (IS_ERR(mnt))
		panic("Can't create rootfs");

	// 创建新的namespace，并与mnt链接起来，参见Filesystem_20.jpg中红色框
	ns = create_mnt_ns(mnt);
	if (IS_ERR(ns))
		panic("Can't allocate initial namespace");

	init_task.nsproxy->mnt_ns = ns;		// 设置INIT进程的根目录
	get_mnt_ns(ns);					// 增加ns->count计数

	root.mnt = ns->root;
	root.dentry = ns->root->mnt_root;

	// 设置当前进程的current->fs->pwd
	set_fs_pwd(current->fs, &root);

	// 设置当前进程的current->fs->root, 即将当前的文件系统设置为根文件系统
	set_fs_root(current->fs, &root);
}
```

函数init_mount_tree()执行后的数据结构，参见Subjects/Chapter04_Boot/Figures/init_mount_tree().jpg

此后，由init_task进程fork出来的子进程也继承了init_task->nsproxy->mnt_ns信息，参见copy_process()节中的:

```
retval = copy_fs(clone_flags, p);
```

综上，函数init_mount_tree()为VFS建立了根目录"/"，而一旦有了根目录，那么这棵树就可以发展壮大，例如: 可以通过系统调用sys_mkdir在这棵树上建立新的叶子节点等。

###### 4.3.4.1.4.3.11.5 bdev_cache_init()

* 字符设备初始化函数之一：bdev_cache_init()，参见本节
* 字符设备初始化函数之二：genhd_device_init()，参见【[10.4.2 块设备的初始化/genhd_device_init()](#)节

该函数定义于fs/block_dev.c:

```
static  __cacheline_aligned_in_smp DEFINE_SPINLOCK(bdev_lock);
static struct kmem_cache * bdev_cachep __read_mostly;

static struct file_system_type bd_type = {
	.name		= "bdev",
	/*
	 * bd_mount()通过如下函数被调用，参见节：
	 * bdev_cache_init()->kern_mount()->kern_mount_data()
	 * ->vfs_kern_mount()->mount_fs()中的type->mount()
	 */
	.mount	= bd_mount,
	.kill_sb	= kill_anon_super,
};

struct super_block *blockdev_superblock __read_mostly;

void __init bdev_cache_init(void)
{
	int err;
	struct vfsmount *bd_mnt;

	// 创建块设备缓存，参见Create a Specific Cache/kmem_cache_create()节
	bdev_cachep = kmem_cache_create("bdev_cache", sizeof(struct bdev_inode), 0,
 			 (SLAB_HWCACHE_ALIGN|SLAB_RECLAIM_ACCOUNT|SLAB_MEM_SPREAD|SLAB_PANIC), init_once);

	// 注册bdev文件系统到file_systems，参见注册/注销文件系统节
	err = register_filesystem(&bd_type);
	if (err)
		panic("Cannot register bdev pseudo-fs");

	// 安装bdev文件系统，参见安装文件系统节
	bd_mnt = kern_mount(&bd_type);
	if (IS_ERR(bd_mnt))
		panic("Cannot create bdev pseudo-fs");
	/*
	 * This vfsmount structure is only used to obtain the
	 * blockdev_superblock, so tell kmemleak not to report it.
	 */
	kmemleak_not_leak(bd_mnt);
	blockdev_superblock = bd_mnt->mnt_sb;	/* For writeback */
}
```

###### 4.3.4.1.4.3.11.6 chrdev_init()

* 字符设备初始化函数之一：chrdev_init()，参见本节
* 字符设备初始化函数之二：chr_dev_init()，参见[10.3.2 字符设备的初始化/chr_dev_init()](#)节

该函数定义于fs/char_dev.c:

```
struct backing_dev_info directly_mappable_cdev_bdi = {
	.name = "char",
	.capabilities	= (
#ifdef CONFIG_MMU
		/* permit private copies of the data to be taken */
		BDI_CAP_MAP_COPY |
#endif
		/* permit direct mmap, for read, write or exec */
		BDI_CAP_MAP_DIRECT |
		BDI_CAP_READ_MAP | BDI_CAP_WRITE_MAP | BDI_CAP_EXEC_MAP |
		/* no writeback happens */
		BDI_CAP_NO_ACCT_AND_WRITEBACK),
};

static struct kobj_map *cdev_map;
static DEFINE_MUTEX(chrdevs_lock);

void __init chrdev_init(void)
{
	/*
	 * 变量cdev_map在如下函数中被访问：
	 * - cdev_map(), 参见10.3.3.3.3.1 cdev_add()节
	 * - kobj_lookup(), 参见10.3.3.3.4.1 kobj_lookup()节
	 */
	cdev_map = kobj_map_init(base_probe, &chrdevs_lock);
	bdi_init(&directly_mappable_cdev_bdi);
}
```

初始化完成后的数据结构:

Subjects/Chapt er10_Device_Driver/01_Char_Device/Figures/chrdevs[]\_2.jpg

图中struct probe的域data指向struct cdev类型的对象，由函数cdev_add()设置，参见[10.3.3.3.3.1 cdev_add()](#)节。

###### 4.3.4.1.4.3.12 proc_root_init()

该函数定义于fs/proc/root.c:

```
static struct file_system_type proc_fs_type = {
	.name		= "proc",
	.mount	= proc_mount,	// 参见proc_mount()节
	.kill_sb	= proc_kill_sb,
};

struct pid_namespace init_pid_ns = {
	.kref = {
		.refcount	= ATOMIC_INIT(2),
	},
	.pidmap = {
		[ 0 ... PIDMAP_ENTRIES-1] = { ATOMIC_INIT(BITS_PER_PAGE), NULL }
	},
	.last_pid		= 0,
	.level		= 0,
	// 初始化进程描述符，参见进程0/swapper, swapper/0, swapper/1, ...节
	.child_reaper	= &init_task,
};

void __init proc_root_init(void)
{
	int err;

	// 分配缓存空间proc_inode_cachep
	proc_init_inodecache();
	// 注册proc文件系统，参见注册/注销文件系统节
	err = register_filesystem(&proc_fs_type);
	if (err)
		return;
	/*
	 * 通过调用kern_mount_data()来安装proc文件系统，
	 * 参见安装文件系统(1)/kern_mount()节和proc_mount()节
	 */
	err = pid_ns_prepare_proc(&init_pid_ns);
	if (err) {
		unregister_filesystem(&proc_fs_type);
		return;
	}

	/*
	 * 创建/proc/mounts到/proc/self/mounts的链接，即/proc/mounts -> /proc/self/mounts
	 * 通过命令 # cat /proc/mounts，可以查看当前系统中安装的文件系统，参见具体的文件系统节
	 */
	proc_symlink("mounts", NULL, "self/mounts");

	// 创建/proc/net到/proc/self/net的链接，即/proc/net -> /proc/self/net
	proc_net_init();

#ifdef CONFIG_SYSVIPC
	proc_mkdir("sysvipc", NULL);	// 创建/proc/sysvipc目录
#endif
	proc_mkdir("fs", NULL);		// 创建/proc/fs目录
	proc_mkdir("driver", NULL);		// 创建/proc/drivers目录
	// 创建/proc/fs/nfsd目录
	proc_mkdir("fs/nfsd", NULL);	/* somewhere for the nfsd filesystem to be mounted */
#if defined(CONFIG_SUN_OPENPROMFS) || defined(CONFIG_SUN_OPENPROMFS_MODULE)
	/* just give it a mountpoint */
	proc_mkdir("openprom", NULL);	// 创建/proc/openprom目录
#endif
	/*
	 * 创建目录: /proc/tty, /proc/tty/ldisc, /proc/tty/driver,
	 * /proc/tty/ldiscs, /proc/tty/drivers
	 */
	proc_tty_init();
#ifdef CONFIG_PROC_DEVICETREE
	proc_device_tree_init();		// 创建/proc/device-tree目录
#endif
	proc_mkdir("bus", NULL);		// 创建/proc/bus目录
	proc_sys_init();				// 创建/proc/sys目录
}
```

###### 4.3.4.1.4.3.13 rest_init()

在start_kernel()函数的最后，调用rest_init()函数进行后续的初始化。在init/main.c中，包含如下有关rest_init()的代码：

```
static __initdata DECLARE_COMPLETION(kthreadd_done);     // 定义并初始化变量kthreadd_done

...
static noinline void __init_refok rest_init(void)
{
	int pid;

	rcu_scheduler_starting();
	/*
	 * We need to spawn init first so that it obtains pid 1, however
	 * the init task will end up wanting to create kthreads, which, if
	 * we schedule it before we create kthreadd, will OOPS.
	 */
	/*
	 * 调用kernel_thread()创建pid=1的内核线程，即init线程，参见kernel_thread()节。
	 * 该线程将执行kernel_init()函数，参见kernel_init()节
	 */
	kernel_thread(kernel_init, NULL, CLONE_FS | CLONE_SIGHAND);
	numa_default_policy();
	/*
	 * 调用kernel_thread()创建pid=2的内核线程，即kthreadd线程，参见kernel_thread()节。
	 * 该线程执行kthreadd()函数，参见kthreadd()节。
	 * 对于全局链表kthread_create_list中的每一项，执行函数kthread()
	 */
	pid = kernel_thread(kthreadd, NULL, CLONE_FS | CLONE_FILES);
	rcu_read_lock();
	// kthreadd_task的定义参见kernel/kthread.c: struct task_struct *kthreadd_task;
	kthreadd_task = find_task_by_pid_ns(pid, &init_pid_ns);
	rcu_read_unlock();
	// 通知kernel_init进程，kthreadd已经完成，参见kernel_init()节
	complete(&kthreadd_done);

	/*
	 * The boot idle thread must execute schedule()
	 * at least once to get things moving:
	 */
	init_idle_bootup_task(current);
	preempt_enable_no_resched();	// 与配置CONFIG_PREEMPT_COUNT有关，参见include/linux/preempt.h
	schedule();				// 如果存在一个准备好的进程，则运行它；否则，调用下面的cpu_init()函数

	/* Call into cpu_idle with preempt disabled */
	preempt_disable();			// 与配置CONFIG_PREEMPT_COUNT有关，参见preempt_disable()节
	cpu_idle();				// 参见cpu_idle()节
}
```

###### 4.3.4.1.4.3.13.1 kernel_init()

该函数定义于init/main.c：

```
static int __init kernel_init(void * unused)
{
	/*
	 * Wait until kthreadd is all set-up.
	 */
	// 等待kthreadd完成，参见rest_init()节中的语句rest_init() -> complete(&kthreadd_done)
	wait_for_completion(&kthreadd_done);
	/*
	 * init can allocate pages on any node
	 */
	set_mems_allowed(node_states[N_HIGH_MEMORY]);
	/*
	 * init can run on any cpu.
	 */
	set_cpus_allowed_ptr(current, cpu_all_mask);

	cad_pid = task_pid(current);

	smp_prepare_cpus(setup_max_cpus);

	do_pre_smp_initcalls();		// 参见do_pre_smp_initcalls()节
	lockup_detector_init();

	smp_init();
	sched_init_smp();

	do_basic_setup();			// 参见do_basic_setup()节

	/* Open the /dev/console on the rootfs, this should never fail */
	if (sys_open((const char __user *) "/dev/console", O_RDWR, 0) < 0)
		printk(KERN_WARNING "Warning: unable to open an initial console.\n");

	(void) sys_dup(0);
	(void) sys_dup(0);

	/*
	 * check if there is an early userspace init.  If yes, let it do all
	 * the work
	 */
	/*
	 * 内核参数"rdinit="用于设置ramdisk_execute_command，
	 * 参见init/main.c:rdinit_setup();
	 * 若无内核参数"rdinit="，则设置ramdisk_execute_command="/init"，
	 * 即initrd.img中的init，参见init_post()节
	 */
	if (!ramdisk_execute_command)
		ramdisk_execute_command = "/init";

	/*
	 * 若ramdisk_execute_command指定的初始化程序不存在，
	 * 则复位ramdisk_execute_command = NULL;
	 * 以避免init_post()执行该初始化程序，参见init_post()节
	 */
	if (sys_access((const char __user *) ramdisk_execute_command, 0) != 0) {
		ramdisk_execute_command = NULL;
		prepare_namespace();		// 参见prepare_namespace()节
	}

	/*
	 * Ok, we have completed the initial bootup, and
	 * we're essentially up and running. Get rid of the
	 * initmem segments and start the user-mode stuff..
	 */
	init_post();				// 参见init_post()节
	return 0;
}
```

###### 4.3.4.1.4.3.13.1.1 do_pre_smp_initcalls()

该函数定义于init/main.c:

```
extern initcall_t __initcall_start[], __initcall_end[], __early_initcall_end[];

static void __init do_pre_smp_initcalls(void)
{
	initcall_t *fn;

	for (fn = __initcall_start; fn < __early_initcall_end; fn++)
		do_one_initcall(*fn);		// 参见do_one_initcall()节
}
```

###### 4.3.4.1.4.3.13.1.2 do_basic_setup()

该函数定义于init/main.c:

```
static void __init do_basic_setup(void)
{
	cpuset_init_smp();
	usermodehelper_init();	// 参见13.3.2.2.1 khelper_wq节
	shmem_init();
	driver_init();			// 参见10.2.1 设备驱动程序的初始化/driver_init()节
	init_irq_proc();
	do_ctors();
	usermodehelper_enable();
	do_initcalls();			// 参见module被编译进内核时的初始化过程节
}
```

###### 4.3.4.1.4.3.13.1.3 prepare_namespace()

该函数定义于init/do_mounts.c:

```
/*
 * Prepare the namespace - decide what/where to mount, load ramdisks, etc.
 */
void __init prepare_namespace(void)
{
	int is_floppy;

	/*
	 * 对于将根文件系统存放到USB或者SCSI设备上的情况，Kernel需要
	 * 等待这些耗时比较久的设备驱动加载完毕，故此处存在一个root_delay
	 *
	 * 内核参数"rootdelay="设置root_delay，
	 * 参见init/do_mounts.c中的root_delay_setup()
	 */
	if (root_delay) {
		printk(KERN_INFO "Waiting %dsec before mounting root device...\n", root_delay);
		ssleep(root_delay);
	}

	/*
	 * wait for the known devices to complete their probing
	 *
	 * Note: this is a potential source of long boot delays.
	 * For example, it is not atypical to wait 5 seconds here
	 * for the touchpad of a laptop to initialize.
	 */
	wait_for_device_probe();

	md_run_setup();

	/*
	 * 根据内核参数"root="来设置saved_root_name[]，
	 * 参见init/do_mounts.c中的root_dev_setup().
	 *
	 * Set the root_device_name variable with the device
	 * filename obtained from the "root" boot parameter.
	 * Also, sets the ROOT_DEV variable with the major
	 * and minor numbers of the same device file.
	 *
	 * 内核参数"root="可通过下列命令查看：
	 * chenwx@chenwx ~ $ cat /proc/cmdline
	 * BOOT_IMAGE=/boot/vmlinuz-3.11.0-12-generic     \
	 * root=UUID=fe67c2d0-9b0f-4fd6-8e97-463ce95a7e0c \
	 * ro quiet splash vt.handoff=7
	 */
	if (saved_root_name[0]) {
		root_device_name = saved_root_name;
		/*
		 * Try #1: 若内核参数"root="代表的字符串以"mtd"或"ubi"开头，
		 * 则调用mount_block_root()解析该内核参数
		 */
		if (!strncmp(root_device_name, "mtd", 3) || !strncmp(root_device_name, "ubi", 3)) {
			mount_block_root(root_device_name, root_mountflags);
			goto out;
		}
		/*
		 * Try #2: 若内核参数"root="代表的字符串以"/dev/"或"PARTUUID="开头，
		 * 则将/dev/<disk_name>转换为Device Number.
		 * 参见源代码中对函数name_to_dev_t()的注释。
		 */
		ROOT_DEV = name_to_dev_t(root_device_name);
		if (strncmp(root_device_name, "/dev/", 5) == 0)
			root_device_name += 5;
	}

	/*
	 * Try #3: 若内核参数"root="代表的字符串以"UUID=<uuid>"开头，
	 * 则需要加载initrd.image，并由其中的init程序(参见kernel_init()节)
	 * 负责解析"root="字符串"UUID=<uuid>"，并挂在相应的设备。
	 *
	 * 函数initrd_load()用于加载映像/boot/initrd.img-3.11.0-12-generic，
	 * 参见CONFIG_BLK_DEV_INITRD=y节
	 *
	 * 可通过下列命令解压initrd.img映像：
	 *   $ mv initrd.img-3.11.0-12-generic initrd.img.gz
	 *   $ gunzip initrd.img.gz
	 *   $ cpio -i -d < initrd.img
	 *   $ rm -rf initrd.img
	 *   $ ls
	 *   bin  conf  etc  init  lib  run  sbin  scripts  usr  var
	 */
	if (initrd_load())
		goto out;

	/*
	 * 内核参数"rootwait"设置root_wait，
	 * 参见init/do_mounts.c中的rootwait_setup()
	 */
	/* wait for any asynchronous scanning to complete */
	if ((ROOT_DEV == 0) && root_wait) {
		printk(KERN_INFO "Waiting for root device %s...\n", saved_root_name);
		while (driver_probe_done() != 0 || (ROOT_DEV = name_to_dev_t(saved_root_name)) == 0)
			msleep(100);
		async_synchronize_full();
	}

	is_floppy = MAJOR(ROOT_DEV) == FLOPPY_MAJOR;

	if (is_floppy && rd_doload && rd_load_disk(0))
		ROOT_DEV = Root_RAM0;

	// 根据ROOT_DEV挂载根文件系统，参见下文；
	mount_root();
out:
	// 挂载devtmpfs文件系统，参见Devtmpfs的安装节
	devtmpfs_mount("dev");
	/*
	 * Moves the mount point of the mounted filesystem on the root
	 * directory of the rootfs filesystem.
	 * Notice that the rootfs special filesystem cannot be unmounted,
	 * it's only hidden under the disk-based root filesystem.
	 * 系统调用sys_mount()参见安装文件系统(2)/sys_mount()节，
	 * 文件系统rootfs参见虚拟文件系统(VFS)的初始化节
	 */
	sys_mount(".", "/", NULL, MS_MOVE, NULL);
	sys_chroot((const char __user __force *)".");
}
```

其中，函数mount_root()定义于init/do_mounts.c:

```
void __init mount_root(void)
{
#ifdef CONFIG_ROOT_NFS
	if (MAJOR(ROOT_DEV) == UNNAMED_MAJOR) {
		if (mount_nfs_root())
			return;

		printk(KERN_ERR "VFS: Unable to mount root fs via NFS, trying floppy.\n");
		ROOT_DEV = Root_FD0;
	}
#endif
#ifdef CONFIG_BLK_DEV_FD
	if (MAJOR(ROOT_DEV) == FLOPPY_MAJOR) {
		/* rd_doload is 2 for a dual initrd/ramload setup */
		if (rd_doload==2) {
			if (rd_load_disk(1)) {
				ROOT_DEV = Root_RAM1;
				root_device_name = NULL;
			}
		} else
			change_floppy("root floppy");
	}
#endif
#ifdef CONFIG_BLOCK
	create_dev("/dev/root", ROOT_DEV);
	mount_block_root("/dev/root", root_mountflags);
#endif
}
```

###### 4.3.4.1.4.3.13.1.4 init_post()

该函数定义于init/main.c:

```
/* This is a non __init function. Force it to be noinline otherwise gcc
 * makes it inline to init() and it becomes part of init.text section
 */
static noinline int init_post(void)
{
	/* need to finish all async __init code before freeing the memory */
	async_synchronize_full();
	free_initmem();		// 参见early_node_map[]=>node_data[]->node_zones[]节
	mark_rodata_ro();
	system_state = SYSTEM_RUNNING;
	numa_default_policy();

	current->signal->flags |= SIGNAL_UNKILLABLE;

	/*
	 * Try #1: 启动ramdisk_execute_command指定的初始化程序，
	 *         其取值参见kernel_init()节的kernel_init():
	 *         a) 由内核参数"rdinit="指定，或者
	 *         b) /init(此初始化程序由initrd.img加载而来，
	 *            参见prepare_namespace()节的Try #3)
	 * 若该进程成功，则转到用户空间；否则，继续尝试
	 */
	if (ramdisk_execute_command) {
		run_init_process(ramdisk_execute_command);
		printk(KERN_WARNING "Failed to execute %s\n", ramdisk_execute_command);
	}

	/*
	 * We try each of these until one succeeds.
	 *
	 * The Bourne shell can be used instead of init if we are
	 * trying to recover a really broken machine.
	 */
	// Try #2: 启动execute_command指定的初始化程序：
	// 由内核参数"init="指定，参见init/main.c中的函数init_setup()
	if (execute_command) {
		run_init_process(execute_command);
		printk(KERN_WARNING "Failed to execute %s.  Attempting defaults...\n", execute_command);
	}
	/*
	 * 依次尝试启动如下初始化程序。若其中之一启动成功，
	 * 则转到用户空间；否则，继续尝试。参见init节
	 */
	run_init_process("/sbin/init");	// Try #3: /sbin/init
	run_init_process("/etc/init");	// Try #4: /etc/init
	run_init_process("/bin/init");	// Try #5: /bin/init
	/*
	 * 若上述init均不存在或无法启动，则启动shell，即/bin/sh;
	 * 若成功，则转到用户空间；否则，终止启动内核
	 */
	run_init_process("/bin/sh");	// Try #6: /bin/sh

	panic("No init found.  Try passing init= option to kernel. "
		   "See Linux Documentation/init.txt for guidance.");
}
```

###### 4.3.4.1.4.3.13.2 kthreadd()

在kernel/kthread.c中，包含如下有关kthreadd()的代码(另参见[kthreadd进程](#)节)：

```
static LIST_HEAD(kthread_create_list);

int kthreadd(void *unused)
{
	struct task_struct *tsk = current;

	/* Setup a clean context for our children to inherit. */
	set_task_comm(tsk, "kthreadd");				// 设置程序名称为kthreadd，参见程序名称节
	ignore_signals(tsk); 						// 忽略所有信号
	set_cpus_allowed_ptr(tsk, cpu_all_mask);
	set_mems_allowed(node_states[N_HIGH_MEMORY]);

	current->flags |= PF_NOFREEZE | PF_FREEZER_NOSIG;

	for (;;) {
		set_current_state(TASK_INTERRUPTIBLE); 	// 设置当前进程为可中断睡眠状态
		// 如果链表kthread_create_list为空，则当前进程进入睡眠状态
		if (list_empty(&kthread_create_list))
			schedule();
		// 如果链表kthread_create_list不为空，则设置当前进程为运行状态
		__set_current_state(TASK_RUNNING);

		spin_lock(&kthread_create_lock);
		while (!list_empty(&kthread_create_list)) {
			struct kthread_create_info *create;

			// 获取链表kthread_create_list中的一项，用于创建指定的内核线程
			create = list_entry(kthread_create_list.next, struct kthread_create_info, list);
			list_del_init(&create->list);
			spin_unlock(&kthread_create_lock);

			// 创建指定的内核线程，该线程执行函数kthread()，参见kthread_run()节
			create_kthread(create);

			spin_lock(&kthread_create_lock);
		}
		spin_unlock(&kthread_create_lock);
	}

	return 0;
}
```

###### 4.3.4.1.4.3.13.3 cpu_idle()

在arch/x86/kernel/process_32.c中，包含如下有关cpu_idle()的代码：

```
/*
 * The idle thread. There's no useful work to be
 * done, so just try to conserve power and have a
 * low exit latency (ie sit in a loop waiting for
 * somebody to say that they'd like to reschedule)
 */
void cpu_idle(void)
{
	int cpu = smp_processor_id();

	/*
	 * If we're the non-boot CPU, nothing set the stack canary up
	 * for us.  CPU0 already has it initialized but no harm in
	 * doing it again.  This is a good place for updating it, as
	 * we wont ever return from this function (so the invalid
	 * canaries already on the stack wont ever trigger).
	 */
	boot_init_stack_canary();

	current_thread_info()->status |= TS_POLLING;

	/* endless idle loop with no priority at all */
	while (1) {
		tick_nohz_stop_sched_tick(1);
		while (!need_resched()) {

			check_pgt_cache();
			rmb();

			if (cpu_is_offline(cpu))
				play_dead();

			local_touch_nmi();
			local_irq_disable();
			/* Don't trace irqs off for idle */
			stop_critical_timings();
			if (cpuidle_idle_call())
				pm_idle();
			start_critical_timings();
		}
		tick_nohz_restart_sched_tick();
		// 与rest_init()中调用schedule()函数的方式类似，参见rest_init()节
		preempt_enable_no_resched();
		// 如果存在一个准备好的进程，则运行它
		schedule();
		// 与rest_init()中调用schedule()函数的方式类似，参见rest_init()节
		preempt_disable();
	}
}
```

### 4.3.5 init

当内核被引导并进行初始化之后，内核就可以启动第一个用户级进程：init进程，其进程号为1。这是系统第一个调用的、使用标准C库编译的程序。此前，还没有执行任何标准的C应用程序。

init进程的启动过程参见[init_post()](#)节。若无法启动init进程，则打印错误信息：```No init found```. 参见Documentation/init.txt。

调用函数run_init_process()来启动init进程，其定义于init/main.c:

```
static const char * argv_init[MAX_INIT_ARGS+2] = { "init", NULL, };
const char * envp_init[MAX_INIT_ENVS+2] = { "HOME=/", "TERM=linux", NULL, };

// 由init_post()节可知，入参init_filename依次为"/sbin/init", "/etc/init", "/bin/init"
static void run_init_process(const char *init_filename)
{
	argv_init[0] = init_filename;
	kernel_execve(init_filename, argv_init, envp_init);
}
```

其中，函数kernel_execve()定义于arch/x86/kernel/sys_i386_32.c:

```
/*
 * Do a system call from kernel instead of calling sys_execve so we
 * end up with proper pt_regs.
 */
int kernel_execve(const char *filename,
		  const char *const argv[],
		  const char *const envp[])
{
	long __res;
	asm volatile ("int $0x80"
		: "=a" (__res)
		: "0" (__NR_execve), "b" (filename), "c" (argv), "d" (envp) : "memory");
	return __res;
}
```

函数kernel_execve()调用系统调用sys_execve()，参见[sys_execve()/exec()](#)节；另参见<<Linux Device Drivers, 2nd Edition>>第16章:

> The final call to execve finalizes the transition to user space. There is no magic involved in this transition. As with any execve call in Unix, this one replaces the memory maps of the current process with new memory maps defined by the binary file being executed. It doesn’t matter that, in this case, the calling process is running in kernel space. That’s transparent to the implementation of execve, which just finds that there are no previous memory maps to release before activating the new ones.
>
> Whatever the system setup or command line, the init process is now executing in user space and any further kernel operation takes place in response to system calls coming from init itself or from the processes it forks out.

#### 4.3.5.1 init的种类

The design of init has diverged in Unix systems, such as System III and System V, from the functionality provided by the init in Research Unix and its BSD derivatives. The usage on most Linux distributions is somewhat compatible with System V, but some distributions, such as Slackware, use a BSD-style and others, such as Gentoo, have their own customized version.

Several replacement init implementations have been written with attempt to address design limitations in the standard versions. These include systemd and Upstart, the latter being used by Ubuntu and some other Linux distributions.

Refer to article "init system other points, and conclusion" in:

* [https://lwn.net/Articles/578209/](https://lwn.net/Articles/578209/)
* [https://lwn.net/Articles/578210/](https://lwn.net/Articles/578210/)

##### 4.3.5.1.1 SysV-style init

System V init examines the /etc/inittab file for an :initdefault: entry, which defines any default runlevel. If there is no default runlevel, then init dumps the user to a system console for manual entry of a runlevel.

/etc/inittab用于设定runlevel，例如:

```
#
# inittab     This file describes how the INIT process should set up
#               the system in a certain run-level.
#
# Author:     Miquel van Smoorenburg, <miquels@drinkel.nl.mugnet.org>
#               Modified for RHS Linux by Marc Ewing and Donnie Barnes
#

# Default runlevel. The runlevels used by RHS are:
#   0 - halt (Do NOT set initdefault to this)
#   1 - Single user mode
#   2 - Multiuser, without NFS (The same as 3, if you do not have networking)
#   3 - Full multiuser mode
#   4 - unused
#   5 - X11
#   6 - reboot (Do NOT set initdefault to this)
#
id:3:initdefault:

# System initialization.
si::sysinit:/etc/rc.d/rc.sysinit

l0:0:wait:/etc/rc.d/rc 0
l1:1:wait:/etc/rc.d/rc 1
l2:2:wait:/etc/rc.d/rc 2
l3:3:wait:/etc/rc.d/rc 3
l4:4:wait:/etc/rc.d/rc 4
l5:5:wait:/etc/rc.d/rc 5
l6:6:wait:/etc/rc.d/rc 6

# Trap CTRL-ALT-DELETE
#ca::ctrlaltdel:/sbin/shutdown -t3 -r now
# s+c disable_abort_keys_tdsc start
ca::ctrlaltdel:/usr/local/etc/acknowledge_ctrlaltdel
# s+c disable_abort_keys_tdsc end

# When our UPS tells us power has failed, assume we have a few minutes
# of power left.  Schedule a shutdown for 2 minutes from now.
# This does, of course, assume you have powerd installed and your
# UPS connected and working correctly.  
pf::powerfail:/sbin/shutdown -f -h +2 "Power Failure; System Shutting Down"

# If power was restored before the shutdown kicked in, cancel it.
pr:12345:powerokwait:/sbin/shutdown -c "Power Restored; Shutdown Cancelled"

# Run gettys in standard runlevels
1:2345:respawn:/sbin/mingetty tty1
2:2345:respawn:/sbin/mingetty tty2
3:2345:respawn:/sbin/mingetty tty3
4:2345:respawn:/sbin/mingetty tty4
5:2345:respawn:/sbin/mingetty tty5
6:2345:respawn:/sbin/mingetty tty6

# Run xdm in runlevel 5
x:5:respawn:/etc/X11/prefdm -nodaemon
```

###### 4.3.5.1.1.1 runlevel

Linux的runlevel取值如下：

| runlevel | Note |
| :------: | :--- |
| 0 | 关机 |
| 1 | 单用户模式 |
| 2 | 无网络支持的多用户模式 |
| 3 | 有网络支持的多用户模式 |
| 4 | 保留 |
| 5 | 有网络支持的X-Window支持的多用户模式 |
| 6 | 重新引导系统，即重启 |

<p/>

Default runlevels for different Linux distributions:

| Operating System | Default runlevel |
| :--------------- | :--------------- |
| AIX | 2 |
| CentOS | 3 (console/server), or<br>5 (graphical/desktop) |
| Debian | 2 |
| Gentoo Linux | 3 |
| HP-UX | 3 (console/server/multiuser), or<br>4 (graphical) |
| Mac OS X | 3 |
| Mandriva Linux | 3 (console/server), or<br>5 (graphical/desktop) |
| Red Hat Enterprise Linux / Fedora | 3 (console/server), or<br>5 (graphical/desktop) |
| Slackware Linux | 3 |
| Solaris | 3 |
| SUSE Linux Enterprise/openSUSE Linux | 3 (console/server), or<br>5 (graphical/desktop) |
| Ubuntu (Server and Desktop) | 2 |

<p/>

On most systems users can check the current runlevel with either of the following commands:

```
chenwx@chenwx ~ $ runlevel
N 2
chenwx@chenwx ~ $ who -r
         run-level 2  2014-04-14 21:26
```

##### 4.3.5.1.2 BSD-style init

BSD init runs the initialization shell script located in /etc/rc, then launches getty on text-based terminals or a windowing system such as X on graphical terminals under the control of /etc/ttys. There are no runlevels; the /etc/rc file determines what programs are run by init. The advantage of this system is that it is simple and easy to edit manually. However, new software added to the system may require changes to existing files that risk producing an unbootable system. To mitigate this, BSD variants have long supported a site-specific /etc/rc.local file that is run in a sub-shell near the end of the boot sequence.

A fully modular system was introduced with NetBSD 1.5 and ported to FreeBSD 5.0 and successors. This system executes scripts in the /etc/rc.d directory. Unlike System V's script ordering, which is derived from the filename of each script, this system uses explicit dependency tags placed within each script. The order in which scripts are executed is determined by the rcorder script based on the requirements stated in these tags.

init进程是非内核进程中第一个被启动运行的，因此它的进程号pid总是1。init读取配置文件/etc/inittab，决定需要启动的运行级别。从根本上说，运行级别规定了整个系统的行为，每个级别满足特定的目的。如果定义了initdefault级别，则直接使用该值，否则需要由用户输入一个代表运行级别的数值。

输入代表运行级别的数字之后，init根据/etc/inittab中的定义执行一个命令脚本程序。缺省的运行级别取决于安装阶段对登录程序的选择：是使用基于文本的，还是使用基于X-Window的登录程序。

当运行级别发生改变时，将根据/etc/inittab中的定义运行一个命令脚本程序。这些命令脚本程序负责启动或者停止该运行级别特定的各种服务。由于需要管理的服务数量很多，因此需要使用rc命令脚本程序。其中，最主要的一个是/etc/rc.d/rc，它负责为每一个运行级别按照正确的顺序调用相应的命令脚本程序。可以想象，这样一个命令脚本程序很容易变得难以控制！为了防止这类事件的发生，需要使用精心设计的方案。

```
/etc/rc.d
|-- rc.sysinit
|-- rc
|-- init.d
|-- nohup.out
|-- rc.local
|-- rc0.d
|-- rc1.d
|-- rc2.d
|-- rc3.d
|-- rc4.d
|-- rc5.d
`-- rc6.d
```

对每一个运行级别来说，在/etc/rc.d子目录中都有一个对应的下级目录。这些运行级别的下级子目录的命名方法是rcX.d，其中X代表运行级别。例如：运行级别3的全部命令脚本程序都保存在/etc/rc.d/rc3.d子目录中。在各个运行级别的子目录中，都建立有到/etc/rc.d/init.d子目录中命令脚本程序的符号链接，但是，这些符号链接并不使用命令脚本程序在/etc/rc.d/init.d子目录中原来的名字。如果命令脚本程序是用来启动一个服务的，其符号链接的名字就以字母S打头；如果命令脚本程序是用来关闭一个服务的，其符号链接的名字就以字母K打头。

许多情况下，这些命令脚本程序的执行顺序都很重要。如果没有先配置网络接口，就没有办法使用DNS服务解析主机名！为了安排它们的执行顺序，在字母S或者K的后面紧跟着两位数字，数值小的在数值大的前面执行。如：/etc/rc.d/rc3.d/S50inet就会在/etc/rc.d/rc3.d/S55named之前执行(S50inet配置网络设置，55named启动DNS服务器)。存放在/etc/rc.d/init.d子目录中的、被符号链接上的命令脚本程序是真正的实干家，是它们完成了启动或者停止各种服务的操作过程。当/etc/rc.d/rc运行通过每个特定的运行级别子目录的时候，它会根据数字的顺序依次调用各个命令脚本程序执行。它先运行以字母K打头的命令脚本程序，然后再运行以字母S打头的命令脚本程序。对以字母K打头的命令脚本程序来说，会传递stop参数；类似地对以字母S打头的命令脚本程序来说，会传递start参数。编写自己的rc命令脚本在维护Linux系统运转时，肯定会遇到需要系统管理员对开机或者关机命令脚本进行修改的情况。

##### 4.3.5.1.3 Replacements for init

**Rational**

The traditional init process was originally only responsible for bringing the computer into a normal running state after power-on, or gracefully shutting down services prior to shutdown. As a result, the design is strictly synchronous, blocking future tasks until the current one has completed. Its tasks must also be defined in advance, as they are limited to this prep or cleanup function. This leaves it unable to handle various non-startup-tasks on a modern desktop computer elegantly, including:

* The addition or removal of USB pen drives and other portable storage / network devices while the machine is running;
* The discovery and scanning of new storage devices, without locking the system, especially when a disk may not even power on until it is scanned;
* The loading of firmware for a device, which may need to occur after it is detected but before it is usable.

**Description of replacements for init**

Traditionally, one of the major drawbacks of init is that it starts tasks serially, waiting for each to finish loading before moving on to the next. When startup processes end up I/O blocked, this can result in long delays during boot.

Various efforts have been made to replace the traditional init daemons to address this and other design problems, including:

| Replacements for init | Notes |
| :-------------------- | :---- |
| BootScripts | used in GoboLinux |
| busybox-init | suited embedded operating systems, employed by OpenWrt before it was replaced with procd |
| DEMONS | a modification of the init start process by KahelOS, where daemons are started only when the DE (desktop environment) started |
| eINIT | a full replacement of init designed to start processes asynchronously, but with the potential of doing it without shell scripts |
| Initng | a full replacement of init designed to start processes asynchronously |
| launchd | a replacement for init introduced in Mac OS X v10.4 (it launches SystemStarter to run old-style 'rc.local' and SystemStarter processes) |
| Mudur | an init replacement written in Python and designed to start process asynchronously in use by the Pardus Linux distribution |
| runit | a cross-platform full replacement for init with parallel starting of services |
| s6 | another cross-platform full replacement for init, similar to runit |
| Service Management Facility | a complete full replacement/redesign of init from the ground up in Solaris starting with Solaris 10 |
| systemd | a full replacement for init with parallel starting of services and other features, used by many distributions |
| SystemStarter | a process spawner started by the BSD-style init in Mac OS X prior to Mac OS X v10.4 |
| Upstart | a full replacement of init designed to start processes asynchronously initiated by Ubuntu |

<p/>

###### 4.3.5.1.3.1 upstart

[upstart](http://upstart.ubuntu.com) is an event-based replacement for the /sbin/init daemon which handles starting of tasks and services during boot, stopping them during shutdown and supervising them while the system is running. That means upstart operates asynchronously.

It was originally developed for the Ubuntu distribution, but is intended to be suitable for deployment in all Linux distributions as a replacement for the venerable System-V init.

Easy transition and perfect backwards compatibility with sysvinit were the explicit design goals; accordingly, Upstart can run unmodified sysvinit scripts. In this way it differs from most other init replacements (beside systemd and OpenRC), which usually assume and require complete transition to run properly, and do not support a mixed environment of traditional and new startup methods.

Upstart allows for extensions to its event model through the use of initctl to input custom, single events, or event bridges to integrate many or more-complicated events. By default, Upstart includes bridges for socket, dbus, udev, file, and dconf events; additionally, more bridges (for example, a Mach ports bridge, or a devd (found on FreeBSD systems) bridge) are possible.

UpStart提供了一系列命令来完成管理系统服务的工作，其中的核心命令是initctl，这是一个带子命令风格的命令行工具：

```
chenwx@chenwx ~ $ initctl version
init (upstart 1.12.1)
chenwx@chenwx ~ $ initctl list
avahi-cups-reload stop/waiting
avahi-daemon start/running, process 532
mountall-net stop/waiting
mountnfs-bootclean.sh start/running
nmbd start/running, process 1637
passwd stop/waiting
rc stop/waiting
rsyslog start/running
...
```

###### 4.3.5.1.3.2 systemd

[systemd](http://freedesktop.org/wiki/Software/systemd/) is a suite of basic building blocks for a Linux system. It provides a system and service manager that runs as PID 1 and starts the rest of the system. systemd provides aggressive parallelization capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, keeps track of processes using Linux control groups, supports snapshotting and restoring of the system state, maintains mount and automount points and implements an elaborate transactional dependency-based service control logic. systemd supports SysV and LSB init scripts and works as a replacement for sysvinit. Other parts include a logging daemon, utilities to control basic system configuration like the hostname, date, locale, maintain a list of logged-in users and running containers and virtual machines, system accounts, runtime directories and settings, and daemons to manage simple network configuration, network time synchronization, log forwarding, and name resolution.

Because it's a system daemon, and under Unix/Linux those are in lower case, and get suffixed with a lower case d. And since systemd manages the system, it's called systemd.

systemd software architecture:

* Subjects/Chapter04_Boot/Figures/systemd_components.png
* Subjects/Chapter04_Boot/Figures/unified_hierarchy_cgroups_and_systemd.png

Git repository

* git://anongit.freedesktop.org/systemd/systemd
* ssh://git.freedesktop.org/git/systemd/systemd

###### 4.3.5.1.3.2.1 systemd的配置文件

systemd的配置文件放置在下面的目录中：

/usr/lib/systemd/system/: 每个服务最主要的启动脚本设置，类似于以前的/etc/init.d下的文件。

/run/systemd/system/: 系统执行过程中所产生的服务脚本，这些脚本的执行优先级要比/usr/lib/systemd/system/目录下的高。

/etc/systemd/system/: 系统管理员根据系统的需求所创建的执行脚本，类似于以前的/etc/rd.d/rc5.d/Sxx之类的功能。这些脚本的执行优先级要比/run/systemd/system/目录下的高。

故，系统开机时会不会执行某些服务其实是看/etc/systemd/system/下面的设置，所以该目录下是一些链接文件，而实际执行的配置文件都放置在/usr/lib/systemd/system/目录下面。

#### 4.3.5.2 查看当前系统使用的init

执行下列命令查看当前子系统中的init进程：
chenwx@chenwx ~ $ init --version
init (upstart 1.12.1)
Copyright (C) 2006-2014 Canonical Ltd., 2011 Scott James Remnant

This is free software; see the source for copying conditions.  There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

或者，init进程更改为systemd:

```
chenwx@chenwx ~ $ lsb_release -a
No LSB modules are available.
Distributor ID:	LinuxMint
Description:	Linux Mint 18 Sarah
Release:	18
Codename:	sarah

chenwx@chenwx ~ $ ll /sbin/init
lrwxrwxrwx 1 root root 20 Jul 13 00:28 /sbin/init -> /lib/systemd/systemd

chenwx@chenwx ~ $ systemd --version
systemd 229
+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ -LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN
```

# 5 系统调用接口 (System Call Interface)

* [Linux System Call Interface](http://syscalls.kernelgrok.com/)

系统调用帮助：

```
# man 2 system_call_name
# man 2 syscalls
```

系统调用在内核源代码中的声明：

```
- include/linux/syscalls.h			- 与体系架构无关
- include/asm-generic/syscalls.h		- 与体系架构无关
- arch/x86/include/asm/syscalls.h		- 与体系架构有关
- include/asm-generic/unistd.h			- 与体系架构无关
- include/linux/unistd.h			- 与体系架构有关
  - arch/x86/include/asm/unistd.h
- arch/x86/include/asm/unistd_32.h		- 定义系统调用号__NR_xxxx
```

* [API changes in the 2.6 kernel series](http://lwn.net/Articles/2.6-kernel-api/)

## 5.1 系统调用简介

Linux内核中设置了一组用于实现各种系统功能的子程序，称为系统调用。用户可以在应用程序中调用系统调用。从某种角度来看，系统调用和普通函数非常相似，区别仅在于：系统调用由操作系统内核提供，运行于核心态；而普通函数由函数库或者用户提供，运行于用户态。

随Linux核心还提供了一些C语言函数库，这些库对系统调用进行了包装和扩展。因为这些库函数与系统调用的关系非常紧密，所以习惯上也把这些函数称为系统调用。

The POSIX standard refers to APIs and not to system calls. A system can be certified as POSIX-compliant if it offers the proper set of APIs to the application programs, no matter how the corresponding functions are implemented. As a matter of fact, several non-Unix systems have been certified as POSIX-compliant, because they offer all traditional Unix services in User Mode libraries.

Linux system architecture:

![assets/Linux_System_Architecture](/assets/Linux_System_Architecture.jpg)

## 5.2 系统调用的执行过程

系统调用的执行过程:

![System_Call_Procedure](/assets/System_Call_Procedure.jpg)

其中，系统调用处理程序为arch/x86/kernel/entry_32.S中的system_call，参见[5.4 系统调用的处理程序/system_call](#5-4-system-call)节。sys_call_table为arch/x86/kernel/syscall_table_32.S中的sys_call_table，参见[5.5.3 系统调用表/sys_call_table](#5-5-3-sys-call-table)节。

## 5.3 系统调用的初始化

对系统调用的初始化，也就是对INT 0x80软中断的初始化。在系统启动时，下列函数将0x80软中断的处理程序设置为system_call:

```
start_kernel()							// 参见4.3.4.1.4.3 start_kernel()节
-> trap_init()							// 参见4.3.4.1.4.3.5 trap_init()节
   -> set_system_trap_gate(SYSCALL_VECTOR, &system_call)	// 设置0x80软中断的处理程序为system_call
```

因而，system_call就是所有系统调用的入口点，参见[5.4 系统调用的处理程序/system_call](#5-4-system-call)节。

## 5.4 系统调用的处理程序/system_call

系统调用的处理程序为system_call，其定义于arch/x86/kernel/entry_32.S:

```
// 该宏表示sys_call_table中系统调用的个数
#define nr_syscalls ((syscall_table_size)/4)

/*
 * syscall stub including irq exit should be protected against kprobes
 */
	.pushsection .kprobes.text, "ax"
	# system call handler stub
// 系统调用处理程序，由trap_init()设置，参见5.3 系统调用的初始化节
ENTRY(system_call)
	RING0_INT_FRAME					# can't unwind into user space anyway
	pushl_cfi %eax					# save orig_eax
	SAVE_ALL
	GET_THREAD_INFO(%ebp)				# system call tracing in operation / emulation
	testl $_TIF_WORK_SYSCALL_ENTRY,TI_flags(%ebp)
	jnz syscall_trace_entry
	cmpl $(nr_syscalls), %eax
	jae syscall_badsys
syscall_call:
	/*
	 * 根据eax寄存器中的系统调用号(参见5.5.2 系统调用号/__NR_xxx节)，
	 * 调用sys_call_table中对应的系统调用，其等价于： call near [eax*4+sys_call_table]
	 * 参见Subjects/Chapter05_System_Call_Interface/Figures/系统调用过程.jpg中的①
	 */
	call *sys_call_table(,%eax,4)
	movl %eax,PT_EAX(%esp)				# store the return value
syscall_exit:
	LOCKDEP_SYS_EXIT
	DISABLE_INTERRUPTS(CLBR_ANY)			# make sure we don't miss an interrupt
							# setting need_resched or sigpending
							# between sampling and the iret
	TRACE_IRQS_OFF
	movl TI_flags(%ebp), %ecx
	testl $_TIF_ALLWORK_MASK, %ecx			# current->work
	jne syscall_exit_work				// 从系统调用返回
...
ENDPROC(system_call)

...
	# perform syscall exit tracing
	ALIGN
syscall_exit_work:
	testl $_TIF_WORK_SYSCALL_EXIT, %ecx
	jz work_pending
	TRACE_IRQS_ON
	ENABLE_INTERRUPTS(CLBR_ANY)			# could let syscall_trace_leave() call schedule() instead
	movl %esp, %eax
	call syscall_trace_leave
	jmp resume_userspace				// 从内核空间返回到用户空间
END(syscall_exit_work)

...
.section .rodata,"a"
/*
 * arch/x86/kernel/syscall_table_32.S定义了sys_call_table，
 * 其中包含系统调用号与系统调用函数的对应关系；
 * 而系统调用函数的声明包含在include/linux/syscalls.h，
 * 参见5.5.1 系统调用的声明与定义节
 */
#include "syscall_table_32.S"

// 获得sys_call_table的大小，即字节数
syscall_table_size=(.-sys_call_table)
```

## 5.5 系统调用

### 5.5.1 系统调用的声明与定义

系统调用的格式为：asmlinkage long sys_XXX(...)，由如下宏来定义系统调用：

```
- SYSCALL_DEFINE0(name)			// 没有入参
- SYSCALL_DEFINE1(name, ...)		// 1个入参
- SYSCALL_DEFINE2(name, ...) 		// 2个入参
- SYSCALL_DEFINE3(name, ...) 		// 3个入参
- SYSCALL_DEFINE4(name, ...) 		// 4个入参
- SYSCALL_DEFINE5(name, ...) 		// 5个入参
- SYSCALL_DEFINE6(name, ...) 		// 6个入参
```

该宏定义于include/linux/syscalls.h:

```
/*
 * 1) 定义系统调用的宏
 */

#define __SC_DECL1(t1, a1)		t1 a1
#define __SC_DECL2(t2, a2, ...)		t2 a2, __SC_DECL1(__VA_ARGS__)
#define __SC_DECL3(t3, a3, ...)		t3 a3, __SC_DECL2(__VA_ARGS__)
#define __SC_DECL4(t4, a4, ...)		t4 a4, __SC_DECL3(__VA_ARGS__)
#define __SC_DECL5(t5, a5, ...)		t5 a5, __SC_DECL4(__VA_ARGS__)
#define __SC_DECL6(t6, a6, ...)		t6 a6, __SC_DECL5(__VA_ARGS__)

#ifdef CONFIG_FTRACE_SYSCALLS
#define SYSCALL_DEFINE0(sname)						\
	SYSCALL_TRACE_ENTER_EVENT(_##sname);				\
	SYSCALL_TRACE_EXIT_EVENT(_##sname);				\
	static struct syscall_metadata __used				\
	  __syscall_meta__##sname = {					\
		.name 		= "sys_"#sname,				\
		.syscall_nr	= -1,	/* Filled in at boot */		\
		.nb_args 		= 0,				\
		.enter_event	= &event_enter__##sname,		\
		.exit_event	= &event_exit__##sname,			\
		.enter_fields	= LIST_HEAD_INIT(__syscall_meta__##sname.enter_fields),	\
	};								\
	static struct syscall_metadata __used				\
	  __attribute__((section("__syscalls_metadata")))	        \
	 *__p_syscall_meta_##sname = &__syscall_meta__##sname;		\
	asmlinkage long sys_##sname(void)
#else
#define SYSCALL_DEFINE0(name)		asmlinkage long sys_##name(void)
#endif

#define SYSCALL_DEFINE1(name, ...) 	SYSCALL_DEFINEx(1, _##name, __VA_ARGS__)
#define SYSCALL_DEFINE2(name, ...) 	SYSCALL_DEFINEx(2, _##name, __VA_ARGS__)
#define SYSCALL_DEFINE3(name, ...) 	SYSCALL_DEFINEx(3, _##name, __VA_ARGS__)
#define SYSCALL_DEFINE4(name, ...) 	SYSCALL_DEFINEx(4, _##name, __VA_ARGS__)
#define SYSCALL_DEFINE5(name, ...) 	SYSCALL_DEFINEx(5, _##name, __VA_ARGS__)
#define SYSCALL_DEFINE6(name, ...) 	SYSCALL_DEFINEx(6, _##name, __VA_ARGS__)

#ifdef CONFIG_FTRACE_SYSCALLS
#define SYSCALL_DEFINEx(x, sname, ...)					\
	static const char *types_##sname[] = {				\
		__SC_STR_TDECL##x(__VA_ARGS__)				\
	};								\
	static const char *args_##sname[] = {				\
		__SC_STR_ADECL##x(__VA_ARGS__)				\
	};								\
	SYSCALL_METADATA(sname, x);					\
	__SYSCALL_DEFINEx(x, sname, __VA_ARGS__)
#else
#define SYSCALL_DEFINEx(x, sname, ...)					\
	__SYSCALL_DEFINEx(x, sname, __VA_ARGS__)
#endif

#ifdef CONFIG_HAVE_SYSCALL_WRAPPERS
#define SYSCALL_DEFINE(name) static inline long SYSC_##name
#define __SYSCALL_DEFINEx(x, name, ...)					\
	asmlinkage long sys##name(__SC_DECL##x(__VA_ARGS__));		\
	static inline long SYSC##name(__SC_DECL##x(__VA_ARGS__));	\
	asmlinkage long SyS##name(__SC_LONG##x(__VA_ARGS__))		\
	{								\
		__SC_TEST##x(__VA_ARGS__);				\
		return (long) SYSC##name(__SC_CAST##x(__VA_ARGS__));	\
	}								\
	SYSCALL_ALIAS(sys##name, SyS##name);				\
	static inline long SYSC##name(__SC_DECL##x(__VA_ARGS__))
#else /* CONFIG_HAVE_SYSCALL_WRAPPERS */
#define SYSCALL_DEFINE(name) asmlinkage long sys_##name
#define __SYSCALL_DEFINEx(x, name, ...)					\
	asmlinkage long sys##name(__SC_DECL##x(__VA_ARGS__))
#endif /* CONFIG_HAVE_SYSCALL_WRAPPERS */

/*
 * 1) 所有系统调用的声明
 */

asmlinkage long sys_restart_syscall(void);
...
asmlinkage long sys_exit(int error_code);
...
```

系统调用的定义分布于内核源代码多个源文件中，参见[http://syscalls.kernelgrok.com/](http://syscalls.kernelgrok.com/).

**关键字asmlinkage的意义**

This is a directive to tell the compiler to look only on the stack for this function’s arguments. This is a required modifier for all system calls.

**为什么返回值为long**

For compatibility between 32- and 64-bit systems, system calls defined to return an int in user-space return a long in the kernel.

### 5.5.2 系统调用号/\_\_NR_xxx

系统调用的声明节中的每个系统调用xxx都对应着一个系统调用号__NR_xxx。当应用程序调用某系统调用时，寄存器eax中保存该系统调用对应的系统调用号。系统调用号定义于如下头文件中：

```
include/linux/unistd.h
+-  arch/x86/include/asm/unistd.h
    +-  arch/x86/include/asm/unistd_32.h
    |   +-  ...
    |   +-  #define __NR_process_vm_writev  348
    |   +-  #define NR_syscalls             349
    +-  arch/x86/include/asm/unistd_64.h
        +-  ...
        +-  #define __NR_process_vm_writev  311
        +-  __SYSCALL(__NR_process_vm_writev, sys_process_vm_writev)
```

在应用程序中仅需包含如下头文件即可：

```
#include <unistd.h>
```

include/linux/unistd.h:

```
#ifndef _LINUX_UNISTD_H_
#define _LINUX_UNISTD_H_

/*
 * Include machine specific syscall numbers
 */
#include <asm/unistd.h>

#endif /* _LINUX_UNISTD_H_ */
```

对于x86而言，asm/unistd.h即为arch/x86/include/asm/unistd.h:

```
#ifdef __KERNEL__
#  ifdef CONFIG_X86_32
#    include "unistd_32.h"
#  else
#    include "unistd_64.h"
#  endif
#else
#  ifdef __i386__
#    include "unistd_32.h"
#  else
#    include "unistd_64.h"
#  endif
#endif

对于x86 32-bit而言，unistd_32.h即为arch/x86/include/asm/unistd_32.h:
#define __NR_restart_syscall		0
#define __NR_exit			1
#define __NR_fork			2
#define __NR_read			3
#define __NR_write			4
#define __NR_open			5
#define __NR_close			6
...
#define __NR_process_vm_readv		347
#define __NR_process_vm_writev		348

#ifdef __KERNEL__
#define NR_syscalls			349
#endif
```

对于x86 64-bit而言，unistd_64.h即为arch/x86/include/asm/unistd_64.h:

```
#define __NR_read				0
__SYSCALL(__NR_read, sys_read)
#define __NR_write				1
__SYSCALL(__NR_write, sys_write)
#define __NR_open				2
__SYSCALL(__NR_open, sys_open)
#define __NR_close				3
__SYSCALL(__NR_close, sys_close)
...
#define __NR_process_vm_readv			310
__SYSCALL(__NR_process_vm_readv, sys_process_vm_readv)
#define __NR_process_vm_writev			311
__SYSCALL(__NR_process_vm_writev, sys_process_vm_writev)

#ifdef __KERNEL__

#ifndef COMPILE_OFFSETS
#include <asm/asm-offsets.h>
#define NR_syscalls		(__NR_syscall_max + 1)
#endif

#endif
```

### 5.5.3 系统调用表/sys_call_table

通过[5.5.2 系统调用号/\_\_NR_xxx](#5-5-2-nr-xxx)节的系统调用号，在系统调用表sys_call_table中查找所对应的处理函数。

对于x86 32-bit而言，系统调用表sys_call_table定义于arch/x86/kernel/syscall_table_32.S:

```
ENTRY(sys_call_table)
	.long sys_restart_syscall		/* 0 - old "setup()" system call, used for restarting */
	.long sys_exit
	.long ptregs_fork
	.long sys_read
	.long sys_write
	.long sys_open				/* 5 */
	.long sys_close

	...
	.long sys_sendmmsg			/* 345 */
	.long sys_setns
	.long sys_process_vm_readv
	.long sys_process_vm_writev
```

对于x86 64-bit而言，系统调用表sys_call_table定义于arch/x86/kernel/syscall_64.c:

```
typedef void (*sys_call_ptr_t)(void);

extern void sys_ni_syscall(void);

const sys_call_ptr_t sys_call_table[__NR_syscall_max+1] = {
	/*
	 * Smells like a like a compiler bug -- it doesn't work
	 * when the & below is removed.
	 */
	[0 ... __NR_syscall_max] = &sys_ni_syscall,

// 参见5.5.2 系统调用号/__NR_xxx节
#include <asm/unistd_64.h>
};
```

### 5.5.4 系统调用的参数传递

#### 5.5.4.1 系统调用的入参

参见《Linux Kernel Development.[3rd Edition].[Robert Love]》第5. System Calls章第System Call Handler节:

Simply entering kernel-space alone is not sufficient because multiple system calls exist, all of which enter the kernel in the same manner. Thus, the system call number must be passed into the kernel. On x86, the syscall number is fed to the kernel via the eax register.

In addition to the system call number, most syscalls require that one or more parameters be passed to them. Somehow, user-space must relay the parameters to the kernel during the trap. The easiest way to do this is via the same means that the syscall number is passed: The parameters are stored in registers. On x86-32, the registers ebx, ecx, edx, esi, and edi contain, in order, the first five arguments. In the unlikely case of six or more arguments, a single register is used to hold a pointer to user-space where all the parameters are stored.

#### 5.5.4.2 系统调用的返回值

参见《Linux Kernel Development.[3rd Edition].[Robert Love]》第5. System Calls章第System Call Handler节:

The return value is sent to user-space also via register. On x86, it is written into the **eax** register.

如果系统调用执行失败，系统调用并不直接返回错误码，而是将错误码保存到全局变量errno中，因而可根据errno的值来确定错误类型。错误码定义于如下头文件中：

```
include/linux/errno.h				// 错误码512-530
- arch/x86/include/asm/errno.h			// 仅包含asm-generic/errno.h，未新增错误码
  - include/asm-generic/errno.h			// 错误码35-133
    - include/asm-generic/errno-base.h		// 错误码1-34
```

也可以执行下列命令获得errno的帮助：

```
# man errno
```

注意：只有当系统调用执行失败时才会设置全局变量errno；如果系统调用执行成功，则errno的值无定义，并不会被置为0。

#### 5.5.4.3 用户空间和内核空间之间的参数传递

参见《Linux Kernel Development.[3rd Edition].[Robert Love]》第5. System Calls章第System Call Implementation节:

For writing into user-space, the method copy_to_user() is provided. It takes three parameters. The first is the destination memory address in the process’s address space. The second is the source pointer in kernel-space. Finally, the third argument is the size in bytes of the data to copy.

For reading from user-space, the method copy_from_user() is analogous to copy_to_user(). The function reads from the second parameter into the first parameter the number of bytes specified in the third parameter.

Both of these functions return the number of bytes they failed to copy on error. On success, they return zero. It is standard for the syscall to return -EFAULT in the case of such an error. The EFAULT is defined in include/asm-generic/errno-base.h. 参见[5.5.4.2 系统调用的返回值](#5-5-4-2-)节:

```
#define EFAULT	14		/* Bad address */
```

##### 5.5.4.3.1 copy_from_user()

要使用函数copy_from_user()，需要包含头文件uaccess.h。内核目录中存在如下两个头文件，其访问顺序参见[3.4.2.1.3.1.1.1.1 编译$(obj)目录下的目标文件](#3-4-2-1-3-1-1-1-1-obj-)节。

* arch/x86/include/asm/uaccess.h
* include/asm-generic/uaccess.h

1) 在arch/x86/include/asm/uaccess.h中，存在如下包含关系：

```
...
#ifdef CONFIG_X86_32
# include "uaccess_32.h"
#else
# include "uaccess_64.h"
#endif
```

arch/x86/include/asm/uaccess_32.h:

```
static inline unsigned long __must_check copy_from_user(void *to, const void __user *from, unsigned long n)
{
	// 获取to指向内存区的大小，参见5.5.4.3.1.1 __compiletime_object_size()节
	int sz = __compiletime_object_size(to);

	if (likely(sz == -1 || sz >= n))
		n = _copy_from_user(to, from, n);	// 验证from指向内存区的可读性，并进行拷贝
	else
		copy_from_user_overflow();		// 打印错误信息：Buffer overflow detected!

	return n;
}
```

arch/x86/include/asm/uaccess_64.h:

```
static inline unsigned long __must_check copy_from_user(void *to, const void __user *from, unsigned long n)
{
	int sz = __compiletime_object_size(to);

	might_fault();					// 调用might_sleep()
	if (likely(sz == -1 || sz >= n))
		n = _copy_from_user(to, from, n);	// 验证from指向内存区的可读性，并进行拷贝
#ifdef CONFIG_DEBUG_VM
	else
		WARN(1, "Buffer overflow detected!\n");
#endif
	return n;
}
```

2) include/asm-generic/uaccess.h:

```
static inline long copy_from_user(void *to, const void __user * from, unsigned long n)
{
	might_sleep();
	if (access_ok(VERIFY_READ, from, n))
		return __copy_from_user(to, from, n);
	else
		return n;
}
```

###### 5.5.4.3.1.1 \_\_compiletime_object_size()

该宏定义于include/linux/compiler-gcc4.h:

```
#if __GNUC_MINOR__ > 0
#define __compiletime_object_size(obj)		__builtin_object_size(obj, 0)
#endif
```

其中，```__builtin_object_size()```为GCC的内置函数，参见《Using the GNU Compiler Collection (GCC) v4.1.2》第5 Extensions to the C Language Family章第5.45 Object Size Checking Builtins节：

```
size_t __builtin_object_size(void * ptr, int type)
is a built-in construct that returns a constant number of bytes from ptr to the end of the object ptr pointer points to (if known at compile time). __builtin_object_size never evaluates its arguments for side-effects.
```

##### 5.5.4.3.2 copy_to_user()

要使用函数copy_to_user()，需要包含头文件uaccess.h。内核目录中存在如下两个头文件，其访问顺序参见[3.4.2.1.3.1.1.1.1 编译$(obj)目录下的目标文件](#3-4-2-1-3-1-1-1-1-obj-)节。

* arch/x86/include/asm/uaccess.h
* include/asm-generic/uaccess.h

在arch/x86/include/asm/uaccess.h中，存在如下包含关系：

1) arch/x86/include/asm/uaccess_32.h:

```
// 此处为声明，其定义于arch/x86/lib/usercopy_32.c
unsigned long __must_check copy_to_user(void __user *to, const void *from, unsigned long n);
```

arch/x86/lib/usercopy_32.c:

```
/**
 * copy_to_user: - Copy a block of data into user space.
 * @to:   Destination address, in user space.
 * @from: Source address, in kernel space.
 * @n:    Number of bytes to copy.
 *
 * Context: User context only.  This function may sleep.
 *
 * Copy data from kernel space to user space.
 *
 * Returns number of bytes that could not be copied.
 * On success, this will be zero.
 */
unsigned long copy_to_user(void __user *to, const void *from, unsigned long n)
{
	if (access_ok(VERIFY_WRITE, to, n))
		n = __copy_to_user(to, from, n);
	return n;
}
```

arch/x86/include/asm/uaccess_64.h:

```
static __always_inline __must_check int copy_to_user(void __user *dst, const void *src, unsigned size)
{
	might_fault();
	return _copy_to_user(dst, src, size);
}
```

2) include/asm-generic/uaccess.h:

```
static inline long copy_to_user(void __user *to, const void *from, unsigned long n)
{
	// 若to指向的区域(或磁盘区)为调入内存，则进程休眠，并调度其他进程运行
	might_sleep();
	// 验证to指向内存区的可写性，并进行拷贝
	if (access_ok(VERIFY_WRITE, to, n))
		return __copy_to_user(to, from, n);
	else
		return n;
}
```

##### 5.5.4.3.3 simple_write_to_buffer()

该函数声明于include/linux/fs.h:

```
extern ssize_t simple_write_to_buffer(void *to, size_t available, loff_t *ppos,
				      const void __user *from, size_t count);
```

该函数定义于fs/libfs.c:

```
/**
 * simple_write_to_buffer - copy data from user space to the buffer
 * @to: the buffer to write to
 * @available: the size of the buffer
 * @ppos: the current position in the buffer
 * @from: the user space buffer to read from
 * @count: the maximum number of bytes to read
 *
 * The simple_write_to_buffer() function reads up to @count bytes from the user
 * space address starting at @from into the buffer @to at offset @ppos.
 *
 * On success, the number of bytes written is returned and the offset @ppos is
 * advanced by this number, or negative value is returned on error.
 **/
ssize_t simple_write_to_buffer(void *to, size_t available, loff_t *ppos,
			       const void __user *from, size_t count)
{
	loff_t pos = *ppos;
	size_t res;

	if (pos < 0)
		return -EINVAL;
	if (pos >= available || !count)
		return 0;
	if (count > available - pos)
		count = available – pos;
	// 参见5.5.4.3.2 copy_from_user()节，该函数返回未成功拷贝的字节数
	res = copy_from_user(to + pos, from, count);
	if (res == count)
		return -EFAULT;
	count -= res;
	*ppos = pos + count;
	return count;
}
```

##### 5.5.4.3.4 simple_read_from_buffer()

该函数声明于include/linux/fs.h:

```
extern ssize_t simple_read_from_buffer(void __user *to, size_t count,
				       loff_t *ppos, const void *from,
				       size_t available);
```

该函数定义于fs/libfs.c:

```
/**
 * simple_read_from_buffer - copy data from the buffer to user space
 * @to: the user space buffer to read to
 * @count: the maximum number of bytes to read
 * @ppos: the current position in the buffer
 * @from: the buffer to read from
 * @available: the size of the buffer
 *
 * The simple_read_from_buffer() function reads up to @count bytes from the
 * buffer @from at offset @ppos into the user space address starting at @to.
 *
 * On success, the number of bytes read is returned and the offset @ppos is
 * advanced by this number, or negative value is returned on error.
 **/
ssize_t simple_read_from_buffer(void __user *to, size_t count, loff_t *ppos,
				const void *from, size_t available)
{
	loff_t pos = *ppos;
	size_t ret;

	if (pos < 0)
		return -EINVAL;
	if (pos >= available || !count)
		return 0;
	if (count > available - pos)
		count = available – pos;
	// 参见5.5.4.3.2 copy_to_user()节，该函数返回未成功拷贝的字节数
	ret = copy_to_user(to, from + pos, count);
	if (ret == count)
		return -EFAULT;
	count -= ret;
	*ppos = pos + count;
	return count;
}
```

## 5.6 如何新增系统调用/v3.2

可以通过如下两种方法为Linux Kernel新增系统调用：

* 通过修改内核源代码新增系统调用；
* 通过内核模块新增系统调用。

相比而言，采用内核模块新增系统调用的方法较好，因为它不需要重新编译内核。

下面以新增系统调用long sys_testsyscall()为例，分别介绍这两种方法。

### 5.6.1 通过修改内核源代码新增系统调用

**1) 确定新增的系统调用号**

修改如下文件来确定新增系统调用的系统调用号，并将其加入系统调用表中：

* 修改arch/x86/include/asm/unistd_32.h，为新增的系统调用定义的系统调用号：

```
#define _NR_testsyscall 350
```

* 修改arch/x86/kernel/syscall_table_32.S，将新增的系统调用加入到系统调用表，即数组sys_call_table中：

```
long sys_testsyscall  /* 350 */
```

**2) 编写新增的系统调用**

编写一个系统调用意味着要给内核增加一个函数，将该函数写入文件kernel/sys.c中，代码如下：

```
SYSCALL_DEFINE0(testsyscall)
{
	console_print("hello world\n");
	return 0;
}
```

**3) 使用新增的系统调用**

因为C库中没有新增的系统调用的程序段，必须自己建立其代码，如下：

```
#inculde <syscalls.h>

SYSCALL_DEFINE0(testsyscall)

void main()
{
    tsetsyscall();
}
```

### 5.6.2 通过内核模块新增系统调用

模块是内核的一部分，但是并没有被编译到内核中。它们被分别编译并连接成一组目标文件，这些文件能被插入到正在运行的内核，或者从正在运行的内核中移走。内核模块至少必须有2个函数：int_module和cleanup_module。第一个函数是在把模块插入内核时调用的； 第二个函数则在删除该模块时调用。

由于内核模块是内核的一部分，所以能访问所有内核资源。根据对linux系统调用机制的分析，如果要新增系统调用，可以编写自己的函数来实现，然后在sys_call_table表中增加一项，使该项中的指针指向自己编写的函数，就可以实现系统调用。

**1) 编写系统调用内核模块**

```
#inculde <linux/kernel.h>
#inculde <linux/module.h>
#inculde <linux/modversions.h>
#inculde <linux/sched.h>
#inculde <asm/uaccess.h>

#define _NR_testsyscall 350

extern void *sys_call_table[];

asmlinkage long testsyscall()
{
    printf("hello world\n");
    return 0;
}

int init_module()
{
    sys_call_table[_NR_tsetsyscall] = testsyscall;
    printf("system call testsyscall() loaded success\n");
    return 0;
}

void cleanup_module()
{
}
```

**2) 使用新增的系统调用**

```
#define <linux/unistd.h>
#define _NR_testsyscall 350

SYSCALL_DEFINE0(testsyscall)

main()
{
    testsyscall();
}
```

**3) 编译内核模块并插入内核**

编译内核的命令为：

```
# gcc -Wall -02 -DMODULE -D_KERNEL_-C syscall.c
```

-Wall通知编译程序显示警告信息；参数-O2是关于代码优化的设置，内核模块必须优化；参数-D_LERNEL通知头文件向内核模块提供正确的定义；参数-D_KERNEL_通知头文件， 这个程序代码将在内核模式下运行。编译成功后将生成syscall.o文件。最后使用命令：

```
# insmod syscall.o
```

命令将模块插入内核后，即可使用新增的系统调用。

## 5.7 如何使用系统调用

程序员使用系统调用的方式：

* 直接调用系统调用
* 通过库函数(如glibc)间接调用系统调用

系统管理员使用系统调用的方式：

* 通过系统命令调用系统调用

### 5.7.1 程序员使用系统调用

程序员可以直接调用系统调用，也可以通过库函数间接地调用系统调用，参见：

![syscall_1](/assets/syscall_1.jpg)

![syscall_2](/assets/syscall_2.jpg)

#### 5.7.1.1 直接调用系统调用

直接调用系统调用示例如下：

```
#include <sys/syscall.h>	// 定义系统调用号SYS_xxx，此处为：#define SYS_getpid  __NR_getpid
#include <unistd.h>		// 定义系统调用号__NR_xxx，此处__NR_getpid取值为20
#include <sys/types.h>		// 定义基本类型，此处用pid_t

int main(int argc, char *argv[])
{
    // syscall()参见帮助 # man 2 syscall，此处实际调用sys_getpid()
    pid_t pid = syscall(SYS_getpid);
    return 0;
}
```

在命令行中执行下列命令查看帮助：

```
# man 2 syscall
SYSCALL(2)                  BSD System Calls Manual                 SYSCALL(2)

NAME
     syscall - indirect system call

SYNOPSIS
     #include <sys/syscall.h>
     #include <unistd.h>

     int syscall(int number, ...);

DESCRIPTION
     Syscall() performs the system call whose assembly language interface has the specified
     number with the specified arguments. Symbolic constants for system calls can be found
     in the header file <sys/syscall.h>.

RETURN VALUES
     The return value is defined by the system call being invoked. In general, a 0 return value
     indicates success.  A -1 return value indicates an error, and an error code is stored in errno.

HISTORY
     The syscall() function call appeared in 4.0BSD.

4BSD                             June 16, 1993                            4BSD
```

#### 5.7.1.2 通过库函数间接调用系统调用

可以通过库函数(如glibc)间接调用系统调用，示例如下：

```
#include <sys/types.h>	// 定义基本类型，此处用pid_t

int main(int argc, char *argv[])
{
   /*
    * 调用库函数getpid()，参见《The GNU C Library Reference Manual》
    * 中第26.3 Process Identification节
    */
    pid_t pid = getpid();
    return 0;
}
```

### 5.7.2 系统管理员使用系统调用

系统命令相对编程接口(API)更高一层，它是内部引用API的可执行程序，如系统命令ls、hostname等。Linux的系统命令格式遵循System V的传统，多数放在/bin和/sbin目录下。

Linux kernel提供了一种非常有用的方法来跟踪某个进程所调用的系统调用，以及该进程所接收到的信号：strace，它可以在命令行中执行，参数为希望跟踪的应用程序。

[举例] 执行strace hostname以查看hostname使用的系统调用，由此可知hostname使用了诸如open、brk、fstat等系统调用：

```
chenwx@chenwx ~/alex $ strace hostname
execve("/bin/hostname", ["hostname"], [/* 36 vars */]) = 0
brk(0)                                  = 0x995c000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
mmap2(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xb76ee000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat64(3, {st_mode=S_IFREG|0644, st_size=83840, ...}) = 0
mmap2(NULL, 83840, PROT_READ, MAP_PRIVATE, 3, 0) = 0xb76d9000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/i386-linux-gnu/libnsl.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\1\1\1\0\0\0\0\0\0\0\0\0\3\0\3\0\1\0\0\0`1\0\0004\0\0\0"..., 512) = 512
fstat64(3, {st_mode=S_IFREG|0644, st_size=92028, ...}) = 0
mmap2(NULL, 104424, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xb76bf000
mmap2(0xb76d5000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x15) = 0xb76d5000
mmap2(0xb76d7000, 6120, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xb76d7000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/i386-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\1\1\1\0\0\0\0\0\0\0\0\0\3\0\3\0\1\0\0\0000\226\1\0004\0\0\0"..., 512) = 512
fstat64(3, {st_mode=S_IFREG|0755, st_size=1730024, ...}) = 0
mmap2(NULL, 1743580, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xb7515000
mprotect(0xb76b8000, 4096, PROT_NONE)   = 0
mmap2(0xb76b9000, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1a3) = 0xb76b9000
mmap2(0xb76bc000, 10972, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xb76bc000
close(3)                                = 0
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xb7514000
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xb7513000
set_thread_area({entry_number:-1 -> 6, base_addr:0xb75136c0, limit:1048575, seg_32bit:1, contents:0, read_exec_only:0, limit_in_pages:1, seg_not_present:0, useable:1}) = 0
mprotect(0xb76b9000, 8192, PROT_READ)   = 0
mprotect(0xb76d5000, 4096, PROT_READ)   = 0
mprotect(0x804b000, 4096, PROT_READ)    = 0
mprotect(0xb7711000, 4096, PROT_READ)   = 0
munmap(0xb76d9000, 83840)               = 0
brk(0)                                  = 0x995c000
brk(0x997d000)                          = 0x997d000
uname({sys="Linux", node="chenwx", ...}) = 0
fstat64(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 0), ...}) = 0
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xb76ed000
write(1, "chenwx\n", 7chenwx
)                 = 7
exit_group(0)                           = ?
```

## 5.8 系统命令、用户编程接口API、系统调用、内核函数之间的关系

不要把内核函数想像的过于复杂，其实它和普通函数很像，只不过在内核实现，因此要满足一些内核编程的要求。系统调用是一层用户进入内核的接口，它本身并非内核函数，进入内核后，不同的系统调用会找到对应到各自的内核函数：系统调用服务例程。实际上针对请求提供服务的是内核函数而非调用接口。

Linux系统中存在许多内核函数，有些是内核文件中自己使用的，有些则是可以export出来供内核其他部分共同使用的。内核公开的(export出来的)内核函数可执行下列命令查看：

```
# cat /proc/kallsyms
```

从用户角度向内核看，依次是系统命令、编程接口、系统调用和内核函数。

## 5.9 特殊的系统调用

### 5.9.1 sys_ni_syscall()

参见《Linux Kernel Development.[3rd Edition].[Robert Love]》第5. System Calls章第System Call Numbers节:

> Linux provides a "not implemented" system call, sys_ni_syscall(), which does nothing except return -ENOSYS, the error corresponding to an invalid system call. This function is used to "plug the hole" in the rare event that a syscall is removed or otherwise made unavailable.

## 5.10 应用程序调用系统调用的过程

对于不同的内核版本，应用程序调用系统调用的过程也不同：

*  对于Linux kernel 2.5及之前版本的内核，x86处理器使用int 0x80中断方式；
* 对于Linux kernel 2.6及之后版本的内核，IA-32处理器使用sysenter和sysexit指令方式。

### 5.10.1 x86处理器/int 0x80中断方式

Linux used to implement system calls on all x86 platforms using software interrupts. To execute a system call, user process will copy desired system call number to %eax and will execute 'int 0x80'. This will generate interrupt 0x80 and an interrupt service routine will be called (which results in execution of the system_call function).

系统调用的入口点参见[系统调用](#)节。

### 5.10.2 IA-32处理器/sysenter和sysexit指令方式

Userland processes (or C library on their behalf) call ```__kernel_vsyscall``` to execute system calls. Address of ```__kernel_vsyscall``` is not fixed. Kernel passes this address to userland processes using AT_SYSINFO elf parameter. AT_ elf parameters, a.k.a. elf auxiliary vectors, are loaded on the process stack at the time of startup, alongwith the process arguments and the environment variables.

arch/x86/include/asm/elf.h

```
#define AT_SYSINFO              32
```

arch/x86/vdso/vdso32/vdso32.lds.S

```
#define VDSO_PRELINK 0
#include "../vdso-layout.lds.S"

/* The ELF entry point can be used to set the AT_SYSINFO value.  */
ENTRY(__kernel_vsyscall);			// 定义于arch/x86/vdso/vdso32/sysenter.S

/*
 * This controls what userland symbols we export from the vDSO.
 */
VERSION
{
	LINUX_2.5 {
	global:
		__kernel_vsyscall;		// 定义于arch/x86/vdso/vdso32/syscall.S
		__kernel_sigreturn;		// 定义于arch/x86/vdso/vdso32/sigreturn.S
		__kernel_rt_sigreturn;		// 定义于arch/x86/vdso/vdso32/sigreturn.S
	local: *;
	};
}

/*
 * Symbols we define here called VDSO* get their values into vdso32-syms.h.
 */
VDSO32_PRELINK		= VDSO_PRELINK;
VDSO32_vsyscall		= __kernel_vsyscall;
VDSO32_sigreturn	= __kernel_sigreturn;
VDSO32_rt_sigreturn	= __kernel_rt_sigreturn;
```

#### 5.10.2.1 vsyscall page

内核中有一个永久固定映射页面(位于0xFFFFE000-0xFFFFEFFF)，名为vsyscall page。这个区域存放了系统调用入口__kernel_vsyscall的代码，以及信号处理程序的返回代码__kernel_sigreturn。当系统初始化时，调用sysenter_setup()函数分配一个空页面，根据系统是否支持syscall、sysenter指令，将vdso32_sysenter_start/ vdso32_sysenter_end，vdso32_sysenter_start/vdso32_sysenter_end，或者vdso32_int80_start/ vdso32_int80_end的代码拷贝过去。页的权限是用户级、只读、可执行，所以用户进程可以直接访问该页代码。

##### 5.10.2.1.1 vsyscall page的创建

在arch/x86/vdso/vdso32-setup.c中，包含如下有关sysenter_setup()的代码：

```
/*
 * X86_FEATURE_SYSENTER32定义于arch/x86/include/asm/cpufeature.h：
 * #define X86_FEATURE_SYSENTER32  (3*32+15) /* "" sysenter in ia32 userspace */
 * boot_cpu_has()定义于lib/raid6/x86.h
 */
#define vdso32_sysenter()          (boot_cpu_has(X86_FEATURE_SYSENTER32))
/*
 * X86_FEATURE_SYSCALL32定义于arch/x86/include/asm/cpufeature.h：
 * #define X86_FEATURE_SYSCALL32   (3*32+14) /* "" syscall in ia32 userspace */
 * boot_cpu_has()定义于lib/raid6/x86.h
 */
#define vdso32_syscall()           (boot_cpu_has(X86_FEATURE_SYSCALL32))

...
int __init sysenter_setup(void)
{
	/*
	 * GFP_ATOMIC定义于include/linux/gfp.h，其最终取值为0x20u
	 * get_zeroed_page()定义于mm/page_alloc.c，该函数返回一个单个的、零填充的页面
	 */
	void *syscall_page = (void *)get_zeroed_page(GFP_ATOMIC);

	const void *vsyscall;
	size_t vsyscall_len;

	/*
	 * The virt_to_page(addr) macro yields the address of the page descriptor
	 * associated with the linear address addr. 其定义于arch/x86/include/asm/page.h:
	 * #define virt_to_page(kaddr)     pfn_to_page(__pa(kaddr) >> PAGE_SHIFT)
	 * 其中，PAGE_SHIFT定义于arch/x86/include/asm/page_types.h : #define PAGE_SHIFT 12
	 */
	vdso32_pages[0] = virt_to_page(syscall_page);

#ifdef CONFIG_X86_32
	gate_vma_init();
#endif

	if (vdso32_syscall()) {
		vsyscall = &vdso32_syscall_start;
		vsyscall_len = &vdso32_syscall_end - &vdso32_syscall_start;
	} else if (vdso32_sysenter()){
		vsyscall = &vdso32_sysenter_start;
		vsyscall_len = &vdso32_sysenter_end - &vdso32_sysenter_start;
	} else {
		vsyscall = &vdso32_int80_start;
		vsyscall_len = &vdso32_int80_end - &vdso32_int80_start;
	}

	memcpy(syscall_page, vsyscall, vsyscall_len);
	relocate_vdso(syscall_page);

	return 0;
}
```

在arch/x86/vdso/vdso32.S中，包含如下有关:

* vdso32_syscall_start / vdso32_syscall_end
* vdso32_sysenter_start / vdso32_sysenter_end
* vdso32_int80_start / vdso32_int80_end

的代码：

```
#include <linux/init.h>

__INITDATA

        .globl vdso32_int80_start, vdso32_int80_end
vdso32_int80_start:
        .incbin "arch/x86/vdso/vdso32-int80.so"			// 编译过程参见arch/x86/vdso/Makefile
vdso32_int80_end:

        .globl vdso32_syscall_start, vdso32_syscall_end
vdso32_syscall_start:
#ifdef CONFIG_COMPAT
        .incbin "arch/x86/vdso/vdso32-syscall.so"		// 编译过程参见arch/x86/vdso/Makefile
#endif
vdso32_syscall_end:

        .globl vdso32_sysenter_start, vdso32_sysenter_end
vdso32_sysenter_start:
        .incbin "arch/x86/vdso/vdso32-sysenter.so"		// 编译过程参见arch/x86/vdso/Makefile
vdso32_sysenter_end:

__FINIT
```

#### 5.10.2.2 用户进程执行系统调用

用户进程调用do_execve()时，该函数把vsyscall页动态链接到进程空间。这样用户程序需要执行系统调用时，可以直接调用vsyscall页里的代码kernel_vsyscall()，根据编译连接情况调用int 80或者sysenter指令实现，从而实现user-kernel的跨越。

采用vsyscall页的内核(V2.5.53以后)，把用户信号处理程序中用到的返回代码__kernel_sigreturn也放在了永久固定映射页，这样就不用再放到堆栈里了。

# 6 内存管理 (Memory Management)

内存管理的代码主要在mm/目录，特定结构的代码在arch/$(ARCH)/mm/目录。

## 6.1 段机制和分页机制

参见《Linux 操作系统内核分析_陈莉君.pdf》第四章。

虚拟地址与物理地址的转换：

![Virtual_Address_to_Real_Address](/assets/Virtual_Address_to_Real_Address.png)

段机制参见[6.1.1 段机制](#6-1-1-)节，分页机制参见[分页机制](#)节。

### 6.1.1 段机制

#### 6.1.1.1 段描述符/Segment Descriptor

描述符desc_struct, gate_desc, ldt_desc, tss_desc定义于arch/x86/include/asm/desc_defs.h:

```
#ifdef CONFIG_X86_64
typedef struct gate_struct64	gate_desc;
typedef struct ldttss_desc64	ldt_desc;
typedef struct ldttss_desc64	tss_desc;
#define gate_offset(g)		((g).offset_low | ((unsigned long)(g).offset_middle << 16) | ((unsigned long)(g).offset_high << 32))
#define gate_segment(g)		((g).segment)
#else
typedef struct desc_struct	gate_desc;
typedef struct desc_struct	ldt_desc;
typedef struct desc_struct	tss_desc;
#define gate_offset(g)		(((g).b & 0xffff0000) | ((g).a & 0x0000ffff))
#define gate_segment(g)		((g).a >> 16)
#endif

struct desc_struct {
	union {
		struct {
			unsigned int a;
			unsigned int b;
		};
		struct {
			u16 limit0;
			u16 base0;
			unsigned base1: 8, type: 4, s: 1, dpl: 2, p: 1;
			unsigned limit: 4, avl: 1, l: 1, d: 1, g: 1, base2: 8;
		};
	};
} __attribute__((packed));

/* 16byte gate */
struct gate_struct64 {
	u16 offset_low;
	u16 segment;
	unsigned ist : 3, zero0 : 5, type : 5, dpl : 2, p : 1;
	u16 offset_middle;
	u32 offset_high;
	u32 zero1;
} __attribute__((packed));

/* LDT or TSS descriptor in the GDT. 16 bytes. */
struct ldttss_desc64 {
	u16 limit0;
	u16 base0;
	unsigned base1 : 8, type : 5, dpl : 2, p : 1;
	unsigned limit1 : 4, zero0 : 3, g : 1, base2 : 8;
	u32 base3;
	u32 zero1;
} __attribute__((packed));

// 用于初始化struct desc_struct类型的变量，参见全局描述符表GDT节
#define GDT_ENTRY_INIT(flags, base, limit) { { {					\
		.a = ((limit) & 0xffff) | (((base) & 0xffff) << 16),			\
		.b = (((base) & 0xff0000) >> 16) | (((flags) & 0xf0ff) << 8) |		\
		     ((limit) & 0xf0000) | ((base) & 0xff000000),			\
	} } }

// 用于表示desc_struct中的type字段取值，参见错误：引用源未找到
enum {
	DESC_TSS = 0x9,
	DESC_LDT = 0x2,
	DESCTYPE_S = 0x10,		/* !system */
};

// 用于表示desc_struct中的type字段取值，参见错误：引用源未找到
enum {
	GATE_INTERRUPT = 0xE, 		// 中断门
	GATE_TRAP = 0xF, 		// 陷阱门
	GATE_CALL = 0xC,
	GATE_TASK = 0x5, 		// 系统门
};
```

在32位体系结构下，其结构参见：

![Register_1](/assets/Register_1.jpg)

![Register_2](/assets/Register_2.jpg)

![Register_3](/assets/Register_3.jpg)

各字段的含义如下表所示：

![Segment_Descriptor_Fields](/assets/Segment_Descriptor_Fields.png)

#### 6.1.1.2 全局段描述符表GDT/全局描述符表寄存器GDTR

##### 6.1.1.2.1 全局描述符表GDT

除了任务门描述符、中断门描述符和陷阱门描述符(这些描述符保存于中断描述符表，参见6.1.1.3 中断描述符表IDT/中断描述符表寄存器IDTR节)外，全局描述符表GDT包含系统中所有任务都可用的那些描述符。

全局描述符表结构struct pdt_page定义于arch/x86/include/asm/desc.h:

```
struct gdt_page {
	/*
	 * struct desc_struct参见段描述符节；
	 * 常量GDT_ENTRIES定义于arch/x86/include/asm/segment.h，取值为32或16
	 */
	struct desc_struct gdt[GDT_ENTRIES];
} __attribute__((aligned(PAGE_SIZE)));		// 页对齐
```

全局描述符表gdt_page的声明及获取函数参见arch/x86/include/asm/desc.h:

```
// 声明全局描述符表gdt_page，该宏定义于include/linux/percpu-defs.h
DECLARE_PER_CPU_PAGE_ALIGNED(struct gdt_page, gdt_page);

// 获取指定CPU的全局描述符表
static inline struct desc_struct *get_cpu_gdt_table(unsigned int cpu)
{
	return per_cpu(gdt_page, cpu).gdt;
}
```

NOTE: In uniprocessor systems there is only one GDT, while in multiprocessor systems there is one GDT for every CPU in the system.

全局描述符表gdt_page定义于arch/x86/kernel/cpu/common.c:

```
/*
 * The first entry of the GDT is always set to 0. This ensures that logical addresses with
 * a null Segment Selector will be considered invalid, thus causing a processor exception.
 */
DEFINE_PER_CPU_PAGE_ALIGNED(struct gdt_page, gdt_page) = {
	.gdt = {
#ifdef CONFIG_X86_64
		/*
		 * We need valid kernel segments for data and code in long mode too
		 * IRET will check the segment types  kkeil 2000/10/28
		 * Also sysret mandates a special GDT layout
		 *
		 * TLS descriptors are currently at a different place compared to i386.
		 * Hopefully nobody expects them at a fixed place (Wine?)
		 */
		[GDT_ENTRY_KERNEL32_CS]		= GDT_ENTRY_INIT(0xc09b, 0, 0xfffff), 	// 1
		[GDT_ENTRY_KERNEL_CS]			= GDT_ENTRY_INIT(0xa09b, 0, 0xfffff), 	// 2
		[GDT_ENTRY_KERNEL_DS]			= GDT_ENTRY_INIT(0xc093, 0, 0xfffff), 	// 3
		[GDT_ENTRY_DEFAULT_USER32_CS]	= GDT_ENTRY_INIT(0xc0fb, 0, 0xfffff), 	// 4
		[GDT_ENTRY_DEFAULT_USER_DS]		= GDT_ENTRY_INIT(0xc0f3, 0, 0xfffff), 	// 5
		[GDT_ENTRY_DEFAULT_USER_CS]		= GDT_ENTRY_INIT(0xa0fb, 0, 0xfffff), 	// 6
#else
		[GDT_ENTRY_KERNEL_CS]			= GDT_ENTRY_INIT(0xc09a, 0, 0xfffff), 	// 12
		[GDT_ENTRY_KERNEL_DS]			= GDT_ENTRY_INIT(0xc092, 0, 0xfffff), 	// 13
		[GDT_ENTRY_DEFAULT_USER_CS]		= GDT_ENTRY_INIT(0xc0fa, 0, 0xfffff), 	// 14
		[GDT_ENTRY_DEFAULT_USER_DS]		= GDT_ENTRY_INIT(0xc0f2, 0, 0xfffff), 	// 15
		/*
		 * Segments used for calling PnP BIOS have byte granularity.
		 * They code segments and data segments have fixed 64k limits,
		 * the transfer segment sizes are set at run time.
		 */
		/* 32-bit code */
		[GDT_ENTRY_PNPBIOS_CS32]		= GDT_ENTRY_INIT(0x409a, 0, 0xffff), 	// 18
		/* 16-bit code */
		[GDT_ENTRY_PNPBIOS_CS16]		= GDT_ENTRY_INIT(0x009a, 0, 0xffff), 	// 19
		/* 16-bit data */
		[GDT_ENTRY_PNPBIOS_DS]		= GDT_ENTRY_INIT(0x0092, 0, 0xffff), 		// 20
		/* 16-bit data */
		[GDT_ENTRY_PNPBIOS_TS1]		= GDT_ENTRY_INIT(0x0092, 0, 0), 		// 21
		/* 16-bit data */
		[GDT_ENTRY_PNPBIOS_TS2]		= GDT_ENTRY_INIT(0x0092, 0, 0), 		// 22
		/*
		 * The APM segments have byte granularity and their bases
		 * are set at run time.  All have 64k limits.
		 */
		/* 32-bit code */
		[GDT_ENTRY_APMBIOS_BASE]		= GDT_ENTRY_INIT(0x409a, 0, 0xffff), 	// 23
		/* 16-bit code */
		[GDT_ENTRY_APMBIOS_BASE+1]		= GDT_ENTRY_INIT(0x009a, 0, 0xffff),	// 24
		/* data */
		[GDT_ENTRY_APMBIOS_BASE+2]		= GDT_ENTRY_INIT(0x4092, 0, 0xffff),	// 25

		[GDT_ENTRY_ESPFIX_SS]			= GDT_ENTRY_INIT(0xc092, 0, 0xfffff), 	// 26
		[GDT_ENTRY_PERCPU]			= GDT_ENTRY_INIT(0xc092, 0, 0xfffff), 	// 27
		GDT_STACK_CANARY_INIT 								// 28
#endif
	}
};
```

其中，宏DEFINE_PER_CPU_PAGE_ALIGNED()定义于include/linux/percpu-defs.h，其他宏定义于arch/x86/include/asm/segment.h。

由段描述符节中GDT_ENTRY_INIT的定义可知，全局描述符表中各表项的基地址(BASE)为0，界限(LIMIT)为0xfffff，故段长为4GB空间(G位为1，故颗粒度为4K字节)。根据段机制，基地址＋偏移量＝线性地址，可知，0+偏移量=线性地址，即虚拟地址直接映射到了线性地址，也就是说**虚拟地址和线性地址是相同的**。

由于IA32段机制规定：
* 必须为代码段和数据段创建不同的段；
* Linux内核运行在特权级0，而用户程序运行在特权级别3。根据IA32的段保护机制规定，特权级3的程序无法访问特权级为0的段，所以Linux必须为内核和用户程序分别创建其代码段和数据段。

故，Linux必须创建4个段描述符：
* 特权级0的代码段和数据段：GDT_ENTRY_KERNEL_CS, GDT_ENTRY_KERNEL_DS
* 特权级3的代码段和数据段：GDT_ENTRY_DEFAULT_USER_CS, GDT_ENTRY_DEFAULT_USER_DS

这四个段定义于arch/x86/include/asm/segment.h:

```
#ifdef CONFIG_X86_32
#define GDT_ENTRY_KERNEL_BASE		(12)

#define GDT_ENTRY_KERNEL_CS			(GDT_ENTRY_KERNEL_BASE+0)
#define GDT_ENTRY_KERNEL_DS			(GDT_ENTRY_KERNEL_BASE+1)

#define GDT_ENTRY_DEFAULT_USER_CS	14
#define GDT_ENTRY_DEFAULT_USER_DS	15
#else
#define GDT_ENTRY_KERNEL_CS 		2
#define GDT_ENTRY_KERNEL_DS 		3

#define GDT_ENTRY_DEFAULT_USER_DS 	5
#define GDT_ENTRY_DEFAULT_USER_CS 	6
#endif
```

这四个段对应的Segment Selector定义于arch/x86/include/asm/segment.h:

```
#define __KERNEL_CS		(GDT_ENTRY_KERNEL_CS*8)		// 96, or 16
#define __KERNEL_DS		(GDT_ENTRY_KERNEL_DS*8)		// 104, or 24
#define __USER_CS		(GDT_ENTRY_DEFAULT_USER_CS*8+3)	// 115, or 51
#define __USER_DS		(GDT_ENTRY_DEFAULT_USER_DS*8+3)	// 123, or 43
```

综上，各段的字段取值：

| Segment | Base  |   G   | Limit |   S   | Type  |  DPL  |  D/B  |   P   |
| :------ | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| user code / __USER_CS | 0x00000000 | 1 | 0xFFFFF | 1 | 10 | 3 | 1 | 1 |
| user data / __USER_DS | 0x00000000 | 1 | 0xFFFFF | 1 | 2  | 3 | 1 | 1 |
| kernel code / __KERNEL_CS | 0x00000000 | 1 | 0xFFFFF | 1  | 10 | 0 | 1 | 1 |
| kernel data / __KERNEL_DS | 0x00000000 | 1 | 0xFFFFF | 1 | 2 | 0 | 1 | 1 |

<p/>

##### 6.1.1.2.2 全局描述符表寄存器GDTR

全局描述符表寄存器(GDTR)是一个48位的寄存器：低16位保存全局描述符表(GDT)的大小，最大取值为64KB；高32位保存GDT的段基址，取值范围为[0, 4G)地址空间。其结构如下图所示：

![GDTR](/assets/GDTR.png)

#### 6.1.1.3 中断描述符表IDT/中断描述符表寄存器IDTR

##### 6.1.1.3.1 中断描述符表IDT

中断描述符结构gate_desc定义于arch/x86/include/asm/desc_defs.h，参见段描述符节。

中断描述符表idt_table定义于arch/x86/kernel/traps.c中，如下：

```
gate_desc idt_table[NR_VECTORS] __page_aligned_data = { { { { 0, 0 } } }, };
```

其中，NR_VECTORS取值为256，即中断描述符表可包含256个描述符，参见中断处理简介节。

中断描述符表只能包含任务门描述符、中断门描述符和陷阱门描述符：

| Task Gate Descriptor | Includes the TSS selector of the process that must replace the current one when an interrupt signal occurs. |
| Interrupt Gate Descriptor | Includes the Segment Selector and the offset inside the segment of an interrupt or exception handler. While transferring control to the proper segment, the processor clears the IF flag, thus disabling further maskable interrupts. |
| Trap Gate Descriptor | Similar to an interrupt gate, except that while transferring control to the proper segment, the processor does not modify the IF flag. |

<p/>

参见下图，bit 40-43代表中断描述符类型，分别用常量GATE_TASK,GATE_INTERRUPT,GATE_TRAP表示，参见段描述符/Segment Descriptor节：

![Gate_Descriptor](/assets/Gate_Descriptor.jpg)

###### 6.1.1.3.1.1 中断描述符表的初步初始化

1) 声明256个门描述符的IDT表空间，参见arch/x86/kernel/head_32.S:

```
idt_descr:
	.word IDT_ENTRIES*8-1		# idt contains 256 entries
	.long idt_table
```

2) 设置指向IDT表地址的寄存器IDTR，参见arch/x86/kernel/head_32.S:

```
	lgdt early_gdt_descr
	lidt idt_descr
	ljmp $(__KERNEL_CS),$1f
1:	movl $(__KERNEL_DS),%eax	# reload all the segment registers

ENTRY(early_gdt_descr)
	.word GDT_ENTRIES*8-1
	.long gdt_page			/* Overwritten for secondary CPUs */
```

3) 初始化256个门描述符。对于每个门描述符，段选择子都指向内核段，段偏移都指向函数igore_int()，该函数只打印信息：

	Unknown interrupt or fault at: %p %p %p\n

```
/*
 *  setup_idt
 *
 *  sets up a idt with 256 entries pointing to
 *  ignore_int, interrupt gates. It doesn't actually load
 *  idt - that can be done only after paging has been enabled
 *  and the kernel moved to PAGE_OFFSET. Interrupts
 *  are enabled elsewhere, when we can be relatively
 *  sure everything is ok.
 *
 *  Warning: %esi is live across this function.
 */
setup_idt:
	lea ignore_int,%edx
	movl $(__KERNEL_CS << 16),%eax
	movw %dx,%ax		/* selector = 0x0010 = cs */
	movw $0x8E00,%dx		/* interrupt gate - dpl=0, present */

	lea idt_table,%edi
	mov $256,%ecx
rp_sidt:
	movl %eax,(%edi)
	movl %edx,4(%edi)
	addl $8,%edi
	dec %ecx
	jne rp_sidt

/* This is the default interrupt "handler" :-) */
	ALIGN
ignore_int:
	cld
#ifdef CONFIG_PRINTK
	pushl %eax
	pushl %ecx
	pushl %edx
	pushl %es
	pushl %ds
	movl $(__KERNEL_DS),%eax
	movl %eax,%ds
	movl %eax,%es
	cmpl $2,early_recursion_flag
	je hlt_loop
	incl early_recursion_flag
	pushl 16(%esp)
	pushl 24(%esp)
	pushl 32(%esp)
	pushl 40(%esp)
	pushl $int_msg
	call printk

	call dump_stack

	addl $(5*4),%esp
	popl %ds
	popl %es
	popl %edx
	popl %ecx
	popl %eax
#endif
	iret

int_msg:
	.asciz "Unknown interrupt or fault at: %p %p %p\n"
```

**NOTE**: The ```ignore_int()``` handler should never be executed. The occurrence of "Unknown interrupt" messages on the console or in the log files denotes either a hardware problem (an I/O device is issuing unforeseen interrupts) or a kernel problem (an interrupt or exception is not being handled properly).

###### 6.1.1.3.1.2 中断描述符表的最终初始化

中断描述符表的最终初始化分为两部分：
* 异常：由函数trap_init()实现，被系统初始化入口函数start_kernel()调用，参见trap_init()节；
* 中断：由函数init_IRQ()实现，被系统初始化入口函数start_kernel()调用，参见init_IRQ()节。

##### 6.1.1.3.2 中断描述符表寄存器IDTR

中断描述符表寄存器(IDTR)与全局描述符表寄存器(GDTR)类似，参见全局描述符表寄存器GDTR节。

#### 6.1.1.4 局部描述符表LDT/局部描述符表寄存器LDTR

##### 6.1.1.4.1 局部描述符表LDT

局部描述符表包含与特定任务有关的描述符，每个任务都有一个各自的局部描述符表LDT。每个任务的局部描述符表也用一个描述符来表示，称为LDT描述符，它包含了局部描述符表的信息，在全局描述符表GDT中(参见错误：引用源未找到，当S=0, TYPE=2时，该项即为LDT描述符)。

局部描述符结构ldt_desc定义于arch/x86/include/asm/desc_defs.h，参见段描述符节。

##### 6.1.1.4.2 局部描述符表寄存器LDTR

局部描述符表寄存器(LDTR)包括如下两部分：
* 可见部分: 16-bit Index，用来选择全局描述符表GDT中的局部描述符表LDT中的描述符；
* 不可见部分: 48-bit BASE/LIMIT，用来保存局部描述符表的基地址和界限。

![Register_5](/assets/Register_5.jpg)

#### 6.1.1.5 段选择器(Segment Selector)与描述符表寄存器

##### 6.1.1.5.1 段选择器(Segment Selector)

在实模式下，段寄存器存储的是真实的段地址；在保护模式下，16位的段寄存器无法存储32位的段地址，故它被称为段选择器，即段寄存器的作用是用来选择段描述符，这样就把段描述符中的32位段地址(参见段描述符节表格中的BASE域)作为实际的段地址。

段选择器结构及各字段含义如下：

![Segment_Selector](/assets/Segment_Selector.png)

| Field | Description |
| :---- | :--- |
| Index | Identifies the Segment Descriptor entry contained in the GDT or in the LDT. 占13 bit，取值范围[0, 8191] |
| TI    | Table Indicator: specifies whether the Segment Descriptor is included in the GDT (TI = 0) or in the LDT (TI = 1). |
| RPL   | Requestor Privilege Level: specifies the Current Privilege Level of the CPU (see section 段描述符) when the corresponding Segment Selector is loaded into the cs register; it also may be used to selectively weaken the processor privilege level when accessing data segments (see Intel documentation for details). |

<p/>

在arch/x86/include/asm/kvm.h中，包含如下类型：

```
struct kvm_segment {
	__u64 base;
	__u32 limit;
	__u16 selector;		// 段选择器
	__u8  type;
	__u8  present, dpl, db, s, l, g, avl;
	__u8  unusable;
	__u8  padding;
};
```

在arch/x86/include/linux/kvm_host.h中，包含如下宏，分别用于获取段选择器中的TI和RPL字段：

```
#define SELECTOR_TI_MASK		(1 << 2)
#define SELECTOR_RPL_MASK		0x03
```

##### 6.1.1.5.2 Logical Address转换到Linear Address

参见<<Understanding the Linux Kernel, 3rd Edition>>第2. Memory Addressing章第Segmentation Unit节:

![Segmentation_Unit](/assets/Segmentation_Unit.png)

The segmentation unit performs the following operations:

* Examines the TI field of the Segment Selector to determine which Descriptor Table stores the Segment Descriptor. This field indicates that the Descriptor is either in the GDT (in which case the segmentation unit gets the base linear address of the GDT from the gdtr register) or in the active LDT (in which case the segmentation unit gets the base linear address of that LDT from the ldtr register).

* Computes the address of the Segment Descriptor from the index field of the Segment Selector. The index field is multiplied by 8 (the size of a Segment Descriptor), and the result is added to the content of the gdtr or ldtr register.

* Adds the offset of the logical address to the BASE field of the Segment Descriptor, thus obtaining the linear address.

### 6.1.2 分页机制

寄存器参见下图：

![Register_7](/assets/Register_7.jpg)

![Register_7_Description](/assets/Register_7_Description.png)

Starting with the 80386, all 80×86 processors support paging; it is enabled by setting the PG flag of a control register named CR0. When PG = 0, linear addresses are interpreted as physical addresses.

80386使用4K字节大小的页。每一页都有4K字节长，并在4K字节的边界上对齐，即每一页的起始地址都能被4K整除。因此，80386把4G字节的线性地址空间划分为1M个页面。因为每页的整个4K字节作为一个单位进行映射，并且每页都对齐4K字节的边界，故线性地址的低12位经过分页机制后直接作为物理地址的低12位使用。重定位函数也因此可看成是把线性地址的高20位转换为对应物理地址的高20位的转换函数。

#### 6.1.2.1 两级页表结构

两级页表结构的第一级为页目录，存储在一个4KB的页中(该页的基地址保存在CR3中，参见错误：引用源未找到)。页目录表中共有1024个表项，每个表项大小为4字节并指向一个第二级表。线性地址的最高10位(即31-22位)用来产生第一级的索引，由索引得到的表项指定并选择了1K个二级表中的一个表。

两级页表结构的第二级为页表，也刚好存储在一个4KB的页中。页表中共有1024个表项，每个表项大小为4字节并包含一个页的物理基地址。线性地址的中间10位(即21-12位)用来产生第二级的索引，以获得包含页物理地址的页表项。这个物理地址的高20位与线性地址的低12位形成最后的物理地址，也就是页转化过程输出的物理地址。

NOTE 1: The aim of this two-level scheme is to reduce the amount of RAM required for per-process Page Tables.

NOTE 2: Each active process must have a Page Directory assigned to it. However, there is no need to allocate RAM for all Page Tables of a process at once; it is more efficient to allocate RAM for a Page Table only when the process effectively needs it.

##### 6.1.2.1.1 页目录项/Page Directory Entry

Refer to <<Intel 64 and IA-32 Architectures Software Developer's Manual_201309>> Figure 4-4. Formats of CR3 and Paging-Structure Entries with 32-Bit Paging:

![Register_7](/assets/Register_7.jpg)

| Field | Description |
| :---- | :---------- |
| P     | If it is set, the referred-to page (or Page Table) is contained in main memory; if the flag is 0, the page is not contained in main memory and the remaining entry bits may be used by the operating system for its own purposes. If the entry of a Page Table or Page Directory needed to perform an address translation has the Presentflag cleared, the paging unit stores the linear address in a control register named cr2 and generates exception 14: the Page Fault exception. |
| R/W   | Contains the access right (Read/Write or Read) of the page or of the Page Table. If the flag of a Page Directory or Page Table entry is equal to 0, the corresponding Page Table or page can only be read; otherwise it can be read and written. |
| U/S   | Contains the privilege level required to access the page or Page Table. When this flag is 0, the page can be addressed only when theCPLis less than 3 (this means, for Linux, when the processor is in Kernel Mode). When the flag is 1, the page can always be addressed. |
| A     | Set each time the paging unit addresses the corresponding page frame. This flag may be used by the operating system when selecting pages to be swapped out. The paging unit never resets this flag; this must be done by the operating system. |
| 20位页表地址 | Because each page frame has a 4-KB capacity, its physical address must be a multiple of 4096, so the 12 least significant bits of the physical address are always equal to 0. If the field refers to a Page Directory, the page frame contains a Page Table; if it refers to a Page Table, the page frame contains a page of data. |
| PS    | Page Size flag. Applies only to Page Directory entries. If it is set, the entry refers to a 2 MB– or 4 MB–long page frame. See section Extended Paging and Physical Address Extension (PAE). |

<p/>

由U/S和R/W为页目录项提供保护属性：

| U/S | R/W | 允许级别3 | 允许级别0、1、2 |
| 0   | 0   | 无       | 读/写          |
| 0   | 1   | 无       | 读/写          |
| 1   | 0   | 只读     | 读/写          |
| 1   | 1   | 读/写    | 读/写          |

<p/>

##### 6.1.2.1.2 页表项/Page Table Entry

Page table entry:

![Register_8](/assets/Register_8.jpg)

| Field | Description |
| :---- | :---------- |
| P     | If it is set, the referred-to page (or Page Table) is contained in main memory; if the flag is 0, the page is not contained in main memory and the remaining entry bits may be used by the operating system for its own purposes. If the entry of a Page Table or Page Directory needed to perform an address translation has the Presentflag cleared, the paging unit stores the linear address in a control register named cr2 and generates exception 14: the Page Fault exception. |
| R/W   | Contains the access right (Read/Write or Read) of the page or of the Page Table. If the flag of a Page Directory or Page Table entry is equal to 0, the corresponding Page Table or page can only be read; otherwise it can be read and written. |
| U/S   | Contains the privilege level required to access the page or Page Table. When this flag is 0, the page can be addressed only when theCPLis less than 3 (this means, for Linux, when the processor is in Kernel Mode). When the flag is 1, the page can always be addressed. |
| A     | Set each time the paging unit addresses the corresponding page frame. This flag may be used by the operating system when selecting pages to be swapped out. The paging unit never resets this flag; this must be done by the operating system. |
| D     | Applies only to the Page Table entries. It is set each time a write operation is performed on the page frame. As with the Accessed flag, Dirty may be used by the operating system when selecting pages to be swapped out. The paging unit never resets this flag; this must be done by the operating system. |
| 20位页表地址 | Because each page frame has a 4-KB capacity, its physical address must be a multiple of 4096, so the 12 least significant bits of the physical address are always equal to 0. If the field refers to a Page Directory, the page frame contains a Page Table; if it refers to a Page Table, the page frame contains a page of data. |
| G     | Applies only to Page Table entries. This flag was introduced in the Pentium Pro to prevent frequently used pages from being flushed from the TLB cache. It works only if the Page Global Enable (PGE) flag of registercr4is set. |

<p/>

#### 6.1.2.2 Linear Address转换到Physical Address

线性地址到物理地址的转换步骤如下：

1) CR3包含页目录的起始地址，用32位线性地址的最高10位A31-A22作为页目录的页目录项的索引，将它乘以4，与CR3中的页目录的起始地址相加，形成相应页表的地址。

2) 从指定的地址中取出32位页目录项，在页目录项中取出高20位页表地址，并与低12位0，形成32位的页表起始地址。用32位线性地址中的A21-A12位作为页表的页面的索引，将它乘以4，与页表的起始地址相加，形成32位页面地址。

3) 将A11-A0作为相对于页面地址的偏移量，与32位页面地址相加，形成32位物理地址。

![Linear_Address_to_Physical_Address](/assets/Linear_Address_to_Physical_Address.jpg)

##### 6.1.2.2.1 Extended Paging

Starting with the Pentium model, 80×86 microprocessors introduce extended paging, which allows page frames to be 4 MB instead of 4 KB in size (see below figure). Extended paging is used to translate large contiguous linear address ranges into corresponding physical ones; in these cases, the kernel can do without intermediate Page Tables and thus save memory and preserve TLB entries.

Extended paging is enabled by setting the Page Size (PS) flag of a Page Directory entry, see section 页目录项/Page Directory Entry.

![Extended_Paging](/assets/Extended_Paging.jpg)

NOTE: Only the 10 most significant bits of the 20-bit physical address field are significant. This is because each physical address is aligned on a 4-MB boundary, so the 22 least significant bits of the address are 0.

#### 6.1.2.3 Physical Address Extension (PAE)

参见 <<Understanding the Linux Kernel, 3rd Edition>>第2. Memory Addressing章第The Physical Address Extension (PAE) Paging Mechanism节:

The amount of RAM supported by a processor is limited by the number of address pins connected to the address bus. Older Intel processors from the 80386 to the Pentium used 32-bit physical addresses. In theory, up to 4 GB of RAM could be installed on such systems.

However, big servers that need to run hundreds or thousands of processes at the same time require more than 4 GB of RAM, and in recent years this created a pressure on Intel to expand the amount of RAM supported on the 32-bit 80×86 architecture.

Intel has satisfied these requests by increasing the number of address pins on its processors from 32 to 36. Starting with the Pentium Pro, all Intel processors are now able to address up to 236 = 64 GB of RAM. However, the increased range of physical addresses can be exploited only by introducing a new paging mechanism that translates 32-bit linear addresses into 36-bit physical ones.

With the Pentium Pro processor, Intel introduced a mechanism called Physical Address Extension (PAE). Another mechanism, Page Size Extension (PSE-36), was introduced in the Pentium III processor, but Linux does not use it.

PAE is activated by setting the Physical Address Extension (PAE) flag in the cr4 control register. The Page Size (PS) flag in the page directory entry enables large page sizes (2 MB when PAE is enabled).

##### 6.1.2.3.1 Paging Mechanism of PAE

Intel has changed the paging mechanism in order to support PAE.

* The 64 GB of RAM are split into 224 distinct page frames, and the physical address field of Page Table entries has been expanded from 20 to 24 bits. Because a PAE Page Table entry must include the 12 flag bits and the 24 physical address bits, for a grand total of 36, the Page Table entry size has been doubled from 32 bits to 64 bits. As a result, a 4-KB PAE Page Table includes 512 entries instead of 1,024.

* A new level of Page Table called the Page Directory Pointer Table (PDPT) consisting of four 64-bit entries has been introduced.

* The cr3 control register contains a 27-bit Page Directory Pointer Table (PDPT) base address field. Because PDPTs are stored in the first 4 GB of RAM and aligned to a multiple of 32 bytes (25), 27 bits are sufficient to represent the base address of such tables.

* When mapping linear addresses to 4 KB pages (PS flag cleared in Page Directory entry), the 32 bits of a linear address are interpreted in the following way. Refer to Subjects/Chapter06_Memory_Management/Figures/PAE1.jpg

* When mapping linear addresses to 2-MB pages (PS flag set in Page Directory entry), the 32 bits of a linear address are interpreted in the following way. Refer to below figure:

![PAE2](/assets/PAE2.jpg)

To summarize, once cr3 is set, it is possible to address up to 4 GB of RAM. If we want to address more RAM, we’ll have to put a new value in cr3 or change the content of the PDPT. However, the main problem with PAE is that linear addresses are still 32 bits long. This forces kernel programmers to reuse the same linear addresses to map different areas of RAM. Clearly, PAE does not enlarge the linear address space of a process, because it deals only with physical addresses. Furthermore, only the kernel can modify the page tables of the processes, thus a process running in User Mode cannot use a physical address space larger than 4 GB. On the other hand, PAE allows the kernel to exploit up to 64 GB of RAM, and thus to increase significantly the number of processes in the system.

#### 6.1.2.4 Paging for 64-bit Architectures

As we have seen in the previous sections, two-level paging is commonly used by 32-bit microprocessors. Two-level paging, however, is not suitable for computers that adopt a 64-bit architecture. Let’s use a thought experiment to explain why:

Start by assuming a standard page size of 4 KB. Because 1 KB covers a range of 210 addresses, 4 KB covers 212 addresses, so the Offset field is 12 bits. This leaves up to 52 bits of the linear address to be distributed between the Table and the Directory fields. If we now decide to use only 48 of the 64 bits for addressing (this restriction leaves us with a comfortable 256 TB address space!), the remaining 48-12 = 36 bits will have to be split among Table and the Directory fields. If we now decide to reserve 18 bits for each of these two fields, both the Page Directory and the Page Tables of each process should include 218 entries—that is, more than 256,000 entries.

For that reason, all hardware paging systems for 64-bit processors make use of additional paging levels. The number of levels used depends on the type of processor. Below table summarizes the main characteristics of the hardware paging systems used by some 64-bit platforms supported by Linux.

![Paging_Levels](/assets/Paging_Levels.png)

NOTE: 在x86-64架构下，不存在高端内存(ZONE_HIGHMEM)区域。

#### 6.1.2.5 页面高速缓冲寄存器

在启用分页机制的情况下，每次存储器访问都要存取两级页表，这就大大降低了访问速度。所以，为了提高速度，在386中设置了一个最近存取页面的高速缓冲寄存器，它自动保存32项处理器最近使用的页面地址，因此可以覆盖128K字节的存储器地址。当进行存储器访问时，先检查要访问的页面是否在高速缓冲器中，如果在，就不必经过两级访问了；如果不在，再进行两级访问。平均而言，页面高速缓冲寄存器大约有98%的命中率，也就是说每次访问存储器时，只有2%的情况必须访问两级分页机构。其示意图如下：

![Paging_Buffer_Register](/assets/Paging_Buffer_Register.png)

#### 6.1.2.6 Paging in Linux Kernel

参见<<Understanding the Linux Kernel, 3rd Edition>>第2. Memory Addressing章第Paging in Linux节:

Two paging levels are sufficient for 32-bit architectures, while 64-bit architectures require a higher number of paging levels. Up to version 2.6.10, the Linux paging model consisted of three paging levels. Starting with version 2.6.11, a four-level paging model has been adopted. The four types of page tables illustrated in below figure are called:
* Page Global Directory
* Page Upper Directory
* Page Middle Directory
* Page Table

Linux paging model, refer to Subjects/Chapter06_Memory_Management/Figures/Linux_paging_model.jpg

The Page Global Directory includes the addresses of several Page Upper Directories, which in turn include the addresses of several Page Middle Directories, which in turn include the addresses of several Page Tables. Each Page Table entry points to a page frame. Thus the linear address can be split into up to five parts. 错误：引用源未找到 does not show the bit numbers, because the size of each part depends on the computer architecture.

**For 32-bit architectures with no Physical Address Extension**, two paging levels are sufficient. Linux essentially eliminates the Page Upper Directory and the Page Middle Directory fields by saying that they contain zero bits. However, the positions of the Page Upper Directory and the Page Middle Directory in the sequence of pointers are kept so that the same code can work on 32-bit and 64-bit architectures. The kernel keeps a position for the Page Upper Directory and the Page Middle Directory by setting the number of entries in them to 1 and mapping these two entries into the proper entry of the Page Global Directory.

**For 32-bit architectures with the Physical Address Extension enabled**, three paging levels are used. The Linux’s Page Global Directory corresponds to the 80×86’s Page Directory Pointer Table (PDPT), the Page Upper Directory is eliminated, the Page Middle Directory corresponds to the 80×86’s Page Directory, and the Linux’s Page Table
corresponds to the 80×86’s Page Table.

Finally, **for 64-bit architectures** three or four levels of paging are used depending on the linear address bit splitting performed by the hardware, see section Paging for 64-bit Architectures Table 2-4. For x86-64, four levels of paging are used.

Each process has its own Page Global Directory (**mm_struct->pgd**) and its own set of Page Tables. When a process switch occurs (see section context_switch()), Linux saves the **cr3** control register in the descriptor of the process previously in execution and then loads **cr3** with the value stored in the descriptor of the process to be executed next. Thus, when the new process resumes its execution on the CPU, the paging unit refers to the correct set of Page Tables.

##### 6.1.2.6.1 页表结构层级

PAGETABLE_LEVELS表示页表层级，取值为2，3，或4，其分别定义于：

arch/x86/include/asm/pgtable-2level_types.h

```
#define PAGETABLE_LEVELS 	2
```

arch/x86/include/asm/pgtable-3level_types.h

```
#define PAGETABLE_LEVELS 	3
```

arch/x86/include/asm/pgtable-64_types.h

```
#define PAGETABLE_LEVELS 	4
```

各头文件的引用关系如下：

```
arch/x86/include/asm/pgtable.h
+- arch/x86/include/asm/pgtable_types.h
|  +- #ifdef CONFIG_X86_32
|  |     #include "pgtable_32_types.h"
|  |     +- #ifdef CONFIG_X86_PAE
|  |     |     #include <asm/pgtable-3level_types.h>		// PAGETABLE_LEVELS = 3
|  |     |     +- typedef u64	pteval_t;
|  |     |     +- typedef u64	pmdval_t;
|  |     |     +- typedef u64	pudval_t;
|  |     |     +- typedef u64	pgdval_t;
|  |     |     +- typedef union {
|  |     |             struct { unsigned long pte_low, pte_high; };
|  |     |             pteval_t pte;
|  |     |     	    } pte_t;
|  |     |     +- #ifdef CONFIG_PARAVIRT
|  |     |            #define SHARED_KERNEL_PMD	(pv_info.shared_kernel_pmd)
|  |     |         #else
|  |     |            #define SHARED_KERNEL_PMD	1
|  |     |         #endif
|  |     |     +- #define PAGETABLE_LEVELS		3
|  |     |     +- #define PGDIR_SHIFT			30
|  |     |     +- #define PTRS_PER_PGD			4
|  |     |     +- #define PMD_SHIFT			21
|  |     |     +- #define PTRS_PER_PMD			512
|  |     |     +- #define PTRS_PER_PTE			512
|  |     +- #else
|  |     |     #include <asm/pgtable-2level_types.h>		// PAGETABLE_LEVELS = 2
|  |     |     +- typedef unsigned long	pteval_t;
|  |     |     +- typedef unsigned long	pmdval_t;
|  |     |     +- typedef unsigned long	pudval_t;
|  |     |     +- typedef unsigned long	pgdval_t;
|  |     |     +- typedef union {
|  |     |             pteval_t pte;
|  |     |             pteval_t pte_low;
|  |     |     	    } pte_t;
|  |     |     +- #define SHARED_KERNEL_PMD		0
|  |     |     +- #define PAGETABLE_LEVELS		2
|  |     |     +- #define PGDIR_SHIFT			22
|  |     |     +- #define PTRS_PER_PGD			1024
|  |     |     +- #define PTRS_PER_PTE			1024
|  |     +- #endif
|  +- #else
|  |     #include "pgtable_64_types.h"				// PAGETABLE_LEVELS = 4
|  |     +- typedef unsigned long	pteval_t;
|  |     +- typedef unsigned long	pmdval_t;
|  |     +- typedef unsigned long	pudval_t;
|  |     +- typedef unsigned long	pgdval_t;
|  |     +- typedef struct { pteval_t pte; } pte_t;
|  |     +- #define SHARED_KERNEL_PMD			0
|  |     +- #define PAGETABLE_LEVELS			4
|  |     +- #define PGDIR_SHIFT				39
|  |     +- #define PTRS_PER_PGD			512
|  |     +- #define PUD_SHIFT				30
|  |     +- #define PTRS_PER_PUD			512
|  |     +- #define PMD_SHIFT				21
|  |     +- #define PTRS_PER_PMD			512
|  |     +- #define PTRS_PER_PTE			512
|  +- #endif
|  |
|  |
|  +- typedef struct { pgdval_t pgd; } pgd_t;
|  |
|  |
|  +- #if PAGETABLE_LEVELS > 3
|  |     typedef struct { pudval_t pud; } pud_t;
|  +- #else
|  |     #include <asm-generic/pgtable-nopud.h>
|  |     +- typedef struct { pgd_t pgd; } pud_t;
|  |     +- #define PUD_SHIFT		PGDIR_SHIFT
|  |     +- #define PTRS_PER_PUD	1
|  +- #endif
|  |
|  +- #if PAGETABLE_LEVELS > 2
|  |     typedef struct { pmdval_t pmd; } pmd_t;
|  +- #else
|  |     #include <asm-generic/pgtable-nopmd.h>
|  |     +- typedef struct { pud_t pud; } pmd_t;
|  |     +- #define PMD_SHIFT		PUD_SHIFT
|  |     +- #define PTRS_PER_PMD	1
|  +- #endif
|
|
+- #ifdef CONFIG_X86_32
|  +- #include "pgtable_32.h"
+- #else
|  +- #include "pgtable_64.h"
+- #endif
```

页表结构:

![Memery_Layout_30](/assets/Memery_Layout_30.jpg)

###### 6.1.2.6.1.1 与页目录表项/页表项有关的操作函数

除了页目录结构/pgd_t节至页面结构/pte_t节中的函数，如下函数用于操作页目录表项/页表项：

* **pgd_none(), pud_none(), pmd_none(), pte_none()**

  Yield the value 1 if the corresponding entry has the value 0; otherwise, they yield the value 0.

* **pgd_clear(), pud_clear(), pmd_clear(), pte_clear()**

  Clear an entry of the corresponding page table, thus forbidding a process to use the linear addresses mapped by the page table entry. The ptep_get_and_clear() function clears a Page Table entry and returns the previous value.

* **set_pgd(), set_pud(), set_pmd(), set_pte()**

  Write a given value into a page table entry; set_pte_atomicis() identical to set_pte(), but when PAE is enabled it also ensures that the 64-bit value is written atomically.

* **pte_same(a,b)**

  Returns 1 if two Page Table entries a and b refer to the same page and specify the same access privileges, 0 otherwise.

* **pmd_large(e)**

  Returns 1 if the Page Middle Directory entryerefers to a large page (2 MB or 4 MB), 0 otherwise.

* **pgd_bad(), pud_bad(), pmd_bad()**

  The pud_bad() and pgd_bad() macros always yield 0.

  The pmd_bad() macro is used by functions to check Page Middle Directory entries passed as input parameters. It yields the value 1 if the entry points to a bad Page Table — that is, if at least one of the following conditions applies:

  * The page is not in main memory (Present flag cleared).
  * The page allows only Read access (Read/Writeflag cleared).
  * Either Accessed or Dirtyis cleared (Linux always forces these flags to be set for every existing Page Table).
  <p/>

  No pte_bad() macro is defined, because it is legal for a Page Table entry to refer to a page that is not present in main memory, not writable, or not accessible at all.

* **pgd_present(), pud_present(), pmd_present(), pte_present()**

  The pud_present() and pgd_present() macros always yield the value 1.

  The pmd_present() macro yields the value 1 if the Present flag of the corresponding entry is equal to 1 — that is, if the corresponding page or Page Table is loaded in main memory.

  The pte_present() macro yields the value 1 if either the Present flag or the Page Size flag of a Page Table entry is equal to 1, the value 0 otherwise. Recall that the Page Size flag in Page Table entries has no meaning for the paging unit of the microprocessor; the kernel, however, marks Present equal to 0 and Page Size equal to 1 for the pages present in main memory but without read, write, or execute privileges. In this way, any access to such pages triggers a Page Fault exception because Present is cleared, and the kernel can detect that the fault is not due to a missing page by checking the value of Page Size.

##### 6.1.2.6.2 页目录结构/pgd_t

###### 6.1.2.6.2.1 pgd_t结构

页目录项结构为pgd_t，如页目录项/Page Directory Entry节的图所示，其定义于arch/x86/include/asm/pgtable_types.h:

```
typedef struct { pgdval_t pgd; } pgd_t;
```

按照体系架构的不同，pgdval_t定义于如下头文件：

1) arch/x86/include/asm/pgtable-2level_types.h

```
typedef unsigned long   pgdval_t;

/*
 * traditional i386 two-level paging structure:
 */
// 线性地址的最高10位用来产生页目录项索引，
// 参见Linear Address转换到Physical Address节
#define PGDIR_SHIFT   	22
#define PTRS_PER_PGD		1024		// 页目录中包含1024个页目录项
```

2) arch/x86/include/asm/pgtable-3level_types.h

```
typedef u64   pgdval_t;

/*
 * PGDIR_SHIFT determines what a top-level page table entry can map
 */
// 线性地址的最高2位用来产生PDPT，参见Paging Mechanism of PAE节
#define PGDIR_SHIFT		30
#define PTRS_PER_PGD		4		// PDPT中包含4个项
```

3) arch/x86/include/asm/pgtable_64_types.h

```
typedef unsigned long   pgdval_t;

/*
 * PGDIR_SHIFT determines what a top-level page table entry can map
 */
// 线性地址中的9位(A47-A39)用来产生页目录项，
// 参见Paging for 64-bit Architectures节
#define PGDIR_SHIFT	39

// 页目录中包含512个页目录项
#define PTRS_PER_PGD	512
```

###### 6.1.2.6.2.2 pgd_offset()/pgd_offset_k()

操作页目录表的函数定义于arch/x86/include/asm/pgtable.h:

```
/*
 * the pgd page can be thought of an array like this: pgd_t[PTRS_PER_PGD]
 *
 * this macro returns the index of the entry in the pgd page which would
 * control the given virtual address
 */
#define pgd_index(address)		(((address) >> PGDIR_SHIFT) & (PTRS_PER_PGD - 1))

/*
 * pgd_offset() returns a (pgd_t *)
 * pgd_index() is used get the offset into the pgd page's array of pgd_t's;
 */
// 用于获取进程虚拟地址address的一级页目录项指针，其中mm为mm_struct类型，参见struct mm_struct节
#define pgd_offset(mm, address)	((mm)->pgd + pgd_index((address)))

/*
 * a shortcut which implies the use of the kernel's pgd, instead of a process's
 */
// 用于获取内核地址address的一级页目录字指针，其中init_mm定义于mm/init-mm.c，
// init_mm->pgd = swapper_pg_dir
#define pgd_offset_k(address)		pgd_offset(&init_mm, (address))
```

###### 6.1.2.6.2.3 pgd_val()/native_pgd_val()/native_make_pgd()

宏pgd_val()用于获取页目录表项的值，其定义于arch/x86/include/asm/pgtable.h:

```
#define pgd_val(x)		native_pgd_val(x)

static inline pgdval_t	native_pgd_val(pgd_t pgd)
{
	return pgd.pgd;
}

static inline pgd_t native_make_pgd(pgdval_t val)
{
	return (pgd_t) { val };
}
```

###### 6.1.2.6.2.4 pgd_flags()

该函数定义于arch/x86/include/asm/pgtable_types.h:

```
/* PTE_PFN_MASK extracts the PFN from a (pte|pmd|pud|pgd)val_t */
#define PTE_PFN_MASK		((pteval_t)PHYSICAL_PAGE_MASK)		// A31-A12置1，其他位置0

/* PTE_FLAGS_MASK extracts the flags from a (pte|pmd|pud|pgd)val_t */
#define PTE_FLAGS_MASK	(~PTE_PFN_MASK)					// A11-A0置1，其他位置0

static inline pgdval_t pgd_flags(pgd_t pgd)
{
	// 函数native_pgd_val()参见pgd_val()/native_pgd_val()/native_make_pgd()节
	return native_pgd_val(pgd) & PTE_FLAGS_MASK;
}
```

其中，PHYSICAL_PAGE_MASK定义于arch/x86/include/asm/page_types.h:

```
/* PAGE_SHIFT determines the page size */
#define PAGE_SHIFT		12
#define PAGE_SIZE		(_AC(1,UL) << PAGE_SHIFT)
#define PAGE_MASK		(~(PAGE_SIZE-1))				// A11-A0置0，其他位置1

#define __PHYSICAL_MASK	((phys_addr_t)((1ULL << __PHYSICAL_MASK_SHIFT) - 1))	// A31-A0置1，高位置0

/* Cast PAGE_MASK to a signed type so that it is sign-extended if
   virtual addresses are 32-bits but physical addresses are larger
   (ie, 32-bit PAE). */
#define PHYSICAL_PAGE_MASK	(((signed long)PAGE_MASK) & __PHYSICAL_MASK)	// A31-A12置1，其他位置0
```

###### 6.1.2.6.2.4.1 PDG Flags

页目录项中各标志位定义于arch/x86/include/asm/pgtable_types.h:

```
#define _PAGE_BIT_PRESENT		0	/* is present */
#define _PAGE_BIT_RW			1	/* writeable */
#define _PAGE_BIT_USER			2	/* userspace addressable */
#define _PAGE_BIT_PWT			3	/* page write through */
#define _PAGE_BIT_PCD			4	/* page cache disabled */
#define _PAGE_BIT_ACCESSED		5	/* was accessed (raised by CPU) */
#define _PAGE_BIT_DIRTY			6	/* was written to (raised by CPU) */
#define _PAGE_BIT_PSE			7	/* 4 MB (or 2MB) page */
#define _PAGE_BIT_PAT			7	/* on 4KB pages */
#define _PAGE_BIT_GLOBAL		8	/* Global TLB entry PPro+ */
#define _PAGE_BIT_UNUSED1		9	/* available for programmer */
#define _PAGE_BIT_IOMAP			10	/* flag used to indicate IO mapping */
#define _PAGE_BIT_HIDDEN		11	/* hidden by kmemcheck */
#define _PAGE_BIT_PAT_LARGE		12	/* On 2MB or 1GB pages */
#define _PAGE_BIT_SPECIAL		_PAGE_BIT_UNUSED1
#define _PAGE_BIT_CPA_TEST		_PAGE_BIT_UNUSED1
#define _PAGE_BIT_SPLITTING		_PAGE_BIT_UNUSED		1 /* only valid on a PSE pmd */
#define _PAGE_BIT_NX			63	/* No execute: only valid after cpuid check */

#define _PAGE_PRESENT	 		(_AT(pteval_t, 1) << _PAGE_BIT_PRESENT)
#define _PAGE_RW	        	(_AT(pteval_t, 1) << _PAGE_BIT_RW)
#define _PAGE_USER	     		(_AT(pteval_t, 1) << _PAGE_BIT_USER)
#define _PAGE_PWT	     		(_AT(pteval_t, 1) << _PAGE_BIT_PWT)
#define _PAGE_PCD	     		(_AT(pteval_t, 1) << _PAGE_BIT_PCD)
#define _PAGE_ACCESSED	 		(_AT(pteval_t, 1) << _PAGE_BIT_ACCESSED)
#define _PAGE_DIRTY	     		(_AT(pteval_t, 1) << _PAGE_BIT_DIRTY)
#define _PAGE_PSE	     		(_AT(pteval_t, 1) << _PAGE_BIT_PSE)
#define _PAGE_GLOBAL	 		(_AT(pteval_t, 1) << _PAGE_BIT_GLOBAL)
#define _PAGE_UNUSED1	 		(_AT(pteval_t, 1) << _PAGE_BIT_UNUSED1)
#define _PAGE_IOMAP	     		(_AT(pteval_t, 1) << _PAGE_BIT_IOMAP)
#define _PAGE_PAT	     		(_AT(pteval_t, 1) << _PAGE_BIT_PAT)
#define _PAGE_PAT_LARGE 		(_AT(pteval_t, 1) << _PAGE_BIT_PAT_LARGE)
#define _PAGE_SPECIAL	 		(_AT(pteval_t, 1) << _PAGE_BIT_SPECIAL)
#define _PAGE_CPA_TEST	 		(_AT(pteval_t, 1) << _PAGE_BIT_CPA_TEST)
#define _PAGE_SPLITTING	 		(_AT(pteval_t, 1) << _PAGE_BIT_SPLITTING)

#ifdef CONFIG_KMEMCHECK
#define _PAGE_HIDDEN	 		(_AT(pteval_t, 1) << _PAGE_BIT_HIDDEN)
#else
#define _PAGE_HIDDEN	 		(_AT(pteval_t, 0))
#endif

#if defined(CONFIG_X86_64) || defined(CONFIG_X86_PAE)
#define _PAGE_NX	         	(_AT(pteval_t, 1) << _PAGE_BIT_NX)
#else
#define _PAGE_NX	         	(_AT(pteval_t, 0))
#endif
```

###### 6.1.2.6.2.5 pgd_page_vaddr()

该函数用于获取PGD所在页面的虚拟地址，其定义于arch/x86/include/asm/pgtable.h:

```
static inline unsigned long pgd_page_vaddr(pgd_t pgd)
{
	// PTE_PFN_MASK定义于pgd_flags()节
	return (unsigned long)__va((unsigned long)pgd_val(pgd) & PTE_PFN_MASK);
}
```

其中，\_\_va(x)定义于arch/x86/include/asm/page.h:

```
#define __va(x)		((void *)((unsigned long)(x)+PAGE_OFFSET))
```

其中，PAGE_OFFSET参见错误：引用源未找到。

###### 6.1.2.6.2.6 pgd_alloc()/pgd_free()

**pgd_alloc(mm)**: Allocates a new Page Global Directory; if PAE is enabled, it also allocates the three children Page Middle Directories that map the User Mode linear addresses. The argument mm (the address of a memory descriptor) is ignored on the 80x86 architecture.

**pgd_free(pgd)**: Releases the Page Global Directory at address pgd; if PAE is enabled, it also releases the three Page Middle Directories that map the User Mode linear addresses.

该函数定义于arch/x86/mm/pgtable.c:

```
pgd_t *pgd_alloc(struct mm_struct *mm)
{
	pgd_t *pgd;
	pmd_t *pmds[PREALLOCATED_PMDS];

	pgd = (pgd_t *)__get_free_page(PGALLOC_GFP);

	if (pgd == NULL)
		goto out;

	// 创建进程的页目录表
	mm->pgd = pgd;

	// 分配pmd_t结构
	if (preallocate_pmds(pmds) != 0)
		goto out_free_pgd;

	if (paravirt_pgd_alloc(mm) != 0)
		goto out_free_pmds;

	/*
	 * Make sure that pre-populating the pmds is atomic with
	 * respect to anything walking the pgd_list, so that they
	 * never see a partially populated pgd.
	 */
	spin_lock(&pgd_lock);

	pgd_ctor(mm, pgd);			// 初始化pgd
	pgd_prepopulate_pmd(mm, pgd, pmds);	// 初始化pmds

	spin_unlock(&pgd_lock);

	return pgd;

out_free_pmds:
	free_pmds(pmds);
out_free_pgd:
	free_page((unsigned long)pgd);
out:
	return NULL;
}

void pgd_free(struct mm_struct *mm, pgd_t *pgd)
{
	pgd_mop_up_pmds(mm, pgd);
	pgd_dtor(pgd);
	paravirt_pgd_free(mm, pgd);
	free_page((unsigned long)pgd);
}
```

##### 6.1.2.6.3 页目录结构/pud_t

###### 6.1.2.6.3.1 pud_t结构

该结构的定义参见页表结构节。

###### 6.1.2.6.3.2 pud_offset()

该函数定义于arch/x86/include/asm/pgtable.h:

```
static inline unsigned long pud_index(unsigned long address)
{
	return (address >> PUD_SHIFT) & (PTRS_PER_PUD - 1);
}

static inline pud_t *pud_offset(pgd_t *pgd, unsigned long address)
{
	// 函数pgd_page_vaddr()参见pgd_page_vaddr()节
	return (pud_t *)pgd_page_vaddr(*pgd) + pud_index(address);
}
```

###### 6.1.2.6.3.3 pud_val()/native_pud_val()

该宏定义于arch/x86/include/asm/pgtable.h:

```
#define pud_val(x)		native_pud_val(x)
```

其中，native_pud_val()定义于arch/x86/include/asm/pgtable_types.h:

```
#if PAGETABLE_LEVELS > 3
typedef struct { pudval_t pud; } pud_t;

static inline pud_t native_make_pud(pmdval_t val)
{
	return (pud_t) { val };
}

static inline pudval_t native_pud_val(pud_t pud)
{
	return pud.pud;
}
#else
#include <asm-generic/pgtable-nopud.h>

static inline pudval_t native_pud_val(pud_t pud)
{
	// 参见pgd_val()/native_pgd_val()节
	return native_pgd_val(pud.pgd);
}
#endif
```

###### 6.1.2.6.3.4 pud_flags()

该函数定义于arch/x86/include/asm/pgtable_types.h:

```
static inline pudval_t pud_flags(pud_t pud)
{
	// PTE_FLAGS_MASK参见pmd_flags()节
	return native_pud_val(pud) & PTE_FLAGS_MASK;
}
```

###### 6.1.2.6.3.5 pud_page_vaddr()

该函数定义于arch/x86/include/asm/pgtable.h:

```
static inline unsigned long pud_page_vaddr(pud_t pud)
{
	return (unsigned long)__va((unsigned long)pud_val(pud) & PTE_PFN_MASK);
}
```

###### 6.1.2.6.3.6 pud_alloc()/pud_free()

**pud_alloc(mm, pgd, addr)**: In a two- or three-level paging system, this function does nothing: it simply returns the linear address of the Page Global Directory entry pgd.

**pud_free(x)**: In a two- or three-level paging system, this macro does nothing.

##### 6.1.2.6.4 页目录结构/pmd_t

###### 6.1.2.6.4.1 pmd_t结构

该结构的定义参见页表结构节。

###### 6.1.2.6.4.2 pmd_offset()

该函数定义于arch/x86/include/asm/pgtable.h:

```
static inline unsigned long pmd_index(unsigned long address)
{
	return (address >> PMD_SHIFT) & (PTRS_PER_PMD - 1);
}

static inline pmd_t *pmd_offset(pud_t *pud, unsigned long address)
{
	return (pmd_t *)pud_page_vaddr(*pud) + pmd_index(address);
}
```

######6.1.2.6.4.3 pmd_val()/native_pmd_val()

该宏定义于arch/x86/include/asm/pgtable.h:

```
#define pmd_val(x)	native_pmd_val(x)
```

其中，native_pmd_val()定义于arch/x86/include/asm/pgtable_types.h:

```
#if PAGETABLE_LEVELS > 2
typedef struct { pmdval_t pmd; } pmd_t;

static inline pmd_t native_make_pmd(pmdval_t val)
{
	return (pmd_t) { val };
}

static inline pmdval_t native_pmd_val(pmd_t pmd)
{
	return pmd.pmd;
}
#else
#include <asm-generic/pgtable-nopmd.h>

static inline pmdval_t native_pmd_val(pmd_t pmd)
{
	// 参见pgd_val()/native_pgd_val()节
	return native_pgd_val(pmd.pud.pgd);
}
#endif
```

###### 6.1.2.6.4.4 pmd_flags()

该函数定义于arch/x86/include/asm/pgtable_types.h:

```
static inline pmdval_t pmd_flags(pmd_t pmd)
{
	// PTE_FLAGS_MASK参见pmd_flags()节
	return native_pmd_val(pmd) & PTE_FLAGS_MASK;
}
```

###### 6.1.2.6.4.5 pmd_page_vaddr() / pmd_pfn()

该函数定义于arch/x86/include/asm/pgtable.h:

```
static inline unsigned long pmd_page_vaddr(pmd_t pmd)
{
	return (unsigned long)__va(pmd_val(pmd) & PTE_PFN_MASK);
}

static inline unsigned long pmd_pfn(pmd_t pmd)
{
	return (pmd_val(pmd) & PTE_PFN_MASK) >> PAGE_SHIFT;
}
```

###### 6.1.2.6.4.6 pmd_alloc()/pmd_free()

**pmd_alloc(mm, pud, addr)**: Defined so generic three-level paging systems can allocate a new Page Middle Directory for the linear address addr. If PAE is not enabled, the function simply returns the input parameter pud — that is, the address of the entry in the Page Global Directory. If PAE is enabled, the function returns the linear address of the Page Middle Directory entry that maps the linear address addr. The argument cw is ignored.

**pmd_free(x)**: Does nothing, because Page Middle Directories are allocated and deallocated together with their parent Page Global Directory.

##### 6.1.2.6.5 页面结构/pte_t

###### 6.1.2.6.5.1 pte_t结构

该结构的定义参见页表结构节。

###### 6.1.2.6.5.2 pte_offset_kernel()

该函数定义于arch/x86/include/asm/pgtable.h:

```
static inline pte_t *pte_offset_kernel(pmd_t *pmd, unsigned long address)
{
	return (pte_t *)pmd_page_vaddr(*pmd) + pte_index(address);
}
```

###### 6.1.2.6.5.3 pte_val()/native_pte_val()

该宏用于获取页表项的值，其定义于arch/x86/include/asm/pgtable.h:

```
#define pte_val(x)		native_pte_val(x)
```

其中，native_pte_val()定义于arch/x86/include/asm/pgtable_types.h:

```
static inline pteval_t native_pte_val(pte_t pte)
{
	return pte.pte;
}

static inline pte_t native_make_pte(pteval_t val)
{
	return (pte_t) { .pte = val };
}
```

###### 6.1.2.6.5.4 pte_flags()

该函数定义于arch/x86/include/asm/pgtable_types.h:

```
static inline pteval_t pte_flags(pte_t pte)
{
	return native_pte_val(pte) & PTE_FLAGS_MASK;
}
```

###### 6.1.2.6.5.4.1 PTE的标志位函数

PTE的标志位函数定义于arch/x86/include/asm/pgtable.h:

```
static inline int pte_dirty(pte_t pte)
{
	return pte_flags(pte) & _PAGE_DIRTY;
}

static inline int pte_young(pte_t pte)
{
	return pte_flags(pte) & _PAGE_ACCESSED;
}

static inline int pte_write(pte_t pte)
{
	return pte_flags(pte) & _PAGE_RW;
}

static inline int pte_file(pte_t pte)
{
	return pte_flags(pte) & _PAGE_FILE;
}

static inline int pte_huge(pte_t pte)
{
	return pte_flags(pte) & _PAGE_PSE;
}

static inline int pte_global(pte_t pte)
{
	return pte_flags(pte) & _PAGE_GLOBAL;
}

static inline int pte_exec(pte_t pte)
{
	return !(pte_flags(pte) & _PAGE_NX);
}

static inline int pte_special(pte_t pte)
{
	return pte_flags(pte) & _PAGE_SPECIAL;
}
```

###### 6.1.2.6.5.5 pte_page()/pte_pfn()

该函数定义于arch/x86/include/asm/pgtable.h:

```
static inline unsigned long pte_pfn(pte_t pte)
{
	return (pte_val(pte) & PTE_PFN_MASK) >> PAGE_SHIFT;
}

#define pte_page(pte)	pfn_to_page(pte_pfn(pte))
```

The **pfn_to_page(pfn)** yields the address of the page descriptor associated with the page frame having number pfn. 其定义于include/asm-generic/memory_model.h:

```
#if defined(CONFIG_FLATMEM)

// 变量mem_map参见mem_map节
#define __pfn_to_page(pfn)	(mem_map + ((pfn) - ARCH_PFN_OFFSET))
#define __page_to_pfn(page)	((unsigned long)((page) - mem_map) + ARCH_PFN_OFFSET)

#elif defined(CONFIG_DISCONTIGMEM)

#define __pfn_to_page(pfn)								\
({	unsigned long __pfn = (pfn);							\
	unsigned long __nid = arch_pfn_to_nid(__pfn);  					\
	NODE_DATA(__nid)->node_mem_map + arch_local_page_offset(__pfn, __nid);	\
})

#define __page_to_pfn(pg) 								\
({	const struct page *__pg = (pg);							\
	struct pglist_data *__pgdat = NODE_DATA(page_to_nid(__pg)); 			\
	(unsigned long)(__pg - __pgdat->node_mem_map) + __pgdat->node_start_pfn;	\
})

#elif defined(CONFIG_SPARSEMEM_VMEMMAP)

/* memmap is virtually contiguous.  */
#define __pfn_to_page(pfn)	(vmemmap + (pfn))
#define __page_to_pfn(page)	(unsigned long)((page) - vmemmap)

#elif defined(CONFIG_SPARSEMEM)
/*
 * Note: section's mem_map is encorded to reflect its start_pfn.
 * section[i].section_mem_map == mem_map's address - start_pfn;
 */
#define __pfn_to_page(pfn)								\
({	unsigned long __pfn = (pfn);							\
	struct mem_section *__sec = __pfn_to_section(__pfn);				\
	__section_mem_map_addr(__sec) + __pfn;						\
})

#define __page_to_pfn(pg)								\
({	const struct page *__pg = (pg);							\
	int __sec = page_to_section(__pg);						\
	(unsigned long)(__pg - __section_mem_map_addr(__nr_to_section(__sec)));		\
})
#endif /* CONFIG_FLATMEM/DISCONTIGMEM/SPARSEMEM */

#define pfn_to_page		__pfn_to_page
#define page_to_pfn		__page_to_pfn
```

###### 6.1.2.6.5.6 pte_alloc_map()/pte_free()/pte_alloc_kernel()/pte_free_kernel()/clear_page_range()

**pte_alloc_map(mm, pmd, addr)**: Receives as parameters the addressof a Page Middle Directory entry pmd and a linear address addr, and returns the address of the Page Table entry corresponding to addr. If the Page Middle Directory entry is null, the function allocatesa new Page Table by invoking pte_alloc_one(). If a new Page Table is allocated, the entry corresponding toaddris initialized and the User/Supervisor flag is set. If the Page Table is kept in high memory, the kernel establishes a temporary kernel mapping, to be released by pte_unmap.

**pte_free(pte)**: Releases the Page Table associated with theptepage descriptor pointer.

**pte_alloc_kernel(mm, pmd, addr)**: If the Page Middle Directory entry pmd associated with the address addr is null, the function allocates a new Page Table. It then returns the linear address of the Page Table entry associated withaddr. Used only for master kernel page tables.

**pte_free_kernel(pte)**: Equivalent to pte_free(), but used for master kernel page tables.

**clear_page_range(mmu, start, end)**: Clears the contents of the page tables of a process from linear address start to end by iteratively releasing its Page Tables and clearing the Page Middle Directory entries.

## 6.2 与内存管理有关的数据结构

### 6.2.1 PAGE_SIZE

PAGE_SIZE表示页面的大小，取值为4096，即页面大小为4KB，其定义于include/asm-generic/page.h:

```
/* PAGE_SHIFT determines the page size */
#define PAGE_SHIFT	12

#ifdef __ASSEMBLY__
#define PAGE_SIZE	(1 << PAGE_SHIFT)
#else
#define PAGE_SIZE	(1UL << PAGE_SHIFT)
#endif

#define PAGE_MASK	(~(PAGE_SIZE-1))
```

### 6.2.2 struct page

该结构定义于include/linux/mm_types.h:

```
struct page {
	/* First double word block */
	// Array of flags (see below).
	// Also encodes the zone number to which the page frame belongs.
	unsigned long				flags;
	// Used when the page is inserted into the page cache, or
	// when it belongs to an anonymous region.
	struct address_space			*mapping;

	/* Second double word */
	struct {
		union {
			// Used by several kernel components with different meanings.
			// For instance, it identifies the position of the data stored
			// in the page frame within the page’s disk image or within an
			// anonymous region, or it stores a swapped-out page identifier.
			pgoff_t			index;	/* Our offset within mapping. */
			void			*freelist;	/* slub first free object */
		};

		union {
			/* Used for cmpxchg_double in slub */
			unsigned long				counters;
			struct {
				union {
					// Number of Page Table entries that refer to the page frame (-1 if none).
					atomic_t		_mapcount;
					struct {
						unsigned	inuse:16;
						unsigned	objects:15;
						unsigned	frozen:1;
					};
				};
				// Page frame’s reference counter. The page_count() returns
				// the value of the _count field.
				// If _count == -1, the corresponding page frame is free and
				// 	can be assigned to any process or to the kernel itself.
				// If _count >= 0,  the page frame is assigned to one or more
				// 	processes or is used to store some kernel data structures.
				atomic_t			_count;
			};
		};
	};

	/* Third double word block */
	union {
		// Contains pointers to the least recently used doubly linked list of pages.
		struct list_head		lru;
		struct {
			struct page		*next;	/* Next partial slab */
#ifdef CONFIG_64BIT
			int			pages;	/* Nr of partial slabs left */
			int			pobjects;	/* Approximate # of objects */
#else
			short int		pages;
			short int		pobjects;
#endif
		};
	};

	/* Remainder is not double word aligned */
	union {
		// Available to the kernel component that is using the page.
		// For instance, it’s a buffer head pointer in case of buffer page.
		// If the page is free, this field is used by the buddy allocator system:
		// 用于保存其order值，参见__rmqueue_smallest()节:
		// * 在__rmqueue_smallest()->rmv_page_order()复位为0；
		// * 在__rmqueue_smallest()->expand()置为特定的order值。
		unsigned long			private;
#if USE_SPLIT_PTLOCKS
		spinlock_t			ptl;
#endif
		struct kmem_cache		*slab;		/* SLUB: Pointer to slab */
		// 通过buffered_rmqueue()->prep_new_page()
		// ->prep_compound_page()设置，参见prep_new_page()节
		struct page			*first_page;	/* Compound tail pages */
	};

#if defined(WANT_PAGE_VIRTUAL)
	Void					*virtual;
#endif

#ifdef CONFIG_WANT_PAGE_DEBUG_FLAGS
	unsigned long				debug_flags;
#endif

#ifdef CONFIG_KMEMCHECK
	Void					*shadow;
#endif
};
```

struct page的结构图:

![Memery_Layout_16](/assets/Memery_Layout_16.jpg)

struct page中flags域的取值如下，参见include/linux/page-flags.h:

```
enum pageflags {
	// for instance, it’s involved in a disk I/O operation.
	PG_locked,		/* Page is locked. Don't touch. */
	PG_error,		// An I/O error occurred while transferring the page.
	PG_referenced,		// The page has been recently accessed.
	PG_uptodate,		// It’s set after completing a read operation, unless a disk I/O error happened.
	PG_dirty,		// The page has been modified.
	PG_lru,			// The page is in the active or inactive page list.
	PG_active,		// The page is in the active page list.
	PG_slab,		// The page frame is included in a slab.
	PG_owner_priv_1,	/* Owner use. If pagecache, fs may use*/
	PG_arch_1,		// Not used on the 80x86 architecture.
	PG_reserved,		// The page frame is reserved for kernel code or is unusable.
	// The private field of the page descriptor stores meaningful data.
	PG_private,		/* If pagecache, has fs-private data */
	PG_private_2,		/* If pagecache, has fs aux data */
	// The page is being written to disk by means of the writepage() method.
	PG_writeback,		/* Page is under writeback */
#ifdef CONFIG_PAGEFLAGS_EXTENDED
	PG_head,		/* A head page */
	PG_tail,		/* A tail page */
#else
	// The page frame is handled through the extended paging mechanism.
	PG_compound,		/* A compound page */
#endif
	// The page belongs to the swap cache.
	PG_swapcache,		/* Swap page: swp_entry_t in private */
	// All data in the page frame corresponds to blocks allocated on disk.
	PG_mappedtodisk,	/* Has blocks allocated on-disk */
	// The page has been marked to be written to disk in order to reclaim memory.
	PG_reclaim,		/* To be reclaimed asap */
	PG_swapbacked,		/* Page is backed by RAM/swap */
	PG_unevictable,		/* Page is "unevictable"  */
#ifdef CONFIG_MMU
	PG_mlocked,		/* Page is vma mlocked */
#endif
#ifdef CONFIG_ARCH_USES_PG_UNCACHED
	PG_uncached,		/* Page has been mapped as uncached */
#endif
#ifdef CONFIG_MEMORY_FAILURE
	PG_hwpoison,		/* hardware poisoned page. Don't touch */
#endif
#ifdef CONFIG_TRANSPARENT_HUGEPAGE
	PG_compound_lock,
#endif
	__NR_PAGEFLAGS,

	/* Filesystems */
	// Used by some filesystems such as Ext2 and Ext3.
	PG_checked		= PG_owner_priv_1,

	/* Two page bits are conscripted by FS-Cache to maintain local caching
	 * state.  These bits are set on pages belonging to the netfs's inodes
	 * when those inodes are being locally cached.
	 */
	PG_fscache		= PG_private_2,	/* page backed by cache */

	/* XEN */
	PG_pinned		= PG_owner_priv_1,
	PG_savepinned		= PG_dirty,

	/* SLOB */
	PG_slob_free		= PG_private,
};
```

#### 6.2.2.1 mem_map

All page descriptors are stored in the mem_map array. 其定义于mm/memory.c:

```
#ifndef CONFIG_NEED_MULTIPLE_NODES
/* use the per-pgdat data instead for discontigmem - mbligh */
unsigned long	max_mapnr;
struct page	*mem_map;
#endif
```

变量mem_map初始化过程如下：

```
start_kernel()
-> setup_arch()
   -> paging_init()
      -> zone_sizes_init()
         -> free_area_init_nodes()
            -> free_area_init_node()
               -> alloc_node_mem_map()
```

函数alloc_node_mem_map()定义于mm/page_alloc.c:

```
static void __init_refok alloc_node_mem_map(struct pglist_data *pgdat)
{
	/* Skip empty nodes */
	if (!pgdat->node_spanned_pages)
		return;

#ifdef CONFIG_FLAT_NODE_MEM_MAP
	/* ia64 gets its own node_mem_map, before this, without bootmem */
	if (!pgdat->node_mem_map) {
		unsigned long size, start, end;
		struct page *map;

		/*
		 * The zone's endpoints aren't required to be MAX_ORDER
		 * aligned but the node_mem_map endpoints must be in order
		 * for the buddy allocator to function correctly.
		 */
		// MAX_ORDER_NR_PAGES = 1024
		start = pgdat->node_start_pfn & ~(MAX_ORDER_NR_PAGES - 1);
		end = pgdat->node_start_pfn + pgdat->node_spanned_pages;
		end = ALIGN(end, MAX_ORDER_NR_PAGES);
		size =  (end - start) * sizeof(struct page);
		map = alloc_remap(pgdat->node_id, size);
		if (!map)
			map = alloc_bootmem_node_nopanic(pgdat, size);
		pgdat->node_mem_map = map + (pgdat->node_start_pfn - start);
	}
#ifndef CONFIG_NEED_MULTIPLE_NODES
	/*
	 * With no DISCONTIG, the global mem_map is just set as node 0's
	 */
	if (pgdat == NODE_DATA(0)) {
		mem_map = NODE_DATA(0)->node_mem_map;
#ifdef CONFIG_ARCH_POPULATES_NODE_MAP
		if (page_to_pfn(mem_map) != pgdat->node_start_pfn)
			mem_map -= (pgdat->node_start_pfn - ARCH_PFN_OFFSET);
#endif /* CONFIG_ARCH_POPULATES_NODE_MAP */
	}
#endif
#endif /* CONFIG_FLAT_NODE_MEM_MAP */
}
```

Page descriptor与其所描述的Page之间的关系:

![Page_Descriptor_and_Page](/assets/Page_Descriptor_and_Page.jpg)

变量mem_map用于计算page descriptor与物理页面之间的映射关系，即宏__pfn_to_page(pfn)和__page_to_pfn(page)，参见pte_page()/pte_pfn()节。

### 6.2.3 struct zone

该结构定义于include/linux/mmzone.h:

```
struct zone {
	// 参见enum zone_watermarks
	unsigned long		watermark[NR_WMARK];
	unsigned long 		percpu_drift_mark;
	unsigned long 		lowmem_reserve[MAX_NR_ZONES];

#ifdef CONFIG_NUMA
	// 取值与struct zone->zone_pgdat->node_nid相同
	int			node;
	unsigned long		min_unmapped_pages;
	unsigned long		min_slab_pages;
#endif

	// The Per-CPU Page Frame Cache
	struct per_cpu_pageset __percpu *pageset;
	spinlock_t		lock;
	int			all_unreclaimable;

#ifdef CONFIG_MEMORY_HOTPLUG
	seqlock_t		span_seqlock;
#endif
	/*
	 * Identifies the blocks of free page frames in the zone.
	 *
	 * Buddy Allocator System Algorithm. All free page frames are grouped into 11 lists
	 * of blocks that contain groups of 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, and 1024
	 * contiguous page frames, respectively. that’s, free_area[k] has 2k contiguous page
	 * frames.
	 *
	 * NOTE #1: The physical address of the first page frame of a block is a multiple of
	 * the group size. for example, the initial address of a 16-page-frame block is a
	 * multiple of 16×212
	 *
	 * NOTE #2: The free_list field of free_area[k] is the head of a doubly linked circular
	 * list that collects the page descriptors associated with the free blocks of 2k pages.
	 * More precisely, this list includes the page descriptors of the starting page frame
	 * of every block of 2k free page frames; the pointers to the adjacent elements in the
	 * list are stored in the lru field of the page descriptor.
	 */
	struct free_area	free_area[MAX_ORDER];

#ifndef CONFIG_SPARSEMEM
	unsigned long		*pageblock_flags;
#endif /* CONFIG_SPARSEMEM */

#ifdef CONFIG_COMPACTION
	unsigned int		compact_considered;
	unsigned int		compact_defer_shift;
#endif

	ZONE_PADDING(_pad1_)

	spinlock_t		lru_lock;
	struct zone_lru {
		struct list_head list;
	} lru[NR_LRU_LISTS];

	struct zone_reclaim_stat reclaim_stat;

	// Counter used when doing page frame reclaiming in the zone
	unsigned long		pages_scanned;
	unsigned long		flags;

	atomic_long_t		vm_stat[NR_VM_ZONE_STAT_ITEMS];

	unsigned int		inactive_ratio;

	ZONE_PADDING(_pad2_)

	// Hash table of wait queues of processes waiting for one of the pages of the zone.
	wait_queue_head_t	*wait_table;
	unsigned long		wait_table_hash_nr_entries;
	// Power-of-2 order of the size of the wait queue hash table array.
	unsigned long		wait_table_bits;

	// struct pglist_data->node_zones[*]指向本结构体，而本域指向struct pglist_data
	struct pglist_data	*zone_pgdat;
	// 本zone包含的物理页的起始帧号，即页地址中12-31位的取值
	unsigned long		zone_start_pfn;

	unsigned long		spanned_pages;	/* total size of the zone in pages, including holes */
	unsigned long		present_pages;	/* amount of memory (excluding holes) */

	// 本zone的名字，取值参见数组zone_names[]
	const char		*name;
} ____cacheline_internodealigned_in_smp;
```

其结构参见错误：引用源未找到。

### 6.2.4 pg_data_t

该类型定义于include/linux/mmzone.h:

```
typedef struct pglist_data {
	struct zone		node_zones[MAX_NR_ZONES];		// Array of zone descriptors of the node
	struct zonelist		node_zonelists[MAX_ZONELISTS]; 		// Used by the page allocator
	int			nr_zones;				// Number of zones in the node

#ifdef CONFIG_FLAT_NODE_MEM_MAP	/* means !SPARSEMEM */
	// The first page of the struct page array representing each physical frame in the node.
	// It will be placed somewhere within the global mem_map array.
	struct page		*node_mem_map;				// Array of page descriptors of the node
#ifdef CONFIG_CGROUP_MEM_RES_CTLR
	struct page_cgroup	*node_page_cgroup;
#endif
#endif

#ifndef CONFIG_NO_BOOTMEM
	// Pointer to Boot Memory Allocatoer, which is used in the kernel initialization phase.
	// 参见free_all_bootmem()/free_all_bootmem_core()节和Initialise the Boot Memory Allocator节
	struct bootmem_data	*bdata;
#endif

#ifdef CONFIG_MEMORY_HOTPLUG
	/*
	 * Must be held any time you expect node_start_pfn, node_present_pages
	 * or node_spanned_pages stay constant.  Holding this will also
	 * guarantee that any pfn_valid() stays that way.
	 *
	 * Nests above zone->lock and zone->size_seqlock.
	 */
	spinlock_t		node_size_lock;
#endif

	// Index of the first page frame in the node
	unsigned long		node_start_pfn;
	// Size of the memory node, excluding holes (in page frames)
	unsigned long		node_present_pages; /* total number of physical pages */
	// Size of the node, including holes (in page frames)
	unsigned long		node_spanned_pages; /* total size of physical page range, including holes */
	// Identifier of the node, starts at 0
	int			node_id;
	// Wait queue for the kswapd pageout daemon
	wait_queue_head_t	kswapd_wait;
	// Pointer to the process descriptor of the kswapd kernel thread. 参见kswapd节
	struct task_struct	*kswapd;
	// Logarithmic size of free blocks to be created by kswapd
	int			kswapd_max_order;
	enum zone_type		classzone_idx;
} pg_data_t;
```

其结构参见错误：引用源未找到。

在mm/bootmem.c中定义了一个该类型的全局变量contig_page_data:

```
#ifndef CONFIG_NEED_MULTIPLE_NODES
struct pglist_data __refdata	contig_page_data = {
	.bdata = &bootmem_node_data[0]
};
#endif
```

该变量可通过include/linux/mmzone.h中的如下宏访问：

```
#ifndef CONFIG_NEED_MULTIPLE_NODES
extern struct pglist_data		contig_page_data;
#define NODE_DATA(nid)			(&contig_page_data)
#define NODE_MEM_MAP(nid)		mem_map
#else /* CONFIG_NEED_MULTIPLE_NODES */
#include <asm/mmzone.h>
#endif /* !CONFIG_NEED_MULTIPLE_NODES */
```

### 6.2.5 gfp_t

该类型定义于include/linux/gfp.h:

![Memery_Layout_06](/assets/Memery_Layout_06.jpg)

### 6.2.6 struct mm_struct

The kernel represents a process’s address space with a data structure called **the memory descriptor**. This structure contains all the information related to the process address space. The memory descriptor is represented by struct mm_struct and defined in include/linux/mm_types.h:

```
struct mm_struct {
	// Pointer to the head of the list of memory region objects. 参见struct vm_area_struct节
	struct vm_area_struct		*mmap;		/* list of VMAs */
	// Pointer to the root of the red-black tree of memory region objects
	struct rb_root 			mm_rb;
	// Pointer to the last referenced memory region object
	struct vm_area_struct 		*mmap_cache;	/* last find_vma result */
#ifdef CONFIG_MMU
	// Method that searches an available linear address interval in the process address space
	unsigned long (*get_unmapped_area) (struct file *filp, unsigned long addr, unsigned long len,
							   unsigned long pgoff, unsigned long flags);
	// Method invoked when releasing a linear address interval
	void (*unmap_area) (struct mm_struct *mm, unsigned long addr);
#endif
	// Identifies the linear address of the first allocated anonymousmemory region or file memory mapping
	unsigned long 			mmap_base;		/* base of mmap area */
	unsigned long 			task_size;		/* size of task vm space */
	unsigned long 			cached_hole_size; 	/* if non-zero, the largest hole below free_area_cache */
	/*
	 * Address from which the kernel will look for a free interval of linear addresses
	 * in the process address space
	 */
	unsigned long 			free_area_cache;	/* first hole of size cached_hole_size or larger */
	/*
	 * Pointer to the Page Global Directory, which is a physical page frame.
	 * 参见Linear Address转换到Physical Address节
	 * On the x86, the process page table is loaded by copying mm_struct->pgd
	 * into the cr3 register which has the side effect of flushing the TLB.
	 * In fact this is how the function __flush_tlb() is implemented in the
	 * architecture dependent code.
	 */
	pgd_t 				*pgd;
	/*
	 * mm_count is main usage counter; all users in mm_users count as one unit in mm_count.
	 * Every time the mm_count is decreased, the kernel checks whether it becomes zero;
	 * if so, the memory descriptor is deallocated because it is no longer in use.
	 */
	atomic_t 			mm_users;	/* How many users with user space? */
	atomic_t 			mm_count;	/* How many references to "struct mm_struct" (users count as 1) */
	/*
	 * map_count field contains the number of memory regions owned by the process.
	 * By default, a process may own up to 65,536 different memory regions;
	 * however, the system administrator may change this limit by writing in
	 * /proc/sys/vm/max_map_count，参do_mmap_pgoff()见节，do_mmap_pgoff():
	 * if (mm->map_count > sysctl_max_map_count)
	 */
	int 				map_count;			/* number of VMAs */

	spinlock_t 			page_table_lock;		/* Protects page tables and some counters */
	struct rw_semaphore 		mmap_sem;			// Memory regions’read/write semaphore

	/*
	 * List of maybe swapped mm's.
	 * These are globally strung together off init_mm.mmlist,
	 * and are protected by mmlist_lock.
	 */
	/*
	 * The first element of list mmlist is init_mm.mmlist,
	 * which is used by process 0 in the initialization
	 */
	struct list_head 		mmlist;

	unsigned long 			hiwater_rss;		/* High-watermark of RSS usage */
	unsigned long 			hiwater_vm;		/* High-water virtual memory usage */

	unsigned long 			total_vm;		/* Total pages mapped */
	unsigned long 			locked_vm;		/* Pages that have PG_mlocked set */
	unsigned long 			pinned_vm;		/* Refcount permanently increased */
	unsigned long 			shared_vm;		/* Shared pages (files) */
	unsigned long 			exec_vm;		/* VM_EXEC & ~VM_WRITE */
	unsigned long 			stack_vm;		/* VM_GROWSUP/DOWN */
	unsigned long 			reserved_vm;		/* VM_RESERVED|VM_IO pages */
	unsigned long 			def_flags;
	unsigned long 			nr_ptes;		/* Page table pages */

	/*
	 * start_code / end_code: Initial / Final address of executable code
	 * start_data / end_data: Initial / Final address of initialized data
	 */
	unsigned long 			start_code, end_code, start_data, end_data;
	/*
	 * start_brk / brk: Initial / Current final address of the heap
	 * start_stack: Initial address of User Mode stack
	 */
	unsigned long 			start_brk, brk, start_stack;
	/*
	 * arg_start / arg_end: Initial / Final address of command-line arguments
	 * env_start / end_start: Initial / Final address of environment variables
	 */
	unsigned long 			arg_start, arg_end, env_start, env_end;

	unsigned long 			saved_auxv[AT_VECTOR_SIZE]; /* for /proc/PID/auxv */

	/*
	 * Special counters, in some configurations protected by the
	 * page_table_lock, in other configurations by being atomic.
	 */
	struct mm_rss_stat 		rss_stat;

	struct linux_binfmt 		*binfmt;

	cpumask_var_t 			cpu_vm_mask_var;

	/* Architecture-specific MM context */
	mm_context_t 			context;

	/* Swap token stuff */
	/*
	 * Last value of global fault stamp as seen by this process.
	 * In other words, this value gives an indication of how long
	 * it has been since this task got the token.
	 * Look at mm/thrash.c
	 */
	unsigned int 			faultstamp;
	unsigned int 			token_priority;
	unsigned int 			last_interval;

	unsigned long 			flags; 		/* Must use atomic bitops to access the bits */

	struct core_state 		*core_state;	/* coredumping support */
#ifdef CONFIG_AIO
	spinlock_t			ioctx_lock;
	struct hlist_head		ioctx_list;
#endif
#ifdef CONFIG_MM_OWNER
	/*
	 * "owner" points to a task that is regarded as the canonical
	 * user/owner of this mm. All of the following must be true in
	 * order for it to be changed:
	 *
	 * current == mm->owner
	 * current->mm != mm
	 * new_owner->mm == mm
	 * new_owner->alloc_lock is held
	 */
	struct task_struct __rcu	*owner;
#endif

	/* store ref to file /proc/<pid>/exe symlink points to */
	struct file 			*exe_file;
	unsigned long 			num_exe_file_vmas;
#ifdef CONFIG_MMU_NOTIFIER
	struct mmu_notifier_mm	*mmu_notifier_mm;
#endif
#ifdef CONFIG_TRANSPARENT_HUGEPAGE
	pgtable_t 			pmd_huge_pte; /* protected by page_table_lock */
#endif
#ifdef CONFIG_CPUMASK_OFFSTACK
	struct cpumask 			cpumask_allocation;
#endif
};
```

链表mm_struct:

![Memery_Layout_24](/assets/Memery_Layout_24.jpg)

若存在进程号为1234的进程，则可通过如下两种方式查看其虚拟内存空间：

```
$ cat /proc/1234/maps
$ cat /proc/1234/smaps
$ pmap 1234
```

### 6.2.7 struct vm_area_struct

Linux implements a memory region by means of an object of type vm_area_struct.

Each memory region descriptor identifies a linear address interval. The vm_start field contains the first linear address of the interval, while the vm_end field contains the first linear address outside of the interval; vm_end – vm_start thus denotes the length of the memory region.

Memory regions owned by a process never overlap, and the kernel tries to merge regions when a new one is allocated right next to an existing one. Two adjacent regions can be merged if their access rights match.

该结构定义于include/linux/mm_types.h:

```
struct vm_area_struct {
	// 参见struct mm_struct节
	struct mm_struct		*vm_mm;		/* The address space we belong to. */
	unsigned long			vm_start;		/* Our start address within vm_mm. */
	unsigned long			vm_end;		/* The first byte after our end address within vm_mm. */

	/* linked list of VM areas per task, sorted by address */
	struct vm_area_struct		*vm_next, *vm_prev;

	pgprot_t			vm_page_prot;	/* Access permissions of this VMA. */
	unsigned long			vm_flags;		/* Flags, see mm.h. */

	struct rb_node			vm_rb;

	/*
	 * For areas with an address space and backing store,
	 * linkage into the address_space->i_mmap prio tree, or
	 * linkage to the list of like vmas hanging off its node, or
	 * linkage of vma in the address_space->i_mmap_nonlinear list.
	 */
	union {
		struct {
			struct list_head		list;
			void				*parent;	/* aligns with prio_tree_node parent */
			struct vm_area_struct		*head;
		} vm_set;

		struct raw_prio_tree_node		prio_tree_node;
	} shared;

	/*
	 * A file's MAP_PRIVATE vma can be in both i_mmap tree and anon_vma
	 * list, after a COW of one of the file pages.	A MAP_SHARED vma
	 * can only be in the i_mmap tree.  An anonymous MAP_PRIVATE, stack
	 * or brk vma (with NULL file) can only be in an anon_vma list.
	 */
	struct list_head			anon_vma_chain;	/* Serialized by mmap_sem & page_table_lock */
	struct anon_vma				*anon_vma;		/* Serialized by page_table_lock */

	/* Function pointers to deal with this struct. */
	// 参见struct vm_operations_struct节
	const struct vm_operations_struct	*vm_ops;

	/* Information about our backing store: */
	/* Offset (within vm_file) in PAGE_SIZE units, *not* PAGE_CACHE_SIZE */
	unsigned long				vm_pgoff;
	// Pointer to the file being mapped, see 错误：引用源未找到
	struct file				*vm_file;		/* File we map to (can be NULL). */
	void				*vm_private_data;	/* was vm_pte (shared mem) */

#ifndef CONFIG_MMU
	struct vm_region		*vm_region;	/* NOMMU mapping region */
#endif
#ifdef CONFIG_NUMA
	struct mempolicy		*vm_policy;	/* NUMA policy for the VMA */
#endif
};
```

All the regions owned by a process are linked in a simple list. Regions appear in the list in ascending order by memory address; however, successive regions can be separated by an area of unused memory addresses.

A full list of mapped regions a process has may be viewed via the proc interface at /proc/<PID>/maps where PID is the process ID of the process that is to be examined.

Descriptors related to the address space of a process，seen

![Memery_Layout_25](/assets/Memery_Layout_25.jpg)

#### 6.2.7.1 struct vm_operations_struct

该结构定义于include/linux/mm_types.h:

```
struct vm_operations_struct {
	// Invoked when the memory region is added to the set of regions owned by a process.
	void	(*open)(struct vm_area_struct * area);
	// Invoked when the memory region is removed from the set of regions owned by a process.
	void	(*close)(struct vm_area_struct * area);
	/*
	 * The callback is responsible for locating the page in the page cache or
	 * allocating a page and populating it with the required data before returning it.
	 * See section fault()/filemap_fault()
	 */
	int	(*fault)(struct vm_area_struct *vma, struct vm_fault *vmf);

	/* notification that a previously read-only page is about to become
	 * writable, if an error is returned it will cause a SIGBUS */
	int	(*page_mkwrite)(struct vm_area_struct *vma, struct vm_fault *vmf);

	/* called by access_process_vm when get_user_pages() fails, typically
	 * for use by special VMAs that can switch between memory and hardware
	 */
	int	(*access)(struct vm_area_struct *vma, unsigned long addr, void *buf, int len, int write);
#ifdef CONFIG_NUMA
	/*
	 * set_policy() op must add a reference to any non-NULL @new mempolicy
	 * to hold the policy upon return.  Caller should pass NULL @new to
	 * remove a policy and fall back to surrounding context--i.e. do not
	 * install a MPOL_DEFAULT policy, nor the task or system default
	 * mempolicy.
	 */
	int	(*set_policy)(struct vm_area_struct *vma, struct mempolicy *new);

	/*
	 * get_policy() op must add reference [mpol_get()] to any policy at
	 * (vma,addr) marked as MPOL_SHARED.  The shared policy infrastructure
	 * in mm/mempolicy.c will do this automatically.
	 * get_policy() must NOT add a ref if the policy at (vma,addr) is not
	 * marked as MPOL_SHARED. vma policies are protected by the mmap_sem.
	 * If no [shared/vma] mempolicy exists at the addr, get_policy() op
	 * must return NULL--i.e., do not "fallback" to task or system default
	 * policy.
	 */
	struct mempolicy *(*get_policy)(struct vm_area_struct *vma, unsigned long addr);
	int	(*migrate)(struct vm_area_struct *vma, const nodemask_t *from,
				const nodemask_t *to, unsigned long flags);
#endif
};
```

##### 6.2.7.1.1 fault()/filemap_fault()

struct vm_operations_struct->fault可被注册为filemap_fault()，其定义于mm/filemap.c:

```
const struct vm_operations_struct generic_file_vm_ops = {
	.fault	= filemap_fault,
};

/**
 * filemap_fault - read in file data for page fault handling
 * @vma:	vma in which the fault was taken
 * @vmf:	struct vm_fault containing details of the fault
 *
 * filemap_fault() is invoked via the vma operations vector for a
 * mapped memory region to read in file data during a page fault.
 *
 * The goto's are kind of ugly, but this streamlines the normal case of having
 * it in the page cache, and handles the special cases reasonably without
 * having a lot of duplicated code.
 */
int filemap_fault(struct vm_area_struct *vma, struct vm_fault *vmf)
{
	int error;
	struct file *file = vma->vm_file;
	struct address_space *mapping = file->f_mapping;
	struct file_ra_state *ra = &file->f_ra;
	struct inode *inode = mapping->host;
	pgoff_t offset = vmf->pgoff;
	struct page *page;
	pgoff_t size;
	int ret = 0;

	size = (i_size_read(inode) + PAGE_CACHE_SIZE - 1) >> PAGE_CACHE_SHIFT;
	if (offset >= size)
		return VM_FAULT_SIGBUS;

	/*
	 * Do we have something in the page cache already?
	 */
	page = find_get_page(mapping, offset);
	if (likely(page)) {
		/*
		 * We found the page, so try async readahead before
		 * waiting for the lock.
		 */
		do_async_mmap_readahead(vma, ra, file, page, offset);
	} else {
		/* No page in the page cache at all */
		do_sync_mmap_readahead(vma, ra, file, offset);
		count_vm_event(PGMAJFAULT);
		mem_cgroup_count_vm_event(vma->vm_mm, PGMAJFAULT);
		ret = VM_FAULT_MAJOR;
retry_find:
		page = find_get_page(mapping, offset);
		if (!page)
			goto no_cached_page;
	}

	if (!lock_page_or_retry(page, vma->vm_mm, vmf->flags)) {
		page_cache_release(page);
		return ret | VM_FAULT_RETRY;
	}

	/* Did it get truncated? */
	if (unlikely(page->mapping != mapping)) {
		unlock_page(page);
		put_page(page);
		goto retry_find;
	}
	VM_BUG_ON(page->index != offset);

	/*
	 * We have a locked page in the page cache, now we need to check
	 * that it's up-to-date. If not, it is going to be due to an error.
	 */
	if (unlikely(!PageUptodate(page)))
		goto page_not_uptodate;

	/*
	 * Found the page and have a reference on it.
	 * We must recheck i_size under page lock.
	 */
	size = (i_size_read(inode) + PAGE_CACHE_SIZE - 1) >> PAGE_CACHE_SHIFT;
	if (unlikely(offset >= size)) {
		unlock_page(page);
		page_cache_release(page);
		return VM_FAULT_SIGBUS;
	}

	vmf->page = page;
	return ret | VM_FAULT_LOCKED;

no_cached_page:
	/*
	 * We're only likely to ever get here if MADV_RANDOM is in
	 * effect.
	 */
	error = page_cache_read(file, offset);

	/*
	 * The page we want has now been added to the page cache.
	 * In the unlikely event that someone removed it in the
	 * meantime, we'll just come back here and read it again.
	 */
	if (error >= 0)
		goto retry_find;

	/*
	 * An error return from page_cache_read can result if the
	 * system is low on memory, or a problem occurs while trying
	 * to schedule I/O.
	 */
	if (error == -ENOMEM)
		return VM_FAULT_OOM;
	return VM_FAULT_SIGBUS;

page_not_uptodate:
	/*
	 * Umm, take care of errors if the page isn't up-to-date.
	 * Try to re-read it _once_. We do this synchronously,
	 * because there really aren't any performance issues here
	 * and we need to check for errors.
	 */
	ClearPageError(page);
	error = mapping->a_ops->readpage(file, page);
	if (!error) {
		wait_on_page_locked(page);
		if (!PageUptodate(page))
			error = -EIO;
	}
	page_cache_release(page);

	if (!error || error == AOP_TRUNCATED_PAGE)
		goto retry_find;

	/* Things didn't work out. Return zero to tell the mm layer so. */
	shrink_readahead_size_eio(file, ra);
	return VM_FAULT_SIGBUS;
}
```

### 6.2.8 struct address_space

该结构定义于include/linux/fs.h:

```
struct address_space {
	struct inode			*host;			/* owner: inode, block_device */
	struct radix_tree_root		page_tree;			/* radix tree of all pages */
	spinlock_t			tree_lock;			/* and lock protecting it */
	unsigned int			i_mmap_writable;		/* count VM_SHARED mappings */
	struct prio_tree_root		i_mmap;			/* tree of private and shared mappings */
	struct list_head		i_mmap_nonlinear;	/*list VM_NONLINEAR mappings */
	struct mutex			i_mmap_mutex;		/* protect tree, count, list */
	/* Protected by tree_lock together with the radix tree */
	unsigned long			nrpages;			/* number of total pages */
	pgoff_t				writeback_index;		/* writeback starts here */
	// 参见struct address_space_operations节
	const struct address_space_operations *a_ops;	/* methods */
	unsigned long			flags;			/* error bits/gfp mask */
	struct backing_dev_info		*backing_dev_info;	/* device readahead, etc */
	spinlock_t				private_lock;		/* for use by the address_space */
	struct list_head			private_list;		/* ditto */
	struct address_space			*assoc_mapping;		/* ditto */
} __attribute__((aligned(sizeof(long))));
```

#### 6.2.8.1 struct address_space_operations

该结构定义于include/linux/fs.h:

```
struct address_space_operations {
	/*
	 * Write a page to disk. The offset within the file
	 * to write to is stored within the struct page.
	 */
	int (*writepage)(struct page *page, struct writeback_control *wbc);
	// Read a page from disk
	int (*readpage)(struct file *, struct page *);

	/* Write back some dirty pages from this mapping. */
	int (*writepages)(struct address_space *, struct writeback_control *);

	/* Set a page dirty.  Return true if this dirtied it */
	int (*set_page_dirty)(struct page *page);

	int (*readpages)(struct file *filp, struct address_space *mapping,
				struct list_head *pages, unsigned nr_pages);

	int (*write_begin)(struct file *, struct address_space *mapping, loff_t pos,
				   unsigned len, unsigned flags, struct page **pagep, void **fsdata);
	int (*write_end)(struct file *, struct address_space *mapping, loff_t pos, unsigned len,
				unsigned copied, struct page *page, void *fsdata);

	/* Unfortunately this kludge is needed for FIBMAP. Don't use it */
	sector_t (*bmap)(struct address_space *, sector_t);
	void (*invalidatepage)(struct page *, unsigned long);
	int (*releasepage)(struct page *, gfp_t);
	void (*freepage)(struct page *);
	ssize_t (*direct_IO)(int, struct kiocb *, const struct iovec *iov,
				     loff_t offset, unsigned long nr_segs);
	int (*get_xip_mem)(struct address_space *, pgoff_t, int, void **, unsigned long *);

	/* migrate the contents of a page to the specified target */
	int (*migratepage)(struct address_space *, struct page *, struct page *);
	int (*launder_page)(struct page *);
	int (*is_partially_uptodate)(struct page *, read_descriptor_t *, unsigned long);
	int (*error_remove_page)(struct address_space *, struct page *);
};
```

### 6.2.9 Boot Memory Allocator/bootmem_data_t

In order to allocate memory to initialise itself, a specialised allocator called the Boot Memory Allocator is used. It is based on the most basic of allocators, a First Fit allocator which uses a bitmap to represent memory instead of linked lists of free blocks. If a bit is 1, the page is allocated and 0 if unallocated. To satisfy allocations of sizes smaller than a page, the allocator records the Page Frame Number (PFN) of the last allocation and the offset the allocation ended at. Subsequent small allocations are "merged" together and stored on the same page.

bootmem_data_t定义于include/linux/bootmem.h:

```
#ifndef CONFIG_NO_BOOTMEM
/*
 * node_bootmem_map is a map pointer - the bits represent all physical
 * memory pages (including holes) on the node.
 */
typedef struct bootmem_data {
	// Starting physical address of the represented block
	unsigned long		node_min_pfn;
	// End physical address, in other words, the end of the ZONE_NORMAL this node represents
	unsigned long 		node_low_pfn;
	// The location of the bitmap representing allocated or free pages with each bit
	void				*node_bootmem_map;
	// The offset within the the page of the end of the last allocation. If 0, the page used is full.
	unsigned long		last_end_off;
	/*
	 * The PFN of the page used with the last allocation.
	 * Using this with the last_end_off field, a test can
	 * be made to see if allocations can be merged with the
	 * page used for the last allocation rather than using
	 * up a full new page.
	 */
	unsigned long		hint_idx;
	struct list_head		list;
} bootmem_data_t;
#endif
```

#### 6.2.9.1 变量bdata_list

所有类型为bootmem_data_t的变量链接到双向循环链表bdata_list中，其赋值过程参见Initialise the Boot Memory Allocator节。该变量定义于mm/bootmem.c:

```
static struct list_head bdata_list __initdata = LIST_HEAD_INIT(bdata_list);
```

链表bdata_list:

![Memery_Layout_26](/assets/Memery_Layout_26.jpg)

#### 6.2.9.2 Initialise the Boot Memory Allocator

Each architecture is required to supply a setup_arch() function which, among other tasks, is responsible for acquiring the necessary parameters to initialise the boot memory allocator.

Each architecture has its own function to get the necessary parameters. On the x86, it is called setup_arch(). Regardless of the architecture, the tasks are essentially the same. See section e820=>memblock.memory. The parameters it calculates are:

| Variable Name | Description |
| :------------ | :---------- |
| min_low_pfn   | Page frame number of the first usable page frame after the kernel image in RAM |
| max_low_pfn   | Page frame number of the last page frame directly mapped by the kernel (low memory) |
| highstart_pfn | Page frame number of the first page frame not directly mapped by the kernel |
| highend_pfn   | Page frame number of the last page frame not directly mapped by the kernel |
| max_pfn       | Page frame number of the last usable page frame |

<p/>

函数init_bootmem()定义于mm/bootmem.c:

```
/**
 * init_bootmem_node - register a node as boot memory
 * @pgdat: node to register
 * @freepfn: pfn where the bitmap for this node is to be placed
 * @startpfn: first pfn on the node
 * @endpfn: first pfn after the node
 *
 * Returns the number of bytes needed to hold the bitmap for this node.
 */
unsigned long __init init_bootmem_node(pg_data_t *pgdat, unsigned long freepfn,
					 unsigned long startpfn, unsigned long endpfn)
{
	return init_bootmem_core(pgdat->bdata, freepfn, startpfn, endpfn);
}
```

其中，函数init_bootmem_core()定义于include/linux/mmzone.h:

```
/*
 * Called once to set up the allocator itself.
 */
static unsigned long __init init_bootmem_core(bootmem_data_t *bdata, unsigned long mapstart,
			 unsigned long start, unsigned long end)
{
	unsigned long mapsize;

	mminit_validate_memmodel_limits(&start, &end);
	bdata->node_bootmem_map = phys_to_virt(PFN_PHYS(mapstart));
	bdata->node_min_pfn = start;
	bdata->node_low_pfn = end;
	link_bootmem(bdata);		// 将bdata插入到链表bdata_list的适当位置

	/*
	 * Initially all pages are reserved - setup_arch() has to
	 * register free RAM areas explicitly.
	 */
	mapsize = bootmap_bytes(end - start);
	memset(bdata->node_bootmem_map, 0xff, mapsize);

	bdebug("nid=%td start=%lx map=%lx end=%lx mapsize=%lx\n",
		  bdata - bootmem_node_data, start, mapstart, end, mapsize);

	return mapsize;
}
```

其中，函数link_bootmem()定义于include/linux/mmzone.h:

```
static void __init link_bootmem(bootmem_data_t *bdata)
{
	struct list_head *iter;

	// 变量bdata_list参见变量bdata_list节
	list_for_each(iter, &bdata_list) {
		bootmem_data_t *ent;

		ent = list_entry(iter, bootmem_data_t, list);
		if (bdata->node_min_pfn < ent->node_min_pfn)
			break;
	}
	list_add_tail(&bdata->list, iter);
}
```

#### 6.2.9.3 Boot Memory Allocator APIs

##### 6.2.9.3.1 Boot Memory Allocator API for UMA Architectures

```
unsigned long init_bootmem(unsigned long start, unsigned long page)
This initialises the memory between 0 and the PFN page. The beginning of usable memory is at the PFN start.

void reserve_bootmem(unsigned long addr, unsigned long size)
Mark the pages between the address addr and addr+size reserved. Requests to partially reserve a page will result in the full page being reserved.

void free_bootmem(unsigned long addr, unsigned long size)
Mark the pages between the address addr and addr+size free.

void *alloc_bootmem(unsigned long size)
Allocate size number of bytes from ZONE_NORMAL. The allocation will be aligned to the L1 hardware cache to get the maximum benefit from the hardware cache.

void *alloc_bootmem_low(unsigned long size)
Allocate size number of bytes from ZONE_DMA. The allocation will be aligned to the L1 hardware cache.

void *alloc_bootmem_pages(unsigned long size)
Allocate size number of bytes from ZONE_NORMAL aligned on a page size so that full pages will be returned to the caller.

void *alloc_bootmem_low_pages(unsigned long size)
Allocate size number of bytes from ZONE_NORMAL aligned on a page size so that full pages will be returned to the caller.

unsigned long bootmem_bootmap_pages(unsigned long pages)
Calculate the number of pages required to store a bitmap representing the allocation state of pages number of pages.

unsigned long free_all_bootmem()
Used at the boot allocator end of life. It cycles through all pages in the bitmap. For each one that is free, the flags are cleared and the page is freed to the physical page allocator (See next chapter) so the runtime allocator can set up its free lists.
```

##### 6.2.9.3.2 Boot Memory Allocator API for NUMA Architectures

```
unsigned long init_bootmem_node(pg_data_t *pgdat, unsigned long freepfn, unsigned long startpfn, unsigned long endpfn)
For use with NUMA architectures. It initialise the memory between PFNs startpfn and endpfn with the first usable PFN at freepfn. Once initialised, the pgdat node is inserted into the pgdat_list.

void reserve_bootmem_node(pg_data_t *pgdat, unsigned long physaddr, unsigned long size)
Mark the pages between the address addr and addr+size on the specified node pgdat reserved. Requests to partially reserve a page will result in the full page being reserved.

void free_bootmem_node(pg_data_t *pgdat, unsigned long physaddr, unsigned long size)
Mark the pages between the address addr and addr+size on the specified node pgdat free.

void *alloc_bootmem_node(pg_data_t *pgdat, unsigned long size)
Allocate size number of bytes from ZONE_NORMAL on the specified node pgdat. The allocation will be aligned to the L1 hardware cache to get the maximum benefit from the hardware cache.

void *alloc_bootmem_pages_node(pg_data_t *pgdat, unsigned long size)
Allocate size number of bytes from ZONE_NORMAL on the specified node pgdat aligned on a page size so that full pages will be returned to the caller.

void *alloc_bootmem_low_pages_node(pg_data_t *pgdat, unsigned long size)
Allocate size number of bytes from ZONE_NORMAL on the specified node pgdat aligned on a page size so that full pages will be returned to the caller.

unsigned long free_all_bootmem_node(pg_data_t *pgdat)
Used at the boot allocator end of life. It cycles through all pages in the bitmap for the specified node. For each one that is free, the page flags are cleared and the page is freed to the physical page allocator (See next chapter) so the runtime allocator can set up its free lists.
```

### 6.2.10 struct vm_struct

该结构定义于include/linux/vmalloc.h:

```
struct vm_struct {
	/*
	 * vm_struct list ordered by address and the
	 * list is protected by the vmlist_lock lock
	 */
	struct vm_struct	*next;
	// The starting address of the memory block.
	void			*addr;
	// the size in bytes
	unsigned long		size;
	/*
	 * Set either to VM_ALLOC, in the case of use
	 * with vmalloc() or VM_IOREMAP when ioremap is
	 * used to map high memory into the kernel virtual
	 * address space.
	 */
	unsigned long		flags;
	struct page		**pages;
	unsigned int		nr_pages;
	phys_addr_t		phys_addr;
	void			*caller;
};
```

该结构参见错误：引用源未找到.

## 6.3 内存管理的初始化

内存管理的初始化分为如下步骤：
* 检测内存段及其大小，参见检测内存段及其大小/boot_params.e820_map节；
* 映射内存页面映射至分区，参见映射内存页面页至分区节。

内存管理的初始化参见mm_init()节。

### 6.3.1 检测内存段及其大小/boot_params.e820_map

系统启动时，将调用arch/x86/boot/main.c中的main()，参见arch/x86/boot/main.c节，其调用关系如下：

```
main()					// arch/x86/boot/main.c
-> detect_memory()
   -> detect_memory_e820()		// Fill boot_params.e820_map by calling BIOS interrupt
```

函数detect_memory_e820()通过调用BIOS中断来检测当前系统中的内存段及其大小，并将结果保存到boot_params.e820_map中，其结构如下图所示。每个连续的内存空间构成boot_params.e820_map[]中的一个元素，其首地址为addr，大小为size，类型为type。

boot_params.e820_map:

![Memery_Layout_08](/assets/Memery_Layout_08.jpg)

### 6.3.2 映射内存页面页至分区/node_data[]->node_zones[]

由检测内存段及其大小/boot_params.e820_map节可知，系统中的内存状态信息保存到数组boot_params.e820_map[]中。此后，在系统启动过程中，该数组将进行如下转换：

```
boot_params.e820_map[]
-> e820 / e820_saved					// 参见boot_params.e820_map[]=>e820节
   -> memblock.memory					// 参见e820=>memblock.memory节
      -> early_node_map[]				// 参见memblock.memory=>early_node_map[]节
         -> node_data[]->node_zones[]			// 参见early_node_map[]=>node_data[]节
```

#### 6.3.2.1 boot_params.e820_map[]=>e820 / e820_saved

内存状态信息从boot_params.e820_map[]到e820 / e820_saved的转换是在如下函数调用中发生的：

```
start_kernel()
-> setup_arch(&command_line)
   -> setup_memory_map()
      -> x86_init.resources.memory_setup()		// Call e820.c: default_machine_specific_memory_setup()
         -> sanitize_e820_map()				// Remove overlaps from boot_params.e820_map
         -> append_e820_map()
            -> __append_e820_map()			// boot_params.e820_map => e820
               -> e820_add_region()
                  -> __e820_add_region(&e820)
      -> memcpy(&e820_saved, &e820, ...)		// e820 => e820_saved
      -> printk(KERN_INFO "BIOS-provided physical RAM map:\n");
      -> e820_print_map()				// 打印e820，示例参见NOTE 1
   -> e820_reserve_setup_data()				// Set reserved setup data in e820
      -> e820_update_range()				// e820 => boot_params.hdr.setup_data, 示例参见NOTE 2
      -> sanitize_e820_map(e820.map, ...)		// Remove overlaps from e820
      -> memcpy(&e820_saved, &e820, ...)		// e820 => e820_saved
      -> printk(KERN_INFO "extended physical RAM map:\n");
      -> e820_print_map()				// Not comes here!
   -> finish_e820_parsing()				// Printing memory info of e820 if userdef is True
```

![Memery_Layout_08.jpg](/assets/Memery_Layout_08.jpg)

**NOTE 1**:

```
e820: BIOS-provided physical RAM map:
BIOS-e820: [mem 0x0000000000000000-0x000000000009fbff] usable
BIOS-e820: [mem 0x000000000009fc00-0x000000000009ffff] reserved
BIOS-e820: [mem 0x00000000000f0000-0x00000000000fffff] reserved
BIOS-e820: [mem 0x0000000000100000-0x000000001ffeffff] usable
BIOS-e820: [mem 0x000000001fff0000-0x000000001fffffff] ACPI data
BIOS-e820: [mem 0x00000000fffc0000-0x00000000ffffffff] reserved
```

**NOTE 2**:

```
e820: update [mem 0x00000000-0x0000ffff] usable ==> reserved
e820: remove [mem 0x000a0000-0x000fffff] usable
```

#### 6.3.2.2 e820=>memblock.memory

内存状态信息从e820到memblock.memory的转换是在如下函数调用中发生的：

```
start_kernel()
-> setup_arch(&command_line)
   -> Functions in section boot_params.e820_map[]=>e820 / e820_saved
   -> max_pfn = e820_end_of_ram_pfn()						// max_pfn = last_pfn
      -> e820_end_pfn(MAX_ARCH_PFN, E820_RAM)					// 查找e820.map[]中类型为E820_RAM的最大页框号
      -> printk(KERN_INFO "last_pfn = %#lx					// 示例参见NOTE 3
                max_arch_pfn = %#lx\n", last_pfn, max_arch_pfn);
   -> find_low_pfn_range()							// 为max_low_pfn赋值
      -> if (max_pfn <= MAXMEM_PFN)
            lowmem_pfn_init()
            -> max_low_pfn = max_pfn;
         else
            highmem_pfn_init()
            -> max_low_pfn = MAXMEM_PFN;
   -> printk(KERN_DEBUG "initial memory mapped : 0 - %08lx\n", max_pfn_mapped<<PAGE_SHIFT);
   -> setup_trampolines()							// 示例参见NOTE 4
   -> max_low_pfn_mapped = init_memory_mapping(0, max_low_pfn<<PAGE_SHIFT);	// 示例参见NOTE 4
      -> find_early_table_space(...)						// 示例参见NOTE 4
   -> max_pfn_mapped = max_low_pfn_mapped;
   -> memblock_x86_fill()							// e820 => memblock.memory
      -> memblock_add()
         -> memblock_add_region(&memblock.memory, ...)
      -> memblock_analyze()							// Update memblock.memory_size
```

memblock.memory的结构:

![Memery_Layout_09](/assets/Memery_Layout_09.jpg)

**NOTE 3**:

```
e820: last_pfn = 0x1fff0 max_arch_pfn = 0x1000000
=> last_pfn表示e820.map[]中类型为E820_RAM的最大页框号
=> max_arch_pfn为最大页框号，与地址空间有关(注意：此时PAE开启)，其取值参见arch/x86/kernel/e820.c:
#ifdef CONFIG_X86_32
# ifdef CONFIG_X86_PAE
#  define MAX_ARCH_PFN	(1ULL<<(36-PAGE_SHIFT))		// 0x0100,0000
# else
#  define MAX_ARCH_PFN	(1ULL<<(32-PAGE_SHIFT))		// 0x0010,0000
# endif
#else /* CONFIG_X86_32 */
# define MAX_ARCH_PFN		MAXMEM>>PAGE_SHIFT
#endif
```

**NOTE 4**:

```
initial memory mapped: [mem 0x00000000-0x01ffffff]
Base memory trampoline at [c009b000] 9b000 size 16384
init_memory_mapping: [mem 0x00000000-0x1ffeffff]
[mem 0x00000000-0x001fffff] page 4k				// 2MB空间，每页面占4KB，共计512个页面
[mem 0x00200000-0x1fdfffff] page 2M				// 508MB空间，每页面占2MB，共计254个页面
[mem 0x1fe00000-0x1ffeffff] page 4k				// ~2MB空间，每页面占4KB，共计496个页面
kernel direct mapping tables up to 0x1ffeffff @ [mem 0x01ffa000-0x01ffffff]
=> 由此可知，当前映射的内存空间约为512MB，其对应的页面描述符占用0x01ffa000-0x01ffffff的内存空间
```

#### 6.3.2.3 memblock.memory=>early_node_map[]

内存状态信息从memblock.memory到early_node_map[]的转换是在如下函数调用中发生的：

```
start_kernel()
-> setup_arch(&command_line)
   -> Functions in section e820=>memblock.memory
   -> initmem_init()							// arch/x86/mm/init_32.c
      -> memblock_x86_register_active_regions()
         // Get active region (Physical Frame Number, pfn)
         -> memblock_x86_find_active_region()
         -> add_active_range()						// memblock.memory => early_node_map[], mm/page_alloc.c
      -> printk(KERN_NOTICE "%ldMB HIGHMEM available.\n",		// 示例参见NOTE 5
                pages_to_mb(highend_pfn - highstart_pfn));
      -> printk(KERN_NOTICE "%ldMB LOWMEM available.\n",		// 示例参见NOTE 6
                pages_to_mb(max_low_pfn));
      -> setup_bootmem_allocator()					// 示例参见NOTE 7
         // 安装bootmem分配器，此分配器在伙伴系统起来之前用来承担内存的分配等任务
         -> after_bootmem = 1;
```

数组early_node_map[]的结构，参见Subjects/Chapter06_Memory_Management/Figures/Memery_Layout_09.jpg，其中
start_pfn和end_pfn域表示Physical Frame Number，取值为内存地址的高20 bits (12-31 bit)。因为内存页大小为4KB，内存页是4KB对齐的，故内存页地址的低12 bits取值为0。因此只需要内存地址的高20 bits就可以表示内存也的地址了。

**NOTE 5**:

```
0MB HIGHMEM available.
```

**NOTE 6**:

```
511MB LOWMEM available.
```

**NOTE 7**:

```
mapped low ram: 0 - 1fff0000
low ram: 0 – 1fff0000
```

#### 6.3.2.4 early_node_map[]=>node_data[]->node_zones[]

内存状态信息从early_node_map[]到node_data[]->node_zones[]的转换是在如下函数调用中发生的：

```
start_kernel()
-> setup_arch(&command_line)
   -> Functions in section memblock.memory=>early_node_map[]
   -> x86_init.paging.pagetable_setup_start(swapper_pg_dir) 	// native_pagetable_setup_start()
   -> paging_init()
      -> pagetable_init()
         // Initialise the page tables necessary to reference all physical memory in
         // ZONE_DMA and ZONE_NORMAL. High memory in ZONE_HIGHMEM cannot be directly
         // referenced and mappings are set up for it.
         -> permanent_kmaps_init(swapper_pg_dir)		// 参见pkmap_page_table的初始化节
      -> __flush_tlb_all()					// Refresh CR3 register
      -> kmap_init()						// 参见emporary Kernel Mapping节
      -> sparse_init()						// mm/sparse.c
      -> zone_sizes_init()
         -> free_area_init_nodes()				// early_node_map[] => node_data[]
            -> sort_node_map()					// Sort early_node_map[] by ->start_pfn
            -> printk("Zone PFN ranges:\n");			// 示例参见NOTE 8
               ...
            -> for_each_online_node(nid) {			//  Set node_data[nid], see 错误：引用源未找到
               -> free_area_init_node(nid, NULL, find_min_pfn_for_node(nid), NULL)
                  // find_min_pfn_for_node(nid)从early_node_map[i].start_pfn中查找最小值
                  -> calculate_node_totalpages()
                     -> pgdat->node_spanned_pages = totalpages;
                        // Fill node_data[]->node_spanned_pages
                     -> pgdat->node_present_pages = realtotalpages;
                        // Fill node_data[]->node_present_pages
                     -> printk(KERN_DEBUG "On node %d totalpages: %lu\n",
                               pgdat->node_id, realtotalpages);
                        // 示例参见NOTE 9
                  -> alloc_node_mem_map(pgdat)
                     // Set mem_map and pgdat->node_mem_map，参见mem_map节，示例参见NOTE 10
                  -> printk(KERN_DEBUG "free_area_init_node: node %d, pgdat %08lx,
                            node_mem_map %08lx\n", nid, (unsigned long)pgdat,
                            (unsigned long)pgdat->node_mem_map);
                     // 示例参见NOTE 10
                     // Set node_data[nid]->node_zones[j]
                  -> free_area_init_core()
                     -> for (j = 0; j < MAX_NR_ZONES; j++) {
                        -> printk(KERN_DEBUG ...)		// 示例参见NOTE 11
                        -> zone_pcp_init()			// 示例参见NOTE 11
                           -> printk(KERN_DEBUG "  %s zone: %lu pages, LIFO batch:%u\n",
                                     zone->name, zone→present_pages, zone_batchsize(zone));
                        -> init_currently_empty_zone()
                           // 初始化node_data[nid]->node_zones[j]->free_area[*], 此时页面不可用
                           -> zone_init_free_lists()
                        -> memmap_init()
                           -> memmap_init_zone()		// mm/page_alloc.c
                              -> for (pfn = start_pfn; pfn < end_pfn; pfn++) {
                                    // Set each page in the range. Get Page Descriptor:
                                    // page = mem_map + pfn;
                                 -> page = pfn_to_page(pfn)
                                    // 设置page->flags中有关zone、node和section的标志位
                                 -> set_page_links(page, ...)
                                    // No user: page->_count = 1
                                 -> init_page_count(page)
                                    // 清除Buddy标志: page->_mapcount=-1
                                 -> reset_page_mapcount(page)
                                    // 置位page->flags中的标志位PG_reserved
                                 -> SetPageReserved(page)
                                 -> set_pageblock_migratetype(page, MIGRATE_MOVABLE)
                                    -> set_pageblock_flags_group()
                                    // 初始化page->lru
                                 -> INIT_LIST_HEAD(&page->lru)
                                    // Set page->virtual
                                 -> set_page_address()
                                 }
                        }
               -> node_set_state(nid, N_HIGH_MEMORY)
               -> check_for_regular_memory(pgdat)
               }
   // native_pagetable_setup_done()
   -> x86_init.paging.pagetable_setup_done(swapper_pg_dir)
-> build_all_zonelists()					// 示例参见NOTE 12
-> mm_init()							// 参见mm_init()节
   -> mem_init()						// 参见mem_init()节，示例参见NOTE 13
      /*
       * 将低端内存转入Buddy Allocator System中管理，
       * 参见free_all_bootmem()/free_all_bootmem_core()节
       */
      -> free_all_bootmem()
         // 参见free_all_bootmem()/free_all_bootmem_core()节
         -> free_all_bootmem_core()
            -> __free_pages_bootmem()
               -> __free_page()					// 参见__free_page()/free_page()节
      // 将高端内存转入Buddy Allocator System中管理，参见set_highmem_pages_init()节
      -> set_highmem_pages_init()
         -> add_highpages_with_active_regions()
            -> __get_free_all_memory_range()
            -> add_one_highpage_init()
               -> __free_page()					// 参见__free_page()/free_page()节
-> rest_init()
   -> kernel_thread(kernel_init, NULL, CLONE_FS | CLONE_SIGHAND);
      -> kernel_init()
         -> init_post()
            -> free_initmem()
               /* All initilisation function that are required only during system
                * start-up are marked __init and put in region __init_begin to
                * __init_end. The function free_initmem() frees all pages from
                * __init_begin to __init_end to the Buddy Allocator System.
                * The region __init_begin to __init_end is defined in vmlinux.lds.
                * 示例参见NOTE 14
                */
               -> printk(KERN_INFO "Freeing %s: %luk freed\n", ...);
```

**NOTE 8**:

```
Zone ranges:
  DMA		[mem 0x00010000-0x00ffffff]	  // 16320 KB, 4080 pages
  Normal   [mem 0x01000000-0x1ffeffff]	  	// 507840 KB, 126960 pages
  HighMem  empty
Movable zone start for each node		  // Print PFNs ZONE_MOVABLE begins at in each node
Early memory node ranges			  // Print early_node_map[], include DMA and Normal.
  node   0: [mem 0x00010000-0x0009efff] 	// early_node_map[0].start_pfn - early_node_map[0].end_pfn
  node   0: [mem 0x00100000-0x1ffeffff] 	// early_node_map[1].start_pfn - early_node_map[1].end_pfn
```

**NOTE 9**;

```
On node 0 totalpages: 130943
=> ((0x0009efff - 0x00010000 + 1) + (0x1ffeffff - 0x00100000 + 1)) / (4 * 1024) = 130943 pages
=> Total memory: 511 MB, include DMA and Normal.
```

**NOTE 10**:

```
free_area_init_node: node 0, pgdat c18a0840, node_mem_map dfbef200
```

**NOTE 11**:

```
  DMA zone: 32 pages used for memmap
  DMA zone: 0 pages reserved
  DMA zone: 3951 pages, LIFO batch:0
  Normal zone: 992 pages used for memmap
  Normal zone: 125968 pages, LIFO batch:31
=> 32 + 3951 + 992 + 125968 = 130943 pages
```

**NOTE 12**:

```
Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 129919
```

**NOTE 13**:

```
Initializing HighMem for node 0 (00000000:00000000)
Memory: 492840k/524224k available (5956k kernel code, 30932k reserved, 2928k data, 756k init, 0k highmem)
virtual kernel memory layout:
    fixmap  : 0xfff15000 - 0xfffff000   ( 936 kB)
    pkmap   : 0xffc00000 - 0xffe00000   (2048 kB)
    vmalloc : 0xe07f0000 - 0xffbfe000   ( 500 MB)
    lowmem  : 0xc0000000 - 0xdfff0000   ( 511 MB)		// [__va(0), high_memory]
      .init : 0xc18ae000 - 0xc196b000   ( 756 kB)		// [__init_begin, __init_end]
      .data : 0xc15d1358 - 0xc18ad6c0   (2928 kB)		// [_etext, _edata]
      .text : 0xc1000000 - 0xc15d1358   (5956 kB)		// [_text, _etext]
=> 各变量定义于vmlinux.lds
=> Virtual Kernel Memory Layout参见错误：引用源未找到和Physical Memory Layout节。
```

**NOTE 14**:

Freeing unused kernel memory: 756k freed

Memory layout on 32-bit kernel:

![Memery_Layout_27](/assets/Memery_Layout_27.jpg)

Memory layout on 64-bit kernel:

![Memery_Layout_28](/assets/Memery_Layout_28.jpg)

Virtual kernel memory layout on 32-bit kernel:

![Memery_Layout_01](/assets/Memery_Layout_01.jpg)

各段内存的用途如下：

**[PAGE_OFFSET, VMALLOC_START - VMALLOC_OFFSET]**

The region is the physical memory map and the size of the region depends on the amount of available RAM. Between the physical memory map and the vmalloc address space, there is a gap of space VMALLOC_OFFSET in size, which on the x86 is 8MB, to guard against out of bounds errors.

**[VMALLOC_START, VMALLOC_END]**

In low memory systems, the remaining amount of the virtual address space, minus a 2 page gap, is used by vmalloc() for representing non-contiguous memory allocations in a contiguous virtual address space. In high-memory systems, the vmalloc area extends as far as PKMAP_BASE minus the two page gap and two extra regions are introduced.

**[PKMAP_BASE, PKMAP_BASE + LAST_PKMAP * PAGE_SIZE]**

This is an area reserved for the mapping of high memory pages into low memory with kmap(), see section kmap(). Refer to arch/x86/include/asm/pgtable_32_types.h:

```
#ifdef CONFIG_X86_PAE
#define LAST_PKMAP	512			// PKMAP区占2MB空间
#else
#define LAST_PKMAP	1024			// PKMAP区占4MB空间
#endif
```

**[FIXADDR_START, FIXADDR_TOP]**

The regain is for fixed virtual address mappings. Fixed virtual addresses are needed for subsystems that need to know the virtual address at compile time such as the Advanced Programmable Interrupt Controller (APIC). FIXADDR_TOP is statically defined to be 0xFFFFE000 on the x86 which is one page before the end of the virtual address space. The size of the fixed mapping region is calculated at compile time in \_\_FIXADDR_SIZE and used to index back from FIXADDR_TOP to give the start of the region FIXADDR_START. See section kmap_atomic().

可通过下列命令查看当前系统的内存布局，其含义参见Documentation/filesystems/proc.txt:

```
chenwx proc # cat /proc/iomem
00000000-00000fff : reserved
00001000-0009fbff : System RAM
0009fc00-0009ffff : reserved
000a0000-000bffff : Video RAM area
000c0000-000c7fff : Video ROM
000e2000-000eebff : Adapter ROM
000f0000-000fffff : reserved
  000f0000-000fffff : System ROM
00100000-5ffeffff : System RAM
  01000000-01831996 : Kernel code
  01831997-01c1c9bf : Kernel data
  01d12000-01dfbfff : Kernel bss
5fff0000-5fffffff : ACPI Tables
e0000000-e3ffffff : 0000:00:02.0
f0000000-f001ffff : 0000:00:03.0
  f0000000-f001ffff : e1000
f0400000-f07fffff : 0000:00:04.0
  f0400000-f07fffff : vboxguest
f0800000-f0803fff : 0000:00:04.0
f0804000-f0804fff : 0000:00:06.0
  f0804000-f0804fff : ohci_hcd
f0806000-f0807fff : 0000:00:0d.0
  f0806000-f0807fff : ahci
fee00000-fee00fff : Local APIC
fffc0000-ffffffff : reserved
```

可通过如何命令查看系统当前的内存信息，其含义参见Documentation/filesystems/proc.txt:

```
chenwx proc # cat /proc/buddyinfo
Node 0, zone     DMA       9      5      2      1      8      4      3      2      0      2      0
Node 0, zone   Normal     98    106     84     63     56     42     12      5      2      4     44
Node 0, zone  HighMem    280    233    119    122     73     33      6      8      3      1     43

chenwx proc # cat /proc/pagetypeinfo
Page block order: 9
Pages per block:  512

Free pages count per migrate type at order       0      1      2      3      4      5      6      7      8      9     10
Node    0, zone      DMA, type    Unmovable      4      2      1      1      1      1      1      1      0      0      0
Node    0, zone      DMA, type  Reclaimable      0      1      0      0      0      1      1      1      0      1      0
Node    0, zone      DMA, type      Movable      3      0      0      0      6      2      1      0      0      0      0
Node    0, zone      DMA, type      Reserve      0      0      0      0      0      0      0      0      0      1      0
Node    0, zone      DMA, type          CMA      0      0      0      0      0      0      0      0      0      0      0
Node    0, zone      DMA, type      Isolate      0      0      0      0      0      0      0      0      0      0      0
Node    0, zone   Normal, type    Unmovable      1      1      0      3      0      0      0      0      0      2      0
Node    0, zone   Normal, type  Reclaimable      8     12      4      2      0      1      1      0      0      1      0
Node    0, zone   Normal, type      Movable      0    142     65     33     30     39     10      4      1      2     43
Node    0, zone   Normal, type      Reserve      0      0      0      0      0      0      0      0      0      0      1
Node    0, zone   Normal, type          CMA      0      0      0      0      0      0      0      0      0      0      0
Node    0, zone   Normal, type      Isolate      0      0      0      0      0      0      0      0      0      0      0
Node    0, zone  HighMem, type    Unmovable      1      0      0      4      8     11      4      5      3      0      1
Node    0, zone  HighMem, type  Reclaimable      0      0      0      0      0      0      0      0      0      0      0
Node    0, zone  HighMem, type      Movable    115     75     73     81     63     22      2      3      0      1     41
Node    0, zone  HighMem, type      Reserve      0      0      0      0      0      0      0      0      0      0      1
Node    0, zone  HighMem, type          CMA      0      0      0      0      0      0      0      0      0      0      0
Node    0, zone  HighMem, type      Isolate      0      0      0      0      0      0      0      0      0      0      0

Number of blocks type     Unmovable  Reclaimable      Movable      Reserve          CMA      Isolate
Node 0, zone      DMA            1            2            4            1            0            0
Node 0, zone   Normal           24           46          366            2            0            0
Node 0, zone  HighMem            9            0          312            1            0            0
```

### 6.3.3 Physical Memory Layout

参见<<Understanding the Linux Kernel, 3rd Edition>>第2. Memory Addressing章第Physical Memory Layout节:

The kernel considers the following page frames asreserved:
* Those falling in the unavailable physical address ranges.
* Those containing the kernel’s code and initialized data structures.
A page contained in a reserved page frame can never be dynamically assigned or swapped to disk.

As a general rule, the Linux kernel is installed in RAM starting from the physical address 0x00100000 — i.e., from the second megabyte.

Variables describing the kernel’s physical memory layout

| Variable Name | Description |
| :------------ | :---------- |
| num_physpages | Page frame number of the highest usable page frame |
| totalram_pages | Total number of usable page frames |
| min_low_pfn | Page frame number of the first usable page frame after the kernel image in RAM |
| max_pfn | Page frame number of the last usable page frame |
| max_low_pfn | Page frame number of the last page frame directly mapped by the kernel (low memory) |
| totalhigh_pages | Total number of page frames not directly mapped by the kernel (high memory) |
| highstart_pfn | Page frame number of the first page frame not directly mapped by the kernel |
| highend_pfn | Page frame number of the last page frame not directly mapped by the kernel |

<p/>

The symbol ```_text```, which corresponds to physical address 0x00100000, denotes the address of the first byte of kernel code. The end of the kernel code is similarly identified by the symbol ```_etext```. Kernel data is divided into two groups: initialized and uninitialized. The initialized data starts right after ```_etext``` and ends at ```_edata```. The uninitialized data follows and ends up at ```_end```. 这些变量的定义参见内核编译时生成的vmlinux.lds.

#### 6.3.3.1 Process Page Tables

The linear address space of a process is divided into two parts:

1) Linear addresses from 0x00000000 to 0xBFFFFFFF can be addressed when the process runs in either User or Kernel Mode.

2) Linear addresses from 0xC0000000 to 0xFFFFFFFF can be addressed only when the process runs in Kernel Mode.

When a process runs in User Mode, it issues linear addresses smaller than 0xC0000000; when it runs in Kernel Mode, it is executing kernel code and the linear addresses issued are greater than or equal to 0xC0000000. In some cases, however, the kernel must access the User Mode linear address space to retrieve or store data.

#### 6.3.3.2 Kernel Page Tables

## 6.4 分配/释放内存页

The buddy allocator system algorithm adopts the page frame as the basic memory area.

### 6.4.1 分配/释放多个内存页

#### 6.4.1.1 alloc_pages()/alloc_pages_node()

The function allocates 2order (that is, 1 << order) contiguous physical pages and returns a pointer to the first page’s page structure; on error it returns NULL.

该函数定义于include/linux/gfp.h:

```
/*
 * IBM-compatible PCs use the Uniform Memory Access model (UMA),
 * thus the NUMA support is not really required.
 */
#ifdef CONFIG_NUMA
extern struct page *alloc_pages_current(gfp_t gfp_mask, unsigned order);	// 定义于mm/mempolicy.c

static inline struct page *alloc_pages(gfp_t gfp_mask, unsigned int order)
{
	return alloc_pages_current(gfp_mask, order);
}
#else
// gfp_mask参见gfp_t节
#define alloc_pages(gfp_mask, order)		alloc_pages_node(numa_node_id(), gfp_mask, order)
#endif
```

函数alloc_pages_node()定义于include/linux/gfp.h:

```
static inline struct page *alloc_pages_node(int nid, gfp_t gfp_mask, unsigned int order)
{
	/* Unknown node is current node */
	if (nid < 0)
		nid = numa_node_id();

	// node_zonelist()返回node_data[]->node_zonelists[]，参见错误：引用源未找到
	return __alloc_pages(gfp_mask, order, node_zonelist(nid, gfp_mask));
}
```

其中，函数__alloc_pages()定义于include/linux/gfp.h:

```
static inline struct page *__alloc_pages(gfp_t gfp_mask, unsigned int order, struct zonelist *zonelist)
{
	return __alloc_pages_nodemask(gfp_mask, order, zonelist, NULL);
}
```

其中，函数__alloc_pages_nodemask()定义于mm/page_alloc.c:

```
/*
 * This is the 'heart' of the zoned buddy allocator.
 */
struct page *__alloc_pages_nodemask(gfp_t gfp_mask, unsigned int order,
				   struct zonelist *zonelist, nodemask_t *nodemask)
{
	enum zone_type high_zoneidx = gfp_zone(gfp_mask);
	struct zone *preferred_zone;
	struct page *page;
	int migratetype = allocflags_to_migratetype(gfp_mask);

	gfp_mask &= gfp_allowed_mask;

	lockdep_trace_alloc(gfp_mask);

	// If __GFP_WAIT is set, then here can wait and reschedule.
	might_sleep_if(gfp_mask & __GFP_WAIT);

	// 通过fail_page_alloc和标志位快速判断是否会分配失败
	if (should_fail_alloc_page(gfp_mask, order))
		return NULL;

	/*
	 * Check the zones suitable for the gfp_mask contain at least one
	 * valid zone. It's possible to have an empty zonelist as a result
	 * of GFP_THISNODE and a memoryless node
	 */
	if (unlikely(!zonelist->_zonerefs->zone))
		return NULL;

	get_mems_allowed();
	/* The preferred zone is used for statistics later */ // 参见first_zones_zonelist()节
	first_zones_zonelist(zonelist, high_zoneidx,
					nodemask ? : &cpuset_current_mems_allowed, &preferred_zone);
	if (!preferred_zone) {
		put_mems_allowed();
		return NULL;
	}

	/* First allocation attempt */	// 参见get_page_from_freelist()节
	page = get_page_from_freelist(gfp_mask|__GFP_HARDWALL, nodemask, order, zonelist,
			high_zoneidx, ALLOC_WMARK_LOW|ALLOC_CPUSET, preferred_zone, migratetype);
	if (unlikely(!page))		// 参见__alloc_pages_slowpath()节
		page = __alloc_pages_slowpath(gfp_mask, order, zonelist,
				high_zoneidx, nodemask, preferred_zone, migratetype);
	put_mems_allowed();

	trace_mm_page_alloc(page, order, gfp_mask, migratetype);
	return page;
}
```

##### 6.4.1.1.1 first_zones_zonelist()

该函数定义于include/linux/mmzone.h:

```
/**
 * first_zones_zonelist - Returns the first zone at or below highest_zoneidx
 *                        within the allowed nodemask in a zonelist
 * @zonelist - The zonelist to search for a suitable zone
 * @highest_zoneidx - The zone index of the highest zone to return
 * @nodes - An optional nodemask to filter the zonelist with
 * @zone - The first suitable zone found is returned via this parameter
 *
 * This function returns the first zone at or below a given zone index that is
 * within the allowed nodemask. The zoneref returned is a cursor that can be
 * used to iterate the zonelist with next_zones_zonelist by advancing it by
 * one before calling.
 */
static inline struct zoneref *first_zones_zonelist(struct zonelist *zonelist,
		enum zone_type highest_zoneidx, nodemask_t *nodes, struct zone **zone)
{
	return next_zones_zonelist(zonelist->_zonerefs, highest_zoneidx, nodes, zone);
}
```

其中，函数next_zones_zonelist()定义于mm/mmzone.c:

```
/* Returns the next zone at or below highest_zoneidx in a zonelist */
struct zoneref *next_zones_zonelist(struct zoneref *z, enum zone_type highest_zoneidx,
							nodemask_t *nodes, struct zone **zone)
{
	/*
	 * Find the next suitable zone to use for the allocation.
	 * Only filter based on nodemask if it's set
	 */
	if (likely(nodes == NULL))
		while (zonelist_zone_idx(z) > highest_zoneidx)		// z->zone_idx > highest_zoneidx
			z++;
	else
		while (zonelist_zone_idx(z) > highest_zoneidx ||	// z->zone_idx > highest_zoneidx
			(z->zone && !zref_in_nodemask(z, nodes)))
			z++;

	*zone = zonelist_zone(z);					// *zone = z->zone
	return z;
}
```

##### 6.4.1.1.2 get_page_from_freelist()

该函数定义于mm/page_alloc.c:

```
/*
 * get_page_from_freelist goes through the zonelist trying to allocate
 * a page.
 */
static struct page *get_page_from_freelist(gfp_t gfp_mask, nodemask_t *nodemask,
					unsigned int order, struct zonelist *zonelist, int high_zoneidx,
					int alloc_flags, struct zone *preferred_zone, int migratetype)
{
	struct zoneref *z;
	struct page *page = NULL;
	int classzone_idx;
	struct zone *zone;
	nodemask_t *allowednodes = NULL;	/* zonelist_cache approximation */
	int zlc_active = 0;			/* set if using zonelist_cache */
	int did_zlc_setup = 0;			/* just call zlc_setup() one time */

	classzone_idx = zone_idx(preferred_zone);
zonelist_scan:
	/*
	 * Scan zonelist, looking for a zone with enough free.
	 * See also cpuset_zone_allowed() comment in kernel/cpuset.c.
	 */
	for_each_zone_zonelist_nodemask(zone, z, zonelist, high_zoneidx, nodemask) {
		if (NUMA_BUILD && zlc_active && !zlc_zone_worth_trying(zonelist, z, allowednodes))
			continue;
		if ((alloc_flags & ALLOC_CPUSET) && !cpuset_zone_allowed_softwall(zone, gfp_mask))
			continue;

		BUILD_BUG_ON(ALLOC_NO_WATERMARKS < NR_WMARK);
		if (!(alloc_flags & ALLOC_NO_WATERMARKS)) {
			unsigned long mark;
			int ret;

			mark = zone->watermark[alloc_flags & ALLOC_WMARK_MASK];
			if (zone_watermark_ok(zone, order, mark, classzone_idx, alloc_flags))
				goto try_this_zone;

			if (NUMA_BUILD && !did_zlc_setup && nr_online_nodes > 1) {
				/*
				 * we do zlc_setup if there are multiple nodes
				 * and before considering the first zone allowed
				 * by the cpuset.
				 */
				allowednodes = zlc_setup(zonelist, alloc_flags);
				zlc_active = 1;
				did_zlc_setup = 1;
			}

			if (zone_reclaim_mode == 0)
				goto this_zone_full;

			/*
			 * As we may have just activated ZLC, check if the first
			 * eligible zone has failed zone_reclaim recently.
			 */
			if (NUMA_BUILD && zlc_active && !zlc_zone_worth_trying(zonelist, z, allowednodes))
				continue;

			ret = zone_reclaim(zone, gfp_mask, order);
			switch (ret) {
			case ZONE_RECLAIM_NOSCAN:
				/* did not scan */
				continue;
			case ZONE_RECLAIM_FULL:
				/* scanned but unreclaimable */
				continue;
			default:
				/* did we reclaim enough */
				if (!zone_watermark_ok(zone, order, mark, classzone_idx, alloc_flags))
					goto this_zone_full;
			}
		}

try_this_zone:
		// 参见buffered_rmqueue()节
		page = buffered_rmqueue(preferred_zone, zone, order, gfp_mask, migratetype);
		if (page)
			break;
this_zone_full:
		if (NUMA_BUILD)
			zlc_mark_zone_full(zonelist, z);
	}

	if (unlikely(NUMA_BUILD && page == NULL && zlc_active)) {
		/* Disable zlc cache for second zonelist scan */
		zlc_active = 0;
		goto zonelist_scan;
	}
	return page;
}
```

###### 6.4.1.1.2.1 buffered_rmqueue()

Function buffered_rmqueue() returns the page descriptor of the first allocated page frame, or NULL if the memory zone does not include a group of contiguous page frames of the requested size.

该函数定义于mm/page_alloc.c:

```
/*
 * Really, prep_compound_page() should be called from __rmqueue_bulk().  But
 * we cheat by calling it from here, in the order > 0 path.  Saves a branch
 * or two.
 */
static inline struct page *buffered_rmqueue(struct zone *preferred_zone,
			struct zone *zone, int order, gfp_t gfp_flags, int migratetype)
{
	unsigned long flags;
	struct page *page;
	/*
	 * 冷页表示该空闲页已经不再高速缓存中了(一般是指L2 Cache)；热页表示该空闲页仍然在高速缓存中。
	 * 冷热页是针对于每CPU的，在每个zone中，都会针对所有的CPU初始化一个包含冷热页的per-cpu-pageset
	 */
	int cold = !!(gfp_flags & __GFP_COLD);

again:
	if (likely(order == 0)) {				// 分配单个页面(从缓存中分配)
		struct per_cpu_pages *pcp;
		struct list_head *list;

		local_irq_save(flags);
		// Per-CPU Page Frame Cache，参见错误：引用源未找到
		pcp = &this_cpu_ptr(zone->pageset)->pcp;
		list = &pcp->lists[migratetype];
		if (list_empty(list)) {
			// 若缓存为空，则分配pcp->batch的页来填充缓存。参见rmqueue_bulk()节
			pcp->count += rmqueue_bulk(zone, 0, pcp->batch, list, migratetype, cold);
			if (unlikely(list_empty(list)))
				goto failed;
		}

		/*
		 * 冷热页是保存在一条链表上的：热页通过list->next访问，冷页通过list->prev访问。
		 * 另参见free_hot_cold_page()节
		 */
		if (cold)
			page = list_entry(list->prev, struct page, lru);
		else
			page = list_entry(list->next, struct page, lru);

		list_del(&page->lru);
		pcp->count--;
	} else {						// 分配2order个连续页面(从Buddy Allocator System中分配)
		if (unlikely(gfp_flags & __GFP_NOFAIL)) {
			/*
			 * __GFP_NOFAIL is not to be used in new code.
			 *
			 * All __GFP_NOFAIL callers should be fixed so that they
			 * properly detect and handle allocation failures.
			 *
			 * We most definitely don't want callers attempting to
			 * allocate greater than order-1 page units with
			 * __GFP_NOFAIL.
			 */
			WARN_ON_ONCE(order > 1);
		}
		spin_lock_irqsave(&zone->lock, flags);
		page = __rmqueue(zone, order, migratetype);	// 参见__rmqueue()节
		spin_unlock(&zone->lock);
		if (!page)
			goto failed;
		// 更新zone->vm_stat[NR_FREE_PAGES]和vm_stat[NR_FREE_PAGES]
		__mod_zone_page_state(zone, NR_FREE_PAGES, -(1 << order));
	}

	__count_zone_vm_events(PGALLOC, zone, 1 << order);
	zone_statistics(preferred_zone, zone, gfp_flags);
	local_irq_restore(flags);

	VM_BUG_ON(bad_range(zone, page));
	if (prep_new_page(page, order, gfp_flags))		// 参见prep_new_page()节
		goto again;
	return page;

failed:
	local_irq_restore(flags);
	return NULL;
}
```

Per-CPU page frame cache:

![Memery_Layout_20](/assets/Memery_Layout_20.jpg)

###### 6.4.1.1.2.1.1 rmqueue_bulk()

该函数定义于mm/page_alloc.c:

```
/*
 * Obtain a specified number of elements from the buddy allocator, all under
 * a single hold of the lock, for efficiency.  Add them to the supplied list.
 * Returns the number of new pages which were placed at *list.
 */
// 由buffered_rmqueue()节可知，rmqueue_bulk(zone, 0, pcp->batch, list, migratetype, cold);
static int rmqueue_bulk(struct zone *zone, unsigned int order, unsigned long count,
				  struct list_head *list, int migratetype, int cold)
{
	int i;

	spin_lock(&zone->lock);
	for (i = 0; i < count; ++i) {
		struct page *page = __rmqueue(zone, order, migratetype);	// 参见__rmqueue()节
		if (unlikely(page == NULL))
			break;

		/*
		 * Split buddy pages returned by expand() are received here
		 * in physical page order. The page is added to the callers and
		 * list and the list head then moves forward. From the callers
		 * perspective, the linked list is ordered by page number in
		 * some conditions. This is useful for IO devices that can
		 * merge IO requests if the physical pages are ordered
		 * properly.
		 */
		if (likely(cold == 0))
			list_add(&page->lru, list);
		else
			list_add_tail(&page->lru, list);
		// page->private = migratetype
		set_page_private(page, migratetype);
		list = &page->lru;
	}
	__mod_zone_page_state(zone, NR_FREE_PAGES, -(i << order));
	spin_unlock(&zone->lock);
	return i;
}
```

###### 6.4.1.1.2.1.1.1 \__rmqueue()

该函数定义于mm/page_alloc.c:

```
/*
 * Do the hard work of removing an element from the buddy allocator.
 * Call me with the zone->lock already held.
 */
static struct page *__rmqueue(struct zone *zone, unsigned int order, int migratetype)
{
	struct page *page;

retry_reserve:
	page = __rmqueue_smallest(zone, order, migratetype);		// 参见__rmqueue_smallest()节

	if (unlikely(!page) && migratetype != MIGRATE_RESERVE) {
		page = __rmqueue_fallback(zone, order, migratetype);	// 参见__rmqueue_fallback()节

		/*
		 * Use MIGRATE_RESERVE rather than fail an allocation. goto
		 * is used because __rmqueue_smallest is an inline function
		 * and we want just one call site
		 */
		if (!page) {
			migratetype = MIGRATE_RESERVE;
			goto retry_reserve;
		}
	}

	trace_mm_page_alloc_zone_locked(page, order, migratetype);
	return page;
}
```

###### 6.4.1.1.2.1.1.1.1 \__rmqueue_smallest()

该函数定义于mm/page_alloc.c:

```
/*
 * Go through the free lists for the given migratetype and remove
 * the smallest available page from the freelists
 */
static inline struct page *__rmqueue_smallest(struct zone *zone, unsigned int order, int migratetype)
{
	unsigned int current_order;
	struct free_area * area;
	struct page *page;

	/*
	 * 与__rmqueue_fallback()不同(参见__rmqueue_fallback()节)：
	 * 此处按order由小到大的顺序分配，且只查找指定的migratetype类型
	 */
	/* Find a page of the appropriate size in the preferred list */
	for (current_order = order; current_order < MAX_ORDER; ++current_order) {
		area = &(zone->free_area[current_order]);
		// 若该大小为2order的free_area为空，则从2order+1的free_area里面找
		if (list_empty(&area->free_list[migratetype]))
			continue;

		// 获取第一个页面，参见错误：引用源未找到
		page = list_entry(area->free_list[migratetype].next, struct page, lru);
		// 将该页面及其后连续的共2order个页面从列表中移出
		list_del(&page->lru);
		// 1) 清除Buddy Allocator标志，即page->_mapcount = -1;
		// 2) 设置page->private = 0. 注：页描述符中的private保存其对应的order值.
		rmv_page_order(page);
		area->nr_free--;
		/*
		 * When it becomes necessary to use a block of 2k page frames to
		 * satisfy a request for 2h page frames (k > h), the program
		 * allocates the first 2h page frames and iteratively reassigns
		 * the last 2k–2h page frames to the free_area lists that have
		 * indexes between h and k.
		 * 此处，current_order >= order，示例参见错误：引用源未找到。
		 * 另参见struct zone节中free_area[]的注释
		 */
		expand(zone, page, order, current_order, area, migratetype);
		return page;
	}

	return NULL;
}
```

其中，函数expand()定义于mm/slab_alloc.c:

```
static inline void expand(struct zone *zone, struct page *page, int low,
							   int high, struct free_area *area, int migratetype)
{
	unsigned long size = 1 << high;

	while (high > low) {
		area--;
		high--;
		size >>= 1;
		VM_BUG_ON(bad_range(zone, &page[size]));
		// 将2high个页面添加到链表area->free_list[]的头部
		list_add(&page[size].lru, &area->free_list[migratetype]);
		area->nr_free++;
		/*
		 * 设置&page[size]->private = high. 注：页描述符中的private保存其对应的order值；
		 * 设置Buddy Allocator标志，即&page[size]->_mapcount = PAGE_BUDDY_MAPCOUNT_VALUE
		 */
		set_page_order(&page[size], high);
	}
}
```

当high=4,low=3时，函数expand()的执行结果:

![Memery_Layout_21](/assets/Memery_Layout_21.jpg)

从order=4的free_area中分配1个页面:

![Memery_Layout_29](/assets/Memery_Layout_29.jpg)

###### 6.4.1.1.2.1.1.1.2 \__rmqueue_fallback()

该函数定义于mm/page_alloc.c:

```
/*
 * This array describes the order lists are fallen back to when
 * the free lists for the desirable migrate type are depleted
 */
static int fallbacks[MIGRATE_TYPES][MIGRATE_TYPES-1] = {
	[MIGRATE_UNMOVABLE]	= { MIGRATE_RECLAIMABLE,	MIGRATE_MOVABLE,		MIGRATE_RESERVE },
	[MIGRATE_RECLAIMABLE]	= { MIGRATE_UNMOVABLE,		MIGRATE_MOVABLE,		MIGRATE_RESERVE },
	[MIGRATE_MOVABLE]	= { MIGRATE_RECLAIMABLE,	MIGRATE_UNMOVABLE,		MIGRATE_RESERVE },
	[MIGRATE_RESERVE]	= { MIGRATE_RESERVE,		MIGRATE_RESERVE,		MIGRATE_RESERVE }, /* Never used */
};

/* Remove an element from the buddy allocator from the fallback list */
static inline struct page *__rmqueue_fallback(struct zone *zone, int order, int start_migratetype)
{
	struct free_area * area;
	int current_order;
	struct page *page;
	int migratetype, i;

	/*
	 * 与__rmqueue_smallest()不同(参见__rmqueue_smallest()节)：
	 * 此处按order由大到小的顺序分配，且查找所有的migratetype类型
	 */
	/* Find the largest possible block of pages in the other list */
	for (current_order = MAX_ORDER-1; current_order >= order; --current_order) {
		for (i = 0; i < MIGRATE_TYPES - 1; i++) {
			migratetype = fallbacks[start_migratetype][i];

			/* MIGRATE_RESERVE handled later if necessary */
			if (migratetype == MIGRATE_RESERVE)
				continue;

			area = &(zone->free_area[current_order]);
			if (list_empty(&area->free_list[migratetype]))
				continue;

			page = list_entry(area->free_list[migratetype].next, struct page, lru);
			area->nr_free--;

			/*
			 * If breaking a large block of pages, move all free
			 * pages to the preferred allocation list. If falling
			 * back for a reclaimable kernel allocation, be more
			 * aggressive about taking ownership of free pages
			 */
			if (unlikely(current_order >= (pageblock_order >> 1))
				 || start_migratetype == MIGRATE_RECLAIMABLE
				 || page_group_by_mobility_disabled) {
				unsigned long pages;
				pages = move_freepages_block(zone, page, start_migratetype);

				/* Claim the whole block if over half of it is free */
				if (pages >= (1 << (pageblock_order-1)) || page_group_by_mobility_disabled)
					set_pageblock_migratetype(page, start_migratetype);

				migratetype = start_migratetype;
			}

			/* Remove the page from the freelists */
			list_del(&page->lru);
			rmv_page_order(page);

			/* Take ownership for orders >= pageblock_order */
			if (current_order >= pageblock_order)
				change_pageblock_range(page, current_order, start_migratetype);

			// 参见__rmqueue_smallest()节
			expand(zone, page, order, current_order, area, migratetype);

			trace_mm_page_alloc_extfrag(page, order, current_order, start_migratetype, migratetype);

			return page;
		}
	}

	return NULL;
}
```

###### 6.4.1.1.2.1.2 prep_new_page()

该函数定义于mm/page_alloc.c:

```
static int prep_new_page(struct page *page, int order, gfp_t gfp_flags)
{
	int i;

	for (i = 0; i < (1 << order); i++) {
		struct page *p = page + i;
		if (unlikely(check_new_page(p)))			// 判断页面合法性，参见prep_new_page()节
			return 1;
	}

	set_page_private(page, 0);					// page->private = 0
	set_page_refcounted(page);					// page->_count = 1

	arch_alloc_page(page, order);
	kernel_map_pages(page, 1 << order, 1);

	if (gfp_flags & __GFP_ZERO)
		prep_zero_page(page, order, gfp_flags);	// Fill the allocated memory area with zeros.

	if (order && (gfp_flags & __GFP_COMP))
		prep_compound_page(page, order);			// 参见prep_compound_page()节

	return 0;
}
```

###### 6.4.1.1.2.1.2.1 check_new_page()

该函数定义于mm/page_alloc.c:

```
static inline int check_new_page(struct page *page)
{
	if (unlikely(page_mapcount(page)				// &(page)->_mapcount) + 1
		 | (page->mapping != NULL)
		 | (atomic_read(&page->_count) != 0)
		 | (page->flags & PAGE_FLAGS_CHECK_AT_PREP)
		 | (mem_cgroup_bad_page_check(page)))) {
		bad_page(page);
		return 1;
	}
	return 0;
}
```

###### 6.4.1.1.2.1.2.2 prep_compound_page()

该函数定义于mm/page_alloc.c:

```
void prep_compound_page(struct page *page, unsigned long order)
{
	int i;
	int nr_pages = 1 << order;

	// page[1].lru.next = (void *)free_compound_page;
	set_compound_page_dtor(page, free_compound_page);
	// page[1].lru.prev = (void *)order;
	set_compound_order(page, order);
	// 设置page->flags中的PG_head标志位，参见include/linux/page-flags.h
	__SetPageHead(page);
	for (i = 1; i < nr_pages; i++) {
		struct page *p = page + i;
		__SetPageTail(p);		// page->flags |= PG_head_tail_mask;
		set_page_count(p, 0);		// page->_count = 0
		p->first_page = page;		// 链接页面
	}
}
```

##### 6.4.1.1.3 \__alloc_pages_slowpath()

该函数定义于mm/page_alloc.c:

```
static inline struct page *__alloc_pages_slowpath(gfp_t gfp_mask, unsigned int order,
	struct zonelist *zonelist, enum zone_type high_zoneidx,
	nodemask_t *nodemask, struct zone *preferred_zone, int migratetype)
{
	const gfp_t wait = gfp_mask & __GFP_WAIT;
	struct page *page = NULL;
	int alloc_flags;
	unsigned long pages_reclaimed = 0;
	unsigned long did_some_progress;
	bool sync_migration = false;

	/*
	 * In the slowpath, we sanity check order to avoid ever trying to
	 * reclaim >= MAX_ORDER areas which will never succeed. Callers may
	 * be using allocators in order of preference for an area that is
	 * too large.
	 */
	if (order >= MAX_ORDER) {
		WARN_ON_ONCE(!(gfp_mask & __GFP_NOWARN));
		return NULL;
	}

	/*
	 * GFP_THISNODE (meaning __GFP_THISNODE, __GFP_NORETRY and
	 * __GFP_NOWARN set) should not cause reclaim since the subsystem
	 * (f.e. slab) using GFP_THISNODE may choose to trigger reclaim
	 * using a larger set of nodes after it has established that the
	 * allowed per node queues are empty and that nodes are
	 * over allocated.
	 */
	if (NUMA_BUILD && (gfp_mask & GFP_THISNODE) == GFP_THISNODE)
		goto nopage;

restart:
	// 参见wake_all_kswapd()节
	if (!(gfp_mask & __GFP_NO_KSWAPD))
		wake_all_kswapd(order, zonelist, high_zoneidx, zone_idx(preferred_zone));

	/*
	 * OK, we're below the kswapd watermark and have kicked background
	 * reclaim. Now things get more complex, so set up alloc_flags according
	 * to how we want to proceed.
	 */
	alloc_flags = gfp_to_alloc_flags(gfp_mask);

	/*
	 * Find the true preferred zone if the allocation is unconstrained by
	 * cpusets.
	 */
	if (!(alloc_flags & ALLOC_CPUSET) && !nodemask)
		first_zones_zonelist(zonelist, high_zoneidx, NULL, &preferred_zone);

rebalance:
	/* This is the last chance, in general, before the goto nopage. */
	// 参见get_page_from_freelist()节
	page = get_page_from_freelist(gfp_mask, nodemask, order, zonelist, high_zoneidx,
			alloc_flags & ~ALLOC_NO_WATERMARKS, preferred_zone, migratetype);
	if (page)
		goto got_pg;

	/* Allocate without watermarks if the context allows */
	if (alloc_flags & ALLOC_NO_WATERMARKS) {
		page = __alloc_pages_high_priority(gfp_mask, order, zonelist,
				high_zoneidx, nodemask, preferred_zone, migratetype);
		if (page)
			goto got_pg;
	}

	/* Atomic allocations - we can't balance anything */
	if (!wait)
		goto nopage;

	/* Avoid recursion of direct reclaim */
	if (current->flags & PF_MEMALLOC)
		goto nopage;

	/* Avoid allocations with no watermarks from looping endlessly */
	if (test_thread_flag(TIF_MEMDIE) && !(gfp_mask & __GFP_NOFAIL))
		goto nopage;

	/*
	 * Try direct compaction. The first pass is asynchronous. Subsequent
	 * attempts after direct reclaim are synchronous
	 */
	page = __alloc_pages_direct_compact(gfp_mask, order, zonelist, high_zoneidx, nodemask,
			alloc_flags, preferred_zone, migratetype, &did_some_progress, sync_migration);
	if (page)
		goto got_pg;
	sync_migration = true;

	/* Try direct reclaim and then allocating */
	page = __alloc_pages_direct_reclaim(gfp_mask, order, zonelist, high_zoneidx,
			nodemask, alloc_flags, preferred_zone, migratetype, &did_some_progress);
	if (page)
		goto got_pg;

	/*
	 * If we failed to make any progress reclaiming, then we are
	 * running out of options and have to consider going OOM
	 */
	if (!did_some_progress) {
		if ((gfp_mask & __GFP_FS) && !(gfp_mask & __GFP_NORETRY)) {
			if (oom_killer_disabled)
				goto nopage;
			page = __alloc_pages_may_oom(gfp_mask, order, zonelist,
					high_zoneidx, nodemask, preferred_zone, migratetype);
			if (page)
				goto got_pg;

			if (!(gfp_mask & __GFP_NOFAIL)) {
				/*
				 * The oom killer is not called for high-order
				 * allocations that may fail, so if no progress
				 * is being made, there are no other options and
				 * retrying is unlikely to help.
				 */
				if (order > PAGE_ALLOC_COSTLY_ORDER)
					goto nopage;
				/*
				 * The oom killer is not called for lowmem
				 * allocations to prevent needlessly killing
				 * innocent tasks.
				 */
				if (high_zoneidx < ZONE_NORMAL)
					goto nopage;
			}

			goto restart;
		}
	}

	/* Check if we should retry the allocation */
	pages_reclaimed += did_some_progress;
	if (should_alloc_retry(gfp_mask, order, pages_reclaimed)) {
		/* Wait for some write requests to complete then retry */
		wait_iff_congested(preferred_zone, BLK_RW_ASYNC, HZ/50);
		goto rebalance;
	} else {
		/*
		 * High-order allocations do not necessarily loop after
		 * direct reclaim and reclaim/compaction depends on compaction
		 * being called after reclaim so call directly if necessary
		 */
		page = __alloc_pages_direct_compact(gfp_mask, order, zonelist, high_zoneidx, nodemask,
				alloc_flags, preferred_zone, migratetype, &did_some_progress, sync_migration);
		if (page)
			goto got_pg;
	}

nopage:
	warn_alloc_failed(gfp_mask, order, NULL);
	return page;
got_pg:
	if (kmemcheck_enabled)
		kmemcheck_pagealloc_alloc(page, order, gfp_mask);
	return page;

}
```

###### 6.4.1.1.3.1 wake_all_kswapd()

该函数定义于mm/page_alloc.c:

```
static inline void wake_all_kswapd(unsigned int order, struct zonelist *zonelist,
				enum zone_type high_zoneidx, enum zone_type classzone_idx)
{
	struct zoneref *z;
	struct zone *zone;

	for_each_zone_zonelist(zone, z, zonelist, high_zoneidx)
		wakeup_kswapd(zone, order, classzone_idx);	// 参见wakeup_kswapd()节
}
```

###### 6.4.1.1.3.1.1 kswapd

###### 6.4.1.1.3.1.1.1 kswapd线程的初始化

结构pg_date_t中的变量kswapd是通过函数kswapd_init()设置的，其定义于mm/vmscan.c:

```
static int __init kswapd_init(void)
{
	int nid;

	swap_setup();
	for_each_node_state(nid, N_HIGH_MEMORY)
 		kswapd_run(nid);
	hotcpu_notifier(cpu_callback, 0);
	return 0;
}

/*
* 由mm/Makefile可知，vmscan.c被直接编译进内核，因此kswapd_init()在系统启动时执行，参见.initcall*.init节
* kernel_init() -> do_basic_setup() -> do_initcalls() -> do_one_initcall()
 *                                                ^
 *                                                +-- 其中的.initcall6.init
 */
module_init(kswapd_init)
```

其中，函数kswapd_run()定义于mm/vmscan.c:

```
int kswapd_run(int nid)
{
	pg_data_t *pgdat = NODE_DATA(nid);
	int ret = 0;

	if (pgdat->kswapd)
		return 0;

	// 创建kswapd内核线程，参见kthread_run()节，该线程执行函数kswapd().
	pgdat->kswapd = kthread_run(kswapd, pgdat, "kswapd%d", nid);
	if (IS_ERR(pgdat->kswapd)) {
		/* failure at boot is fatal */
		BUG_ON(system_state == SYSTEM_BOOTING);
		printk("Failed to start kswapd on node %d\n",nid);
		ret = -1;
	}
	return ret;
}
```

其中，函数kswapd()定义于mm/vmscan.c:

```
static int kswapd(void *p)
{
	unsigned long order, new_order;
	unsigned balanced_order;
	int classzone_idx, new_classzone_idx;
	int balanced_classzone_idx;
	pg_data_t *pgdat = (pg_data_t*)p;
	struct task_struct *tsk = current;

	struct reclaim_state reclaim_state = {
		.reclaimed_slab = 0,
	};
	const struct cpumask *cpumask = cpumask_of_node(pgdat->node_id);

	lockdep_set_current_reclaim_state(GFP_KERNEL);

	if (!cpumask_empty(cpumask))
		set_cpus_allowed_ptr(tsk, cpumask);
	current->reclaim_state = &reclaim_state;

	/*
	 * Tell the memory management that we're a "memory allocator",
	 * and that if we need more memory we should get access to it
	 * regardless (see "__alloc_pages()"). "kswapd" should
	 * never get caught in the normal page freeing logic.
	 *
	 * (Kswapd normally doesn't need memory anyway, but sometimes
	 * you need a small amount of memory in order to be able to
	 * page out something else, and this flag essentially protects
	 * us from recursively trying to free more memory as we're
	 * trying to free the first piece of memory in the first place).
	 */
	tsk->flags |= PF_MEMALLOC | PF_SWAPWRITE | PF_KSWAPD;
	set_freezable();

	order = new_order = 0;
	balanced_order = 0;
	classzone_idx = new_classzone_idx = pgdat->nr_zones - 1;
	balanced_classzone_idx = classzone_idx;
	for ( ; ; ) {
		int ret;

		/*
		 * If the last balance_pgdat was unsuccessful it's unlikely a
		 * new request of a similar or harder type will succeed soon
		 * so consider going to sleep on the basis we reclaimed at
		 */
		if (balanced_classzone_idx >= new_classzone_idx && balanced_order == new_order) {
			new_order = pgdat->kswapd_max_order;
			new_classzone_idx = pgdat->classzone_idx;
			pgdat->kswapd_max_order =  0;
			pgdat->classzone_idx = pgdat->nr_zones - 1;
		}

		if (order < new_order || classzone_idx > new_classzone_idx) {
			/*
			 * Don't sleep if someone wants a larger 'order'
			 * allocation or has tigher zone constraints
			 */
			order = new_order;
			classzone_idx = new_classzone_idx;
		} else {
			kswapd_try_to_sleep(pgdat, balanced_order, balanced_classzone_idx);
			order = pgdat->kswapd_max_order;
			classzone_idx = pgdat->classzone_idx;
			new_order = order;
			new_classzone_idx = classzone_idx;
			pgdat->kswapd_max_order = 0;
			pgdat->classzone_idx = pgdat->nr_zones - 1;
		}

		ret = try_to_freeze();
		if (kthread_should_stop())
			break;

		/*
		 * We can speed up thawing tasks if we don't call balance_pgdat
		 * after returning from the refrigerator
		 */
		if (!ret) {
			trace_mm_vmscan_kswapd_wake(pgdat->node_id, order);
			balanced_classzone_idx = classzone_idx;
			balanced_order = balance_pgdat(pgdat, order, &balanced_classzone_idx);
		}
	}
	return 0;
}
```

###### 6.4.1.1.3.1.1.2 wakeup_kswapd()

该函数定义于mm/vmscan.c:

```
void wakeup_kswapd(struct zone *zone, int order, enum zone_type classzone_idx)
{
	pg_data_t *pgdat;

	if (!populated_zone(zone))
		return;

	if (!cpuset_zone_allowed_hardwall(zone, GFP_KERNEL))
		return;
	pgdat = zone->zone_pgdat;
	if (pgdat->kswapd_max_order < order) {
		pgdat->kswapd_max_order = order;
		pgdat->classzone_idx = min(pgdat->classzone_idx, classzone_idx);
	}
	if (!waitqueue_active(&pgdat->kswapd_wait))
		return;
	if (zone_watermark_ok_safe(zone, order, low_wmark_pages(zone), 0, 0))
		return;

	trace_mm_vmscan_wakeup_kswapd(pgdat->node_id, zone_idx(zone), order);
	// 唤醒pgdat->kswapd_wait进程，参见wake_up_xxx()节
	wake_up_interruptible(&pgdat->kswapd_wait);
}
```

#### 6.4.1.2 page_address()

The page_address() function returns the linear address associated with the page frame, or NULL if the page frame is in high memory and is not mapped.

根据编译选项的不同，其定义也不同，如下表所示：

| Macros Definitions<br>WANT_PAGE_VIRTUAL | Macros Definitions<br>CONFIG_HIGHMEM | page_address() |
|:--------------------------------------- | :----------------------------------- | :------------- |
| Defined     | -           | #define page_address(page) ((page)->virtual) |
| Not Defined | Not Defined | #define page_address(page) lowmem_page_address(page)，参见lowmem_page_address()节 |
| Not Defined | Defined     | 定义于mm/highmem.c，参见page_address() in mm/highmem.c节 |

<p/>

参见include/linux/mm.h:

```
#if defined(CONFIG_HIGHMEM) && !defined(WANT_PAGE_VIRTUAL)
#define HASHED_PAGE_VIRTUAL
#endif

#if defined(WANT_PAGE_VIRTUAL)
#define page_address(page)		((page)->virtual)
#define set_page_address(page, address)			\
	do {						\
		(page)->virtual = (address);		\
	} while(0)
#define page_address_init()		do { } while(0)
#endif

#if defined(HASHED_PAGE_VIRTUAL)
void *page_address(const struct page *page);	// mm/highmem.c
void set_page_address(struct page *page, void *virtual);
void page_address_init(void);
#endif

#if !defined(HASHED_PAGE_VIRTUAL) && !defined(WANT_PAGE_VIRTUAL)
#define page_address(page)			lowmem_page_address(page)
#define set_page_address(page, address) 	do { } while(0)
#define page_address_init()			do { } while(0)
#endif
```

##### 6.4.1.2.1 lowmem_page_address()

该函数定义于include/linux/mm.h:

```
static __always_inline void *lowmem_page_address(const struct page *page)
{
	// page_to_pfn()参见pte_page()/pte_pfn()节，__va()参见pgd_page_vaddr()节
	return __va(PFN_PHYS(page_to_pfn(page)));
}
```

其中，宏PFN_PHYS()定义于include/linux/pfn.h:

```
#define PFN_PHYS(x)		((phys_addr_t)(x) << PAGE_SHIFT)
```

##### 6.4.1.2.2 page_address() in mm/highmem.c

该函数定义于mm/highmem.c:

```
/**
 * page_address - get the mapped virtual address of a page
 * @page: &struct page to get the virtual address of
 *
 * Returns the page's virtual address.
 */
void *page_address(const struct page *page)
{
	unsigned long flags;
	void *ret;
	struct page_address_slot *pas;

	// 若不是高端内存，参见lowmem_page_address()节
	if (!PageHighMem(page))
		return lowmem_page_address(page);

	/*
	 * 获取page_address_htable中page所在的表项，
	 * 参见错误：引用源未找到
	 */
	pas = page_slot(page);
	ret = NULL;
	spin_lock_irqsave(&pas->lock, flags);
	if (!list_empty(&pas->lh)) {
		struct page_address_map *pam;

		list_for_each_entry(pam, &pas->lh, list) {
			if (pam->page == page) {
				ret = pam->virtual;
				goto done;
			}
		}
	}
done:
	spin_unlock_irqrestore(&pas->lock, flags);
	return ret;
}
```

变量page_address_htable:

![Memery_Layout_11](/assets/Memery_Layout_11.jpg)

#### 6.4.1.3 \__get_free_pages()

Function that is similar to alloc_pages(), but it returns the linear address of the first allocated page.

该函数定义于mm/page_alloc.c:

```
unsigned long __get_free_pages(gfp_t gfp_mask, unsigned int order)
{
	struct page *page;

	/*
	 * __get_free_pages() returns a 32-bit address, which cannot represent
	 * a highmem page
	 */
	VM_BUG_ON((gfp_mask & __GFP_HIGHMEM) != 0);

	page = alloc_pages(gfp_mask, order);		// 参见alloc_pages()节
	if (!page)
		return 0;
	return (unsigned long) page_address(page);	// 参见page_address()节
}
```

#### 6.4.1.4 \__get_dma_pages()

Macro used to get page frames suitable for DMA; see include/linux/gfp.h:

```
// 参见__get_free_pages()节
#define __get_dma_pages(gfp_mask, order)		\
		 __get_free_pages((gfp_mask) | GFP_DMA, (order))
```

#### 6.4.1.5 free_pages()/\__free_pages()

```
void __free_pages(struct page *page, unsigned int order);
```

The function ```__free_pages()``` checks the page descriptor pointed to by page; if the page frame is not reserved (i.e., if the PG_reserved flag is equal to 0), it decreases the count field of the descriptor. If count becomes 0, it assumes that 2order contiguous page frames starting from the one corresponding to page are no longer used. In this case, the function releases the page frames.

```
void free_pages(unsigned long addr, unsigned int order);
```

The function free_pages() is similar to ```__free_pages()```, but it receives as an argument the linear address addr of the first page frame to be released.

函数free_pages()定义于mm/page_alloc.c:

```
void free_pages(unsigned long addr, unsigned int order)
{
	if (addr != 0) {
		VM_BUG_ON(!virt_addr_valid((void *)addr));
		__free_pages(virt_to_page((void *)addr), order);
	}
}
```

函数__free_pages()定义于mm/page_alloc.c:

```
void __free_pages(struct page *page, unsigned int order)
{
	// if page->_count-- is 0, then the page has no users, release it!
	if (put_page_testzero(page)) {
		if (order == 0)
			free_hot_cold_page(page, 0);	// 参见free_hot_cold_page()节
		else
			__free_pages_ok(page, order);	// 参见__free_pages_ok()节
	}
}
```

##### 6.4.1.5.1 free_hot_cold_page()

该函数定义于mm/page_alloc.c:

```
/*
 * Free a 0-order page
 * cold == 1 ? free a cold page : free a hot page
 */
void free_hot_cold_page(struct page *page, int cold)
{
	struct zone *zone = page_zone(page);
	struct per_cpu_pages *pcp;
	unsigned long flags;
	int migratetype;
	// 判断并清除page->flags中的PG_mlocked标志位
	int wasMlocked = __TestClearPageMlocked(page);

	// 参见free_pages_prepare()节
	if (!free_pages_prepare(page, 0))
		return;

	migratetype = get_pageblock_migratetype(page);
	// page->private = migratetype
	set_page_private(page, migratetype);
	local_irq_save(flags);
	if (unlikely(wasMlocked))
		// 更新page->vm_stat[NR_MLOCK]和vm_stat[NR_MLOCK]
		free_page_mlock(page);
	// 更新vm_event_states.event[PGFREE]
	__count_vm_event(PGFREE);

	/*
	 * We only track unmovable, reclaimable and movable on pcp lists.
	 * Free ISOLATE pages back to the allocator because they are being
	 * offlined but treat RESERVE as movable pages so we can get those
	 * areas back if necessary. Otherwise, we may have to free
	 * excessively into the page allocator
	 */
	if (migratetype >= MIGRATE_PCPTYPES) {
		if (unlikely(migratetype == MIGRATE_ISOLATE)) {
			// 参见free_one_page()节
			free_one_page(zone, page, 0, migratetype);
			goto out;
		}
		migratetype = MIGRATE_MOVABLE;
	}

	/*
	 * 将该页面插入Per-CPU Page Frame Cache，
	 * 参见错误：引用源未找到
	 */
	pcp = &this_cpu_ptr(zone->pageset)->pcp;
	if (cold)
		list_add_tail(&page->lru, &pcp->lists[migratetype]);
	else
		list_add(&page->lru, &pcp->lists[migratetype]);
	pcp->count++;
	/*
	 * 若超过阀值，则释放batch个页面到Buddy Allocator System
	 * 与buffered_rmqueue()->rmqueue_bulk()对应，
	 * 参见buffered_rmqueue()节
	 */
	if (pcp->count >= pcp->high) {
		free_pcppages_bulk(zone, pcp->batch, pcp);
		pcp->count -= pcp->batch;
	}

out:
	local_irq_restore(flags);
}
```

###### 6.4.1.5.1.1 free_pages_prepare()

该函数定义于mm/page_alloc.c:

```
static bool free_pages_prepare(struct page *page, unsigned int order)
{
	int i;
	int bad = 0;

	trace_mm_page_free_direct(page, order);
	kmemcheck_free_shadow(page, order);

	// page->mapping & PAGE_MAPPING_ANON) != 0
	if (PageAnon(page))
		page->mapping = NULL;
	for (i = 0; i < (1 << order); i++)
		// 与check_new_page()对应，参见prep_new_page()节
		bad += free_pages_check(page + i);
	if (bad)
		return false;

	// 判断是否为高端内存
	if (!PageHighMem(page)) {
		debug_check_no_locks_freed(page_address(page),PAGE_SIZE << order);
		debug_check_no_obj_freed(page_address(page), PAGE_SIZE << order);
	}
	arch_free_page(page, order);
	kernel_map_pages(page, 1 << order, 0);

	return true;
}
```

###### 6.4.1.5.1.2 free_one_page()

该函数定义于mm/page_alloc.c:

```
static void free_one_page(struct zone *zone, struct page *page, int order, int migratetype)
{
	spin_lock(&zone->lock);
	zone->all_unreclaimable = 0;
	zone->pages_scanned = 0;

	// 参见__free_one_page()节
	__free_one_page(page, zone, order, migratetype);
	__mod_zone_page_state(zone, NR_FREE_PAGES, 1 << order);
	spin_unlock(&zone->lock);
}
```

###### 6.4.1.5.1.2.1 \__free_one_page()

该函数定义于mm/page_alloc.c:

```
static inline void __free_one_page(struct page *page,
		struct zone *zone, unsigned int order, int migratetype)
{
	unsigned long page_idx;
	unsigned long combined_idx;
	unsigned long uninitialized_var(buddy_idx);
	struct page *buddy;

	// 判断是否为复合页：page->flags & ((1L << PG_head) | (1L << PG_tail)
	if (unlikely(PageCompound(page)))
		if (unlikely(destroy_compound_page(page, order)))
			return;

	VM_BUG_ON(migratetype == -1);

	// page_idx取页框号的低11比特位，参见struct zone节中free_area[]的注释
	page_idx = page_to_pfn(page) & ((1 << MAX_ORDER) - 1);

	VM_BUG_ON(page_idx & ((1 << order) - 1));
	VM_BUG_ON(bad_range(zone, page));

	// 按order从小到大的顺序，查找该页面对应的最大伙伴页面
	while (order < MAX_ORDER-1) {
		// 获得该页对应的伙伴页的索引，其中page[8]对应的伙伴页为page
		buddy_idx = __find_buddy_index(page_idx, order);
		// 找到该页对应的伙伴页，并判断其合法性
		buddy = page + (buddy_idx - page_idx);
		if (!page_is_buddy(page, buddy, order))
			break;

		/* Our buddy is free, merge with it and move up one order. */
		list_del(&buddy->lru);
		zone->free_area[order].nr_free--;
		// 1) 清除Buddy Allocator标志，即page->_mapcount = -1;
		// 2) 设置page->private = 0. 注：页描述符中的private保存其对应的order值.
		rmv_page_order(buddy);
		combined_idx = buddy_idx & page_idx;
		page = page + (combined_idx - page_idx);
		page_idx = combined_idx;
		order++;
	}
	/*
	 * 找到最大的伙伴页面后，设置标志：
	 * 设置page->private = order. 注：页描述符中的private保存其对应的order值；
	 * 设置Buddy Allocator标志，即page->_mapcount = PAGE_BUDDY_MAPCOUNT_VALUE
	 */
	set_page_order(page, order);

	/*
	 * If this is not the largest possible page, check if the buddy
	 * of the next-highest order is free. If it is, it's possible
	 * that pages are being freed that will coalesce soon. In case,
	 * that is happening, add the free page to the tail of the list
	 * so it's less likely to be used soon and more likely to be merged
	 * as a higher order page
	 */
	if ((order < MAX_ORDER-2) && pfn_valid_within(page_to_pfn(buddy))) {
		struct page *higher_page, *higher_buddy;
		combined_idx = buddy_idx & page_idx;
		higher_page = page + (combined_idx - page_idx);
		buddy_idx = __find_buddy_index(combined_idx, order + 1);
		higher_buddy = page + (buddy_idx - combined_idx);
		if (page_is_buddy(higher_page, higher_buddy, order + 1)) {
			list_add_tail(&page->lru, &zone->free_area[order].free_list[migratetype]);
			goto out;
		}
	}

	// 将最大的伙伴页面链接到对应order的空闲链表中，并更新计数
	list_add(&page->lru, &zone->free_area[order].free_list[migratetype]);
out:
	zone->free_area[order].nr_free++;
}
```

###### 6.4.1.5.1.3 free_pcppages_bulk()

该函数定义于mm/page_alloc.c:

```
/*
 * Frees a number of pages from the PCP lists
 * Assumes all pages on list are in same zone, and of same order.
 * count is the number of pages to free.
 *
 * If the zone was previously in an "all pages pinned" state then look to
 * see if this freeing clears that state.
 *
 * And clear the zone's pages_scanned counter, to hold off the "all pages are
 * pinned" detection logic.
 */
static void free_pcppages_bulk(struct zone *zone, int count, struct per_cpu_pages *pcp)
{
	int migratetype = 0;
	int batch_free = 0;
	int to_free = count;

	spin_lock(&zone->lock);
	zone->all_unreclaimable = 0;
	zone->pages_scanned = 0;

	while (to_free) {
		struct page *page;
		struct list_head *list;

		/*
		 * Remove pages from lists in a round-robin fashion. A
		 * batch_free count is maintained that is incremented when an
		 * empty list is encountered.  This is so more pages are freed
		 * off fuller lists instead of spinning excessively around empty
		 * lists
		 */
		do {
			batch_free++;
			if (++migratetype == MIGRATE_PCPTYPES)
				migratetype = 0;
			list = &pcp->lists[migratetype];
		} while (list_empty(list));

		/* This is the only non-empty list. Free them all. */
		if (batch_free == MIGRATE_PCPTYPES)
			batch_free = to_free;

		do {
			page = list_entry(list->prev, struct page, lru);
			/* must delete as __free_one_page list manipulates */
			list_del(&page->lru);
			/* MIGRATE_MOVABLE list may include MIGRATE_RESERVEs */
			// 参见__free_one_page()节
			__free_one_page(page, zone, 0, page_private(page));
			trace_mm_page_pcpu_drain(page, 0, page_private(page));
		} while (--to_free && --batch_free && !list_empty(list));
	}
	__mod_zone_page_state(zone, NR_FREE_PAGES, count);
	spin_unlock(&zone->lock);
}
```

##### 6.4.1.5.2 \__free_pages_ok()

该函数定义于mm/page_alloc.c:

```
static void __free_pages_ok(struct page *page, unsigned int order)
{
	unsigned long flags;
	// 判断并清除page->flags中的PG_mlocked标志位
	int wasMlocked = __TestClearPageMlocked(page);

	// 参见free_pages_prepare()节
	if (!free_pages_prepare(page, order))
		return;

	local_irq_save(flags);
	if (unlikely(wasMlocked))
		free_page_mlock(page);
	__count_vm_events(PGFREE, 1 << order);
	// 参见free_one_page()节
	free_one_page(page_zone(page), page, order, get_pageblock_migratetype(page));
	local_irq_restore(flags);
}
```

### 6.4.2 分配/释放单个内存页

#### 6.4.2.1 alloc_page()

The macro alloc_page() used to get a single page frame; see include/linux/gfp.h:

```
// 参见alloc_pages()节
#define alloc_page(gfp_mask)		alloc_pages(gfp_mask, 0)
```

It returns the address of the descriptor of the allocated page frame or returns NULL if the allocation failed.

#### 6.4.2.2 get_zeroed_page()

Function get_zeroed_page() used to obtain a page frame filled with zeros; see mm/page_alloc.c:

```
unsigned long get_zeroed_page(gfp_t gfp_mask)
{
	// 参见__get_free_pages()节
	return __get_free_pages(gfp_mask | __GFP_ZERO, 0);
}
```

It returns the linear address of the obtained page frame.

#### 6.4.2.3 \__get_free_page()

The macro ```__get_free_page()``` used to get a single page frame; see include/linux/gfp.h:

```
// 参见__get_free_pages()节
#define __get_free_page(gfp_mask)	__get_free_pages((gfp_mask), 0)
```

#### 6.4.2.4 \__free_page()/free_page()

Macro ```__free_page()``` releases the page frame having the descriptor pointed to by page; Macro free_page() releases the page frame having the linear address addr. See include/linux/gfp.h:

```
// 参见free_pages()/__free_pages()节
#define __free_page(page)		__free_pages((page), 0)
#define free_page(addr)			free_pages((addr), 0)
```

## 6.5 Slab Allocator

Running a memory area allocation algorithm on top of the buddy algorithm (参见分配/释放内存页节) is not particularly efficient. A better algorithm is derived from the slab allocator schema that was adopted for the first time in the Sun Microsystems Solaris 2.4 operating system.

The slab allocator groups objects into caches. Each cache is a "store" of objects of the same type.

The area of main memory that contains a cache is divided into slabs; each slab consists of one or more contiguous page frames that contain both allocated and free objects.

Run following command to get a full list of caches available on a running system (参见6.5.1.1.2.1 查看slab的分配信息节):

```
# cat /proc/slabinfo
```

![Slab_Cache](/assets/Slab_Cache.png)

### 6.5.0 SLAB/SLUB/SLOB Allocator配置选项

通过如下选项配置SLAB/SLUB/SLOB Allocator:

```
General setup  --->
  Choose SLAB allocator (SLAB)  --->
    (X) SLAB
    ( ) SLUB (Unqueued Allocator)
    ( ) SLOB (Simple Allocator)
```

由此可知，这三个配置选项是互斥的，因而只能选择其中之一！

NOTE: SLAB/SLUB/SLOB allocator的区别
* SLAB是基础，是最早从Sun OS那引进的；
* SLUB是在Slab上进行的改进，在大型机上表现出色，据说还被IA-64作为默认；
* SLOB是针对小型系统设计的，主要是嵌入式。

### 6.5.1 Cache Descriptor/struct kmem_cache

Each cache is described by a structure of type struct kmem_cache. 该结构定义于include/linux/slab_def.h:

```
struct kmem_cache {
/* 1) Cache tunables. Protected by cache_chain_mutex */
	// Number of objects to be transferred in bulk to or from the local caches.
	unsigned int batchcount;
	// Maximum number of free objects in the local caches.
	unsigned int limit;
	unsigned int shared;

	unsigned int buffer_size;
	u32 reciprocal_buffer_size;

/* 2) touched by every alloc & free from the backend */
	// See SLAB_xxx in include/linux/slab.h
	unsigned int flags;		/* constant flags */
	// Number of objects packed into a single slab.
	// All slabs of the cache have the same size.
	unsigned int num;		/* # of objs per slab */

/* 3) cache_grow/shrink */
	/* order of pgs per slab (2^n) */
	// Logarithm of the number of contiguous page frames included in a single slab.
	unsigned int gfporder;

	/* force GFP flags, e.g. GFP_DMA */
	// Set of flags passed to the buddy allocator system function when allocating page frames.
	gfp_t gfpflags;

	// Number of colors for the slabs
	size_t colour;				/* cache colouring range */
	unsigned int colour_off;	/* colour offset */
	/*
	 * Pointer to the general slab cache containing the slab descriptors.
	 * NULL if internal slab descriptors are used;
	 */
	struct kmem_cache *slabp_cache;
	// The size of a single slab.
	unsigned int slab_size;
	// Set of flags that describe dynamic properties of the cache.
	unsigned int dflags;		/* dynamic flags */

	/* constructor func */
	void (*ctor)(void *obj);

/* 4) cache creation/removal */
	// Character array storing the name of the cache.
	const char *name;
	/*
	 * Pointers for the doubly linked list of cache descriptors.
	 * 参见Subjects/Chapter06_Memory_Management/Figures/Memery_Layout_15.jpg
	 */
	struct list_head next;

/* 5) statistics */
#ifdef CONFIG_DEBUG_SLAB
	unsigned long num_active;
	unsigned long num_allocations;
	unsigned long high_mark;
	unsigned long grown;
	unsigned long reaped;
	unsigned long errors;
	unsigned long max_freeable;
	unsigned long node_allocs;
	unsigned long node_frees;
	unsigned long node_overflow;
	atomic_t allochit;
	atomic_t allocmiss;
	atomic_t freehit;
	atomic_t freemiss;

	/*
	 * If debugging is enabled, then the allocator can add additional
	 * fields and/or padding to every object. buffer_size contains the total
	 * object size including these internal fields, the following two
	 * variables contain the offset to the user object and its size.
	 */
	int obj_offset;
	int obj_size;
#endif /* CONFIG_DEBUG_SLAB */

/* 6) per-cpu/per-node data, touched during every alloc/free */
	/*
	 * We put array[] at the end of kmem_cache, because we want to size
	 * this array to nr_cpu_ids slots instead of NR_CPUS (see kmem_cache_init()).
	 * We still use [NR_CPUS] and not [1] or [0] because cache_cache
	 * is statically defined, so we reserve the max number of cpus.
	 */
	struct kmem_list3 **nodelists;
	// Per-CPU array of pointers to local caches of free objects.
	struct array_cache *array[NR_CPUS];
	/*
	 * Do not add fields after array[]
	 */
};

struct kmem_list3定义于mm/slab.c:
struct kmem_list3 {
	// Doubly linked circular list of slab descriptors with both free and nonfree object.
	struct list_head slabs_partial;	/* partial list first, better asm code */
	// Doubly linked circular list of slab descriptors with no free objects.
	struct list_head slabs_full;
	// Doubly linked circular list of slab descriptors with free objects only.
	struct list_head slabs_free;

	// Number of free objects in the cache.
	unsigned long	free_objects;
	unsigned int	free_limit;
	unsigned int	colour_next;	/* Per-node cache coloring */
	spinlock_t		list_lock;
	// Pointer to a local cache shared by all CPUs.
	struct array_cache *shared;		/* shared per node */
	struct array_cache **alien;		/* on other nodes */
	// Below two variable are used by the slab allocator’s page reclaiming algorithm.
	unsigned long	next_reap;		/* updated without locking */
	int			free_touched;	/* updated without locking */
};
```

Relationship between cache and slab descriptors:

![Memery_Layout_14](/assets/Memery_Layout_14.jpg)

#### 6.5.1.1 General Cache/Specific Cache

Caches are divided into two types: general and specific.
* General caches are used only by the slab allocator for its own purposes;
* Specific caches are used by the remaining parts of the kernel.

The names of all general and specific caches can be obtained at runtime by reading /proc/slabinfo; this file also specifies the number of free objects and the number of allocated objects in each cache.

The general caches are:

1) A first cache called kmem_cache whose objects are the cache descriptors of the remaining caches used by the kernel. The cache_cache variable contains the descriptor of this special cache. See mm/slab.c:

```
/* internal cache of cache description objs */
static struct kmem_list3 *cache_cache_nodelists[MAX_NUMNODES];
static struct kmem_cache cache_cache = {
	.nodelists	= cache_cache_nodelists,
	.batchcount	= 1,
	.limit		= BOOT_CPUCACHE_ENTRIES,	// 1
	.shared		= 1,
	.buffer_size	= sizeof(struct kmem_cache),
	.name			= "kmem_cache",
};
```

2) Several additional caches contain general purpose memory areas. The range of the memory area sizes typically includes 13 geometrically distributed sizes. A table called malloc_sizes (whose elements are of type cache_sizes) points to 26 cache descriptors associated with memory areas of size 32, 64, 128, 256, 512, 1,024, 2,048, 4,096, 8,192, 16,384, 32,768, 65,536, and 131,072 bytes. For each size, there are two caches: one suitable for ISA DMA allocations and the other for normal allocations. See mm/slab.c:

```
struct cache_sizes malloc_sizes[] = {
#define CACHE(x) { .cs_size = (x) },
#include <linux/kmalloc_sizes.h>
	CACHE(ULONG_MAX)
#undef CACHE
};

static struct cache_names __initdata cache_names[] = {
#define CACHE(x) { .name = "size-" #x, .name_dma = "size-" #x "(DMA)" },
#include <linux/kmalloc_sizes.h>
	{NULL,}
#undef CACHE
};
```

数组malloc_sizes[]的结构示意图:

![Memery_Layout_15](/assets/Memery_Layout_15.jpg)

其中，数组malloc_sizes[]和cache_names[]被扩展为：

```
struct cache_sizes malloc_sizes[] = {
#if (PAGE_SIZE == 4096)
	{ .cs_size = 32 },
#endif
	{ .cs_size = 64 },
#if L1_CACHE_BYTES < 64
	{ .cs_size = 96 },
#endif
	{ .cs_size = 128 },
#if L1_CACHE_BYTES < 128
	{ .cs_size = 192 },
#endif
	{ .cs_size = 256 },
	{ .cs_size = 512 },
	{ .cs_size = 1024 },
	{ .cs_size = 2048 },
	{ .cs_size = 4096 },
	{ .cs_size = 8192 },
	{ .cs_size = 16384 },
	{ .cs_size = 32768 },
	{ .cs_size = 65536 },
	{ .cs_size = 131072 },
#if KMALLOC_MAX_SIZE >= 262144
	{ .cs_size = 262144 },
#endif
#if KMALLOC_MAX_SIZE >= 524288
	{ .cs_size = 524288 },
#endif
#if KMALLOC_MAX_SIZE >= 1048576
	{ .cs_size = 1048576 },
#endif
#if KMALLOC_MAX_SIZE >= 2097152
	{ .cs_size = 2097152 },
#endif
#if KMALLOC_MAX_SIZE >= 4194304
	{ .cs_size = 4194304 },
#endif
#if KMALLOC_MAX_SIZE >= 8388608
	{ .cs_size = 8388608 },
#endif
#if KMALLOC_MAX_SIZE >= 16777216
	{ .cs_size = 16777216 },
#endif
#if KMALLOC_MAX_SIZE >= 33554432
	{ .cs_size = 33554432 },
#endif
	{ .cs_size = ULONG_MAX }
};

static struct cache_names __initdata cache_names[] = {
#if (PAGE_SIZE == 4096)
	{ .name = "size-32", .name_dma = "size-32(MDA)" },
#endif
	{ .name = "size-64", .name_dma = "size-64(MDA)" },
#if L1_CACHE_BYTES < 64
	{ .name = "size-96", .name_dma = "size-96(MDA)" },
#endif
	{ .name = "size-128", .name_dma = "size-128(MDA)" },
#if L1_CACHE_BYTES < 128
	{ .name = "size-192", .name_dma = "size-192(MDA)" },
#endif
	{ .name = "size-256", .name_dma = "size-256(MDA)" },
	{ .name = "size-512", .name_dma = "size-512(MDA)" },
	{ .name = "size-1024", .name_dma = "size-1024(MDA)" },
	{ .name = "size-2048", .name_dma = "size-2048(MDA)" },
	{ .name = "size-4096", .name_dma = "size-4096(MDA)" },
	{ .name = "size-8192", .name_dma = "size-8192(MDA)" },
	{ .name = "size-16384", .name_dma = "size-16384(MDA)" },
	{ .name = "size-32768", .name_dma = "size-32768(MDA)" },
	{ .name = "size-65536", .name_dma = "size-65536(MDA)" },
	{ .name = "size-131072", .name_dma = "size-131072(MDA)" },
#if KMALLOC_MAX_SIZE >= 262144
	{ .name = "size-262144", .name_dma = "size-262144(MDA)" },
#endif
#if KMALLOC_MAX_SIZE >= 524288
	{ .name = "size-524288", .name_dma = "size-524288(MDA)" },
#endif
#if KMALLOC_MAX_SIZE >= 1048576
	{ .name = "size-1048576", .name_dma = "size-1048576(MDA)" },
#endif
#if KMALLOC_MAX_SIZE >= 2097152
	{ .name = "size-2097152", .name_dma = "size-2097152(MDA)" },
#endif
#if KMALLOC_MAX_SIZE >= 4194304
	{ .name = "size-4194304", .name_dma = "size-4194304(MDA)" },
#endif
#if KMALLOC_MAX_SIZE >= 8388608
	{ .name = "size-8388608", .name_dma = "size-8388608(MDA)" },
#endif
#if KMALLOC_MAX_SIZE >= 16777216
	{ .name = "size-16777216", .name_dma = "size-16777216(MDA)" },
#endif
#if KMALLOC_MAX_SIZE >= 33554432
	{ .name = "size-33554432", .name_dma = "size-33554432(MDA)" },
#endif
	{ NULL, }
};
```

##### 6.5.1.1.1 Initialize General Cache/kmem_cache_init()

The kmem_cache_init() function is invoked during system initialization to set up the general caches.

```
start_kernel()				// 参见start_kernel()节
-> mm_init()				// 参见mm_init()节
   -> kmem_cache_init()
```

该函数定义于mm/slab.c:

```
#define NUM_INIT_LISTS (3 * MAX_NUMNODES)
static struct kmem_list3 __initdata initkmem_list3[NUM_INIT_LISTS];
static struct list_head cache_chain;

/*
 * Initialisation.  Called after the page allocator have been initialised and
 * before smp_init().
 */
void __init kmem_cache_init(void)
{
	size_t left_over;
	struct cache_sizes *sizes;
	struct cache_names *names;
	int i;
	int order;
	int node;

	if (num_possible_nodes() == 1)
		use_alien_caches = 0;

	for (i = 0; i < NUM_INIT_LISTS; i++) {
		kmem_list3_init(&initkmem_list3[i]);
		if (i < MAX_NUMNODES)
			cache_cache.nodelists[i] = NULL;
	}
	// cache_cache->nodelists[i] = &initkmem_list3[i]
	set_up_list3s(&cache_cache, CACHE_CACHE);

	/*
	 * Fragmentation resistance on low memory - only use bigger
	 * page orders on machines with more than 32MB of memory.
	 */
	if (totalram_pages > (32 << 20) >> PAGE_SHIFT)
		slab_break_gfp_order = BREAK_GFP_ORDER_HI;

	/* Bootstrap is tricky, because several objects are allocated
	 * from caches that do not exist yet:
	 * 1) initialize the cache_cache cache: it contains the struct
	 *    kmem_cache structures of all caches, except cache_cache itself:
	 *    cache_cache is statically allocated.
	 *    Initially an __init data area is used for the head array and the
	 *    kmem_list3 structures, it's replaced with a kmalloc allocated
	 *    array at the end of the bootstrap.
	 * 2) Create the first kmalloc cache.
	 *    The struct kmem_cache for the new cache is allocated normally.
	 *    An __init data area is used for the head array.
	 * 3) Create the remaining kmalloc caches, with minimally sized
	 *    head arrays.
	 * 4) Replace the __init data head arrays for cache_cache and the first
	 *    kmalloc cache with kmalloc allocated arrays.
	 * 5) Replace the __init data for kmem_list3 for cache_cache and
	 *    the other cache's with kmalloc allocated memory.
	 * 6) Resize the head arrays of the kmalloc caches to their final sizes.
	 */

	node = numa_mem_id();

	/* 1) create the cache_cache. 并将cache_cache链接到链表cache_chain中 */
	INIT_LIST_HEAD(&cache_chain);
	list_add(&cache_cache.next, &cache_chain);
	cache_cache.colour_off = cache_line_size();
	cache_cache.array[smp_processor_id()] = &initarray_cache.cache;
	cache_cache.nodelists[node] = &initkmem_list3[CACHE_CACHE + node];

	/*
	 * struct kmem_cache size depends on nr_node_ids & nr_cpu_ids
	 */
	cache_cache.buffer_size = offsetof(struct kmem_cache, array[nr_cpu_ids]) +
								    nr_node_ids * sizeof(struct kmem_list3 *);
#if DEBUG
	cache_cache.obj_size = cache_cache.buffer_size;
#endif
	cache_cache.buffer_size = ALIGN(cache_cache.buffer_size, cache_line_size());
	cache_cache.reciprocal_buffer_size = reciprocal_value(cache_cache.buffer_size);

	for (order = 0; order < MAX_ORDER; order++) {
		cache_estimate(order, cache_cache.buffer_size, cache_line_size(), 0,
						  &left_over, &cache_cache.num);
		if (cache_cache.num)
			break;
	}
	BUG_ON(!cache_cache.num);
	cache_cache.gfporder = order;
	cache_cache.colour = left_over / cache_cache.colour_off;
	cache_cache.slab_size = ALIGN(cache_cache.num * sizeof(kmem_bufctl_t) + sizeof(struct slab),
										cache_line_size());

	/* 2+3) create the kmalloc caches */
	sizes = malloc_sizes;		// 变量malloc_sizes参见General Cache/Specific Cache节
	names = cache_names;		// 变量cache_names参见General Cache/Specific Cache节

	/*
	 * Initialize the caches that provide memory for the array cache and the
	 * kmem_list3 structures first.  Without this, further allocations will bug.
	 */
	/*
	 * 创建一个cache并链接到链表cache_chain中，
	 * 参见Create a Specific Cache/kmem_cache_create()节
	 */
	sizes[INDEX_AC].cs_cachep = kmem_cache_create(names[INDEX_AC].name, sizes[INDEX_AC].cs_size,
					ARCH_KMALLOC_MINALIGN, ARCH_KMALLOC_FLAGS|SLAB_PANIC, NULL);

	if (INDEX_AC != INDEX_L3) {
		/*
		 * 创建一个cache并链接到链表cache_chain中，
		 * 参见Create a Specific Cache/kmem_cache_create()节
		 */
		sizes[INDEX_L3].cs_cachep = kmem_cache_create(names[INDEX_L3].name, sizes[INDEX_L3].cs_size,
					ARCH_KMALLOC_MINALIGN, ARCH_KMALLOC_FLAGS|SLAB_PANIC, NULL);
	}

	slab_early_init = 0;

	while (sizes->cs_size != ULONG_MAX) {
		/*
		 * For performance, all the general caches are L1 aligned.
		 * This should be particularly beneficial on SMP boxes, as it
		 * eliminates "false sharing".
		 * Note for systems short on memory removing the alignment will
		 * allow tighter packing of the smaller caches.
		 */
		if (!sizes->cs_cachep) {
			/*
			 * 创建一个cache并链接到链表cache_chain中，
			 * 参见Create a Specific Cache/kmem_cache_create()节
			 */
			sizes->cs_cachep = kmem_cache_create(names->name, sizes->cs_size,
					ARCH_KMALLOC_MINALIGN, ARCH_KMALLOC_FLAGS|SLAB_PANIC, NULL);
		}
#ifdef CONFIG_ZONE_DMA
		/*
		 * 创建一个cache并链接到链表cache_chain中，
		 * 参见Create a Specific Cache/kmem_cache_create()节
		 */
		sizes->cs_dmacachep = kmem_cache_create(names->name_dma, sizes->cs_size,
					ARCH_KMALLOC_MINALIGN, ARCH_KMALLOC_FLAGS|SLAB_CACHE_DMA|SLAB_PANIC, NULL);
#endif
		sizes++;
		names++;
	}
	/* 4) Replace the bootstrap head arrays */
	{
		struct array_cache *ptr;

		ptr = kmalloc(sizeof(struct arraycache_init), GFP_NOWAIT);
		BUG_ON(cpu_cache_get(&cache_cache) != &initarray_cache.cache);
		memcpy(ptr, cpu_cache_get(&cache_cache), sizeof(struct arraycache_init));
		/*
		 * Do not assume that spinlocks can be initialized via memcpy:
		 */
		spin_lock_init(&ptr->lock);
		cache_cache.array[smp_processor_id()] = ptr;
		ptr = kmalloc(sizeof(struct arraycache_init), GFP_NOWAIT);
		BUG_ON(cpu_cache_get(malloc_sizes[INDEX_AC].cs_cachep) != &initarray_generic.cache);
		memcpy(ptr, cpu_cache_get(malloc_sizes[INDEX_AC].cs_cachep), sizeof(struct arraycache_init));
		/*
		 * Do not assume that spinlocks can be initialized via memcpy:
		 */
		spin_lock_init(&ptr->lock);
		malloc_sizes[INDEX_AC].cs_cachep->array[smp_processor_id()] = ptr;
	}
	/* 5) Replace the bootstrap kmem_list3's */
	{
		int nid;

		for_each_online_node(nid) {
			init_list(&cache_cache, &initkmem_list3[CACHE_CACHE + nid], nid);
			init_list(malloc_sizes[INDEX_AC].cs_cachep, &initkmem_list3[SIZE_AC + nid], nid);

			if (INDEX_AC != INDEX_L3) {
				init_list(malloc_sizes[INDEX_L3].cs_cachep, &initkmem_list3[SIZE_L3 + nid], nid);
			}
		}
	}

	g_cpucache_up = EARLY;
}
```

##### 6.5.1.1.2 Create a Specific Cache/kmem_cache_create()

宏KMEM_CACHE()用于创建cache，其定义于include/linux/slab.h:

```
/*
 * Please use this macro to create slab caches. Simply specify the
 * name of the structure and maybe some flags that are listed above.
 *
 * The alignment of the struct determines object alignment. If you
 * f.e. add ____cacheline_aligned_in_smp to the struct declaration
 * then the objects will be properly aligned in SMP configurations.
 */
#define KMEM_CACHE(__struct, __flags) kmem_cache_create(#__struct,	\
		sizeof(struct __struct), __alignof__(struct __struct),	\
		(__flags), NULL)
```

或者直接调用函数kmem_cache_create()来创建cache，其定义于mm/slab.c:

```
/**
 * kmem_cache_create - Create a cache.
 * @name: A string which is used in /proc/slabinfo to identify this cache.
 * @size: The size of objects to be created in this cache.
 * @align: The required alignment for the objects.
 * @flags: SLAB flags
 * @ctor: A constructor for the objects.
 *
 * Returns a ptr to the cache on success, NULL on failure.
 * Cannot be called within a int, but can be interrupted.
 * The @ctor is run when new pages are allocated by the cache.
 *
 * @name must be valid until the cache is destroyed. This implies that
 * the module calling this has to destroy the cache before getting unloaded.
 *
 * The flags are
 *
 * %SLAB_POISON - Poison the slab with a known test pattern (a5a5a5a5)
 * to catch references to uninitialised memory.
 *
 * %SLAB_RED_ZONE - Insert `Red' zones around the allocated memory to check
 * for buffer overruns.
 *
 * %SLAB_HWCACHE_ALIGN - Align the objects in this cache to a hardware
 * cacheline.  This can be beneficial if you're counting cycles as closely
 * as davem.
 */
struct kmem_cache *kmem_cache_create(const char *name, size_t size, size_t align,
				unsigned long flags, void (*ctor)(void *))
{
	size_t left_over, slab_size, ralign;
	struct kmem_cache *cachep = NULL, *pc;
	gfp_t gfp;

	/*
	 * Sanity checks... these are all serious usage bugs.
	 */
	if (!name || in_interrupt() || (size < BYTES_PER_WORD) || size > KMALLOC_MAX_SIZE) {
		printk(KERN_ERR "%s: Early error in slab %s\n", __func__, name);
		BUG();
	}

	/*
	 * We use cache_chain_mutex to ensure a consistent view of
	 * cpu_online_mask as well.  Please see cpuup_callback
	 */
	if (slab_is_available()) {
		get_online_cpus();
		mutex_lock(&cache_chain_mutex);
	}

	// 检查链表cache_chain中是否已存在该cache
	list_for_each_entry(pc, &cache_chain, next) {
		char tmp;
		int res;

		/*
		 * This happens when the module gets unloaded and doesn't
		 * destroy its slab cache and no-one else reuses the vmalloc
		 * area of the module.  Print a warning.
		 */
		res = probe_kernel_address(pc->name, tmp);
		if (res) {
			printk(KERN_ERR "SLAB: cache with size %d has lost its name\n", pc->buffer_size);
			continue;
		}

		if (!strcmp(pc->name, name)) {
			printk(KERN_ERR "kmem_cache_create: duplicate cache %s\n", name);
			dump_stack();
			goto oops;
		}
	}

#if DEBUG
	WARN_ON(strchr(name, ' '));	/* It confuses parsers */
#if FORCED_DEBUG
	/*
	 * Enable redzoning and last user accounting, except for caches with
	 * large objects, if the increased size would increase the object size
	 * above the next power of two: caches with object sizes just above a
	 * power of two have a significant amount of internal fragmentation.
	 */
	if (size < 4096 || fls(size - 1) == fls(size-1 + REDZONE_ALIGN + 2 * sizeof(unsigned long long)))
		flags |= SLAB_RED_ZONE | SLAB_STORE_USER;
	if (!(flags & SLAB_DESTROY_BY_RCU))
		flags |= SLAB_POISON;
#endif
	if (flags & SLAB_DESTROY_BY_RCU)
		BUG_ON(flags & SLAB_POISON);
#endif
	/*
	 * Always checks flags, a caller might be expecting debug support which
	 * isn't available.
	 */
	/* To prevent callers using the wrong flags, a CREATE_MASK is defined
	 * consisting of all the allowable flags. When a cache is being created,
	 * the requested flags are compared against the CREATE_MASK and reported
	 * as a bug if invalid flags are used.
	 */
	BUG_ON(flags & ~CREATE_MASK);

	/*
	 * Check that size is in terms of words.  This is needed to avoid
	 * unaligned accesses for some archs when redzoning is used, and makes
	 * sure any on-slab bufctl's are also correctly aligned.
	 */
	if (size & (BYTES_PER_WORD - 1)) {
		size += (BYTES_PER_WORD - 1);
		size &= ~(BYTES_PER_WORD - 1);
	}

	/* calculate the final buffer alignment: */

	/*
	 * The objects managed by the slab allocator are aligned in memory
	 * - that is, they are stored in memory cells whose initial physical
	 * addresses are multiples of a given constant, which is usually a
	 * power of 2. This constant is called the alignment factor.
	 * The largest alignment factor allowed by the slab allocator
	 * is 4,096 — the page frame size.
	 */

	/* 1) arch recommendation: can be overridden for debug */
	if (flags & SLAB_HWCACHE_ALIGN) {
		/*
		 * Default alignment: as specified by the arch code.  Except if
		 * an object is really small, then squeeze multiple objects into
		 * one cacheline.
		 */
		ralign = cache_line_size();
		while (size <= ralign / 2)
			ralign /= 2;
	} else {
		/*
		 * Usually, microcomputers access memory cells more quickly
		 * if their physical addresses are aligned with respect to
		 * the word size (that's, to the width of the internal memory
		 * bus of the computer).
		 */
		ralign = BYTES_PER_WORD;
	}

	/*
	 * Redzoning and user store require word alignment or possibly larger.
	 * Note this will be overridden by architecture or caller mandated
	 * alignment if either is greater than BYTES_PER_WORD.
	 */
	if (flags & SLAB_STORE_USER)
		ralign = BYTES_PER_WORD;

	if (flags & SLAB_RED_ZONE) {
		ralign = REDZONE_ALIGN;
		/* If redzoning, ensure that the second redzone is suitably
		 * aligned, by adjusting the object size accordingly. */
		size += REDZONE_ALIGN - 1;
		size &= ~(REDZONE_ALIGN - 1);
	}

	/* 2) arch mandated alignment */
	if (ralign < ARCH_SLAB_MINALIGN) {
		ralign = ARCH_SLAB_MINALIGN;
	}
	/* 3) caller mandated alignment */
	if (ralign < align) {
		ralign = align;
	}
	/* disable debug if necessary */
	if (ralign > __alignof__(unsigned long long))
		flags &= ~(SLAB_RED_ZONE | SLAB_STORE_USER);
	/*
	 * 4) Store it.
	 */
	align = ralign;

	if (slab_is_available())
		gfp = GFP_KERNEL;
	else
		gfp = GFP_NOWAIT;

	/* Get cache's description obj. 参见kmem_cache_zalloc()节 */
	cachep = kmem_cache_zalloc(&cache_cache, gfp);
	if (!cachep)
		goto oops;

	cachep->nodelists = (struct kmem_list3 **)&cachep->array[nr_cpu_ids];
#if DEBUG
	cachep->obj_size = size;

	/*
	 * Both debugging options require word-alignment which is calculated
	 * into align above.
	 */
	if (flags & SLAB_RED_ZONE) {
		/* add space for red zone words */
		cachep->obj_offset += sizeof(unsigned long long);
		size += 2 * sizeof(unsigned long long);
	}
	if (flags & SLAB_STORE_USER) {
		/* user store requires one word storage behind the end of
		 * the real object. But if the second red zone needs to be
		 * aligned to 64 bits, we must allow that much space.
		 */
		if (flags & SLAB_RED_ZONE)
			size += REDZONE_ALIGN;
		else
			size += BYTES_PER_WORD;
	}
#if FORCED_DEBUG && defined(CONFIG_DEBUG_PAGEALLOC)
	if (size >= malloc_sizes[INDEX_L3 + 1].cs_size &&
		 cachep->obj_size > cache_line_size() &&
		 ALIGN(size, align) < PAGE_SIZE) {
		cachep->obj_offset += PAGE_SIZE - ALIGN(size, align);
		size = PAGE_SIZE;
	}
#endif
#endif

	/*
	 * Determine if the slab management is 'on' or 'off' slab.
	 * (bootstrapping cannot cope with offslab caches so don't do
	 * it too early on. Always use on-slab management when
	 * SLAB_NOLEAKTRACE to avoid recursive calls into kmemleak)
	 */
	if ((size >= (PAGE_SIZE >> 3)) && !slab_early_init && !(flags & SLAB_NOLEAKTRACE))
		/*
		 * Size is large, assume best to place the slab management obj
		 * off-slab (should allow better packing of objs).
		 */
		flags |= CFLGS_OFF_SLAB;

	size = ALIGN(size, align);

	left_over = calculate_slab_order(cachep, size, align, flags);

	if (!cachep->num) {
		printk(KERN_ERR "kmem_cache_create: couldn't create cache %s.\n", name);
		kmem_cache_free(&cache_cache, cachep);
		cachep = NULL;
		goto oops;
	}
	slab_size = ALIGN(cachep->num * sizeof(kmem_bufctl_t) + sizeof(struct slab), align);

	/*
	 * If the slab has been placed off-slab, and we have enough space then
	 * move it on-slab. This is at the expense of any extra colouring.
	 */
	if (flags & CFLGS_OFF_SLAB && left_over >= slab_size) {
		flags &= ~CFLGS_OFF_SLAB;
		left_over -= slab_size;
	}

	if (flags & CFLGS_OFF_SLAB) {
		/* really off slab. No need for manual alignment */
		slab_size = cachep->num * sizeof(kmem_bufctl_t) + sizeof(struct slab);

#ifdef CONFIG_PAGE_POISONING
		/* If we're going to use the generic kernel_map_pages()
		 * poisoning, then it's going to smash the contents of
		 * the redzone and userword anyhow, so switch them off.
		 */
		if (size % PAGE_SIZE == 0 && flags & SLAB_POISON)
			flags &= ~(SLAB_RED_ZONE | SLAB_STORE_USER);
#endif
	}

	cachep->colour_off = cache_line_size();
	/* Offset must be a multiple of the alignment. */
	if (cachep->colour_off < align)
		cachep->colour_off = align;
	cachep->colour = left_over / cachep->colour_off;
	cachep->slab_size = slab_size;
	cachep->flags = flags;
	cachep->gfpflags = 0;
	if (CONFIG_ZONE_DMA_FLAG && (flags & SLAB_CACHE_DMA))
		cachep->gfpflags |= GFP_DMA;
	cachep->buffer_size = size;
	cachep->reciprocal_buffer_size = reciprocal_value(size);

	if (flags & CFLGS_OFF_SLAB) {
		cachep->slabp_cache = kmem_find_general_cachep(slab_size, 0u);
		/*
		 * This is a possibility for one of the malloc_sizes caches.
		 * But since we go off slab only for object size greater than
		 * PAGE_SIZE/8, and malloc_sizes gets created in ascending order,
		 * this should not happen at all.
		 * But leave a BUG_ON for some lucky dude.
		 */
		BUG_ON(ZERO_OR_NULL_PTR(cachep->slabp_cache));
	}
	cachep->ctor = ctor;
	cachep->name = name;

	// 设置cachep->array[*]
	if (setup_cpu_cache(cachep, gfp)) {
		__kmem_cache_destroy(cachep);
		cachep = NULL;
		goto oops;
	}

	if (flags & SLAB_DEBUG_OBJECTS) {
		/*
		 * Would deadlock through slab_destroy()->call_rcu()->
		 * debug_object_activate()->kmem_cache_alloc().
		 */
		WARN_ON_ONCE(flags & SLAB_DESTROY_BY_RCU);

		slab_set_debugobj_lock_classes(cachep);
	}

	/* cache setup completed, link it into the list */
	list_add(&cachep->next, &cache_chain);

oops:
	if (!cachep && (flags & SLAB_PANIC))
		panic("kmem_cache_create(): failed to create slab `%s'\n", name);
	if (slab_is_available()) {
		mutex_unlock(&cache_chain_mutex);
		put_online_cpus();
	}
	return cachep;
}
```

###### 6.5.1.1.2.1 查看slab的分配信息

调用宏KMEM_CACHE()或者函数kmem_cache_create()来创建specific cache时，若满足如下条件之一，则可以在/proc/slabinfo中显示slab的分配信息：
* 入参flags中包含SLAB_POISON, SLAB_RED_ZONE等标志，仅包含SLAB_HWCACHE_ALIGN，则不可以；
* 入参ctor不为NULL；即定义了构造函数，即使该构造函数为空函数。

使用下列命令查看slab的分配信息：

```
chenwx@chenwx ~ $ sudo cat /proc/slabinfo
slabinfo - version: 2.1
# name            <active_objs> <num_objs> <objsize> <objperslab> <pagesperslab> : tunables <limit> <batchcount> <sharedfactor> : slabdata <active_slabs> <num_slabs> <sharedavail>
UDPLITEv6              0      0   1088   15    4 : tunables    0    0    0 : slabdata      0      0      0
UDPv6                 17     30   1088   15    4 : tunables    0    0    0 : slabdata      2      2      0
tw_sock_TCPv6          0      0    256   16    1 : tunables    0    0    0 : slabdata      0      0      0
...
kmalloc-64         22167  22336     64   64    1 : tunables    0    0    0 : slabdata    349    349      0
kmalloc-32         10328  10752     32  128    1 : tunables    0    0    0 : slabdata     84     84      0
kmalloc-16          5888   5888     16  256    1 : tunables    0    0    0 : slabdata     23     23      0
kmalloc-8           5118   5120      8  512    1 : tunables    0    0    0 : slabdata     10     10      0
kmem_cache_node      192    192     64   64    1 : tunables    0    0    0 : slabdata      3      3      0
kmem_cache           112    112    256   16    1 : tunables    0    0    0 : slabdata      7      7      0

chenwx@chenwx ~ $ sudo slabtop
 Active / Total Objects (% used)    : 654908 / 679233 (96.4%)
 Active / Total Slabs (% used)      : 26620 / 26620 (100.0%)
 Active / Total Caches (% used)     : 65 / 95 (68.4%)
 Active / Total Size (% used)       : 191054.42K / 194205.16K (98.4%)
 Minimum / Average / Maximum Object : 0.01K / 0.29K / 8.00K

  OBJS ACTIVE  USE OBJ SIZE  SLABS OBJ/SLAB CACHE SIZE NAME                   
179556 173481  96%    0.10K   4604       39     18416K buffer_head
174594 174490  99%    0.19K   8314       21     33256K dentry
 94736  94736 100%    0.96K   5921       16     94736K ext4_inode_cache
 41514  30931  74%    0.04K    407      102      1628K ext4_extent_status
 31794  31187  98%    0.55K   2271       14     18168K radix_tree_node
 24570  23241  94%    0.19K   1170       21      4680K kmalloc-192
 23364  23051  98%    0.11K    649       36      2596K sysfs_dir_cache
 22656  21742  95%    0.06K    354       64      1416K kmalloc-64
 11102  11065  99%    0.57K    793       14      6344K inode_cache
 10752  10016  93%    0.03K     84      128       336K kmalloc-32
  8576   7744  90%    0.06K    134       64       536K anon_vma
  8304   7635  91%    0.25K    519       16      2076K kmalloc-256
  7225   7225 100%    0.05K     85       85       340K shared_policy_node
  5888   5888 100%    0.02K     23      256        92K kmalloc-16
  5120   5118  99%    0.01K     10      512        40K kmalloc-8
...

chenwx@chenwx ~/linux-next $ ll /sys/kernel/slab/
total 0
drwxr-xr-x 2 root root 0 Jan 19 21:43 :at-0000016
drwxr-xr-x 2 root root 0 Jan 19 21:43 :at-0000032
...
lrwxrwxrwx 1 root root 0 Jan 19 21:43 Acpi-Namespace -> :t-0000040
lrwxrwxrwx 1 root root 0 Jan 19 21:43 Acpi-Operand -> :t-0000072
lrwxrwxrwx 1 root root 0 Jan 19 21:43 Acpi-Parse -> :t-0000048
lrwxrwxrwx 1 root root 0 Jan 19 21:43 Acpi-ParseExt -> :t-0000072
lrwxrwxrwx 1 root root 0 Jan 19 21:43 Acpi-State -> :t-0000080
lrwxrwxrwx 1 root root 0 Jan 19 21:43 PING -> :t-0000896
lrwxrwxrwx 1 root root 0 Jan 19 21:43 PINGv6 -> :t-0001088
lrwxrwxrwx 1 root root 0 Jan 19 21:43 RAW -> :t-0000896
lrwxrwxrwx 1 root root 0 Jan 19 21:43 RAWv6 -> :t-0001088
...
```

若系统配置了SLUB，则可用下列命令查看系统中的slab信息：

```
chenwx@chenwx ~/linux-next/tools/vm $ grep "CONFIG_SLUB" /boot/config-3.13.0-24-generic
CONFIG_SLUB_DEBUG=y
CONFIG_SLUB=y
CONFIG_SLUB_CPU_PARTIAL=y
# CONFIG_SLUB_DEBUG_ON is not set
# CONFIG_SLUB_STATS is not set

chenwx@chenwx ~/linux-next/tools/vm $ ./slabinfo -a      

:at-0000104  <- ext4_prealloc_space buffer_head
:at-0000136  <- ext4_allocation_context ext4_groupinfo_4k
:at-0000256  <- jbd2_transaction_s dquot
:t-0000016   <- dm_mpath_io kmalloc-16 ecryptfs_file_cache
:t-0000024   <- numa_policy fsnotify_event_holder scsi_data_buffer
:t-0000032   <- ecryptfs_dentry_info_cache kmalloc-32 sd_ext_cdb inotify_event_private_data fanotify_response_event dnotify_struct
:t-0000040   <- Acpi-Namespace dm_io khugepaged_mm_slot ext4_system_zone
:t-0000048   <- shared_policy_node ksm_mm_slot ksm_stable_node fasync_cache Acpi-Parse jbd2_inode nsproxy identity ftrace_event_field ip_fib_alias
:t-0000056   <- ip_fib_trie uhci_urb_priv
:t-0000064   <- ecryptfs_key_sig_cache fib6_nodes id_kmem_cache secpath_cache dmaengine-unmap-2 kmalloc-64 tcp_bind_bucket anon_vma_chain io ksm_rmap_item fs_cache ecryptfs_global_auth_tok_cache
:t-0000072   <- ftrace_event_file Acpi-ParseExt Acpi-Operand eventpoll_pwq
:t-0000104   <- flow_cache blkdev_ioc
:t-0000112   <- sysfs_dir_cache task_delay_info fsnotify_mark blkdev_integrity
:t-0000120   <- fsnotify_event dnotify_mark inotify_inode_mark cfq_io_cq
:t-0000128   <- ecryptfs_key_tfm_cache eventpoll_epi ip6_mrt_cache kmalloc-128 scsi_sense_cache btree_node pid ip_mrt_cache uid_cache kiocb
:t-0000192   <- kmalloc-192 dmaengine-unmap-16 key_jar cred_jar inet_peer_cache vm_area_struct bio_integrity_payload ip_dst_cache file_lock_cache bio-0
:t-0000256   <- filp sgpool-8 scsi_cmd_cache skbuff_head_cache biovec-16 kmalloc-256 request_sock_TCP request_sock_TCPv6 pool_workqueue
:t-0000384   <- ip6_dst_cache blkdev_requests i915_gem_object
:t-0000512   <- skbuff_fclone_cache kmalloc-512 sgpool-16 task_xstate
:t-0000640   <- dio kioctx files_cache
:t-0000896   <- PING UNIX mm_struct ecryptfs_sb_cache RAW
:t-0001024   <- sgpool-32 kmalloc-1024 biovec-64
:t-0001088   <- signal_cache dmaengine-unmap-128 PINGv6 RAWv6
:t-0002048   <- biovec-128 sgpool-64 kmalloc-2048
:t-0002112   <- idr_layer_cache dmaengine-unmap-256
:t-0004096   <- names_cache biovec-256 ecryptfs_headers net_namespace kmalloc-4096 ecryptfs_xattr_cache sgpool-128
```

###### 6.5.1.1.2.2 如何创建和读取文件/proc/slabinfo

1) Create file /proc/slabinfo

```
slab_proc_init()
-> proc_create("slabinfo", S_IWUSR|S_IRUSR, NULL, &proc_slabinfo_operations);

static const struct file_operations proc_slabinfo_operations = {
	.open		= slabinfo_open,
	.read		= seq_read,
	.write	= slabinfo_write,
	.llseek	= seq_lseek,
	.release	= seq_release,
};
```

2) Read from /proc/slabinfo

```
proc_slabinfo_operations->open()
-> slabinfo_open()
   -> seq_open(file, &slabinfo_op);
      -> p = file->private_data;
      -> p->op = op;                    // file->private_data->op = &slabinfo_op;

static const struct seq_operations slabinfo_op = {
	.start	= s_start,
	.next		= s_next,
	.stop		= s_stop,
	.show		= s_show,
};

proc_slabinfo_operations->read()
-> seq_read()
   -> m = file->private_data;
   -> m->op->start(m, &pos);		// slabinfo_op->start => s_start()
   -> m->op->show(m, p);		// slabinfo_op->show  => s_show()
   -> m->op->next(m, p, &pos);		// slabinfo_op->next  => s_next()
   -> m->op->stop(m, p);		// slabinfo_op->stop  => s_stop()
   -> ... loop again ...

proc_slabinfo_operations->close()
-> seq_release()
   -> m = file->private_data;
   -> kfree(m->buf);
   -> kfree(m);
```

##### 6.5.1.1.3 Allocate an object from Specific Cache

###### 6.5.1.1.3.1 kmem_cache_zalloc()

该函数的调用关系如下：

```
kmem_cache_zalloc(&cache_cache, gfp)
-> kmem_cache_alloc(k, flags | __GFP_ZERO)		// 参见6.5.1.1.3.2 kmem_cache_alloc()节
   -> __cache_alloc(cachep, flags, ..)
      -> __do_cache_alloc()
         -> ____cache_alloc()
            -> cache_alloc_refill()
               -> cache_grow()
                  -> kmem_getpages()
                     -> alloc_pages_exact_node()
                        -> __alloc_pages()		// 参见alloc_pages()节
```

该函数定义于include/linux/slab.h:

```
static inline void *kmem_cache_zalloc(struct kmem_cache *k, gfp_t flags)
{
	// 参见6.5.1.1.3.2 kmem_cache_alloc()节
	return kmem_cache_alloc(k, flags | __GFP_ZERO);
}
```

###### 6.5.1.1.3.2 kmem_cache_alloc()

该函数定义于mm/slab.c:

```
/**
 * kmem_cache_alloc - Allocate an object
 * @cachep: The cache to allocate from.
 * @flags: See kmalloc().
 *
 * Allocate an object from this cache.  The flags are only relevant
 * if the cache has no available objects.
 */
void *kmem_cache_alloc(struct kmem_cache *cachep, gfp_t flags)
{
	void *ret = __cache_alloc(cachep, flags, __builtin_return_address(0));

	trace_kmem_cache_alloc(_RET_IP_, ret, obj_size(cachep), cachep->buffer_size, flags);

	return ret;
}
```

其中，函数__cache_alloc()定义于mm/slab.c:

```
static __always_inline void *__cache_alloc(struct kmem_cache *cachep, gfp_t flags, void *caller)
{
	unsigned long save_flags;
	void *objp;

	flags &= gfp_allowed_mask;

	lockdep_trace_alloc(flags);

	if (slab_should_failslab(cachep, flags))
		return NULL;

	cache_alloc_debugcheck_before(cachep, flags);
	local_irq_save(save_flags);
	objp = __do_cache_alloc(cachep, flags);
	local_irq_restore(save_flags);
	objp = cache_alloc_debugcheck_after(cachep, flags, objp, caller);
	kmemleak_alloc_recursive(objp, obj_size(cachep), 1, cachep->flags, flags);
	prefetchw(objp);

	if (likely(objp))
		kmemcheck_slab_alloc(cachep, flags, objp, obj_size(cachep));

	if (unlikely((flags & __GFP_ZERO) && objp))
		memset(objp, 0, obj_size(cachep));

	return objp;
}
```

其中，函数__do_cache_alloc()定义于mm/slab.c:

```
#ifdef CONFIG_NUMA
static __always_inline void *__do_cache_alloc(struct kmem_cache *cache, gfp_t flags)
{
	void *objp;

	if (unlikely(current->flags & (PF_SPREAD_SLAB | PF_MEMPOLICY))) {
		objp = alternate_node_alloc(cache, flags);
		if (objp)
			goto out;
	}
	objp = ____cache_alloc(cache, flags);

	/*
	 * We may just have run out of memory on the local node.
	 * ____cache_alloc_node() knows how to locate memory on other nodes
	 */
	if (!objp)
		objp = ____cache_alloc_node(cache, flags, numa_mem_id());

  out:
	return objp;
}

#else

static __always_inline void *__do_cache_alloc(struct kmem_cache *cachep, gfp_t flags)
{
	return ____cache_alloc(cachep, flags);
}

#endif /* CONFIG_NUMA */
```

其中，函数____cache_alloc()定义于mm/slab.c:

```
static inline void *____cache_alloc(struct kmem_cache *cachep, gfp_t flags)
{
	void *objp;
	struct array_cache *ac;

	check_irq_off();

	// ac = cachep->array[smp_processor_id()];
	ac = cpu_cache_get(cachep);
	if (likely(ac->avail)) {
		STATS_INC_ALLOCHIT(cachep);
		ac->touched = 1;
		/*
		 * The avail field contains the index in the local cache
		 * of the entry that points to the last freed object.
		 */
		objp = ac->entry[--ac->avail];
	} else {
		STATS_INC_ALLOCMISS(cachep);
		// 参见cache_alloc_refill()节
		objp = cache_alloc_refill(cachep, flags);
		/*
		 * the 'ac' may be updated by cache_alloc_refill(),
		 * and kmemleak_erase() requires its correct value.
		 */
		// ac = cachep->array[smp_processor_id()];
		ac = cpu_cache_get(cachep);
	}
	/*
	 * To avoid a false negative, if an object that is in one of the
	 * per-CPU caches is leaked, we need to make sure kmemleak doesn't
	 * treat the array pointers as a reference to the object.
	 */
	if (objp)
		kmemleak_erase(&ac->entry[ac->avail]);
	return objp;
}
```

###### 6.5.1.1.3.2.1 cache_alloc_refill()

该函数定义于mm/slab.c:

```
static void *cache_alloc_refill(struct kmem_cache *cachep, gfp_t flags)
{
	int batchcount;
	struct kmem_list3 *l3;
	struct array_cache *ac;
	int node;

retry:
	check_irq_off();
	node = numa_mem_id();
	ac = cpu_cache_get(cachep);
	batchcount = ac->batchcount;
	if (!ac->touched && batchcount > BATCHREFILL_LIMIT) {
		/*
		 * If there was little recent activity on this cache, then
		 * perform only a partial refill.  Otherwise we could generate
		 * refill bouncing.
		 */
		batchcount = BATCHREFILL_LIMIT;
	}
	l3 = cachep->nodelists[node];

	BUG_ON(ac->avail > 0 || !l3);
	spin_lock(&l3->list_lock);

	/* See if we can refill from the shared array */
	if (l3->shared && transfer_objects(ac, l3->shared, batchcount)) {
		l3->shared->touched = 1;
		goto alloc_done;
	}

	while (batchcount > 0) {
		struct list_head *entry;
		struct slab *slabp;
		/* Get slab alloc is to come from. */
		// 1) Get slab alloc from ->slabs_parial by default;
		entry = l3->slabs_partial.next;
		// 2) Get slab alloc from ->slabs_free is ->slabs_parial is empty;
		if (entry == &l3->slabs_partial) {
			l3->free_touched = 1;
			entry = l3->slabs_free.next;
			// 3) Alloc new slab even if ->slabs_free is empty.
			if (entry == &l3->slabs_free)
				goto must_grow;
		}

		slabp = list_entry(entry, struct slab, list);
		check_slabp(cachep, slabp);
		check_spinlock_acquired(cachep);

		/*
		 * The slab was either on partial or free list so
		 * there must be at least one object available for
		 * allocation.
		 */
		BUG_ON(slabp->inuse >= cachep->num);

		while (slabp->inuse < cachep->num && batchcount--) {
			STATS_INC_ALLOCED(cachep);
			STATS_INC_ACTIVE(cachep);
			STATS_SET_HIGH(cachep);

			// 参见slab_get_obj()节
			ac->entry[ac->avail++] = slab_get_obj(cachep, slabp, node);
		}
		check_slabp(cachep, slabp);

		/* move slabp to correct slabp list: */
		list_del(&slabp->list);
		if (slabp->free == BUFCTL_END)
			list_add(&slabp->list, &l3->slabs_full);
		else
			list_add(&slabp->list, &l3->slabs_partial);
	}

must_grow:
	l3->free_objects -= ac->avail;
alloc_done:
	spin_unlock(&l3->list_lock);

	if (unlikely(!ac->avail)) {
		int x;
		// 参见cache_grow()节
		x = cache_grow(cachep, flags | GFP_THISNODE, node, NULL);

		/* cache_grow can reenable interrupts, then ac could change. */
		ac = cpu_cache_get(cachep);
		if (!x && ac->avail == 0)	/* no objects in sight? abort */
			return NULL;

		if (!ac->avail)		/* objects refilled by interrupt? */
			goto retry;
	}
	ac->touched = 1;
	return ac->entry[--ac->avail];
}
```

###### 6.5.1.1.3.2.1.1 slab_get_obj()

该函数定义于mm/slab.c:

```
static void *slab_get_obj(struct kmem_cache *cachep, struct slab *slabp, int nodeid)
{
	// objp = slabp->s_mem + cachep->buffer_size * slabp->free;
	void *objp = index_to_obj(cachep, slabp, slabp->free);
	kmem_bufctl_t next;

	slabp->inuse++;
	// next = (kmem_bufctl_t *)(slabp + 1)[slabp->free];
	next = slab_bufctl(slabp)[slabp->free];
#if DEBUG
	slab_bufctl(slabp)[slabp->free] = BUFCTL_FREE;
	WARN_ON(slabp->nodeid != nodeid);
#endif
	slabp->free = next;

	return objp;
}
```

###### 6.5.1.1.3.2.2 cache_grow()

该函数定义于mm/slab.c:

```
/*
 * Grow (by 1) the number of slabs within a cache.  This is called by
 * kmem_cache_alloc() when there are no active objs left in a cache.
 */
static int cache_grow(struct kmem_cache *cachep, gfp_t flags, int nodeid, void *objp)
{
	struct slab *slabp;
	size_t offset;
	gfp_t local_flags;
	struct kmem_list3 *l3;

	/*
	 * Be lazy and only check for valid flags here,  keeping it out of the
	 * critical path in kmem_cache_alloc().
	 */
	BUG_ON(flags & GFP_SLAB_BUG_MASK);
	local_flags = flags & (GFP_CONSTRAINT_MASK|GFP_RECLAIM_MASK);

	/* Take the l3 list lock to change the colour_next on this node */
	check_irq_off();
	l3 = cachep->nodelists[nodeid];
	spin_lock(&l3->list_lock);

	/* Get colour for the slab, and cal the next value. */
	offset = l3->colour_next;
	l3->colour_next++;
	if (l3->colour_next >= cachep->colour)
		l3->colour_next = 0;
	spin_unlock(&l3->list_lock);

	offset *= cachep->colour_off;

	if (local_flags & __GFP_WAIT)
		local_irq_enable();

	/*
	 * The test for missing atomic flag is performed here, rather than
	 * the more obvious place, simply to reduce the critical path length
	 * in kmem_cache_alloc(). If a caller is seriously mis-behaving they
	 * will eventually be caught here (where it matters).
	 */
	kmem_flagcheck(cachep, flags);

	/*
	 * Get mem for the objs.  Attempt to allocate a physical page from 'nodeid'.
	 */
	if (!objp)
		objp = kmem_getpages(cachep, local_flags, nodeid);	// 参见kmem_getpages()节
	if (!objp)
		goto failed;

	/* Get slab management. */
	slabp = alloc_slabmgmt(cachep, objp, offset, local_flags & ~GFP_CONSTRAINT_MASK, nodeid);
	if (!slabp)
		goto opps1;

	slab_map_pages(cachep, slabp, objp);

	// Applies the constructor method (if defined)
	// to all the objects contained in the new slab.
	cache_init_objs(cachep, slabp);

	if (local_flags & __GFP_WAIT)
		local_irq_disable();
	check_irq_off();
	spin_lock(&l3->list_lock);

	/* Make slab active. */
	// Add the newly obtained slab descriptor at the end
	// of the fully free slab list of the cache descriptor.
	list_add_tail(&slabp->list, &(l3->slabs_free));
	STATS_INC_GROWN(cachep);
	l3->free_objects += cachep->num;
	spin_unlock(&l3->list_lock);
	return 1;

opps1:
	kmem_freepages(cachep, objp);
failed:
	if (local_flags & __GFP_WAIT)
		local_irq_disable();
	return 0;
}
```

###### 6.5.1.1.3.2.2.1 kmem_getpages()

The method obtains from the zoned page frame allocator the group of page frames needed to store a single slab.

该函数定义于mm/slab.c:

```
/*
 * Interface to system's page allocator. No need to hold the cache-lock.
 *
 * If we requested dmaable memory, we will get it. Even if we
 * did not request dmaable memory, we might get it, but that
 * would be relatively rare and ignorable.
 */
static void *kmem_getpages(struct kmem_cache *cachep, gfp_t flags, int nodeid)
{
	struct page *page;
	int nr_pages;
	int i;

#ifndef CONFIG_MMU
	/*
	 * Nommu uses slab's for process anonymous memory allocations, and thus
	 * requires __GFP_COMP to properly refcount higher order allocations
	 */
	flags |= __GFP_COMP;
#endif

	flags |= cachep->gfpflags;
	if (cachep->flags & SLAB_RECLAIM_ACCOUNT)
		flags |= __GFP_RECLAIMABLE;

	// 通过调用__alloc_pages()分配2cachep->gfporder个连续物理页面，参见alloc_pages()节
	page = alloc_pages_exact_node(nodeid, flags | __GFP_NOTRACK, cachep->gfporder);
	if (!page)
		return NULL;

	nr_pages = (1 << cachep->gfporder);
	if (cachep->flags & SLAB_RECLAIM_ACCOUNT)
		add_zone_page_state(page_zone(page), NR_SLAB_RECLAIMABLE, nr_pages);
	else
		add_zone_page_state(page_zone(page), NR_SLAB_UNRECLAIMABLE, nr_pages);
	for (i = 0; i < nr_pages; i++)
		__SetPageSlab(page + i);	// 设置page->flags中的标志位PG_slab

	if (kmemcheck_enabled && !(cachep->flags & SLAB_NOTRACK)) {
		kmemcheck_alloc_shadow(page, cachep->gfporder, flags, nodeid);

		if (cachep->ctor)
			kmemcheck_mark_uninitialized_pages(page, nr_pages);
		else
			kmemcheck_mark_unallocated_pages(page, nr_pages);
	}

	return page_address(page);
}
```

###### 6.5.1.1.3.2.2.2 alloc_slabmgmt()

该函数定义于mm/slab.c:

```
/*
 * Get the memory for a slab management obj.
 * For a slab cache when the slab descriptor is off-slab, slab descriptors
 * always come from malloc_sizes caches.  The slab descriptor cannot
 * come from the same cache which is getting created because,
 * when we are searching for an appropriate cache for these
 * descriptors in kmem_cache_create, we search through the malloc_sizes array.
 * If we are creating a malloc_sizes cache here it would not be visible to
 * kmem_find_general_cachep till the initialization is complete.
 * Hence we cannot have slabp_cache same as the original cache.
 */
static struct slab *alloc_slabmgmt(struct kmem_cache *cachep, void *objp,
				   int colour_off, gfp_t local_flags, int nodeid)
{
	struct slab *slabp;

	/*
	 * 检测cachep->flags中的标志位CFLGS_OFF_SLAB:
	 * If the CFLGS_OFF_SLAB flag of the cache descriptor is set,
	 * the slab descriptor is allocated from the general cache
	 * pointed to by the slabp_cache field of the cache descriptor;
	 * Otherwise, the slab descriptor is allocated in the first
	 * page frame of the slab.
	 */
	if (OFF_SLAB(cachep)) {
		/* Slab management obj is off-slab. */
		/*
		 * 通过调用kmem_cache_alloc(cachep, flags)来分配object，
		 * 参见kmem_cache_zalloc()节
		 */
		slabp = kmem_cache_alloc_node(cachep->slabp_cache, local_flags, nodeid);
		/*
		 * If the first object in the slab is leaked (it's allocated
		 * but no one has a reference to it), we want to make sure
		 * kmemleak does not treat the ->s_mem pointer as a reference
		 * to the object. Otherwise we will not report the leak.
		 */
		kmemleak_scan_area(&slabp->list, sizeof(struct list_head), local_flags);
		if (!slabp)
			return NULL;
	} else {
		slabp = objp + colour_off;
		colour_off += cachep->slab_size;
	}
	slabp->inuse = 0;
	slabp->colouroff = colour_off;
	slabp->s_mem = objp + colour_off;
	slabp->nodeid = nodeid;
	slabp->free = 0;
	return slabp;
}
```

###### 6.5.1.1.3.2.2.3 slab_map_pages()

The kernel must be able to determine, given a page frame, whether it is used by the slab allocator and, if so, to derive quickly the addresses of the corresponding cache and slab descriptors. Therefore, slab_map_pages() scans all page descriptors of the page frames assigned to the new slab, and loads the next and prev subfields of the lru fields in the page descriptors with the addresses of, respectively, the cache descriptor and the slab descriptor. This works correctly because the lru field is used by functions of the buddy system only when the page frame is free, while page frames handled by the slab allocator functions have the PG_slab flag set and are not free as far as the buddy allocator system is concerned.

该函数定义于mm/slab.c:

```
/*
 * Map pages beginning at addr to the given cache and slab. This is required
 * for the slab allocator to be able to lookup the cache and slab of a
 * virtual address for kfree, ksize, and slab debugging.
 */
static void slab_map_pages(struct kmem_cache *cache, struct slab *slab, void *addr)
{
	int nr_pages;
	struct page *page;

	page = virt_to_page(addr);

	nr_pages = 1;
	if (likely(!PageCompound(page)))
		nr_pages <<= cache->gfporder;

	do {
		// page->lru.next = (struct list_head *)cache;
		page_set_cache(page, cache);
		// page->lru.prev = (struct list_head *)slab;
		page_set_slab(page, slab);
		page++;
	} while (--nr_pages);
}
```

##### 6.5.1.1.4 Deallocate an object to Specific Cache/kmem_cache_free()

该函数定义于mm/slab.c:

```
/**
 * kmem_cache_free - Deallocate an object
 * @cachep: The cache the allocation was from.
 * @objp: The previously allocated object.
 *
 * Free an object which was previously allocated from this
 * cache.
 */
void kmem_cache_free(struct kmem_cache *cachep, void *objp)
{
	unsigned long flags;

	local_irq_save(flags);
	debug_check_no_locks_freed(objp, obj_size(cachep));
	if (!(cachep->flags & SLAB_DEBUG_OBJECTS))
		debug_check_no_obj_freed(objp, obj_size(cachep));
	__cache_free(cachep, objp, __builtin_return_address(0));
	local_irq_restore(flags);

	trace_kmem_cache_free(_RET_IP_, objp);
}
```

##### 6.5.1.1.5 Destroy a Specific Cache/kmem_cache_destroy()

该函数定义于mm/slab.c:

```
/**
 * kmem_cache_destroy - delete a cache
 * @cachep: the cache to destroy
 *
 * Remove a &struct kmem_cache object from the slab cache.
 *
 * It is expected this function will be called by a module when it is
 * unloaded.  This will remove the cache completely, and avoid a duplicate
 * cache being allocated each time a module is loaded and unloaded, if the
 * module doesn't have persistent in-kernel storage across loads and unloads.
 *
 * The cache must be empty before calling this function.
 *
 * The caller must guarantee that no one will allocate memory from the cache
 * during the kmem_cache_destroy().
 */
void kmem_cache_destroy(struct kmem_cache *cachep)
{
	BUG_ON(!cachep || in_interrupt());

	/* Find the cache in the chain of caches. */
	get_online_cpus();
	mutex_lock(&cache_chain_mutex);
	/*
	 * the chain is never empty, cache_cache is never destroyed
	 */
	list_del(&cachep->next);
	// 参见__cache_shrink()节
	if (__cache_shrink(cachep)) {
		slab_error(cachep, "Can't free all objects");
		list_add(&cachep->next, &cache_chain);
		mutex_unlock(&cache_chain_mutex);
		put_online_cpus();
		return;
	}

	if (unlikely(cachep->flags & SLAB_DESTROY_BY_RCU))
		rcu_barrier();

	// 参见__kmem_cache_destroy()节
	__kmem_cache_destroy(cachep);
	mutex_unlock(&cache_chain_mutex);
	put_online_cpus();
}
```

###### 6.5.1.1.5.1 \__cache_shrink()

该函数定义于mm/slab.c:

```
/* Called with cache_chain_mutex held to protect against cpu hotplug */
static int __cache_shrink(struct kmem_cache *cachep)
{
	int ret = 0, i = 0;
	struct kmem_list3 *l3;

	drain_cpu_caches(cachep);

	check_irq_on();
	for_each_online_node(i) {
		l3 = cachep->nodelists[i];
		if (!l3)
			continue;

		drain_freelist(cachep, l3, l3->free_objects);

		ret += !list_empty(&l3->slabs_full) || !list_empty(&l3->slabs_partial);
	}
	return (ret ? 1 : 0);		// cachep中是否还存在空闲slabs
}
```

###### 6.5.1.1.5.2 \__kmem_cache_destroy()

该函数定义于mm/slab.c:

```
static void __kmem_cache_destroy(struct kmem_cache *cachep)
{
	int i;
	struct kmem_list3 *l3;

	for_each_online_cpu(i)
	    kfree(cachep->array[i]);

	/* NUMA: free the list3 structures */
	for_each_online_node(i) {
		l3 = cachep->nodelists[i];
		if (l3) {
			kfree(l3->shared);
			free_alien_cache(l3->alien);
			kfree(l3);
		}
	}
	kmem_cache_free(&cache_cache, cachep);
}
```

### 6.5.2 Slab Descriptor/struct slab

该结构定义于mm/slab.c:

```
struct slab {
	union {
		struct {
			/*
			 * Pointers for one of the three doubly linked list of slab
			 * descriptors (either the slabs_full, slabs_partial, or slabs_free
			 * list in the kmem_list3 structure of the cache descriptor)
			 */
			struct list_head	list;

			// Offset of the first object in the slab.
			// The address of the first object is s_mem + colouroff.
			unsigned long		colouroff;

			// Address of first object (either allocated or free) in the slab.
			void			*s_mem;	/* including colour offset */

			// Number of objects in the slab that are currently used (not free).
			unsigned int		inuse;	/* num of objs active in slab */

			// Index of next free object in the slab, or BUFCTL_END
			// if there are no free objects left.
			kmem_bufctl_t		free;

			unsigned short		nodeid;
		};
		struct slab_rcu			__slab_cover_slab_rcu;
	};
};
```

Slab descriptors can be stored in two possible places:

1) External slab descriptor: Stored outside the slab, in one of the general caches not suitable for ISA DMA pointed to by cache_sizes.

2) Internal slab descriptor: Stored inside the slab, at the beginning of the first page frame assigned to the slab.

The slab allocator chooses the second solution when the size of the objects is smaller than 512MB or when internal fragmentation leaves enough space for the slab descriptor and the object descriptor inside the slab. The CFLGS_OFF_SLAB flag in the flags field of the cache descriptor is set to one if the slab descriptor is stored outside the slab; it is set to zero otherwise. 参见alloc_slabmgmt()节中的alloc_slabmgmt().

### 6.5.3 Object Descriptor/kmem_bufctl_t

该结构定义于mm/slab.c：

```
typedef unsigned int kmem_bufctl_t;

#define BUFCTL_END	(((kmem_bufctl_t)(~0U))-0)		// 0xFFFF
#define BUFCTL_FREE	(((kmem_bufctl_t)(~0U))-1)		// 0xFFFE
#define BUFCTL_ACTIVE	(((kmem_bufctl_t)(~0U))-2)		// 0xFFFD
#define SLAB_LIMIT	(((kmem_bufctl_t)(~0U))-3)		// 0xFFFC
```

Each object has a short descriptor of type kmem_bufctl_t. Object descriptors are stored in an array placed right after the corresponding slab descriptor. Thus, like the slab descriptors themselves, the object descriptors of a slab can be stored in two possible ways:

1) External object descriptors

Stored outside the slab, in the general cache pointed to by the slabp_cache field of the cache descriptor. The size of the memory area, and thus the particular general cache used to store object descriptors, depends on the number of objects stored in the slab (num field of the cache descriptor).

![Slab_with_External_Descriptors](/assets/Slab_with_External_Descriptors.png)

2) Internal object descriptors

Stored inside the slab, right before the objects they describe.

![Slab_with_Internal_Descriptors](/assets/Slab_with_Internal_Descriptors.png)

## 6.6 分配/释放内存区域(memory area)

### 6.6.1 Allocate Physically Contiguous Memory

#### 6.6.1.1 kzalloc()/kmalloc()

该函数定义于include/linux/slab.h:

```
/**
 * kzalloc - allocate memory. The memory is set to zero.
 * @size: how many bytes of memory are required.
 * @flags: the type of memory to allocate (see kmalloc).
 */
static inline void *kzalloc(size_t size, gfp_t flags)
{
	return kmalloc(size, flags | __GFP_ZERO);
}
```

函数kmalloc()定义于include/linux/slab_def.h:

```
static __always_inline void *kmalloc(size_t size, gfp_t flags)
{
	struct kmem_cache *cachep;
	void *ret;

	/*
	 * GCC buitin function __builtin_constant_p():
	 * returns the integer 1 if the argument is known
	 * to be a compiletime constant and 0 if it is not
	 * known to be a compile-time constant.
	 */
	if (__builtin_constant_p(size)) {
		int i = 0;

		if (!size)
			return ZERO_SIZE_PTR;

		/*
		 * Use the malloc_sizes table to locate the
		 * nearest power-of-2 size to the requested size.
		 */
#define CACHE(x)				\
		if (size <= x)			\
			goto found;		\
		else				\
			i++;
#include <linux/kmalloc_sizes.h>
#undef CACHE

		return NULL;

found:
#ifdef CONFIG_ZONE_DMA
		if (flags & GFP_DMA)
			cachep = malloc_sizes[i].cs_dmacachep;
		else
#endif
			cachep = malloc_sizes[i].cs_cachep;

		// 参见kmem_cache_alloc_trace()节
		ret = kmem_cache_alloc_trace(size, cachep, flags);

		return ret;
	}

	// 参见__kmalloc()节
	return __kmalloc(size, flags);
}
```

##### 6.6.1.1.1 kmem_cache_alloc_trace()

该函数定义于include/linux/slab_def.h:

```
#ifdef CONFIG_TRACING
extern void *kmem_cache_alloc_trace(size_t size, struct kmem_cache *cachep, gfp_t flags);
#else
static __always_inline void *kmem_cache_alloc_trace(size_t size, struct kmem_cache *cachep, gfp_t flags)
{
	// 参见6.5.1.1.3.1 kmem_cache_zalloc()节
	return kmem_cache_alloc(cachep, flags);
}
#endif
```

##### 6.6.1.1.2 \__kmalloc()

该函数定义于mm/slab.c:

```
#if defined(CONFIG_DEBUG_SLAB) || defined(CONFIG_TRACING)
void *__kmalloc(size_t size, gfp_t flags)
{
	return __do_kmalloc(size, flags, __builtin_return_address(0));
}
#else
void *__kmalloc(size_t size, gfp_t flags)
{
	return __do_kmalloc(size, flags, NULL);
}
#endif
```

#### 6.6.1.2 kcalloc()

该函数定义于include/linux/slab.h:

```
/**
 * kcalloc - allocate memory for an array. The memory is set to zero.
 * @n: number of elements.
 * @size: element size.
 * @flags: the type of memory to allocate.
 */
static inline void *kcalloc(size_t n, size_t size, gfp_t flags)
{
	if (size != 0 && n > ULONG_MAX / size)
		return NULL;

	// 参见__kmalloc()节
	return __kmalloc(n * size, flags | __GFP_ZERO);
}
```

#### 6.6.1.3 kfree()

该函数定义于mm/slab.c:

```
/**
 * kfree - free previously allocated memory
 * @objp: pointer returned by kmalloc.
 *
 * If @objp is NULL, no operation is performed.
 *
 * Don't free memory not originally allocated by kmalloc()
 * or you will run into trouble.
 */
void kfree(const void *objp)
{
	struct kmem_cache *c;
	unsigned long flags;

	trace_kfree(_RET_IP_, objp);

	if (unlikely(ZERO_OR_NULL_PTR(objp)))
		return;
	local_irq_save(flags);
	kfree_debugcheck(objp);
	// 参见virt_to_cache()节
	c = virt_to_cache(objp);
	debug_check_no_locks_freed(objp, obj_size(c));
	debug_check_no_obj_freed(objp, obj_size(c));
	__cache_free(c, (void *)objp, __builtin_return_address(0));
	local_irq_restore(flags);
}
```

##### 6.6.1.3.1 virt_to_cache()

该函数定义于mm/slab.c:

```
static inline struct kmem_cache *virt_to_cache(const void *obj)
{
	// page = virt_to_page(obj)->first_page
	struct page *page = virt_to_head_page(obj);
	// (struct slab *)page->lru.prev; 参见slab_map_pages()节
	return page_get_cache(page);
}
```

### 6.6.2 Allocate Virtually Contiguous Memory

#### 6.6.2.1 vzalloc()/vmalloc()

函数vzalloc()定义于mm/vmalloc.c:

```
/**
 *	vzalloc - allocate virtually contiguous memory with zero fill
 *	@size:	allocation size
 *	Allocate enough pages to cover @size from the page level
 *	allocator and map them into contiguous kernel virtual space.
 *	The memory allocated is set to zero.
 *
 *	For tight control over page level allocator and protection flags
 *	use __vmalloc() instead.
 */
void *vzalloc(unsigned long size)
{
	return __vmalloc_node_flags(size, -1, GFP_KERNEL | __GFP_HIGHMEM | __GFP_ZERO);
}
```

函数vmalloc()定义于mm/vmalloc.c:

```
/**
 *	vmalloc  -  allocate virtually contiguous memory
 *	@size:		allocation size
 *	Allocate enough pages to cover @size from the page level
 *	allocator and map them into contiguous kernel virtual space.
 *
 *	For tight control over page level allocator and protection flags
 *	use __vmalloc() instead.
 */
void *vmalloc(unsigned long size)
{
	return __vmalloc_node_flags(size, -1, GFP_KERNEL | __GFP_HIGHMEM);
}
```

其中，函数__vmalloc_node_flags()定义于mm/vmalloc.c:

```
static inline void *__vmalloc_node_flags(unsigned long size, int node, gfp_t flags)
{
	return __vmalloc_node(size, 1, flags, PAGE_KERNEL, node, __builtin_return_address(0));
}
```

其中，函数__vmalloc_node()定义于mm/vmalloc.c:

```
/**
 *	__vmalloc_node  -  allocate virtually contiguous memory
 *	@size:		allocation size
 *	@align:		desired alignment
 *	@gfp_mask:	flags for the page level allocator
 *	@prot:		protection mask for the allocated pages
 *	@node:		node to use for allocation or -1
 *	@caller:	caller's return address
 *
 *	Allocate enough pages to cover @size from the page level
 *	allocator with @gfp_mask flags.  Map them into contiguous
 *	kernel virtual space, using a pagetable protection of @prot.
 */
static void *__vmalloc_node(unsigned long size, unsigned long align,
			    gfp_t gfp_mask, pgprot_t prot, int node, void *caller)
{
	/*
	 * 函数vmalloc()从区间[VMALLOC_START, VMALLOC_END]中分配内存空间，
	 * 参见__vmalloc_node_range()节
	 */
	return __vmalloc_node_range(size, align, VMALLOC_START, VMALLOC_END,
					gfp_mask, prot, node, caller);
}
```

##### 6.6.2.1.1 \__vmalloc_node_range()

该函数定义于mm/vmalloc.c:

```
/**
 *	__vmalloc_node_range  -  allocate virtually contiguous memory
 *	@size:		allocation size
 *	@align:		desired alignment
 *	@start:		vm area range start
 *	@end:		vm area range end
 *	@gfp_mask:	flags for the page level allocator
 *	@prot:		protection mask for the allocated pages
 *	@node:		node to use for allocation or -1
 *	@caller:	caller's return address
 *
 *	Allocate enough pages to cover @size from the page level
 *	allocator with @gfp_mask flags.  Map them into contiguous
 *	kernel virtual space, using a pagetable protection of @prot.
 */
void *__vmalloc_node_range(unsigned long size, unsigned long align,
			unsigned long start, unsigned long end, gfp_t gfp_mask,
			pgprot_t prot, int node, void *caller)
{
	struct vm_struct *area;
	void *addr;
	unsigned long real_size = size;

	/*
	 * Round up the value of the size to a multiple of 4,096
	 * (the page frame size); The main advantage of this schema
	 * is to avoid external fragmentation, while the disadvantage
	 * is that it is necessary to fiddle with the kernel Page
	 * Tables. Clearly, the size of a noncontiguous memory area
	 * must be a multiple of 4,096.
	 */
	size = PAGE_ALIGN(size);
	if (!size || (size >> PAGE_SHIFT) > totalram_pages)
		goto fail;

	// 参见__get_vm_area_node()节
	area = __get_vm_area_node(size, align, VM_ALLOC | VM_UNLIST,
				  start, end, node, gfp_mask, caller);
	if (!area)
		goto fail;

	// 参见__vmalloc_area_node()节
	addr = __vmalloc_area_node(area, gfp_mask, prot, node, caller);
	if (!addr)
		return NULL;

	/*
	 * In this function, newly allocated vm_struct is not added
	 * to vmlist at __get_vm_area_node(). so, it is added here.
	 */
	// 参见insert_vmalloc_vmlist()节
	insert_vmalloc_vmlist(area);

	/*
	 * A ref_count = 3 is needed because the vm_struct and vmap_area
	 * structures allocated in the __get_vm_area_node() function contain
	 * references to the virtual address of the vmalloc'ed block.
	 */
	kmemleak_alloc(addr, real_size, 3, gfp_mask);

	return addr;

fail:
	warn_alloc_failed(gfp_mask, 0, "vmalloc: allocation failure: %lu bytes\n", real_size);
	return NULL;
}
```

函数vmalloc()的返回结果addr:

![Memery_Layout_23](/assets/Memery_Layout_23.jpg)

###### 6.6.2.1.1.1 \__get_vm_area_node()

该函数定义于mm/vmalloc.c:

```
static struct vm_struct *__get_vm_area_node(unsigned long size,
		unsigned long align, unsigned long flags, unsigned long start,
		unsigned long end, int node, gfp_t gfp_mask, void *caller)
{
	struct vmap_area *va;
	struct vm_struct *area;

	BUG_ON(in_interrupt());
	if (flags & VM_IOREMAP) {
		int bit = fls(size);

		if (bit > IOREMAP_MAX_ORDER)
			bit = IOREMAP_MAX_ORDER;
		else if (bit < PAGE_SHIFT)
			bit = PAGE_SHIFT;

		align = 1ul << bit;
	}

	size = PAGE_ALIGN(size);
	if (unlikely(!size))
		return NULL;

	// 参见kzalloc_node()节
	area = kzalloc_node(sizeof(*area), gfp_mask & GFP_RECLAIM_MASK, node);
	if (unlikely(!area))
		return NULL;

	/*
	 * We always allocate a guard page.
	 */
	size += PAGE_SIZE;

	// 参见alloc_vmap_area()节
	va = alloc_vmap_area(size, align, start, end, node, gfp_mask);
	if (IS_ERR(va)) {
		kfree(area);
		return NULL;
	}

	/*
	 * When this function is called from __vmalloc_node_range,
	 * we do not add vm_struct to vmlist here to avoid
	 * accessing uninitialized members of vm_struct such as
	 * pages and nr_pages fields. They will be set later.
	 * To distinguish it from others, we use a VM_UNLIST flag.
	 */
	if (flags & VM_UNLIST)
		setup_vmalloc_vm(area, va, flags, caller);	// 参见setup_vmalloc_vm()节
	else
		insert_vmalloc_vm(area, va, flags, caller);

	return area;
}
```

###### 6.6.2.1.1.1.1 kzalloc_node()

该函数定义于mm/vmalloc.c:

```
/**
 * kzalloc_node - allocate zeroed memory from a particular memory node.
 * @size: how many bytes of memory are required.
 * @flags: the type of memory to allocate (see kmalloc).
 * @node: memory node from which to allocate
 */
static inline void *kzalloc_node(size_t size, gfp_t flags, int node)
{
	/*
	 * Invoke kmalloc() to request a group of contiguous
	 * page frames large enough to contain an array of page
	 * descriptor pointers. 参见kzalloc()/kmalloc()节
	 */
	return kmalloc_node(size, flags | __GFP_ZERO, node);
}
```

###### 6.6.2.1.1.1.2 alloc_vmap_area()

该函数定义于mm/vmalloc.c:

```
/*
 * Allocate a region of KVA of the specified size and alignment, within the
 * vstart and vend.
 */
static struct vmap_area *alloc_vmap_area(unsigned long size, unsigned long align,
				unsigned long vstart, unsigned long vend, int node, gfp_t gfp_mask)
{
	struct vmap_area *va;
	struct rb_node *n;
	unsigned long addr;
	int purged = 0;
	struct vmap_area *first;

	BUG_ON(!size);
	BUG_ON(size & ~PAGE_MASK);
	BUG_ON(!is_power_of_2(align));

	/*
	 * Invoke kmalloc() to request a group of contiguous
	 * page frames large enough to contain an array of
	 * page descriptor pointers. 参见kzalloc()/kmalloc()节
	 */
	va = kmalloc_node(sizeof(struct vmap_area), gfp_mask & GFP_RECLAIM_MASK, node);
	if (unlikely(!va))
		return ERR_PTR(-ENOMEM);

retry:
	spin_lock(&vmap_area_lock);
	/*
	 * Invalidate cache if we have more permissive parameters.
	 * cached_hole_size notes the largest hole noticed _below_
	 * the vmap_area cached in free_vmap_cache: if size fits
	 * into that hole, we want to scan from vstart to reuse
	 * the hole instead of allocating above free_vmap_cache.
	 * Note that __free_vmap_area may update free_vmap_cache
	 * without updating cached_hole_size or cached_align.
	 */
	if (!free_vmap_cache
		 || size < cached_hole_size
		 || vstart < cached_vstart
		 || align < cached_align) {
nocache:
		cached_hole_size = 0;
		free_vmap_cache = NULL;
	}
	/* record if we encounter less permissive parameters */
	cached_vstart = vstart;
	cached_align = align;

	/* find starting point for our search */
	if (free_vmap_cache) {
		first = rb_entry(free_vmap_cache, struct vmap_area, rb_node);
		addr = ALIGN(first->va_end, align);
		if (addr < vstart)
			goto nocache;
		if (addr + size - 1 < addr)
			goto overflow;

	} else {
		addr = ALIGN(vstart, align);
		if (addr + size - 1 < addr)
			goto overflow;

		n = vmap_area_root.rb_node;
		first = NULL;

		while (n) {
			struct vmap_area *tmp;
			tmp = rb_entry(n, struct vmap_area, rb_node);
			if (tmp->va_end >= addr) {
				first = tmp;
				if (tmp->va_start <= addr)
					break;
				n = n->rb_left;
			} else
				n = n->rb_right;
		}

		if (!first)
			goto found;
	}

	/* from the starting point, walk areas until a suitable hole is found */
	while (addr + size > first->va_start && addr + size <= vend) {
		if (addr + cached_hole_size < first->va_start)
			cached_hole_size = first->va_start - addr;
		addr = ALIGN(first->va_end, align);
		if (addr + size - 1 < addr)
			goto overflow;

		n = rb_next(&first->rb_node);
		if (n)
			first = rb_entry(n, struct vmap_area, rb_node);
		else
			goto found;
	}

found:
	if (addr + size > vend)
		goto overflow;

	va->va_start = addr;
	va->va_end = addr + size;
	va->flags = 0;
	// 将新分配的va插入到红黑树vmap_area_root中
	__insert_vmap_area(va);
	free_vmap_cache = &va->rb_node;
	spin_unlock(&vmap_area_lock);

	BUG_ON(va->va_start & (align-1));
	BUG_ON(va->va_start < vstart);
	BUG_ON(va->va_end > vend);

	return va;

overflow:
	spin_unlock(&vmap_area_lock);
	if (!purged) {
		purge_vmap_area_lazy();
		purged = 1;
		goto retry;
	}
	if (printk_ratelimit())
		printk(KERN_WARNING "vmap allocation for size %lu failed: "
			"use vmalloc=<size> to increase size.\n", size);
	kfree(va);
	return ERR_PTR(-EBUSY);
}
```

###### 6.6.2.1.1.1.3 setup_vmalloc_vm()

该函数定义于mm/vmalloc.c:

```
static void setup_vmalloc_vm(struct vm_struct *vm, struct vmap_area *va,
			      unsigned long flags, void *caller)
{
	vm->flags = flags;
	vm->addr = (void *)va->va_start;
	vm->size = va->va_end - va->va_start;
	vm->caller = caller;
	va->private = vm;
	va->flags |= VM_VM_AREA;
}
```

###### 6.6.2.1.1.2 \__vmalloc_area_node()

该函数定义于mm/vmalloc.c:

```
static void *__vmalloc_area_node(struct vm_struct *area, gfp_t gfp_mask,
				 pgprot_t prot, int node, void *caller)
{
	const int order = 0;
	struct page **pages;
	unsigned int nr_pages, array_size, i;
	gfp_t nested_gfp = (gfp_mask & GFP_RECLAIM_MASK) | __GFP_ZERO;

	nr_pages = (area->size - PAGE_SIZE) >> PAGE_SHIFT;
	array_size = (nr_pages * sizeof(struct page *));

	area->nr_pages = nr_pages;
	/* Please note that the recursion is strictly bounded. */
	if (array_size > PAGE_SIZE) {
		// 参见vzalloc()/vmalloc()节
		pages = __vmalloc_node(array_size, 1, nested_gfp|__GFP_HIGHMEM, PAGE_KERNEL, node, caller);
		area->flags |= VM_VPAGES;
	} else {
		/*
		 * Invoke kmalloc() to request a group of contiguous
		 * page frames large enough to contain an array of
		 * page descriptor pointers. 参见kzalloc()/kmalloc()节
		 */
		pages = kmalloc_node(array_size, nested_gfp, node);
	}
	area->pages = pages;
	area->caller = caller;
	if (!area->pages) {
		remove_vm_area(area->addr);
		kfree(area);
		return NULL;
	}

	for (i = 0; i < area->nr_pages; i++) {
		struct page *page;
		gfp_t tmp_mask = gfp_mask | __GFP_NOWARN;

		if (node < 0)
			page = alloc_page(tmp_mask);				// 参见alloc_page()节
		else
			page = alloc_pages_node(node, tmp_mask, order);		// 参见alloc_pages()节

		if (unlikely(!page)) {
			/* Successfully allocated i pages, free them in __vunmap() */
			area->nr_pages = i;
			goto fail;
		}
		area->pages[i] = page;
	}

	if (map_vm_area(area, prot, &pages))
		goto fail;
	return area->addr;

fail:
	warn_alloc_failed(gfp_mask, order,
			  "vmalloc: allocation failure, allocated %ld of %ld bytes\n",
			  (area->nr_pages*PAGE_SIZE), area->size);
	vfree(area->addr);
	return NULL;
}
```

###### 6.6.2.1.1.3 insert_vmalloc_vmlist()

该函数定义于mm/vmalloc.c:

```
static void insert_vmalloc_vmlist(struct vm_struct *vm)
{
	struct vm_struct *tmp, **p;

	vm->flags &= ~VM_UNLIST;
	write_lock(&vmlist_lock);
	for (p = &vmlist; (tmp = *p) != NULL; p = &tmp->next) {
		if (tmp->addr >= vm->addr)
			break;
	}
	vm->next = *p;
	*p = vm;
	write_unlock(&vmlist_lock);
}
```

#### 6.6.2.2 vmalloc_32()

该函数定义于mm/vmalloc.c:

```
/**
 *	vmalloc_32  -  allocate virtually contiguous memory (32bit addressable)
 *	@size:		allocation size
 *
 *	Allocate enough 32bit PA addressable pages to cover @size from the
 *	page level allocator and map them into contiguous kernel virtual space.
 */
void *vmalloc_32(unsigned long size)
{
	// 参见vzalloc()/vmalloc()节
	return __vmalloc_node(size, 1, GFP_VMALLOC32, PAGE_KERNEL, -1, __builtin_return_address(0));
}
```

#### 6.6.2.3 vfree()

The ```vfree()``` function releases noncontiguous memory areas created by ```vmalloc()``` or ```vmalloc_32()```, while the ```vunmap()``` function releases memory areas created by ```vmap()```.

该函数定义于mm/vmalloc.c:

```
/**
 *	vfree  -  release memory allocated by vmalloc()
 *	@addr:		memory base address
 *
 *	Free the virtually continuous memory area starting at @addr, as
 *	obtained from vmalloc(), vmalloc_32() or __vmalloc(). If @addr is
 *	NULL, no operation is performed.
 *
 *	Must not be called in interrupt context.
 */
void vfree(const void *addr)
{
	BUG_ON(in_interrupt());

	kmemleak_free(addr);

	__vunmap(addr, 1);	// 参见__vunmap()节
}
```

##### 6.6.2.3.1 \__vunmap()

该函数定义于mm/vmalloc.c:

```
static void __vunmap(const void *addr, int deallocate_pages)
{
	struct vm_struct *area;

	if (!addr)
		return;

	if ((PAGE_SIZE-1) & (unsigned long)addr) {
		WARN(1, KERN_ERR "Trying to vfree() bad address (%p)\n", addr);
		return;
	}

	area = remove_vm_area(addr);			// 参见remove_vm_area()节
	if (unlikely(!area)) {
		WARN(1, KERN_ERR "Trying to vfree() nonexistent vm area (%p)\n", addr);
		return;
	}

	debug_check_no_locks_freed(addr, area->size);
	debug_check_no_obj_freed(addr, area->size);

	if (deallocate_pages) {
		int i;

		for (i = 0; i < area->nr_pages; i++) {
			struct page *page = area->pages[i];

			BUG_ON(!page);
			__free_page(page);		// 参见__free_page()/free_page()节
		}

		if (area->flags & VM_VPAGES)
			vfree(area->pages);		// 参见vfree()节
		else
			kfree(area->pages);		// 参见kfree()节
	}

	kfree(area);					// 参见kfree()节
	return;
}
```

###### 6.6.2.3.1.1 remove_vm_area()

该函数定义于mm/vmalloc.c:

```
/**
 *	remove_vm_area  -  find and remove a continuous kernel virtual area
 *	@addr:		base address
 *
 *	Search for the kernel VM area starting at @addr, and remove it.
 *	This function returns the found VM area, but using it is NOT safe
 *	on SMP machines, except for its size or flags.
 */
struct vm_struct *remove_vm_area(const void *addr)
{
	struct vmap_area *va;

	va = find_vmap_area((unsigned long)addr);
	if (va && va->flags & VM_VM_AREA) {
		// 将va移出链表vmlist，参见错误：引用源未找到
		struct vm_struct *vm = va->private;

		if (!(vm->flags & VM_UNLIST)) {
			struct vm_struct *tmp, **p;
			/*
			 * remove from list and disallow access to
			 * this vm_struct before unmap. (address range
			 * confliction is maintained by vmap.)
			 */
			write_lock(&vmlist_lock);
			for (p = &vmlist; (tmp = *p) != vm; p = &tmp->next)
				;
			*p = tmp->next;
			write_unlock(&vmlist_lock);
		}

		vmap_debug_free_range(va->va_start, va->va_end);
		free_unmap_vmap_area(va);
		vm->size -= PAGE_SIZE;

		return vm;
	}
	return NULL;
}
```

## 6.7 Kernel Mappings of High-Memory Page Frames

The linear address that corresponds to the end of the directly mapped physical memory, and thus to the beginning of the high memory, is stored in the high_memory variable, which is set to 896 MB. Page frames above the 896 MB boundary are not generally mapped in the fourth gigabyte of the kernel linear address spaces, so the kernel is unable to directly access them. This implies that each page allocator function that returns the linear address of the assigned page frame doesn’t work for high memory page frames, that is, for page frames in the ZONE_HIGHME Mmemory zone.

变量high_memory定义于mm/memory.c:

```
/*
 * A number of key systems in x86 including ioremap() rely on the assumption
 * that high_memory defines the upper bound on direct map memory, then end
 * of ZONE_NORMAL.  Under CONFIG_DISCONTIG this means that max_low_pfn and
 * highstart_pfn must be the same; there must be no gap between ZONE_NORMAL
 * and ZONE_HIGHMEM.
 */
void * high_memory;
```

变量high_memory的初始化过程如下：

```
start_kernel()
-> setup_arch()
   -> initmem_init()		// arch/x86/mm/init_32.c
```

The allocation of high-memory page frames is done only through the alloc_pages() function and its alloc_page() shortcut.

Page frames in high memory that do not have a linear address cannot be accessed by the kernel. Therefore, part of the last 128 MB of the kernel linear address space is dedicated to mapping high-memory page frames.

The kernel uses three different mechanisms to map page frames in high memory; they are called:
* Permanent Kernel Mapping, see section Permanent Kernel Mapping
* Temporary Kernel Mapping, see section emporary Kernel Mapping
* Noncontiguous Memory Allocation, see section Allocate Virtually Contiguous Memory

### 6.7.1 Permanent Kernel Mapping

Permanent kernel mappings allow the kernel to establish long-lasting mappings of high-memory page frames into the kernel address space. They use a dedicated Page Table in the master kernel page tables. The pkmap_page_table variable (see section pkmap_page_table的初始化) stores the address of this Page Table, while the LAST_PKMAP macro yields the number of entries. As usual, the Page Table includes either 512 or 1,024 entries, according to whether PAE is enabled or disabled; thus, the kernel can access at most 2 or 4 MB of high memory at once. The Page Table maps the linear addresses starting from PKMAP_BASE.

The current state of the page table entries is managed by a simple array called pkmap_count which has LAST_PKMAP entries in it. Each element is not exactly a reference count but it is very close. If the entry is 0, the page is free and has not been used since the last TLB flush. If it is 1, the slot is unused but a page is still mapped there waiting for a TLB flush. Flushes are delayed until every slot has been used at least once as a global flush is required for all CPUs when the global page tables are modified and is extremely expensive. Any higher value is a reference count of n-1 users of the page.

Establishing a permanent kernel mapping may block the current process; this happens when no free Page Table entries exist that can be used as "windows" on the page frames in high memory. Thus, a permanent kernel mapping cannot be established in interrupt handlers and deferrable functions.

参见mm/highmem.c:

```
static int pkmap_count[LAST_PKMAP];
static unsigned int last_pkmap_nr;
static  __cacheline_aligned_in_smp DEFINE_SPINLOCK(kmap_lock);
pte_t *pkmap_page_table;
static DECLARE_WAIT_QUEUE_HEAD(pkmap_map_wait);
```

其中，LAST_PKMAP和PKMAP_BASE定义于arch/x86/include/asm/pgtable_32_types.h:

```
#ifdef CONFIG_X86_PAE
#define LAST_PKMAP	512
#else
#define LAST_PKMAP	1024
#endif

#define PKMAP_BASE	((FIXADDR_BOOT_START - PAGE_SIZE * (LAST_PKMAP + 1))	& PMD_MASK)
```

变量pkmap_page_table的结果:

![Memery_Layout_12](/assets/Memery_Layout_12.jpg)

#### 6.7.1.1 pkmap_page_table的初始化

```
start_kernel()
-> setup_arch()
   -> paging_init()
      -> pagetable_init()		// 参见early_node_map[]=>node_data[]->node_zones[]节
         -> permanent_kmaps_init(swapper_pg_dir)
```

函数permanent_kmaps_init()定义于arch/x86/mm/init_32.c:

```
#ifdef CONFIG_HIGHMEM
static void __init permanent_kmaps_init(pgd_t *pgd_base)
{
	unsigned long vaddr;
	pgd_t *pgd;
	pud_t *pud;
	pmd_t *pmd;
	pte_t *pte;

	vaddr = PKMAP_BASE;
	// 即调用：page_table_range_init(PKMAP_BASE, PKMAP_BASE + PAGE_SIZE*LAST_PKMAP, swapper_pg_dir);
	page_table_range_init(vaddr, vaddr + PAGE_SIZE*LAST_PKMAP, pgd_base);

	pgd = swapper_pg_dir + pgd_index(vaddr);
	pud = pud_offset(pgd, vaddr);
	pmd = pmd_offset(pud, vaddr);
	pte = pte_offset_kernel(pmd, vaddr);
	/*
	 * The page table entry for use with kmap() is called
	 * pkmap_page_table which is located at PKMAP_BASE.
	 */
	pkmap_page_table = pte;
}
#endif
```

其中，函数page_table_range_init()定义于arch/x86/mm/init_32.c:

```
// 即调用：page_table_range_init(PKMAP_BASE, PKMAP_BASE + PAGE_SIZE*LAST_PKMAP, swapper_pg_dir);
static void __init page_table_range_init(unsigned long start, unsigned long end, pgd_t *pgd_base)
{
	int pgd_idx, pmd_idx;
	unsigned long vaddr;
	pgd_t *pgd;
	pmd_t *pmd;
	pte_t *pte = NULL;

	vaddr = start;
	pgd_idx = pgd_index(vaddr);
	pmd_idx = pmd_index(vaddr);
	pgd = pgd_base + pgd_idx;

	for ( ; (pgd_idx < PTRS_PER_PGD) && (vaddr != end); pgd++, pgd_idx++) {
		pmd = one_md_table_init(pgd);
		pmd = pmd + pmd_index(vaddr);
		for (; (pmd_idx < PTRS_PER_PMD) && (vaddr != end); pmd++, pmd_idx++) {
			pte = page_table_kmap_check(one_page_table_init(pmd), pmd, vaddr, pte);
			vaddr += PMD_SIZE;
		}
		pmd_idx = 0;
	}
}
```

#### 6.7.1.2 kmap()

The kmap() function establishes a permanent kernel mapping.

**NOTE**: The kmap pool is quite small so it is important that users of ```kmap()``` call ```kunmap()``` as quickly as possible because the pressure on this small window grows incrementally worse as the size of high memory grows in comparison to low memory.

该函数定义于arch/x86/mm/highmem_32.c:

```
void *kmap(struct page *page)
{
	might_sleep();

	/*
	 * If the page is already in low memory and simply
	 * returns the address if it is.
	 */
	if (!PageHighMem(page))
		return page_address(page);	// 参见page_address()节

	/* If it is a high page to be mapped, kmap_high() is
	 * called to map a highmem page into memory.
	 */
	return kmap_high(page);			// 参见kmap_high()节
}
```

##### 6.7.1.2.1 kmap_high()

该函数定义于mm/highmem.c:

```
/**
 * kmap_high - map a highmem page into memory
 * @page: &struct page to map
 *
 * Returns the page's virtual memory address.
 *
 * We cannot call this from interrupts, as it may block.
 */
void *kmap_high(struct page *page)
{
	unsigned long vaddr;

	/*
	 * For highmem pages, we can't trust "virtual" until
	 * after we have the lock.
	 */
	lock_kmap();

	/*
	 * If the page isn’t mapped yet (vaddr = NULL), call
	 * map_new_virtual() to provide a mapping for the page.
	 */
	vaddr = (unsigned long)page_address(page);	// 参见page_address() in mm/highmem.c节
	if (!vaddr)
		vaddr = map_new_virtual(page);		// 参见map_new_virtual()节

	/*
	 * Once a mapping has been created, the corresponding
	 * entry in the pkmap_count array is incremented and
	 * the virtual address in low memory returned.
	 */
	pkmap_count[PKMAP_NR(vaddr)]++;
	BUG_ON(pkmap_count[PKMAP_NR(vaddr)] < 2);

	unlock_kmap();
	return (void*) vaddr;
}
```

###### 6.7.1.2.1.1 map_new_virtual()

该函数定义于mm/highmem.c:

```
static inline unsigned long map_new_virtual(struct page *page)
{
	unsigned long vaddr;
	int count;

start:
	count = LAST_PKMAP;
	/* Find an empty entry */
	/*
	 * linearly scan pkmap_count to find an empty entry
	 * starting at last_pkmap_nr instead of 0
	 */
	for (;;) {
		last_pkmap_nr = (last_pkmap_nr + 1) & LAST_PKMAP_MASK;
		if (!last_pkmap_nr) {
			/*
			 * flush_all_zero_pkmaps() starts scan of the counters
			 * that have the value 1. Each counter that has a value
			 * of 1 denotes an entry in pkmap_page_table that is free
			 * but cannot be used because the corresponding TLB entry
			 * has not yet been flushed. flush_all_zero_pkmaps() resets
			 * their counters to zero, deletes the corresponding elements
			 * from page_address_htable hash table, and issues TLB flushes
			 * on all entries of pkmap_page_table.
			 */
			flush_all_zero_pkmaps();
			count = LAST_PKMAP;
		}
		if (!pkmap_count[last_pkmap_nr])
			break;		/* Found a usable entry */
		if (--count)
			continue;

		/*
		 * If cannot find a null counter in pkmap_count, then  blocks the
		 * current process until some other process releases an entry of
		 * the pkmap_page_table Page Table. That’s, the process sleeps on
		 * the pkmap_map_wait wait queue until it’s woken up after next
		 * kunmap(). 参见kunmap()节
		 */
		/*
		 * Sleep for somebody else to unmap their entries
		 */
		{
			// 参见定义/初始化等待队列/wait_queue_t节
			DECLARE_WAITQUEUE(wait, current);

			__set_current_state(TASK_UNINTERRUPTIBLE);
			add_wait_queue(&pkmap_map_wait, &wait);
			unlock_kmap();
			schedule();
			remove_wait_queue(&pkmap_map_wait, &wait);
			lock_kmap();

			/* Somebody else might have mapped it while we slept */
			// 参见page_address() in mm/highmem.c节
			if (page_address(page))
				return (unsigned long)page_address(page);

			/* Re-start */
			goto start;
		}
	}
	vaddr = PKMAP_ADDR(last_pkmap_nr);
	set_pte_at(&init_mm, vaddr, &(pkmap_page_table[last_pkmap_nr]), mk_pte(page, kmap_prot));

	// 设置引用计数，并将该page链接到page_address_htable中的适当位置
	pkmap_count[last_pkmap_nr] = 1;
	set_page_address(page, (void *)vaddr);

	return vaddr;
}
```

#### 6.7.1.3 kunmap()

The ```kunmap()``` function destroys a permanent kernel mapping established previously by ```kmap()```.

该函数定义于mm/highmem_32.c:

```
void kunmap(struct page *page)
{
	if (in_interrupt())
		BUG();
	/*
	 * If the page already exists in low memory and
	 * needs no further handling.
	 */
	if (!PageHighMem(page))
		return;
	kunmap_high(page);	// 参见kunmap_high()节
}
```

##### 6.7.1.3.1 kunmap_high()

该函数定义于mm/highmem.c:

```
/**
 * kunmap_high - unmap a highmem page into memory
 * @page: &struct page to unmap
 *
 * If ARCH_NEEDS_KMAP_HIGH_GET is not defined then this may be called
 * only from user context.
 */
void kunmap_high(struct page *page)
{
	unsigned long vaddr;
	unsigned long nr;
	unsigned long flags;
	int need_wakeup;

	lock_kmap_any(flags);
	vaddr = (unsigned long)page_address(page);
	BUG_ON(!vaddr);
	nr = PKMAP_NR(vaddr);	// pkmap_count[]和pkmap_page_table[]下标

	/*
	 * A count must never go down to zero without a TLB flush!
	 */
	need_wakeup = 0;
	/*
	 * Decrement the corresponding element for this page in
	 * pkmap_count. If it reaches 1, which means no more users
	 * but a TLB flush is required), any process waiting on
	 * the pkmap_map_wait is woken up as a slot is now available.
	 */
	switch (--pkmap_count[nr]) {
	case 0:
		BUG();
	case 1:
		/*
		 * Avoid an unnecessary wake_up() function call.
		 * The common case is pkmap_count[] == 1, but
		 * no waiters.
		 * The tasks queued in the wait-queue are guarded
		 * by both the lock in the wait-queue-head and by
		 * the kmap_lock.  As the kmap_lock is held here,
		 * no need for the wait-queue-head's lock.  Simply
		 * test if the queue is empty.
		 */
		// pkmap_map_wait中的等待进程是由kmap()->kmap_high()->map_new_virtual()设置的
		need_wakeup = waitqueue_active(&pkmap_map_wait);
	}
	unlock_kmap_any(flags);

	/* do wake-up, if needed, race-free outside of the spin lock */
	if (need_wakeup)
		wake_up(&pkmap_map_wait);
}
```

### 6.7.2 Temporary Kernel Mapping

Temporary kernel mappings are simpler to implement than permanent kernel mappings; moreover, they can be used inside interrupt handlers and deferrable functions, because requesting a temporary kernel mapping never blocks the current process.

Every page frame in high memory can be mapped through a window in the kernel address space — namely, a Page Table entry that is reserved for this purpose. The number of windows reserved for temporary kernel mappings is quite small. Each CPU has its own set of windows, represented by the enum km_type data structure. Each symbol defined in this data structure identifies the linear address of a window. See include/asm-generic/kmap_types.h.

The kernel must ensure that the same window is never used by two kernel control paths at the same time. Thus, each symbol in the km_type structure is dedicated to one kernel component and is named after the component.

Each symbol in km_type, except the last one, is an index of a fix-mapped linear address. The enum fixed_addresses data structure includes the symbols FIX_KMAP_BEGIN and FIX_KMAP_END; the latter is assigned to the index FIX_KMAP_BEGIN + (KM_TYPE_NR * NR_CPUS) - 1. In this manner, there are KM_TYPE_NR fix-mapped linear addresses for each CPU in the system. Furthermore, the kernel initializes the kmap_pte variable with the address of the Page Table entry corresponding to the fix_to_virt(FIX_KMAP_BEGIN) linear address:

```
start_kernel()
-> setup_arch()
   -> paging_init()
      -> kmap_init()	// 参见early_node_map[]=>node_data[]->node_zones[]节
```

#### 6.7.2.1 kmap_atomic()

To establish a temporary kernel mapping, the kernel invokes the ```kmap_atomic()``` function.

该宏定义于include/linux/highmem.h:

```
#define kmap_atomic(page, args...)	__kmap_atomic(page)
```

其中，函数__kmap_atomic()定义于arch/x86/mm/highmem_32.c:

```
void *__kmap_atomic(struct page *page)
{
	return kmap_atomic_prot(page, kmap_prot);
}

/*
 * kmap_atomic/kunmap_atomic is significantly faster than kmap/kunmap because
 * no global lock is needed and because the kmap code must perform a global TLB
 * invalidation when the kmap pool wraps.
 *
 * However when holding an atomic kmap it is not legal to sleep, so atomic
 * kmaps are appropriate for short, tight code paths only.
 */
void *kmap_atomic_prot(struct page *page, pgprot_t prot)
{
	unsigned long vaddr;
	int idx, type;

	/* even !CONFIG_PREEMPT needs this, for in_atomic in do_page_fault */
	pagefault_disable();

	if (!PageHighMem(page))
		return page_address(page);

	type = kmap_atomic_idx_push();
	idx = type + KM_TYPE_NR*smp_processor_id();
	vaddr = __fix_to_virt(FIX_KMAP_BEGIN + idx);
	BUG_ON(!pte_none(*(kmap_pte-idx)));
	set_pte(kmap_pte-idx, mk_pte(page, prot));
	arch_flush_lazy_mmu_mode();

	return (void *)vaddr;
}
```

#### 6.7.2.2 kunmap_atomic()

To destroy a temporary kernel mapping, the kernel uses the ```kunmap_atomic()``` function.

该宏定义于include/linux/highmem.h:

```
#define kunmap_atomic(addr, args...)					\
do {									\
	BUILD_BUG_ON(__same_type((addr), struct page *));		\
	__kunmap_atomic(addr);						\
} while (0)
```

其中，函数__kunmap_atomic()定义于arch/x86/mm/highmem_32.c:

```
void __kunmap_atomic(void *kvaddr)
{
	unsigned long vaddr = (unsigned long) kvaddr & PAGE_MASK;

	if (vaddr >= __fix_to_virt(FIX_KMAP_END) &&
		 vaddr <= __fix_to_virt(FIX_KMAP_BEGIN)) {
		int idx, type;

		type = kmap_atomic_idx();
		idx = type + KM_TYPE_NR * smp_processor_id();

#ifdef CONFIG_DEBUG_HIGHMEM
		WARN_ON_ONCE(vaddr != __fix_to_virt(FIX_KMAP_BEGIN + idx));
#endif
		/*
		 * Force other mappings to Oops if they'll try to access this
		 * pte without first remap it.  Keeping stale mappings around
		 * is a bad idea also, in case the page changes cacheability
		 * attributes or becomes a protected page in a hypervisor.
		 */
		kpte_clear_flush(kmap_pte-idx, vaddr);
		kmap_atomic_idx_pop();
		arch_flush_lazy_mmu_mode();
	}
#ifdef CONFIG_DEBUG_HIGHMEM
	else {
		BUG_ON(vaddr < PAGE_OFFSET);
		BUG_ON(vaddr >= (unsigned long)high_memory);
	}
#endif

	pagefault_enable();
}
```

## 6.8 虚拟内存空间/Virtual Memory Area

与Virtual Memory Area有关的数据结构参见struct vm_area_struct节，其结构参见错误：引用源未找到。

### 6.8.1 Find a Memory Regin

**find_vma_intersection()**

Find the first memory region that overlaps a given linear address interval.

**find_vma_prepare()**

Locate the position of the new leaf in the red-black tree that corresponds to a given linear address and returns the addresses of the preceding memory region and of the parent node of the leaf to be inserted.

**get_unmapped_area()**

Searche the process address space to find an available linear address interval.

#### 6.8.1.1 find_vma()

Function ```find_vma()``` is used to find the closest region to a given address.

该函数定义于mm/mmap.c:

```
/* Look up the first VMA which satisfies  addr < vm_end,  NULL if none. */
struct vm_area_struct *find_vma(struct mm_struct *mm, unsigned long addr)
{
	struct vm_area_struct *vma = NULL;

	if (mm) {
		/* Check the cache first. */
		/* (Cache hit rate is typically around 35%.) */
		vma = mm->mmap_cache;
		if (!(vma && vma->vm_end > addr && vma->vm_start <= addr)) {
			struct rb_node * rb_node;

			rb_node = mm->mm_rb.rb_node;
			vma = NULL;

			while (rb_node) {
				struct vm_area_struct * vma_tmp;

				vma_tmp = rb_entry(rb_node, struct vm_area_struct, vm_rb);

				if (vma_tmp->vm_end > addr) {
					vma = vma_tmp;
					if (vma_tmp->vm_start <= addr)
						break;
					rb_node = rb_node->rb_left;
				} else
					rb_node = rb_node->rb_right;
			}
			if (vma)
				mm->mmap_cache = vma;
		}
	}
	return vma;
}
```

#### 6.8.1.2 find_vma_prev()

The ```find_vma_prev()``` function is similar to ```find_vma()```, except that it writes in an additional pprev parameter a pointer to the descriptor of the memory region that precedes the one selected by the function.

该函数定义于mm/mmap.c:

```
/* Same as find_vma, but also return a pointer to the previous VMA in *pprev. */
struct vm_area_struct *find_vma_prev(struct mm_struct *mm, unsigned long addr,
					struct vm_area_struct **pprev)
{
	struct vm_area_struct *vma = NULL, *prev = NULL;
	struct rb_node *rb_node;
	if (!mm)
		goto out;

	/* Guard against addr being lower than the first VMA */
	vma = mm->mmap;

	/* Go through the RB tree quickly. */
	rb_node = mm->mm_rb.rb_node;

	while (rb_node) {
		struct vm_area_struct *vma_tmp;
		vma_tmp = rb_entry(rb_node, struct vm_area_struct, vm_rb);

		if (addr < vma_tmp->vm_end) {
			rb_node = rb_node->rb_left;
		} else {
			prev = vma_tmp;
			if (!prev->vm_next || (addr < prev->vm_next->vm_end))
				break;
			rb_node = rb_node->rb_right;
		}
	}

out:
	*pprev = prev;
	return prev ? prev->vm_next : vma;
}
```

### 6.8.2 Allocate a Linear Address Interval

#### 6.8.2.1 do_mmap()

该函数定义于include/linux/mm.h:

```
static inline unsigned long do_mmap(struct file *file, unsigned long addr,
				   unsigned long len, unsigned long prot,
				   unsigned long flag, unsigned long offset)
{
	unsigned long ret = -EINVAL;
	if ((offset + PAGE_ALIGN(len)) < offset)
		goto out;
	if (!(offset & ~PAGE_MASK))
		ret = do_mmap_pgoff(file, addr, len, prot, flag, offset >> PAGE_SHIFT);
out:
	return ret;
}
```

##### 6.8.2.1.1 do_mmap_pgoff()

该函数定义于mm/mmap.c:

```
unsigned long do_mmap_pgoff(struct file *file, unsigned long addr,
				  unsigned long len, unsigned long prot,
				  unsigned long flags, unsigned long pgoff)
{
	struct mm_struct * mm = current->mm;
	struct inode *inode;
	vm_flags_t vm_flags;
	int error;
	unsigned long reqprot = prot;

	/*
	 * Does the application expect PROT_READ to imply PROT_EXEC?
	 *
	 * (the exception is when the underlying filesystem is noexec
	 *  mounted, in which case we dont add PROT_EXEC.)
	 */
	if ((prot & PROT_READ) && (current->personality & READ_IMPLIES_EXEC))
		if (!(file && (file->f_path.mnt->mnt_flags & MNT_NOEXEC)))
			prot |= PROT_EXEC;

	if (!len)
		return -EINVAL;

	if (!(flags & MAP_FIXED))
		addr = round_hint_to_min(addr);

	/* Careful about overflows.. */
	len = PAGE_ALIGN(len);
	if (!len)
		return -ENOMEM;

	/* offset overflow? */
	if ((pgoff + (len >> PAGE_SHIFT)) < pgoff)
               return -EOVERFLOW;

	/* Too many mappings? */
	if (mm->map_count > sysctl_max_map_count)
		return -ENOMEM;

	/* Obtain the address to map to. we verify (or select) it and ensure
	 * that it represents a valid section of the address space.
	 */
	// 参见Find a Memory Regin节
	addr = get_unmapped_area(file, addr, len, pgoff, flags);
	if (addr & ~PAGE_MASK)
		return addr;

	/* Do simple checking here so the lower-level routines won't have
	 * to. we assume access permissions have been handled by the open
	 * of the memory object, so we don't do any here.
	 */
	vm_flags = calc_vm_prot_bits(prot) | calc_vm_flag_bits(flags) |
				 mm->def_flags | VM_MAYREAD | VM_MAYWRITE | VM_MAYEXEC;

	if (flags & MAP_LOCKED)
		if (!can_do_mlock())
			return -EPERM;

	/* mlock MCL_FUTURE? */
	if (vm_flags & VM_LOCKED) {
		unsigned long locked, lock_limit;
		locked = len >> PAGE_SHIFT;
		locked += mm->locked_vm;
		lock_limit = rlimit(RLIMIT_MEMLOCK);
		lock_limit >>= PAGE_SHIFT;
		if (locked > lock_limit && !capable(CAP_IPC_LOCK))
			return -EAGAIN;
	}

	inode = file ? file->f_path.dentry->d_inode : NULL;

	if (file) {
		switch (flags & MAP_TYPE) {
		case MAP_SHARED:
			if ((prot & PROT_WRITE) && !(file->f_mode & FMODE_WRITE))
				return -EACCES;

			/*
			 * Make sure we don't allow writing to an append-only
			 * file..
			 */
			if (IS_APPEND(inode) && (file->f_mode & FMODE_WRITE))
				return -EACCES;

			/*
			 * Make sure there are no mandatory locks on the file.
			 */
			if (locks_verify_locked(inode))
				return -EAGAIN;

			vm_flags |= VM_SHARED | VM_MAYSHARE;
			if (!(file->f_mode & FMODE_WRITE))
				vm_flags &= ~(VM_MAYWRITE | VM_SHARED);

			/* fall through */
		case MAP_PRIVATE:
			if (!(file->f_mode & FMODE_READ))
				return -EACCES;
			if (file->f_path.mnt->mnt_flags & MNT_NOEXEC) {
				if (vm_flags & VM_EXEC)
					return -EPERM;
				vm_flags &= ~VM_MAYEXEC;
			}

			if (!file->f_op || !file->f_op->mmap)
				return -ENODEV;
			break;

		default:
			return -EINVAL;
		}
	} else {
		switch (flags & MAP_TYPE) {
		case MAP_SHARED:
			/*
			 * Ignore pgoff.
			 */
			pgoff = 0;
			vm_flags |= VM_SHARED | VM_MAYSHARE;
			break;
		case MAP_PRIVATE:
			/*
			 * Set pgoff according to addr for anon_vma.
			 */
			pgoff = addr >> PAGE_SHIFT;
			break;
		default:
			return -EINVAL;
		}
	}

	// 调用变量security_ops中的对应函数，参见security_xxx()节
	error = security_file_mmap(file, reqprot, prot, flags, addr, 0);
	if (error)
		return error;

	// 参见mmap_region()节
	return mmap_region(file, addr, len, flags, vm_flags, pgoff);
}
```

###### 6.8.2.1.1.1 mmap_region()

该函数定义于mm/mmap.c:

```
unsigned long mmap_region(struct file *file, unsigned long addr, unsigned long len,
			   unsigned long flags, vm_flags_t vm_flags, unsigned long pgoff)
{
	struct mm_struct *mm = current->mm;
	struct vm_area_struct *vma, *prev;
	int correct_wcount = 0;
	int error;
	struct rb_node **rb_link, *rb_parent;
	unsigned long charged = 0;
	struct inode *inode =  file ? file->f_path.dentry->d_inode : NULL;

	/* Clear old maps */
	error = -ENOMEM;
munmap_back:
	// 参见Find a Memory Regin节
	vma = find_vma_prepare(mm, addr, &prev, &rb_link, &rb_parent);
	if (vma && vma->vm_start < addr + len) {
		if (do_munmap(mm, addr, len))	// 参见do_munmap()节
			return -ENOMEM;
		goto munmap_back;
	}

	/* Check against address space limit. */
	if (!may_expand_vm(mm, len >> PAGE_SHIFT))
		return -ENOMEM;

	/*
	 * Set 'VM_NORESERVE' if we should not account for the
	 * memory use of this mapping.
	 */
	if ((flags & MAP_NORESERVE)) {
		/* We honor MAP_NORESERVE if allowed to overcommit */
		if (sysctl_overcommit_memory != OVERCOMMIT_NEVER)
			vm_flags |= VM_NORESERVE;

		/* hugetlb applies strict overcommit unless MAP_NORESERVE */
		if (file && is_file_hugepages(file))
			vm_flags |= VM_NORESERVE;
	}

	/*
	 * Private writable mapping: check memory availability
	 */
	if (accountable_mapping(file, vm_flags)) {
		charged = len >> PAGE_SHIFT;
		// 调用变量security_ops中的对应函数，参见security_xxx()节
		if (security_vm_enough_memory(charged))
			return -ENOMEM;
		vm_flags |= VM_ACCOUNT;
	}

	/*
	 * Can we just expand an old mapping?
	 */
	/*
	 * Check whether the preceding memory region can be expanded
	 * in such a way to include the new interval.
	 * The preceding memory region must have exactly the same flags
	 * as those memory regions stored in vm_flags.
	 * 参见节
	 */
	vma = vma_merge(mm, prev, addr, addr + len, vm_flags, NULL, file, pgoff, NULL);
	if (vma)
		goto out;

	/*
	 * Determine the object being mapped and call the appropriate
	 * specific mapper. the address has already been validated, but
	 * not unmapped, but the maps are removed from the list.
	 */
	vma = kmem_cache_zalloc(vm_area_cachep, GFP_KERNEL);	// 参见kmem_cache_zalloc()节
	if (!vma) {
		error = -ENOMEM;
		goto unacct_error;
	}

	vma->vm_mm = mm;
	vma->vm_start = addr;
	vma->vm_end = addr + len;
	vma->vm_flags = vm_flags;
	vma->vm_page_prot = vm_get_page_prot(vm_flags);
	vma->vm_pgoff = pgoff;
	INIT_LIST_HEAD(&vma->anon_vma_chain);

	if (file) {
		error = -EINVAL;
		if (vm_flags & (VM_GROWSDOWN|VM_GROWSUP))
			goto free_vma;
		if (vm_flags & VM_DENYWRITE) {
			error = deny_write_access(file);
			if (error)
				goto free_vma;
			correct_wcount = 1;
		}
		vma->vm_file = file;
		get_file(file);
		error = file->f_op->mmap(file, vma);
		if (error)
			goto unmap_and_free_vma;
		if (vm_flags & VM_EXECUTABLE)
			added_exe_file_vma(mm);

		/* Can addr have changed??
		 *
		 * Answer: Yes, several device drivers can do it in their
		 *         f_op->mmap method. -DaveM
		 */
		addr = vma->vm_start;
		pgoff = vma->vm_pgoff;
		vm_flags = vma->vm_flags;
	} else if (vm_flags & VM_SHARED) {
		/*
		 * If MAP_SHARED is set and the new memory region
		 * doesn’t map a file on disk, it’s a shared anonymous
		 * region. Shared anonymous regions are mainly used
		 * for interprocess communications.
		 */
		error = shmem_zero_setup(vma);
		if (error)
			goto free_vma;
	}

	if (vma_wants_writenotify(vma)) {
		pgprot_t pprot = vma->vm_page_prot;

		/* Can vma->vm_page_prot have changed??
		 *
		 * Answer: Yes, drivers may have changed it in their
		 *         f_op->mmap method.
		 *
		 * Ensures that vmas marked as uncached stay that way.
		 */
		vma->vm_page_prot = vm_get_page_prot(vm_flags & ~VM_SHARED);
		if (pgprot_val(pprot) == pgprot_val(pgprot_noncached(pprot)))
			vma->vm_page_prot = pgprot_noncached(vma->vm_page_prot);
	}

	// Insert the new region in the memory region list and red-black tree.
	vma_link(mm, vma, prev, rb_link, rb_parent);
	file = vma->vm_file;

	/* Once vma denies write, undo our temporary denial count */
	if (correct_wcount)
		atomic_inc(&inode->i_writecount);
out:
	perf_event_mmap(vma);

	mm->total_vm += len >> PAGE_SHIFT;
	vm_stat_account(mm, vm_flags, file, len >> PAGE_SHIFT);
	/*
	 * Invoke make_pages_present() to allocate all pages
	 * of memory region in succession & lock them in RAM
	 */
	if (vm_flags & VM_LOCKED) {
		if (!mlock_vma_pages_range(vma, addr, addr + len))
			mm->locked_vm += (len >> PAGE_SHIFT);
	} else if ((flags & MAP_POPULATE) && !(flags & MAP_NONBLOCK))
		make_pages_present(addr, addr + len);

	// Return the linear address of the new memory region
	return addr;

unmap_and_free_vma:
	if (correct_wcount)
		atomic_inc(&inode->i_writecount);
	vma->vm_file = NULL;
	fput(file);

	/* Undo any partial mapping done by a device driver. */
	unmap_region(mm, vma, prev, vma->vm_start, vma->vm_end);
	charged = 0;
free_vma:
	kmem_cache_free(vm_area_cachep, vma);
unacct_error:
	if (charged)
		vm_unacct_memory(charged);
	return error;
}
```

###### 6.8.2.1.1.1.1 Merge Contiguous Region/vma_merge()

该函数定义于mm/mmap.c:

```
struct vm_area_struct *vma_merge(struct mm_struct *mm, struct vm_area_struct *prev,
			unsigned long addr, unsigned long end, unsigned long vm_flags, struct anon_vma *anon_vma,
			struct file *file, pgoff_t pgoff, struct mempolicy *policy)
{
	pgoff_t pglen = (end - addr) >> PAGE_SHIFT;
	struct vm_area_struct *area, *next;
	int err;

	/*
	 * We later require that vma->vm_flags == vm_flags,
	 * so this tests vma->vm_flags & VM_SPECIAL, too.
	 */
	if (vm_flags & VM_SPECIAL)
		return NULL;

	if (prev)
		next = prev->vm_next;
	else
		next = mm->mmap;
	area = next;
	if (next && next->vm_end == end)			/* cases 6, 7, 8 */
		next = next->vm_next;

	/*
	 * Can it merge with the predecessor?
	 */
	if (prev && prev->vm_end == addr &&
  		 mpol_equal(vma_policy(prev), policy) &&
		 can_vma_merge_after(prev, vm_flags, anon_vma, file, pgoff)) {
		/*
		 * OK, it can.  Can we now merge in the successor as well?
		 */
		if (next && end == next->vm_start &&
			 mpol_equal(policy, vma_policy(next)) &&
			 can_vma_merge_before(next, vm_flags, anon_vma, file, pgoff+pglen) &&
			 is_mergeable_anon_vma(prev->anon_vma, next->anon_vma, NULL)) {	/* cases 1, 6 */
			err = vma_adjust(prev, prev->vm_start, next->vm_end, prev->vm_pgoff, NULL);
		} else						/* cases 2, 5, 7 */
			err = vma_adjust(prev, prev->vm_start, end, prev->vm_pgoff, NULL);
		if (err)
			return NULL;
		khugepaged_enter_vma_merge(prev);
		return prev;
	}

	/*
	 * Can this new request be merged in front of next?
	 */
	if (next && end == next->vm_start &&
 		 mpol_equal(policy, vma_policy(next)) &&
		 can_vma_merge_before(next, vm_flags, anon_vma, file, pgoff+pglen)) {
		if (prev && addr < prev->vm_end)		/* case 4 */
			err = vma_adjust(prev, prev->vm_start, addr, prev->vm_pgoff, NULL);
		else						/* cases 3, 8 */
			err = vma_adjust(area, addr, next->vm_end, next->vm_pgoff - pglen, NULL);
		if (err)
			return NULL;
		khugepaged_enter_vma_merge(area);
		return area;
	}

	return NULL;
}
```

### 6.8.3 Insert a Memory Region

#### 6.8.3.1 insert_vm_struct()

该函数定义于mm/mmap.c:

```
/* Insert vm structure into process list sorted by address
 * and into the inode's i_mmap tree.  If vm_file is non-NULL
 * then i_mmap_mutex is taken here.
 */
int insert_vm_struct(struct mm_struct * mm, struct vm_area_struct * vma)
{
	struct vm_area_struct * __vma, * prev;
	struct rb_node ** rb_link, * rb_parent;

	/*
	 * The vm_pgoff of a purely anonymous vma should be irrelevant
	 * until its first write fault, when page's anon_vma and index
	 * are set.  But now set the vm_pgoff it will almost certainly
	 * end up with (unless mremap moves it elsewhere before that
	 * first wfault), so /proc/pid/maps tells a consistent story.
	 *
	 * By setting it to reflect the virtual start address of the
	 * vma, merges and splits can happen in a seamless way, just
	 * using the existing file pgoff checks and manipulations.
	 * Similarly in do_mmap_pgoff and in do_brk.
	 */
	if (!vma->vm_file) {
		BUG_ON(vma->anon_vma);
		vma->vm_pgoff = vma->vm_start >> PAGE_SHIFT;
	}
	// 参见Find a Memory Regin节
	__vma = find_vma_prepare(mm,vma->vm_start,&prev,&rb_link,&rb_parent);
	if (__vma && __vma->vm_start < vma->vm_end)
		return -ENOMEM;
	if ((vma->vm_flags & VM_ACCOUNT) && security_vm_enough_memory_mm(mm, vma_pages(vma)))
		return -ENOMEM;
	vma_link(mm, vma, prev, rb_link, rb_parent);
	return 0;
}
```

### 6.8.4 Remap and Move a Memory Region

#### 6.8.4.1 sys_mremap()

该函数定义于mm/mremap.c:

```
SYSCALL_DEFINE5(mremap, unsigned long, addr, unsigned long, old_len,
		unsigned long, new_len, unsigned long, flags, unsigned long, new_addr)
{
	unsigned long ret;

	down_write(&current->mm->mmap_sem);
	ret = do_mremap(addr, old_len, new_len, flags, new_addr);	// 参见do_mremap()节
	up_write(&current->mm->mmap_sem);
	return ret;
}
```

##### 6.8.4.1.1 do_mremap()

该函数定义于mm/mremap.c:

```
/*
 * Expand (or shrink) an existing mapping, potentially moving it at the
 * same time (controlled by the MREMAP_MAYMOVE flag and available VM space)
 *
 * MREMAP_FIXED option added 5-Dec-1999 by Benjamin LaHaise
 * This option implies MREMAP_MAYMOVE.
 */
unsigned long do_mremap(unsigned long addr, unsigned long old_len,
	unsigned long new_len, unsigned long flags, unsigned long new_addr)
{
	struct mm_struct *mm = current->mm;
	struct vm_area_struct *vma;
	unsigned long ret = -EINVAL;
	unsigned long charged = 0;

	if (flags & ~(MREMAP_FIXED | MREMAP_MAYMOVE))
		goto out;

	if (addr & ~PAGE_MASK)
		goto out;

	old_len = PAGE_ALIGN(old_len);
	new_len = PAGE_ALIGN(new_len);

	/*
	 * We allow a zero old-len as a special case
	 * for DOS-emu "duplicate shm area" thing. But
	 * a zero new-len is nonsensical.
	 */
	if (!new_len)
		goto out;

	if (flags & MREMAP_FIXED) {
		if (flags & MREMAP_MAYMOVE)
			ret = mremap_to(addr, old_len, new_addr, new_len);
		goto out;
	}

	/*
	 * Always allow a shrinking remap: that just unmaps
	 * the unnecessary pages..
	 * do_munmap does all the needed commit accounting
	 */
	if (old_len >= new_len) {
		ret = do_munmap(mm, addr+new_len, old_len - new_len);	// 参见do_munmap()节
		if (ret && old_len != new_len)
			goto out;
		ret = addr;
		goto out;
	}

	/*
	 * Ok, we need to grow..
	 */
	vma = vma_to_resize(addr, old_len, new_len, &charged);
	if (IS_ERR(vma)) {
		ret = PTR_ERR(vma);
		goto out;
	}

	/* old_len exactly to the end of the area..
	 */
	if (old_len == vma->vm_end - addr) {
		/* can we just expand the current mapping? */
		if (vma_expandable(vma, new_len - old_len)) {
			int pages = (new_len - old_len) >> PAGE_SHIFT;

			if (vma_adjust(vma, vma->vm_start, addr + new_len, vma->vm_pgoff, NULL)) {
				ret = -ENOMEM;
				goto out;
			}

			mm->total_vm += pages;
			vm_stat_account(mm, vma->vm_flags, vma->vm_file, pages);
			if (vma->vm_flags & VM_LOCKED) {
				mm->locked_vm += pages;
				mlock_vma_pages_range(vma, addr + old_len, addr + new_len);
			}
			ret = addr;
			goto out;
		}
	}

	/*
	 * We weren't able to just expand or shrink the area,
	 * we need to create a new one and move it..
	 */
	ret = -ENOMEM;
	if (flags & MREMAP_MAYMOVE) {
		unsigned long map_flags = 0;
		if (vma->vm_flags & VM_MAYSHARE)
			map_flags |= MAP_SHARED;

		new_addr = get_unmapped_area(vma->vm_file, 0, new_len,
					vma->vm_pgoff + ((addr - vma->vm_start) >> PAGE_SHIFT), map_flags);
		if (new_addr & ~PAGE_MASK) {
			ret = new_addr;
			goto out;
		}

		// 调用变量security_ops中的对应函数，参见security_xxx()节
		ret = security_file_mmap(NULL, 0, 0, 0, new_addr, 1);
		if (ret)
			goto out;
		ret = move_vma(vma, addr, old_len, new_len, new_addr);
	}
out:
	if (ret & ~PAGE_MASK)
		vm_unacct_memory(charged);
	return ret;
}
```

### 6.8.5 Release/Delete a Linear Address Interval

#### 6.8.5.1 do_munmap()

该函数定义于mm/mmap.c:

```
/* Munmap is split into 2 main parts -- this part which finds
 * what needs doing, and the areas themselves, which do the
 * work.  This now handles partial unmappings.
 * Jeremy Fitzhardinge <jeremy@goop.org>
 */
int do_munmap(struct mm_struct *mm, unsigned long start, size_t len)
{
	unsigned long end;
	struct vm_area_struct *vma, *prev, *last;

	if ((start & ~PAGE_MASK) || start > TASK_SIZE || len > TASK_SIZE-start)
		return -EINVAL;

	if ((len = PAGE_ALIGN(len)) == 0)
		return -EINVAL;

	/* Find the first overlapping VMA */
	vma = find_vma(mm, start);				// 参见find_vma()节
	if (!vma)
		return 0;
	prev = vma->vm_prev;
	/* we have  start < vma->vm_end  */

	/* if it doesn't overlap, we have nothing.. */
	end = start + len;
	if (vma->vm_start >= end)
		return 0;

	/*
	 * If we need to split any vma, do it now to save pain later.
	 *
	 * Note: mremap's move_vma VM_ACCOUNT handling assumes a partially
	 * unmapped vm_area_struct will remain in use: so lower split_vma
	 * places tmp vma above, and higher split_vma places tmp vma below.
	 */
	if (start > vma->vm_start) {
		int error;

		/*
		 * Make sure that map_count on return from munmap() will
		 * not exceed its limit; but let map_count go just above
		 * its limit temporarily, to help free resources as expected.
		 */
		if (end < vma->vm_end && mm->map_count >= sysctl_max_map_count)
			return -ENOMEM;

		error = __split_vma(mm, vma, start, 0);		// 参见__split_vma()节
		if (error)
			return error;
		prev = vma;
	}

	/* Does it split the last one? */
	last = find_vma(mm, end); 				// 参见find_vma()节
	if (last && end > last->vm_start) {
		int error = __split_vma(mm, last, end, 1);	// 参见__split_vma()节
		if (error)
			return error;
	}
	vma = prev? prev->vm_next : mm->mmap;

	/*
	 * unlock any mlock()ed ranges before detaching vmas
	 */
	if (mm->locked_vm) {
		struct vm_area_struct *tmp = vma;
		while (tmp && tmp->vm_start < end) {
			if (tmp->vm_flags & VM_LOCKED) {
				mm->locked_vm -= vma_pages(tmp);
				munlock_vma_pages_all(tmp);
			}
			tmp = tmp->vm_next;
		}
	}

	/*
	 * Remove the vma's, and unmap the actual pages
	 */
	detach_vmas_to_be_unmapped(mm, vma, prev, end);
	unmap_region(mm, vma, prev, start, end);		// 参见unmap_region()节

	/* Fix up all other VM information */
	remove_vma_list(mm, vma);

	return 0;
}
```

##### 6.8.5.1.1 \__split_vma()

The purpose of the ```split_vma()``` function is to split a memory region that intersects a linear address interval into two smaller regions, one outside of the interval and the other inside. The input parameter new_below specifies whether the intersection occurs at the beginning or at the end of the interval.

该函数定义于mm/mmap.c:

```
static int __split_vma(struct mm_struct * mm, struct vm_area_struct * vma,
			unsigned long addr, int new_below)
{
	struct mempolicy *pol;
	struct vm_area_struct *new;
	int err = -ENOMEM;

	if (is_vm_hugetlb_page(vma) && (addr & ~(huge_page_mask(hstate_vma(vma)))))
		return -EINVAL;

	// 参见6.5.1.1.3.1 kmem_cache_zalloc()节
	new = kmem_cache_alloc(vm_area_cachep, GFP_KERNEL);
	if (!new)
		goto out_err;

	/* most fields are the same, copy all, and then fixup */
	*new = *vma;

	INIT_LIST_HEAD(&new->anon_vma_chain);

	if (new_below)
		new->vm_end = addr;
	else {
		new->vm_start = addr;
		new->vm_pgoff += ((addr - vma->vm_start) >> PAGE_SHIFT);
	}

	pol = mpol_dup(vma_policy(vma));
	if (IS_ERR(pol)) {
		err = PTR_ERR(pol);
		goto out_free_vma;
	}
	vma_set_policy(new, pol);

	if (anon_vma_clone(new, vma))
		goto out_free_mpol;

	if (new->vm_file) {
		get_file(new->vm_file);
		if (vma->vm_flags & VM_EXECUTABLE)
			added_exe_file_vma(mm);
	}

	if (new->vm_ops && new->vm_ops->open)
		new->vm_ops->open(new);

	if (new_below)
		err = vma_adjust(vma, addr, vma->vm_end, vma->vm_pgoff +
				 ((addr - new->vm_start) >> PAGE_SHIFT), new);
	else
		err = vma_adjust(vma, vma->vm_start, addr, vma->vm_pgoff, new);

	/* Success. */
	if (!err)
		return 0;

	/* Clean everything up if vma_adjust failed. */
	if (new->vm_ops && new->vm_ops->close)
		new->vm_ops->close(new);
	if (new->vm_file) {
		if (vma->vm_flags & VM_EXECUTABLE)
			removed_exe_file_vma(mm);
		fput(new->vm_file);
	}
	unlink_anon_vmas(new);
out_free_mpol:
	mpol_put(pol);
out_free_vma:
	kmem_cache_free(vm_area_cachep, new);
out_err:
	return err;
}
```

##### 6.8.5.1.2 unmap_region()

The ```unmap_region()``` function walks through a list of memory regions and releases the page frames belonging to them.

该函数定义于mm/mmap.c:

```
static void unmap_region(struct mm_struct *mm, struct vm_area_struct *vma,
			  struct vm_area_struct *prev, unsigned long start, unsigned long end)
{
	struct vm_area_struct *next = prev? prev->vm_next: mm->mmap;
	struct mmu_gather tlb;
	unsigned long nr_accounted = 0;

	lru_add_drain();
	/*
	 * Initialize a per-CPU variable named mmu_gathers:
	 * The contents of mmu_gathers are architecture-dependent:
	 * generally speaking, the variable should store all
	 * information required for a successful updating of
	 * the page table entries of a process.
	 */
	tlb_gather_mmu(&tlb, mm, 0);
	update_hiwater_rss(mm);
	/*
	 * Scan all Page Table entries belonging to the linear
	 * address interval: if only one CPU is available, the
	 * function invokes free_swap_and_cache() repeatedly to
	 * release the corresponding page; otherwise, the function
	 * saves the pointers of the corresponding page descriptors
	 * in the mmu_gathers local variable.
	 */
	unmap_vmas(&tlb, vma, start, end, &nr_accounted, NULL);
	vm_unacct_memory(nr_accounted);
	/*
	 * Try to reclaim the Page Tables of the process that have
	 * been emptied in the previous step.
	 */
	free_pgtables(&tlb, vma, prev ? prev->vm_end : FIRST_USER_ADDRESS,
			next ? next->vm_start : 0);
	/*
	 * Invokes flush_tlb_mm() to flush the TLB;
	 * In multiprocessor system, invokes free_pages_and_swap_cache()
	 * to release the page frames whose pointers have been collected
	 * in the mmu_gather data structure.
	 */
	tlb_finish_mmu(&tlb, start, end);
}
```

#### 6.8.5.2 exit_mmap()

该函数定义于mm/mmap.c:

```
/* Release all mmaps. */
void exit_mmap(struct mm_struct *mm)
{
	struct mmu_gather tlb;
	struct vm_area_struct *vma;
	unsigned long nr_accounted = 0;
	unsigned long end;

	/* mm's last user has gone, and its about to be pulled down */
	mmu_notifier_release(mm);

	if (mm->locked_vm) {
		vma = mm->mmap;
		while (vma) {
			if (vma->vm_flags & VM_LOCKED)
				munlock_vma_pages_all(vma);
			vma = vma->vm_next;
		}
	}

	arch_exit_mmap(mm);

	vma = mm->mmap;
	if (!vma)	/* Can happen if dup_mmap() received an OOM */
		return;

	lru_add_drain();
	flush_cache_mm(mm);
	tlb_gather_mmu(&tlb, mm, 1);
	/* update_hiwater_rss(mm) here? but nobody should be looking */
	/* Use -1 here to ensure all VMAs in the mm are unmapped */
	end = unmap_vmas(&tlb, vma, 0, -1, &nr_accounted, NULL);
	vm_unacct_memory(nr_accounted);

	free_pgtables(&tlb, vma, FIRST_USER_ADDRESS, 0);
	tlb_finish_mmu(&tlb, 0, end);

	/*
	 * Walk the list again, actually closing and freeing it,
	 * with preemption enabled, without holding any MM locks.
	 */
	while (vma)
		vma = remove_vma(vma);

	BUG_ON(mm->nr_ptes > (FIRST_USER_ADDRESS+PMD_SIZE-1)>>PMD_SHIFT);
}
```

## 6.9 Page Fault/do_page_fault()

Each architecture registers an architecture-specific function for the handling of page faults.

Pages in the process linear address space are not necessarily resident in memory. For example, allocations made on behalf of a process are not satisfied immediately as the space is just reserved within the vm_area_struct. Other examples of non-resident pages include the page having been swapped out to backing storage or writing a read-only page.

Linux, like most operating systems, has a Demand Fetch policy as its fetch policy for dealing with pages that are not resident. This states that the page is only fetched from backing storage when the hardware raises a page fault exception (see Vec=0xEC in 错误：引用源未找到) which the operating system traps and allocates a page.

There are two types of page fault, major and minor faults. Major page faults occur when data has to be read from disk which is an expensive operation, else the fault is referred to as a minor, or soft page fault. Linux maintains statistics on the number of these types of page faults with the task_struct->maj_flt and task_struct->min_flt fields respectively (see section 进程描述符/struct task_struct).

The page fault handler in Linux is expected to recognise and act on a number of different types of page faults listed in 错误：引用源未找到.

Reasons For Page Faulting:

| Exception | Type | Action |
| :-------- | :--- | :----- |
| Region valid but page not allocated | Minor | Allocate a page frame from the physical page allocator |
| Region not valid but is beside an expandable region like the stack | Minor | Expand the region and allocate a page |
| Page swapped out but present in swap cache | Minor | Re-establish the page in the process page tables and drop a reference to the swap cache |
| Page swapped out to backing storage | Major | Find where the page with information stored in the PTE and read it from disk |
| Page write when marked read-only | Minor | If the page is a COW page, make a copy of it, mark it writable and assign it to the process. If it is in fact a bad write, send a SIGSEGV signal |
| Region is invalid or process has no permissions to access | Error | Send a SEGSEGV signal to the process |
| Fault occurred in the kernel portion address space | Minor | If the fault occurred in the vmalloc area of the address space, the current process page tables are updated against the master page table held by init_mm. This is the only valid kernel page fault that may occur |
| Fault occurred in the userspace region while in kernel mode | Error | If a fault occurs, it means a kernel system did not copy from userspace properly and caused a page fault. This is a kernel bug which is treated quite severely. |

<p/>

函数do_page_fault()定义于arch/x86/mm/fault.c:

```
/*
 * This routine handles page faults.  It determines the address, and the problem,
 * and then passes it off to one of the appropriate routines.
 */
dotraplinkage void __kprobes do_page_fault(struct pt_regs *regs, unsigned long error_code)
{
	struct vm_area_struct *vma;
	struct task_struct *tsk;
	unsigned long address;
	struct mm_struct *mm;
	int fault;
	int write = error_code & PF_WRITE;
	unsigned int flags = FAULT_FLAG_ALLOW_RETRY | FAULT_FLAG_KILLABLE |
					(write ? FAULT_FLAG_WRITE : 0);

	tsk = current;
	mm = tsk->mm;

	/* Get the faulting address: */
	address = read_cr2();		// 参见错误：引用源未找到

	/*
	 * Detect and handle instructions that would cause a page fault for
	 * both a tracked kernel page and a userspace page.
	 */
	if (kmemcheck_active(regs))
		kmemcheck_hide(regs);
	prefetchw(&mm->mmap_sem);

	if (unlikely(kmmio_fault(regs, address)))
		return;

	/*
	 * We fault-in kernel-space virtual memory on-demand. The
	 * 'reference' page table is init_mm.pgd.
	 *
	 * NOTE! We MUST NOT take any locks for this case. We may
	 * be in an interrupt or a critical region, and should
	 * only copy the information from the master page table,
	 * nothing more.
	 *
	 * This verifies that the fault happens in kernel space
	 * (error_code & 4) == 0, and that the fault was not a
	 * protection error (error_code & 9) == 0.
	 */
	if (unlikely(fault_in_kernel_space(address))) {	// address >= TASK_SIZE_MAX
		if (!(error_code & (PF_RSVD | PF_USER | PF_PROT))) {
			// Handle a fault on the vmalloc area
			if (vmalloc_fault(address) >= 0)
				return;

			if (kmemcheck_fault(regs, address, error_code))
				return;
		}

		/* Can handle a stale RO->RW TLB: */
		// Handle a spurious fault caused by a stale TLB entry
		if (spurious_fault(error_code, address))
			return;

		/* kprobes don't want to hook the spurious faults: */
		if (notify_page_fault(regs))
			return;
		/*
		 * Don't take the mm semaphore here. If we fixup a prefetch
		 * fault we could otherwise deadlock:
		 */
		bad_area_nosemaphore(regs, error_code, address);

		return;
	}

	/* kprobes don't want to hook the spurious faults: */
	if (unlikely(notify_page_fault(regs)))
		return;
	/*
	 * It's safe to allow irq's after cr2 has been saved and the
	 * vmalloc fault has been handled.
	 *
	 * User-mode registers count as a user access even for any
	 * potential system fault or CPU buglet:
	 */
	if (user_mode_vm(regs)) {
		local_irq_enable();
		error_code |= PF_USER;
	} else {
		if (regs->flags & X86_EFLAGS_IF)
			local_irq_enable();
	}

	if (unlikely(error_code & PF_RSVD))
		pgtable_bad(regs, error_code, address);

	perf_sw_event(PERF_COUNT_SW_PAGE_FAULTS, 1, regs, address);

	/*
	 * If we're in an interrupt, have no user context or are running
	 * in an atomic region then we must not take the fault:
	 */
	if (unlikely(in_atomic() || !mm)) {
		bad_area_nosemaphore(regs, error_code, address);
		return;
	}

	/*
	 * When running in the kernel we expect faults to occur only to
	 * addresses in user space.  All other faults represent errors in
	 * the kernel and should generate an OOPS.  Unfortunately, in the
	 * case of an erroneous fault occurring in a code path which already
	 * holds mmap_sem we will deadlock attempting to validate the fault
	 * against the address space.  Luckily the kernel only validly
	 * references user space from well defined areas of code, which are
	 * listed in the exceptions table.
	 *
	 * As the vast majority of faults will be valid we will only perform
	 * the source reference check when there is a possibility of a
	 * deadlock. Attempt to lock the address space, if we cannot we then
	 * validate the source. If this is invalid we can skip the address
	 * space check, thus avoiding the deadlock:
	 */
	if (unlikely(!down_read_trylock(&mm->mmap_sem))) {
		if ((error_code & PF_USER) == 0 && !search_exception_tables(regs->ip)) {
			bad_area_nosemaphore(regs, error_code, address);
			return;
		}
retry:
		down_read(&mm->mmap_sem);
	} else {
		/*
		 * The above down_read_trylock() might have succeeded in
		 * which case we'll have missed the might_sleep() from
		 * down_read():
		 */
		might_sleep();
	}

	vma = find_vma(mm, address);	// 参见find_vma()节
	if (unlikely(!vma)) {
		bad_area(regs, error_code, address);
		return;
	}
	if (likely(vma->vm_start <= address))
		goto good_area;
	if (unlikely(!(vma->vm_flags & VM_GROWSDOWN))) {
		bad_area(regs, error_code, address);
		return;
	}
	if (error_code & PF_USER) {
		/*
		 * Accessing the stack below %sp is always a bug.
		 * The large cushion allows instructions like enter
		 * and pusha to work. ("enter $65535, $31" pushes
		 * 32 pointers and then decrements %sp by 65535.)
		 */
		if (unlikely(address + 65536 + 32 * sizeof(unsigned long) < regs->sp)) {
			bad_area(regs, error_code, address);
			return;
		}
	}
	if (unlikely(expand_stack(vma, address))) {
		bad_area(regs, error_code, address);
		return;
	}

	/*
	 * Ok, we have a good vm_area for this memory access, so
	 * we can handle it..
	 */
good_area:
	if (unlikely(access_error(error_code, vma))) {
		bad_area_access_error(regs, error_code, address);
		return;
	}

	/*
	 * If for any reason at all we couldn't handle the fault,
	 * make sure we exit gracefully rather than endlessly redo
	 * the fault:
	 */
	/*
	 * If handle_mm_fault() returns 1, it’s a minor fault,
	 * 2 is a major fault, 0 sends a SIGBUS error and any
	 * other value invokes the out of memory handler.
	 * 参见handle_mm_fault()节
	 */
	fault = handle_mm_fault(mm, vma, address, flags);

	if (unlikely(fault & (VM_FAULT_RETRY|VM_FAULT_ERROR))) {
		if (mm_fault_error(regs, error_code, address, fault))
			return;
	}

	/*
	 * Major/minor page fault accounting is only done on the
	 * initial attempt. If we go through a retry, it is extremely
	 * likely that the page will be found in page cache at that point.
	 */
	if (flags & FAULT_FLAG_ALLOW_RETRY) {
		if (fault & VM_FAULT_MAJOR) {
			tsk->maj_flt++;
			perf_sw_event(PERF_COUNT_SW_PAGE_FAULTS_MAJ, 1, regs, address);
		} else {
			tsk->min_flt++;
			perf_sw_event(PERF_COUNT_SW_PAGE_FAULTS_MIN, 1, regs, address);
		}
		if (fault & VM_FAULT_RETRY) {
			/* Clear FAULT_FLAG_ALLOW_RETRY to avoid any risk
			 * of starvation. */
			flags &= ~FAULT_FLAG_ALLOW_RETRY;
			goto retry;
		}
	}

	check_v8086_mode(regs, address, tsk);

	up_read(&mm->mmap_sem);
}
```

### 6.9.1 handle_mm_fault()

该函数定义于mm/memory.c:

```
int handle_mm_fault(struct mm_struct *mm, struct vm_area_struct *vma,
			unsigned long address, unsigned int flags)
{
	pgd_t *pgd;
	pud_t *pud;
	pmd_t *pmd;
	pte_t *pte;

	__set_current_state(TASK_RUNNING);

	count_vm_event(PGFAULT);
	mem_cgroup_count_vm_event(mm, PGFAULT);

	/* do counter updates before entering really critical section. */
	check_sync_rss_stat(current);

	if (unlikely(is_vm_hugetlb_page(vma)))
		return hugetlb_fault(mm, vma, address, flags);

	pgd = pgd_offset(mm, address);
	pud = pud_alloc(mm, pgd, address);
	if (!pud)
		return VM_FAULT_OOM;
	pmd = pmd_alloc(mm, pud, address);
	if (!pmd)
		return VM_FAULT_OOM;
	if (pmd_none(*pmd) && transparent_hugepage_enabled(vma)) {
		if (!vma->vm_ops)
			return do_huge_pmd_anonymous_page(mm, vma, address, pmd, flags);
	} else {
		pmd_t orig_pmd = *pmd;
		barrier();
		if (pmd_trans_huge(orig_pmd)) {
			if (flags & FAULT_FLAG_WRITE &&
				!pmd_write(orig_pmd) &&
				!pmd_trans_splitting(orig_pmd))
				return do_huge_pmd_wp_page(mm, vma, address, pmd, orig_pmd);
			return 0;
		}
	}

	/*
	 * Use __pte_alloc instead of pte_alloc_map, because we can't
	 * run pte_offset_map on the pmd, if an huge pmd could
	 * materialize from under us from a different thread.
	 */
	if (unlikely(pmd_none(*pmd)) && __pte_alloc(mm, vma, pmd, address))
		return VM_FAULT_OOM;
	/* if an huge pmd materialized from under us just retry later */
	if (unlikely(pmd_trans_huge(*pmd)))
		return 0;
	/*
	 * A regular pmd is established and it can't morph into a huge pmd
	 * from under us anymore at this point because we hold the mmap_sem
	 * read mode and khugepaged takes it in write mode. So now it's
	 * safe to run pte_offset_map().
	 */
	pte = pte_offset_map(pmd, address);

	// 参见handle_pte_fault()节
	return handle_pte_fault(mm, vma, address, pte, pmd, flags);
}
```

#### 6.9.1.1 handle_pte_fault()

该函数定义于mm/memory.c:

```
int handle_pte_fault(struct mm_struct *mm, struct vm_area_struct *vma,
		     unsigned long address, pte_t *pte, pmd_t *pmd, unsigned int flags)
{
	pte_t entry;
	spinlock_t *ptl;

	entry = *pte;
	if (!pte_present(entry)) {
		/*
		 * If no PTE has been allocated, do_anonymous_page()
		 * is called which handles Demand Allocation.
		 */
		if (pte_none(entry)) {
			if (vma->vm_ops) {
				if (likely(vma->vm_ops->fault))
					return do_linear_fault(mm, vma, address, pte, pmd, flags, entry);
			}
			return do_anonymous_page(mm, vma, address, pte, pmd, flags);
		}
		if (pte_file(entry))
			return do_nonlinear_fault(mm, vma, address, pte, pmd, flags, entry);
		/*
		 * Otherwise it is a page that has been swapped out
		 * to disk and do_swap_page() performs Demand Paging.
		 */
		return do_swap_page(mm, vma, address, pte, pmd, flags, entry);
	}

	ptl = pte_lockptr(mm, pmd);
	spin_lock(ptl);
	if (unlikely(!pte_same(*pte, entry)))
		goto unlock;
	if (flags & FAULT_FLAG_WRITE) {
		/*
		 * If the PTE is write protected, then do_wp_page() is
		 * called as the page is a Copy-On-Write (COW) page.
		 * A COW page is one which is shared between multiple
		 * processes (usually a parent and child) until a write
		 * occurs after which a private copy is made for the
		 * writing process.
		 */
		if (!pte_write(entry))
			return do_wp_page(mm, vma, address, pte, pmd, ptl, entry);
		/*
		 * If it is not a COW page, the page is simply marked
		 * dirty as it has been written to.
		 */
		entry = pte_mkdirty(entry);
	}
	/*
	 * If the page has been read and is present but a fault still
	 * occurred. This can occur with some architectures that do
	 * not have a three level page table. In this case, the PTE
	 * is simply established and marked young.
	 */
	entry = pte_mkyoung(entry);
	if (ptep_set_access_flags(vma, address, pte, entry, flags & FAULT_FLAG_WRITE)) {
		update_mmu_cache(vma, address, pte);
	} else {
		/*
		 * This is needed only for protection faults but the arch code
		 * is not yet telling us if this is a protection fault or not.
		 * This still avoids useless tlb flushes for .text page faults
		 * with threads.
		 */
		if (flags & FAULT_FLAG_WRITE)
			flush_tlb_fix_spurious_fault(vma, address);
	}
unlock:
	pte_unmap_unlock(pte, ptl);
	return 0;
}
```

### 6.9.2 Out Of Memory (OOM) Management

Out Of Memory (OOM) manager has one simple task: check if there is enough available memory to satisfy, verify that the system is truely out of memory and if so, select a process to kill.

#### 6.9.2.1 mm_fault_error()

该函数定义于arch/x86/mm/fault.c:

```
static noinline int mm_fault_error(struct pt_regs *regs, unsigned long error_code,
				  unsigned long address, unsigned int fault)
{
	/*
	 * Pagefault was interrupted by SIGKILL. We have no reason to
	 * continue pagefault.
	 */
	if (fatal_signal_pending(current)) {
		if (!(fault & VM_FAULT_RETRY))
			up_read(&current->mm->mmap_sem);
		if (!(error_code & PF_USER))
			no_context(regs, error_code, address);
		return 1;
	}
	if (!(fault & VM_FAULT_ERROR))
		return 0;

	if (fault & VM_FAULT_OOM) {
		/* Kernel mode? Handle exceptions or die: */
		if (!(error_code & PF_USER)) {
			up_read(&current->mm->mmap_sem);
			no_context(regs, error_code, address);
			return 1;
		}

		out_of_memory(regs, error_code, address);
	} else {
		if (fault & (VM_FAULT_SIGBUS|VM_FAULT_HWPOISON|VM_FAULT_HWPOISON_LARGE))
			do_sigbus(regs, error_code, address, fault);
		else
			BUG();
	}
	return 1;
}
```

其中，函数out_of_memory()定义于arch/x86/mm/fault.c:

```
static void out_of_memory(struct pt_regs *regs, unsigned long error_code, unsigned long address)
{
	/*
	 * We ran out of memory, call the OOM killer, and return the userspace
	 * (which will retry the fault, or kill us if we got oom-killed):
	 */
	up_read(&current->mm->mmap_sem);

	pagefault_out_of_memory();
}
```

其中，函数pagefault_out_of_memory()定义于mm/oom_kill.c:

```
/*
 * The pagefault handler calls here because it is out of memory, so kill a
 * memory-hogging task.  If a populated zone has ZONE_OOM_LOCKED set, a parallel
 * oom killing is already in progress so do nothing.  If a task is found with
 * TIF_MEMDIE set, it has been killed so do nothing and allow it to exit.
 */
void pagefault_out_of_memory(void)
{
	if (try_set_system_oom()) {
		out_of_memory(NULL, 0, 0, NULL);	// 参见out_of_memory()节
		clear_system_oom();
	}
	if (!test_thread_flag(TIF_MEMDIE))
		schedule_timeout_uninterruptible(1);
}
```

##### 6.9.2.1.1 out_of_memory()

该函数定义于mm/oom_kill.c:

```
/**
 * out_of_memory - kill the "best" process when we run out of memory
 * @zonelist: zonelist pointer
 * @gfp_mask: memory allocation flags
 * @order: amount of memory being requested as a power of 2
 * @nodemask: nodemask passed to page allocator
 *
 * If we run out of memory, we have the choice between either
 * killing a random task (bad), letting the system crash (worse)
 * OR try to be smart about which process to kill. Note that we
 * don't have to be perfect here, we just have to be good.
 */
void out_of_memory(struct zonelist *zonelist, gfp_t gfp_mask, int order, nodemask_t *nodemask)
{
	const nodemask_t *mpol_mask;
	struct task_struct *p;
	unsigned long totalpages;
	unsigned long freed = 0;
	unsigned int points;
	enum oom_constraint constraint = CONSTRAINT_NONE;
	int killed = 0;

	blocking_notifier_call_chain(&oom_notify_list, 0, &freed);
	if (freed > 0)
		/* Got some memory back in the last second. */
		return;

	/*
	 * If current has a pending SIGKILL, then automatically select it.  The
	 * goal is to allow it to allocate so that it may quickly exit and free
	 * its memory.
	 */
	if (fatal_signal_pending(current)) {
		set_thread_flag(TIF_MEMDIE);
		return;
	}

	/*
	 * Check if there were limitations on the allocation (only relevant for
	 * NUMA) that may require different handling.
	 */
	constraint = constrained_alloc(zonelist, gfp_mask, nodemask, &totalpages);
	mpol_mask = (constraint == CONSTRAINT_MEMORY_POLICY) ? nodemask : NULL;
	check_panic_on_oom(constraint, gfp_mask, order, mpol_mask);

	read_lock(&tasklist_lock);
	if (sysctl_oom_kill_allocating_task &&
		 !oom_unkillable_task(current, NULL, nodemask) &&
		 current->mm) {
		/*
		 * oom_kill_process() needs tasklist_lock held.  If it returns
		 * non-zero, current could not be killed so we must fallback to
		 * the tasklist scan.
		 */
		if (!oom_kill_process(current, gfp_mask, order, 0, totalpages, NULL, nodemask,
						"Out of memory (oom_kill_allocating_task)"))
			goto out;
	}

retry:
	/*
	 * It's responsible for choosing a process to kill.
	 * It decides by stepping through each running task
	 * and calculating how suitable it is for killing
	 * with the function oom_badness().
	 */
	p = select_bad_process(&points, totalpages, NULL, mpol_mask);
	if (PTR_ERR(p) == -1UL)
		goto out;

	/* Found nothing?!?! Either we hang forever, or we panic. */
	if (!p) {
		dump_header(NULL, gfp_mask, order, NULL, mpol_mask);
		read_unlock(&tasklist_lock);
		panic("Out of memory and no killable processes...\n");
	}

	/*
	 * Once a task is selected, the list is walked again and
	 * each process that shares the same mm_struct as the
	 * selected process (i.e. they are threads) is sent a signal.
	 * If the process has CAP_SYS_RAWIO capabilities, a SIGTERM
	 * is sent to give the process a chance of exiting cleanly,
	 * otherwise a SIGKILL is sent.
	 */
	if (oom_kill_process(p, gfp_mask, order, points, totalpages, NULL, nodemask, "Out of memory"))
		goto retry;
	killed = 1;
out:
	read_unlock(&tasklist_lock);

	/*
	 * Give "p" a good chance of killing itself before we
	 * retry to allocate memory unless "p" is current
	 */
	if (killed && !test_thread_flag(TIF_MEMDIE))
		schedule_timeout_uninterruptible(1);
}
```

## 6.10 Reserved Page Frame Pool

参见<<Understanding the Linux Kernel, 3rd Edition>> 第8. Memory Management章第The Pool of Reserved Page Frames节:

Memory allocation requests can be satisfied in two different ways. If enough free memory is available, the request can be satisfied immediately. Otherwise, some memory reclaiming must take place, and the kernel control path that made the request is blocked until additional memory has been freed.

However, some kernel control paths cannot be blocked while requesting memory — this happens, for instance, when handling an interrupt or when executing code inside a critical region. In these cases, a kernel control path should issue atomic memory allocation requests (using the GFP_ATOMIC flag). An atomic request never blocks: if there are not enough free pages, the allocation simply fails.

Although there is no way to ensure that an atomic memory allocation request never fails, the kernel tries hard to minimize the likelihood of this unfortunate event. In order to do this, the kernel reserves a pool of page frames for atomic memory allocation requests to be used only on low-on-memory conditions.

The amount of the reserved memory (in kilobytes) is stored in the min_free_kbytes variable. Its initial value is set during kernel initialization and depends on the amount of physical memory that is directly mapped in the kernel’s fourth gigabyte of linear addresses — that is, it depends on the number of page frames included in the ZONE_DMA and ZONE_NORMAL memory zones:

![Reserved_Memory](/assets/Reserved_Memory.png)

However, initially min_free_kbytes cannot be lower than 128 and greater than 65,536.

全局变量min_free_kbytes定义于mm/page_alloc.c:

```
int min_free_kbytes = 1024;

int __meminit init_per_zone_wmark_min(void)
{
	unsigned long lowmem_kbytes;

	lowmem_kbytes = nr_free_buffer_pages() * (PAGE_SIZE >> 10);

	min_free_kbytes = int_sqrt(lowmem_kbytes * 16);
	if (min_free_kbytes < 128)
		min_free_kbytes = 128;
	if (min_free_kbytes > 65536)
		min_free_kbytes = 65536;

	setup_per_zone_wmarks();
	refresh_zone_stat_thresholds();
	setup_per_zone_lowmem_reserve();
	setup_per_zone_inactive_ratio();

	return 0;
}

/*
 * 由mm/Makefile可知，mm/page_alloc.c被直接编译进内核，
 * 故在系统启动时如下初始化函数被调用，
 * 参见module被编译进内核时的初始化过程节
 */
module_init(init_per_zone_wmark_min)
```

The ZONE_DMA and ZONE_NORMAL memory zones contribute to the reserved memory with a number of page frames proportional to their relative sizes.

The **pages_min** field of the zone descriptor stores the number of reserved page frames inside the zone. That field plays also a role for the page frame reclaiming algorithm, together with the **pages_low** and **pages_high** fields. The **pages_low** field is always set to 5/4 of the value of **pages_min**, and **pages_high** is always set to 3/2 of the value of **pages_min**.

# Appendixes

## Appendix A: make -f scripts/Makefile.build obj=列表

```
// Refer to target scripts_basic in top Makefile
make -f scripts/Makefile.build obj=scripts/basic
// Refer to target prepare0 in top Makefile
make -f scripts/Makefile.build obj=.
// Refer to target scripts in top Makefile
make -f scripts/Makefile.build obj=scripts
make -f scripts/Makefile.build obj=scripts/mod
// Refer to $(init-y) in top Makefile
make -f scripts/Makefile.build obj=init
// Refer to $(core-y) in top Makefile
make -f scripts/Makefile.build obj=usr
make -f scripts/Makefile.build obj=arch/x86
make -f scripts/Makefile.build obj=arch/x86/crypto
make -f scripts/Makefile.build obj=arch/x86/kernel
make -f scripts/Makefile.build obj=arch/x86/kernel/acpi
make -f scripts/Makefile.build obj=arch/x86/kernel/apic
make -f scripts/Makefile.build obj=arch/x86/kernel/cpu
make -f scripts/Makefile.build obj=arch/x86/kernel/cpu/mtrr
make -f scripts/Makefile.build obj=arch/x86/mm
make -f scripts/Makefile.build obj=arch/x86/net
make -f scripts/Makefile.build obj=arch/x86/platform
make -f scripts/Makefile.build obj=arch/x86/platform/ce4100
make -f scripts/Makefile.build obj=arch/x86/platform/efi
make -f scripts/Makefile.build obj=arch/x86/platform/geode
make -f scripts/Makefile.build obj=arch/x86/platform/iris
make -f scripts/Makefile.build obj=arch/x86/platform/mrst
make -f scripts/Makefile.build obj=arch/x86/platform/olpc
make -f scripts/Makefile.build obj=arch/x86/platform/scx200
make -f scripts/Makefile.build obj=arch/x86/platform/sfi
make -f scripts/Makefile.build obj=arch/x86/platform/uv
make -f scripts/Makefile.build obj=arch/x86/platform/visws
make -f scripts/Makefile.build obj=arch/x86/vdso
make -f scripts/Makefile.build obj=kernel
make -f scripts/Makefile.build obj=kernel/events
make -f scripts/Makefile.build obj=kernel/irq
make -f scripts/Makefile.build obj=kernel/time
make -f scripts/Makefile.build obj=mm
make -f scripts/Makefile.build obj=fs
make -f scripts/Makefile.build obj=fs/devpts
make -f scripts/Makefile.build obj=fs/exofs
make -f scripts/Makefile.build obj=fs/nls
make -f scripts/Makefile.build obj=fs/notify
make -f scripts/Makefile.build obj=fs/notify/dnotify
make -f scripts/Makefile.build obj=fs/notify/fanotify
make -f scripts/Makefile.build obj=fs/notify/inotify
make -f scripts/Makefile.build obj=fs/partitions
make -f scripts/Makefile.build obj=fs/proc
make -f scripts/Makefile.build obj=fs/quota
make -f scripts/Makefile.build obj=fs/ramfs
make -f scripts/Makefile.build obj=fs/sysfs
make -f scripts/Makefile.build obj=ipc
make -f scripts/Makefile.build obj=security
make -f scripts/Makefile.build obj=crypto
make -f scripts/Makefile.build obj=block
// Refer to $(drivers-y) in top Makefile
make -f scripts/Makefile.build obj=drivers
make -f scripts/Makefile.build obj=drivers/auxdisplay
make -f scripts/Makefile.build obj=drivers/base
make -f scripts/Makefile.build obj=drivers/base/power
make -f scripts/Makefile.build obj=drivers/block
make -f scripts/Makefile.build obj=drivers/cdrom
make -f scripts/Makefile.build obj=drivers/char
make -f scripts/Makefile.build obj=drivers/clk
make -f scripts/Makefile.build obj=drivers/clocksource
make -f scripts/Makefile.build obj=drivers/firewire
make -f scripts/Makefile.build obj=drivers/firmware
make -f scripts/Makefile.build obj=drivers/gpio
make -f scripts/Makefile.build obj=drivers/gpu
make -f scripts/Makefile.build obj=drivers/gpu/drm
make -f scripts/Makefile.build obj=drivers/gpu/drm/i2c
make -f scripts/Makefile.build obj=drivers/gpu/stub
make -f scripts/Makefile.build obj=drivers/gpu/vga
make -f scripts/Makefile.build obj=drivers/i2c
make -f scripts/Makefile.build obj=drivers/i2c/algos
make -f scripts/Makefile.build obj=drivers/i2c/busses
make -f scripts/Makefile.build obj=drivers/i2c/muxes
make -f scripts/Makefile.build obj=drivers/idle
make -f scripts/Makefile.build obj=drivers/ieee802154
make -f scripts/Makefile.build obj=drivers/input
make -f scripts/Makefile.build obj=drivers/input/keyboard
make -f scripts/Makefile.build obj=drivers/input/serio
make -f scripts/Makefile.build obj=drivers/leds
make -f scripts/Makefile.build obj=drivers/lguest
make -f scripts/Makefile.build obj=drivers/macintosh
make -f scripts/Makefile.build obj=drivers/media
make -f scripts/Makefile.build obj=drivers/media/common
make -f scripts/Makefile.build obj=drivers/media/common/tuners
make -f scripts/Makefile.build obj=drivers/media/rc
make -f scripts/Makefile.build obj=drivers/media/rc/keymaps
make -f scripts/Makefile.build obj=drivers/media/video
make -f scripts/Makefile.build obj=drivers/media/video/davinci
make -f scripts/Makefile.build obj=drivers/mfd
make -f scripts/Makefile.build obj=drivers/misc
make -f scripts/Makefile.build obj=drivers/misc/carma
make -f scripts/Makefile.build obj=drivers/misc/cb710
make -f scripts/Makefile.build obj=drivers/misc/eeprom
make -f scripts/Makefile.build obj=drivers/misc/lis3lv02d
make -f scripts/Makefile.build obj=drivers/misc/ti-st
make -f scripts/Makefile.build obj=drivers/net
make -f scripts/Makefile.build obj=drivers/nfc
make -f scripts/Makefile.build obj=drivers/pinctrl
make -f scripts/Makefile.build obj=drivers/platform
make -f scripts/Makefile.build obj=drivers/platform/x86
make -f scripts/Makefile.build obj=drivers/tty
make -f scripts/Makefile.build obj=drivers/tty/ipwireless
make -f scripts/Makefile.build obj=drivers/tty/serial
make -f scripts/Makefile.build obj=drivers/tty/vt
make -f scripts/Makefile.build obj=drivers/video
make -f scripts/Makefile.build obj=drivers/video/backlight
make -f scripts/Makefile.build obj=drivers/video/console
make -f scripts/Makefile.build obj=drivers/video/display
make -f scripts/Makefile.build obj=drivers/video/omap2
make -f scripts/Makefile.build obj=drivers/video/omap2/displays
make -f scripts/Makefile.build obj=sound
make -f scripts/Makefile.build obj=firmware
// Refer to $(net-y) in top Makefile
make -f scripts/Makefile.build obj=net
// Refer to $(libs-y) in top Makefile
make -f scripts/Makefile.build obj=lib
make -f scripts/Makefile.build obj=arch/x86/lib
```

## Appendix B: Makefile Tree

```
linux-3.2/Makefile
+- include scripts/Kbuild.include
|  +- build := -f $(srctree)/scripts/Makefile.build obj	// 参见下文
+- include arch/$(SRCARCH)/Makefile					// 以x86为例，即include linux-3.2/arch/x86/Makefile
|  +- include $(srctree)/arch/x86/Makefile_32.cpu
```

```
linux-3.2/scripts/Makefile.build
+- -include include/config/auto.conf
+- include scripts/Kbuild.include
+- include $(kbuild-file)			// 包含指定目录下的Kbuild，或者Makefile(若不存在Kbuild的话)
+- include scripts/Makefile.lib
+- include scripts/Makefile.host
+- include $(cmd_files)
```

可运行下列命令查看完成的Makefile/Kbuild的包含关系:

```
chenwx@chenwx ~/linux $ make -d O=../linux-build/ -n bzImage > ../linux-build/build.log

chenwx@chenwx ~/linux $ grep "Reading makefile" ../linux-build/build.log
Reading makefiles...
Reading makefile 'Makefile'...
Reading makefiles...
Reading makefile '/home/chenwx/linux/Makefile'...
Reading makefile 'scripts/Kbuild.include' (search path) (no ~ expansion)...
Reading makefile 'include/config/auto.conf' (search path) (don't care) (no ~ expansion)...
Reading makefile 'include/config/auto.conf.cmd' (search path) (don't care) (no ~ expansion)...
Reading makefile 'arch/x86/Makefile' (search path) (no ~ expansion)...
Reading makefile 'arch/x86/Makefile_32.cpu' (search path) (no ~ expansion)...
Reading makefile 'scripts/Makefile.gcc-plugins' (search path) (no ~ expansion)...
Reading makefile 'scripts/Makefile.kasan' (search path) (no ~ expansion)...
Reading makefile 'scripts/Makefile.extrawarn' (search path) (no ~ expansion)...
Reading makefile 'scripts/Makefile.ubsan' (search path) (no ~ expansion)...
Reading makefile '.vmlinux.cmd' (search path) (no ~ expansion)...
Reading makefiles...
Reading makefile '/home/chenwx/linux/scripts/Makefile.build'...
Reading makefile 'include/config/auto.conf' (search path) (don't care) (no ~ expansion)...
Reading makefile 'scripts/Kbuild.include' (search path) (no ~ expansion)...
Reading makefile '/home/chenwx/linux/arch/x86/entry/syscalls/Makefile' (search path) (no ~ expansion)...
Reading makefile 'scripts/Makefile.lib' (search path) (no ~ expansion)...
...
```

## Appendix C: Kconfig tree

```
linux-3.2/Kconfig
+- source "arch/$(SRCARCH)/Kconfig"	// 此处以x86体系为例，即source "arch/x86/Kconfig"
|  +- source "init/Kconfig"
|  |  +- source "kernel/irq/Kconfig"
|  |  +- source "usr/Kconfig"
|  |  +- source "arch/Kconfig"
|  |  |  +- source "kernel/gcov/Kconfig"
|  |  +- source "block/Kconfig"
|  |  |  +- source block/Kconfig.iosched
|  |  +- source "kernel/Kconfig.locks"
|  +- source "kernel/Kconfig.freezer"
|  +- source "kernel/time/Kconfig"
|  +- source "arch/x86/xen/Kconfig"
|  +- source "arch/x86/lguest/Kconfig"
|  +- source "arch/x86/Kconfig.cpu"
|  +- source "kernel/Kconfig.preempt"
|  +- source "mm/Kconfig"
|  +- source kernel/Kconfig.hz
|  +- source "kernel/power/Kconfig"
|  +- source "drivers/acpi/Kconfig"
|  +- source "drivers/sfi/Kconfig"
|  +- source "drivers/cpufreq/Kconfig"
|  +- source "drivers/cpuidle/Kconfig"
|  +- source "drivers/idle/Kconfig"
|  +- source "drivers/pci/pcie/Kconfig"
|  +- source "drivers/pci/Kconfig"
|  +- source "drivers/eisa/Kconfig"
|  +- source "drivers/mca/Kconfig"
|  +- source "drivers/pcmcia/Kconfig"
|  +- source "drivers/pci/hotplug/Kconfig"
|  +- source "drivers/rapidio/Kconfig"
|  +- source "fs/Kconfig.binfmt"
|  +- source "net/Kconfig"
|  |  +- source "net/packet/Kconfig"
|  |  +- source "net/unix/Kconfig"
|  |  +- source "net/xfrm/Kconfig"
|  |  +- source "net/iucv/Kconfig"
|  |  +- source "net/ipv4/Kconfig"
|  |  +- source "net/ipv6/Kconfig"
|  |  +- source "net/netlabel/Kconfig"
|  |  +- source "net/netfilter/Kconfig"
|  |  +- source "net/ipv4/netfilter/Kconfig"
|  |  +- source "net/ipv6/netfilter/Kconfig"
|  |  +- source "net/decnet/netfilter/Kconfig"
|  |  +- source "net/bridge/netfilter/Kconfig"
|  |  +- source "net/dccp/Kconfig"
|  |  +- source "net/sctp/Kconfig"
|  |  +- source "net/rds/Kconfig"
|  |  +- source "net/tipc/Kconfig"
|  |  +- source "net/atm/Kconfig"
|  |  +- source "net/l2tp/Kconfig"
|  |  +- source "net/802/Kconfig"
|  |  +- source "net/bridge/Kconfig"
|  |  +- source "net/dsa/Kconfig"
|  |  +- source "net/8021q/Kconfig"
|  |  +- source "net/decnet/Kconfig"
|  |  +- source "net/llc/Kconfig"
|  |  +- source "net/ipx/Kconfig"
|  |  +- source "drivers/net/appletalk/Kconfig"
|  |  +- source "net/x25/Kconfig"
|  |  +- source "net/lapb/Kconfig"
|  |  +- source "net/econet/Kconfig"
|  |  +- source "net/wanrouter/Kconfig"
|  |  +- source "net/phonet/Kconfig"
|  |  +- source "net/ieee802154/Kconfig"
|  |  +- source "net/sched/Kconfig"
|  |  +- source "net/dcb/Kconfig"
|  |  +- source "net/dns_resolver/Kconfig"
|  |  +- source "net/batman-adv/Kconfig"
|  |  +- source "net/ax25/Kconfig"
|  |  +- source "net/can/Kconfig"
|  |  +- source "net/irda/Kconfig"
|  |  +- source "net/bluetooth/Kconfig"
|  |  +- source "net/rxrpc/Kconfig"
|  |  +- source "net/wireless/Kconfig"
|  |  +- source "net/mac80211/Kconfig"
|  |  +- source "net/wimax/Kconfig"
|  |  +- source "net/rfkill/Kconfig"
|  |  +- source "net/9p/Kconfig"
|  |  +- source "net/caif/Kconfig"
|  |  +- source "net/ceph/Kconfig"
|  |  +- source "net/nfc/Kconfig"
|  +- source "drivers/Kconfig"
|  |  +- source "drivers/base/Kconfig"
|  |  +- source "drivers/connector/Kconfig"
|  |  +- source "drivers/mtd/Kconfig"
|  |  +- source "drivers/of/Kconfig"
|  |  +- source "drivers/parport/Kconfig"
|  |  +- source "drivers/pnp/Kconfig"
|  |  +- source "drivers/block/Kconfig"
|  |  +- source "drivers/misc/Kconfig"
|  |  +- source "drivers/ide/Kconfig"
|  |  +- source "drivers/scsi/Kconfig"
|  |  +- source "drivers/ata/Kconfig"
|  |  +- source "drivers/md/Kconfig"
|  |  +- source "drivers/target/Kconfig"
|  |  +- source "drivers/message/fusion/Kconfig"
|  |  +- source "drivers/firewire/Kconfig"
|  |  +- source "drivers/message/i2o/Kconfig"
|  |  +- source "drivers/macintosh/Kconfig"
|  |  +- source "drivers/net/Kconfig"
|  |  +- source "drivers/isdn/Kconfig"
|  |  +- source "drivers/telephony/Kconfig"
|  |  +- source "drivers/input/Kconfig"
|  |  +- source "drivers/char/Kconfig"
|  |  +- source "drivers/i2c/Kconfig"
|  |  +- source "drivers/spi/Kconfig"
|  |  +- source "drivers/pps/Kconfig"
|  |  +- source "drivers/ptp/Kconfig"
|  |  +- source "drivers/pinctrl/Kconfig"
|  |  +- source "drivers/gpio/Kconfig"
|  |  +- source "drivers/w1/Kconfig"
|  |  +- source "drivers/power/Kconfig"
|  |  +- source "drivers/hwmon/Kconfig"
|  |  +- source "drivers/thermal/Kconfig"
|  |  +- source "drivers/watchdog/Kconfig"
|  |  +- source "drivers/ssb/Kconfig"
|  |  +- source "drivers/bcma/Kconfig"
|  |  +- source "drivers/mfd/Kconfig"
|  |  +- source "drivers/regulator/Kconfig"
|  |  +- source "drivers/media/Kconfig"
|  |  +- source "drivers/video/Kconfig"
|  |  +- source "sound/Kconfig"
|  |  +- source "drivers/hid/Kconfig"
|  |  +- source "drivers/usb/Kconfig"
|  |  +- source "drivers/uwb/Kconfig"
|  |  +- source "drivers/mmc/Kconfig"
|  |  +- source "drivers/memstick/Kconfig"
|  |  +- source "drivers/leds/Kconfig"
|  |  +- source "drivers/accessibility/Kconfig"
|  |  +- source "drivers/infiniband/Kconfig"
|  |  +- source "drivers/edac/Kconfig"
|  |  +- source "drivers/rtc/Kconfig"
|  |  +- source "drivers/dma/Kconfig"
|  |  +- source "drivers/dca/Kconfig"
|  |  +- source "drivers/auxdisplay/Kconfig"
|  |  +- source "drivers/uio/Kconfig"
|  |  +- source "drivers/vlynq/Kconfig"
|  |  +- source "drivers/virtio/Kconfig"
|  |  +- source "drivers/xen/Kconfig"
|  |  +- source "drivers/staging/Kconfig"
|  |  +- source "drivers/platform/Kconfig"
|  |  +- source "drivers/clk/Kconfig"
|  |  +- source "drivers/hwspinlock/Kconfig"
|  |  +- source "drivers/clocksource/Kconfig"
|  |  +- source "drivers/iommu/Kconfig"
|  |  +- source "drivers/virt/Kconfig"
|  |  +- source "drivers/hv/Kconfig"
|  |  +- source "drivers/devfreq/Kconfig"
|  +- source "drivers/firmware/Kconfig"
|  +- source "fs/Kconfig"
|  |  +- source "fs/ext2/Kconfig"
|  |  +- source "fs/ext3/Kconfig"
|  |  +- source "fs/ext4/Kconfig"
|  |  +- source "fs/jbd/Kconfig"
|  |  +- source "fs/jbd2/Kconfig"
|  |  +- source "fs/reiserfs/Kconfig"
|  |  +- source "fs/jfs/Kconfig"
|  |  +- source "fs/xfs/Kconfig"
|  |  +- source "fs/gfs2/Kconfig"
|  |  +- source "fs/ocfs2/Kconfig"
|  |  +- source "fs/btrfs/Kconfig"
|  |  +- source "fs/nilfs2/Kconfig"
|  |  +- source "fs/notify/Kconfig"
|  |  +- source "fs/quota/Kconfig"
|  |  +- source "fs/autofs4/Kconfig"
|  |  +- source "fs/fuse/Kconfig"
|  |  +- source "fs/fscache/Kconfig"
|  |  +- source "fs/cachefiles/Kconfig"
|  |  +- source "fs/isofs/Kconfig"
|  |  +- source "fs/udf/Kconfig"
|  |  +- source "fs/fat/Kconfig"
|  |  +- source "fs/ntfs/Kconfig"
|  |  +- source "fs/proc/Kconfig"
|  |  +- source "fs/sysfs/Kconfig"
|  |  +- source "fs/configfs/Kconfig"
|  |  +- source "fs/adfs/Kconfig"
|  |  +- source "fs/affs/Kconfig"
|  |  +- source "fs/ecryptfs/Kconfig"
|  |  +- source "fs/hfs/Kconfig"
|  |  +- source "fs/hfsplus/Kconfig"
|  |  +- source "fs/befs/Kconfig"
|  |  +- source "fs/bfs/Kconfig"
|  |  +- source "fs/efs/Kconfig"
|  |  +- source "fs/jffs2/Kconfig"
|  |  +- source "fs/ubifs/Kconfig"
|  |  +- source "fs/logfs/Kconfig"
|  |  +- source "fs/cramfs/Kconfig"
|  |  +- source "fs/squashfs/Kconfig"
|  |  +- source "fs/freevxfs/Kconfig"
|  |  +- source "fs/minix/Kconfig"
|  |  +- source "fs/omfs/Kconfig"
|  |  +- source "fs/hpfs/Kconfig"
|  |  +- source "fs/qnx4/Kconfig"
|  |  +- source "fs/romfs/Kconfig"
|  |  +- source "fs/pstore/Kconfig"
|  |  +- source "fs/sysv/Kconfig"
|  |  +- source "fs/ufs/Kconfig"
|  |  +- source "fs/exofs/Kconfig"
|  |  +- source "fs/nfs/Kconfig"
|  |  +- source "fs/nfsd/Kconfig"
|  |  +- source "net/sunrpc/Kconfig"
|  |  +- source "fs/ceph/Kconfig"
|  |  +- source "fs/cifs/Kconfig"
|  |  +- source "fs/ncpfs/Kconfig"
|  |  +- source "fs/coda/Kconfig"
|  |  +- source "fs/afs/Kconfig"
|  |  +- source "fs/9p/Kconfig"
|  |  +- source "fs/partitions/Kconfig"
|  |  +- source "fs/nls/Kconfig"
|  |  +- source "fs/dlm/Kconfig"
|  +- source "arch/x86/Kconfig.debug"
|  |  +- source "lib/Kconfig.debug"
|  +- source "security/Kconfig"
|  |  +- source security/selinux/Kconfig
|  |  +- source security/smack/Kconfig
|  |  +- source security/tomoyo/Kconfig
|  |  +- source security/apparmor/Kconfig
|  |  +- source security/integrity/Kconfig
|  +- source "crypto/Kconfig"
|  |  +- source "crypto/async_tx/Kconfig"
|  |  +- source "drivers/crypto/Kconfig"
|  +- source "arch/x86/kvm/Kconfig"
|  |  +- source "virt/kvm/Kconfig"
|  |  +- source drivers/vhost/Kconfig
|  |  +- source drivers/lguest/Kconfig
|  +- source "lib/Kconfig"
|  |  +- source "lib/xz/Kconfig"
```

## Appendix D: make -f scripts/Makefile.modbuiltin obj=列表

```
make -f scripts/Makefile.modbuiltin obj=init
make -f scripts/Makefile.modbuiltin obj=usr
make -f scripts/Makefile.modbuiltin obj=arch/x86
make -f scripts/Makefile.modbuiltin obj=arch/x86/crypto
make -f scripts/Makefile.modbuiltin obj=arch/x86/kernel
make -f scripts/Makefile.modbuiltin obj=arch/x86/kernel/acpi
make -f scripts/Makefile.modbuiltin obj=arch/x86/kernel/apic
make -f scripts/Makefile.modbuiltin obj=arch/x86/kernel/cpu
make -f scripts/Makefile.modbuiltin obj=arch/x86/kernel/cpu/mcheck
make -f scripts/Makefile.modbuiltin obj=arch/x86/kernel/cpu/mtrr
make -f scripts/Makefile.modbuiltin obj=arch/x86/mm
make -f scripts/Makefile.modbuiltin obj=arch/x86/net
make -f scripts/Makefile.modbuiltin obj=arch/x86/platform
make -f scripts/Makefile.modbuiltin obj=arch/x86/platform/ce4100
make -f scripts/Makefile.modbuiltin obj=arch/x86/platform/efi
make -f scripts/Makefile.modbuiltin obj=arch/x86/platform/geode
make -f scripts/Makefile.modbuiltin obj=arch/x86/platform/iris
make -f scripts/Makefile.modbuiltin obj=arch/x86/platform/mrst
make -f scripts/Makefile.modbuiltin obj=arch/x86/platform/olpc
make -f scripts/Makefile.modbuiltin obj=arch/x86/platform/scx200
make -f scripts/Makefile.modbuiltin obj=arch/x86/platform/sfi
make -f scripts/Makefile.modbuiltin obj=arch/x86/platform/uv
make -f scripts/Makefile.modbuiltin obj=arch/x86/platform/visws
make -f scripts/Makefile.modbuiltin obj=arch/x86/vdso
make -f scripts/Makefile.modbuiltin obj=kernel
make -f scripts/Makefile.modbuiltin obj=kernel/events
make -f scripts/Makefile.modbuiltin obj=kernel/gcov
make -f scripts/Makefile.modbuiltin obj=kernel/irq
make -f scripts/Makefile.modbuiltin obj=kernel/power
make -f scripts/Makefile.modbuiltin obj=kernel/time
make -f scripts/Makefile.modbuiltin obj=kernel/trace
make -f scripts/Makefile.modbuiltin obj=mm
make -f scripts/Makefile.modbuiltin obj=fs
make -f scripts/Makefile.modbuiltin obj=fs/debugfs
make -f scripts/Makefile.modbuiltin obj=fs/devpts
make -f scripts/Makefile.modbuiltin obj=fs/exofs
make -f scripts/Makefile.modbuiltin obj=fs/exportfs
make -f scripts/Makefile.modbuiltin obj=fs/nls
make -f scripts/Makefile.modbuiltin obj=fs/notify
make -f scripts/Makefile.modbuiltin obj=fs/notify/dnotify
make -f scripts/Makefile.modbuiltin obj=fs/notify/fanotify
make -f scripts/Makefile.modbuiltin obj=fs/notify/inotify
make -f scripts/Makefile.modbuiltin obj=fs/partitions
make -f scripts/Makefile.modbuiltin obj=fs/proc
make -f scripts/Makefile.modbuiltin obj=fs/quota
make -f scripts/Makefile.modbuiltin obj=fs/ramfs
make -f scripts/Makefile.modbuiltin obj=fs/sysfs
make -f scripts/Makefile.modbuiltin obj=ipc
make -f scripts/Makefile.modbuiltin obj=security
make -f scripts/Makefile.modbuiltin obj=crypto
make -f scripts/Makefile.modbuiltin obj=block
make -f scripts/Makefile.modbuiltin obj=drivers
make -f scripts/Makefile.modbuiltin obj=drivers/accessibility
make -f scripts/Makefile.modbuiltin obj=drivers/accessibility/braille
make -f scripts/Makefile.modbuiltin obj=drivers/acpi
make -f scripts/Makefile.modbuiltin obj=drivers/acpi/acpica
make -f scripts/Makefile.modbuiltin obj=drivers/auxdisplay
make -f scripts/Makefile.modbuiltin obj=drivers/base
make -f scripts/Makefile.modbuiltin obj=drivers/base/power
make -f scripts/Makefile.modbuiltin obj=drivers/base/regmap
make -f scripts/Makefile.modbuiltin obj=drivers/block
make -f scripts/Makefile.modbuiltin obj=drivers/cdrom
make -f scripts/Makefile.modbuiltin obj=drivers/char
make -f scripts/Makefile.modbuiltin obj=drivers/clk
make -f scripts/Makefile.modbuiltin obj=drivers/clocksource
make -f scripts/Makefile.modbuiltin obj=drivers/cpufreq
make -f scripts/Makefile.modbuiltin obj=drivers/cpuidle
make -f scripts/Makefile.modbuiltin obj=drivers/cpuidle/governors
make -f scripts/Makefile.modbuiltin obj=drivers/crypto
make -f scripts/Makefile.modbuiltin obj=drivers/dma
make -f scripts/Makefile.modbuiltin obj=drivers/edac
make -f scripts/Makefile.modbuiltin obj=drivers/firewire
make -f scripts/Makefile.modbuiltin obj=drivers/firmware
make -f scripts/Makefile.modbuiltin obj=drivers/firmware/google
make -f scripts/Makefile.modbuiltin obj=drivers/gpio
make -f scripts/Makefile.modbuiltin obj=drivers/gpu
make -f scripts/Makefile.modbuiltin obj=drivers/gpu/drm
make -f scripts/Makefile.modbuiltin obj=drivers/gpu/drm/i2c
make -f scripts/Makefile.modbuiltin obj=drivers/gpu/stub
make -f scripts/Makefile.modbuiltin obj=drivers/gpu/vga
make -f scripts/Makefile.modbuiltin obj=drivers/i2c
make -f scripts/Makefile.modbuiltin obj=drivers/i2c/algos
make -f scripts/Makefile.modbuiltin obj=drivers/i2c/busses
make -f scripts/Makefile.modbuiltin obj=drivers/i2c/muxes
make -f scripts/Makefile.modbuiltin obj=drivers/idle
make -f scripts/Makefile.modbuiltin obj=drivers/ieee802154
make -f scripts/Makefile.modbuiltin obj=drivers/input
make -f scripts/Makefile.modbuiltin obj=drivers/input/joystick
make -f scripts/Makefile.modbuiltin obj=drivers/input/keyboard
make -f scripts/Makefile.modbuiltin obj=drivers/input/misc
make -f scripts/Makefile.modbuiltin obj=drivers/input/serio
make -f scripts/Makefile.modbuiltin obj=drivers/iommu
make -f scripts/Makefile.modbuiltin obj=drivers/isdn
make -f scripts/Makefile.modbuiltin obj=drivers/isdn/hardware
make -f scripts/Makefile.modbuiltin obj=drivers/isdn/hardware/avm
make -f scripts/Makefile.modbuiltin obj=drivers/isdn/hardware/eicon
make -f scripts/Makefile.modbuiltin obj=drivers/leds
make -f scripts/Makefile.modbuiltin obj=drivers/lguest
make -f scripts/Makefile.modbuiltin obj=drivers/macintosh
make -f scripts/Makefile.modbuiltin obj=drivers/md
make -f scripts/Makefile.modbuiltin obj=drivers/media
make -f scripts/Makefile.modbuiltin obj=drivers/media/common
make -f scripts/Makefile.modbuiltin obj=drivers/media/common/tuners
make -f scripts/Makefile.modbuiltin obj=drivers/media/rc
make -f scripts/Makefile.modbuiltin obj=drivers/media/rc/keymaps
make -f scripts/Makefile.modbuiltin obj=drivers/media/video
make -f scripts/Makefile.modbuiltin obj=drivers/media/video/davinci
make -f scripts/Makefile.modbuiltin obj=drivers/mfd
make -f scripts/Makefile.modbuiltin obj=drivers/misc
make -f scripts/Makefile.modbuiltin obj=drivers/misc/carma
make -f scripts/Makefile.modbuiltin obj=drivers/misc/cb710
make -f scripts/Makefile.modbuiltin obj=drivers/misc/eeprom
make -f scripts/Makefile.modbuiltin obj=drivers/misc/lis3lv02d
make -f scripts/Makefile.modbuiltin obj=drivers/misc/ti-st
make -f scripts/Makefile.modbuiltin obj=drivers/net
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/3com
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/8390
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/amd
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/atheros
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/broadcom
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/fujitsu
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/intel
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/marvell
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/mellanox
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/natsemi
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/oki-semi
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/packetengines
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/qlogic
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/racal
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/rdc
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/sis
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/smsc
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/stmicro
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/sun
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/ti
make -f scripts/Makefile.modbuiltin obj=drivers/net/ethernet/via
make -f scripts/Makefile.modbuiltin obj=drivers/net/wan
make -f scripts/Makefile.modbuiltin obj=drivers/net/wireless
make -f scripts/Makefile.modbuiltin obj=drivers/nfc
make -f scripts/Makefile.modbuiltin obj=drivers/pci
make -f scripts/Makefile.modbuiltin obj=drivers/pci/pcie
make -f scripts/Makefile.modbuiltin obj=drivers/pci/pcie/aer
make -f scripts/Makefile.modbuiltin obj=drivers/pinctrl
make -f scripts/Makefile.modbuiltin obj=drivers/platform
make -f scripts/Makefile.modbuiltin obj=drivers/platform/x86
make -f scripts/Makefile.modbuiltin obj=drivers/pnp
make -f scripts/Makefile.modbuiltin obj=drivers/pnp/isapnp
make -f scripts/Makefile.modbuiltin obj=drivers/pnp/pnpacpi
make -f scripts/Makefile.modbuiltin obj=drivers/tty
make -f scripts/Makefile.modbuiltin obj=drivers/tty/ipwireless
make -f scripts/Makefile.modbuiltin obj=drivers/tty/serial
make -f scripts/Makefile.modbuiltin obj=drivers/tty/vt
make -f scripts/Makefile.modbuiltin obj=drivers/usb
make -f scripts/Makefile.modbuiltin obj=drivers/usb/early
make -f scripts/Makefile.modbuiltin obj=drivers/usb/host
make -f scripts/Makefile.modbuiltin obj=drivers/video
make -f scripts/Makefile.modbuiltin obj=drivers/video/backlight
make -f scripts/Makefile.modbuiltin obj=drivers/video/console
make -f scripts/Makefile.modbuiltin obj=drivers/video/display
make -f scripts/Makefile.modbuiltin obj=drivers/video/omap2
make -f scripts/Makefile.modbuiltin obj=drivers/video/omap2/displays
make -f scripts/Makefile.modbuiltin obj=drivers/watchdog
make -f scripts/Makefile.modbuiltin obj=sound
make -f scripts/Makefile.modbuiltin obj=firmware
make -f scripts/Makefile.modbuiltin obj=arch/x86/pci
make -f scripts/Makefile.modbuiltin obj=arch/x86/power
make -f scripts/Makefile.modbuiltin obj=arch/x86/video
make -f scripts/Makefile.modbuiltin obj=net
make -f scripts/Makefile.modbuiltin obj=net/802
make -f scripts/Makefile.modbuiltin obj=net/8021q
make -f scripts/Makefile.modbuiltin obj=net/core
make -f scripts/Makefile.modbuiltin obj=net/ethernet
make -f scripts/Makefile.modbuiltin obj=net/ipv6
make -f scripts/Makefile.modbuiltin obj=net/ipv6/netfilter
make -f scripts/Makefile.modbuiltin obj=net/netfilter
make -f scripts/Makefile.modbuiltin obj=net/netlink
make -f scripts/Makefile.modbuiltin obj=net/sched
make -f scripts/Makefile.modbuiltin obj=net/wireless
make -f scripts/Makefile.modbuiltin obj=net/xfrm
make -f scripts/Makefile.modbuiltin obj=lib
make -f scripts/Makefile.modbuiltin obj=lib/lzo
make -f scripts/Makefile.modbuiltin obj=arch/x86/lib
```

## Appendix E: arch目录下处理器体系架构介绍

**alpha处理器**

Alpha处理器最早由美国DEC公司设计制造，在Compaq(康柏)公司收购DEC之后，Alpha处理器继续得到发展，并且应用于许多高档的Compaq服务器上，HP(惠普)收购Compaq后，Alpha便为HP(惠普)所有，不过HP(惠普)已经放弃发展alpha 处理器。

**arm处理器**

Arm系列处理器是英国Arm公司设计的主流嵌入式32位RISC处理器，Arm公司不直接生产Arm处理器，而是采用IP授权的方式由第三方开发生产，著名的公司如Ti、Samsung等都有出品Arm处理器。目前在手机领域广泛应用。

**avr32处理器**

Avr32处理器是美国Atmel公司设计开发的32位RISC处理器，设计目的是在每一个时钟周期内完成更多处理工作，从而在较低的时钟频率下实现相同的吞吐量。适合在工业控制、汽车电子等嵌入式设备领域中使用。Avr32属于MCU(Micro Control Unit)型处理器。

**blackfin处理器**

Blackfin处理器是美国ADI公司开发的具有DSP能力的32位RISC处理器，Blackfin处理器基于由ADI和Intel公司联合开发的微信号架构(MSA)，适用于嵌入式音频、视频和通信应用等领域。

**cris处理器**

Cris处理器是瑞典Axis通信公司开发的32位RISC处理器，主要用于网络设备，属于比较专业的应用领域。因为Axis通信公司主要开发网络监控设备，所以Cris处理器在其网络监控设备中应用广泛。

**frv处理器**

Frv处理器是日本富士通开发的32位高性能RISC处理器，采用VLIW(Very Long Instruction Word)构架，具备良好的多媒体处理能力，在机顶盒(STB)、数码刻录机(DVR)、数码相机(DSC)等嵌入式领域应用广泛。

**h8300处理器**

H8300处理器是日本瑞萨科技开发的32位高性能RISC处理器，具有强大的位操作指令，最适于实时控制应用如汽车电子、家用电器、医疗器械等领域。H8300属于MCU型的处理器。

**hexagon处理器**

Hexagon is a DSP based CPU architecture developed by Qualcomm. It uses VLIW and is capable of dispatching up to 4 instructions to 4 Execution Units every clock. The Hexagon architecture is designed to deliver performance with low power over a variety of applications. It has features such as multithreading, privilege levels, VLIW, SIMD, and instructions geared toward efficient signal processing. The port of Linux for Hexagon runs under a hypervisor layer and was merged with the 3.2 release of the kernel. Support for Hexagon was added in 3.1 release of LLVM by Tony Linthicum. There is also a non-FSF maintained branch of GCC. Hexagon DSPs are included in Snapdragon SoC since 2006. In Snapdragon S4 (MSM8960 and newer) there are three Hexagon cores, two in the Modem subsystem and one in the Multimedia subsystem. There are four generations of DSP architecture: H1 (2006), H2 (2007-2008), H3 (2009), H4 (2010-2011). H4 has 20 DMIPS per milliwatt, works with frequency 500 MHz. Clock speed of Hexagon varies in 400-600 MHz for QDSP6 and in 256-350 MHz for QDSP5.

**ia64处理器**

Ia64处理器是美国英特尔开发的面向服务器应用的64位处理器，由于具有64位寻址能力，它能够使用100万TB的地址空间，足以运算企业级或超大规模的数据库任务；64位宽的寄存器可以使CPU浮点运算达到非常高的精度。

**m32r处理器**

M32r处理器是日本瑞萨科技开发的32位高性能RISC处理器，内置大容量存储器，适用于车载系统、数字AV设备、数字成像设备等产品领域。属于MCU型的处理器。

**m68k处理器**

M68k处理器是美国Motorola公司开发的高性能处理器，具有高性价比、高集成度等特点，在工业自动化设备、控制设备、医疗仪器系统、安全系统等领域多有应用。现在为Freescale公司所有，风头已不敌PowerPC处理器。

**microblaze处理器**

Microblaze处理器是美国Xilinx公司提供的嵌入在其FPGA芯片上的32位RISC软核。 它具有运算能力强、外围接口配置灵活等特点，集成在FPGA中，可以和FPGA实现协同设计，具备软硬件可配置的灵活性。

**mips处理器**

Mips处理器是由美国斯坦福大学Hennessy教授领导的研究小组研制出来，现为Mips公司拥有，和Arm处理器一样采用IP授权的方式由第三方开发生产。著名的公司如Broadcom、Nxp等都有出品Mips处理器。我国的龙芯CPU也是采用Mips体系结构。

**mn10300处理器**

Mn10300处理器是日本松下开发的32位多媒体处理器。

**openrisc处理器**

OpenRisc是OpenCores组织提供的基于GPL协议的开放源代码的RISC(精简指令集计算机)处理器。有人认为其性能介于ARM7和ARM9之间，适合一般的嵌入式系统使用。最重要的一点是OpenCores组织提供了大量的开放源代码IP核供研究人员使用，因此对于一般的开发单位具有很大的吸引力。

**parisc处理器**

Parisc处理器是由HP(惠普)开发设计的处理器，主要用于HP(惠普)公司的服务器中，目前HP(惠普)已经放弃Parisc处理器的开发，不过一些Parisc处理器技术已经融合到ia64处理器之中。

**powerpc处理器**

Powerpc处理器是由美国IBM、Apple、Motorola联合开发的处理器，Powepc处理器在IBM的服务器、Apple的MAC电脑中都有应用。不过现在多应用在网络设备、视频系统、工业系统等领域。Sony PS3游戏机的Cell处理器也是Powerpc体系结构。

**s390处理器**

S390处理器是由美国IBM开发的面向大型机应用的处理器。

**score处理器**

Score处理器是由台湾凌阳开发的32位RISC处理器。Score属于MCU型处理器。

**sh处理器**

Sh处理器又称SuperH处理器，最先由日本Hitachi公司开发，后由Hitachi及ST Microelectronics两家公司共同开发，2003年瑞萨科技从Hitachi公司继承到拥有权。Sh属于MCU型处理器。

**sparc处理器**

Sparc处理器是由美国SUN和TI公司共同开发的RISC微处理器，最突出的特点是它的可扩展性。SUN公司将它做为高端处理器应用到服务器产品。

**tile处理器**

-

**um处理器**

-

**unicore32处理器**

-

**x86处理器**

X86处理器是由美国Intel推出的复杂指令集(cisc)处理器，广泛应用在PC电脑领域和服务器领域，在工业控制领域也有应用。目前主要是Intel、AMD、VIA在开发x86体系结构的处理器。

**xtensa处理器**

Xtensa处理器是由美国Tensilica(泰思立达)公司开发的可配置及可扩展的微处理器。

## Appendix F: vmlinux.lds.S

```
/*
 * ld script for the x86 kernel
 *
 * Historic 32-bit version written by Martin Mares <mj@atrey.karlin.mff.cuni.cz>
 *
 * Modernisation, unification and other changes and fixes:
 *   Copyright (C) 2007-2009  Sam Ravnborg <sam@ravnborg.org>
 *
 *
 * Don't define absolute symbols until and unless you know that symbol
 * value is should remain constant even if kernel image is relocated
 * at run time. Absolute symbols are not relocated. If symbol value should
 * change if kernel is relocated, make the symbol section relative and
 * put it inside the section definition.
 */

#ifdef CONFIG_X86_32
/*
 * See arch/x86/include/asm/page_32_types.h for __PAGE_OFFSET,
 * 由.config中的配置CONFIG_PAGE_OFFSET有关
 */
#define LOAD_OFFSET __PAGE_OFFSET
#else
/*
 * See arch/x86/include/asm/page_64_types.h
 * for __START_KERNEL_map
 */
#define LOAD_OFFSET __START_KERNEL_map
#endif

#include <asm-generic/vmlinux.lds.h>
#include <asm/asm-offsets.h>
#include <asm/thread_info.h>
#include <asm/page_types.h>
#include <asm/cache.h>
#include <asm/boot.h>

#undef i386     /* in case the preprocessor is a 32bit one */

// Alex Note: See .config for CONFIG_OUTPUT_FORMAT
OUTPUT_FORMAT(CONFIG_OUTPUT_FORMAT, CONFIG_OUTPUT_FORMAT, CONFIG_OUTPUT_FORMAT)

#ifdef CONFIG_X86_32
OUTPUT_ARCH(i386)		// Refer to output of linux command 'objdump -i'
ENTRY(phys_startup_32)	// See System.map
jiffies = jiffies_64;
#else
OUTPUT_ARCH(i386:x86-64)
ENTRY(phys_startup_64)
jiffies_64 = jiffies;
#endif

#if defined(CONFIG_X86_64) && defined(CONFIG_DEBUG_RODATA)
/*
 * On 64-bit, align RODATA to 2MB so that even with CONFIG_DEBUG_RODATA
 * we retain large page mappings for boundaries spanning kernel text, rodata
 * and data sections.
 *
 * However, kernel identity mappings will have different RWX permissions
 * to the pages mapping to text and to the pages padding (which are freed) the
 * text section. Hence kernel identity mappings will be broken to smaller
 * pages. For 64-bit, kernel text and kernel identity mappings are different,
 * so we can enable protection checks that come with CONFIG_DEBUG_RODATA,
 * as well as retain 2MB large page mappings for kernel text.
 */
#define X64_ALIGN_DEBUG_RODATA_BEGIN	. = ALIGN(HPAGE_SIZE);

#define X64_ALIGN_DEBUG_RODATA_END		\
		. = ALIGN(HPAGE_SIZE);		\
		__end_rodata_hpage_align = .;

#else

#define X64_ALIGN_DEBUG_RODATA_BEGIN
#define X64_ALIGN_DEBUG_RODATA_END

#endif

PHDRS {
	text PT_LOAD FLAGS(5);          /* R_E */	// 代码段配置，可加载，可读可执行
	data PT_LOAD FLAGS(6);          /* RW_ */	// 数据段配置，可加载，可读可写
#ifdef CONFIG_X86_64
#ifdef CONFIG_SMP
	percpu PT_LOAD FLAGS(6);        /* RW_ */
#endif
	init PT_LOAD FLAGS(7);          /* RWE */
#endif
	note PT_NOTE FLAGS(0);          /* ___ */	// 注释段配置
}

SECTIONS
{
#ifdef CONFIG_X86_32
		/*
		 * LOAD_PHYSICAL_ADDR定义于arch\x86\include\asm\boot.h
		 * 由CONFIG_PHYSICAL_START、CONFIG_PHYSICAL_ALIGN计算而来
		 */
        . = LOAD_OFFSET + LOAD_PHYSICAL_ADDR;
        phys_startup_32 = startup_32 - LOAD_OFFSET;
#else
        . = __START_KERNEL;
        phys_startup_64 = startup_64 - LOAD_OFFSET;
#endif

	/* Text and read-only data */
	.text :  AT(ADDR(.text) - LOAD_OFFSET) {
		_text = .;
		/* bootstrapping code */
		HEAD_TEXT				// See include/asm-generic/vmlinux.lds.h
#ifdef CONFIG_X86_32
		. = ALIGN(PAGE_SIZE);		// See arch/x86/include/asm/page_types.h
		*(.text..page_aligned)
#endif
		. = ALIGN(8);
		_stext = .;
		TEXT_TEXT				// See include/asm-generic/vmlinux.lds.h
		SCHED_TEXT				// See include/asm-generic/vmlinux.lds.h
		LOCK_TEXT				// See include/asm-generic/vmlinux.lds.h
		KPROBES_TEXT			// See include/asm-generic/vmlinux.lds.h
		ENTRY_TEXT				// See include/asm-generic/vmlinux.lds.h
		IRQENTRY_TEXT			// See include/asm-generic/vmlinux.lds.h
		*(.fixup)
		*(.gnu.warning)
		/* End of text section */
		_etext = .;
	} :text = 0x9090

	NOTES :text :note

	EXCEPTION_TABLE(16) :text = 0x9090

#if defined(CONFIG_DEBUG_RODATA)
	/* .text should occupy whole number of pages */
	. = ALIGN(PAGE_SIZE);
#endif
	X64_ALIGN_DEBUG_RODATA_BEGIN
	RO_DATA(PAGE_SIZE)
	X64_ALIGN_DEBUG_RODATA_END

	/* Data */
	.data : AT(ADDR(.data) - LOAD_OFFSET) {
		/* Start of data section */
		_sdata = .;

		/* init_task */
		INIT_TASK_DATA(THREAD_SIZE)

#ifdef CONFIG_X86_32
		/* 32 bit has nosave before _edata */
		NOSAVE_DATA
#endif

		PAGE_ALIGNED_DATA(PAGE_SIZE)

		CACHELINE_ALIGNED_DATA(L1_CACHE_BYTES)

		DATA_DATA
		CONSTRUCTORS

		/* rarely changed data like cpu maps */
		READ_MOSTLY_DATA(INTERNODE_CACHE_BYTES)

		/* End of data section */
		_edata = .;
	} :data

#ifdef CONFIG_X86_64

	. = ALIGN(PAGE_SIZE);
	__vvar_page = .;

	.vvar : AT(ADDR(.vvar) - LOAD_OFFSET) {
		/* work around gold bug 13023 */
		__vvar_beginning_hack = .;

		/* Place all vvars at the offsets in asm/vvar.h. */
#define EMIT_VVAR(name, offset) 				\
		. = __vvar_beginning_hack + offset;	\
		*(.vvar_ ## name)
#define __VVAR_KERNEL_LDS
#include <asm/vvar.h>
#undef __VVAR_KERNEL_LDS
#undef EMIT_VVAR

	} :data

       . = ALIGN(__vvar_page + PAGE_SIZE, PAGE_SIZE);

#endif /* CONFIG_X86_64 */

	/* Init code and data - will be freed after init */
	. = ALIGN(PAGE_SIZE);
	.init.begin : AT(ADDR(.init.begin) - LOAD_OFFSET) {
		__init_begin = .; /* paired with __init_end */
	}

#if defined(CONFIG_X86_64) && defined(CONFIG_SMP)
	/*
	 * percpu offsets are zero-based on SMP.  PERCPU_VADDR() changes the
	 * output PHDR, so the next output section - .init.text - should
	 * start another segment - init.
	 */
	PERCPU_VADDR(INTERNODE_CACHE_BYTES, 0, :percpu)
#endif

	INIT_TEXT_SECTION(PAGE_SIZE)
#ifdef CONFIG_X86_64
	:init
#endif

	INIT_DATA_SECTION(16)

	.x86_cpu_dev.init : AT(ADDR(.x86_cpu_dev.init) - LOAD_OFFSET) {
		__x86_cpu_dev_start = .;
		*(.x86_cpu_dev.init)
		__x86_cpu_dev_end = .;
	}

	/*
	 * start address and size of operations which during runtime
	 * can be patched with virtualization friendly instructions or
	 * baremetal native ones. Think page table operations.
	 * Details in paravirt_types.h
	 */
	. = ALIGN(8);
	.parainstructions : AT(ADDR(.parainstructions) - LOAD_OFFSET) {
		__parainstructions = .;
		*(.parainstructions)
		__parainstructions_end = .;
	}

	/*
	 * struct alt_inst entries. From the header (alternative.h):
	 * "Alternative instructions for different CPU types or capabilities"
	 * Think locking instructions on spinlocks.
	 */
	. = ALIGN(8);
	.altinstructions : AT(ADDR(.altinstructions) - LOAD_OFFSET) {
		__alt_instructions = .;
		*(.altinstructions)
		__alt_instructions_end = .;
	}

	/*
	 * And here are the replacement instructions. The linker sticks
	 * them as binary blobs. The .altinstructions has enough data to
	 * get the address and the length of them to patch the kernel safely.
	 */
	.altinstr_replacement : AT(ADDR(.altinstr_replacement) - LOAD_OFFSET) {
		*(.altinstr_replacement)
	}

	/*
	 * struct iommu_table_entry entries are injected in this section.
	 * It is an array of IOMMUs which during run time gets sorted depending
	 * on its dependency order. After rootfs_initcall is complete
	 * this section can be safely removed.
	 */
	.iommu_table : AT(ADDR(.iommu_table) - LOAD_OFFSET) {
		__iommu_table = .;
		*(.iommu_table)
		__iommu_table_end = .;
	}

	. = ALIGN(8);
	.apicdrivers : AT(ADDR(.apicdrivers) - LOAD_OFFSET) {
		__apicdrivers = .;
		*(.apicdrivers);
		__apicdrivers_end = .;
	}

	. = ALIGN(8);
	/*
	 * .exit.text is discard at runtime, not link time, to deal with
	 *  references from .altinstructions and .eh_frame
	 */
	.exit.text : AT(ADDR(.exit.text) - LOAD_OFFSET) {
		EXIT_TEXT
	}

	.exit.data : AT(ADDR(.exit.data) - LOAD_OFFSET) {
		EXIT_DATA
	}

#if !defined(CONFIG_X86_64) || !defined(CONFIG_SMP)
	PERCPU_SECTION(INTERNODE_CACHE_BYTES)
#endif

	. = ALIGN(PAGE_SIZE);

	/* freed after init ends here */
	.init.end : AT(ADDR(.init.end) - LOAD_OFFSET) {
		__init_end = .;
	}

	/*
	 * smp_locks might be freed after init
	 * start/end must be page aligned
	 */
	. = ALIGN(PAGE_SIZE);
	.smp_locks : AT(ADDR(.smp_locks) - LOAD_OFFSET) {
		__smp_locks = .;
		*(.smp_locks)
		. = ALIGN(PAGE_SIZE);
		__smp_locks_end = .;
	}

#ifdef CONFIG_X86_64
	.data_nosave : AT(ADDR(.data_nosave) - LOAD_OFFSET) {
		NOSAVE_DATA
	}
#endif

	/* BSS */
	. = ALIGN(PAGE_SIZE);
	.bss : AT(ADDR(.bss) - LOAD_OFFSET) {
		__bss_start = .;
		*(.bss..page_aligned)
		*(.bss)
		. = ALIGN(PAGE_SIZE);
		__bss_stop = .;
	}

	. = ALIGN(PAGE_SIZE);
	.brk : AT(ADDR(.brk) - LOAD_OFFSET) {
		__brk_base = .;
		. += 64 * 1024;		/* 64k alignment slop space */
		*(.brk_reservation)	/* areas brk users have reserved */
		__brk_limit = .;
	}

	_end = .;

     STABS_DEBUG
     DWARF_DEBUG

	/* Sections to be discarded */
	DISCARDS
	/DISCARD/ : { *(.eh_frame) }
}


#ifdef CONFIG_X86_32
/*
 * The ASSERT() sink to . is intentional, for binutils 2.14 compatibility:
 */
. = ASSERT((_end - LOAD_OFFSET <= KERNEL_IMAGE_SIZE),
	   "kernel image bigger than KERNEL_IMAGE_SIZE");
#else
/*
 * Per-cpu symbols which need to be offset from __per_cpu_load
 * for the boot processor.
 */
#define INIT_PER_CPU(x) init_per_cpu__##x = x + __per_cpu_load
INIT_PER_CPU(gdt_page);
INIT_PER_CPU(irq_stack_union);

/*
 * Build-time check on the image size:
 */
. = ASSERT((_end - _text <= KERNEL_IMAGE_SIZE),
	   "kernel image bigger than KERNEL_IMAGE_SIZE");

#ifdef CONFIG_SMP
. = ASSERT((irq_stack_union == 0),
           "irq_stack_union is not at start of per-cpu area");
#endif

#endif /* CONFIG_X86_32 */

#ifdef CONFIG_KEXEC
#include <asm/kexec.h>

. = ASSERT(kexec_control_code_size <= KEXEC_CONTROL_CODE_MAX_SIZE,
           "kexec control code size is too big");
#endif
```

## Appendix G: vmlinux.lds

vmlinux.lds是由vmlinux.lds.S经过预处理而生成的文件，用于链接器ld连接.o文件时的link script。该文件的生成过程参见$(vmlinux-lds)节，其具体内容如下：

```
OUTPUT_FORMAT("elf32-i386", "elf32-i386", "elf32-i386")
OUTPUT_ARCH(i386)
ENTRY(phys_startup_32)
jiffies = jiffies_64;

PHDRS {
  text PT_LOAD FLAGS(5); /* R_E */
  data PT_LOAD FLAGS(6); /* RW_ */
  note PT_NOTE FLAGS(0); /* ___ */
}

SECTIONS
{
  . = 0xC0000000 + ((0x1000000 + (0x1000000 - 1)) & ~(0x1000000 - 1));
  phys_startup_32 = startup_32 - 0xC0000000;

  /* Text and read-only data */
  .text : AT(ADDR(.text) - 0xC0000000) {
    _text = .;
    /* bootstrapping code */
    *(.head.text)
    . = ALIGN((1 << 12));
    *(.text..page_aligned)
    . = ALIGN(8);
    _stext = .;
    . = ALIGN(8); *(.text.hot) *(.text) *(.ref.text) *(.devinit.text) *(.devexit.text) *(.text.unlikely)
    . = ALIGN(8); __sched_text_start = .; *(.sched.text) __sched_text_end = .;
    . = ALIGN(8); __lock_text_start = .; *(.spinlock.text) __lock_text_end = .;
    . = ALIGN(8); __kprobes_text_start = .; *(.kprobes.text) __kprobes_text_end = .;
    . = ALIGN(8); __entry_text_start = .; *(.entry.text) __entry_text_end = .;

    *(.fixup)
    *(.gnu.warning)
    /* End of text section */
    _etext = .;
  } :text = 0x9090

  .notes : AT(ADDR(.notes) - 0xC0000000) { __start_notes = .; *(.note.*) __stop_notes = .; } :text :note
  . = ALIGN(16); __ex_table : AT(ADDR(__ex_table) - 0xC0000000) { __start___ex_table = .; *(__ex_table) __stop___ex_table = .; } :text = 0x9090

  . = ALIGN(((1 << 12))); .rodata : AT(ADDR(.rodata) - 0xC0000000) { __start_rodata = .; *(.rodata) *(.rodata.*) *(__vermagic) . = ALIGN(8); __start___tracepoints_ptrs = .; *(__tracepoints_ptrs) __stop___tracepoints_ptrs = .; *(__tracepoints_strings) } .rodata1 : AT(ADDR(.rodata1) - 0xC0000000) { *(.rodata1) } . = ALIGN(8); __bug_table : AT(ADDR(__bug_table) - 0xC0000000) { __start___bug_table = .; *(__bug_table) __stop___bug_table = .; } .pci_fixup : AT(ADDR(.pci_fixup) - 0xC0000000) { __start_pci_fixups_early = .; *(.pci_fixup_early) __end_pci_fixups_early = .; __start_pci_fixups_header = .; *(.pci_fixup_header) __end_pci_fixups_header = .; __start_pci_fixups_final = .; *(.pci_fixup_final) __end_pci_fixups_final = .; __start_pci_fixups_enable = .; *(.pci_fixup_enable) __end_pci_fixups_enable = .; __start_pci_fixups_resume = .; *(.pci_fixup_resume) __end_pci_fixups_resume = .; __start_pci_fixups_resume_early = .; *(.pci_fixup_resume_early) __end_pci_fixups_resume_early = .; __start_pci_fixups_suspend = .; *(.pci_fixup_suspend) __end_pci_fixups_suspend = .; } .builtin_fw : AT(ADDR(.builtin_fw) - 0xC0000000) { __start_builtin_fw = .; *(.builtin_fw) __end_builtin_fw = .; } .rio_ops : AT(ADDR(.rio_ops) - 0xC0000000) { __start_rio_switch_ops = .; *(.rio_switch_ops) __end_rio_switch_ops = .; } . = ALIGN(4); .tracedata : AT(ADDR(.tracedata) - 0xC0000000) { __tracedata_start = .; *(.tracedata) __tracedata_end = .; } __ksymtab : AT(ADDR(__ksymtab) - 0xC0000000) { __start___ksymtab = .; *(SORT(___ksymtab+*)) __stop___ksymtab = .; } __ksymtab_gpl : AT(ADDR(__ksymtab_gpl) - 0xC0000000) { __start___ksymtab_gpl = .; *(SORT(___ksymtab_gpl+*)) __stop___ksymtab_gpl = .; } __ksymtab_unused : AT(ADDR(__ksymtab_unused) - 0xC0000000) { __start___ksymtab_unused = .; *(SORT(___ksymtab_unused+*)) __stop___ksymtab_unused = .; } __ksymtab_unused_gpl : AT(ADDR(__ksymtab_unused_gpl) - 0xC0000000) { __start___ksymtab_unused_gpl = .; *(SORT(___ksymtab_unused_gpl+*)) __stop___ksymtab_unused_gpl = .; } __ksymtab_gpl_future : AT(ADDR(__ksymtab_gpl_future) - 0xC0000000) { __start___ksymtab_gpl_future = .; *(SORT(___ksymtab_gpl_future+*)) __stop___ksymtab_gpl_future = .; } __kcrctab : AT(ADDR(__kcrctab) - 0xC0000000) { __start___kcrctab = .; *(SORT(___kcrctab+*)) __stop___kcrctab = .; } __kcrctab_gpl : AT(ADDR(__kcrctab_gpl) - 0xC0000000) { __start___kcrctab_gpl = .; *(SORT(___kcrctab_gpl+*)) __stop___kcrctab_gpl = .; } __kcrctab_unused : AT(ADDR(__kcrctab_unused) - 0xC0000000) { __start___kcrctab_unused = .; *(SORT(___kcrctab_unused+*)) __stop___kcrctab_unused = .; } __kcrctab_unused_gpl : AT(ADDR(__kcrctab_unused_gpl) - 0xC0000000) { __start___kcrctab_unused_gpl = .; *(SORT(___kcrctab_unused_gpl+*)) __stop___kcrctab_unused_gpl = .; } __kcrctab_gpl_future : AT(ADDR(__kcrctab_gpl_future) - 0xC0000000) { __start___kcrctab_gpl_future = .; *(SORT(___kcrctab_gpl_future+*)) __stop___kcrctab_gpl_future = .; } __ksymtab_strings : AT(ADDR(__ksymtab_strings) - 0xC0000000) { *(__ksymtab_strings) } __init_rodata : AT(ADDR(__init_rodata) - 0xC0000000) { *(.ref.rodata) *(.devinit.rodata) *(.devexit.rodata) } __param : AT(ADDR(__param) - 0xC0000000) { __start___param = .; *(__param) __stop___param = .; } __modver : AT(ADDR(__modver) - 0xC0000000) { __start___modver = .; *(__modver) __stop___modver = .; . = ALIGN(((1 << 12))); __end_rodata = .; } . = ALIGN(((1 << 12)));

  /* Data */
  .data : AT(ADDR(.data) - 0xC0000000) {
    /* Start of data section */
    _sdata = .;
    /* init_task */
    . = ALIGN(((1 << 12) << 1)); *(.data..init_task)
    /* 32 bit has nosave before _edata */
    . = ALIGN((1 << 12)); __nosave_begin = .; *(.data..nosave) . = ALIGN((1 << 12)); __nosave_end = .;
    . = ALIGN((1 << 12)); *(.data..page_aligned)
    . = ALIGN((1 << (5))); *(.data..cacheline_aligned)
    *(.data) *(.ref.data) *(.data..shared_aligned) *(.devinit.data) *(.devexit.data) . = ALIGN(32); *(__tracepoints) . = ALIGN(8); __start___jump_table = .; *(__jump_table) __stop___jump_table = .; . = ALIGN(8); __start___verbose = .; *(__verbose) __stop___verbose = .; __start_annotated_branch_profile = .; *(_ftrace_annotated_branch) __stop_annotated_branch_profile = .; __start___trace_bprintk_fmt = .; *(__trace_printk_fmt) __stop___trace_bprintk_fmt = .;
    CONSTRUCTORS
    /* rarely changed data like cpu maps */
    . = ALIGN((1 << 5)); *(.data..read_mostly) . = ALIGN((1 << 5));
    /* End of data section */
    _edata = .;
  } :data

  /* Init code and data - will be freed after init */
  . = ALIGN((1 << 12));
  .init.begin : AT(ADDR(.init.begin) - 0xC0000000) {
    __init_begin = .; /* paired with __init_end */
  }
  . = ALIGN((1 << 12)); .init.text : AT(ADDR(.init.text) - 0xC0000000) { _sinittext = .; *(.init.text) *(.cpuinit.text) *(.meminit.text) _einittext = .; }
  .init.data : AT(ADDR(.init.data) - 0xC0000000) { *(.init.data) *(.cpuinit.data) *(.meminit.data) . = ALIGN(8); __ctors_start = .; *(.ctors) __ctors_end = .; *(.init.rodata) . = ALIGN(8); __start_ftrace_events = .; *(_ftrace_events) __stop_ftrace_events = .; *(.cpuinit.rodata) *(.meminit.rodata) . = ALIGN(32); __dtb_start = .; *(.dtb.init.rodata) __dtb_end = .; . = ALIGN(16); __setup_start = .; *(.init.setup) __setup_end = .; __initcall_start = .; *(.initcallearly.init) __early_initcall_end = .; *(.initcall0.init) *(.initcall0s.init) *(.initcall1.init) *(.initcall1s.init) *(.initcall2.init) *(.initcall2s.init) *(.initcall3.init) *(.initcall3s.init) *(.initcall4.init) *(.initcall4s.init) *(.initcall5.init) *(.initcall5s.init) *(.initcallrootfs.init) *(.initcall6.init) *(.initcall6s.init) *(.initcall7.init) *(.initcall7s.init) __initcall_end = .; __con_initcall_start = .; *(.con_initcall.init) __con_initcall_end = .; __security_initcall_start = .; *(.security_initcall.init) __security_initcall_end = .; }
 /*
  * Code and data for a variety of lowlevel trampolines, to be
  * copied into base memory (< 1 MiB) during initialization.
  * Since it is copied early, the main copy can be discarded
  * afterwards.
  */
  .x86_trampoline : AT(ADDR(.x86_trampoline) - 0xC0000000) {
    x86_trampoline_start = .;
    *(.x86_trampoline)
    x86_trampoline_end = .;
  }
  .x86_cpu_dev.init : AT(ADDR(.x86_cpu_dev.init) - 0xC0000000) {
    __x86_cpu_dev_start = .;
    *(.x86_cpu_dev.init)
    __x86_cpu_dev_end = .;
  }
  /*
   * start address and size of operations which during runtime
   * can be patched with virtualization friendly instructions or
   * baremetal native ones. Think page table operations.
   * Details in paravirt_types.h
   */
  . = ALIGN(8);
  .parainstructions : AT(ADDR(.parainstructions) - 0xC0000000) {
    __parainstructions = .;
    *(.parainstructions)
    __parainstructions_end = .;
  }
  /*
   * struct alt_inst entries. From the header (alternative.h):
   * "Alternative instructions for different CPU types or capabilities"
   * Think locking instructions on spinlocks.
   */
  . = ALIGN(8);
  .altinstructions : AT(ADDR(.altinstructions) - 0xC0000000) {
    __alt_instructions = .;
    *(.altinstructions)
    __alt_instructions_end = .;
  }
  /*
   * And here are the replacement instructions. The linker sticks
   * them as binary blobs. The .altinstructions has enough data to
   * get the address and the length of them to patch the kernel safely.
   */
  .altinstr_replacement : AT(ADDR(.altinstr_replacement) - 0xC0000000) {
    *(.altinstr_replacement)
  }
  /*
   * struct iommu_table_entry entries are injected in this section.
   * It is an array of IOMMUs which during run time gets sorted depending
   * on its dependency order. After rootfs_initcall is complete
   * this section can be safely removed.
   */
  .iommu_table : AT(ADDR(.iommu_table) - 0xC0000000) {
    __iommu_table = .;
    *(.iommu_table)
    __iommu_table_end = .;
  }
  . = ALIGN(8);
  .apicdrivers : AT(ADDR(.apicdrivers) - 0xC0000000) {
    __apicdrivers = .;
    *(.apicdrivers);
    __apicdrivers_end = .;
  }
  . = ALIGN(8);
  /*
   * .exit.text is discard at runtime, not link time, to deal with
   *  references from .altinstructions and .eh_frame
   */
  .exit.text : AT(ADDR(.exit.text) - 0xC0000000) {
    *(.exit.text) *(.cpuexit.text) *(.memexit.text)
  }
  .exit.data : AT(ADDR(.exit.data) - 0xC0000000) {
    *(.exit.data) *(.cpuexit.data) *(.cpuexit.rodata) *(.memexit.data) *(.memexit.rodata)
  }
  . = ALIGN((1 << 12)); .data..percpu : AT(ADDR(.data..percpu) - 0xC0000000) { __per_cpu_load = .; __per_cpu_start = .; *(.data..percpu..first) . = ALIGN((1 << 12)); *(.data..percpu..page_aligned) . = ALIGN((1 << 5)); *(.data..percpu..readmostly) . = ALIGN((1 << 5)); *(.data..percpu) *(.data..percpu..shared_aligned) __per_cpu_end = .; }
  . = ALIGN((1 << 12));
  /* freed after init ends here */
  .init.end : AT(ADDR(.init.end) - 0xC0000000) {
    __init_end = .;
  }
  /*
   * smp_locks might be freed after init
   * start/end must be page aligned
   */
  . = ALIGN((1 << 12));
  .smp_locks : AT(ADDR(.smp_locks) - 0xC0000000) {
    __smp_locks = .;
    *(.smp_locks)
    . = ALIGN((1 << 12));
    __smp_locks_end = .;
  }
  /* BSS */
  . = ALIGN((1 << 12));
  .bss : AT(ADDR(.bss) - 0xC0000000) {
    __bss_start = .;
    *(.bss..page_aligned)
    *(.bss)
    . = ALIGN((1 << 12));
    __bss_stop = .;
  }
  . = ALIGN((1 << 12));
  .brk : AT(ADDR(.brk) - 0xC0000000) {
    __brk_base = .;
    . += 64 * 1024; /* 64k alignment slop space */
    *(.brk_reservation) /* areas brk users have reserved */
    __brk_limit = .;
  }
  _end = .;

  .stab 0 : { *(.stab) } .stabstr 0 : { *(.stabstr) } .stab.excl 0 : { *(.stab.excl) } .stab.exclstr 0 : { *(.stab.exclstr) } .stab.index 0 : { *(.stab.index) } .stab.indexstr 0 : { *(.stab.indexstr) } .comment 0 : { *(.comment) }
  .debug 0 : { *(.debug) } .line 0 : { *(.line) } .debug_srcinfo 0 : { *(.debug_srcinfo) } .debug_sfnames 0 : { *(.debug_sfnames) } .debug_aranges 0 : { *(.debug_aranges) } .debug_pubnames 0 : { *(.debug_pubnames) } .debug_info 0 : { *(.debug_info .gnu.linkonce.wi.*) } .debug_abbrev 0 : { *(.debug_abbrev) } .debug_line 0 : { *(.debug_line) } .debug_frame 0 : { *(.debug_frame) } .debug_str 0 : { *(.debug_str) } .debug_loc 0 : { *(.debug_loc) } .debug_macinfo 0 : { *(.debug_macinfo) } .debug_weaknames 0 : { *(.debug_weaknames) } .debug_funcnames 0 : { *(.debug_funcnames) } .debug_typenames 0 : { *(.debug_typenames) } .debug_varnames 0 : { *(.debug_varnames) }

  /* Sections to be discarded */
  /DISCARD/ : { *(.exit.text) *(.cpuexit.text) *(.memexit.text) *(.exit.data) *(.cpuexit.data) *(.cpuexit.rodata) *(.memexit.data) *(.memexit.rodata) *(.exitcall.exit) *(.discard) *(.discard.*) }
  /DISCARD/ : { *(.eh_frame) }
}

  /*
   * The ASSERT() sink to . is intentional, for binutils 2.14 compatibility:
   */
  . = ASSERT((_end - 0xC0000000 <= (512 * 1024 * 1024)), "kernel image bigger than KERNEL_IMAGE_SIZE");
```
命令readelf -a vmlinux的输出参见文档vmlinux.lds/vmlinux.readelf -a.txt.zip

## Appendix H: scripts/module-common.lds

script/module-common.lds是生成*.ko文件的链接脚本文件，其包含如下内容，引用参见[3.4.3.4.2.3 $(modules)](#3-4-3-4-2-3-modules-)节:

```
/*
 * Common module linker script, always used when linking a module.
 * Archs are free to supply their own linker scripts.  ld will
 * combine them automatically.
 */
SECTIONS {
	/DISCARD/ : { *(.discard) }

	__ksymtab			: { *(SORT(___ksymtab+*)) }
	__ksymtab_gpl		: { *(SORT(___ksymtab_gpl+*)) }
	__ksymtab_unused		: { *(SORT(___ksymtab_unused+*)) }
	__ksymtab_unused_gpl	: { *(SORT(___ksymtab_unused_gpl+*)) }
	__ksymtab_gpl_future	: { *(SORT(___ksymtab_gpl_future+*)) }

	__kcrctab			: { *(SORT(___kcrctab+*)) }
	__kcrctab_gpl		: { *(SORT(___kcrctab_gpl+*)) }
	__kcrctab_unused		: { *(SORT(___kcrctab_unused+*)) }
	__kcrctab_unused_gpl	: { *(SORT(___kcrctab_unused_gpl+*)) }
	__kcrctab_gpl_future	: { *(SORT(___kcrctab_gpl_future+*)) }
}
```

## Appendix I: Targets Tree

![Targets_Tree](/assets/Targets_Tree.jpg)

# References

* [The Linux Kernel Documentation](https://www.kernel.org/doc/html/latest/index.html)
* [The Linux Kernel Archives](https://www.kernel.org/)
* [Linux Kernel Master Branch Repository](https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/)
* [Linux Kernel Stable Branch Repository](https://git.kernel.org/cgit/linux/kernel/git/stable/linux-stable.git/)
* [Linux Kernel Next Branch Repository](https://git.kernel.org/cgit/linux/kernel/git/next/linux-next.git/)
* [LWN.net](https://lwn.net/)
* [Linux Kernel Newbies](https://kernelnewbies.org/)
