---
layout: post
title:  "Git: Install latest version and configure it"
date:   2015-04-19 23:05:00
---

Git is used more and more popular in big company projects, and it also used in personal projects. It becomes more and more important in software developer's life. In this article, I'll give a short description of installing latest version of Git, and then the configure Git I used in work and personal projects will be posted.

# Install latest version of Git

If you have Git installed in system but not the latest version, you properly want to install latest version of Git to experience the latest feature of it. Here is it.

## Install needed library

	$ sudo apt-get update
	$ sudo apt-get install libcurl4-openssl-dev
	$ sudo apt-get install libexpat1-dev
	$ sudo apt-get install asciidoc
	$ sudo apt-get install xsltproc
	$ sudo apt-get install xmlto
	$ sudo apt-get install docbook2x

## Download git source code

By following command, you can download git source code from git official website:

	$ git clone git://git.kernel.org/pub/scm/git/git.git

or, from github repository

	$ git clone http://github.com/git/git

to directory ~/git

## Build and install git

First, check old installed version by command:

	$ git --version

Then, check out specific tag of git source code:
	$ git checkout master
	$ git pull
	$ git tag -l | tail
	$ git checkout <latest-tag>

It's time to build and install git (including doc, html, info):

	$ make prefix=/usr all doc info
	$ sudo make prefix=/usr install install-doc install-html install-info

The latest version of Git will be installed:

	$ git --version

Remember to clean-up the Git source directory:

	$ make distclean
	$ git checkout master

# Git Configure

The following Git configuration used in my work and personal projects improves work efficiency:

	# set user name and email address
	git config --global user.name "Chen Weixiang"
	git config --global user.email "weixiangx.chen@outlook.com"
	
	# enable auto-correct function for mistype commands
	#git config --global help.autocorrect 1

	# abbreviate commit hashes to 12 characters
	git config --global core.abbrev 12
	
	# set highlight for terminal
	git config --global color.ui true
	git config --global color.status auto
	git config --global color.branch auto
	git config --global color.showbranch auto
	git config --global color.diff auto
	git config --global color.grep auto
	git config --global color.interactive auto
	
	# abbreviation
	git config --global alias.br branch
	git config --global alias.co checkout
	git config --global alias.ci commit
	git config --global alias.st status
	git config --global alias.dt difftool
	git config --global alias.mt mergetool
	git config --global alias.desc 'describe'
	
	# List commit History. => Usage: git lh
	git config --global alias.lh "log --date=short --pretty=format:'%Cgreen%h %Cred%ad %Cblue%cn %Cred%d %Creset%s'"
	
	# Log commit History with Graphical. => Usage: git lhg
	git config --global alias.lhg "log --date=short --pretty=format:'%Cgreen%h %Cred%ad %Cblue%cn %Cred%d %Creset%s' --graph --topo-order --decorate"
	
	# List Commit. => Usage: git lc <commmit-id>
	git config --global alias.lc "log --stat -1 -c --decorate --pretty=fuller"
	
	# List Commit with Patch format. => Usage: git lcp <commmit-id>
	git config --global alias.lcp "log --no-prefix -1 -p --decorate --pretty=fuller"
	
	# List Commit with Detail information. => Usage: git lcd <commmit-id>
	git config --global alias.lcd "cat-file -p"
	
	# Diff Two Commits. => Usage: git dtc <commmit-id1> <commmit-id2>
	git config --global alias.dtc "diff --no-prefix"
	
	# List Tag. => Usage: git lt <commmit-id>
	git config --global alias.lt 'tag --points-at'
	
	#git config --global alias.stash-unapply '!git stash show -p | git apply -R'

	# set difftool / mergetool to Beyond Compare 3
	git config --global diff.tool bc3
	git config --global difftool.bc3.trustexitcode true
	
	git config --global merge.tool bc3
	git config --global mergetool.prompt false
	git config --global mergetool.keepbackup false
	git config --global mergetool.bc3.trustexitcode true

