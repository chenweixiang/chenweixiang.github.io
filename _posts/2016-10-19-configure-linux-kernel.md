---
layout: post
title: "Configure Linux Kernel"
tag: Linux kernel
toc: true
---

This article introduces how to configure the Linux kernel.

<!--more-->

# Create Output Directory

It's better to build Linux kernel on a directory outside of local kernel repository, such as *~/linux-build*. In order to use another directory to build Linux kernel, the repository should be clean up:

```
chenwx@chenwx ~/linux $ make distclean
chenwx@chenwx ~/linux $ mkdir ../linux-build
```

And then, use parameter ```O=../linux-build/``` in each make command later, such as configure Linux kernel:

```
chenwx@chenwx ~/linux $ make O=../linux-build/ menuconfig
```

# Configure Kernel

## procedure of make \*config

The following figure shows the procedure of ```make *config```:

![make_config](/assets/make_config.jpg)

## use old existed configure

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

I like to use the command ```make menuconfig``` to configure linux kerenel because it much more easier to use it.

# Kconfig Tree

The following table shows the kconfig tree of x86 architecture:

```
linux-3.2/Kconfig
+- source "arch/$(SRCARCH)/Kconfig"
|  |  >> 此处以x86体系为例，即source "arch/x86/Kconfig"
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

# References

* [The Linux Kernel Archives](https://www.kernel.org/)
