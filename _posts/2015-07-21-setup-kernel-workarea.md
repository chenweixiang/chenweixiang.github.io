---
layout: post
title: "Setup Linux Kernel Workarea"
tag: Linux kernel
toc: true
---

This article introduces how to setup Linux kernel workarea.

<!--more-->

# Clone Linux Kernel Repository

Run following commands to clone all linux kernel repositories into the same directory:

```
# (1) Clone linux.git to ~/linux
# - git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
# - https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
chenwx@chenwx ~ $ git clone https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
Cloning into 'linux'...
remote: Counting objects: 3841355, done.
remote: Compressing objects: 100% (75674/75674), done.
remote: Total 3841355 (delta 56478), reused 0 (delta 0)
Receiving objects: 100% (3841355/3841355), 892.40 MiB | 2.47 MiB/s, done.
Resolving deltas: 100% (3147072/3147072), done.
Checking connectivity... done.
Checking out files: 100% (47936/47936), done.

# (2) Add linux-next tree to ~/linux
# - git://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git
# - https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git
chenwx@chenwx ~ $ git remote add linux-next https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git

# (2.1) Download source code from linux-next tree
chenwx@chenwx ~ $ git fetch linux-next
chenwx@chenwx ~ $ git fetch --tags linux-next

# (2.2) Create local branch to track master branch of linux-next tree
chenwx@chenwx ~ $ git branch --track next-master linux-next/master

# (3) Add linux-stable tree to ~/linux
# - git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git
# - https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git
chenwx@chenwx ~ $ git remote add linux-stable https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git

# (3.1) Download source code from linux-stable tree
chenwx@chenwx ~ $ git fetch linux-stable
chenwx@chenwx ~ $ git fetch --tags linux-stable

# (3.2) Create local branches to track longterm stable branches
chenwx@chenwx ~ $ git co linux-2.6.32.y
chenwx@chenwx ~ $ git co linux-3.2.y
chenwx@chenwx ~ $ git co linux-3.4.y
chenwx@chenwx ~ $ git co linux-3.10.y
chenwx@chenwx ~ $ git co linux-3.12.y
chenwx@chenwx ~ $ git co linux-3.14.y
chenwx@chenwx ~ $ git co linux-3.18.y
chenwx@chenwx ~ $ git co linux-3.19.y

# (4) Local branches
chenwx@chenwx ~/linux $ git br
  linux-2.6.32.y
  linux-3.10.y
  linux-3.12.y
  linux-3.14.y
  linux-3.18.y
  linux-3.19.y
  linux-3.2.y
  linux-3.4.y
* master
  next-master

# (5) Use following command to fetch objects from all remotes
chenwx@chenwx ~ $ git remote update
Fetching origin
Fetching linux-stable
Fetching linux-next
```

# References

* [https://www.kernel.org/](https://www.kernel.org/)
* [Linux Kernel Master Branch Repository](https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/)
* [Linux Kernel Stable Branch Repository](https://git.kernel.org/cgit/linux/kernel/git/stable/linux-stable.git/)
* [Linux Kernel Next Branch Repository](https://git.kernel.org/cgit/linux/kernel/git/next/linux-next.git/)
* [LWN.net](https://lwn.net/)
