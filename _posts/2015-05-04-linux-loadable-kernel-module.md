---
layout: post
title: "Linux Loadable Kernel Module (LKM)"
tag: Linux kernel
toc: true
---

This article introduces the Linux Loadable Kernel Module (LKM).

<!--more-->

# Brief Introduction to LKM

The loadable kernel module (LKM) are typically used to add support for new hardware and/or filesystems, or for adding system calls in Linux kernel.

# How to Write LKM

## An Example of LKM

Here is source code of helloworld.c:

	#include <linux/module.h>
	#include <linux/init.h>

	MODULE_LICENSE("GPL");
	MODULE_AUTHOR("Chen Weixiang");
	MODULE_DESCRIPTION("A Hello Module");

	int isSayHello = 0;
	static int sayHello()
	{
		isSayHello = 1;
		printk("Hello World\n");
		return 0;
	}
	EXPORT_SYMBOL_GPL(isSayHello);
	EXPORT_SYMBOL_GPL(sayHello);

	static int __init hello_init(void)
	{
		printk("Hello module init\n");
		sayHello();
		return 0;
	}

	static void __exit hello_exit(void)
	{
	    printk("Hello module exit\n");
	}

	module_init(hello_init);
	module_exit(hello_exit);

## An Example of Makefile

Here is the corresponding makefile for building helloworld.c on kernels > 2.4:

	#
	# Usage:
	#   make o=<one source file name with or without extension>
	#   make o="<multiple source file names with or without extension>"
	#
	objects := $(addsuffix .o,$(basename $(strip $(o))))

	ifneq ($(filter-out clean, $(MAKECMDGOALS)),)
	  ifeq ($(objects),)
	    $(error No object to be compiled)
	  else
	    $(warning Compiling $(objects))
	  endif
	endif

	obj-m := $(objects)

	# 'uname -r' print kernel release
	KDIR := /lib/modules/$(shell uname -r)/build
	PWD := $(shell pwd)

	# enable macor DEBUG in order to use pr_debug()
	ccflags-y += -DDEBUG

	# targets
	all:
		make -C $(KDIR) M=$(PWD) modules

	clean:
		make -C $(KDIR) M=$(PWD) clean

Put the makefile into the same directory of helloword.c, and run command:

	$ make helloworld.c

to build helloworld. In the following list, **helloworld.ko** is the built external module:

	$ ls -la
	drwxr-xr-x 3 chenwx chenwx   4096 May  6 00:09 .
	drwxr-xr-x 3 chenwx chenwx   4096 May  6 07:49 ..
	-rw-r--r-- 1 chenwx chenwx    267 May  6 00:09 .helloworld.ko.cmd
	-rw-r--r-- 1 chenwx chenwx  26232 May  6 00:09 .helloworld.mod.o.cmd
	-rw-r--r-- 1 chenwx chenwx  26129 May  6 00:09 .helloworld.o.cmd
	drwxr-xr-x 2 chenwx chenwx   4096 May  6 00:09 .tmp_versions
	-rw-r--r-- 1 chenwx chenwx    638 May  3 16:59 Makefile
	-rw-r--r-- 1 chenwx chenwx     79 May  6 00:09 Module.symvers
	-rw-r--r-- 1 chenwx chenwx    492 May  3 17:09 helloworld.c
	-rw-r--r-- 1 chenwx chenwx 116618 May  6 00:09 helloworld.ko
	-rw-r--r-- 1 chenwx chenwx    764 May  6 00:09 helloworld.mod.c
	-rw-r--r-- 1 chenwx chenwx  64528 May  6 00:09 helloworld.mod.o
	-rw-r--r-- 1 chenwx chenwx  56016 May  6 00:09 helloworld.o
	-rw-r--r-- 1 chenwx chenwx     55 May  6 00:09 modules.order

## How to insert / remove module

If you want to

# Macros used in LKM

# Module Parameters

# How to Build LKM

# Load and Remove LKM

# LKM in System

# Initialize and Cleanup LKM




