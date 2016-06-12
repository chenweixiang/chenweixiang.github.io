---
layout: post
title: "Linux: Tcsh"
tag: Linux
toc: true
---

This article introduces the **tcsh** in detail. And the most of the content is from [Tcsh Manual v6.19.00](http://www.tcsh.org/tcsh.html/top.html). I try to understand all features and add some examples in this article.

<!--more-->

# Instruction

The official website of Tcsh is [here](http://www.tcsh.org/).

## What's csh?

The C shell (**csh**) is a Unix shell that was created by *Bill Joy* while he was a graduate student at *University of California, Berkeley* in the late 1970s. It has been distributed widely, beginning with the 2BSD release of the BSD Unix system that Joy began distributing in 1978. Other early contributors to the ideas or the code were *Michael Ubell*, *Eric Allman*, *Mike O'Brien* and *Jim Kulp*.

The C shell is a command processor typically run in a text window, allowing the user to type commands. The C shell can also read commands from a file, called a script. Like all Unix shells, it supports *filename wildcarding*, *piping*, *here documents*, *command substitution*, *variables and control structures for condition-testing and iteration*. What differentiated the C shell from others, especially in the 1980s, were its interactive features and overall style. Its new features made it easier and faster to use. The overall style of the language looked more like C and was seen as more readable.

## What's Tcsh?

**Tcsh** is a Unix shell based on and compatible with the C shell (**csh**). It is essentially the C shell with **programmable command-line completion**, **command-line editing**, and **a few other features**. Unlike the other common shells, functions cannot be defined in a tcsh script and the user must use aliases instead (as in **csh**).

The **t** in **t**csh comes from the **T** in **T**ENEX, an operating system which inspired *Ken Greer* at Carnegie Mellon University, the author of **tcsh**, with its command-completion feature. Greer began working on his code to implement **Tenex-style file name completion** in September 1975, finally merging it into the C shell in December 1981. Mike Ellis at Fairchild A.I. Labs added **command completion** in September 1983. On October 3, 1983, Greer posted source to the *net.sources* newsgroup.

## Tcsh Releases

| Releases |  Date  |
| :------: | :----: |
| 6.00.00  | 1995-09-23 |
| 6.01.00  | 1995-09-23 |
| 6.02.00  | 1995-09-23 |
| 6.03.00  | 1995-09-23 |
| 6.04.00  | 1995-09-23 |
| 6.05.00  | 1995-09-23 |
| 6.06.00  | 1995-09-23 |
| 6.07.00  | 1996-10-27 |
| 6.08.00  | 1998-10-02 |
| 6.09.00  | 1999-08-06 |
| 6.10.00  | 2000-11-19 |
| 6.11.00  | 2001-09-02 |
| 6.12.00  | 2002-07-23 |
| 6.13.00  | 2004-05-19 |
| 6.14.00  | 2005-03-25 |
| 6.15.00  | 2007-03-03 |
| 6.16.00  | 2008-10-09 |
| 6.17.00  | 2009-07-10 |
| 6.18.00  | 2012-01-14 |
| **6.19.00**  | **2015-05-21** |

<p/>

# SYNOPSIS

***Formats:***
```tcsh [-bcdefFimnqstvVxX] [-Dname[=value]] [arg ...]```
```tcsh -l```

If the first argument (argument 0) to the shell is ```-``` then it is a **login shell**. A **login shell** can be also specified by invoking the shell with the ```-l``` flag as the only argument.

The rest of the flag arguments are interpreted as follows:

| Options | Description |
| :------ | :---------- |
| ```-b``` | Forces a ```break``` from option processing, causing any further shell arguments to be treated as non-option arguments. The remaining arguments will not be interpreted as shell options. This may be used to pass options to a shell script without confusion or possible subterfuge. The shell will not run a set-user ID script without this option. |
| ```-c``` | Commands are read from the following argument (which must be present, and must be a single argument), stored in the **command** shell variable for reference, and executed. Any remaining arguments are placed in the **argv** shell variable. |
| ```-d``` | The shell loads the directory stack from ***~/.cshdirs*** as described under [Startup and shutdown](#startup-and-shutdown), whether or not it is a login shell. (+) |
| ```-e``` | The shell exits if any invoked command terminates abnormally or yields a non-zero exit status. |
| ```-f``` | The shell does not load any resource or startup files, or perform any command hashing, and thus starts **f**aster. |
| ```-F``` | The shell uses *fork*(2) instead of *vfork*(2) to spawn processes. (+) |
| ```-i``` | The shell is **interactive** and prompts for its top-level input, even if it appears to not be a terminal. Shells are interactive without this option if their inputs and outputs are terminals. |
| ```-l``` | The shell is a **login shell**. Applicable only if ```-l``` is the only flag specified. |
| ```-m``` | The shell loads ***~/.tcshrc*** even if it does not belong to the effective user. Newer versions of **su**(1) can pass ```-m``` to the shell. (+) |
| ```-n``` | The shell parses commands but does not execute them. This aids in debugging shell scripts. |
| ```-q``` | The shell accepts **SIGQUIT** and behaves when it is used under a debugger. Job control is disabled. (u) |
| ```-s``` | Command input is taken from the standard input. |
| ```-t``` | The shell reads and executes a single line of input. A ```\``` may be used to escape the newline at the end of this line and continue onto another line. |
| ```-v``` | Sets the **verbose** shell variable, so that command input is echoed after history substitution. |
| ```-V``` | Sets the **verbose** shell variable even before executing ***~/.tcshrc***. |
| ```-x``` | Sets the **echo** shell variable, so that commands are echoed immediately before execution. |
| ```-X``` | Is to ```-x``` as ```-V``` is to ```-v```. |
| ```-Dname[=value]``` | Sets the environment variable *name* to *value*. (Domain/OS only) (+) |
| ```--help``` | Print a help message on the standard output and exit. (+) |
| ```--version``` | Print the version/platform/compilation options on the standard output and exit. This information is also contained in the **version** shell variable. (+) |

<p/>

After processing of flag arguments, if arguments remain but none of the ```-c```, ```-i```, ```-s```, or ```-t``` options were given, the first argument is taken as the name of a file of commands, or *script*, to be executed. The shell opens this file and saves its name for possible resubstitution by **$0**. Because many systems use either the standard version 6 or version 7 shells whose shell scripts are not compatible with this shell, the shell uses such a *standard* shell to execute a script whose first character is not a ```#```, i.e., that does not start with a comment.

Remaining arguments are placed in the **argv** shell variable.

# DESCRIPTION

## Startup and shutdown

A **login shell** begins by executing commands from the system files ***/etc/csh.cshrc*** and ***/etc/csh.login***. It then executes commands from files in the user's home directory: first ***~/.tcshrc*** (+) or, if ***~/.tcshrc*** is not found, ***~/.cshrc***, then ***~/.history*** (or the value of the **histfile** shell variable), then ***~/.login***, and finally ***~/.cshdirs*** (or the value of the **dirsfile** shell variable) (+). The shell may read ***/etc/csh.login*** before instead of after ***/etc/csh.cshrc***, and ***~/.login*** before instead of after ***~/.tcshrc*** or ***~/.cshrc*** and ***~/.history***, if so compiled; see the **version** shell variable. (+)

**Non-login shells** read only ***/etc/csh.cshrc*** and ***~/.tcshrc*** or ***~/.cshrc*** on startup.

For examples of startup files, please consult [the tcshrc project](http://tcshrc.sourceforge.net).

Commands like *stty*(1) and *tset*(1), which need be run only once per login, usually go in one's ***~/.login*** file. Users who need to use the same set of files with both *csh*(1) and *tcsh* can have only a ***~/.cshrc*** which checks for the existence of the **tcsh** shell variable (q.v.) before using *tcsh-specific* commands, or can have both a ***~/.cshrc*** and a ***~/.tcshrc*** which sources (see the builtin command) ***~/.cshrc***. The rest of this manual uses ***~/.tcshrc*** to mean ***~/.tcshrc*** or, if ***~/.tcshrc*** is not found, ***~/.cshrc***.

In the normal case, the shell begins reading commands from the terminal, prompting with ```> ```. (Processing of arguments and the use of the shell to process files containing command scripts are described later.) The shell repeatedly reads a line of command input, breaks it into words, places it on the command history list, parses it and executes each command in the line.

One can log out by typing ```^D``` on an empty line, ```logout``` or ```login``` or via the shell's **autologout** mechanism (see the **autologout** shell variable). When a login shell terminates it sets the **logout** shell variable to ```normal``` or ```automatic``` as appropriate, then executes commands from the files ***/etc/csh.logout*** and ***~/.logout***. The shell may drop **DTR** on logout if so compiled; see the **version** shell variable.

The names of the system login and logout files vary from system to system for compatibility with different *csh*(1) variants; see [FILES](#files).

When startup, the shell begins by executing commands from the following system files:

| Files | Login tcsh | Non-login tcsh |
| :---- | :--------- | :------------- |
| ***/etc/csh.cshrc*** | Yes | Yes |
| ***/etc/csh.login*** | Yes | No  |
| ***~/.tcshrc*** | Yes | Yes |
| ***~/.cshrc*** | Yes, if ***~/.tcshrc*** is not found | Yes, if ***~/.tcshrc*** is not found |
| ***~/.history*** | Yes | No |
| value of **histfile** shell variable | Yes, if ***~/.history*** is not found | No |
| ***~/.login*** | Yes | No |
| ***~/.cshdirs*** | Yes | No |
| value of **dirsfile** shell variable | Yes, if ***~/.cshdirs*** is not found | No |

<p/>

Note: The shell may read ***/etc/csh.login*** before instead of after ***/etc/csh.cshrc***, and ***~/.login*** before instead of after ***~/.tcshrc*** or ***~/.cshrc*** and ***~/.history***, if so compiled; see the **version** shell variable. (+)

When a **login shell** terminates, the shell begins by executing commands from the following system files:

| Files | Login tcsh |
| :---- | :--------: |
| ***/etc/csh.logout*** | Yes |
| ***~/.logout*** | Yes |

<p/>

## The command-line editor (+)

Command-line input can be edited using key sequences much like those used in *emacs*(1) or *vi*(1). The editor is active only when the **edit** shell variable is set, which it is by default in **interactive shells**. The **bindkey** builtin can display and change key bindings. *emacs*(1)-style key bindings are used by default (unless the shell was compiled otherwise; see the **version** shell variable), but **bindkey** can change the key bindings to *vi*(1)-style bindings en masse.

The shell always binds the arrow keys (as defined in the **TERMCAP** environment variable) to

| TERMCAP | Description |
| :------ | :---------- |
| down    | *down-history* |
| up      | *up-history* |
| left    | *backward-char* |
| right   | *forward-char* |

<p/>

unless doing so would alter another single-character binding. One can set the arrow key escape sequences to the empty string with *settc* to prevent these bindings. The ANSI/VT100 sequences for arrow keys are always bound.

Other key bindings are, for the most part, what *emacs*(1) and *vi*(1) users would expect and can easily be displayed by **bindkey**, so there is no need to list them here. Likewise, **bindkey** can list the editor commands with a short description of each. Certain key bindings have different behavior depending if *emacs*(1) or *vi*(1) style bindings are being used; see **vimode** for more information.

Note that editor commands do not have the same notion of a *word* as does the shell. The editor delimits words with any non-alphanumeric characters not in the shell variable **wordchars**, while the shell recognizes only whitespace and some of the characters with special meanings to it, listed under [Lexical structure](#lexical-structure).

***Examples:***

```
chenwx@chenwx ~ $ tcsh
chenwx:~> bindkey
Standard key bindings
"^@"           ->  set-mark-command
"^A"           ->  beginning-of-line
"^B"           ->  backward-char
"^C"           ->  tty-sigintr
"^D"           ->  delete-char-or-list-or-eof
"^E"           ->  end-of-line
"^F"           ->  forward-char
"^G"           ->  is undefined
"^H"           ->  backward-delete-char
"^I"           ->  complete-word
"^J"           ->  newline
"^K"           ->  kill-line
"^L"           ->  clear-screen
...
```

## Completion and listing (+)

The shell is often able to complete words when given a unique abbreviation. Type part of a word (for example ```ls /usr/lost```) and hit the **tab** key to run the **complete-word** editor command. The shell completes the filename ```/usr/lost``` to ```/usr/lost+found/```, replacing the incomplete word with the complete word in the input buffer. (Note the terminal ```/```; completion adds a ```/``` to the end of completed directories and a space to the end of other completed words, to speed typing and provide a visual indicator of successful completion. The **addsuffix** shell variable can be unset to prevent this.) If no match is found (perhaps ```/usr/lost+found``` doesn't exist), the terminal bell rings. If the word is already complete (perhaps there is a ```/usr/lost``` on your system, or perhaps you were thinking too far ahead and typed the whole thing) a ```/``` or space is added to the end if it isn't already there.

Completion works anywhere in the line, not at just the end; completed text pushes the rest of the line to the right. Completion in the middle of a word often results in leftover characters to the right of the cursor that need to be deleted.

Commands and variables can be completed in much the same way. For example, typing ```em[tab]``` would complete ```em``` to ```emacs``` if *emacs* were the only command on your system beginning with ```em```. Completion can find a command in any directory in path or if given a full pathname. Typing ```echo $ar[tab]``` would complete ```$ar``` to ```$argv``` if no other variable began with ```ar```.

The shell parses the input buffer to determine whether the word you want to complete should be completed as a filename, command or variable. The first word in the buffer and the first word following ```;```, ```|```, ```|&```, ```&&``` or ```||``` is considered to be a command. A word beginning with ```$``` is considered to be a variable. Anything else is a filename. An empty line is completed as a filename.

You can list the possible completions of a word at any time by typing ```^D``` to run the **delete-char-or-list-or-eof** editor command. The shell lists the possible completions using the **ls-F** builtin (q.v.) and reprints the prompt and unfinished command line, for example:

```
> ls /usr/l[^D]
lbin/ lib/ local/ lost+found/
> ls /usr/l
```

 If the **autolist** shell variable is set, the shell lists the remaining choices (if any) whenever completion fails:

```
> set autolist
> nm /usr/lib/libt[tab]
libtermcap.a@ libtermlib.a@
> nm /usr/lib/libterm
```

If **autolist** is set to ```ambiguous```, choices are listed only when completion fails and adds no new characters to the word being completed.

A filename to be completed can contain variables, your own or others' home directories abbreviated with ```~``` (see [Filename substitution](#filename-substitution)) and directory stack entries abbreviated with ```=``` (see [Directory stack substitution](#directory-stack-substitution)). For example,

```
> ls ~k[^D]
kahn kas kellogg
> ls ~ke[tab]
> ls ~kellogg/
```

or

```
> set local = /usr/local
> ls $lo[tab]
> ls $local/[^D]
bin/ etc/ lib/ man/ src/
> ls $local/
```

Note that variables can also be expanded explicitly with the **expand-variables** editor command.

**delete-char-or-list-or-eof** lists at only the end of the line; in the middle of a line it deletes the character under the cursor and on an empty line it logs one out or, if **ignoreeof** is set, does nothing. ```M-^D```, bound to the editor command **list-choices**, lists completion possibilities anywhere on a line, and **list-choices** (or any one of the related editor commands that do or don't delete, list and/or log out, listed under **delete-char-or-list-or-eof**) can be bound to ```^D``` with the bindkey builtin command if so desired.

The **complete-word-fwd** and **complete-word-back** editor commands (not bound to any keys by default) can be used to cycle up and down through the list of possible completions, replacing the current word with the next or previous word in the list.

The shell variable **fignore** can be set to a list of suffixes to be ignored by completion. Consider the following:

```
> ls
Makefile condiments.h~ main.o side.c
README main.c meal side.o
condiments.h main.c~
> set fignore = (.o \~)
> emacs ma[^D]
main.c main.c~ main.o
> emacs ma[tab]
> emacs main.c
```

```main.c~``` and ```main.o``` are ignored by completion (but not listing), because they end in suffixes in fignore. Note that a ```\``` was needed in front of ```~``` to prevent it from being expanded to home as described under Filename substitution. **fignore** is ignored if only one completion is possible.

If the **complete** shell variable is set to ```enhance```, completion 1) ignores case and 2) considers periods, hyphens and underscores (```.```, ```-``` and ```_```) to be word separators and hyphens and underscores to be equivalent. If you had the following files

```comp.lang.c comp.lang.perl comp.std.c++ comp.lang.c++ comp.std.c```

and typed ```mail -f c.l.c[tab]```, it would be completed to ```mail -f comp.lang.c```, and ```^D``` would list ```comp.lang.c``` and ```comp.lang.c++```. ```mail -f c..c++[^D]``` would list ```comp.lang.c++``` and ```comp.std.c++```. Typing ```rm a--file[^D]``` in the following directory

```A_silly_file a-hyphenated-file another_silly_file```

would list all three files, because case is ignored and hyphens and underscores are equivalent. Periods, however, are not equivalent to hyphens or underscores.

If the complete shell variable is set to ```Enhance```, completion ignores case and differences between a hyphen and an underscore word separator only when the user types a lowercase character or a hyphen. Entering an uppercase character or an underscore will not match the corresponding lowercase character or hyphen word separator. Typing ```rm a--file[^D]``` in the directory of the previous example would still list all three files, but typing ```rm A--file``` would match only ```A_silly_file``` and typing ```rm a__file[^D]``` would match just ```A_silly_file``` and ```another_silly_file``` because the user explicitly used an uppercase or an underscore character.

Completion and listing are affected by several other shell variables:

**recexact** can be set to complete on the shortest possible unique match, even if more typing might result in a longer match:

```
> ls
fodder foo food foonly
> set recexact
> rm fo[tab]
```

just beeps, because ```fo``` could expand to ```fod``` or ```foo```, but if we type another ```o```,

```
> rm foo[tab]
> rm foo
```

the completion completes on ```foo```, even though ```food``` and ```foonly``` also match.

**autoexpand** can be set to run the **expand-history** editor command before each completion attempt.

**autocorrect** can be set to spelling-correct the word to be completed (see Spelling correction) before each completion attempt and correct can be set to complete commands automatically after one hits ```return```.

**matchbeep** can be set to make completion beep or not beep in a variety of situations;

**nobeep** can be set to never beep at all.

**nostat** can be set to a list of directories and/or patterns that match directories to prevent the completion mechanism from *stat*(2)ing those directories.

**listmax** and **listmaxrows** can be set to limit the number of items and rows (respectively) that are listed without asking first.

**recognize_only_executables** can be set to make the shell list only executables when listing commands, but it is quite slow.

Finally, the **complete** builtin command can be used to tell the shell how to complete words other than filenames, commands and variables. Completion and listing do not work on glob-patterns (see [Filename substitution](#filename-substitution)), but the **list-glob** and **expand-glob** editor commands perform equivalent functions for glob-patterns.

## Spelling correction (+)

The shell can sometimes correct the spelling of filenames, commands and variable names as well as completing and listing them.

Individual words can be spelling-corrected with the **spell-word** editor command (usually bound to ```M-s``` and ```M-S```) and the entire input buffer with **spell-line** (usually bound to ```M-$```). The **correct** shell variable can be set to ```cmd``` to correct the command name or ```all``` to correct the entire line each time return is typed, and **autocorrect** can be set to correct the word to be completed before each completion attempt.

When spelling correction is invoked in any of these ways and the shell thinks that any part of the command line is misspelled, it prompts with the corrected line:

```
> set correct = cmd
> lz /usr/bin
CORRECT>ls /usr/bin (y|n|e|a)?
```

One can answer:

* ***y*** or ***space*** to execute the corrected line,
* ***e*** to leave the uncorrected command in the input buffer,
* ***a*** to abort the command as if ```^C``` had been hit, and
* anything else to execute the original line unchanged.

Spelling correction recognizes user-defined completions (see the **complete** builtin command). If an input word in a position for which a completion is defined resembles a word in the completion list, spelling correction registers a misspelling and suggests the latter word as a correction. However, if the input word does not match any of the possible completions for that position, spelling correction does not register a misspelling.

Like completion, spelling correction works anywhere in the line, pushing the rest of the line to the right and possibly leaving extra characters to the right of the cursor.

## Editor commands (+)

```bindkey``` lists key bindings and ```bindkey -l``` lists and briefly describes editor commands. Only new or especially interesting editor commands are described here. See *emacs*(1) and *vi*(1) for descriptions of each editor's key bindings.

```^character``` means a control character and ```M-character``` a meta character, typed as escape-*character* on terminals without a meta key. Case counts, but commands that are bound to letters by default are bound to both lower- and uppercase letters for convenience.

| Commands | Default Bindings | Description |
| :------- | :--------------- | :---------- |
| backward-char | ```^B```<br>```left``` | Move back a character. Cursor behavior modified by **vimode**. |
| forward-char | ```^F```<br>```right``` | Move forward one character. Cursor behavior modified by **vimode**. |
| backward-delete-word | ```M-^H```<br>```M-^?``` | Cut from beginning of current word to cursor - saved in cut buffer. Word boundary behavior modified by **vimode**. |
| backward-word | ```M-b```<br>```M-B``` | Move to beginning of current word. Word boundary and cursor behavior modified by **vimode**. |
| forward-word | ```M-f```<br>```M-F``` | Move forward to end of current word. Word boundary and cursor behavior modified by **vimode**. |
| beginning-of-line | ```^A```<br>```home``` | Move to beginning of line. Cursor behavior modified by **vimode**. |
| end-of-line | ```^E```<br>```end``` | Move cursor to end of line. Cursor behavior modified by **vimode**. |
| capitalize-word | ```M-c```<br>```M-C``` | Capitalize the characters from cursor to end of current word. Word boundary behavior modified by **vimode**. |
| downcase-word | ```M-l```<br>```M-L``` | Lowercase the characters from cursor to end of current word. Word boundary behavior modified by **vimode**. |
| complete-word | ```tab``` | Completes a word as described under [Completion and listing](#completion-and-listing). |
| complete-word-raw | ```^X-tab``` | Like **complete-word**, but ignores user-defined completions. |
| complete-word-fwd | *not bound* | Replaces the current word with the first word in the list of possible completions. May be repeated to step down through the list. At the end of the list, beeps and reverts to the incomplete word. |
| complete-word-back | *not bound* | Like **complete-word-fwd**, but steps up from the end of the list. |
| copy-prev-word | ```M-^_``` | Copies the previous word in the current line into the input buffer. See also **insert-last-word**. Word boundary behavior modified by **vimode**. |
| dabbrev-expand | ```M-/``` | Expands the current word to the most recent preceding one for which the current is a leading substring, wrapping around the history list (once) if necessary. Repeating **dabbrev-expand** without any intervening typing changes to the next previous word etc., skipping identical matches much like **history-search-backward** does. |
| delete-char | *not bound* | Deletes the character under the cursor. See also **delete-char-or-list-or-eof**. Cursor behavior modified by **vimode**. |
| delete-char-or-list | *not bound* | Does **delete-char** if there is a character under the cursor or list-choices at the end of the line. See also **delete-char-or-list-or-eof**. |
| delete-char-or-list-or-eof | ```^D``` | Does **delete-char** if there is a character under the cursor, list-choices at the end of the line or end-of-file on an empty line. See also those three commands, each of which does only a single action, and **delete-char-or-eof**, **delete-char-or-list** and **list-or-eof**, each of which does a different two out of the three. |
| delete-char-or-eof | *not bound* | Does **delete-char** if there is a character under the cursor or end-of-file on an empty line. See also **delete-char-or-list-or-eof**. Cursor behavior modified by **vimode**. |
| delete-word | ```M-d```<br>```M-D``` | Cut from cursor to end of current word - save in cut buffer. Word boundary behavior modified by **vimode**. |
| up-history | ```up-arrow```<br>```^P``` | Copies the previous entry in the history list into the input buffer. If **histlit** is set, uses the literal form of the entry. May be repeated to step up through the history list, stopping at the top. |
| down-history | ```down-arrow```<br>```^N``` | Like **up-history**, but steps down, stopping at the original input line. |
| history-search-backward | ```M-p```<br>```M-P``` | Searches backwards through the history list for a command beginning with the current contents of the input buffer up to the cursor and copies it into the input buffer. The search string may be a glob-pattern (see [Filename substitution](#filename-substitution)) containing ```*```, ```?```, ```[]``` or ```{}```. **up-history** and **down-history** will proceed from the appropriate point in the history list. Emacs mode only. See also **history-search-forward** and **i-search-back**. |
| history-search-forward | ```M-n```<br>```M-N``` | Like **history-search-backward**, but searches forward. |
|  i-search-back | *not bound* | Searches backward like **history-search-backward**, copies the first match into the input buffer with the cursor positioned at the end of the pattern, and prompts with ```bck: ``` and the first match. Additional characters may be typed to extend the search, **i-search-back** may be typed to continue searching with the same pattern, wrapping around the history list if necessary. |
| i-search-fwd | *not bound* | Like **i-search-back**, but searches forward. Word boundary behavior modified by **vimode**. |
| end-of-file | *not bound* | Signals an end of file, causing the shell to exit unless the **ignoreeof** shell variable (q.v.) is set to prevent this. See also **delete-char-or-list-or-eof**. |
| expand-history | ```M-space``` | Expands history substitutions in the current word. See [History substitution](#history-substitution). See also **magic-space**, **toggle-literal-history** and the **autoexpand** shell variable. |
| expand-glob | ```^X-*``` | Expands the glob-pattern to the left of the cursor. See [Filename substitution](#filename-substitution). |
| expand-line | *not bound* | Like **expand-history**, but expands history substitutions in each word in the input buffer. |
| expand-variables | ```^X-$``` | Expands the variable to the left of the cursor. See [Variable substitution](#variable-substitution). |
| insert-last-word | ```M-_``` | Inserts the last word of the previous input line (```!$```) into the input buffer. See also **copy-prev-word**. |
| list-choices | ```M-^D``` | Lists completion possibilities as described under [Completion and listing](#completion-and-listing). See also **delete-char-or-list-or-eof** and **list-choices-raw**. |
| list-choices-raw | ```^X-^D``` | Like **list-choices**, but ignores user-defined completions. |
| list-glob | ```^X-g```<br>```^X-G``` | Lists (via the **ls-F** builtin) matches to the glob-pattern (see [Filename substitution](#filename-substitution)) to the left of the cursor. |
| list-or-eof | *not bound* | Does **list-choices** or **end-of-file** on an empty line. See also **delete-char-or-list-or-eof*. |
| magic-space | *not bound* | Expands history substitutions in the current line, like **expand-history**, and inserts a space. **magic-space** is designed to be bound to the space bar, but is not bound by default. |
| normalize-command | ```^X-?``` | Searches for the current word in **PATH** and, if it is found, replaces it with the full path to the executable. Special characters are quoted. Aliases are expanded and quoted but commands within aliases are not. This command is useful with commands that take commands as arguments, e.g., ```dbx``` and ```sh -x```. |
| normalize-path | ```^X-n```<br>```^X-N``` | Expands the current word as described under the **expand** setting of the **symlinks** shell variable. |
| overwrite-mode | *not bound* | Toggles between input and overwrite modes. |
| run-fg-editor | ```M-^Z``` | Saves the current input line and looks for a stopped job where the file name portion of its first word is found in the **editors** shell variable. If **editors** is not set, then the file name portion of the **EDITOR** environment variable (```ed``` if unset) and the **VISUAL** environment variable (```vi``` if unset) will be used. If such a job is found, it is restarted as if ```fg %job``` had been typed. This is used to toggle back and forth between an editor and the shell easily. Some people bind this command to ```^Z``` so they can do this even more easily. |
| run-help | ```M-h```<br>```M-H``` | Searches for documentation on the current command, using the same notion of ```current command``` as the completion routines, and prints it. There is no way to use a pager; run-help is designed for short help files. If the special alias **helpcommand** is defined, it is run with the command name as a sole argument. Else, documentation should be in a file named *command.help*, *command.1*, *command.6*, *command.8* or *command*, which should be in one of the directories listed in the **HPATH** environment variable. If there is more than one help file only the first is printed. |
| self-insert-command | *text characters* | In insert mode (the default), inserts the typed character into the input line after the character under the cursor. In overwrite mode, replaces the character under the cursor with the typed character. The input mode is normally preserved between lines, but the **inputmode** shell variable can be set to ```insert``` or ```overwrite``` to put the editor in that mode at the beginning of each line. See also **overwrite-mode**. |
| sequence-lead-in | ```arrow prefix```<br><br>```meta prefix```<br><br>```^X``` | Indicates that the following characters are part of a multi-key sequence. Binding a command to a multi-key sequence really creates two bindings: the first character to **sequence-lead-in** and the whole sequence to the command. All sequences beginning with a character bound to **sequence-lead-in** are effectively bound to undefined-key unless bound to another command. |
| spell-line | ```M-$``` | Attempts to correct the spelling of each word in the input buffer, like **spell-word**, but ignores words whose first character is one of ```-```, ```!```, ```^``` or ```%```, or which contain ```\```, ```*``` or ```?```, to avoid problems with switches, substitutions and the like. See [Spelling correction](#spelling-correction). |
| spell-word | ```M-s```<br>```M-S``` | Attempts to correct the spelling of the current word as described under [Spelling correction](#spelling-correction). Checks each component of a word which appears to be a pathname. |
| toggle-literal-history | ```M-r```<br>```M-R``` | Expands or ```unexpands``` history substitutions in the input buffer. See also **expand-history** and the **autoexpand** shell variable. |
| undefined-key | *any unbound key* | Beeps. |
| vi-beginning-of-next-word | *not bound* | Vi goto the beginning of next word. Word boundary and cursor behavior modified by **vimode**. |
| vi-eword | *not bound* | Vi move to the end of the current word. Word boundary behavior modified by **vimode**. |
| vi-search-back | ```?``` | Prompts with ```?``` for a search string (which may be a **glob-pattern**, as with **history-search-backward**), searches for it and copies it into the input buffer. The bell rings if no match is found. Hitting return ends the search and leaves the last match in the input buffer. Hitting escape ends the search and executes the match. **vi** mode only. |
| vi-search-fwd | ```/``` | Like **vi-search-back**, but searches forward. |
| which-command | ```M-?``` | Does a which (see the description of the **builtin** command) on the first word of the input buffer. |
| yank-pop | ```M-y``` | When executed immediately after a yank or another **yank-pop**, replaces the yanked string with the next previous string from the killring. This also has the effect of rotating the killring, such that this string will be considered the most recently killed by a later **yank** command. Repeating **yank-pop** will cycle through the killring any number of times. |

<p/>

## Lexical structure

The shell splits input lines into words at **blanks** and **tabs**. The special characters ```&``` ```|``` ```;``` ```<``` ```>``` ```(``` ```)``` and the doubled characters ```&&``` ```||``` ```<<``` ```>>``` are always separate words, whether or not they are surrounded by whitespace.

When the shell's input is not a terminal, the character ```#``` is taken to begin a comment. Each ```#``` and the rest of the input line on which it appears is discarded before further parsing.

A special character (including a **blank** or **tab**) may be prevented from having its special meaning, and possibly made part of another word, by preceding it with a backslash (```\```) or enclosing it in single (```'```), double (```"```) or backward (``` \` ```) quotes. When not otherwise quoted a newline preceded by a ``` \' ``` is equivalent to a blank, but inside quotes this sequence results in a newline.

Furthermore, all [Substitutions](#substitutions) except [History substitution](#history-substitution) can be prevented by enclosing the strings (or parts of strings) in which they appear with single quotes or by quoting the crucial character(s) (e.g., ```$``` or ``` \` ``` for [Variable substitution](#variable-substitution) or [Command substitution](#command-substitution) respectively) with ```\```. ([Alias substitution](#alias-substitution) is no exception: quoting in any way any character of a word for which an alias has been defined prevents substitution of the alias. The usual way of quoting an alias is to precede it with a backslash.) [History substitution](#history-substitution) is prevented by backslashes but not by single quotes. Strings quoted with double or backward quotes undergo [Variable substitution](#variable-substitution) and [Command substitution](#command-substitution), but other substitutions are prevented.

Text inside single or double quotes becomes a single word (or part of one). Metacharacters in these strings, including **blank** and **tabs**, do not form separate words. Only in one special case (see [Command substitution](#command-substitution)) can a double-quoted string yield parts of more than one word; single-quoted strings never do. Backward quotes are special: they signal Command substitution (q.v.), which may result in more than one word.

Quoting complex strings, particularly strings which themselves contain quoting characters, can be confusing. Remember that quotes need not be used as they are in human writing! It may be easier to quote not an entire string, but only those parts of the string which need quoting, using different types of quoting to do so if appropriate.

The **backslash_quote** shell variable (q.v.) can be set to make backslashes always quote ```\```, ```'```, and ```"```. (+) This may make complex quoting tasks easier, but it can cause syntax errors in *csh*(1) scripts.

# Substitutions

We now describe the various transformations the shell performs on the input in the order in which they occur. We note in passing the data structures involved and the commands and variables which affect them. Remember that substitutions can be prevented by quoting as described under [Lexical structure](#lexical-structure).

## History substitution

Each command, or **event**, input from the terminal is saved in the history list. The previous command is always saved, and the **history** shell variable can be set to a number to save that many commands. The **histdup** shell variable can be set to not save duplicate events or consecutive duplicate events.

Saved commands are numbered sequentially from 1 and stamped with the time. It is not usually necessary to use event numbers, but the current event number can be made part of the prompt by placing an ```!``` in the **prompt** shell variable.

The shell actually saves history in expanded and literal (unexpanded) forms. If the **histlit** shell variable is set, commands that display and store history use the literal form.

The **history** builtin command can print, store in a file, restore and clear the history list at any time, and the **savehist** and **histfile** shell variables can be set to store the history list automatically on logout and restore it on login.

History substitutions introduce words from the history list into the input stream, making it easy to repeat commands, repeat arguments of a previous command in the current command, or fix spelling mistakes in the previous command with little typing and a high degree of confidence.

History substitutions begin with the character ```!```. They may begin anywhere in the input stream, but they do not nest. The ```!``` may be preceded by a ```\``` to prevent its special meaning; for convenience, a ```!``` is passed unchanged when it is followed by a **blank**, **tab**, **newline**, ```=``` or ```(```. History substitutions also occur when an input line begins with ```^```. This special abbreviation will be described later. The characters used to signal history substitution (```!``` and ```^```) can be changed by setting the **histchars** shell variable. Any input line which contains a history substitution is printed before it is executed.

A history substitution may have an **event specification**, which indicates the event from which words are to be taken, a **word designator**, which selects particular words from the chosen event, and/or a **modifier**, which manipulates the selected words.

An event specification can be

| event | Description |
| :---: | :---------- |
| *n*   | A number, referring to a particular event |
| *-n*  | An offset, referring to the event *n* before the current event |
| *#*   | The current event. This should be used carefully in *csh*(1), where there is no check for recursion. **tcsh** allows 10 levels of recursion. (+) |
| !     | The previous event (equivalent to ```-1```) |
| *s*   | The most recent event whose first word begins with the string *s* |
| ?*s*? | The most recent event which contains the string *s*. The second ```?``` can be omitted if it is immediately followed by a newline. |

<p/>

For example, consider this bit of someone's history list:

```
9 8:30 nroff -man wumpus.man
10 8:31 cp wumpus.man wumpus.man.old
11 8:36 vi wumpus.man
12 8:37 diff wumpus.man.old wumpus.man
```

The commands are shown with their event numbers and time stamps. The current event, which we haven't typed in yet, is event 13. ```!11``` and ```!-2``` refer to event 11. ```!!``` refers to the previous event, 12. ```!!``` can be abbreviated ```!``` if it is followed by ```:```. ```!n``` refers to event 9, which begins with ```n```. ```!?old?``` also refers to event 12, which contains ```old```. Without word designators or modifiers history references simply expand to the entire event, so we might type ```!cp``` to redo the copy command or ```!!|more``` if the ```diff``` output scrolled off the top of the screen.

History references may be insulated from the surrounding text with braces if necessary. For example, ```!vdoc``` would look for a command beginning with ```vdoc```, and, in this example, not find one, but ```!{v}doc``` would expand unambiguously to ```vi wumpus.mandoc```. Even in braces, history substitutions do not nest.

(+) While *csh*(1) expands, for example, ```!3d``` to event 3 with the letter ```d``` appended to it, tcsh expands it to the last event beginning with ```3d```; only completely numeric arguments are treated as event numbers. This makes it possible to recall events beginning with numbers. To expand ```!3d``` as in *csh*(1) say ```!{3}d```.

To select words from an event we can follow the **event specification** by a ```:``` and a designator for the desired words. The words of an input line are numbered from 0, the first (usually command) word being 0, the second word (first argument) being 1, etc. The basic word designators are:

| Designators | Description |
| :---------: | :---------- |
| 0           | The first (command) word |
| n           | The *n*th argument |
| ^           | The first argument, equivalent to **1** |
| $           | The last argument |
| %           | The word matched by an **?s?** search |
| x-y         | A range of words |
| -y          | Equivalent to **0-y** |
| *           | Equivalent to ```^-$```, but returns nothing if the event contains only 1 word |
| x*          | Equivalent to ```x-$``` |
| x-          | Equivalent to ```x*```, but omitting the last word (```$```) |

<p/>

Selected words are inserted into the command line separated by single blanks. For example, the **diff** command in the previous example might have been typed as ```diff !!:1.old !!:1``` (using ```:1``` to select the first argument from the previous event) or ```diff !-2:2 !-2:1``` to select and swap the arguments from the **cp** command. If we didn't care about the order of the **diff** we might have said ```diff !-2:1-2``` or simply ```diff !-2:*```. The **cp** command might have been written ```cp wumpus.man !#:1.old```, using ```#``` to refer to the current event. ```!n:- hurkle.man``` would reuse the first two words from the **nroff** command to say ```nroff -man hurkle.man```.

The ```:``` separating the event specification from the word designator can be omitted if the argument selector begins with a ```^```, ```$```, ```*```, ```%``` or ```-```. For example, our **diff** command might have been ```diff !!^.old !!^``` or, equivalently, ```diff !!$.old !!$```. However, if ```!!``` is abbreviated ```!```, an argument selector beginning with ```-``` will be interpreted as an event specification.

A history reference may have a word designator but no event specification. It then references the previous command. Continuing our **diff** example, we could have said simply ```diff !^.old !^``` or, to get the arguments in the opposite order, just ```diff !*```.

## Alias substitution

*TBD*

## Variable substitution

*TBD*

## Command, filename and directory stack substitution

*TBD*

## Command substitution

*TBD*

## Filename substitution

*TBD*

## Directory stack substitution (+)

*TBD*

## Other substitutions (+)

*TBD*

# Commands

## Simple commands, pipelines and sequences

*TBD*

## Builtin and non-builtin command execution

*TBD*

## Input/output

*TBD*

# Features

## Control flow

*TBD*

## Expressions

*TBD*

## Logical, arithmetical and comparison operators

*TBD*

## Command exit status

*TBD*

## File inquiry operators

*TBD*

# Jobs

## Status reporting

*TBD*

## Automatic, periodic and timed events (+)

*TBD*

## Native Language System support (+)

*TBD*

## OS variant support (+)

*TBD*

## Signal handling

*TBD*

## Terminal management (+)

*TBD*

# REFERENCE

## Builtin commands

| Builtins | Description |
| :------- | :---------- |
| ```builtins``` | ```builtins``` (+)<br>Prints the names of all builtin commands. |
| ```jobs``` | ```jobs [-l]```<br>Lists the active jobs. With ```-l```, lists process IDs in addition to the normal information. On TCF systems, prints the site on which each job is executing. |
| ```fg``` | ```fg [%job ...]```<br>Brings the specified jobs (or, without arguments, the current job) into the foreground, continuing each if it is stopped. *job* may be a number, a string, ``` ` ```, ```%```, ```+``` or ```-``` as described under [Jobs](#jobs). See also the *run-fg-editor* editor command. |
| ```bg``` | ```bg [%job ...]```<br>Puts the specified jobs (or, without arguments, the current job) into the background, continuing each if it is stopped. *job* may be a number, a string, ``` ` ```, ```%```, ```+``` or ```-``` as described under [Jobs](#jobs). |
| ```%job``` | A synonym for the **fg** builtin command. |
| ```%job &``` | A synonym for the **bg** builtin command. |
| ```stop``` | ```stop %job|pid ...```<br>Stops the specified jobs or processes which are executing in the background. *job* may be a number, a string, ``` ` ```, ```%```, ```+``` or ```-``` as described under [Jobs](#jobs). There is no default *job*; saying just ```stop``` does not stop the current job. |
| ```kill``` | ```kill [-s signal] %job|pid ...```<br>The first and second forms sends the specified *signal* (or, if none is given, the **TERM** (terminate) signal) to the specified jobs or processes. *job* may be a number, a string, ``` ` ```, ```%```, ```+``` or ```-``` as described under [Jobs](#jobs). Signals are either given by number or by name (as given in ```/usr/include/signal.h```, stripped of the prefix **SIG**). There is no default job; saying just ```kill``` does not send a signal to the current job. If the signal being sent is **TERM** (terminate) or **HUP** (hangup), then the job or process is sent a **CONT** (continue) signal as well.<br><br>```kill -l```<br>The third form lists the signal names. |
| ```notify``` | ```notify [%job ...]```<br>Causes the shell to notify the user asynchronously when the status of any of the specified jobs (or, without ```%job```, the current job) changes, instead of waiting until the next prompt as is usual. *job* may be a number, a string, ``` ` ```, ```%```, ```+``` or ```-``` as described under [Jobs](#jobs). See also the **notify** shell variable. |
| ```:``` | Does nothing, successfully. |
| ```wait``` | The shell waits for all background jobs. If the shell is interactive, an interrupt will disrupt the **wait** and cause the shell to print the names and job numbers of all outstanding jobs. |
| ```@``` | ```@```<br>The first form prints the values of all shell variables.<br><br>```@ name = expr```<br>The second form assigns the value of *expr* to *name*.<br><br>```@ name[index] = expr```<br>The third form assigns the value of *expr* to the *index*'th component of *name*; both *name* and its *index*'th component must already exist. *expr* may contain the operators ```*```, ```+```, etc., as in C. If *expr* contains ```<```, ```>```, ```&``` or ``` ` ``` then at least that part of *expr* must be placed within ```()```. Note that the syntax of *expr* has nothing to do with that described under [Expressions](#expressions).<br><br>```@ name++|--```<br>```@ name[index]++|--```<br>The fourth and fifth forms increment (```++```) or decrement (```--```) *name* or its *index*'th component.<br><br>The space between ```@``` and *name* is required. The spaces between *name* and ```=``` and between ```=``` and *expr* are optional. Components of *expr* must be separated by spaces. |
| ```alias``` | ```alias [name [wordlist]]```<br>Without arguments, prints all aliases. With *name*, prints the alias for *name*. With *name* and *wordlist*, assigns *wordlist* as the alias of *name*. *wordlist* is command and filename substituted. *name* may not be ```alias``` or ```unalias```. See also the **unalias** builtin command. |
| ```unalias``` | ```unalias pattern```<br>Removes all aliases whose names match *pattern*. ```unalias *``` thus removes all aliases. It is not an error for nothing to be **unalias**ed. |
| ```alloc``` | ```alloc```<br>Shows the amount of dynamic memory acquired, broken down into used and free memory. With an argument shows the number of free and used blocks in each size category. The categories start at size 8 and double at each step. This command's output may vary across system types, because systems other than the VAX may use a different memory allocator. |
| ```bindkey``` | ```bindkey [-l|-d|-e|-v|-u]``` (+)<br>```bindkey [-a] [-b] [-k] [-r] [--] key``` (+)<br>```bindkey [-a] [-b] [-k] [-c|-s] [--] key command``` (+)<br>Without options, the first form lists all bound keys and the editor command to which each is bound, the second form lists the editor command to which *key* is bound and the third form binds the editor command *command* to *key*. |
| ```bs2cmd``` | ```bs2cmd bs2000-command``` (+)<br>Passes *bs2000-command* to the BS2000 command interpreter for execution. Only non-interactive commands can be executed, and it is not possible to execute any command that would overlay the image of the current process, like /EXECUTE or /CALL-PROCEDURE. (BS2000 only) |
| ```cd``` | ```cd [-p] [-l] [-n|-v] [\I--] [name]```<br>If a directory *name* is given, changes the shell's working directory to *name*. If not, changes to **home**, unless the **cdtohome** variable is not set, in which case a *name* is required. If *name* is ```-``` it is interpreted as the previous working directory. (+) If *name* is not a subdirectory of the current directory (and does not begin with ```/```, ```./``` or ```../```), each component of the variable **cdpath** is checked to see if it has a subdirectory *name*. Finally, if all else fails but *name* is a shell variable whose value begins with ```/``` or ```.```, then this is tried to see if it is a directory, and the ```-p``` option is implied.<br><br>With ```-p```, prints the final directory stack, just like **dirs**. The ```-l```, ```-n``` and ```-v``` flags have the same effect on **cd** as on **dirs**, and they imply ```-p```. (+) Using ```--``` forces a break from option processing so the next word is taken as the directory name even if it begins with ```-```. (+)<br><br>See also the **implicitcd** and **cdtohome** shell variables. |
| ```chdir``` | ```chdir```<br>A synonym for the **cd** builtin command. |
| ```complete``` | ```complete [command [word/pattern/list[:select]/[[suffix]/] ...]]``` (+)<br>Without arguments, lists all completions. With *command*, lists completions for *command*. With *command* and *word* etc., defines completions. *command* may be a full command name or a glob-pattern (see [Filename substitution](#filename-substitution)). It can begin with ```-``` to indicate that completion should be used only when *command* is ambiguous. |
| ```uncomplete``` | ```uncomplete pattern``` (+)<br>Removes all completions whose names match *pattern*. ```uncomplete *``` thus removes all completions. It is not an error for nothing to be uncompleted. |
| ```dirs``` | ```dirs [-l] [-n|-v]```<br>The first form prints the directory stack. The top of the stack is at the left and the first directory in the stack is the current directory.<br>With ```-l```, ```~``` or ```~name\fP``` in the output is expanded explicitly to **home** or the pathname of the home directory for user **name\fP**. (+)<br>With ```-n```, entries are wrapped before they reach the edge of the screen. (+)<br>With ```-v```, entries are printed one per line, preceded by their stack positions. (+)<br>If more than one of ```-n``` or ```-v``` is given, ```-v``` takes precedence. ```-p``` is accepted but does nothing.<br><br>```dirs -S|-L [filename]``` (+)<br>With ```-S```, the second form saves the directory stack to *filename* as a series of **cd** and **pushd** commands.<br>With ```-L```, the shell sources *filename*, which is presumably a directory stack file saved by the ```-S``` option or the **savedirs** mechanism. In either case, **dirsfile** is used if *filename* is not given and ```~/.cshdirs``` is used if **dirsfile** is unset.<br><br>Note that **login shells** do the equivalent of ```dirs -L``` on startup and, if **savedirs** is set, ```dirs -S``` before exiting. Because only ```~/.tcshrc``` is normally sourced before ```~/.cshdirs```, **dirsfile** should be set in ```~/.tcshrc``` rather than ```~/.login```.<br><br>```dirs -c``` (+)<br>The last form clears the directory stack. |
| ```echo``` | ```echo [-n] word ...```<br>Writes each word to the shell's standard output, separated by spaces and terminated with a newline. The **echo_style** shell variable may be set to emulate (or not) the flags and escape sequences of the BSD and/or System V versions of echo; see *echo*(1). |
| ```glob``` | ```glob wordlist```<br>Like **echo**, but the ```-n``` parameter is not recognized and words are delimited by null characters in the output. Useful for programs which wish to use the shell to filename expand a list of words. |
| ```telltc``` | ```telltc``` (+)<br>Lists the values of all terminal capabilities (see *termcap*(5)). |
| ```settc``` | ```settc cap value``` (+)<br>Tells the shell to believe that the terminal capability *cap* (as defined in *termcap*(5)) has the value *value*. No sanity checking is done. Concept terminal users may have to ```settc xn no``` to get proper wrapping at the rightmost column. |
| ```echotc``` | ```echotc [-sv] arg ...``` (+)<br>Exercises the terminal capabilities (see *termcap*(5)) in args. For example, ```echotc home``` sends the cursor to the home position, ```echotc cm 3 10``` sends it to column 3 and row 10, and ```echotc ts 0; echo "This is a test."; echotc fs``` prints "This is a test." in the status line. |
| ```eval``` | ```eval arg ...```<br>Treats the arguments as input to the shell and executes the resulting command(s) in the context of the current shell. This is usually used to execute commands generated as the result of command or variable substitution, because parsing occurs before these substitutions. See *tset*(1) for a sample use of *eval*. |
| ```exec``` | ```exec command```<br>Executes the specified *command* in place of the current shell. |
| ```exit``` | ```exit [expr]```<br>The shell exits either with the value of the specified *expr* (an expression, as described under [Expressions](#expressions)) or, without *expr*, with the value 0. |
| ```filetest``` | ```filetest -op file ...``` (+)<br>Applies *op* (which is a file inquiry operator as described under [File inquiry operators](#file-inquiry-operators)) to each *file* and returns the results as a space-separated list. |
| ```getspath``` | ```getspath``` (+)<br>Prints the system execution path. (TCF only) |
| ```getxvers``` | ```getxvers``` (+)<br>Prints the experimental version prefix. (TCF only) |
| ```goto``` | ```goto word```<br>*word* is filename and command-substituted to yield a string of the form ```label```. The shell rewinds its input as much as possible, searches for a line of the form ```label:```, possibly preceded by blanks or tabs, and continues execution after that line. |
| ```hashstat``` | ```hashstat```<br>Prints a statistics line indicating how effective the internal hash table has been at locating commands (and avoiding *exec*'s). An *exec* is attempted for each component of the **path** where the hash function indicates a possible hit, and in each component which does not begin with a ```/```. On machines without *vfork*(2), prints only the number and size of hash buckets. |
| ```rehash``` | ```rehash```<br>Causes the internal hash table of the contents of the directories in the **path** variable to be recomputed. This is needed if the **autorehash** shell variable is not set and new commands are added to directories in path while you are logged in. With **autorehash**, a new command will be found automatically, except in the special case where another command of the same name which is located in a different directory already exists in the hash table. Also flushes the cache of home directories built by tilde expansion. |
| ```unhash``` | ```unhash```<br>Disables use of the internal hash table to speed location of executed programs. |
| ```history``` | ```history [-hTr] [n]```<br>The first form prints the history event list. If *n* is given only the *n* most recent events are printed or saved.<br>With ```-h```, the history list is printed without leading numbers.<br>If ```-T``` is specified, timestamps are printed also in comment form. (This can be used to produce files suitable for loading with ```history -L``` or ```source -h```.)<br>With ```-r```, the order of printing is most recent first rather than oldest first.<br><br>```history -S|-L|-M [filename]``` (+)<br>With ```-S```, the second form saves the history list to *filename*. If the first word of the **savehist** shell variable is set to a number, at most that many lines are saved. If the second word of **savehist** is set to ```merge```, the history list is merged with the existing history file instead of replacing it (if there is one) and sorted by time stamp. (+) Merging is intended for an environment like the X Window System with several shells in simultaneous use. If the second word of **savehist** is ```merge``` and the third word is set to ```lock```, the history file update will be serialized with other shell sessions that would possibly like to merge history at exactly the same time.<br>With ```-L```, the shell appends *filename*, which is presumably a history list saved by the ```-S``` option or the **savehist** mechanism, to the history list. ```-M``` is like ```-L```, but the contents of *filename* are merged into the history list and sorted by timestamp. In either case, **histfile** is used if *filename* is not given and ```~/.history``` is used if **histfile** is unset. ```history -L``` is exactly like ```source -h``` except that it does not require a *filename*.<br><br>Note that **login shells** do the equivalent of ```history -L``` on startup and, if **savehist** is set, ```history -S``` before exiting. Because only ```~/.tcshrc``` is normally sourced before ```~/.history```, **histfile** should be set in ```~/.tcshrc``` rather than ```~/.login```.<br><br>If **histlit** is set, the first and second forms print and save the literal (unexpanded) form of the history list.<br><br>```history -c``` (+)<br>The last form clears the history list. |
| ```hup``` | ```hup [command]``` (+)<br>With *command*, runs *command* such that it will exit on a hangup signal and arranges for the shell to send it a hangup signal when the shell exits. Note that commands may set their own response to hangups, overriding **hup**. Without an argument, causes the non-interactive shell only to exit on a hangup for the remainder of the script. See also [Signal handling](#signal-handling) and the **nohup** builtin command. |
| ```nohup``` | ```nohup [command]```<br>With *command*, runs *command* such that it will ignore hangup signals. Note that commands may set their own response to hangups, overriding **nohup**. Without an argument, causes the non-interactive shell only to ignore hangups for the remainder of the script. See also [Signal handling](#signal-handling) and the **hup** builtin command. |
| ```inlib``` | ```inlib shared-library ...``` (+)<br>Adds each *shared-library* to the current environment. There is no way to remove a shared library. (Domain/OS only) |
| ```limit``` | ```limit [-h] [resource [maximum-use]]```<br>Limits the consumption by the current process and each process it creates to not individually exceed maximum-use on the specified resource. If no maximum-use is given, then the current limit is printed; if no resource is given, then all limitations are given. If the ```-h``` flag is given, the hard limits are used instead of the current limits. The hard limits impose a ceiling on the values of the current limits. Only the super-user may raise the hard limits, but a user may lower or raise the current limits within the legal range. |
| ```unlimit``` | ```unlimit [-hf] [resource]```<br>Removes the limitation on *resource* or, if no *resource* is specified, all resource limitations. With ```-h```, the corresponding hard limits are removed. Only the super-user may do this. Note that **unlimit** may not exit successful, since most systems do not allow descriptors to be unlimited. With ```-f``` errors are ignored. |
| ```log``` | ```log``` (+)<br>Prints the **watch** shell variable and reports on each user indicated in **watch** who is logged in, regardless of when they last logged in. See also **watchlog**. |
| ```watchlog``` | ```watchlog``` (+)<br>An alternate name for the **log** builtin command (q.v.). Available only if the shell was so compiled; see the **version** shell variable. |
| ```login``` | ```login```<br>Terminates a **login shell**, replacing it with an instance of **/bin/login**. This is one way to log off, included for compatibility with *sh*(1). |
| ```logout``` | ```logout```<br>Terminates a **login shell**. Especially useful if **ignoreeof** is set. |
| ```bye``` | ```bye``` (+)<br>A synonym for the **logout** builtin command. Available only if the shell was so compiled; see the **version** shell variable. |
| ```ls-F``` | ```ls-F [-switch ...] [file ...]``` (+)<br>Lists files like ```ls -F```, but much faster. It identifies each type of special file in the listing with a special character:<br>```/``` Directory<br>```*``` Executable<br>```#``` Block device<br>```%``` Character device<br>```|``` Named pipe (systems with named pipes only)<br>```=``` Socket (systems with sockets only)<br>```@``` Symbolic link (systems with symbolic links only)<br>```+``` Hidden directory (AIX only) or context dependent (HP/UX only)<br>```:``` Network special (HP/UX only)<br><br>If the **listlinks** shell variable is set, symbolic links are identified in more detail (on only systems that have them, of course):<br>```@``` Symbolic link to a non-directory<br>```>``` Symbolic link to a directory<br>```&``` Symbolic link to nowhere<br><br>**listlinks** also slows down ```ls-F``` and causes partitions holding files pointed to by symbolic links to be mounted.<br><br>If the **listflags** shell variable is set to ```x```, ```a``` or ```A```, or any combination thereof (e.g., ```xA```), they are used as flags to ```ls-F```, making it act like ```ls -xF```, ```ls -Fa```, ```ls -FA``` or a combination (e.g., ```ls -FxA```). On machines where ```ls -C``` is not the default, ```ls-F``` acts like ```ls -CF```, unless **listflags** contains an ```x```, in which case it acts like ```ls -xF```. ```ls-F``` passes its arguments to *ls*(1) if it is given any switches, so ```alias ls ls-F``` generally does the right thing.<br><br>The ```ls-F``` builtin can list files using different colors depending on the filetype or extension. See the **color** shell variable and the **LS_COLORS** environment variable. |
| ```migrate``` | ```migrate [-site] pid|%jobid ...``` (+)<br>The first form migrates the process or job to the site specified or the default site determined by the system path.<br><br>```migrate -site``` (+)<br>The second form is equivalent to ```migrate -site $$```: it migrates the current process to the specified site. Migrating the shell itself can cause unexpected behavior, because the shell does not like to lose its tty. (TCF only) |
| ```newgrp``` | ```newgrp [-] [group]``` (+)<br>Equivalent to ```exec newgrp```; see *newgrp*(1). Available only if the shell was so compiled; see the **version** shell variable. |
| ```nice``` | ```nice [+number] [command]```<br>Sets the scheduling priority for the shell to *number*, or, without number, to **4**. With *command*, runs *command* at the appropriate priority. The greater the *number*, the less cpu the process gets. The super-user may specify negative priority by using ```nice -number ...```. Command is always executed in a sub-shell, and the restrictions placed on commands in simple **if** statements apply. |
| ```onintr``` | ```onintr [-|label]```<br>Controls the action of the shell on interrupts.<br>Without arguments, restores the default action of the shell on interrupts, which is to terminate shell scripts or to return to the terminal command input level.<br>With ```-```, causes all interrupts to be ignored.<br>With *label*, causes the shell to execute a ```goto label``` when an interrupt is received or a child process terminates because it was interrupted. **onintr** is ignored if the shell is running detached and in system startup files (see [FILES](#files)), where interrupts are disabled anyway. |
| ```pushd``` | ```pushd [-p] [-l] [-n|-v] [name|+n]```<br>Without arguments, exchanges the top two elements of the directory stack. If **pushdtohome** is set, **pushd** without arguments does ```pushd ~```, like **cd**. (+)<br><br>With *name*, pushes the current working directory onto the directory stack and changes to *name*. If name is ```-``` it is interpreted as the previous working directory (see [Filename substitution](#filename-substitution)). (+) If **dunique** is set, **pushd** removes any instances of name from the stack before pushing it onto the stack. (+)<br><br>With a number ```+n```, rotates the *n*th element of the directory stack around to be the top element and changes to it. If **dextract** is set, however, ```pushd +n``` extracts the *n*th directory, pushes it onto the top of the stack and changes to it. (+)<br><br>Finally, all forms of **pushd** print the final directory stack, just like **dirs**. The **pushdsilent** shell variable can be set to prevent this and the ```-p``` flag can be given to override **pushdsilent**.<br><br>The ```-l```, ```-n``` and ```-v``` flags have the same effect on **pushd** as on **dirs**. (+) |
| ```popd``` | ```popd [-p] [-l] [-n|-v] [+n]```<br>Without arguments, pops the directory stack and returns to the new top directory.<br><br>With a number ```+n```, discards the *n*'th entry in the stack.<br><br>Finally, all forms of **popd** print the final directory stack, just like **dirs**. The **pushdsilent** shell variable can be set to prevent this and the ```-p``` flag can be given to override **pushdsilent**.<br><br>The ```-l```, ```-n``` and ```-v``` flags have the same effect on **popd** as on **dirs**. (+) |
| ```set``` | ```set```<br>The first form of the command prints the value of all shell variables. Variables which contain more than a single word print as a parenthesized word list.<br><br>```set name ...```<br>The second form sets name to the null string.<br><br>```set name=word ...```<br>The third form sets name to the single word.<br><br>```set [-r] [-f|-l] name=(wordlist) ...``` (+)<br>The fourth form sets name to the list of words in *wordlist*. In all cases the value is command and filename expanded. If ```-r``` is specified, the *value* is set read-only. If ```-f``` or ```-l``` are specified, set only unique words keeping their order. ```-f``` prefers the first occurrence of a word, and ```-l``` the last.<br><br>```set name[index]=word ...```<br>The fifth form sets the *index*'th component of *name* to *word*; this component must already exist.<br><br>```set -r``` (+)The sixth form lists only the names of all shell variables that are read-only.<br><br>```set -r name ...``` (+)<br>The seventh form makes *name* read-only, whether or not it has a value.<br><br>```set -r name=word ...``` (+)<br>The eighth form is the same as the third form, but make name read-only at the same time.<br><br>These arguments can be repeated to set and/or make read-only multiple variables in a single set command. Note, however, that variable expansion happens for all arguments before any setting occurs. Note also that ```=``` can be adjacent to both *name* and *word* or separated from both by whitespace, but cannot be adjacent to only one or the other. See also the **unset** builtin command. |
| ```unset``` | ```unset pattern```<br>Removes all variables whose names match *pattern*, unless they are read-only. ```unset *``` thus removes all variables unless they are read-only; this is a bad idea. It is not an error for nothing to be **unset**. |
| ```setenv``` | ```setenv [name [value]]```<br>Without arguments, prints the names and values of all environment variables. Given *name*, sets the environment variable *name* to *value* or, without *value*, to the null string. |
| ```unsetenv``` | ```unsetenv pattern```<br>Removes all environment variables whose names match *pattern*. ```unsetenv *``` thus removes all environment variables; this is a bad idea. It is not an error for nothing to be **unsetenv**ed. |
| ```printenv``` | ```printenv [name]``` (+)<br>Prints the names and values of all environment variables or, with *name*, the value of the environment variable *name*. |
| ```repeat``` | ```repeat count command```<br>The specified *command*, which is subject to the same restrictions as the *command* in the one line **if** statement above, is executed *count* times. I/O redirections occur exactly once, even if *count* is 0. |
| ```rootnode``` | ```rootnode //nodename``` (+)<br>Changes the rootnode to ```//nodename```, so that ```/``` will be interpreted as ```//nodename```. (Domain/OS only) |
| ```sched``` | ```sched``` (+)<br>The first form prints the scheduled-event list. The **sched** shell variable may be set to define the format in which the scheduled-event list is printed.<br><br>```sched [+]hh:mm command``` (+)<br>The second form adds command to the scheduled-event list.<br><br>```sched -n``` (+) |
| ```setpath``` | ```setpath path``` (+)<br>Equivalent to *setpath*(1). (Mach only) |
| ```setspath``` | ```setspath LOCAL|site|cpu ...``` (+)<br>Sets the system execution path. (TCF only) |
| ```setty``` | ```setty [-d|-q|-x] [-a] [[+|-]mode]``` (+)<br>Controls which tty modes (see [Terminal management](#terminal-management)) the shell does not allow to change. ```-d```, ```-q``` or ```-x``` tells **setty** to act on the ```edit```, ```quote``` or ```execute``` set of tty modes respectively; without ```-d```, ```-q``` or ```-x```, ```execute``` is used.<br><br>Without other arguments, **setty** lists the modes in the chosen set which are fixed on (```+mode```) or off (```-mode```). The available modes, and thus the display, vary from system to system.<br><br>With ```-a```, lists all tty modes in the chosen set whether or not they are fixed. With ```+mode```, ```-mode``` or ```mode```, fixes mode on or off or removes control from *mode* in the chosen set. For example, ```setty +echok echoe``` fixes ```echok``` mode on and allows commands to turn ```echoe``` mode on or off, both when the shell is executing commands. |
| ```setxvers``` | ```setxvers [string]``` (+)<br>Set the experimental version prefix to *string*, or removes it if *string* is omitted. (TCF only) |
| ```shift``` | ```shift [variable]```<br>Without arguments, discards **argv[1]** and shifts the members of **argv** to the left. It is an error for **argv** not to be set or to have less than one word as value. With *variable*, performs the same function on *variable*. |
| ```source``` | ```source [-h] name [args ...]```<br>The shell reads and executes commands from *name*. The commands are not placed on the history list. If any *args* are given, they are placed in **argv**. (+) **source** commands may be nested; if they are nested too deeply the shell may run out of file descriptors. An error in a **source** at any level terminates all nested **source** commands. With ```-h```, commands are placed on the history list instead of being executed, much like ```history -L```. |
| ```suspend``` | Causes the shell to stop in its tracks, much as if it had been sent a stop signal with ```^Z```. This is most often used to stop shells started by *su*(1). |
| ```termname``` | ```termname [terminal type]``` (+)<br>Tests if terminal type (or the current value of **TERM** if no terminal type is given) has an entry in the hosts *termcap*(5) or *terminfo*(5) database. Prints the terminal type to stdout and returns 0 if an entry is present otherwise returns 1. |
| ```time``` | ```time [command]```<br>Executes *command* (which must be a simple command, not an alias, a pipeline, a command list or a parenthesized command list) and prints a time summary as described under the **time** variable. If necessary, an extra shell is created to print the time statistic when the command completes. Without *command*, prints a time summary for the current shell and its children. |
| ```umask``` | ```umask [value]```<br>Sets the file creation mask to *value*, which is given in octal. Common values for the mask are 002, giving all access to the group and read and execute access to others, and 022, giving read and execute access to the group and others. Without *value*, prints the current file creation mask. |
| ```universe``` | ```universe universe``` (+)<br>Sets the universe to *universe*. (Masscomp/RTU only) |
| ```warp``` | ```warp universe``` (+)<br>Sets the universe to *universe*. (Convex/OS only) |
| ```ver``` | ```ver [systype [command]]``` (+)<br>Without arguments, prints **SYSTYPE**. With *systype*, sets **SYSTYPE** to *systype*. With *systype* and *command*, executes *command* under *systype*. *systype* may be ```bsd4.3``` or ```sys5.3```. (Domain/OS only) |
| ```where``` | ```where command``` (+)<br>Reports all known instances of *command*, including aliases, builtins and executables in **path**. |
| ```which``` | ```which command``` (+)<br>Displays the command that will be executed by the shell after substitutions, path searching, etc. The builtin command is just like *which*(1), but it correctly reports tcsh aliases and builtins and is 10 to 100 times faster. See also the *which-command* editor command. |

<p/>

### if

***Format #1:***

```if (expr) command```

If *expr* (an expression, as described under [Expressions](#expressions)) evaluates true, then *command* is executed. Variable substitution on *command* happens early, at the same time it does for the rest of the **if** command. *command* must be a simple command, not an alias, a pipeline, a command list or a parenthesized command list, but it may have arguments. Input/output redirection occurs even if *expr* is false and *command* is thus not executed; this is a bug.

***Format #2:***

```
if (expr) then
    ...
else if (expr2) then
    ...
else
    ...
endif
```

If the specified *expr* is true then the commands to the first *else* are executed; otherwise if *expr2* is true then the commands to the second *else* are executed, etc. Any number of *else-if* pairs are possible; only one *endif* is needed. The *else* part is likewise optional. (The words *else* and *endif* must appear at the beginning of input lines; the *if* must appear alone on its input line or after an *else*.)

### switch

***Format:***

```
switch (string)
case str1:
    ...
    breaksw

case str2:
    ...
    breaksw

...

default:
    ...
    breaksw

endsw
```

Each case label is successively matched, against the specified *string* which is first command and filename expanded. The file metacharacters ```*```, ```?``` and ```[...]``` may be used in the case labels, which are variable expanded. If none of the labels match before a ```default``` label is found, then the execution begins after the default label. **Each case label and the default label must appear at the beginning of a line**. The command **breaksw** causes execution to continue after the **endsw**. Otherwise control may fall through case labels and default labels as in C. If no label matches and there is no default, execution continues after the **endsw**.

### foreach

***Format:***

```
foreach name (wordlist)
    ...
    break
    ...
    continue
    ...
end
```

Successively sets the variable *name* to each member of *wordlist* and executes the sequence of commands between this command and the matching *end*. (Both **foreach** and **end** must appear alone on separate lines.) The builtin command **continue** may be used to continue the loop prematurely and the builtin command **break** to terminate it prematurely. When this command is read from the terminal, the loop is read once prompting with ```foreach? ``` (or **prompt2**) before any statements in the loop are executed. If you make a mistake typing in a loop at the terminal you can rub it out.

### while

***Format:***

```
while (expr)
    ...
    break
    ...
    continue
    ...
end
```

Executes the commands between the **while** and the matching **end** while *expr* (an expression, as described under [Expressions](#expressions)) evaluates non-zero. **while** and **end** must appear alone on their input lines. **break** and **continue** may be used to terminate or continue the loop prematurely. If the input is a terminal, the user is prompted the first time through the loop as with **foreach**. |

## Special aliases (+)

If set, each of these aliases executes automatically at the indicated time. They are all initially undefined.

| Special_aliases | Description |
| :-------------- | :---------- |
| ```beepcmd``` | Runs when the shell wants to ring the terminal bell. |
| ```cwdcmd``` | Runs after every change of working directory. For example, if the user is working on an X window system using *xterm*(1) and a re-parenting window manager that supports title bars such as *twm*(1) and does<br>```> alias cwdcmd 'echo -n "^[]2;${HOST}:$cwd ^G"'```<br>then the shell will change the title of the running *xterm*(1) to be the name of the host, a colon, and the full current working directory. A fancier way to do that is<br>```> alias cwdcmd 'echo -n "^[]2;${HOST}:$cwd^G^[]1;${HOST}^G"'```<br>This will put the hostname and working directory on the title bar but only the hostname in the icon manager menu.<br><br>Note that putting a **cd**, **pushd** or **popd** in **cwdcmd** may cause an infinite loop. It is the author's opinion that anyone doing so will get what they deserve. |
| ```jobcmd``` | Runs before each command gets executed, or when the command changes state. This is similar to **postcmd**, but it does not print builtins.<br>```> alias jobcmd 'echo -n "^[]2\;\!#:q^G"'```<br>then executing ```vi foo.c``` will put the command string in the xterm title bar. |
| ```postcmd``` | Runs before each command gets executed.<br>```> alias postcmd 'echo -n "^[]2\;\!#:q^G"'```<br>then executing ```vi foo.c``` will put the command string in the xterm title bar. |
| ```helpcommand``` | Invoked by the *run-help* editor command. The command name for which help is sought is passed as sole argument. For example, if one does<br>```> alias helpcommand '\!:1 --help'```<br>then the help display of the command itself will be invoked, using the GNU help calling convention. Currently there is no easy way to account for various calling conventions (e.g., the customary Unix ```-h```), except by using a table of many commands. |
| ```periodic``` | Runs every **tperiod** minutes. This provides a convenient means for checking on common but infrequent changes such as new mail. For example, if one does<br>```> set tperiod = 30```<br>```> alias periodic checknews```<br>then the *checknews*(1) program runs every 30 minutes. If **periodic** is set but **tperiod** is unset or set to 0, **periodic** behaves like **precmd**. |
| ```precmd``` | Runs just before each prompt is printed. For example, if one does<br>```> alias precmd date```<br>then *date*(1) runs just before the shell prompts for each command. There are no limits on what **precmd** can be set to do, but discretion should be used. |
| ```shell``` | Specifies the interpreter for executable scripts which do not themselves specify an interpreter. The first word should be a full path name to the desired interpreter (e.g., ```/bin/csh``` or ```/usr/local/bin/tcsh```). |

<p/>

## Special shell variables

# ENVIRONMENT

| Variables | Description |
| :-------- | :---------- |
| **AFSUSER** (+) | Equivalent to the **afsuser** shell variable. |
| **COLUMNS** | The number of columns in the terminal. See [Terminal management](). |
| **DISPLAY** | Used by X Window System. If set, the shell does not set **autologout** (q.v.). |
| **EDITOR** | The pathname to a default editor. Used by the ***run-fg-editor*** editor command if the the **editors** shell variable is unset. See also the **VISUAL** environment variable. |
| **GROUP** (+) | Equivalent to the **group** shell variable. |
| **HOME** | Equivalent to the **home** shell variable. |
| **HOST** (+) | Initialized to the name of the machine on which the shell is running, as determined by the *gethostname*(2) system call. |
| **HOSTTYPE** (+) | Initialized to the type of machine on which the shell is running, as determined at compile time. This variable is obsolete and will be removed in a future version. |
| **HPATH** (+) | A colon-separated list of directories in which the *run-help* editor command looks for command documentation. |
| **LANG** | Gives the preferred character environment. See [Native Language System support](). |
| **LC_CTYPE** | If set, only ctype character handling is changed. See [Native Language System support](). |
| **LINES** | The number of lines in the terminal. See [Terminal management](). |
| **LS_COLORS** | The format of this variable is reminiscent of the **termcap**(5) file format; a colon-separated list of expressions of the form ```xx=string```, where ```xx``` is a two-character variable name. |
| **MACHTYPE** (+) | The machine type (microprocessor class or machine model), as determined at compile time. |
| **NOREBIND** (+) | If set, printable characters are not rebound to *self-insert-command*. See [Native Language System support](). |
| **OSTYPE** (+) | The operating system, as determined at compile time. |
| **PATH** | A colon-separated list of directories in which to look for executables. Equivalent to the **path** shell variable, but in a different format. |
| **PWD** (+) | Equivalent to the **cwd** shell variable, but not synchronized to it; updated only after an actual directory change. |
| **REMOTEHOST** (+) | The host from which the user has logged in remotely, if this is the case and the shell is able to determine it. Set only if the shell was so compiled; see the **version** shell variable. |
| **SHLVL** (+) | Equivalent to the **shlvl** shell variable. |
| **SYSTYPE** (+) | The current system type. (Domain/OS only) |
| **TERM** | Equivalent to the **term** shell variable. |
| **TERMCAP** | The terminal capability string. See [Terminal management](). |
| **USER** | Equivalent to the **user** shell variable. |
| **VENDOR** (+) | The vendor, as determined at compile time. |
| **VISUAL** | The pathname to a default full-screen editor. Used by the *run-fg-editor* editor command if the the **editors** shell variable is unset. See also the **EDITOR** environment variable. |

<p/>

# FILES

| Files | Description |
| :---- | :---------- |
| ***/etc/csh.cshrc*** | Read first by every shell. ConvexOS, Stellix and Intel use ***/etc/cshrc*** and NeXTs use ***/etc/cshrc.std***. A/UX, AMIX, Cray and IRIX have no equivalent in **csh**, but read this file in **tcsh** anyway. Solaris 2.x does not have it either, but **tcsh** reads ***/etc/.cshrc***. (+) |
| ***/etc/csh.login*** | Read by login shells after ***/etc/csh.cshrc***. ConvexOS, Stellix and Intel use ***/etc/login***, NeXTs use ***/etc/login.std***, Solaris 2.x uses ***/etc/.login*** and A/UX, AMIX, Cray and IRIX use ***/etc/cshrc***. |
| ***~/.tcshrc*** (+) | Read by every shell after ***/etc/csh.cshrc*** or its equivalent. |
| ***~/.cshrc*** | Read by every shell, if ***~/.tcshrc*** doesn't exist, after ***/etc/csh.cshrc*** or its equivalent. This manual uses ***~/.tcshrc*** to mean ***~/.tcshrc or, if ***~/.tcshrc*** is not found, ***~/.cshrc***. |
| ***~/.history*** | Read by login shells after ***~/.tcshrc*** if ```savehist``` is set, but see also **histfile**. |
| ***~/.login*** | Read by login shells after ***~/.tcshrc*** or ***~/.history***. The shell may be compiled to read ***~/.login*** before instead of after ***~/.tcshrc*** and ***~/.history***; see the **version** shell variable. |
| ***~/.cshdirs*** (+) | Read by login shells after ***~/.login*** if ```savedirs``` is set, but see also **dirsfile**. |
| ***/etc/csh.logout*** | Read by login shells at logout. ConvexOS, Stellix and Intel use ***/etc/logout*** and NeXTs use ***/etc/logout.std***. A/UX, AMIX, Cray and IRIX have no equivalent in **csh**, but read this file in **tcsh** anyway. Solaris 2.x does not have it either, but **tcsh** reads ***/etc/.logout***. (+) |
| ***~/.logout*** | Read by login shells at logout after ***/etc/csh.logout*** or its equivalent. |
| ***/bin/sh*** | Used to interpret shell scripts not starting with a ```#```. |
| ***/tmp/sh\**** | Temporary file for ```<<```. |
| ***/etc/passwd*** | Source of home directories for ```~name``` substitutions. |

<p/>

The order in which startup files are read may differ if the shell was so compiled.

# NEW FEATURES (+)

# THE ***T*** IN TCSH

In 1964, DEC produced the **PDP-6**. The **PDP-10** was a later re-implementation. It was re-christened the DECsystem-10 in 1970 or so when DEC brought out the second model, the **KI10**.

**TENEX** was created at Bolt, Beranek & Newman (a Cambridge, Massachusetts think tank) in 1972 as an experiment in demand-paged virtual memory operating systems. They built a new pager for the DEC PDP-10 and created the OS to go with it. It was extremely successful in academia.

In 1975, DEC brought out a new model of the PDP-10, the **KL10**; they intended to have only a version of **TENEX**, which they had licensed from BBN, for the new box. They called their version **TOPS-20** (their capitalization is trademarked). A lot of **TOPS-10** users (The OPerating System for PDP-10) objected; thus DEC found themselves supporting two incompatible systems on the same hardware -- but then there were 6 on the PDP-11!

TENEX, and TOPS-20 to version 3, had command completion via a user-code-level subroutine library called ULTCMD. With version 3, DEC moved all that capability and more into the monitor ('kernel' for you Unix types), accessed by the COMND% JSYS ('Jump to SYStem' instruction, the supervisor call mechanism).

The creator of **tcsh** was impressed by this feature and several others of TENEX and TOPS-20, and created a version of **csh** which mimicked them.

# LIMITATIONS

The system limits argument lists to ARG_MAX characters.

The number of arguments to a command which involves filename expansion is limited to 1/6th the number of characters allowed in an argument list.

Command substitutions may substitute no more characters than are allowed in an argument list.

To detect looping, the shell restricts the number of alias substitutions on a single line to 20.

# References

* [Tcsh Manual](http://www.tcsh.org/tcsh.html/top.html)
* [Download Tcsh (US)](ftp://ftp.astron.com/pub/tcsh/)
* [Download Tcsh (Finland)](http://ftp.funet.fi/pub/mirrors/ftp.astron.com/pub/tcsh/)
