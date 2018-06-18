---
layout: post
title: "Linux Kernel Releases"
tag: Linux kernel
toc: true
---

This article introduces Linux kernel releases.

<!--more-->

# Relationship of Tags

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

# Linux Kernel Release Note

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

# References

* [The Linux Kernel Archives](https://www.kernel.org/)
* [Linux Kernel Newbies](https://kernelnewbies.org/)
