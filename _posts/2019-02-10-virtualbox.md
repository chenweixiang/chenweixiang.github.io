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

# Setup LinuxMint in VirtualBox

## VirtualBox Settings

| VirtualBox Version | [VirtualBox v6.0.4 r128413](https://www.virtualbox.org/wiki/Downloads) |
| Host Operating System | Windows 10 |
| Guest Operating System | [Linux Mint 19.1 Tessa, Cinnamon Edition, 64-bit](https://www.linuxmint.com/download.php) |
| Name | LinuxMint |
| Type | Linux |
| Version | Ubuntu (64-bit) |
| Memory size | 4096 MB |
| Hard disk | Create a virtual hard disk now |
| Hard disk file type | VDI (VirtualBox Disk Image) |
| Storage on physical hard disk | Dynamically allocated |
| File location and size | LinuxMint, 50.00 GB |

<p/>

## LinuxMint Settings

| Language of LinuxMint | English |
| Keyboard layout | English (US) |
| Your name | chenwx |
| Your computer's name | chenwx |
| Pick a username | chenwx |
| Choose a password | chenwx |
| Confirm your password | chenwx |

<p/>

## Snapshots

Take the following snapshots:

| Name of Snapshots | Description of the Snapshot | When to Take the Snapshot |
| :---------------- | :-------------------------- | :------------------------ |
| 01 Linux Mint 19.1 Tessa Installed | Output of commands "lsb_release -a", "uname -a", "df -h" | Take the snapshot after the following tasks are done:<br>1) Linux Mint 19.1 Tessa is installed.<br>2) Upgrade Linux Mint 19.1 with shell commands "sudo apt update" and "sudo apt upgrade".<br>3) Setup desktop and taskbar. |
| 02 Basic Tools Installed | Installed tools' information | Take the snapshot after the following tasks are done:<br>1) Common tools are installed, including Sogou PinYin Input Method, LibreOffice, WPS Office, Atom, Firefox Plug-ins (such as, Proxy SwitchyOmega, uBlock Origin, 转换至简体), Meld, Shutter, Dia, Wine.<br>2) Development tools are installed, including Git, Jekyll, Source Insight 3.5. |
| 03 Setup Repos | Repos' location | Take the snapshot after the following tasks are done:<br>1) The following repos are cloned:<br>~/repo/blog<br>~/repo/scripts<br>~/repo/linux-kernel-test<br>~/repo/git<br>~/repo/linux<br>~/repo/linux-kernel-history<br>~/repo/linux-kernel-send-mail<br>2) The Bash environment is setup.|
| 04 Linux Mint ... Installed | Target Version of Linux Mint | Take the snapshot after Linux Mint is upgraded to target version. |

<p/>

## Export LinuxMint

If the [snapshots](#snapshots) are not needed within different hosts, then share the Linux Mint virtual machine by exporting it in **OVA** format (**Open Virtualization Format 1.0**), see [How to Import and Export OVA Files in VirtualBox](#how-to-import-and-export-ova-files-in-virtualbox).

If all [snapshots](#snapshots) are needed within different hosts, then share the Linux Mint virtual machine by [Moving A VirtualBox VM With Snapshots](#moving-a-virtualbox-vm-with-snapshots).

| Name of Exported VM | Name of Cloned VM |
| :-----------------: | :---------------: |
| LinuxMintExport     | LinuxMintClone    |

<p/>

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
* [Increase VirtualBox Disk Size](/docs/Increase_VirtualBox_Disk_Size.pdf)

## Fixing the "No Space left on disk" Error

* [Fixing the "No Space left on disk" Error](/docs/Fixing_the_No_Space_left_on_disk_Error.pdf)

## Fixing LinuxMint "Running in software rendering mode" on VirtualBox

* [LinuxMint Running in software rendering mode on VirtualBox](/docs/LinuxMint_Running_in_software_rendering_mode_on_VirtualBox.pdf)

## How to Import and Export OVA Files in VirtualBox

* [How to Import and Export OVA Files in VirtualBox](/docs/How_to_Import_and_Export_OVA_Files_in_VirtualBox.pdf)

## Moving A VirtualBox VM With Snapshots

* [Moving a VirtualBox VM with Snapshots](/docs/Moving_a_VirutalBox_VM_with_Snapshots.pdf)
* [Resolve Attached Media Conflicts in VirtualBox](/docs/Resolve_Attached_Media_Conflicts_in_VirtualBox.pdf)

# References

* [VirtualBox](https://www.virtualbox.org/)
* [VirtualBox Documentation](https://www.virtualbox.org/wiki/Documentation)
