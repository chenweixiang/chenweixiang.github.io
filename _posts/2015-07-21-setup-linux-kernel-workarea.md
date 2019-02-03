---
layout: post
title: "[Kernel] Setup Linux Kernel Workarea"
tag: Linux
toc: true
---

This article introduces how to setup Linux kernel workarea.

<!--more-->

# Clone Linux Kernel Repository

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

# Linux Kernel Repository

## linux-next Tree

The *linux-next* tree can be cloned from:

* git://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git
* https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git
* https://kernel.googlesource.com/pub/scm/linux/kernel/git/next/linux-next.git

The following materials related to *linux-next* tree:

* [http://lwn.net/Articles/268881/](http://lwn.net/Articles/268881/)
* [http://lwn.net/Articles/269120/](http://lwn.net/Articles/269120/)
* [http://lwn.net/Articles/289013/](http://lwn.net/Articles/289013/)
* [http://lwn.net/Articles/289245/](http://lwn.net/Articles/289245/)

The *linux-next* tree, to be maintained by *Stephen Rothwell*, is intended to be a gathering point for the patches which are planned to be merged in the next development cycle.

You can see which trees have been included by looking in the *Next/Trees* file in the source. There are also *quilt-import.log* and *merge.log* files in the *Next/* directory.

The linux-next tree has following branches:

* **stable** branch, trackes the master branch of linux mainline tree;
* **akpm** and **akpm-current** branches, track http://www.ozlabs.org/~akpm/mmotm/
* **master** branch, the tags such as **next-20160726** are on this branch.

```
chenwx@chenwx ~/linux $ git br -r | grep linux-next
  linux-next/akpm
  linux-next/akpm-base
  linux-next/master
  linux-next/stable
```

### How to track linux-next tree

Tracking linux-next tree is a little bit different from usual trees. In particular, since *Stephen Rothwell* rebases it quite frequently, you shouldn't do a git pull on linux-next.

Note that linux-next isn't an *evolving* tree like mainline, it's best to see it as being a list of individual kernels released as tags, i.e. you shouldn't be merging one into another.

Use following commands to track linux-next tree:

```
# (1) Change directory to ~/linux
chenwx@chenwx ~ $ cd linux

# (2) Fetch linux-next plus tags
chenwx@chenwx ~/linux $ git fetch linux-next
chenwx@chenwx ~/linux $ git fetch --tags linux-next

# (3) Or, update linux-next tree
chenwx@chenwx ~/linux $ git checkout next-master
chenwx@chenwx ~/linux $ git remote update
Fetching origin
remote: Counting objects: 4569, done.
remote: Compressing objects: 100% (722/722), done.
remote: Total 4569 (delta 3842), reused 4568 (delta 3841)
Receiving objects: 100% (4569/4569), 916.87 KiB | 296.00 KiB/s, done.
Resolving deltas: 100% (3842/3842), completed with 791 local objects.
From https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux
   e65805251f2d..3fc9d690936f  master     -> origin/master
Fetching linux-next
Fetching linux-stable

# (4) List recent linux-next tags
chenwx@chenwx ~/linux $ git tag -l "next-*" | tail
...
next-20160724
next-20160725
next-20160726

# (5) Choose the linux-next version that you will work from, and
#     create a local branch next-br based on that version
chenwx@chenwx ~/linux-next $ git checkout next-20160726
chenwx@chenwx ~/linux-next $ git checkout next-20160726 -b next-br
Switched to a new branch 'next-br'
```

## mainline Tree

The linux mainline tree can be cloned from:

* git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
* https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
* https://kernel.googlesource.com/pub/scm/linux/kernel/git/torvalds/linux.git

This is *Linux Torvalds* git tree. There is only one branch, that's **master** branch, on the mainline tree.

As a kernel developer, you should send patches against *linux-staging* or *linux-next* tree, not the mainline tree.

## stable Tree

Refer to *Documentataion/stable_kernel_rules.txt*.

**Linux kernel stable tree**

The linux stable tree can be cloned from:

* https://git.kernel.org/cgit/linux/kernel/git/stable/linux-stable.git
* git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git
* http://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git
* https://kernel.googlesource.com/pub/scm/linux/kernel/git/stable/linux-stable.git

**Linux kernel stable patch queue**

Here is the linux kernel stable patch queue:

* https://git.kernel.org/cgit/linux/kernel/git/stable/stable-queue.git
* git://git.kernel.org/pub/scm/linux/kernel/git/stable/stable-queue.git
* https://git.kernel.org/pub/scm/linux/kernel/git/stable/stable-queue.git
* https://kernel.googlesource.com/pub/scm/linux/kernel/git/stable/stable-queue.git

Each stable release has a corresponding branch on stable tree, such as *linux-3.2.y*. And its latest *commits/maintainers* can be found at *https://git.kernel.org/cgit/linux/kernel/git/stable/linux-stable.git/refs/heads*

# References

* [The Linux Kernel Documentation](https://www.kernel.org/doc/html/latest/index.html)
* [The Linux Kernel Archives](https://www.kernel.org/)
* [Linux Kernel Master Branch Repository](https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/)
* [Linux Kernel Stable Branch Repository](https://git.kernel.org/cgit/linux/kernel/git/stable/linux-stable.git/)
* [Linux Kernel Next Branch Repository](https://git.kernel.org/cgit/linux/kernel/git/next/linux-next.git/)
* [LWN.net](https://lwn.net/)
