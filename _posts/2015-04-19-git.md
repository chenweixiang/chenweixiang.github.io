---
layout: post
title:  "Git: Distributed Version Control System"
tag: Linux
toc: true
---

Git is used more and more popular in projects. It becomes more important in software developer's life. In this article, I'll give a short description of installing latest version of Git, and then configure Git to improve work efficiency.

<!--more-->

# Git Theory

The following figure shows the important concepts of Git:

![Git_Note](/assets/Git_Note.jpg)

Git Cheat Sheet from [git-scm.com](https://git-scm.com/):

![Git Cheat Sheet](/docs/Git_Cheat_Sheet.svg)

[Git Cheat Sheet from zeroturnaround.com](/docs/Git_cheat_sheet.pdf)

# Git Hooks

Git hooks are programs you can place in a hooks directory to trigger actions at certain points in git’s execution. By default the hooks directory is ```$GIT_DIR/hooks```, but that can be changed via the ```core.hooksPath``` configuration variable:

```
chenwx@chenwx ~/linux $ ll .git/hooks/
-rwxrwxrwx 1 chenwx chenwx  478 Jul 22  2016 applypatch-msg.sample
-rwxrwxrwx 1 chenwx chenwx  896 Jul 22  2016 commit-msg.sample
-rwxrwxrwx 1 chenwx chenwx  189 Jul 22  2016 post-update.sample
-rwxrwxrwx 1 chenwx chenwx  424 Jul 22  2016 pre-applypatch.sample
-rwxrwxrwx 1 chenwx chenwx 1.7K Jul 22  2016 pre-commit.sample
-rwxrwxrwx 1 chenwx chenwx 1.4K Jul 22  2016 pre-push.sample
-rwxrwxrwx 1 chenwx chenwx 4.9K Jul 22  2016 pre-rebase.sample
-rwxrwxrwx 1 chenwx chenwx 1.3K Jul 22  2016 prepare-commit-msg.sample
-rwxrwxrwx 1 chenwx chenwx 3.6K Jul 22  2016 update.sample
```

Git hooks that don’t have the executable bit set are ignored, so you may need to change the file permissions of the script if you’re creating it from scratch:

```
chenwx@chenwx ~/linux $ touch pre-commit
chenwx@chenwx ~/linux $ chmod +x pre-commit
```

Before Git invokes a hook, it changes its working directory to either ```$GIT_DIR``` in a bare repository or the root of the working tree in a non-bare repository. An exception are hooks triggered during a push (**pre-receive**, **update**, **post-receive**, **post-update**, **push-to-checkout**) which are always executed in ```$GIT_DIR```.

Hooks can get their arguments via the **environment**, **command-line arguments**, and **stdin**.

Git hooks are scripts that run automatically every time a particular event occurs in a Git repository. They let you customize Git’s internal behavior and trigger customizable actions at key points in the development life cycle. Common use cases for Git hooks include encouraging a commit policy, altering the project environment depending on the state of the repository, and implementing continuous integration workflows. But, since scripts are infinitely customizable, you can use Git hooks to automate or optimize virtually any aspect of your development workflow.

The built-in scripts of Git hooks are mostly shell and PERL scripts, but you can use any scripting language you like as long as it can be run as an executable. The shebang line (```#!/bin/sh```) in each script defines how your file should be interpreted. So, to use a different language, all you have to do is change it to the path of your interpreter. For instance, you can write an executable Python script in the **prepare-commit-msg** file instead of using shell commands:

```
#!/usr/bin/env python
import sys, os
commit_msg_filepath = sys.argv[1]
with open(commit_msg_filepath, 'w') as f:
f.write("# Please include a useful commit message!")
```

Hooks are local to any given Git repository, and they are not copied over to the new repository when you run ```git clone```. And, since hooks are local, they can be altered by anybody with access to the repository. This has an important impact when configuring hooks for a team of developers. First, you need to find a way to make sure hooks stay up-to-date amongst your team members. Second, you can’t force developers to create commits that look a certain way—you can only encourage them to do so.

Maintaining hooks for a team of developers can be a little tricky because the ```.git/hooks``` directory isn’t cloned with the rest of your project, nor is it under version control. A simple solution to both of these problems is to store your hooks in the actual project directory (above the ```.git``` directory). This lets you edit them like any other version-controlled file. To install the hook, you can either create a symlink to it in ```.git/hooks```, or you can simply copy and paste it into the ```.git/hooks``` directory whenever the hook is updated.

As an alternative, Git also provides a [Template Directory](http://git-scm.com/docs/git-init#_template_directory) mechanism that makes it easier to install hooks automatically. All of the files and directories contained in this template directory are copied into the .git directory every time you use git init or git clone.

Also refer to:

* [githooks Documentation](https://git-scm.com/docs/githooks)
* [Git Hooks](https://githooks.com/)
* [Git Hooks Tutorial](https://www.atlassian.com/git/tutorials/git-hooks)

# Git Protocol Version 2

The main improvements of [Git protocol version 2 specification](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/technical/protocol-v2.html) are:

* Server-side filtering of references
* Easy extensibility for new features like ref-in-want and fetching and pushing symrefs
* Simplified client handling of the http transport

The Git protocol version 2 is already merged to **Git 2.18**, refer to [release notes]().

Refer to [Introducing Git protocol version 2](https://opensource.googleblog.com/2018/05/introducing-git-protocol-version-2.html).

# Install Git by Compiling

If you have Git installed in system but not the latest version, you properly want to install latest version of Git to experience the new features of it.

## Install needed packages

```
$ sudo apt-get update
$ sudo apt-get install libcurl4-openssl-dev libexpat1-dev asciidoc xsltproc xmlto docbook2x
```

## Clone Git Repo

By following command, you can download Git source code to directory **~/git** from its official website:

```
~ $ git clone git://git.kernel.org/pub/scm/git/git.git
```

or, from github repository:

```
~ $ git clone https://github.com/git/git.git
```

## Build and Install Git

First, check version of installed Git by command:

```
~/git $ git --version
```

Then, check out specific tag of Git source code:

```
~/git $ git checkout master
~/git $ git pull
~/git $ git tag -l | tail
  v2.3.3
  v2.3.4
  v2.3.5
  v2.4.0-rc0
~/git $ git checkout v2.3.5
```

Now, it's time to build and install Git (including doc, html and info):

```
~/git $ make prefix=/usr all doc info
~/git $ sudo make prefix=/usr install install-doc install-html install-info
```

The latest version of Git is installed:

```
~/git $ git --version
```

Remember to clean-up the Git source directory:

```
~/git $ make distclean
~/git $ git checkout master
```

# Git Configure

The Git configuration [git-config.conf](https://github.com/chenweixiang/scripts/blob/master/git-config.conf) used in my work and personal projects improves work efficiency, which can be included in [.bashrc](https://github.com/chenweixiang/scripts/blob/master/bashrc.conf).

The following command shows the Git configuration:

```
# Show the configuration applied to all users in the system
$ git config --system -l

# Show the configuration applied to all repositories of an user
$ git config --global -l

# Show the configuration applied to the current repository
$ git config --local -l

# Show the alias of configurations
$ git config -l | grep alias.
alias.br=branch
alias.co=checkout
alias.ci=commit
alias.st=status
alias.dt=difftool
alias.mt=mergetool
alias.desc=describe
...
```

# Useful Commands

## List All Files with Absolute Path in a Commit

If you want to print the absolute path of a commit, you could execute the script [git-ls.sh](https://github.com/chenweixiang/scripts/blob/master/git-ls.sh) to print the files changed by a commit with absolute path:

```
chenwx@chenwx ~/linux/arch/x86/kernel $ . ~/git-ls.sh 90a2282e23f0
/home/chenwx/linux/arch/x86/include/asm/irq.h /home/chenwx/linux/arch/x86/kernel/apic/vector.c /home/chenwx/linux/arch/x86/kernel/irq.c

chenwx@chenwx ~/linux/arch/x86/kernel $ git lc 90a2282e23f
commit 90a2282e23f0522e4b3f797ad447c5e91bf7fe32
Author:     Thomas Gleixner <tglx@linutronix.de>
AuthorDate: Thu Dec 31 16:30:53 2015 +0000
Commit:     Thomas Gleixner <tglx@linutronix.de>
CommitDate: Fri Jan 15 13:44:01 2016 +0100

    x86/irq: Call irq_force_move_complete with irq descriptor

    First of all there is no point in looking up the irq descriptor again, but we
    also need the descriptor for the final cleanup race fix in the next
    patch. Make that change seperate. No functional difference.

    Signed-off-by: Thomas Gleixner <tglx@linutronix.de>
    Tested-by: Borislav Petkov <bp@alien8.de>
    Tested-by: Joe Lawrence <joe.lawrence@stratus.com>
    Cc: Jiang Liu <jiang.liu@linux.intel.com>
    Cc: Jeremiah Mahler <jmmahler@gmail.com>
    Cc: andy.shevchenko@gmail.com
    Cc: Guenter Roeck <linux@roeck-us.net>
    Cc: stable@vger.kernel.org #4.3+
    Link: http://lkml.kernel.org/r/20151231160107.125211743@linutronix.de
    Signed-off-by: Thomas Gleixner <tglx@linutronix.de>

 arch/x86/include/asm/irq.h    |  5 +++--
 arch/x86/kernel/apic/vector.c | 11 +++++++----
 arch/x86/kernel/irq.c         |  2 +-
 3 files changed, 11 insertions(+), 7 deletions(-)
```

## Show Root Directory of Git Repository

Run the following commands to show the local git repository (.git):

```
chenwx@chenwx ~/xx-net/code/default/x_tunnel/local $ pwd
/home/chenwx/xx-net/code/default/x_tunnel/local

# Show the location of .git/ directory of currenty local repository
chenwx@chenwx ~/xx-net/code/default/x_tunnel/local $ git rev-parse --git-dir
/home/chenwx/xx-net/.git

# Show the working area of current local repository (absolute path)
chenwx@chenwx ~/xx-net/code/default/x_tunnel/local $ git rev-parse --show-toplevel
/home/chenwx/xx-net

# Show the working area of current local repository (relative path)
chenwx@chenwx ~/xx-net/code/default/x_tunnel/local $ git rev-parse --show-prefix  
code/default/x_tunnel/local/

# The deepth from current directory to the root directory of working area
chenwx@chenwx ~/xx-net/code/default/x_tunnel/local $ git rev-parse --show-cdup  
../../../../
```

## Show Remotes

The following command shows the remotes:

```
$ git remote -v
```

Then, use the following command to show detail information of specific remote:

```
$ git remote show <remote>
```

## Show Summarize of Commits

The following command shows summarize of *git log* output:

```
$ git shortlog
```

## Archive Specified Commit

Archive the latest version of repository:

```
chenwx@chenwx /media/chenwx/Work/blog $ git rev-parse --short HEAD
94f0da70a606

chenwx@chenwx /media/chenwx/Work/blog $ git archive -o commit-`git rev-parse --short HEAD`.zip HEAD

chenwx@chenwx /media/chenwx/Work/blog $ ll commit-94f0da70a606.zip
-rwxrwxrwx 1 chenwx chenwx 18M Jul 21 19:13 commit-94f0da70a606.zip
```

or, use the script [git-archive.sh](https://github.com/chenweixiang/scripts/blob/master/git-archive.sh) to archive the specified commit.

## List Tags with Sorting

Use the following command to list tags with sorting:

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
...
```

## Update Author and Commiter's Name and Email

Use the following command to reset author's / commiter's name and email for commit <commit> and commits after it:

```
git rebase -i <commit> --exec 'git commit --amend --reset-author --no-edit'
```

## Clean All Untracked Files

First, use the following command to show what would be removed without actually remove anything:

```
git clean -nfxd

```

Then, use the following command to remove untracked files:

```
git clean -fxd
```

# Git Clients

* [Git GUI](https://git-scm.com/docs/git-gui)
* [SmartGit](http://www.syntevo.com/smartgit/)
* [GitHub Desktop](https://desktop.github.com/)
* [Source Tree](https://www.sourcetreeapp.com/)
* [TortoiseGit](https://tortoisegit.org/)
* [Fork](https://git-fork.com/)
* [Git Extensions](https://sourceforge.net/projects/gitextensions/)
* [Gitkraken](https://www.gitkraken.com/)
* [Tower](https://www.git-tower.com/)
* [Git-cola](http://git-cola.github.io/)
* [Giggle](https://wiki.gnome.org/giggle)
* [Gitg](https://wiki.gnome.org/Apps/Gitg)
* [Qgit](http://digilander.libero.it/mcostalba/)
* [GitForce](https://sites.google.com/site/gitforcetool/home)
* [Egit](http://www.eclipse.org/egit/)
* [GitEye](http://www.collab.net/products/giteye)

# References

* [Git Official Site](https://git-scm.com/)
* [Git Repository on GitHub](https://github.com/git/git)
* [Git Reference Manual](https://git-scm.com/docs)
* [Git Reference](http://gitref.org/index.html)
* [Gerrit](https://www.gerritcodereview.com/)
* [GitHub](https://github.com/)
* [GitLab](https://about.gitlab.com/)
* [Coding](https://coding.net/)
* [Quilt](http://savannah.nongnu.org/git/?group=quilt)
