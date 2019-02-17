---
layout: post
title:  "VirtualBox"
tag: Tools
toc: true
---

This article introduces the powerful x86 and AMD64/Intel64 virtualization product **VirtualBox**.

<!--more-->

# Overview

[VirtualBox](https://www.virtualbox.org/) is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use. Not only is VirtualBox an extremely feature rich, high performance product for enterprise customers, it is also the only professional solution that is freely available as Open Source Software under the terms of the GNU General Public License (GPL) version 2.

# Usage of VirtualBox

## Convert VirtualBox .vmdk to .vdi format

On Windows, execute the following command in cmd:

```
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\chenqwei>cd c:\program files\oracle\virtualbox

c:\Program Files\Oracle\VirtualBox>VBoxManage clonehd --format VDI "C:\Users\chenqwei\VirtualBox VMs\LinuxMint16\LinuxMint16-disk1_1.vmdk" "C:\Users\chenqwei\VirtualBox VMs\LinuxMint16\LinuxMint16.vdi"
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
```

## Shrink and Resize VirtualBox .vdi

On Windows, execute the following command in cmd:

```
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\chenqwei> cd C:\Program Files\Oracle VM VirtualBox

C:\Program Files\Oracle VM VirtualBox> VboxManage modifyhd "C:\Users\chenwx\VirtualBox VMs\LinuxMint16\LinuxMint16.vdi" --compact
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%

C:\Program Files\Oracle VM VirtualBox> VboxManage modifyhd "C:\Users\chenwx\VirtualBox VMs\LinuxMint16\LinuxMint16.vdi" --resize 10240
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%

C:\Program Files\Oracle VM VirtualBox> VboxManage modifyhd "C:\Users\chenwx\VirtualBox VMs\LinuxMint16\LinuxMint16.vdi" --resize 25600
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%

C:\Program Files\Oracle VM VirtualBox> VboxManage modifyhd "C:\Users\chenwx\VirtualBox VMs\LinuxMint16\LinuxMint16.vdi" --resize 30720
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
```

## Resizing VirtualBox and Linux Partitions with GParted

[GParted](http://gparted.sourceforge.net/download.php) is a free partition manager that enables you to resize, copy, and move partitions without data loss. Refer to the following documentations:

* [Resizing VirtualBox and Linux Partitions with GParted](/docs/Resizing_VirtualBox_and_Linux_Partitions_with_GParted.pdf)
* [Expanding a Linux disk with GParted (and getting swap out of the way)](/docs/Expanding_a_Linux_disk_with_GParted.pdf)

## Fixing the "No Space left on disk" Error

* [Fixing the "No Space left on disk" Error](/docs/Fixing_the_No_Space_left_on_disk_Error.pdf)

## Fixing LinuxMint "Running in software rendering mode" on VirtualBox

[LinuxMint Running in software rendering mode on VirtualBox](/docs/LinuxMint_Running_in_software_rendering_mode_on_VirtualBox.pdf)

# References

* [VirtualBox](https://www.virtualbox.org/)
* [VirtualBox Documentation](https://www.virtualbox.org/wiki/Documentation)
