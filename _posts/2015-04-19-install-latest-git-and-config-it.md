---
layout: post
title:  "Git: Install latest version and configure it"
tag: Linux
toc: true
---

Git is used more and more popular in projects. It becomes more important in software developer's life. In this article, I'll give a short description of installing latest version of Git, and then configure Git to improve work efficiency.

<!--more-->

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

	# Diff Two Commits with Statistics. => Usage: git dtcs <commmit-id1> <commmit-id2>
	git config --global alias.dtcs "diff --no-prefix --shortstat"

	# List Tag. => Usage: git lt <commmit-id>
	git config --global alias.lt 'tag --points-at'

	# List closest Tagname on first parent. => Usage: git llt
	git config --global alias.llt 'describe --abbrev=0 --tags --first-parent HEAD'
	# List Branch which contains specific Tag or commit. => Usage: git lbt <tag-or-commit-id>
	git config --global alias.lbt 'branch -a --contain'

	# List Merge Bases for the specified commits, tags, or branches. => Usage: git lmb {<branch-1> | <tag-1> | <commit-1>} {<branch-2> | <tag-2> | <commit-2>}
	git config --global alias.lmb 'show-branch --merge-base'

	# Grep commit Log. => Usage: git gl <keyword> [-- <files>]
	git config --global alias.gl "log --all --stat --grep"

	# Print Lines matching a pattern. => Usage: git pl <keyword> [-- <files>]
	git config --global alias.pl "grep --full-name -n --heading --break -p"

	# Print Lines matching a pattern (Ignore case). => Usage: git pl <keyword> [-- <files>]
	git config --global alias.pli "grep --full-name -n --heading --break -p -i"

	# List Untracked ALL directories and files from working tree. => Usage: git luall
	git config --global alias.luall "clean -d -n"

	# Remove ALL untracked directories and files from working tree. => Usage: git rmall
	git config --global alias.rmall "clean -d -f -X"

	# List References in a local repository. => Usage: git lf
	git config --global alias.lr "show-ref --head --heads --tags -d"

	#git config --global alias.unstash '!git stash show -p | git apply -R'

	# Clear all modifications in working directory (BE CAREFULL). => usage: git unstage
	git config --global alias.unstage 'reset HEAD --'

	# set difftool / mergetool to Beyond Compare 3
	git config --global diff.tool bc3
	git config --global difftool.bc3.trustexitcode true

	git config --global merge.tool bc3
	git config --global mergetool.prompt false
	git config --global mergetool.keepbackup false
	git config --global mergetool.bc3.trustexitcode true

The following command shows the remotes:

	$ git remote -v

Then, use the following command to show detail information of specific remote:

	$ git remote show <remote>

And, the following command shows summarize of 'git log' output:

	$ git shortlog

## All files with absolute path in a commit

If you want to print the absolute path of a commit, you can save the the following script to file *git-ls-each-file.bash*:

    #-------------------------------------------------------------------------------
    # This Bash script is used to print the files changed by commit with absolute
    # path. The commit is specified by input parameter $1.
    #
    # Usage: git-ls-each-file [commit-id]
    #-------------------------------------------------------------------------------

    #
    # 1) Get the commit and its parent
    #

    if [ "$1" == "" ]; then
        cmt="HEAD"
        parent_cmt="HEAD~"
    else
        cmt=$1
        parent_cmt=${cmt}~
    fi

    #
    # 2) Get all changed files in <commit-id>~ and <commit-id>
    #

    files=`git diff-tree --no-commit-id --name-only -r ${parent_cmt} ${cmt}`

    #
    # 3) Print the absolute path of each file
    #

    toppath=`git rev-parse --show-toplevel`

    unset absolute_files

    for f in $files
    do
        absolute_files+="$toppath/$f "
    done

    echo $absolute_files

Then, run the script to print the files changed by a commit with absolute path:

    chenwx@chenwx ~/linux/arch/x86/kernel $ . ~/git-ls-each-file.bash 90a2282e23f0
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

# References

* [Git Official Site](https://git-scm.com/)
* [Git Repository on GitHub](https://github.com/git/git)
* [Gerrit](https://www.gerritcodereview.com/)
* [GitHub](https://github.com/)
* [GitLab](https://about.gitlab.com/)
* [Coding](https://coding.net/)
* [Quilt](http://savannah.nongnu.org/git/?group=quilt)
