---
layout: post
title:  "Git: Install latest version and configure it"
date:   2015-04-19 23:05:00
---

Git is used more and more popular in projects. It becomes more important in software developer's life. In this article, I'll give a short description of installing latest version of Git, and then configure Git to improve work efficiency.

# Install latest version of Git

If you have Git installed in system but not the latest version, you properly want to install latest version of Git to experience the new features of it.

## Install needed packages

	$ sudo apt-get update
	$ sudo apt-get install libcurl4-openssl-dev
	$ sudo apt-get install libexpat1-dev
	$ sudo apt-get install asciidoc
	$ sudo apt-get install xsltproc
	$ sudo apt-get install xmlto
	$ sudo apt-get install docbook2x

## Download Git source code

By following command, you can download Git source code to directory **~/git** from its official website:

	~ $ git clone git://git.kernel.org/pub/scm/git/git.git

or, from github repository:

	~ $ git clone https://github.com/git/git.git

## Build and install Git

First, check version of installed Git by command:

	~/git $ git --version

Then, check out specific tag of Git source code:

	~/git $ git checkout master
	~/git $ git pull
	~/git $ git tag -l | tail
	  v2.3.3
	  v2.3.4
	  v2.3.5
	  v2.4.0-rc0
	~/git $ git checkout v2.3.5

Now, it's time to build and install Git (including doc, html and info):

	~/git $ make prefix=/usr all doc info
	~/git $ sudo make prefix=/usr install install-doc install-html install-info

The latest version of Git is installed:

	~/git $ git --version

Remember to clean-up the Git source directory:

	~/git $ make distclean
	~/git $ git checkout master

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
	
	# List commit History of First Parent. => Usage: git lhfp
	git config --global alias.lhfp "log --date=short --pretty=format:'%Cgreen%h %Cred%ad %Cblue%cn %Cred%d %Creset%s' --first-parent"
	
	# Log commit History of First Parent with Graphical. => Usage: git lhgfp
	git config --global alias.lhgfp "log --date=short --pretty=format:'%Cgreen%h %Cred%ad %Cblue%cn %Cred%d %Creset%s' --graph --topo-order --decorate --first-parent"	
	
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

	# List Branch which contains specific Tag or commit. => Usage: git lbt <tag-or-commit-id>
	git config --global alias.lbt 'branch -a --contain'
	
	# List Merge Bases for the specified commits, tags, or branches. => Usage: git lmb {<branch-1> | <tag-1> | <commit-1>} {<branch-2> | <tag-2> | <commit-2>}
	git config --global alias.lmb 'show-branch --merge-base'
		
	#git config --global alias.stash-unapply '!git stash show -p | git apply -R'

	# set difftool / mergetool to Beyond Compare 3
	git config --global diff.tool bc3
	git config --global difftool.bc3.trustexitcode true
	
	git config --global merge.tool bc3
	git config --global mergetool.prompt false
	git config --global mergetool.keepbackup false
	git config --global mergetool.bc3.trustexitcode true

