---
layout: post
title: "Linux: GNU Bash"
tag: Linux
toc: true
---

This article introduces the GNU Bash in detail. And the most of the content is from [Bash Reference Manual v4.3](https://www.gnu.org/software/bash/manual/). I try to understand all features of GNU Bash and add some examples in this article.

<!--more-->

# Introduction

## What is a shell?

At its base, a shell is simply a **macro processor** that executes commands. The term **macro processor** means functionality where text and symbols are expanded to create larger expressions.

A Unix shell is both a **command interpreter** and a **programming language**. As a command interpreter, the shell provides the user interface to the rich set of GNU utilities. The programming language features allow these utilities to be combined. Files containing commands can be created, and become commands themselves. These new commands have the same status as system commands in directories such as ```/bin```, allowing users or groups to establish custom environments to automate their common tasks.

Shells may be used **interactively** or **non-interactively**. In interactive mode, they accept input typed from the keyboard. When executing non-interactively, shells execute commands read from a file.

A shell allows execution of GNU commands, both **synchronously** and **asynchronously**. The shell waits for synchronous commands to complete before accepting more input; asynchronous commands continue to execute in parallel with the shell while it reads and executes additional commands. The *redirection* constructs permit fine-grained control of the input and output of those commands. Moreover, the shell allows control over the contents of commands' environments.

Shells also provide a small set of built-in commands (*builtins*) implementing functionality impossible or inconvenient to obtain via separate utilities. For example, **cd**, **break**, **continue**, and **exec** cannot be implemented outside of the shell because they directly manipulate the shell itself. The **history**, **getopts**, **kill**, or **pwd** builtins, among others, could be implemented in separate utilities, but they are more convenient to use as builtin commands. All of the shell builtins are described in subsequent sections.

While executing commands is essential, most of the power (and complexity) of shells is due to their embedded programming languages. Like any high-level language, the shell provides variables, flow control constructs, quoting, and functions.

Shells offer features geared specifically for **interactive use** rather than to augment the programming language. These interactive features include [job control](#job-control), [command line editing](#command-line-editing), [command history](#using-history-interactively) and [aliases](#aliases).

## What is Bash?

**Bash** is the shell, or command language interpreter, for the GNU operating system. The name is an acronym for the **B**ourne-**A**gain **SH**ell, a pun on *Stephen Bourne*, the author of the direct ancestor of the current Unix shell **sh**, which appeared in the Seventh Edition Bell Labs Research version of Unix.

Bash is largely compatible with **sh** and incorporates useful features from the Korn shell **ksh** and the C shell **csh**. It is intended to be a conformant implementation of the IEEE POSIX ***Shell and Tools portion*** of the IEEE POSIX specification (**IEEE Standard 1003.1**). It offers functional improvements over **sh** for both interactive and programming use.

While the GNU operating system provides other shells, including a version of **csh**, Bash is the default shell. Like other GNU software, Bash is quite portable. It currently runs on nearly every version of Unix and a few other operating systems - independently-supported ports exist for MS-DOS, OS/2, and Windows platforms.

## Bash Releases

Here is [GNU Bash official site](https://www.gnu.org/software/bash/), and here is [Bash Reference Manual](https://www.gnu.org/software/bash/manual/). The GNU Bash releases following versions:

| Bash Version | Release Date |
| :----------: | :----------: |
| 2.02.1       |  1998-07-24  |
| 2.03         |  1999-02-20  |
| 2.04b5       |  2000-02-24  |
| 2.04         |  2000-03-21  |
| 2.05         |  2001-04-09  |
| 2.05a        |  2001-11-16  |
| 2.05b        |  2002-07-18  |
| 3.0          |  2004-07-30  |
| 3.2          |  2007-11-13  |
| 4.0          |  2009-03-17  |
| 4.1          |  2010-01-29  |
| 4.2          |  2011-05-10  |
| **4.3**      | **2014-02-26** |

<p/>

## Bash Repository

The GNU Bash Git repository is located [here](http://savannah.gnu.org/git/?group=bash). Run the following command to get a copy of the GNU Bash source code from repository:

    $ git clone git://git.savannah.gnu.org/bash.git

or, browse sources repository online [here](http://git.savannah.gnu.org/cgit/bash.git).

# Definitions

## Metacharacter

A ***metacharacter*** is a character that, when unquoted, separates words. It is a ***blank*** or one of the following characters: ```|``` ```&``` ```;``` ```(``` ```)``` ```<``` ```>```

## Control Operator

A token that performs a control function. It is a ***newline*** or one of the following: ```||``` ```&&``` ```&``` ```;``` ```;;``` ```|``` ```|&``` ```(``` ```)```

# Basic Shell Features

## Shell Syntax

### Shell Operation

The following is a brief description of the shell's operation when it reads and executes a command. Basically, the shell does the following:

1. Reads its input from a **shell script**, from a **string** supplied as an argument to the ```-c``` invocation option, or from **the user's terminal**.
2. Breaks the input into **words** and **operators**, obeying the quoting rules described in [Quoting](#quoting). These tokens are separated by [metacharacters](#metacharacter). [Alias expansion](#aliases) is performed by this step.
3. Parses the tokens into [simple commands](#simple-commands) and [compound commands](#compound-commands).
4. Performs the various [shell expansions](#shell-expansions), breaking the expanded tokens into lists of [filenames](#filename-expansion), commands and arguments.
5. Performs any necessary [redirections](#redirections) and removes the redirection operators and their operands from the argument list.
6. [Executes the command](#executing-commands).
7. Optionally waits for the command to complete and collects its [exit status](#exit-status).

### Quoting

#### Escape Character

A non-quoted backslash (```\```) is the Bash escape character. It preserves the literal value of the next character that follows, with the exception of ***newline***. If a ```\newline``` pair appears, and the backslash itself is not quoted, the ```\newline``` is treated as a **line continuation**, that's, it is removed from the input stream and effectively ignored.

***Examples:***

```
chenwx@chenwx ~ $ echo abc\
> def
abcdef

chenwx@chenwx ~ $ echo abc\\
abc\
```

#### Single Quotes

Enclosing characters in single quotes (```'```) preserves the literal value of each character within the quotes. **A single quote may not occur between single quotes, even when preceded by a backslash**.

***Examples:***

```
chenwx@chenwx ~ $ echo 'abc123~`!@#$%^&*()_-+=|\<,>.?/'
abc123~`!@#$%^&*()_-+=|\<,>.?/
```

#### Double Quotes

Enclosing characters in double quotes (```"```) preserves the literal value of all characters within the quotes, with the exception of ```$```, ```` ` ````, ```\```, and, when history expansion is enabled, ```!```. **A double quote may be quoted within double quotes by preceding it with a backslash**.

| Chars | Description |
| :---: | :---------- |
| ```$```   | The character ```$``` retains its special meaning within double quotes, refer to the following sections in [Shell Expansions](#shell-expansions):<br>- [Parameter and variable expansion](#parameter-and-variable-expansion)<br>- [Arithmetic expansion](#arithmetic-expansion)<br>- [Command substitution](#command-substitution)<br>- [Filename expansion](#filename-expansion) |
| ``` ` ``` | The character ``` ` ``` retains its special meaning within double quotes, refer to the following sections in [Shell Expansions](#shell-expansions):<br>- [Command substitution](#command-substitution) |
| ```\```   | The backslash retains its special meaning only when followed by one of the following characters: ```$``` ``` ` ``` ```\``` ```"``` or ***newline***. Within double quotes, backslashes that are followed by one of these characters are removed. Backslashes preceding characters without a special meaning are left unmodified. |
| ```!```   | If enabled, **history expansion** will be performed unless an ```!``` appearing in double quotes is escaped using a backslash. The backslash preceding the ```!``` is not removed. |
| ```*```   | The character ```*``` has special meaning when in double quotes, refer to [Parameter and variable expansion](#parameter-and-variable-expansion). |
| ```@```   | The character ```@``` has special meaning when in double quotes, refer to [Parameter and variable expansion](#parameter-and-variable-expansion). |

<p/>

#### ANSI-C Quoting

***Format:***

```
$'string'
```

Words of the form ```$'string'``` are treated specially. The word expands to *string*, with backslash-escaped characters replaced as specified by the **ANSI C standard**. Backslash escape sequences, if present, are decoded as following table. The expanded result is ***single-quoted***, as if the dollar sign had not been present.

| Sequences | Description |
| :-------- | :---------- |
| ```\a```  | Alert (bell) |
| ```\b```  | Backspace |
| ```\e```<br>```\E``` | An escape character (**not ANSI C**). |
| ```\f```  | Form feed, which means advance downward to the next *page*. |
| ```\n```  | Newline |
| ```\r```  | Carriage return |
| ```\t```  | Horizontal tab |
| ```\v```  | Vertical tab |
| ```\\```  | Backslash |
| ```\'```  | Single quote |
| ```\"```  | Double quote |
| ```\nnn``` | The eight-bit character whose value is the octal value *nnn* (one to three digits). |
| ```\xHH``` | The eight-bit character whose value is the hexadecimal value *HH* (one or two hex digits). |
| ```\uHHHH``` | The Unicode (ISO/IEC 10646) character whose value is the hexadecimal value *HHHH* (one to four hex digits). |
| ```\UHHHHHHHH``` | The Unicode (ISO/IEC 10646) character whose value is the hexadecimal value *HHHHHHHH* (one to eight hex digits). |
| ```\cx``` | A control-x character. |

<p/>

***Examples:***

```
chenwx@chenwx ~ $ echo abc$'\a'def
abcdef
chenwx@chenwx ~ $ echo abc$'\b'def
abdef

chenwx@chenwx ~ $ echo abc$'\f'def
abc
   def

chenwx@chenwx ~ $ echo abc$'\n'def
abc
def
chenwx@chenwx ~ $ echo abc$'\r'def
def
chenwx@chenwx ~ $ echo abc$'\n'def$'\r'ghi
abc
ghi

chenwx@chenwx ~ $ echo abc$'\t'def
abc	def
chenwx@chenwx ~ $ echo abc$'\v'def
abc
   def
chenwx@chenwx ~ $ echo abc$'\v'def$'\v'hgi
abc
   def
      hgi

chenwx@chenwx ~ $ echo abc$'\\'def
abc\def

chenwx@chenwx ~ $ echo abc$'\60'def
abc0def
chenwx@chenwx ~ $ echo abc$'\71'def
abc9def
chenwx@chenwx ~ $ echo abc$'\101'def
abcAdef
chenwx@chenwx ~ $ echo abc$'\132'def
abcZdef

chenwx@chenwx ~ $ echo abc$'\x30'def
abc0def
chenwx@chenwx ~ $ echo abc$'\x39'def
abc9def
chenwx@chenwx ~ $ echo abc$'\x41'def
abcAdef
chenwx@chenwx ~ $ echo abc$'\x5A'def
abcZdef

chenwx@chenwx ~ $ echo abc$'\u30'def
abc0def
chenwx@chenwx ~ $ echo abc$'\u39'def
abc9def
chenwx@chenwx ~ $ echo abc$'\u41'def
abcAdef
chenwx@chenwx ~ $ echo abc$'\u5A'def
abcZdef

chenwx@chenwx ~ $ echo abc$'\cx'def
abc#def
```

#### Locale-Specific Translation

***Format:***

```
$"string"
```

A **double-quoted** *string* preceded by a dollar sign (```$```) will cause the *string* to be translated according to the current locale. If the current locale is **C** or **POSIX**, the dollar sign is ignored. If the *string* is translated and replaced, the replacement is ***double-quoted***.

Refer to [How to add localization support to your bash scripts](http://mywiki.wooledge.org/BashFAQ/098).

***Example:***

```
chenwx@chenwx ~ $ echo $"abcdef"
abcdef
```

### Comments

In a non-interactive shell, or an interactive shell in which the ```interactive_comments``` option to the **shopt** builtin is enabled (see [The *shopt* Builtin](#the-em-shopt-em-builtin)), a word beginning with ```#``` causes that word and all remaining characters on that line to be ignored. An interactive shell without the ```interactive_comments``` option enabled does not allow comments. The ```interactive_comments``` option is **on** by default in **interactive shells**.

***Examples:***

```
chenwx@chenwx ~ $ shopt -p interactive_comments
shopt -s interactive_comments
chenwx@chenwx ~ $ echo abc #print first three characters
abc
chenwx@chenwx ~ $ shopt -u interactive_comments
chenwx@chenwx ~ $ echo abc #print first three characters
abc #print first three characters
```

## Shell Commands

### Simple Commands

***Formats:***

```
command
command ;
command &
```

A simple command is just a sequence of words separated by *blanks*, terminated by one of the shell's [control operators](#control-operator). The first word generally specifies a command to be executed, with the rest of the words being that command's arguments.

### Pipelines

A **pipeline** is a sequence of **simple commands** separated by one of the control operators ```|``` or ```|&```. The output of each command in the pipeline is connected via a pipe to the input of the next command.

***Format #1:***

```
[time [-p]] [!] command1 [ | command2 ] ...
```

***Format #2:***

```
[time [-p]] [!] command1 [ |& command2 ] ...
[time [-p]] [!] command1 [ 2>&1 | command2 ] ...
```

If ```|&``` is used, *command1*'s standard error, in addition to its standard output, is connected to *command2*'s standard input through the pipe; it is shorthand for ```2>&1 |```.

If the reserved word ```!``` precedes the pipeline, the exit status is the logical negation of the [exit status](#exit-status).

### Lists of Commands

A **list** is a sequence of one or more **pipelines** separated by one of the operators ```&&``` ```||``` ```;``` ```&```, and optionally terminated by one of ```;``` ```&``` or a ***newline***. Of these list operators, ```&&``` and ```||``` have equal precedence, followed by ```;``` and ```&```, which have equal precedence. A sequence of one or more ***newlines*** may appear in a list to delimit commands, equivalent to a semicolon.

***Format #1:***

```
pipeline-command1 ; pipeline-command2
pipeline-command1 ; pipeline-command2 ;
pipeline-command1 ; pipeline-command2 &
```

***Format #2:***

```
pipeline-command1 & pipeline-command2
pipeline-command1 & pipeline-command2 ;
pipeline-command1 & pipeline-command2 &
```

***Format #3:***

```
pipeline-command1 && pipeline-command2
pipeline-command1 && pipeline-command2 ;
pipeline-command1 && pipeline-command2 &
```

***Format #4:***

```
pipeline-command1 || pipeline-command2
pipeline-command1 || pipeline-command2 ;
pipeline-command1 || pipeline-command2 &
```

***Format #5:***

```
pipeline-command1 && pipeline-command2 ; pipeline-command3 || pipeline-command4
pipeline-command1 && pipeline-command2 ; pipeline-command3 || pipeline-command4 &
```

Commands separated by a ```;``` are executed sequentially; the shell waits for each command to terminate in turn. The return status is the exit status of the last command executed.

If a command is terminated by the control operator ```&```, the shell executes the command asynchronously in a ***subshell***. This is known as executing the command in the ***background***. The shell does not wait for the command to finish, and the return status is **0** (true). When job control is not active (see [Job Control](#job-control)), the standard input for asynchronous commands, in the absence of any explicit redirections, is redirected from ```/dev/null```.

An **AND** list has the form ```command1 && command2```, the *command2* is executed if, and only if, *command1* returns an exit status of **zero**.

An **OR** list has the form ```command1 || command2```, the *command2* is executed if, and only if, *command1* returns a **non-zero** exit status.

The return status of **AND** and **OR** lists is the exit status of the last command executed in the list.

***Examples:***

```
chenwx@chenwx ~ $ echo abc ; echo def
abc
def
chenwx@chenwx ~ $ echo abc ; echo def ;
abc
def
chenwx@chenwx ~ $ echo abc ; echo def &
abc
[1] 4928
chenwx@chenwx ~ $ def

[1]+  Done                    echo def
chenwx@chenwx ~ $ echo abc & echo def  
[1] 4942
abc
def
chenwx@chenwx ~ $ echo abc & echo def ;
[2] 4943
def
[1]   Done                    echo abc
chenwx@chenwx ~ $ abc

[2]+  Done                    echo abc
chenwx@chenwx ~ $ echo abc & echo def &
[1] 4944
abc
[2] 4945
[1]-  Done                    echo abc
def
chenwx@chenwx ~ $
[2]+  Done                    echo def
chenwx@chenwx ~ $ echo abc && echo def  
abc
def
chenwx@chenwx ~ $ echo abc && echo def ;
abc
def
chenwx@chenwx ~ $ echo abc && echo def &
[1] 4956
chenwx@chenwx ~ $ abc
def

[1]+  Done                    echo abc && echo def
chenwx@chenwx ~ $ echo abc || echo def  
abc
chenwx@chenwx ~ $ echo abc || echo def ;
abc
chenwx@chenwx ~ $ echo abc || echo def &
[1] 4959
abc
chenwx@chenwx ~ $
[1]+  Done                    echo abc || echo def
```

### Compound Commands

Compound commands are the shell programming constructs. Each construct begins with a reserved word or control operator and is terminated by a corresponding reserved word or operator. Any redirections (see [Redirections](#redirections)) associated with a compound command apply to all commands within that compound command unless explicitly overridden.

In most cases a list of commands in a compound command's description may be separated from the rest of the command by one or more ***newlines***, and may be followed by a ***newline*** in place of a semicolon.

Bash provides **looping constructs**, **conditional commands**, and mechanisms to **group commands** and execute them as a unit.

#### Looping Constructs

Note that wherever a ```;``` appears in the description of a command's syntax, it may be replaced with one or more ***newlines***.

##### until

***Format #1:***

```
until test-commands; do consequent-commands; done
```

***Format #2:***

```
until test-commands
do
    consequent-commands
done
```

Execute *consequent-commands* as long as *test-commands* has an exit status which is **not zero**.

The return status is the exit status of the last command executed in *consequent-commands*, or **zero** if none was executed.

***Example:*** save the following code into *ex.sh*:

```
#!/bin/bash

cnt=5

until (( cnt == 0 ))
do
    echo ${cnt}
    let cnt--
done
```

Then, execute the shell script:

```
chenwx@chenwx ~/ex $ chmod u+x ex.sh
chenwx@chenwx ~/ex $ ./ex.sh
5
4
3
2
1
```

Or, execute the code in command line directly:

```
chenwx@chenwx ~/ex $ cnt=5
chenwx@chenwx ~/ex $ until (( cnt == 0 ))
> do
>     echo ${cnt}
>     let cnt--
> done
5
4
3
2
1
```

##### while

***Format #1:***

```
while test-commands; do consequent-commands; done
```

***Format #2:***

```
while test-commands
do
    consequent-commands
done
```

Execute *consequent-commands* as long as *test-commands* has an exit status of **zero**.

The return status is the exit status of the last command executed in *consequent-commands*, or **zero** if none was executed.

***Example:*** save the following code into *ex.sh*:

```
#!/bin/bash

cnt=5

while (( cnt <= 10 ))
do
    echo ${cnt}
    let cnt++
done
```

Then, execute the shell script:

```
chenwx@chenwx ~/ex $ chmod u+x ex.sh
chenwx@chenwx ~/ex $ ./ex.sh
5
6
7
8
9
10
```

Or, execute the code in command line directly:

```
chenwx@chenwx ~/ex $ cnt=5
chenwx@chenwx ~/ex $ while (( cnt <= 10 ))
> do
>     echo ${cnt}
>     let cnt++
> done
5
6
7
8
9
10
```

##### for

***Format #1:***

```
for name [ [in [words ...] ] ; ] do commands; done
```

***Format #2:***

```
for name [in [words ...] ]
do
    commands
done
```

Expand *words*, and execute *commands* once for each member in the resultant list, with *name* bound to the current member.

If ```in words``` is not present, the *for* command executes the *commands* once for each **positional parameter** that is set, as if ```in "$@"``` had been specified. Refer to [Special Parameters](#special-parameters).

The return status is the exit status of the last command that executes. If there are no items in the expansion of *words*, no commands are executed, and the return status is **zero**.

***Format #3:***

```
for (( expr1 ; expr2 ; expr3 )) ; do commands ; done
```

***Format #4:***

```
for (( expr1 ; expr2 ; expr3 ))
do
    commands
done
```

First, the arithmetic expression *expr1* is evaluated. The arithmetic expression *expr2* is then evaluated repeatedly until it evaluates to **zero**. Each time *expr2* evaluates to a **non-zero** value, *commands* are executed and the arithmetic expression *expr3* is evaluated. If any expression is omitted, it behaves as if it evaluates to **1**.

The return value is the exit status of the last command in commands that is executed, or **false** if any of the expressions is invalid.

***Example #1:*** save the following code into *ex.sh*:

```
#!/bin/bash

# print $0
echo '$0' is $0

# print $1 ~ $N
cnt=1
for i
do
    echo "\$${cnt} is $i"
    let cnt++
done
```

Then, execute the shell script:

```
chenwx@chenwx ~/ex $ chmod u+x ex.sh
chenwx@chenwx ~/ex $ ./ex.sh a b c
$0 is ./ex.sh
$1 is a
$2 is b
$3 is c
```

***Example #2:*** save the following code into *ex.sh*:

```
#!/bin/bash

# print $0
echo '$0' is $0

# print $1 ~ $N
cnt=1
for i
do
    echo "\$${cnt} is $i"
    let cnt++
done
```

Then, execute the shell script:

```
chenwx@chenwx ~/ex $ chmod u+x ex.sh
chenwx@chenwx ~/ex $ ./ex.sh a b c
$0 is ./ex.sh
$1 is a
$2 is b
$3 is c

chenwx@chenwx ~/ex $ . ./ex.sh a b c
$0 is bash
$1 is a
$2 is b
$3 is c
```

***Example #3:*** save the following code into *ex.sh*:

```
#!/bin/bash

# print $0
echo '$0' is $0

# print $1 ~ $N
cnt=1
for i in $@
do
    echo "\$${cnt} is $i"
    let cnt++
done
```

Then, execute the shell script:

```
chenwx@chenwx ~/ex $ chmod u+x ex.sh
chenwx@chenwx ~/ex $ ./ex.sh a b c
$0 is ./ex.sh
$1 is a
$2 is b
$3 is c

chenwx@chenwx ~/ex $ . ./ex.sh a b c
$0 is bash
$1 is a
$2 is b
$3 is c
```

***Example #4:*** save the following code into *ex.sh*:

```
#!/bin/bash

for (( cnt=5 ; cnt <= 10 ; cnt++ ))
do
    echo ${cnt}
done
```

then, execute the shell script:

```
chenwx@chenwx ~/ex $ chmod u+x ex.sh
chenwx@chenwx ~/ex $./ex.sh
5
6
7
8
9
10
```

##### break

Refer to [Bourne Shell Builtins](#bourne-shell-builtins) for details.

***Example:*** save the following code into *ex.sh*:

```
#!/bin/bash

for (( cnt=5 ; cnt <= 10 ; cnt++ ))
do
    echo ${cnt}

    if [ "${cnt}" == 8 ]; then
        break
    fi
done
```

Then, execute the shell script:

```
chenwx@chenwx ~/ex $ chmod u+x ex.sh
chenwx@chenwx ~/ex $ ./ex.sh
5
6
7
8
```

##### continue

Refer to [Bourne Shell Builtins](#bourne-shell-builtins) for details.

***Example:*** save the following code into *ex.sh*:

```
#!/bin/bash

for (( cnt=5 ; cnt <= 10 ; cnt++ ))
do
    echo "${cnt} before"

    if [ "${cnt}" == 8 ]; then
        continue
    fi

    echo "${cnt} after"
done
```

Then, execute the shell script:

```
chenwx@chenwx ~/ex $ chmod u+x ex.sh
chenwx@chenwx ~/ex $ ./ex.sh
5 before
5 after
6 before
6 after
7 before
7 after
8 before
9 before
9 after
10 before
10 after
```

#### Conditional Constructs

##### if

***Format:***

```
if test-commands; then
    consequent-commands;
[elif more-test-commands; then
    more-consequents;]
[else
    alternate-consequents;]
fi
```

The *test-commands* list is executed, and if its return status is **zero**, the *consequent-commands* list is executed. If *test-commands* returns a **non-zero** status, each *elif* list is executed in turn, and if its exit status is **zero**, the corresponding *more-consequents* is executed and the command completes. If *else alternate-consequents* is present, and the final command in the final *if* or *elif* clause has a **non-zero** exit status, then *alternate-consequents* is executed.

The return status is the exit status of the last command executed, or **zero** if no condition tested true.

***Example:*** save the following code into *ex.sh*:

```
#!/bin/bash

if [[ "$1" == 0 ]]; then
    echo "Enter if statement when \$1 is $1"
elif [[ "$1" == 1 ]]; then
    echo "Enter elif statement when \$1 is $1"
else
    echo "Enter else statement when \$1 is not 0 or 1"
fi
```

Then, execute the shell script:

```
chenwx@chenwx ~/ex $ ./ex.sh 0
Enter if statement when $1 is 0
chenwx@chenwx ~/ex $ ./ex.sh 1
Enter elif statement when $1 is 1
chenwx@chenwx ~/ex $ ./ex.sh 2
Enter else statement when $1 is not 0 or 1
```

##### case

***Format:***

```
case word in
    [ [(] pattern1 [| pattern2]... ) command-list ;; ]
    ...
    [ [(] pattern1 [| pattern2]... ) command-list ;& ]
    ...
    [ [(] pattern1 [| pattern2]... ) command-list ;;& ]
    ...
    [ [()] *) always-match-command-list ;; ]
esac
```

*case* will selectively execute the *command-list* corresponding to the first *pattern* that matches *word*. If the shell option ```nocasematch``` (see [The *shopt* Builtin](#the-em-shopt-em-builtin)) is enabled, the match is performed without regard to the case of alphabetic characters. The ```|``` is used to separate multiple patterns, and the ```)``` operator terminates a pattern list. A list of *patterns* and an associated *command-list* is known as a ***clause***.

Each ***clause*** must be terminated with ```;;``` ```;&``` ```;;&```. The *word* undergoes [tilde expansion](#tilde-expansion), [parameter expansion](#parameter-and-variable-expansion), [command substitution](#command-substitution), [arithmetic expansion](#arithmetic-expansion), and [quote removal](#quote-removal) before matching is attempted. Each *pattern* undergoes [tilde expansion](#tilde-expansion), [parameter expansion](#parameter-and-variable-expansion), [command substitution](#command-substitution), and [arithmetic expansion](#arithmetic-expansion).

There may be an arbitrary number of **case** clauses, each terminated by a ```;;``` ```;&``` or ```;;&```. The first *pattern* that matches determines the *command-list* that is executed. It's a common idiom to use ```*``` as the final pattern to define the default case, since that pattern will always match.

* If the ```;;``` operator is used, no subsequent matches are attempted after the first pattern match.
* Using ```;&``` in place of ```;;``` causes execution to continue with the *command-list* associated with the next clause, if any.
* Using ```;;&``` in place of ```;;``` causes the shell to test the patterns in the next clause, if any, and execute any associated *command-list* on a successful match.

The return status is **zero** if no pattern is matched. Otherwise, the return status is the exit status of the *command-list* executed.

***Example:*** save the following code to *ex.sh*:

```
#!/bin/sh

print ()
{
    echo Input $1;

    case $1 in
        a) echo "case a: ---match a---" ;;
        b) echo "case b: ---match b---" ;&
        c) echo "case c: ---match c---" ;;
        d) echo "case d: ---match d---" ;;&
        e) echo "case e: ---match e---" ;;
        f) echo "case f: ---match f---" ;;&
        *) echo "case *: ---match all---" ;;
    esac
}

print $1
```

Then, execute the shell script:

```
chenwx@chenwx ~/ex $ . ./ex.sh a
Input a
case a: ---match a---
chenwx@chenwx ~/ex $ . ./ex.sh b
Input b
case b: ---match b---
case c: ---match c---
chenwx@chenwx ~/ex $ . ./ex.sh c
Input c
case c: ---match c---
chenwx@chenwx ~/ex $ . ./ex.sh d
Input d
case d: ---match d---
case *: ---match all---
chenwx@chenwx ~/ex $ . ./ex.sh e
Input e
case e: ---match e---
chenwx@chenwx ~/ex $ . ./ex.sh f
Input f
case f: ---match f---
case *: ---match all---
chenwx@chenwx ~/ex $ . ./ex.sh x
Input x
case *: ---match all---
```

##### select

The **select** construct allows the easy generation of menus. It has almost the same syntax as the **for** command:

***Format #1:***

```
select name [in words ...]; do commands; done
```

***Format #2:***

```
select name [in words ...]
do
    commands
done
```

The list of **words** following **in** is expanded, generating a list of items. The set of expanded words is printed on the **standard error** output stream, each preceded by a number. If the ```in words``` is omitted, the [positional parameters](#positional-parameters) are printed, as if ```in "$@"``` had been specified, refer to [Special Parameters](#special-parameters). The **PS3** prompt is then displayed and a line is read from the **standard input**. If the line consists of a number corresponding to one of the displayed words, then the value of *name* is set to that word. If the line is empty, the words and prompt are displayed again. If **EOF** is read, the **select** command completes. Any other value read causes *name* to be set to null. The line read is saved in the variable **REPLY**.

The *commands* are executed after each selection until a **break** command is executed, at which point the **select** command completes.

***Example:*** save the following code to *ex.sh*:

```
#!/bin/bash

print ()
{
    select name in a b
    do
        if [ "$name" == "a" ]; then
            echo "\$REPLY is $REPLY, \$name is $name, let\'s try again!"
        fi
        if [ "$name" == "b" ]; then
            echo "\$REPLY is $REPLY, \$name is $name, break now!"
            break
        fi
    done
}

print
```

Then, execute the shell script:

```
chenwx@chenwx ~/Downloads/ex $ . ./ex.sh
1) a
2) b
#? 1
$REPLY is 1, $name is a, let\'s try again!
#? 2
$REPLY is 2, $name is b, break now!
```

##### (( expression ))

***Format:***

```
(( expression ))
```

The **arithmetic expression** *expression* is evaluated. If the value of the *expression* is **non-zero**, the return status is **0**; otherwise the return status is **1**. This is exactly equivalent to ```let "expression"``` for a full description of the ```let``` builtin, refer to [Bash Builtin Commands](#bash-builtin-commands).

***Example:***

```
chenwx@chenwx ~ $ echo $(( 3+4 ))
7

chenwx@chenwx ~ $ SUM1=$(( 3+4 ))
chenwx@chenwx ~ $ echo $SUM1
7

chenwx@chenwx ~ $ let SUM2="3+4"
chenwx@chenwx ~ $ echo $SUM2
7

chenwx@chenwx ~/blog $ if (( 1+1 )); then echo "if statement"; else echo "else statement"; fi
if statement

chenwx@chenwx ~/blog $ if (( 1-1 )); then echo "if statement"; else echo "else statement"; fi
else statement
```

##### [[ expression ]]

***Format:***

```
[[ expression ]]
```

Return a status of **0** or **1** depending on the evaluation of the **conditional expression** *expression*. Expressions are composed of the primaries described in [Bash Conditional Expressions](#bash-conditional-expressions).

**Word splitting** and **filename expansion** are not performed on the words between the ```[[``` and ```]]```; **tilde expansion**, **parameter and variable expansion**, **arithmetic expansion**, **command substitution**, **process substitution**, and **quote removal** are performed. Conditional operators such as ```-f``` must be unquoted to be recognized as primaries.

When used with ```[[```, the ```<``` and ```>``` operators sort lexicographically using the current locale.

When the ```==``` and ```!=``` operators are used, the string to the right of the operator is considered a pattern and matched according to the rules described in [Pattern Matching](#filename-expansion), as if the ```extglob``` shell option were enabled (see [The *shopt* Builtin](#the-em-shopt-em-builtin)). The ```=``` operator is identical to ```==```. If the shell option ```nocasematch``` is enabled (see [The *shopt* Builtin](#the-em-shopt-em-builtin)), the match is performed without regard to the case of alphabetic characters. The return value is **0** if the string matches (```==```) or does not match (```!=```)the pattern, and **1** otherwise. Any part of the pattern may be quoted to force the quoted portion to be matched as a string.

An additional binary operator, ```=~```, is available, with the same precedence as ```==``` and ```!=```. When it is used, the string to the right of the operator is considered an extended regular expression and matched accordingly (as in *regex*3)). The return value is **0** if the string matches the pattern, and **1** otherwise. If the regular expression is syntactically incorrect, the conditional expression's return value is **2**. If the shell option ```nocasematch``` is enabled (see [The *shopt* Builtin](#the-em-shopt-em-builtin)), the match is performed without regard to the case of alphabetic characters. Any part of the pattern may be quoted to force the quoted portion to be matched as a string. Bracket expressions in regular expressions must be treated carefully, since normal quoting characters lose their meanings between brackets. If the pattern is stored in a shell variable, quoting the variable expansion forces the entire pattern to be matched as a string. Substrings matched by parenthesized subexpressions within the regular expression are saved in the array variable **BASH_REMATCH**. The element of **BASH_REMATCH** with index 0 is the portion of the string matching the entire regular expression. The element of **BASH_REMATCH** with index n is the portion of the string matching the nth parenthesized subexpression.

For example, the following will match a line (stored in the shell variable line) if there is a sequence of characters in the value consisting of any number, including zero, of space characters, zero or one instances of ```a```, then a ```b```:

```
[[ $line =~ [[:space:]]*(a)?b ]]
```

That means values like ```aab``` and ``` aaaaaab``` will match, as will a line containing a ```b``` anywhere in its value.

Storing the regular expression in a shell variable is often a useful way to avoid problems with quoting characters that are special to the shell. It is sometimes difficult to specify a regular expression literally without using quotes, or to keep track of the quoting used by regular expressions while paying attention to the shell's quote removal. Using a shell variable to store the pattern decreases these
problems. For example, the following is equivalent to the above:

```
pattern='[[:space:]]*(a)?b'
[[ $line =~ $pattern ]]
```

If you want to match a character that's special to the regular expression grammar, it has to be quoted to remove its special meaning. This means that in the pattern ```xxx.txt```, the ```.``` matches any character in the string (its usual regular expression meaning), but in the pattern ```"xxx.txt"``` it can only match a literal ```.```. Shell programmers should take special care with backslashes, since backslashes are used both by the shell and regular expressions to remove the special meaning from the following character. The following two sets of commands are *not* equivalent:

```
pattern='\.'

[[ . =~ $pattern ]]
[[ . =~ \. ]]

[[ . =~ "$pattern" ]]
[[ . =~ '\.' ]]
```

The first two matches will succeed, but the second two will not, because in the second two the backslash will be part of the pattern to be matched. In the first two examples, the backslash removes the special meaning from ```.```, so the literal ```.``` matches. If the string in the first examples were anything other than ```.```, say ```a```, the pattern would not match, because the quoted ```.``` in the pattern loses its special meaning of matching any single character.

Expressions may be combined using the following operators, listed in **decreasing order of precedence**:

| Combined_Expressions | Description |
| :------------------- | :---------- |
| ```( expression )``` | Returns the value of *expression*. This may be used to override the normal precedence of operators. |
| ```! expression```   | True if *expression* is false. |
| ```expr1 && expr2``` | True if both *expr1* and *expr2* are true. |
| ```expr1 || expr2``` | True if either *expr1* or *expr2* is true. |

<p/>

The ```&&``` and ```||``` operators do not evaluate *expression2* if the value of *expression1* is sufficient to determine the return value of the entire conditional expression.

#### Grouping Commands

Bash provides two ways to group a list of commands to be executed as a unit. When commands are grouped, redirections may be applied to the entire command list. For example, the output of all the commands in the list may be redirected to a single stream.

##### ( list )

***Format:***

```
( list )
```

Placing a list of commands between parentheses causes a ***subshell*** environment to be created (see [Command Execution Environment](#command-execution-environment)), and each of the commands in *list* to be executed in that ***subshell***. Since the *list* is executed in a subshell, variable assignments do not remain in effect after the subshell completes.

##### { list; }

***Format:***

```
{ list; }
```

Placing a list of commands between curly braces causes the list to be executed in the ***current shell context***. **No subshell is created**. The semicolon (or *newline*) following list is required.

**[NOTE]**
In addition to the creation of a ***subshell***, there is a subtle difference between these two constructs due to historical reasons:

* The braces are **reserved words**, so they must be separated from the list by *blanks* or other shell [*metacharacters*](#metacharacter).
* The parentheses are **operators**, and are recognized as separate tokens by the shell even if they are not separated from the *list* by whitespace.

The exit status of both of these constructs is the exit status of *list*.

### Coprocesses

A **coprocess** is a shell command preceded by the **coproc** reserved word. **A coprocess is executed asynchronously in a subshell**, as if the command had been terminated with the ```&``` [control operator](#control-operator), with a two-way pipe established between the executing shell and the coprocess.

***Format:***

```
coproc [NAME] command [redirections]
```

This creates a coprocess named *NAME*. If *NAME* is not supplied, the default name is *COPROC*. *NAME* must not be supplied if *command* is a [simple command](#simple-commands); otherwise, it is interpreted as the first word of the simple command.

When the coprocess is executed, the shell creates an array variable (see [Arrays](#arrays)) named *NAME* in the context of the executing shell. The standard output of *command* is connected via a pipe to a file descriptor in the executing shell, and that file descriptor is assigned to **NAME[0]**. The standard input of *command* is connected via a pipe to a file descriptor in the executing shell, and that file descriptor is assigned to **NAME[1]**. This pipe is established before any redirections specified by the command (see [Redirections](#redirections)). The file descriptors can be utilized as arguments to shell commands and redirections using standard word expansions. The file descriptors are not available in subshells.

The process ID of the shell spawned to execute the coprocess is available as the value of the variable **NAME_PID**. The **wait** builtin command may be used to wait for the coprocess to terminate.

Since the coprocess is created as an asynchronous command, the **coproc** command always returns success. The return status of a coprocess is the exit status of *command*.

### GNU Parallel

There are ways to run commands in parallel that are not built into Bash. **GNU Parallel** is a tool to do just that.

GNU Parallel, as its name suggests, can be used to build and run commands in parallel. You may run the same command with different arguments, whether they are filenames, usernames, hostnames, or lines read from files. GNU Parallel provides shorthand references to many of the most common operations (input lines, various portions of the input line, different ways to specify the input source, and so on). Parallel can replace **xargs** or **feed** commands from its input sources to several different instances of Bash.

For a complete description, refer to the *GNU Parallel documentation*. A few examples should provide a brief introduction to its use.

For example, it is easy to replace **xargs** to gzip all html files in the current directory and its subdirectories:

```
find . -type f -name '*.html' -print | parallel gzip
```

If you need to protect special characters such as *newlines* in file names, use **find**'s ```-print0``` option and **parallel**'s ```-0``` option.

You can use Parallel to move files from the current directory when the number of files is too large to process with one **mv** invocation:

```
ls | parallel mv {} destdir
```

As you can see, the ```{}``` is replaced with each line read from standard input. While using **ls** will work in most instances, it is not sufficient to deal with all filenames. If you need to accommodate special characters in filenames, you can use:

```
find . -depth 1 \! -name '.*' -print0 | parallel -0 mv {} destdir
```

as alluded to above.

This will run as many **mv** commands as there are files in the current directory. You can emulate a parallel **xargs** by adding the ```-X``` option:

```
find . -depth 1 \! -name '.*' -print0 | parallel -0 -X mv {} destdir
```

GNU Parallel can replace certain common idioms that operate on lines read from a file (in this case, filenames listed one per line):

```
while IFS= read -r x; do
do-something1 "$x" "config-$x"
do-something2 < "$x"
done < file | process-output
```

with a more compact syntax reminiscent of lambdas:

```
cat list | parallel "do-something1 {} config-{} ; do-something2 < {}" | process-output
```

Parallel provides a built-in mechanism to remove filename extensions, which lends itself to batch file transformations or renaming:

```
ls *.gz | parallel -j+0 "zcat {} | bzip2 >{.}.bz2 && rm {}"
```

This will recompress all files in the current directory with names ending in .gz using bzip2, running one job per CPU (-j+0) in parallel. (We use **ls** for brevity here; using **find** as above is more robust in the face of filenames containing unexpected characters.) Parallel can take arguments from the command line; the above can also be written as

```
parallel "zcat {} | bzip2 >{.}.bz2 && rm {}" ::: *.gz
```

If a command generates output, you may want to preserve the input order in the output. For instance, the following command

```
{ echo foss.org.my ; echo debian.org; echo freenetproject.org; } | parallel traceroute
```

will display as output the traceroute invocation that finishes first. Adding the ```-k``` option

```
{ echo foss.org.my ; echo debian.org; echo freenetproject.org; } | parallel -k traceroute
```

will ensure that the output of **traceroute foss.org.my** is displayed first.

Finally, Parallel can be used to run a sequence of shell commands in parallel, similar to ```cat file | bash```. It is not uncommon to take a list of filenames, create a series of shell commands to operate on them, and feed that list of commnds to a shell. Parallel can speed this up. Assuming that **file** contains a list of shell commands, one per line,

```
parallel -j 10 < file
```

will evaluate the commands using the shell (since no explicit command is supplied as an argument), in blocks of ten shell jobs at a time.

## Shell Functions

Shell functions are a way to group commands for later execution using a single name for the group. They are executed just like a *regular* command. When the name of a shell function is used as a simple command name, the list of commands associated with that function name is executed. **Shell functions are executed in the current shell context; no new process is created to interpret them**.

Functions are declared using this syntax:

```
name () compound-command [ redirections ]

name ()
{
    compound-command
} [ redirections ]
```

or,

```
function name [()] compound-command [ redirections ]

function name [()]
{
    compound-command
} [ redirections ]
```

This defines a shell function named *name*. The reserved word **function** is optional. If the **function** reserved word is supplied, the parentheses are optional. The body of the function is the compound command *compound-command* (see [Compound Commands](#compound-commands)). That command is usually a *list* enclosed between ```{``` and ```}```, but may be any compound command listed above. *compound-command* is executed whenever *name* is specified as the name of a command. When the shell is in POSIX mode (see
[Bash POSIX Mode](#bash-posix-mode)), *name* may not be the same as one of the special builtins (see [Special Builtins](#special-builtins)). Any *redirections* (see [Redirections](#redirections)) associated with the shell function are performed when the function is executed.

A function definition may be deleted using the ```-f``` option to the **unset** builtin.

The exit status of a function definition is **zero** unless a syntax error occurs or a readonly function with the same name already exists. When executed, the exit status of a function is the exit status of the last command executed in the body.

Note that for historical reasons, in the most common usage the curly braces that surround the body of the function must be separated from the body by ***blanks*** or ***newlines***. This is because the braces are reserved words and are only recognized as such when they are separated from the command list by ***whitespace*** or another shell [***metacharacter***](#metacharacter). Also, when using the braces, the *list* must be terminated by a ***semicolon***, a ```&```, or a ***newline***.

Functions are invoked using this syntax:

```
func-name "param1" "param2" ...
```

When a function is executed, the arguments to the function become the **positional parameters** during its execution (see [Positional Parameters](#positional-parameters)). The special parameter ```#``` that expands to the number of **positional parameters** is updated to reflect the change. Special parameter **0** is unchanged. The first element of the **FUNCNAME** variable is set to the name of the function while the function is executing.

All other aspects of the shell execution environment are identical between a function and its caller with these exceptions: the **DEBUG** and **RETURN** traps are not inherited unless the function has been given the **trace** attribute using the **declare** builtin or the ```-o functrace``` option has been enabled with the **set** builtin, (in which case all functions inherit the **DEBUG** and **RETURN** traps), and the **ERR** trap is not inherited unless the ```-o errtrace``` shell option has been enabled. See [Bourne Shell Builtins](#bourne-shell-builtins), for the description of the **trap** builtin.

The **FUNCNEST** variable, if set to a numeric value greater than **0**, defines a maximum function nesting level. Function invocations that exceed the limit cause the entire command to abort.

If the builtin command **return** is executed in a function, the function completes and execution resumes with the next command after the function call. Any command associated with the **RETURN** trap is executed before execution resumes. When a function completes, the values of the positional parameters and the special parameter ```#``` are restored to the values they had prior to the function's execution. If a numeric argument is given to **return**, that is the function's return status; otherwise the function's return status is the exit status of the last command executed before the **return**.

Variables local to the function may be declared with the **local** builtin. These variables are visible only to the function and the commands it invokes.

Function names and definitions may be listed with the ```-f``` option to the **declare** (**typeset**) builtin command (see [Bash Builtins](#bash-builtins)). The ```-F``` option to **declare** or **typeset** will list the function names only (and optionally the source file and line number, if the ```extdebug``` shell option is enabled). Functions may be exported so that subshells automatically have them defined with the ```-f``` option to the **export** builtin (see [Bourne Shell Builtins](#bourne-shell-builtins)). Note that shell functions and variables with the same name may result in multiple identically-named entries in the environment passed to the shell's children. Care should be taken in cases where this may cause a problem.

Functions may be recursive. The **FUNCNEST** variable may be used to limit the depth of the function call stack and restrict the number of function invocations. By default, no limit is placed on the number of recursive calls.

***Examples:*** save the following code into *ex.sh*:

```
#! /bin/bash

###################################
# Part 1: Definition of functions
###################################

func1 ()
{
    echo -e "Executing function $FUNCNAME with $# positional parameters...\n"

    local cnt=${1}
    until (( cnt == 0 ))
    do
        echo ${cnt}
        let cnt--
    done
}

function func2 ()
{
    echo -e "Executing function $FUNCNAME with $# positional parameters...\n"

    local cnt=${1}
    while (( cnt <= 10 ))
    do
        echo ${cnt}
        let cnt++
    done
} > ~/Downloads/ex/output.txt

###################################
# Part 2: Execution of functions
###################################

echo -e "== 1 == Call function func1() with 1 input parameter\n"
func1 5

echo -e "\n== 2 == Call function func2() with 1 input parameter\n"
func2 5
echo -e "Content of ~/Downloads/ex/output.txt:\n"
cat ~/Downloads/ex/output.txt

echo -e "\n== 3 == Local variable cnt in function func1() and func2() has value: >>${cnt}<<\n"

echo -e "== 4 == Unset function func1():\n"
unset func1

echo -e "== 5 == Call function func1() again after it's deleted\n"
func1 5
```

Then, execute the shell script *ex.sh*:

```
chenwx@chenwx ~/Downloads/ex $ chmod +x ./ex.sh
chenwx@chenwx ~/Downloads/ex $ ./ex.sh
== 1 == Call function func1() with 1 input parameter

Executing function func1 with 1 positional parameters...

5
4
3
2
1

== 2 == Call function func2() with 1 input parameter

Content of ~/Downloads/ex/output.txt:

Executing function func2 with 1 positional parameters...

5
6
7
8
9
10

== 3 == Local variable cnt in function func1() and func2() has value: >><<

== 4 == Unset function func1():

== 5 == Call function func1() again after it's deleted

./ex.sh: line 42: func1: command not found
```

## Shell Parameters

### Positional Parameters

A **positional parameter** is a parameter denoted by **one or more digits**, other than the single digit **0**. Positional parameters are assigned from the shell's arguments when it is invoked, and may be reassigned using the **set** builtin command.

Positional parameter ***N*** may be referenced as ```${N}```, or as ```$N``` when ***N*** consists of a single digit. When a positional parameter consisting of more than a single digit is expanded, it must be enclosed in braces, that's ```${N}```.

Positional parameters may not be assigned to with assignment statements. The **set** and **shift** builtins are used to set and unset them, see [Shell Builtin Commands](#shell-builtin-commands). The positional parameters are temporarily replaced when a shell function is executed, see [Shell Functions](#shell-functions).

### Special Parameters

The shell treats several parameters specially. These parameters may only be referenced; assignment to them is not allowed.

|  Chars  | References | Description |
| :-----: | :--------: | :---------- |
| ```*``` | ```$*```   | Expands to the **positional parameters**, starting from one.<br><br>When the expansion is not within double quotes, each positional parameter expands to a separate word. In contexts where it is performed, those words are subject to further **word splitting** and **pathname expansion**.<br><br>When the expansion occurs within double quotes, it expands to a single word with the value of each parameter separated by the first character of the **IFS** special variable. That is, ```$*``` is equivalent to ```$1c$2c...```, where *c* is the first character of the value of the **IFS** variable. If **IFS** is unset, the parameters are separated by spaces. If **IFS** is null, the parameters are joined without intervening separators. |
| ```@``` | ```$@```   | Expands to the **positional parameters**, starting from one.<br><br>When the expansion occurs within double quotes, each parameter expands to a separate word. That is, ```"$@"``` is equivalent to ```"$1" "$2" ...```.<br><br>If the double-quoted expansion occurs within a word, the expansion of the first parameter is joined with the beginning part of the original word, and the expansion of the last parameter is joined with the last part of the original word.<br><br>When there are no **positional parameters**, ```"$@"``` and ```$@``` expand to nothing (i.e., they are removed). |
| ```#``` | ```$#```   | Expands to the number of **positional parameters** in decimal.  |
| ```?``` | ```$?```   | Expands to the exit status of the most recently executed foreground pipeline. |
| ```-``` | ```$-```   | Expands to the current option flags as specified upon invocation, by the **set** builtin command, or those set by the shell itself (such as the ```-i``` option). |
| ```$``` | ```$$```   | ```$$``` expands to the process ID of the shell. In a ```()``` subshell, it expands to the process ID of the invoking shell, not the subshell. |
| ```!``` | ```$!```   | Expands to the process ID of the job most recently placed into the background, whether executed as an asynchronous command or using the ```bg``` builtin. |
| ```0``` | ```$0```   | Expands to the name of the shell or shell script. This is set at shell initialization.<br><br>If Bash is invoked with a file of commands, ```$0``` is set to the name of that file.<br><br>If Bash is started with the ```-c``` option (see [Invoking Bash](#invoking-bash)), then ```$0``` is set to the first argument after the string to be executed, if one is present. Otherwise, it is set to the filename used to invoke Bash, as given by argument zero. |
| ```_``` | ```$_```   | At shell startup, set to the absolute pathname used to invoke the shell or shell script being executed as passed in the environment or argument list. Subsequently, expands to the last argument to the previous command, after expansion. Also set to the full pathname used to invoke each command executed and placed in the environment exported to that command. When checking mail, this parameter holds the name of the mail file. |

<p/>

## Shell Expansions

Expansion is performed on the command line after it has been split into tokens, refer to *step 4* in [Shell Operation](#shell-operation). There are several kinds of expansion performed:

1. **Brace expansion**
2. **Tilde expansion**
3. **Parameter and variable expansion**
4. **Arithmetic expansion**
5. **Command substitution**
6. ***Process substitution*** (on systems that support *named pipes (FIFOs)* or the */dev/fd* method of naming open files)
7. **Word splitting**
8. **Filename expansion**

On systems that can support it, there is an additional expansion available: ***process substitution***. This is performed at the same time as tilde, parameter, variable, and arithmetic expansion and command substitution.

The order of expansions is:

| Priority | Expansions | Description |
| :------: | :--------- | :---------- |
|    1     | **Brace expansion** | Highest priority |
|    2     | **Tilde expansion**, **Parameter and variable expansion**, **Arithmetic expansion**, **Command substitution**, ***Process substitution*** (if supported by system) | They have the same priority and done in a *left-to-right* fashion. |
|    3     | **Word splitting** | |
|    4     | **Filename expansion** | Lowest priority |

<p/>

Only **brace expansion**, **word splitting**, and **filename expansion** can change the number of words of the expansion; other expansions expand a single word to a single word. The only exceptions to this are the expansions of ```$@``` (see [Special Parameters](#special-parameters)) and ```${name[@]}``` (see [Arrays](#arrays)).

After all expansions, **quote removal** (see [Quote Removal](#quote-removal)) is performed.

### Brace expansion

Brace expansion is a mechanism by which arbitrary strings may be generated. This mechanism is similar to **filename expansion** (see [Filename Expansion](#filename-expansion)), but the filenames generated need not exist.

***Format #1:***

```
[preamble]{str1,[str2,[str3,...]]}[postscript]
```

Patterns to be brace expanded take the form of an optional *preamble*, followed by either a series of comma-separated strings or a sequence expression between a pair of braces, followed by an optional *postscript*. The *preamble* is prefixed to each string contained within the braces, and the *postscript* is then appended to each resulting string, expanding left to right.

***Examples:***

| Brace_pattern | Expansions | Note |
| :------------ | :--------- | :--- |
| ```a{b,c,d}e``` | abe ace ade | Brace expansions may be nested. The results of each expanded string are not sorted; left to right order is preserved. |
| ```a{b,c,{e,f}}g``` | abg acg aeg afg | Brace expansions may be nested. |

<p/>

***Format #2:***

```
{x..y[..incr]}
```

where *x* and *y* are either integers or single characters, and *incr*, an optional increment, is an integer.

* When integers are supplied, the expression expands to each number between *x* and *y*, inclusive. Supplied integers may be prefixed with ```0``` to force each term to have the same width. When either *x* or *y* begins with a **zero**, the shell attempts to force all generated terms to contain the same number of digits, zero-padding where necessary.

* When characters are supplied, the expression expands to each character lexicographically between *x* and *y*, inclusive, using the default **C** locale. Note that both **x** and **y** must be of the same type.

* When the increment is supplied, it is used as the difference between each term. The default increment is **1** or **-1** as appropriate.

***Examples:***

| Brace_pattern | Expansions | Note |
| :------------ | :--------- | :--- |
| ```echo {a..e}```  | a b c d e | *x* and *y* are single characters. The default increment is 1 or -1 as appropriate. |
| ```echo {a..e..2}``` | a c e | *x* and *y* are single characters. |
| ```echo {e..a..2}``` | e c a | *x* and *y* are single characters. |
| ```echo {e..a..-2}``` | e c a | *x* and *y* are single characters. |
| ```echo {1..5}```  | 1 2 3 4 5 | *x* and *y* are integers. The default increment is 1 or -1 as appropriate. |
| ```echo {5..1}```  | 5 4 3 2 1 | *x* and *y* are integers. The default increment is 1 or -1 as appropriate. |
| ```echo {1..5..2}``` | 1 3 5 | *x* and *y* are integers |
| ```echo {5..1..2}``` | 5 3 1 | *x* and *y* are integers |
| ```echo {5..1..-2}``` | 5 3 1 | *x* and *y* are integers |
| ```echo {01..5..2}``` | 01 03 05 | Prefixed with **0** to force each term to have the same width. |
| ```echo {01..10..2}``` | 01 03 05 07 09 | Prefixed with **0** to force each term to have the same width. |

<p/>

Brace expansion is performed before any other expansions, and any characters special to other expansions are preserved in the result. It is strictly textual. Bash does not apply any syntactic interpretation to the context of the expansion or the text between the braces. To avoid conflicts with **parameter expansion**, the string ```${``` is not considered eligible for brace expansion.

A correctly-formed brace expansion must contain unquoted opening and closing braces, and at least one unquoted comma or a valid sequence expression. Any incorrectly formed brace expansion is left unchanged.

A ```{``` or ```,``` may be quoted with a backslash to prevent its being considered part of a brace expression.

This construct is typically used as shorthand when the common prefix of the strings to be generated is longer than in the above example:

```
mkdir /usr/local/src/bash/{old,new,dist,bugs}
```

or,

```
chown root /usr/{ucb/{ex,edit},lib/{ex?.?*,how_ex}}
```

### Tilde expansion

If a word begins with an unquoted tilde character ```~```, all of the characters up to the first unquoted slash (or all characters, if there is no unquoted slash) are considered a *tilde-prefix*:

* If none of the characters in the *tilde-prefix* are quoted, the characters in the *tilde-prefix* following the tilde are treated as a possible login name.

* If this login name is the null string, the tilde is replaced with the value of the **HOME** shell variable. If **HOME** is unset, the home directory of the user executing the shell is substituted instead.

* Otherwise, the *tilde-prefix* is replaced with the home directory associated with the specified login name.

* If the *tilde-prefix* is ```~+```, the value of the shell variable **PWD** replaces the *tilde-prefix*.

* If the *tilde-prefix* is ```~-```, the value of the shell variable **OLDPWD**, if it is set, is substituted.

* If the characters following the tilde in the *tilde-prefix* consist of a number *N*, optionally prefixed by a ```+``` or a ```-```, the *tilde-prefix* is replaced with the corresponding element from the directory stack, as it would be displayed by the **dirs** builtin invoked with the characters following tilde in the *tilde-prefix* as an argument (see [The Directory Stack](#the-directory-stack)). If the *tilde-prefix*, sans the tilde, consists of a number without a leading ```+``` or ```-```, ```+``` is assumed.

If the login name is invalid, or the tilde expansion fails, the word is left unchanged.

Each variable assignment is checked for unquoted *tilde-prefixes* immediately following a ```:``` or the first ```=```. In these cases, tilde expansion is also performed. Consequently, one may use filenames with tildes in assignments to **PATH**, **MAILPATH**, and **CDPATH**, and the shell assigns the expanded value.

The following table shows how Bash treats unquoted *tilde-prefixes*:

| Tilde_prefixes | Expansions |
| :------------- | :--------- |
| ```~```        | The value of **$HOME** |
| ```~/foo```    | **$HOME**/foo |
| ```~fred/foo``` | The subdirectory *foo* of the home directory of the user ***fred*** |
| ```~+/foo```   | **$PWD**/foo |
| ```~-/foo```   | ```${OLDPWD-'~-'}/foo``` |
| ```~N```       | The string that would be displayed by ```dirs +N```. |
| ```~+N```      | The string that would be displayed by ```dirs +N``` |
| ```~-N```      | The string that would be displayed by ```dirs -N``` |

<p/>

### Parameter and variable expansion

The ```$``` character introduces **parameter expansion**, **command substitution**, or **arithmetic expansion**. The parameter name or symbol to be expanded may be enclosed in braces, which are optional but serve to protect the variable to be expanded from characters immediately following it which could be interpreted as part of the name.

When braces are used, the matching ending brace is the first ```}``` not escaped by a backslash or within a quoted string, and not within an embedded **arithmetic expansion**, **command substitution**, or **parameter expansion**.

#### Format #1

```
${parameter}
```

The value of *parameter* is substituted. The *parameter* is a shell parameter as described in [Shell Parameters](#shell-parameters) or an array reference (see [Arrays](#arrays)). The braces are required when *parameter* is a **positional parameter** with more than one digit, or when *parameter* is followed by a character that is not to be interpreted as part of its name.

If the first character of *parameter* is an exclamation point (!), it introduces a level of variable indirection. Bash uses the value of the variable formed from the rest of *parameter* as the name of the variable; this variable is then expanded and that value is used in the rest of the substitution, rather than the value of *parameter* itself. This is known as **indirect expansion**. The exceptions to this are the expansions of ```${!prefix*}``` and ```${!name[@]}``` described below. The exclamation point must immediately follow the left brace in order to introduce indirection.

In each of the cases below, *word* is subject to **tilde expansion**, **parameter expansion**, **command substitution**, and **arithmetic expansion**.

When not performing substring expansion, using the form described below (e.g., ```:-```), Bash tests for a parameter that is unset or null. Omitting the colon results in a test only for a parameter that is unset. Put another way, if the colon is included, the operator tests for both parameter's existence and that its value is not null; if the colon is omitted, the operator tests only for existence.

***Examples:***

```
$ p1=10
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${p1}``` | 10 | |

<p/>

#### Format #2

```
${parameter:-word}
```

If *parameter* is unset or null, the expansion of *word* is substituted. Otherwise, the value of *parameter* is substituted.

***Examples:***

```
$ unset p1
$ p2=20
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${p1:-20}``` | 20 | The parameter *p1* is not assigned. |
| ```echo ${p1:-p2}``` | p2 | The parameter *p2* is not expanded. |
| ```echo ${p1:-${p2}}``` | 20 | The parameter *p2* is expanded. |
| ```echo ${p1}``` | *None is printed!* | The parameter *p1* is not assigned. |

<p/>

***Examples:***

```
$ p1=10
$ p2=20
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${p1:-20}``` | 10 |  |
| ```echo ${p1:-p2}``` | 10 |  |
| ```echo ${p1:-${p2}}``` | 10 |  |

<p/>

#### Format #3

```
${parameter:=word}
```

If *parameter* is unset or null, the expansion of *word* is assigned to *parameter*. The value of *parameter* is then substituted. [Positional parameters](#positional-parameters) and [special parameters](#special-parameters) may not be assigned to in this way.

***Examples:***

```
$ unset p1
$ p2=20
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${p1:=20}``` | 20 |  |
| ```echo ${p1}``` | 20 |  |

<p/>

***Examples:***

```
$ unset p1
$ p2=20
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${p1:=p2}``` | p2 | The parameter *p2* is not expanded. |
| ```echo ${p1}``` | p2 | The parameter *p1* is assigned. |

<p/>

***Examples:***

```
$ unset p1
$ p2=20
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${p1:=${p2}}``` | 20 | The parameter *p2* is expanded. |
| ```echo ${p1}``` | 20 | The parameter *p1* is assigned. |

<p/>

#### Format #4

```
${parameter:?word}
```

If *parameter* is null or unset, the expansion of *word* is written to the standard error and the shell, if it is not interactive, exits. Otherwise, the value of *parameter* is substituted.

***Examples:***

```
$ unset p1
$ p2=20
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${p1:?p2}``` | ```bash: p1: p2``` | The parameter *p2* is not expanded. |
| ```echo ${p1}``` | *None is printed!* | The parameter *p1* is not assigned. |

<p/>

***Examples:***

```
$ unset p1
$ p2=20
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${p1:?${p2}}``` | 20 | The parameter *p2* is expanded. |
| ```echo ${p1}``` | *None is printed!* | The parameter *p1* is not assigned. |

<p/>

***Examples:***

```
$ p1=10
$ p2=20
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${p1:?p2}``` | 10 |  |
| ```echo ${p1:?${p2}}``` | 10 |  |

<p/>

#### Format #5

```
${parameter:+word}
```

If *parameter* is null or unset, nothing is substituted. Otherwise, the expansion of *word* is substituted.

***Examples:***

```
$ unset p1
$ p2=20
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${p1:+p2}``` | *None is printed!* |  |
| ```echo ${p1}``` | *None is printed!* |  |

<p/>

***Examples:***

```
$ p1=10
$ p2=20
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${p1:+p2}``` | p2 | The parameter *p2* is not expanded. |
| ```echo ${p1}``` | 10 |  |

<p/>

***Examples:***

```
$ p1=10
$ p2=20
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${p1:+${p2}}``` | 20 | The parameter *p2* is expanded. |
| ```echo ${p1}``` | 10 |  |

<p/>

#### Format #6

```
${parameter:offset}
${parameter:offset:length}
```

This is referred to as **Substring Expansion**. It expands to up to *length* characters of the value of *parameter* starting at the character specified by *offset*. If *length* is omitted, it expands to the substring of the value of *parameter* starting at the character specified by *offset* and extending to the end of the value. *length* and *offset* are arithmetic expressions.

If *offset* evaluates to a number **less than zero**, the value is used as an *offset* in characters from the end of the value of *parameter*. If *length* evaluates to a number **less than zero**, it is interpreted as an *offset* in characters from the end of the value of *parameter* rather than a number of characters, and the expansion is the characters between *offset* and that result. Note that a negative *offset* must be separated from the colon by at least one space to avoid being confused with the ```:-``` expansion.

***Examples:***

```
$ string=01234567890abcdefgh
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${string:7}``` | 7890abcdefgh | |
| ```echo ${string:7:2}``` | 78 | |
| ```echo ${string:7:-2}``` | 7890abcdef | |
| ```echo ${string: -7}``` | bcdefgh | |
| ```echo ${string: -7:2}``` | bc | |
| ```echo ${string: -7:-2}``` | bcdef | |

<p/>

***Examples:***

```
$ set -- 01234567890abcdefgh
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${1:7}``` | 7890abcdefgh | |
| ```echo ${1:7:2}``` | 78 | |
| ```echo ${1:7:-2}``` | 7890abcdef | |
| ```echo ${1: -7}``` | bcdefgh | |
| ```echo ${1: -7:2}``` | bc | |
| ```echo ${1: -7:-2}``` | bcdef | |

<p/>

If *parameter* is ```@```, the result is length **positional parameters** beginning at *offset*. A negative *offset* is taken relative to one greater than the greatest positional parameter, so an offset of **-1** evaluates to the last positional parameter. It is an expansion error if *length* evaluates to a number less than zero.

***Examples:***

```
$ set -- 1 2 3 4 5 6 7 8 9 0 a b c d e f g h
```

| Formats | Expansions |
| :-------| :--------- |
| ```echo ${@:7}``` | 7 8 9 0 a b c d e f g h |
| ```echo ${@:7:2}``` | 7 8 |
| ```echo ${@:7:-2}``` | bash: -2: substring expression < 0 |
| ```echo ${@: -1}``` | h<br><br>A negative *offset* is taken relative to one greater than the greatest positional<br>parameter, so an offset of *-1* evaluates to the last [positional parameter](#positional-parameters). |
| ```echo ${@: -7}``` | b c d e f g h |
| ```echo ${@: -7:2}``` | b c |
| ```echo ${@:0}``` | bash 1 2 3 4 5 6 7 8 9 0 a b c d e f g h |
| ```echo ${@:0:2}``` | bash 1 |

<p/>

If *parameter* is an indexed array name subscripted by ```@``` or ```*```, the result is the *length* members of the array beginning with **${parameter[offset]}**. A negative *offset* is taken relative to one greater than the maximum index of the specified array. It is an expansion error if length evaluates to a number less than zero.

***Examples:***

```
$ array=(0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h)
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${array[@]:7}``` | 7 8 9 0 a b c d e f g h | |
| ```echo ${array[@]:7:2}``` | 7 8 | |
| ```echo ${array[@]:7:-2}``` | bash: -2: substring expression < 0 | |
| ```echo ${array[@]:0}``` | 0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h | |
| ```echo ${array[@]:0:2}``` | 0 1 | |

<p/>

Substring expansion applied to an **associative array** produces undefined results.

Substring indexing is zero-based unless the positional parameters are used, in which case the indexing starts at 1 by default. If *offset* is **0**, and the positional parameters are used, ```$@``` is prefixed to the list.

#### Format #7

```
${!prefix@}
${!prefix*}
```

Expands to the names of variables whose names begin with *prefix*, separated by the first character of the **IFS** special variable. When ```@``` is used and the expansion appears within double quotes, each variable name expands to a separate word.

***Examples:***

```
$ string1=01234567890abcdefgh
$ string2=abcdefghijk01234567
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${!strin*}``` | string1 string2 | |
| ```echo ${!strin@}``` | string1 string2 | |

<p/>

#### Format #8

```
${!name[@]}
${!name[*]}
```

If *name* is an array variable, expands to the list of array indices (keys) assigned in *name*. If *name* is not an array, expands to **0** if *name* is set and null otherwise. When ```@``` is used and the expansion appears within double quotes, each key expands to a separate word.

***Examples:***

```
$ array1=(0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h)
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${!array1[*]}``` | 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 | |
| ```echo ${!array1[@]}``` | 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 | |

<p/>

#### Format #9

```
${#parameter}
```

The length in characters of the expanded value of *parameter* is substituted.

* If *parameter* is ```*``` or ```@```, the value substituted is the number of [positional parameters](#positional-parameters).

* If *parameter* is an array name subscripted by ```*``` or ```@```, the value substituted is the number of elements in the array.

* If *parameter* is an **indexed array** name subscripted by a negative number, that number is interpreted as relative to one greater than the maximum index of *parameter*, so negative indices count back from the end of the array, and an index of **-1** references the
last element.

***Examples:***

```
$ string=01234567890abcdefgh
$ set -- 0 1 2 3 4 5 6 7 8 9
$ array=(0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h)
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${#string}``` | 19 | |
| ```echo ${#*}``` | 10 | [positional parameters](#positional-parameters) |
| ```echo ${#@}``` | 10 | [positional parameters](#positional-parameters) |
| ```echo ${#array[*]}``` | 19 | array |
| ```echo ${#array[@]}``` | 19 | array |
| ```echo ${#array[-1]}``` | 1 | indexed array with negative subscript |

<p/>

#### Format #10

```
${parameter#word}
${parameter##word}
```

The *word* is expanded to produce a pattern just as in filename expansion. If the pattern matches the **beginning** of the expanded value of *parameter*, then the result of the expansion is the expanded value of *parameter* with the shortest matching pattern (the ```#``` case) or the longest matching pattern (the ```##``` case) deleted.

* If *parameter* is ```@``` or ```*```, the pattern removal operation is applied to each **positional parameter** in turn, and the expansion is the resultant list.

* If *parameter* is an array variable subscripted with ```@``` or ```*```, the pattern removal operation is applied to each member of the array in turn, and the expansion is the resultant list.

***Examples:***

```
$ string=012345012345abcdeabcde
$ set -- 0 1 2 3 4 5 6 7 8 9
$ array=(0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h)
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${string#012*5}``` | 012345abcdeabcde | |
| ```echo ${string##012*5}``` | abcdeabcde | |
| ```echo ${string##012*5}``` | abcdeabcde | |
| ```echo ${string#012?5}``` | 012345abcdeabcde | |
| ```echo ${string##012?5}``` | 012345abcdeabcde | |
| ```echo ${*#5}``` | 0 1 2 3 4 6 7 8 9 | [positional parameters](#positional-parameters) |
| ```echo ${array[*]#b}``` | 0 1 2 3 4 5 6 7 8 9 0 a c d e f g h | array |
| ```echo ${array[@]#b}``` | 0 1 2 3 4 5 6 7 8 9 0 a c d e f g h | array |

<p/>

#### Format #11

```
${parameter%word}
${parameter%%word}
```

The *word* is expanded to produce a pattern just as in filename expansion. If the pattern matches a **trailing** portion of the expanded value of *parameter*, then the result of the expansion is the value of *parameter* with the shortest matching pattern (the ```%``` case) or the longest matching pattern (the ```%%``` case) deleted.

* If *parameter* is ```@``` or ```*```, the pattern removal operation is applied to each **positional parameter** in turn, and the expansion is the resultant list.

* If *parameter* is an array variable subscripted with ```@``` or ```*```, the pattern removal operation is applied to each member of the array in turn, and the expansion is the resultant list.

***Examples:***

```
$ string=012345012345abcdeabcde
$ set -- 0 1 2 3 4 5 6 7 8 9
$ array=(0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h)
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${string%abc*e}``` | 012345012345abcde | |
| ```echo ${string%%abc*e}``` | 012345012345 | |
| ```echo ${string%abc?de}``` | 012345012345abcde | |
| ```echo ${string%%abc?de}``` | 012345012345abcde | |
| ```echo ${*%8}``` | 0 1 2 3 4 5 6 7 9 | [positional parameters](#positional-parameters) |
| ```echo ${array[*]%b}``` | 0 1 2 3 4 5 6 7 8 9 0 a c d e f g h | array |
| ```echo ${array[@]%%b}``` | 0 1 2 3 4 5 6 7 8 9 0 a c d e f g h | array |

<p/>

#### Format #12

```
${parameter/pattern/string}
```

The *pattern* is expanded to produce a pattern just as in filename expansion. *parameter* is expanded and the longest match of *pattern* against its value is replaced with *string*.

* If *pattern* begins with ```/```, all matches of *pattern* are replaced with *string*. Normally only the first match is replaced.

* If *pattern* begins with ```#```, it must match at the beginning of the expanded value of *parameter*.

* If *pattern* begins with ```%```, it must match at the end of the expanded value of *parameter*.

* If *string* is null, matches of *pattern* are deleted and the ```/``` following *pattern* may be omitted.

* If *parameter* is ```@``` or ```*```, the substitution operation is applied to each positional parameter in turn, and the expansion is the resultant list.

* If *parameter* is an array variable subscripted with ```@``` or ```*```, the substitution operation is applied to each member of the array in turn, and the expansion is the resultant list.

***Examples:***

```
$ string=012345012345abcdeabcde
$ set -- 0 1 2 3 4 5 6 7 8 9
$ array=(0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h)
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${string/abc/xyz}``` | 012345012345xyzdeabcde | |
| ```echo ${string//abc/xyz}``` | 012345012345xyzdexyzde | |
| ```echo ${string/#012/xyz}``` | xyz345012345abcdeabcde | |
| ```echo ${string/%cde/xyz}``` | 012345012345abcdeabxyz | |
| ```echo ${string/cde/}``` | 012345012345abcdeab | |
| ```echo ${*/2/x}``` | 0 1 x 3 4 5 6 7 8 9 | [positional parameters](#positional-parameters) |
| ```echo ${@/2/x}``` | 0 1 x 3 4 5 6 7 8 9 | [positional parameters](#positional-parameters) |
| ```echo ${*/2/}``` | 0 1 3 4 5 6 7 8 9 | [positional parameters](#positional-parameters) |
| ```echo ${@/2/}``` | 0 1 3 4 5 6 7 8 9 | [positional parameters](#positional-parameters) |
| ```echo ${array[*]/a/x}``` | 0 1 2 3 4 5 6 7 8 9 0 x b c d e f g h | array |
| ```echo ${array[@]/a/x}``` | 0 1 2 3 4 5 6 7 8 9 0 x b c d e f g h | array |
| ```echo ${array[*]/a/}``` | 0 1 2 3 4 5 6 7 8 9 0 b c d e f g h | array |
| ```echo ${array[@]/a/}``` | 0 1 2 3 4 5 6 7 8 9 0 b c d e f g h | array |

<p/>

#### Format #13

```
${parameter^pattern}
${parameter^^pattern}
${parameter,pattern}
${parameter,,pattern}
```

This expansion modifies the case of alphabetic characters in *parameter*. The *pattern* is expanded to produce a *pattern* just as in filename expansion. Each character in the expanded value of *parameter* is tested against *pattern*, and, if it matches the *pattern*, its case is converted.

* The *pattern* should not attempt to match more than one character.

* The ```^``` operator converts lowercase letters matching pattern to uppercase; the ```,``` operator converts matching uppercase letters to lowercase.

* The ```^^``` and ```,,``` expansions convert each matched character in the expanded value; the ```^``` and ```,``` expansions match and convert only the first character in the expanded value.

* If *parameter* is ```@``` or ```*```, the case modification operation is applied to each **positional parameter** in turn, and the expansion is the resultant list.

* If *parameter* is an array variable subscripted with ```@``` or ```*```, the case modification operation is applied to each member of the array in turn, and the expansion is the resultant list.

***Examples:***

```
$ string=abcdeABCDEabcdeABCDE
$ set -- ABCDEabcdeABCDEabcde
$ array=(A B C D E a b c d e A B C D E a b c d e)
```

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo ${string^a}``` | AbcdeABCDEabcdeABCDE | |
| ```echo ${string^^a}``` | AbcdeABCDEAbcdeABCDE | |
| ```echo ${string,A}``` | abcdeABCDEabcdeABCDE | |
| ```echo ${string,,A}``` | abcdeaBCDEabcdeaBCDE | |
| ```echo ${*^a}``` | ABCDEabcdeABCDEabcde | [positional parameters](#positional-parameters) |
| ```echo ${*^^a}``` | ABCDEAbcdeABCDEAbcde | [positional parameters](#positional-parameters) |
| ```echo ${@^a}``` | ABCDEabcdeABCDEabcde | [positional parameters](#positional-parameters) |
| ```echo ${@^^a}``` | ABCDEAbcdeABCDEAbcde | [positional parameters](#positional-parameters) |
| ```echo ${*,A}``` | aBCDEabcdeABCDEabcde | [positional parameters](#positional-parameters) |
| ```echo ${*,,A}``` | aBCDEabcdeaBCDEabcde | [positional parameters](#positional-parameters) |
| ```echo ${@,A}``` | aBCDEabcdeABCDEabcde | [positional parameters](#positional-parameters) |
| ```echo ${@,,A}``` | aBCDEabcdeaBCDEabcde | [positional parameters](#positional-parameters) |
| ```echo ${array[*]^a}``` | A B C D E A b c d e A B C D E A b c d e | array |
| ```echo ${array[*]^^a}``` | A B C D E A b c d e A B C D E A b c d e | array |
| ```echo ${array[@]^a}``` | A B C D E A b c d e A B C D E A b c d e | array |
| ```echo ${array[@]^^a}``` | A B C D E A b c d e A B C D E A b c d e | array |
| ```echo ${array[*],A}``` | a B C D E a b c d e a B C D E a b c d e | array |
| ```echo ${array[*],,A}``` | a B C D E a b c d e a B C D E a b c d e | array |
| ```echo ${array[@],A}``` | a B C D E a b c d e a B C D E a b c d e | array |
| ```echo ${array[@],,A}``` | a B C D E a b c d e a B C D E a b c d e | array |

<p/>

### Arithmetic expansion

***Format:***

```
$(( expression ))
```

Arithmetic expansion allows the evaluation of an arithmetic expression and the substitution of the result.

The *expression* is treated as if it were within double quotes, but a double quote inside the parentheses is not treated specially. All tokens in the *expression* undergo [parameter and variable expansion](#parameter-and-variable-expansion), [command substitution](#command-substitution), and [quote removal](#quote-removal). The result is treated as the arithmetic expression to be evaluated. **Arithmetic expansions may be nested**.

The evaluation is performed according to the rules listed in [Shell Arithmetic](#shell-arithmetic). If the *expression* is invalid, Bash prints a message indicating failure to the standard error and no substitution occurs.

***Examples:***

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo $(( 1+2 ))``` | 3 | |
| ```echo $(( $(( 1+2 )) + 3 ))``` | 6 | Arithmetic expansions may be nested. |

### Command Substitution

***Formats:***

```
$(command)
`command`
```

Command substitution allows the output of a command to replace the command itself.

Bash performs the expansion by executing *command* and replacing the command substitution with the standard output of the *command*, **with any trailing newlines deleted**. Embedded newlines are not deleted, but they may be removed during **word splitting**. The command substitution ```$(cat file)``` can be replaced by the equivalent but faster ```$(< file)```.

When the old-style backquote form of substitution is used, backslash retains its literal meaning except when followed by ```$```, ```'```, or ```\```. The first backquote not preceded by a backslash terminates the command substitution. When using the ```$(command)``` form, all characters between the parentheses make up the command; none are treated specially.

**Command substitutions may be nested**. To nest when using the backquoted form, escape the inner backquotes with backslashes.

If the substitution appears within double quotes, **word splitting** and **filename expansion** are not performed on the results.

***Examples:***

| Formats | Expansions | Note |
| :-------| :--------- | :--- |
| ```echo $(ls *ml)``` | _config.yml feed.xml index.html |
| ```echo `ls *ml```` | _config.yml feed.xml index.html |

<p/>

### Process Substitution

***Formats:***

```
<(list)
>(list)
```

Process substitution is supported on systems that support **named pipes** (**FIFO**s) or the **/dev/fd** method of naming open files.

The process *list* is run with its input or output connected to a **FIFO** or some file in **/dev/fd**. The name of this file is passed as an argument to the current command as the result of the expansion.

* If the ```>(list)``` form is used, writing to the file will provide input for *list*.
* If the ```<(list)``` form is used, the file passed as an argument should be read to obtain the output of *list*.

Note that no space may appear between the ```<``` or ```>``` and the left parenthesis, otherwise the construct would be interpreted as a redirection.

When available, process substitution is performed simultaneously with [parameter and variable expansion](#parameter-and-variable-expansion), [command substitution](#command-substitution), and [arithmetic expansion](#arithmetic-expansion).

### Word Splitting

The shell scans the results of [parameter and variable expansion](#parameter-and-variable-expansion), [command substitution](#command-substitution), and [arithmetic expansion](#arithmetic-expansion) that **did not occur within double quotes** for word splitting.

The shell treats each character of ```$IFS``` as a delimiter, and splits the results of the other expansions into words using these characters as field terminators.

* If **IFS** is unset, or its value is exactly ```<space><tab><newline>```, the default, then sequences of ```<space>```, ```<tab>```, and ```<newline>``` at the beginning and end of the results of the previous expansions are ignored, and any sequence of **IFS** characters not at the beginning or end serves to delimit words.

* If **IFS** has a value other than the default, then sequences of the whitespace characters **space** and **tab** are ignored at the beginning and end of the word, as long as the whitespace character is in the value of **IFS** (an **IFS** whitespace character). Any character in **IFS** that is not **IFS** whitespace, along with any adjacent **IFS** whitespace characters, delimits a field. A sequence of **IFS** whitespace characters is also treated as a delimiter.

* If the value of **IFS** is null, no word splitting occurs.

Explicit null arguments (```""``` or ```''```) are retained. Unquoted implicit null arguments, resulting from the expansion of parameters that have no values, are removed. If a parameter with no value is expanded within double quotes, a null argument results and is retained.

Note that if no expansion occurs, no splitting is performed.

### Filename Expansion

After word splitting, unless the ```-f``` option has been set, Bash scans each word for the characters ```*```, ```?```, and ```[```. If one of these characters appears, then the word is regarded as a *pattern*, and replaced with an alphabetically sorted list of filenames matching the pattern (see [Pattern Matching](#pattern-matching)).

* If no matching filenames are found, and the shell option ```nullglob``` is disabled, the word is left unchanged. If the ```nullglob``` option is set, and no matches are found, the word is removed.

* If the shell option ```failglob``` is set, and no matches are found, an error message is printed and the command is not executed.

* If the shell option ```nocaseglob``` is enabled, the match is performed without regard to the case of alphabetic characters.

When a pattern is used for filename expansion, the character ```.``` at the start of a filename or immediately following a slash must be matched explicitly, unless the shell option ```dotglob``` is set. When matching a filename, the slash character must always be matched explicitly. In other cases, the ```.``` character is not treated specially.

See the description of **shopt** in [The *shopt* Builtin](#the-em-shopt-em-builtin) for a description of the ```nocaseglob```, ```nullglob```, ```failglob```, and ```dotglob``` options.

The shell variable ```GLOBIGNORE``` may be used to restrict the set of filenames matching a pattern.

* If ```GLOBIGNORE``` is set, each matching filename that also matches one of the patterns in ```GLOBIGNORE``` is removed from the list of matches. The filenames ```.``` and ```..``` are always ignored when ```GLOBIGNORE``` is set and not null. However, setting ```GLOBIGNORE``` to a non-null value has the effect of enabling the ```dotglob``` shell option, so all other filenames beginning with a ```.``` will match.

* To get the old behavior of ignoring filenames beginning with a ```.```, make ```.*``` one of the patterns in ```GLOBIGNORE```. The ```dotglob``` option is disabled when ```GLOBIGNORE``` is unset.

#### Pattern Matching

Any character that appears in a pattern, other than the special pattern characters described below, matches itself. The NUL character may not occur in a pattern. A backslash escapes the following character; the escaping backslash is discarded when matching. The special pattern characters must be quoted if they are to be matched literally.

The special pattern characters have the following meanings:

| Special_Pattern | Description |
| :-------------- | :---------- |
| ```*```              | Matches any string, including the null string.<br><br>When the ```globstar``` shell option is enabled, and ```*``` is used in a filename expansion context, two adjacent ```*``` used as a single pattern will match all files and zero or more directories and subdirectories. If followed by a ```/```, two adjacent ```*``` will match only directories and subdirectories. |
| ```?```              | Matches any single character. |
| ```[...]``` | Matches any one of the enclosed characters. The sorting order of characters in range expressions is determined by the current locale and the values of the ```LC_COLLATE``` and ```LC_ALL``` shell variables, if set.<br><br>```[a-z]```<br>```[a-zA-Z]```<br>A pair of characters separated by a hyphen ```-``` denotes a range expression; any character that falls between those two characters, inclusive, using the current locale's collating sequence and character set, is matched.<br><br>```[!...]```<br>```[^...]```<br>If the first character following the ```[``` is a ```!``` or a ```^``` then any character not enclosed is matched.<br><br>```[-...]```<br>```[...-]```<br>A ```-``` may be matched by including it as the first or last character in the set.<br><br>```[]...]```<br>A ```]``` may be matched by including it as the first character in the set.<br><br>```[:class:]```<br>Within ```[``` and ```]```, *character classes* can be specified using the syntax ```[:class:]```, where *class* is one of the following classes defined in the POSIX standard:<br>```alnum``` ```alpha``` ```ascii``` ```blank``` ```cntrl``` ```digit``` ```graph```<br>```lower``` ```print``` ```punct``` ```space``` ```upper``` ```word``` ```xdigit```<br>A character class matches any character belonging to that class. The ```word``` character class matches **letters**, **digits**, and the character ```_```.<br><br>```[=c=]```<br>Within ```[``` and ```]```, an *equivalence class* can be specified using the syntax ```[=c=]```, which matches all characters with the same collation weight as the character *c*.<br><br>```[.symbol.]```<br>Within ```[``` and ```]```, the syntax ```[.symbol.]``` matches the collating symbol *symbol*. |

<p/>

If the ```extglob``` shell option is enabled using the **shopt** builtin, several extended pattern matching operators are recognized. In the following description, a *pattern-list* is a list of one or more patterns separated by a ```|```. Composite patterns may be formed using one or more of the following sub-patterns:

| Extended_Pattern | Description |
| :--------------- | :---------- |
| ```?(pattern-list)``` | Matches **zero or one** occurrence of the given patterns if the shell option ```extglob``` is enabled using the ```shopt``` builtin. A *pattern-list* is a list of one or more patterns separated by a ```|```. |
| ```*(pattern-list)```<br>```+(pattern-list)``` | Matches **zero or more** occurrences of the given patterns if the shell option ```extglob``` is enabled using the ```shopt``` builtin. A *pattern-list* is a list of one or more patterns separated by a ```|```. |
| ```@(pattern-list)``` | Matches **one** of the given patterns if the shell option ```extglob``` is enabled using the ```shopt``` builtin. A *pattern-list* is a list of one or more patterns separated by a ```|```. |
| ```!(pattern-list)``` | Matches anything except one of the given patterns if the shell option ```extglob``` is enabled using the ```shopt``` builtin. A *pattern-list* is a list of one or more patterns separated by a ```|```. |

<p/>

### Quote Removal

After the preceding expansions, all unquoted occurrences of the characters ```\```, ```'```, and ```"``` that did not result from one of the above expansions are removed.

## Redirections

Before a command is executed, its input and output may be *redirected* using a special notation interpreted by the shell. Redirection allows commands' file handles to be duplicated, opened, closed, made to refer to different files, and can change the files the command reads from and writes to. Redirection may also be used to modify file handles in the current shell execution environment. The following redirection operators may precede or appear anywhere **within a simple command** or may **follow a command**. Redirections are processed in the order they appear, from left to right.

Each redirection that may be preceded by a file descriptor number may instead be preceded by a word of the form ```{varname}```. In this case, for each redirection operator except ```>&-``` and ```<&-```, the shell will allocate a file descriptor **greater than 10** and assign it to ```{varname}```. If ```>&-``` or ```<&-``` is preceded by ```{varname}```, the value of *varname* defines the file descriptor to close.

In the following descriptions, if the file descriptor number is omitted, and the first character of the redirection operator is ```<```, the redirection refers to the **standard input** (file descriptor **0**). If the first character of the redirection operator is ```>```, the redirection refers to the **standard output** (file descriptor **1**).

The word following the redirection operator in the following descriptions, unless otherwise noted, is subjected to **brace expansion**, **tilde expansion**, **parameter expansion**, **command substitution**, **arithmetic expansion**, **quote removal**, **filename expansion**, and **word splitting**. If it expands to more than one word, Bash reports an error.

Note that the order of redirections is significant. For example, the command ```ls > dirlist 2>&1``` directs both standard output (file descriptor 1) and standard error (file descriptor 2) to the file *dirlist*, while the command ```ls 2>&1 > dirlist``` directs only the standard output to file *dirlist*, because the standard error was made a copy of the standard output before the standard output was redirected to *dirlist*.

A failure to open or create a file causes the redirection to fail.

Redirections using file descriptors greater than **9** should be used with care, as they may conflict with file descriptors the shell uses internally.

Bash handles several filenames specially when they are used in redirections, as described in the following table:

| Special_Filenames | Descriptions |
| :---------------- | :----------- |
| ```/dev/fd/fd``` | If *fd* is a valid integer, file descriptor *fd* is duplicated. |
| ```/dev/stdin``` | File descriptor **0** is duplicated. |
| ```/dev/stdout``` | File descriptor **1** is duplicated. |
| ```/dev/stderr``` | File descriptor **2** is duplicated. |
| ```/dev/tcp/host/port``` | If *host* is a valid hostname or Internet address, and *port* is an integer port number or service name, Bash attempts to open the corresponding **TCP socket**. |
| ```/dev/udp/host/port``` | If *host* is a valid hostname or Internet address, and *port* is an integer port number or service name, Bash attempts to open the corresponding **UDP socket**. |

<p/>

Redirection operators:

| Redirections | Descriptions |
| :----------- | :----------- |
| ```[n]<word``` | Redirection of input causes the file whose name results from the expansion of *word* to be opened for reading on file descriptor *n*, or the **standard input** (file descriptor **0**) if *n* is not specified. |
| ```[n]>[|]word``` | Redirection of output causes the file whose name results from the expansion of *word* to be opened for writing on file descriptor *n*, or the **standard output** (file descriptor **1**) if *n* is not specified. If the file does not exist it is created; if it does exist it is truncated to **zero** size.<br><br>If the redirection operator is ```>```, and the ```noclobber``` option to the **set** builtin has been enabled, the redirection will fail if the file whose name results from the expansion of *word* exists and is a regular file.<br><br>If the redirection operator is ```>|```, or the redirection operator is ```>``` and the ```noclobber``` option is not enabled, the redirection is attempted even if the file named by *word* exists.  |
| ```[n]>>word``` | Redirection of output in this fashion causes the file whose name results from the expansion of *word* to be opened for appending on file descriptor *n*, or the **standard output** (file descriptor **1**) if *n* is not specified. If the file does not exist it is created. |
| Format #1:<br>```&>word```<br>```>word 2>&1```<br><br>Format #2:<br>```>&word``` | This construct allows both the **standard output** (file descriptor **1**) and the **standard error output** (file descriptor **2**) to be redirected to the file whose name is the expansion of *word*.<br><br>The form ```&>word``` is preferred, which is semantically equivalent to ```>word 2>&1```.<br><br>When using the form ```>&word```, *word* may not expand to a number or ```-```. If it does, other redirection operators apply for compatibility reasons. |
| ```&>>word```<br>```>>word 2>&1``` | This construct allows both the **standard output** (file descriptor **1**) and the **standard error output** (file descriptor **2**) to be appended to the file whose name is the expansion of *word*. |
| ```<<[-]word```<br>```<TAB>here-document```<br>```delimiter``` | **Here Documents**. This type of redirection instructs the shell to read input from the current source until a line containing only *word* (with no trailing blanks) is seen. All of the lines read up to that point are then used as the **standard input** for a command.<br><br>No parameter and variable expansion, command substitution, arithmetic expansion, or filename expansion is performed on word. If any characters in *word* are quoted, the *delimiter* is the result of quote removal on *word*, and the lines in the *here-document* are not expanded.<br><br>If word is unquoted, all lines of the *here-document* are subjected to parameter expansion, command substitution, and arithmetic expansion, the character sequence ```\newline``` is ignored, and ```\``` must be used to quote the characters ```\```, ```$```, and ``` ` ```.<br><br>If the redirection operator is ```<<-```, then all leading tab characters are stripped from input lines and the line containing *delimiter*. This allows *here-documents* within shell scripts to be indented in a natural fashion. |
| ```<<< word``` | **Here Strings** is variant of **Here Documents**. The *word* undergoes **brace expansion**, **tilde expansion**, **parameter and variable expansion**, **command substitution**, **arithmetic expansion**, and **quote removal**. **Pathname expansion** and **word splitting** are not performed. The result is supplied as a single string to the command on its **standard input**. |
| ```[n]<&word``` | **Duplicating Input File Descriptors**. It is used to duplicate input file descriptors. If *word* expands to one or more digits, the file descriptor denoted by *n* is made to be a copy of that file descriptor. If the digits in *word* do not specify a file descriptor open for input, a redirection error occurs. If word evaluates to ```-```, file descriptor *n* is closed. If *n* is not specified, the **standard input** (file descriptor **0**) is used. |
| ```[n]>&word``` | **Duplicating Output File Descriptors**. It is used similarly to duplicate output file descriptors. If *n* is not specified, the **standard output** (file descriptor **1**) is used. If the digits in *word* do not specify a file descriptor open for output, a redirection error occurs. If word evaluates to ```-```, file descriptor *n* is closed. As a special case, if *n* is omitted, and *word* does not expand to one or more digits or ```-```, the **standard output** and **standard error** are redirected as described previously. |
| ```[n]<&digit-``` | **Moving Input File Descriptors**. It moves the file descriptor *digit* to file descriptor *n*, or the **standard input** (file descriptor **0**) if *n* is not specified. *digit* is closed after being duplicated to *n*. |
| ```[n]>&digit-``` | **Moving Output File Descriptors**. It moves the file descriptor *digit* to file descriptor *n*, or the **standard output** (file descriptor **1**) if *n* is not specified. |
| ```[n]<>word``` | **Opening File Descriptors for Reading and Writing**. It causes the file whose name is the expansion of *word* to be opened for both reading and writing on file descriptor *n*, or on file descriptor **0** if *n* is not specified. If the file does not exist, it is created. |

## Executing Commands

### Simple Command Expansion

When a simple command is executed, the shell performs the following expansions, assignments, and redirections, from left to right.

1. The words that the parser has marked as **variable assignments** (those preceding the command name) and **redirections** are saved for later processing.

2. The words that are not **variable assignments** or **redirections** are expanded (see [Shell Expansions](#shell-expansions)). If any words remain after expansion, the first word is taken to be the name of the command and the remaining words are the arguments.

3. Redirections are performed as described in [Redirections](#redirections).

4. The text after the ```=``` in each variable assignment undergoes **tilde expansion**, **parameter expansion**, **command substitution**, **arithmetic expansion**, and **quote removal** before being assigned to the variable.

5. If no command name results, the **variable assignments** affect the current shell environment. Otherwise, the variables are added to the environment of the executed command and do not affect the current shell environment. If any of the assignments attempts to assign a value to a readonly variable, an error occurs, and the command exits with a non-zero status.

If no command name results, **redirections** are performed, but do not affect the current shell environment. A redirection error causes the command to exit with a non-zero status.

If there is a command name left after expansion, execution proceeds as described below. Otherwise, the command exits. If one of the expansions contained a command substitution, the exit status of the command is the exit status of the last command substitution performed. If there were no command substitutions, the command exits with a status of **zero**.

### Command Search and Execution

The following figure shows the command search and execution:

![Command Search and Execution](/assets/Executing_Commands.png)

### Command Execution Environment

The shell has an *execution environment*, which consists of the following:

* open files inherited by the shell at invocation, as modified by redirections supplied to the **exec** builtin

* the current working directory as set by **cd**, **pushd**, or **popd**, or inherited by the shell at invocation

* the file creation mode mask as set by **umask** or inherited from the shell's parent

* current traps set by **trap**

* shell parameters that are set by variable assignment or with **set** or inherited from the shell's parent in the environment

* shell functions defined during execution or inherited from the shell's parent in the environment

* options enabled at invocation (either by default or with command-line arguments) or by **set**

* options enabled by **shopt** (see [The *shopt* Builtin](#the-em-shopt-em-builtin))

* shell aliases defined with **alias** (see [Aliases](#aliases))

* various process IDs, including those of background jobs, the value of ```$$```, and the value of ```$PPID```

When a **simple command** other than a **builtin** or **shell function** is to be executed, it is invoked in a separate execution environment that consists of the following. Unless otherwise noted, the values are inherited from the shell.

* the shell's open files, plus any modifications and additions specified by redirections to the command

* the current working directory

* the file creation mode mask

* shell variables and functions marked for export, along with variables exported for the command, passed in the environment (see [Environment](#environment))

* traps caught by the shell are reset to the values inherited from the shell's parent, and traps ignored by the shell are ignored

A command invoked in this separate environment cannot affect the shell’s execution environment.

Command substitution, commands grouped with parentheses, and asynchronous commands are invoked in a subshell environment that is a duplicate of the shell environment, except that traps caught by the shell are reset to the values that the shell inherited from its parent at invocation. Builtin commands that are invoked as part of a pipeline are also executed in a subshell environment. Changes made to the subshell environment cannot affect the shell’s execution environment.

Subshells spawned to execute command substitutions inherit the value of the ```-e``` option from the parent shell. When not in posix mode, Bash clears the ```-e``` option in such subshells.

If a command is followed by a ```&``` and job control is not active, the default standard input for the command is the empty file ```/dev/null```. Otherwise, the invoked command inherits the file descriptors of the calling shell as modified by redirections.

### Environment

When a program is invoked it is given an array of strings called the *environment*. This is a list of name-value pairs, of the form ```name=value```.

Bash provides several ways to manipulate the environment. On invocation, the shell scans its own environment and creates a parameter for each name found, automatically marking it for export to child processes. Executed commands inherit the environment. The ```export``` and ```declare -x``` commands allow parameters and functions to be added to and deleted from the environment. If the value of a parameter in the environment is modified, the new value becomes part of the environment, replacing the old. The environment inherited by any executed command consists of the shell's initial environment, whose values may be modified in the shell, less any pairs removed by the ```unset``` and ```export -n``` commands, plus any additions via the ```export``` and ```declare -x``` commands.

The environment for any simple command or function may be augmented temporarily by prefixing it with parameter assignments, as described in [Shell Parameters](#shell-parameters). These assignment statements affect only the environment seen by that command.

If the ```-k``` option is set (see [The *set* Builtin](#the-em-set-em-builtin)), then all parameter assignments are placed in the environment for a command, not just those that precede the command name.

When Bash invokes an external command, the variable ```$_``` is set to the full pathname of the command and passed to that command in its environment, see [Special Parameters](#special-parameters).

### Exit Status

The exit status of an executed command is the value returned by the ***waitpid*** system call or equivalent function. Exit statuses fall **between 0 and 255**, though, as explained below, the shell may use values above **125** specially. Exit statuses from **shell builtins** and **compound commands** are also limited to this range. Under certain circumstances, the shell will use special values to indicate specific failure modes.

For the shell's purposes, **a command which exits with a zero exit status has succeeded**. **A non-zero exit status indicates failure**. This seemingly counter-intuitive scheme is used so there is one well-defined way to indicate success and a variety of ways to indicate various failure modes.

* If a command is found but is not executable, the return status is **126**.

* If a command is not found, the child process created to execute it returns a status of **127**.

* If a command terminates on a **fatal signal** whose number is ***N***, Bash uses the value **128+*****N*** as the exit status.

* If a command fails because of an error during expansion or redirection, the exit status is **greater than zero**.

The exit status is used by the Bash conditional commands and some of the list constructs.

All of the Bash **builtins** return an exit status of zero if they succeed and a non-zero status on failure, so they may be used by the conditional and list constructs. All **builtins** return an exit status of **2** to indicate incorrect usage.

Check the special parameter **$?** to get the exit status of the most recently executed foreground pipeline.

| Exit_values | Description |
| :---------: | :---------- |
| **0**       | The command is executed successfully. |
| **2**       | All **builtins** return an exit status of **2** to indicate incorrect usage. |
| **126**     | If a command is found but is not executable, the return status is **126**. |
| **127**     | If a command is not found, the child process created to execute it returns a status of **127**. |
| **128+***N* | If a command terminates on a **fatal signal** whose number is *N*, Bash uses the value **128+***N* as the exit status. |

<p/>

### Signals

When Bash is interactive, in the absence of any traps, it ignores **SIGTERM** (so that **kill 0** does not kill an interactive shell), and **SIGINT** is caught and handled (so that the **wait** builtin is interruptible). When Bash receives a **SIGINT**, it breaks out of any executing loops. In all cases, Bash ignores **SIGQUIT**. If job control is in effect (see [Job Control](#job-control)), Bash ignores **SIGTTIN**, **SIGTTOU**, and **SIGTSTP**.

Non-builtin commands started by Bash have signal handlers set to the values inherited by the shell from its parent. When job control is not in effect, asynchronous commands ignore **SIGINT** and **SIGQUIT** in addition to these inherited handlers. Commands run as a result of command substitution ignore the keyboard-generated job control signals **SIGTTIN**, S**IGTTOU**, and **SIGTSTP**.

The shell exits by default upon receipt of a **SIGHUP**. Before exiting, an interactive shell resends the **SIGHUP** to all jobs, running or stopped. Stopped jobs are sent **SIGCONT** to ensure that they receive the **SIGHUP**. To prevent the shell from sending the **SIGHUP** signal to a particular job, it should be removed from the jobs table with the disown builtin (see [Job Control Builtins](#job-control-builtins)) or marked to not receive **SIGHUP** using ```disown -h```.

If the **huponexit** shell option has been set with **shopt** (see [The *shopt* Builtin](#the-em-shopt-em-builtin)), Bash sends a **SIGHUP** to all jobs when an interactive login shell exits.

If Bash is waiting for a command to complete and receives a signal for which a trap has been set, the trap will not be executed until the command completes. When Bash is waiting for an asynchronous command via the **wait** builtin, the reception of a signal for which a trap has been set will cause the **wait** builtin to return immediately with an exit status greater than **128**, immediately after which the trap is executed.

## Shell Scripts

A shell script is a text file containing shell commands. When such a file is used as the first non-option argument when invoking Bash, and neither the ```-c``` nor ```-s``` option is supplied (see [Invoking Bash](#invoking-bash)), Bash reads and executes commands from the file, then exits. This mode of operation creates a **non-interactive shell**. The shell first searches for the file in the **current directory**, and looks in the directories in **$PATH** if not found there.

When Bash runs a shell script, it sets the special parameter **0** to the name of the file, rather than the name of the shell, and the **positional parameters** are set to the remaining arguments, if any are given. If no additional arguments are supplied, the **positional parameters** are unset.

A shell script may be made executable by using the **chmod** command to turn on the execute bit. When Bash finds such a file while searching the **$PATH** for a command, it spawns a **subshell** to execute it. In other words, executing ```filename arguments``` is equivalent to executing ```bash filename arguments``` if *filename* is an executable shell script. This subshell reinitializes itself, so that the effect is as if a new shell had been invoked to interpret the script, with the exception that the locations of commands remembered by the parent (see the description of **hash** in [Bourne Shell Builtins](#bourne-shell-builtins)) are retained by the child.

Most versions of Unix make this a part of the operating system's command execution mechanism. If the first line of a script begins with the two characters ```#!```, the remainder of the line specifies an interpreter for the program. Thus, you can specify **Bash**, **awk**, **Perl**, or some other interpreter and write the rest of the script file in that language.

The arguments to the interpreter consist of a single optional argument following the interpreter name on the first line of the script file, followed by the name of the script file, followed by the rest of the arguments. Bash will perform this action on operating systems that do not handle it themselves. Note that some older versions of Unix limit the interpreter name and argument to a maximum of **32** characters.

Bash scripts often begin with ```#! /bin/bash``` (assuming that Bash has been installed in ```/bin```), since this ensures that Bash will be used to interpret the script, even if it is executed under another shell.

***Example:*** save the following code to *ex1.sh*:

```
#! /bin/bash

echo Your input is "$1"
```

and save the following code to *ex2.sh*:

```
#! /bin/bash -v

echo Your input is "$1"
```

Then, execute the following commands:

```
chenwx@chenwx ~ $ chmod +x ex1.sh ex2.sh
chenwx@chenwx ~ $ ./ex1.sh 1
Your input is 1
chenwx@chenwx ~ $ ./ex2.sh 2
#! /bin/bash -v

echo Your input is "$1"
Your input is 2

```

# Shell Builtin Commands

## Bourne Shell Builtins

The following shell builtin commands are inherited from the **Bourne Shell**. These commands are implemented as specified by the **POSIX** standard, see [Shell and Utilities, Issue 7 (XCU7)](http://chenweixiang.github.io/2015/12/07/unix-system-overview.html#shell-and-utilities-issue-7-xcu7).

|    Builtins    | Description |
| :------------- | :---------- |
| ```:```        | Format:<br>```: [arguments]```<br><br>Do nothing beyond expanding *arguments* and performing redirections. The return status is zero. |
| ```.```        | Format:<br>```. filename [arguments]```<br><br>Read and execute commands from the *filename* argument in the current shell context. If *filename* does not contain a slash, the **PATH** variable is used to find *filename*.<br><br>The return status is the exit status of the last command executed, or zero if no commands are executed. If *filename* is not found, or cannot be read, the return status is non-zero.<br><br>This builtin is equivalent to ```source```. |
| ```break```    | Format:<br>```break [n]```<br><br>Exit from a *for*, *while*, *until*, or *select* loop. If *n* is supplied, the *n*th enclosing loop is exited. *n* must be greater than or equal to 1.<br><br>The return status is zero unless *n* is not greater than or equal to 1. |
| ```cd```       | Format:<br>```cd [-L|[-P [-e]] [-@] [directory]```<br><br>Change the current working directory to *directory*.<br><br>If *directory* is not supplied, the value of the **HOME** shell variable is used. Any additional arguments following *directory* are ignored. If the shell variable **CDPATH** exists, it is used as a search path: each directory name in **CDPATH** is searched for *directory*, with alternative directory names in **CDPATH** separated by a colon (**:**). If directory begins with a slash, **CDPATH** is not used.<br><br>If directory is ```-```, it is converted to **$OLDPWD** before the directory change is attempted.<br><br>The return status is zero if the directory is successfully changed, non-zero otherwise. |
| ```continue``` | Format:<br>```continue [n]```<br><br>Resume the next iteration of an enclosing *for*, *while*, *until*, or *select* loop. If *n* is supplied, the execution of the *n*th enclosing loop is resumed. *n* must be greater than or equal to 1.<br><br>The return status is zero unless *n* is not greater than or equal to 1. |
| ```eval```     | Format:<br>```eval [arguments]```<br><br>The *arguments* are concatenated together into a single command, which is then read and executed, and its exit status returned as the exit status of *eval*. If there are no arguments or only empty arguments, the return status is zero. |
| ```exec```     | Format:<br>```exec [-cl] [-a name] [command [arguments]]```<br><br>If *command* is supplied, it replaces the shell without creating a new process.<br><br>If the ```-l``` option is supplied, the shell places a dash (```-```) at the beginning of the *zero*th argument passed to *command*. This is what the ```login``` program does.<br>The ```-c``` option causes *command* to be executed with an empty environment.<br>If the ```-a``` option is supplied, the shell passes *name* as the *zero*th argument to *command*.<br><br>If *command* cannot be executed for some reason, a **non-interactive shell** exits, unless the ```execfail``` shell option is enabled. In that case, it returns failure. An **interactive shell** returns failure if the file cannot be executed.<br><br>If no *command* is specified, redirections may be used to affect the current shell environment. If there are no redirection errors, the return status is zero; otherwise the return status is non-zero.  |
| ```exit```     | Format:<br>```exit [n]```<br><br>Exit the shell, returning a status of *n* to the shell's parent. If *n* is omitted, the exit status is that of the last command executed. Any trap on **EXIT** is executed before the shell terminates.  |
| ```export```   | Format:<br>```export [-fn] [-p] [name[=value]]```<br><br>Mark each *name* to be passed to child processes in the environment.<br><br>If the ```-f``` option is supplied, the *names* refer to shell functions; otherwise the *names* refer to shell variables. <br>The ```-n``` option means to no longer mark each *name* for export.<br>If no *names* are supplied, or if the ```-p``` option is given, a list of names of all exported variables is displayed.<br>The ```-p``` option displays output in a form that may be reused as input.<br>If a variable name is followed by ```=value```, the value of the variable is set to value.<br><br>The return status is zero unless an invalid option is supplied, one of the names is not a valid shell variable name, or ```-f``` is supplied with a name that is not a shell function.  |
| ```getopts```  | Format:<br>```getopts optstring name [args]```<br><br>*getopts* is used by shell scripts to parse **positional parameters**. *optstring* contains the option characters to be recognized; if a character is followed by a colon (```:```), the option is expected to have an argument, which should be separated from it by whitespace. The colon (```:```) and question mark (```?```) may not be used as option characters.<br><br>Each time it is invoked, *getopts* places the next option in the shell variable *name*, initializing *name* if it does not exist, and the index of the next argument to be processed into the variable **OPTIND**. **OPTIND** is initialized to 1 each time the shell or a shell script is invoked.<br><br>```getopts``` normally parses the **positional parameters**, but if more arguments are given in *args*, ```getopts``` parses those instead.  |
| ```hash```     | Format:<br>```hash [-r] [-p filename] [-dt] [name]```<br><br>Each time *hash* is invoked, it remembers the full pathnames of the commands specified as *name* arguments, so they need not be searched for on subsequent invocations. The commands are found by searching through the directories listed in **$PATH**. Any previously-remembered pathname is discarded.<br><br>The ```-p``` option inhibits the path search, and *filename* is used as the location of *name*.<br>The ```-r``` option causes the shell to forget all remembered locations.<br>The ```-d``` option causes the shell to forget the remembered location of each *name*.<br>If the ```-t``` option is supplied, the full pathname to which each *name* corresponds is printed. If multiple *name* arguments are supplied with ```-t``` the *name* is printed before the hashed full pathname.<br>The ```-l``` option causes output to be displayed in a format that may be reused as input.<br>If no arguments are given, or if only ```-l``` is supplied, information about remembered commands is printed.<br><br>The return status is zero unless a *name* is not found or an invalid option is supplied. |
| ```pwd```      | Format:<br>```pwd [-LP]```<br><br>Print the absolute pathname of the current working directory.<br><br>If the ```-P``` option is supplied, the pathname printed will not contain symbolic links.<br>If the ```-L``` option is supplied, the pathname printed may contain symbolic links.<br><br>The return status is zero unless an error is encountered while determining the name of the current directory or an invalid option is supplied. |
| ```readonly``` | Format:<br>```readonly [-aAf] [-p] [name[=value]] ...```<br><br>Mark each *name* as readonly. The values of these names may not be changed by subsequent assignment.<br><br>If the ```-f``` option is supplied, each *name* refers to a shell function.<br>The ```-a``` option means each *name* refers to an indexed array variable; the ```-A``` option means each *name* refers to an associative array variable. If both options are supplied, ```-A``` takes precedence.<br>If no *name* arguments are given, or if the ```-p``` option is supplied, a list of all readonly names is printed. The other options may be used to restrict the output to a subset of the set of readonly names.<br>The ```-p``` option causes output to be displayed in a format that may be reused as input.<br>If a variable *name* is followed by ```=value```, the value of the variable is set to *value*.<br><br>The return status is zero unless an invalid option is supplied, one of the *name* arguments is not a valid shell variable or function name, or the ```-f``` option is supplied with a *name* that is not a shell function.  |
| ```return```   | Format:<br>```return [n]```<br><br>Cause a shell function to stop executing and return the value *n* to its caller. If *n* is not supplied, the return value is the exit status of the last command executed in the function.<br><br>*return* may also be used to terminate execution of a script being executed with the ```.``` (*source*) builtin, returning either *n* or the exit status of the last command executed within the script as the exit status of the script.<br><br>If *n* is supplied, the return value is its least significant 8 bits. Any command associated with the **RETURN** trap is executed before execution resumes after the function or script.<br><br>The return status is non-zero if return is supplied a non-numeric argument or is used outside a function and not during the execution of a script by ```.``` or ```source```. |
| ```shift```    | Format:<br>```shift [n]```<br><br>Shift the **positional parameters** to the left by *n*. The positional parameters from ***n+1*** ... ***$#*** are renamed to ***$1*** ... ***$#-n***. Parameters represented by the numbers ***$#*** to ***$#-n+1*** are unset.<br><br>*n* must be a non-negative number less than or equal to ***$#***.<br>If *n* is zero or greater than ***$#***, the positional parameters are not changed.<br>If *n* is not supplied, it is assumed to be 1.<br><br>The return status is zero unless *n* is greater than ***$#*** or less than zero, non-zero otherwise.  |
| ```test```<br>```[``` | Format:<br>```test expr```<br><br>Evaluate a conditional expression *expr* and return a status of 0 (true) or 1 (false). Each operator and operand must be a separate argument. *test* does not accept any options, nor does it accept and ignore an argument of ```--``` as signifying the end of options.<br><br>When the ```[``` form is used, the last argument to the command must be a ```]```.<br><br>Expressions may be combined using the following operators, listed in decreasing order of precedence. The evaluation depends on the number of arguments; see below. Operator precedence is used when there are five or more arguments.<br><br>```! expr``` True if expr is false.<br>```( expr )``` Returns the value of *expr*. This may be used to override the normal precedence of operators.<br>```expr1 -a expr2``` True if both *expr1* and *expr2* are true.<br>```expr1 -o expr2``` True if either *expr1* or *expr2* is true. |
| ```times```    | Format:<br>```times```<br><br>Print out the user and system times used by the shell and its children. The return status is zero. |
| ```trap```     | Format:<br>```trap [-lp] [arg] [sigspec ...]```<br><br>The commands in *arg* are to be read and executed when the shell receives signal *sigspec*.<br><br>If *arg* is absent (and there is a single *sigspec*) or equal to ```-```, each specified signal's disposition is reset to the value it had when the shell was started.<br>If *arg* is the null string, then the signal specified by each *sigspec* is ignored by the shell and commands it invokes.<br>If *arg* is not present and ```-p``` has been supplied, the shell displays the *trap* commands associated with each *sigspec*. If no arguments are supplied, or only ```-p``` is given, *trap* prints the list of commands associated with each signal number in a form that may be reused as shell input.<br>The ```-l``` option causes the shell to print a list of signal names and their corresponding numbers.<br><br>Each *sigspec* is either a signal name or a signal number. Signal names are case insensitive and the SIG prefix is optional.<br><br>If a *sigspec* is 0 or EXIT, *arg* is executed when the shell exits.<br>If a *sigspec* is DEBUG, the command *arg* is executed before every simple command, *for* command, *case* command, *select* command, every arithmetic *for* command, and before the first command executes in a shell function.<br> If a *sigspec* is RETURN, the command *arg* is executed each time a shell function or a script executed with the ```.``` or ```source``` builtins finishes executing.<br><br>If a *sigspec* is ERR, the command *arg* is executed whenever a pipeline (which may consist of a single simple command), a list, or a compound command returns a non-zero exit status, subject to the following conditions. The **ERR** trap is not executed if the failed command is part of the command list immediately following an *until* or *while* keyword, part of the test following the *if* or *elif* reserved words, part of a command executed in a ```&&``` or ```||``` list except the command following the final ```&&``` or ```||```, any command in a pipeline but the last, or if the command's return status is being inverted using ```!```. These are the same conditions obeyed by the *errexit* (-e) option.<br><br>Signals ignored upon entry to the shell cannot be trapped or reset. Trapped signals that are not being ignored are reset to their original values in a subshell or subshell environment when one is created.<br><br>The return status is zero unless a sigspec does not specify a valid signal. |
| ```umask```    | Format:<br>```umask [-p] [-S] [mode]```<br><br>Set the shell process's file creation mask to *mode*.<br><br>If *mode* begins with a digit, it is interpreted as an octal number; if not, it is interpreted as a symbolic mode mask similar to that accepted by the *chmod* command.<br>If mode is omitted, the current value of the mask is printed.<br>If the ```-S``` option is supplied without a *mode* argument, the mask is printed in a symbolic format.<br>If the ```-p``` option is supplied, and *mode* is omitted, the output is in a form that may be reused as input.<br><br>The return status is zero if the mode is successfully changed or if no mode argument is supplied, and non-zero otherwise.<br><br>Note that when the *mode* is interpreted as an octal number, each number of the umask is subtracted from 7. Thus, a umask of 022 results in permissions of 755. |
| ```unset```    | Format:<br>```unset [-fnv] [name]```<br><br>Remove each variable or function *name*.<br><br>If the ```-v``` option is given, each *name* refers to a shell variable and that variable is removed.<br>If the ```-f``` option is given, the *names* refer to shell functions, and the function definition is removed.<br>If the ```-n``` option is given, and *name* is a variable with the nameref attribute, *name* will be unset rather than the variable it references. ```-n``` has no effect if the ```-f``` option is supplied.<br>If no options are supplied, each *name* refers to a variable; if there is no variable by that *name*, any function with that name is unset. Readonly variables and functions may not be unset.<br><br>The return status is zero unless a *name* is readonly.  |

<p/>

## Bash Builtin Commands

This section describes builtin commands which are unique to or have been extended in **Bash**. Some of these commands are specified in the **POSIX** standard, see [Shell and Utilities, Issue 7 (XCU7)](http://chenweixiang.github.io/2015/12/07/unix-system-overview.html#shell-and-utilities-issue-7-xcu7).

| Bash_builtins | Description |
| :------------ | :---------- |
| ```alias```   | Format:<br>```alias [-p] [name[=value] ...]```<br><br>Without arguments or with the ```-p``` option, *alias* prints the list of aliases on the standard output in a form that allows them to be reused as input.<br><br>If arguments are supplied, an alias is defined for each *name* whose *value* is given. If no *value* is given, the *name* and value of the alias is printed. Also refer to [Aliases](#aliases).<br><br>```$ alias ll```<br>```alias ll='ls --color=auto -l'``` |
| ```bind```    | Format:<br>```bind [-m keymap] [-lpsvPSVX]```<br>```bind [-m keymap] [-q function] [-u function] [-r keyseq]```<br>```bind [-m keymap] -f filename```<br>```bind [-m keymap] -x keyseq:shell-command```<br>```bind [-m keymap] keyseq:function-name```<br>```bind readline-command```<br><br>Display current Readline key and function bindings, bind a key sequence to a Readline function or macro, or set a Readline variable. Each non-option argument is a command as it would appear in a Readline initialization file, but each binding or command must be passed as a separate argument.<br><br>```bind -p```<br>```"\C-x\C-r":re-read-init-file```.<br><br>The return status is zero unless an invalid option is supplied or an error occurs.<br><br>Also refer to [Readline Init File Syntax](#readline-init-file-syntax). |
| ```builtin``` | Format:<br>```builtin [shell-builtin [args]]```<br><br>Run a shell builtin, passing it *args*, and return its exit status. This is useful when defining a shell function with the same name as a shell builtin, retaining the functionality of the builtin within the function. The return status is non-zero if *shell-builtin* is not a shell builtin command. |
| ```caller```  | Format:<br>```caller [expr]```<br><br>Returns the context of any active subroutine call (a shell function or a script executed with the . or source builtins).<br><br>Without *expr*, *caller* displays the line number and source filename of the current subroutine call. If a non-negative integer is supplied as *expr*, *caller* displays the line number, subroutine name, and source file corresponding to that position in the current execution call stack. This extra information may be used, for example, to print a stack trace. The current frame is frame 0.<br><br>The return value is 0 unless the shell is not executing a subroutine call or *expr* does not correspond to a valid position in the call stack. |
| ```command``` | Format:<br>```command [-pVv] command [arguments ...]```<br><br>Runs *command* with *arguments* ignoring any shell function named *command*. Only shell builtin commands or commands found by searching the **PATH** are executed. If there is a shell function named *ls*, running ```command ls``` within the function will execute the external command *ls* instead of calling the function recursively. The ```-p``` option means to use a default value for PATH that is guaranteed to find all of the standard utilities. The return status in this case is 127 if command cannot be found or an error occurred, and the exit status of command otherwise.<br><br>If either the ```-V``` or ```-v``` option is supplied, a description of command is printed. The ```-v``` option causes a single word indicating the command or file name used to invoke command to be displayed; the ```-V``` option produces a more verbose description. In this case, the return status is zero if command is found, and non-zero if not. |
| ```declare``` | Format:<br>```declare [-aAfFgilnrtux] [-p] [name[=value] ...]```<br><br>Declare variables and give them attributes. If no names are given, then display the values of variables instead. |
| ```echo```    | Format:<br>```echo [-neE] [arg ...]```<br><br>Output the args, separated by spaces, terminated with a newline.<br><br>The return status is 0 unless a write error occurs.<br><br>If ```-n``` is specified, the trailing newline is suppressed.<br>If the ```-e``` option is given, interpretation of the backslash-escaped characters is enabled.<br>The ```-E``` option disables the interpretation of these escape characters, even on systems where they are interpreted by default.<br><br>The ```xpg_echo``` shell option may be used to dynamically determine whether or not echo expands these escape characters by default. echo does not interpret ```--``` to mean the end of options. |
| ```enable```  | Format:<br>```enable [-a] [-dnps] [-f filename] [name ...]```<br><br>Enable and disable builtin shell commands. Disabling a builtin allows a disk command which has the same name as a shell builtin to be executed without specifying a full pathname, even though the shell normally searches for builtins before disk commands.<br><br>If ```-n``` is used, the names become disabled. Otherwise names are enabled.<br><br>If the ```-p``` option is supplied, or no name arguments appear, a list of shell builtins is printed. With no other arguments, the list consists of all enabled shell builtins. The ```-a``` option means to list each builtin with an indication of whether or not it is enabled.<br><br>The return status is zero unless a name is not a shell builtin or there is an error loading a new builtin from a shared object. |
| ```help```    | Format:<br>```help [-dms] [pattern]```<br><br>Display helpful information about builtin commands. If *pattern* is specified, *help* gives detailed help on all commands matching pattern, otherwise a list of the builtins is printed.<br><br>The return status is zero unless no command matches pattern. |
| ```let```     | Format:<br>```let expression [expression ...]```<br><br>The *let* builtin allows arithmetic to be performed on shell variables. Each expression is evaluated according to the rules given in ```(( expression ))```, refer to [Conditional Constructs](#conditional-constructs). If the last *expression* evaluates to 0, let returns 1; otherwise 0 is returned. |
| ```local```   | Format:<br>```local [option] name[=value] ...```<br><br>For each argument, a local variable named *name* is created, and assigned *value*. The *option* can be any of the options accepted by *declare*. *local* can only be used within a function; it makes the variable name have a visible scope restricted to that function and its children.<br><br>The return status is zero unless *local* is used outside a function, an invalid *name* is supplied, or *name* is a readonly variable. |
| ```logout```  | Format:<br>```logout [n]```<br><br>Exit a login shell, returning a status of *n* to the shell's parent. |
| ```mapfile``` | Format:<br>```mapfile [-n count] [-O origin] [-s count] [-t] [-u fd] [-C callback] [-c quantum] [array]```<br><br>Read lines from the standard input into the indexed array variable *array*, or from file descriptor *fd* if the ```-u``` option is supplied. The variable *MAPFILE* is the default array.<br><br>mapfile returns successfully unless an invalid option or option argument is supplied, array is invalid or unassignable, or array is not an indexed array. |
| ```printf```  | Format:<br>```printf [-v var] format [arguments]```<br><br>Write the formatted *arguments* to the standard output under the control of the format. The ```-v``` option causes the output to be assigned to the variable *var* rather than being printed to the standard output. |
| ```read```    | Format:<br>```read [-ers] [-a aname] [-d delim] [-i text] [-n nchars] [-N nchars] [-p prompt] [-t timeout] [-u fd] [name ...]```<br><br>One line is read from the standard input, or from the file descriptor *fd* supplied as an argument to the ```-u``` option, and the first word is assigned to the first *name*, the second word to the second *name*, and so on, with leftover words and their intervening separators assigned to the last *name*. If there are fewer words read from the input stream than names, the remaining names are assigned empty values. The characters in the value of the **IFS** variable are used to split the line into words using the same rules the shell uses for expansion. |
| ```readarray``` | Format:<br>```readarray [-n count] [-O origin] [-s count] [-t] [-u fd] [-C callback] [-c quantum] [array]```<br><br>Read lines from the standard input into the indexed array variable *array*, or from file descriptor *fd* if the ```-u``` option is supplied. A synonym for *mapfile*. |
| ```source```  | Format:<br>```source filename```<br><br>A synonym for ```.```. |
| ```type```    | Format:<br>```type [-afptP] [name ...]```<br><br>For each *name*, indicate how it would be interpreted if used as a command name.<br><br>The return status is zero if all of the names are found, non-zero if any are not found. |
| ```typeset``` | Format:<br>```typeset [-afFgrxilnrtux] [-p] [name[=value] ...]```<br><br>The *typeset* command is supplied for compatibility with the Korn shell. It is a synonym for the *declare* builtin command. |
| ```ulimit```  | Format:<br>```ulimit [-abcdefilmnpqrstuvxHST] [limit]```<br><br>*ulimit* provides control over the resources available to processes started by the shell, on systems that allow such control.<br><br>If *limit* is given, and the ```-a``` option is not used, *limit* is the new value of the specified resource. The special *limit* values *hard*, *soft*, and *unlimited* stand for the current hard limit, the current soft limit, and no limit, respectively. A hard limit cannot be increased by a non-root user once it is set; a soft limit may be increased up to the value of the hard limit. Otherwise, the current value of the soft limit for the specified resource is printed, unless the ```-H``` option is supplied.<br><br>When setting new limits, if neither ```-H``` nor ```-S``` is supplied, both the hard and soft limits are set. If no option is given, then ```-f``` is assumed.<br><br>The return status is zero unless an invalid option or argument is supplied, or an error occurs while setting a new limit.<br><br>```ulimit -a```<br>```core file size          (blocks, -c) 0```<br>```data seg size           (kbytes, -d) unlimited```<br>```scheduling priority             (-e) 0```<br>```...``` |
| ```unalias``` | Format:<br>```unalias [-a] [name ...]```<br><br>Remove each *name* from the list of aliases. If ```-a``` is supplied, all aliases are removed. Also refer to [Aliases](#aliases). |

<p/>

## Modifying Shell Behavior

### The *set* Builtin

The shell builtin **set** allows you to change the values of shell options and set the **positional parameters**, or to display the names and values of shell variables.

***Formats:***

```
set [--abefhkmnptuvxBCEHPT] [-o option-name] [argument ...]
set [+abefhkmnptuvxBCEHPT] [+o option-name] [argument ...]
```

If no options or arguments are supplied, **set** displays the names and values of all shell variables and functions, sorted according to the current locale, in a format that may be reused as input for setting or resetting the currently-set variables. Read-only variables cannot be reset. In POSIX mode, only shell variables are listed.

When options are supplied, they set or unset shell attributes. Options, if specified, have the following meanings:

| Options | Description |
| :-----: | :---------- |
| ```-a``` | Mark variables and function which are modified or created for export to the environment of subsequent commands. |
| ```-b``` | Cause the status of terminated background jobs to be reported immediately, rather than before printing the next primary prompt. |
| ```-e``` | Exit immediately if a pipeline (see [Pipelines](#pipelines)), which may consist of a single simple command (see [Simple Commands](#simple-commands)), a list (see [Lists](#lists-of-commands)), or a compound command (see [Compound Commands](#compound-commands)) returns a non-zero status. The shell does not exit if the command that fails is part of the command list immediately following a **while** or **until** keyword, part of the test in an **if** statement, part of any command executed in a ```&&``` or ```||``` list except the command following the final ```&&``` or ```||```, any command in a pipeline but the last, or if the command's return status is being inverted with ```!```. If a compound command other than a subshell returns a non-zero status because a command failed while ```-e``` was being ignored, the shell does not exit. A trap on **ERR**, if set, is executed before the shell exits.<br><br>This option applies to the shell environment and each subshell environment separately (see [Command Execution Environment](#command-execution-environment)), and may cause subshells to exit before executing all the commands in the subshell.<br><br>If a compound command or shell function executes in a context where ```-e``` is being ignored, none of the commands executed within the compound command or function body will be affected by the ```-e``` setting, even if ```-e``` is set and a command returns a failure status. If a compound command or shell function sets ```-e``` while executing in a context where ```-e``` is ignored, that setting will not have any effect until the compound command or the command containing the function call completes. |
| ```-f``` | Disable filename expansion (globbing). |
| ```-h``` | Locate and remember (hash) commands as they are looked up for execution. This option is enabled by default. |
| ```-k``` | All arguments in the form of assignment statements are placed in the environment for a command, not just those that precede the command name. |
| ```-m``` | Job control is enabled. All processes run in a separate process group. When a background job completes, the shell prints a line containing its exit status. |
| ```-n``` | Read commands but do not execute them; this may be used to check a script for syntax errors. This option is ignored by interactive shells. |
| ```-p``` | Turn on privileged mode. In this mode, the ```$BASH_ENV``` and ```$ENV``` files are not processed, shell functions are not inherited from the environment, and the **SHELLOPTS**, **BASHOPTS**, **CDPATH** and **GLOBIGNORE** variables, if they appear in the environment, are ignored. If the shell is started with the effective user (group) id not equal to the real user (group) id, and the ```-p``` option is not supplied, these actions are taken and the effective user id is set to the real user id. If the ```-p``` option is supplied at startup, the effective user id is not reset. Turning this option off causes the effective user and group ids to be set to the real user and group ids. |
| ```-t``` | Exit after reading and executing one command. |
| ```-u``` | Treat unset variables and parameters other than the special parameters ```@``` or ```*``` as an error when performing parameter expansion. An error message will be written to the standard error, and a noninteractive shell will exit. |
| ```-v``` | Print shell input lines as they are read. |
| ```-x``` | Print a trace of simple commands, **for** commands, **case** commands, **select** commands, and arithmetic for commands and their arguments or associated word lists after they are expanded and before they are executed. The value of the **PS4** variable is expanded and the resultant value is printed before the command and its expanded arguments. |
| ```-B``` | The shell will perform **brace expansion**. This option is on by default. |
| ```-C``` | Prevent output redirection using ```>```, ```>&```, and ```<>``` from overwriting existing files. |
| ```-E``` | If set, any trap on **ERR** is inherited by shell functions, command substitutions, and commands executed in a subshell environment. The ERR trap is normally not inherited in such cases. |
| ```-H``` | Enable ```!``` style history substitution. This option is on by default for interactive shells. |
| ```-P``` | If set, do not resolve symbolic links when performing commands such as ```cd``` which change the current directory. The physical directory is used instead. By default, Bash follows the logical chain of directories when performing commands which change the current directory. |
| ```-T``` | If set, any trap on **DEBUG** and **RETURN** are inherited by shell functions, command substitutions, and commands executed in a subshell environment. The **DEBUG** and **RETURN** traps are normally not inherited in such cases. |
| ```--``` | If no arguments follow this option, then the positional parameters are unset. Otherwise, the positional parameters are set to the arguments, even if some of them begin with a ```-```. |
| ```-```  | Signal the end of options, cause all remaining arguments to be assigned to the positional parameters. The ```-x``` and ```-v``` options are turned off. If there are no arguments, the positional parameters remain unchanged. |

<p/>

The ```-o option-name``` sets the option corresponding to *option-name*:

| *option-name* | Description |
| :---------- | :---------- |
| ```allexport``` | Same as ```-a```. |
| ```braceexpand``` | Same as ```-B```. |
| ```emacs``` | Use an emacs-style line editing interface. This also affects the editing interface used for read ```-e```. |
| ```errexit``` | Same as ```-e```. |
| ```errtrace``` | Same as ```-E```. |
| ```functrace``` | Same as ```-T```. |
| ```hashall``` | Same as ```-h```. |
| ```histexpand``` | Same as ```-H```. |
| ```history``` | Enable command history. This option is **on** by default in **interactive shells**. |
| ```ignoreeof``` | An **interactive shell** will not exit upon reading **EOF**. |
| ```keyword``` | Same as ```-k```. |
| ```monitor``` | Same as ```-m```. |
| ```noclobber``` | Same as ```-C```. |
| ```noexec``` | Same as ```-n```. |
| ```noglob``` | Same as ```-f```. |
| ```nolog``` | Currently ignored. |
| ```notify``` | Same as ```-b```. |
| ```nounset``` | Same as ```-u```.
| ```onecmd``` | Same as ```-t```. |
| ```physical``` | Same as ```-P```. |
| ```pipefail``` | If set, the return value of a pipeline is the value of the last (rightmost) command to exit with a **non-zero** status, or **zero** if all commands in the pipeline exit successfully. This option is **disabled** by default. |
| ```posix``` | Change the behavior of Bash where the default operation differs from the posix standard to match the standard. This is intended to make Bash behave as a strict superset of that standard. |
| ```privileged``` | Same as ```-p```. |
| ```verbose``` | Same as ```-v```. |
| ```vi``` | Use a **vi**-style line editing interface. This also affects the editing interface used for read ```-e```. |
| ```xtrace``` | Same as ```-x```. |

<p/>

Using ```+``` rather than ```-``` causes these options to be turned off. The options can also be used upon invocation of the shell. The current set of options may be found in ```$-```.

The remaining **N** arguments are positional parameters and are assigned, in order, to ```$1, $2, ... $N```. The special parameter ```#``` is set to **N**.

The return status is always **zero** unless an invalid option is supplied.

***Examples:***

```
chenwx@chenwx ~ $ set | more
BASH=/bin/bash
BASHOPTS=checkwinsize:cmdhist:complete_fullquote:expand_aliases:extglob:extquote:force_fignore:interactive_comments:progcomp:promptvars:sourcepath
BASH_ALIASES=()
BASH_ARGC=()
BASH_ARGV=()
BASH_CMDS=()
BASH_COMPLETION_COMPAT_DIR=/etc/bash_completion.d
BASH_LINENO=()
BASH_REMATCH=()
BASH_SOURCE=()
BASH_VERSINFO=([0]="4" [1]="3" [2]="11" [3]="1" [4]="release" [5]="x86_64-pc-linux-gnu")
BASH_VERSION='4.3.11(1)-release'
CLUTTER_IM_MODULE=ibus
COLORTERM=gnome-terminal
...

chenwx@chenwx ~ $ echo $-
bhimBH
```

### The *shopt* Builtin

***Format:***

```
shopt [-pqsu] [-o] [optname ...]
```

The shell builtin **shopt** allows you to change additional shell optional behavior. Toggle the values of settings controlling optional shell behavior. The settings can be either those listed below, or, if the ```-o``` option is used, those available with the ```-o``` option to the **set** builtin command (see [The *set* Builtin](#the-em-set-em-builtin)).

| Options | Description |
| :------ | :---------- |
| ```-p``` | With no options, or with the ```-p``` option, a list of all settable options is displayed, with an indication of whether or not each is set. The ```-p``` option causes output to be displayed in a form that may be reused as input. |
| ```-q``` | Suppresses normal output; the return status indicates whether the *optname* is set or unset. If multiple *optname* arguments are given with ```-q```, the return status is **zero** if all optnames are enabled; **nonzero** otherwise. |
| ```-s``` | Enable (set) each *optname*. |
| ```-u``` | Disable (unset) each *optname*. |
| ```-o``` | Restricts the values of *optname* to be those defined for the ```-o``` option to the **set** builtin (see [The *set* Builtin](#the-em-set-em-builtin)). |

<p/>

If either ```-s``` or ```-u``` is used with no *optname* arguments, *shopt* shows only those options which are set or unset, respectively.

Unless otherwise noted, the **shopt** options are disabled (off) by default.

The return status when listing options is **zero** if all *optnames* are enabled, **nonzero** otherwise. When setting or unsetting options, the return status is **zero** unless an *optname* is not a valid shell option.

The list of **shopt** options is:

| *optname* | Description |
| :-------- | :---------- |
| ```autocd``` | If set, a command name that is the name of a directory is executed as if it were the argument to the **cd** command. This option is only used by **interactive shells**. |
| ```cdable_vars``` | If this is set, an argument to the **cd** builtin command that is not a directory is assumed to be the name of a variable whose value is the directory to change to. |
| ```cdspell``` | If set, minor errors in the spelling of a directory component in a **cd** command will be corrected. The errors checked for are transposed characters, a missing character, and a character too many. If a correction is found, the corrected path is printed, and the command proceeds. This option is only used by **interactive shells**. |
| ```checkhash``` | If this is set, Bash checks that a command found in the hash table exists before trying to execute it. If a hashed command no longer exists, a normal path search is performed. |
| ```checkjobs``` | If set, Bash lists the status of any stopped and running jobs before exiting an interactive shell. If any jobs are running, this causes the exit to be deferred until a second exit is attempted without an intervening command (see [Job Control](#job-control)). The shell always postpones exiting if any jobs are stopped. |
| ```checkwinsize``` | If set, Bash checks the window size after each command and, if necessary, updates the values of **LINES** and **COLUMNS**. |
| ```cmdhist``` | If set, Bash attempts to save all lines of a multiple-line command in the same history entry. This allows easy re-editing of multi-line commands. |
| ```compat31``` | If set, Bash changes its behavior to that of version 3.1 with respect to quoted arguments to the conditional command's ```=~``` operator and with respect to locale-specific string comparison when using the ```[[``` conditional command's ```<``` and ```>``` operators. Bash versions prior to bash-4.1 use ASCII collation and **strcmp**(3); bash-4.1 and later use the current locale's collation sequence and **strcoll**(3). |
| ```compat32``` | If set, Bash changes its behavior to that of version 3.2 with respect to locale-specific string comparison when using the ```[[``` conditional command's ```<``` and ```>``` operators (see previous item). |
| ```compat40``` | If set, Bash changes its behavior to that of version 4.0 with respect to locale-specific string comparison when using the ```[[``` conditional command's ```<``` and ```>``` operators (see description of **compat31**) and the effect of interrupting a command list. Bash versions 4.0 and later interrupt the list as if the shell received the interrupt; previous versions continue with the next command in the list. |
| ```compat41``` | If set, Bash, when in POSIX mode, treats a single quote in a doublequoted parameter expansion as a special character. The single quotes must match (an even number) and the characters between the single quotes are considered quoted. This is the behavior of POSIX mode through version 4.1. The default Bash behavior remains as in previous versions. |
| ```compat42``` | If set, Bash does not process the replacement string in the pattern substitution word expansion using quote removal. |
| ```complete_fullquote``` | If set, Bash quotes all shell metacharacters in filenames and directory names when performing completion. If not set, Bash removes metacharacters such as the dollar sign from the set of characters that will be quoted in completed filenames when these metacharacters appear in shell variable references in words to be completed. This means that dollar signs in variable names that expand to directories will not be quoted; however, any dollar signs appearing in filenames will not be quoted, either. This is active only when bash is using backslashes to quote completed filenames. This variable is set by default, which is the default Bash behavior in versions through 4.2. |
| ```direxpand``` | If set, Bash replaces directory names with the results of word expansion when performing filename completion. This changes the contents of the readline editing buffer. If not set, Bash attempts to preserve what the user typed. |
| ```dirspell``` | If set, Bash attempts spelling correction on directory names during word completion if the directory name initially supplied does not exist. |
| ```dotglob``` | If set, Bash includes filenames beginning with a ```.``` in the results of filename expansion. |
| ```execfail``` | If this is set, a non-interactive shell will not exit if it cannot execute the file specified as an argument to the **exec** builtin command. An interactive shell does not exit if **exec** fails. |
| ```expand_aliases``` | If set, aliases are expanded as described under [Aliases](#aliases). This option is enabled by default for interactive shells. |
| ```extdebug``` | If set, behavior intended for use by debuggers is enabled:<br><br>1. The ```-F``` option to the **declare** builtin (see [Bash Builtins](#bash-builtin-commands)) displays the source file name and line number corresponding to each function name supplied as an argument.<br><br>2. If the command run by the **DEBUG** trap returns a **non-zero** value, the next command is skipped and not executed.<br><br>3. If the command run by the **DEBUG** trap returns a value of **2**, and the shell is executing in a subroutine (a shell function or a shell script executed by the ```.``` or ```source``` builtins), a call to **return** is simulated.<br><br>4. **BASH_ARGC** and **BASH_ARGV** are updated as described in their descriptions (see [Bash Variables](#bash-variables)).<br><br>5. Function tracing is enabled: command substitution, shell functions, and subshells invoked with ```( command )``` inherit the **DEBUG** and **RETURN** traps.<br><br>6. Error tracing is enabled: command substitution, shell functions, and subshells invoked with ```( command )``` inherit the **ERR** trap. |
| ```extglob``` | If set, the extended pattern matching features described above (see [Pattern Matching](#pattern-matching)) are enabled. |
| ```extquote``` | If set, ```$'string'``` and ```$"string"``` quoting is performed within ```${parameter}``` expansions enclosed in double quotes. This option is enabled by default. |
| ```failglob``` | If set, patterns which fail to match filenames during filename expansion result in an expansion error. |
| ```force_fignore``` | If set, the suffixes specified by the **FIGNORE** shell variable cause words to be ignored when performing word completion even if the ignored words are the only possible completions. See [Bash Variables](#bash-variables) for a description of FIGNORE. This option is enabled by default. |
| ```globasciiranges``` | If set, range expressions used in pattern matching bracket expressions (see [Pattern Matching](#pattern-matching)) behave as if in the traditional **C** locale when performing comparisons. That is, the current locale's collating sequence is not taken into account, so ```b``` will not collate between ```A``` and ```B```, and upper-case and lowercase ASCII characters will collate together. |
| ```globstar``` | If set, the pattern ```**``` used in a filename expansion context will match all files and zero or more directories and subdirectories. If the pattern is followed by a ```/```, only directories and subdirectories match. |
| ```gnu_errfmt``` | If set, shell error messages are written in the standard gnu error message format. |
| ```histappend``` | If set, the history list is appended to the file named by the value of the **HISTFILE** variable when the shell exits, rather than overwriting the file. |
| ```histreedit``` | If set, and Readline is being used, a user is given the opportunity to re-edit a failed history substitution. |
| ```histverify``` | If set, and Readline is being used, the results of history substitution are not immediately passed to the shell parser. Instead, the resulting line is loaded into the Readline editing buffer, allowing further modification. |
| ```hostcomplete``` | If set, and Readline is being used, Bash will attempt to perform hostname completion when a word containing a ```@``` is being completed (see [Commands For Completion](#commands-for-completion)). This option is enabled by default. |
| ```huponexit``` | If set, Bash will send **SIGHUP** to all jobs when an interactive login shell exits (see [Signals](#signals). |
| ```interactive_comments``` | Allow a word beginning with ‘#’ to cause that word and all remaining characters on that line to be ignored in an interactive shell. This option is enabled by default. |
| ```lastpipe``` | If set, and job control is not active, the shell runs the last command of a pipeline not executed in the background in the current shell environment. |
| ```lithist``` | If enabled, and the **cmdhist** option is enabled, multi-line commands are saved to the history with embedded newlines rather than using semicolon separators where possible. |
| ```login_shell``` | The shell sets this option if it is started as a login shell (see [Invoking Bash](#invoking-bash)). The value may not be changed. |
| ```mailwarn``` | If set, and a file that Bash is checking for mail has been accessed since the last time it was checked, the message ***The mail in mailfile has been read*** is displayed. |
| ```no_empty_cmd_completion``` | If set, and Readline is being used, Bash will not attempt to search the **PATH** for possible completions when completion is attempted on an empty line. |
| ```nocaseglob``` | If set, Bash matches filenames in a case-insensitive fashion when performing filename expansion. |
| ```nocasematch``` | If set, Bash matches patterns in a case-insensitive fashion when performing matching while executing case or ```[[``` conditional commands. |
| ```nullglob``` | If set, Bash allows filename patterns which match no files to expand to a null string, rather than themselves. |
| ```progcomp``` | If set, the programmable completion facilities (see [Programmable Completion](#programmable-completion)) are enabled. This option is enabled by default. |
| ```promptvars``` | If set, prompt strings undergo **parameter expansion**, **command substitution**, **arithmetic expansion**, and **quote removal** after being expanded as described in [Controlling the Prompt](#controlling-the-prompt). This option is enabled by default. |
| ```restricted_shell``` | The shell sets this option if it is started in restricted mode (see [The Restricted Shell](#the-restricted-shell)). The value may not be changed. This is not reset when the startup files are executed, allowing the startup files to discover whether or not a shell is restricted. |
| ```shift_verbose``` | If this is set, the **shift** builtin prints an error message when the shift count exceeds the number of positional parameters. |
| ```sourcepath``` | If set, the **source** builtin uses the value of **PATH** to find the directory containing the file supplied as an argument. This option is enabled by default. |
| ```xpg_echo``` | If set, the **echo** builtin expands backslash-escape sequences by default. |

<p/>

The return status when listing options is **zero** if all *optnames* are enabled, **nonzero** otherwise. When setting or unsetting options, the return status is **zero** unless an *optname* is not a valid shell option.

***Examples:***

```
chenwx@chenwx ~ $ shopt -p
shopt -u autocd
shopt -u cdable_vars
shopt -u cdspell
shopt -u checkhash
shopt -u checkjobs
shopt -s checkwinsize
shopt -s cmdhist
shopt -u compat31
shopt -u compat32
shopt -u compat40
shopt -u compat41
shopt -u compat42
shopt -s complete_fullquote
shopt -u direxpand
shopt -u dirspell
shopt -u dotglob
shopt -u execfail
shopt -s expand_aliases
shopt -u extdebug
shopt -s extglob
shopt -s extquote
shopt -u failglob
shopt -s force_fignore
shopt -u globstar
shopt -u globasciiranges
shopt -u gnu_errfmt
shopt -u histappend
shopt -u histreedit
shopt -u histverify
shopt -u hostcomplete
shopt -u huponexit
shopt -s interactive_comments
shopt -u lastpipe
shopt -u lithist
shopt -u login_shell
shopt -u mailwarn
shopt -u no_empty_cmd_completion
shopt -u nocaseglob
shopt -u nocasematch
shopt -u nullglob
shopt -s progcomp
shopt -s promptvars
shopt -u restricted_shell
shopt -u shift_verbose
shopt -s sourcepath
shopt -u xpg_echo

chenwx@chenwx ~ $ shopt -sp
shopt -s checkwinsize
shopt -s cmdhist
shopt -s complete_fullquote
shopt -s expand_aliases
shopt -s extglob
shopt -s extquote
shopt -s force_fignore
shopt -s interactive_comments
shopt -s progcomp
shopt -s promptvars
shopt -s sourcepath

chenwx@chenwx ~ $ shopt -p autocd cdspell
shopt -u autocd
shopt -u cdspell

chenwx@chenwx ~ $ shopt autocd cdspell
autocd         	off
cdspell        	off
```

## Special Builtins

For historical reasons, the POSIX standard has classified several builtin commands as *special*. When Bash is executing in **POSIX mode**, the special builtins differ from other builtin commands in three respects:

1. Special builtins are found before shell functions during command lookup.
2. If a special builtin returns an error status, a non-interactive shell exits.
3. Assignment statements preceding the command stay in effect in the shell environment after the command completes.

When Bash is not executing in POSIX mode, these builtins behave no differently than the rest of the Bash builtin commands.

These are the POSIX special builtins:

```
break : . continue eval exec exit export readonly return set shift trap unset
```

# Shell Variables

Bash automatically assigns default values to a number of variables.

## Bourne Shell Variables

Bash uses certain shell variables in the same way as the **Bourne shell**. In some cases, Bash assigns a default value to the variable.

| Variables | Description |
| :-------- | :---------- |
| **CDPATH** | A colon-separated list of directories used as a search path for the **cd** builtin command. |
| **HOME** | The current user's home directory; the default for the **cd** builtin command. The value of this variable is also used by [tilde expansion](#tilde-expansion). |
| **IFS** | A list of characters that separate fields; used when the shell splits words as part of expansion. |
| **MAIL** | If this parameter is set to a filename or directory name and the **MAILPATH** variable is not set, Bash informs the user of the arrival of mail in the specified file or Maildir-format directory. |
| **MAILPATH** | A colon-separated list of filenames which the shell periodically checks for new mail. Each list entry can specify the message that is printed when new mail arrives in the mail file by separating the filename from the message with a ```?```. When used in the text of the message, ```$_``` expands to the name of the current mail file. |
| **OPTARG** | The value of the last option argument processed by the **getopts** builtin. |
| **OPTIND** | The index of the last option argument processed by the **getopts** builtin. |
| **PATH** | A colon-separated list of directories in which the shell looks for commands. A zero-length (null) directory name in the value of **PATH** indicates the current directory. A null directory name may appear as two adjacent colons, or as an initial or trailing colon. |
| **PS1** | The primary prompt string. The default value is ```\s-\v\$ ```, see [Controlling the Prompt](#controlling-the-prompt). |
| **PS2** | The secondary prompt string. The default value is ```> ```, see [Controlling the Prompt](#controlling-the-prompt). |

<p/>

## Bash Variables

These variables are set or used by Bash, but other shells do not normally treat them specially.

A few variables used by Bash are described in different chapters: variables for controlling the job control facilities (see [Job Control Variables](#job-control-variables)).

| Variables | Readonly? | Description |
| :-------- | :-------: | :---------- |
| **BASH** | No | The full pathname used to execute the current instance of Bash. |
| **BASHOPTS** | Yes | A colon-separated list of enabled shell options. Each word in the list is a valid argument for the -s option to the *shopt* builtin command. The options appearing in **BASHOPTS** are those reported as ```on``` by **shopt** builtin. If this variable is in the environment when Bash starts up, each shell option in the list will be enabled before reading any startup files. |
| **BASHPID** | No | Expands to the process ID of the current Bash process. This differs from ```$$``` under certain circumstances, such as subshells that do not require Bash to be re-initialized. |
| **BASH_ALIASES** | No | An associative array variable whose members correspond to the internal list of aliases as maintained by the **alias** builtin. Elements added to this array appear in the alias list; unsetting array elements cause aliases to be removed from the alias list. |
| **BASH_ARGC** | No | An array variable whose values are the number of parameters in each frame of the current bash execution call stack. The number of parameters to the current subroutine (shell function or script executed with ```.``` or ```source```) is at the top of the stack. When a subroutine is executed, the number of parameters passed is pushed onto **BASH_ARGC**. The shell sets **BASH_ARGC** only when in extended debugging mode. |
| **BASH_ARGV** | No | An array variable containing all of the parameters in the current bash execution call stack. The final parameter of the last subroutine call is at the top of the stack; the first parameter of the initial call is at the bottom. When a subroutine is executed, the parameters supplied are pushed onto **BASH_ARGV**. The shell sets **BASH_ARGV** only when in extended debugging mode. |
| **BASH_CMDS** | No | An associative array variable whose members correspond to the internal hash table of commands as maintained by the **hash** builtin. Elements added to this array appear in the hash table; unsetting array elements cause commands to be removed from the hash table. |
| **BASH_COMMAND** | No | The command currently being executed or about to be executed, unless the shell is executing a command as the result of a trap, in which case it is the command executing at the time of the trap. |
| **BASH_COMPAT** | No | The value is used to set the shell's compatibility level. The value may be a decimal number (e.g., 4.2) or an integer (e.g., 42) corresponding to the desired compatibility level. If **BASH_COMPAT** is unset or set to the empty string, the compatibility level is set to the default for the current version. If **BASH_COMPAT** is set to a value that is not one of the valid compatibility levels, the shell prints an error message and sets the compatibility level to the default for the current version. The valid compatibility levels correspond to the compatibility options accepted by the **shopt** builtin described in [The *shopt* Builtin](#the-em-shopt-em-builtin) (for example, compat42 means that 4.2 and 42 are valid values). The current version is also a valid value. |
| **BASH_ENV** | No | If this variable is set when Bash is invoked to execute a shell script, its value is expanded and used as the name of a startup file to read before executing the script. |
| **BASH_EXECUTION_STRING** | No | The command argument to the ```-c``` invocation option. |
| **BASH_LINENO** | No | An array variable whose members are the line numbers in source files where each corresponding member of **FUNCNAME** was invoked. **${BASH_LINENO[$i]}** is the line number in the source file (**${BASH_SOURCE[$i+1]}**) where **${FUNCNAME[$i]}** was called (or **${BASH_LINENO[$i-1]}** if referenced within another shell function). Use **LINENO** to obtain the current line number. |
| **BASH_REMATCH** | Yes | An array variable whose members are assigned by the ```=~``` binary operator to the ```[[``` conditional command. The element with index 0 is the portion of the string matching the entire regular expression. The element with index *n* is the portion of the string matching the *n*th parenthesized subexpression. |
| **BASH_SOURCE** | No | An array variable whose members are the source filenames where the corresponding shell function names in the **FUNCNAME** array variable are defined. The shell function **${FUNCNAME[$i]}** is defined in the file **${BASH_SOURCE[$i]}** and called from **${BASH_SOURCE[$i+1]}**. |
| **BASH_SUBSHELL** | No | Incremented by one within each subshell or subshell environment when the shell begins executing in that environment. The initial value is **0**. |
| **BASH_VERSINFO** | Yes | A readonly array variable whose members hold version information for this instance of Bash. The values assigned to the array members are as follows:<br>**BASH_VERSINFO[0]**: The major version number (the release).<br>**BASH_VERSINFO[1]**:The minor version number (the version).<br>**BASH_VERSINFO[2]**:The patch level.<br>**BASH_VERSINFO[3]**:The build version.<br>**BASH_VERSINFO[4]**:The release status (e.g., beta1).<br>**BASH_VERSINFO[5]**:The value of **MACHTYPE**. |
| **BASH_VERSION** | No | The version number of the current instance of Bash. |
| **BASH_XTRACEFD** | No | If set to an integer corresponding to a valid file descriptor, Bash will write the trace output generated when ```set -x``` is enabled to that file descriptor. This allows tracing output to be separated from diagnostic and error messages. The file descriptor is closed when **BASH_XTRACEFD** is unset or assigned a new value. Unsetting **BASH_XTRACEFD** or assigning it the empty string causes the trace output to be sent to the standard error. Note that setting **BASH_XTRACEFD** to **2** (the standard error file descriptor) and then unsetting it will result in the standard error being closed. |
| **CHILD_MAX** | No | Set the number of exited child status values for the shell to remember. Bash will not allow this value to be decreased below a posix-mandated minimum, and there is a maximum value (currently 8192) that this may not exceed. The minimum value is system-dependent. |
| **COLUMNS** | No | Used by the **select** command to determine the terminal width when printing selection lists. Automatically set if the checkwinsize option is enabled, or in an interactive shell upon receipt of a **SIGWINCH**. |
| **COMP_CWORD** | No | An index into **${COMP_WORDS}** of the word containing the current cursor position. This variable is available only in shell functions invoked by the programmable completion facilities. |
| **COMP_LINE** | No | The current command line. This variable is available only in shell functions and external commands invoked by the programmable completion facilities. |
| **COMP_POINT** | No | The index of the current cursor position relative to the beginning of the current command. If the current cursor position is at the end of the current command, the value of this variable is equal to **${#COMP_LINE}**. This variable is available only in shell functions and external commands invoked by the programmable completion facilities. |
| **COMP_TYPE** | No | Set to an integer value corresponding to the type of completion attempted that caused a completion function to be called: TAB, for normal completion, ```?```, for listing completions after successive tabs, ```!```, for listing alternatives on partial word completion, ```@```, to list completions if the word is not unmodified, or ```%```, for menu completion. This variable is available only in shell functions and external commands invoked by the programmable completion facilities. |
| **COMP_KEY** | No | The key (or final key of a key sequence) used to invoke the current completion function. |
| **COMP_WORDBREAKS** | No | The set of characters that the Readline library treats as word separators when performing word completion. If **COMP_WORDBREAKS** is unset, it loses its special properties, even if it is subsequently reset. |
| **COMP_WORDS** | No | An array variable consisting of the individual words in the current command line. The line is split into words as Readline would split it, using **COMP_WORDBREAKS** as described above. This variable is available only in shell functions invoked by the programmable completion facilities. |
| **COMPREPLY** | No | An array variable from which Bash reads the possible completions generated by a shell function invoked by the programmable completion facility. Each array element contains one possible completion. |
| **COPROC** | No | An array variable created to hold the file descriptors for output from and input to an unnamed coprocess. |
| **DIRSTACK** | No | An array variable containing the current contents of the directory stack. Directories appear in the stack in the order they are displayed by the *dirs* builtin. Assigning to members of this array variable may be used to modify directories already in the stack, but the pushd and popd builtins must be used to add and remove directories. Assignment to this variable will not change the current directory. If **DIRSTACK** is unset, it loses its special properties, even if it is subsequently reset. |
| **EMACS** | No | If Bash finds this variable in the environment when the shell starts with value ```t```, it assumes that the shell is running in an Emacs shell buffer and disables line editing. |
| **ENV** | No | Similar to **BASH_ENV**; used when the shell is invoked in POSIX Mode. |
| **EUID** | Yes | The numeric effective user id of the current user. |
| **FCEDIT** | No |  The editor used as a default by the ```-e``` option to the *fc* builtin command. |
| **FIGNORE** | No |  A colon-separated list of suffixes to ignore when performing filename completion. A filename whose suffix matches one of the entries in **FIGNORE** is excluded from the list of matched filenames. A sample value is ```.o:~```. |
| **FUNCNAME** | No |  An array variable containing the names of all shell functions currently in the execution call stack. The element with index 0 is the name of any currently executing shell function. The bottom-most element (the one with the highest index) is **main**. This variable exists only when a shell function is executing. Assignments to **FUNCNAME** have no effect and return an error status. If **FUNCNAME** is unset, it loses its special properties, even if it is subsequently reset.<br><br>This variable can be used with **BASH_LINENO** and **BASH_SOURCE**. Each element of **FUNCNAME** has corresponding elements in **BASH_LINENO** and **BASH_SOURCE** to describe the call stack. For instance, **${FUNCNAME[$i]}** was called from the file **${BASH_SOURCE[$i+1]}** at line number **${BASH_LINENO[$i]}**. The *caller* builtin displays the current call stack using this information. |
| **FUNCNEST** | No |  If set to a numeric value greater than 0, defines a maximum function nesting level. Function invocations that exceed this nesting level will cause the current command to abort. |
| **GLOBIGNORE** | No |  A colon-separated list of patterns defining the set of filenames to be ignored by **filename expansion**. If a filename matched by a filename expansion pattern also matches one of the patterns in **GLOBIGNORE**, it is removed from the list of matches. |
| **GROUPS** | No |  An array variable containing the list of groups of which the current user is a member. Assignments to **GROUPS** have no effect and return an error status. If **GROUPS** is unset, it loses its special properties, even if it is subsequently reset. |
| **histchars** | No |  Up to three characters which control history expansion, quick substitution, and tokenization.<br><br>The first character is the history expansion character, that is, the character which signifies the start of a history expansion, normally ```!```.<br><br>The second character is the character which signifies ```quick substitution``` when seen as the first character on a line, normally ```^```.<br><br>The optional third character is the character which indicates that the remainder of the line is a comment when found as the first character of a word, usually ```#```. The history comment character causes history substitution to be skipped for the remaining words on the line. It does not necessarily cause the shell parser to treat the rest of the line as a comment. |
| **HISTCMD** | No |  The history number, or index in the history list, of the current command. If **HISTCMD** is unset, it loses its special properties, even if it is subsequently reset. |
| **HISTCONTROL** | No |  Refer to [Bash History Facilities](#bash-history-facilities). |
| **HISTFILE** | No |  Refer to [Bash History Facilities](#bash-history-facilities). |
| **HISTFILESIZE** | No |  Refer to [Bash History Facilities](#bash-history-facilities). |
| **HISTIGNORE** | No |  Refer to [Bash History Facilities](#bash-history-facilities). |
| **HISTSIZE** | No |  Refer to [Bash History Facilities](#bash-history-facilities). |
| **HISTTIMEFORMAT** | No |  Refer to [Bash History Facilities](#bash-history-facilities). |
| **HOSTFILE** | No |  Contains the name of a file in the same format as */etc/hosts* that should be read when the shell needs to complete a hostname. The list of possible hostname completions may be changed while the shell is running; the next time hostname completion is attempted after the value is changed, Bash adds the contents of the new file to the existing list. If **HOSTFILE** is set, but has no value, or does not name a readable file, Bash attempts to read */etc/hosts* to obtain the list of possible hostname completions. When **HOSTFILE** is unset, the hostname list is cleared. |
| **HOSTNAME** | No |  The name of the current host. |
| **HOSTTYPE** | No |  A string describing the machine Bash is running on. |
| **IGNOREEOF** | No |  Controls the action of the shell on receipt of an **EOF** character as the sole input. If set, the value denotes the number of consecutive **EOF** characters that can be read as the first character on an input line before the shell will exit. If the variable exists but does not have a numeric value (or has no value) then the default is **10**. If the variable does not exist, then **EOF** signifies the end of input to the shell. This is only in effect for **interactive shells**. |
| **INPUTRC** | No |  The name of the Readline initialization file, overriding the default of ```~/.inputrc```. |
| **LANG** | No |  Used to determine the locale category for any category not specifically selected with a variable starting with **LC_**. |
| **LC_ALL** | No |  This variable overrides the value of **LANG** and any other **LC_** variable specifying a locale category. |
| **LC_COLLATE** | No |  This variable determines the collation order used when sorting the results of filename expansion, and determines the behavior of range expressions, equivalence classes, and collating sequences within filename expansion and pattern matching. |
| **LC_CTYPE** | No |  This variable determines the interpretation of characters and the behavior of character classes within filename expansion and pattern matching. |
| **LC_MESSAGES** | No |  This variable determines the locale used to translate double-quoted strings preceded by a ```$```. |
| **LC_NUMERIC** | No |  This variable determines the locale category used for number formatting. |
| **LINENO** | No |  The line number in the script or shell function currently executing. |
| **LINES** | No |  Used by the **select** command to determine the column length for printing selection lists. Automatically set if the ```checkwinsize``` option is enabled by the **shopt** builtin, or in an interactive shell upon receipt of a **SIGWINCH**. |
| **MACHTYPE** | No |  A string that fully describes the system type on which Bash is executing, in the standard gnu *cpu-company-system* format. |
| **MAILCHECK** | No |  How often (in seconds) that the shell should check for mail in the files specified in the **MAILPATH** or **MAIL** variables. The default is **60 seconds**. When it is time to check for mail, the shell does so before displaying the primary prompt. If this variable is unset, or set to a value that is not a number greater than or equal to zero, the shell disables mail checking. |
| **MAPFILE** | No |  An array variable created to hold the text read by the **mapfile** builtin when no variable name is supplied. |
| **OLDPWD** | No |  The previous working directory as set by the **cd** builtin. |
| **OPTERR** | No |  If set to the value **1**, Bash displays error messages generated by the **getopts** builtin command. |
| **OSTYPE** | No |  A string describing the operating system Bash is running on. |
| **PIPESTATUS** | No |  An array variable containing a list of exit status values from the processes in the most-recently-executed foreground pipeline (which may contain only a single command). |
| **POSIXLY_CORRECT** | No |  If this variable is in the environment when Bash starts, the shell enters POSIX mode before reading the startup files, as if the ```--posix``` invocation option had been supplied. If it is set while the shell is running, Bash enables POSIX mode, as if the command ```set -o posix``` had been executed. |
| **PPID** | Yes | The process id of the shell’s parent process. |
| **PROMPT_COMMAND** | No |  If set, the value is interpreted as a command to execute before the printing of each primary prompt **$PS1**. |
| **PROMPT_DIRTRIM** | No |  If set to a number greater than zero, the value is used as the number of trailing directory components to retain when expanding the ```\w``` and ```\W``` prompt string escapes. Characters removed are replaced with an ellipsis. |
| **PS3** | No |  The value of this variable is used as the prompt for the select command. If this variable is not set, the *select* command prompts with ```#? ```. |
| **PS4** | No |  The value is the prompt printed before the command line is echoed when the ```-x``` option is *set* builtin. The first character of PS4 is replicated multiple times, as necessary, to indicate multiple levels of indirection. The default is ```+ ```. |
| **PWD** | No |  The current working directory as set by the *cd* builtin. |
| **RANDOM** | No |  Each time this parameter is referenced, a random integer **between 0 and 32767** is generated. Assigning a value to this variable seeds the random number generator. |
| **READLINE_LINE** | No |  The contents of the Readline line buffer, for use with ```bind -x```. |
| **READLINE_POINT** | No |  The position of the insertion point in the Readline line buffer, for use with ```bind -x```. |
| **REPLY** | No |  The default variable for the **read** builtin. |
| **SECONDS** | No |  This variable expands to the number of seconds since the shell was started. Assignment to this variable resets the count to the value assigned, and the expanded value becomes the value assigned plus the number of seconds since the assignment. |
| **SHELL** | No |  The full pathname to the shell is kept in this environment variable. If it is not set when the shell starts, Bash assigns to it the full pathname of the current user's login shell. |
| **SHELLOPTS** | Yes | A colon-separated list of enabled shell options. Each word in the list is a valid argument for the ```-o``` option to the **set** builtin command. The options appearing in **SHELLOPTS** are those reported as ```on``` by ```set -o```. If this variable is in the environment when Bash starts up, each shell option in the list will be enabled before reading any startup files. |
| **SHLVL** | No |  Incremented by one each time a new instance of Bash is started. This is intended to be a count of how deeply your Bash shells are nested. |
| **TIMEFORMAT** | No |  The value of this parameter is used as a format string specifying how the timing information for pipelines prefixed with the *time* reserved word should be displayed.<br><br>If this variable is not set, Bash acts as if it had the value ```$'\nreal\t%3lR\nuser\t%3lU\nsys\t%3lS'```.<br><br>If the value is null, no timing information is displayed. A trailing newline is added when the format string is displayed. |
| **TMOUT** | No |  If set to a value greater than zero, **TMOUT** is treated as the default timeout for the **read** builtin. The **select** command terminates if input does not arrive after **TMOUT** seconds when input is coming from a terminal.<br><br>In an interactive shell, the value is interpreted as the number of seconds to wait for a line of input after issuing the primary prompt. Bash terminates after waiting for that number of seconds if a complete line of input does not arrive. |
| **TMPDIR** | No |  If set, Bash uses its value as the name of a directory in which Bash creates temporary files for the shell's use. |
| **UID** | Yes | The numeric real user id of the current user. |

<p/>

# Bash Features

## Invoking Bash

***Format #1:***

```
bash [long-opt] [-ir] [-abefhkmnptuvxdBCDHP] [-o option] [-O shopt_option] [argument ...]
```

***Format #2:***

```
bash [long-opt] -s [-abefhkmnptuvxdBCDHP] [-o option] [-O shopt_option] [argument ...]
```

***Format #3:***

```
bash [long-opt] [-abefhkmnptuvxdBCDHP] [-o option] [-O shopt_option] -c string [argument ...]
```

All of the single-character options used with the **set** builtin can be used as options when the shell is invoked.

These options must appear on the command line before the single-character options to be recognized:

| long_opt | Description |
| :---------- | :---------- |
| ```--debugger``` | Arrange for the debugger profile to be executed before the shell starts. Turns on extended debugging mode (see [The *shopt* Builtin](#the-em-shopt-em-builtin) for a description of the ```extdebug``` option). |
| ```--dump-po-strings``` | A list of all double-quoted strings preceded by **$** is printed on the standard output in the GNU *gettext* PO (portable object) file format. Equivalent to ```-D``` except for the output format. |
| ```--dump-strings``` | Equivalent to ```-D```. |
| ```--init-file filename```<br>```--rcfile filename``` | Execute commands from *filename* (instead of ```~/.bashrc```) in an interactive shell. |
| ```--login``` | Equivalent to ```-l```. |
| ```--noprofile``` | Don't load the system-wide startup file ```/etc/profile``` or any of the personal initialization files ```~/.bash_profile```, ```~/.bash_login```, or ```~/.profile``` when Bash is invoked as a **login shell**. |
| ```--noediting``` | Do not use the GNU **Readline** library to read command lines when the shell is **interactive**. Refer to [Command Line Editing](#command-line-editing). |
| ```--norc``` | Don't read the ```~/.bashrc``` initialization file in an **interactive shell**. ***This is on by default if the shell is invoked as*** ```sh```. |
| ```--posix``` | Change the behavior of Bash where the default operation differs from the POSIX standard to match the standard. This is intended to make Bash behave as a strict superset of that standard. Refer to [Bash POSIX Mode](https://www.gnu.org/software/bash/manual/bash.html#Bash-POSIX-Mode). |
| ```--restricted``` | Make the shell a **restricted shell**. Refer to [The Restricted Shell](https://www.gnu.org/software/bash/manual/bash.html#The-Restricted-Shell). |
| ```--verbose``` | Equivalent to ```-v```. Print shell input lines as they're read. |
| ```--version``` | Show version information for this instance of Bash on the standard output and exit successfully. |
| ```--help``` | Display a usage message on standard output and exit successfully.<br><br>Type ```bash -c "help set"``` for more information about shell options.<br>Type ```bash -c help``` for more information about shell builtin commands. |

<p/>

There are several single-character options that may be supplied at invocation which are not available with the **set** builtin.

| single_character_opt | Description |
| :------------------- | :---------- |
| ```-s``` | If the ```-s``` option is present, or if no arguments remain after option processing, then commands are read from the **standard input**. This option allows the positional parameters to be set when invoking an **interactive shell**. |
| ```-c``` | If the ```-c``` option is present, then commands are read from *string*. If there are arguments after the *string*, they are assigned to the positional parameters, starting with **$0**.|
| ```-l``` | Make this shell act as if it had been directly invoked by login.<br><br>When the shell is interactive, this is equivalent to starting a login shell with ```exec -l bash```.<br><br>When the shell is not interactive, the login shell startup files will be executed.<br><br> ```exec bash -l``` or ```exec bash --login``` will replace the current shell with a Bash login shell. |
| ```-i``` | Force the shell to run **interactively**. |
| ```-r``` | Make the shell a **restricted shell**. Refer to [The Restricted Shell](https://www.gnu.org/software/bash/manual/bash.html#The-Restricted-Shell). |
| ```-D``` | A list of all double-quoted strings preceded by **$** is printed on the standard output. These are the strings that are subject to language translation when the current locale is not **C** or **POSIX**. This implies the ```-n``` option; no commands will be executed. |
| ```[-+]O [shopt_option]``` | *shopt_option* is one of the shell options accepted by the *shopt* builtin.<br><br>If *shopt_option* is present, ```-O``` sets the value of that option; ```+O``` unsets it.<br>If *shopt_option* is not supplied, the names and values of the shell options accepted by *shopt* are printed on the standard output.<br><br>If the invocation option is ```+O```, the output is displayed in a format that may be reused as input. |
| ```--``` | A ```--``` signals the end of options and disables further option processing. Any arguments after the ```--``` are treated as filenames and arguments. An argument of ```-``` is equivalent to ```--```. |

<p/>

A **login shell** is one whose first character of argument zero is ```-```, or one invoked with the ```--login``` option.

An **interactive shell** is one started without non-option arguments, unless ```-s``` is specified, without specifying the ```-c``` option, and whose input and output are both connected to terminals, or one started with the ```-i``` option.

If arguments remain after option processing, and neither the ```-c``` nor the ```-s``` option has been supplied, the first argument is assumed to be the name of a file containing shell commands. When Bash is invoked in this fashion, **$0** is set to the name of the file, and the positional parameters are set to the remaining arguments. Bash reads and executes commands from this file, then exits. Bash's exit status is the exit status of the last command executed in the script. If no commands are executed, the exit status is **0**.

## Bash Startup Files

This section describes how Bash executes its startup files. If any of the files exist but cannot be read, Bash reports an error. Tildes are expanded in filenames as described above under Tilde Expansion (see [Tilde Expansion](#tilde-expansion)).

**Invoked as an interactive login shell, or with ```--login```**

When Bash is invoked as an **interactive login shell**, or as a **non-interactive shell** with the ```--login``` option, it first reads and executes commands from the file ***/etc/profile***, if that file exists. After reading that file, it looks for ***~/.bash_profile***, ***~/.bash_login***, and ***~/.profile***, in that order, and reads and executes commands from the first one that exists and is readable. The ```--noprofile``` option may be used when the shell is started to inhibit this behavior.

When a **login shell** exits, Bash reads and executes commands from the file ***~/.bash_logout***, if it exists.

**Invoked as an interactive non-login shell**

When an **interactive shell** that is not a **login shell** is started, Bash reads and executes commands from ***~/.bashrc***, if that file exists. This may be inhibited by using the ```--norc``` option. The ```--rcfile file``` option will force Bash to read and execute commands from *file* instead of ***~/.bashrc***.

So, typically, your ***~/.bash_profile*** contains the following line after (or before) any login-specific initializations.

```
if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
```

**Invoked non-interactively**

When Bash is started **non-interactively**, to run a shell script, for example, it looks for the variable **BASH_ENV** in the environment, expands its value if it appears there, and uses the expanded value as the name of a file to read and execute. Bash behaves as if the following command were executed:

```
if [ -n "$BASH_ENV" ]; then . "$BASH_ENV"; fi
```

but the value of the **PATH** variable is not used to search for the filename.

As noted above, if a **non-interactive shell** is invoked with the ```--login``` option, Bash attempts to read and execute commands from the login shell startup files.

**Invoked with name ```sh```**

If Bash is invoked with the name **sh**, it tries to mimic the startup behavior of historical versions of **sh** as closely as possible, while conforming to the POSIX standard as well.

When invoked as an **interactive login shell**, or as a **non-interactive shell** with the ```--login``` option, it first attempts to read and execute commands from ***/etc/profile*** and ***~/.profile***, in that order. The ```--noprofile``` option may be used to inhibit this behavior. When invoked as an **interactive shell** with the name **sh**, Bash looks for the variable **ENV**, expands its value if it is defined, and uses the expanded value as the name of a file to read and execute. Since a shell invoked as **sh** does not attempt to read and execute commands from any other startup files, the ```--rcfile``` option has no effect. A **non-interactive shell** invoked with the name **sh** does not attempt to read any other startup files.

When invoked as **sh**, Bash enters POSIX mode after the startup files are read.

**Invoked in POSIX mode**

When Bash is started in POSIX mode, as with the ```--posix``` command line option, it follows the POSIX standard for startup files. In this mode, **interactive shells** expand the **ENV** variable and commands are read and executed from the file whose name is the expanded value. No other startup files are read.

**Invoked by remote shell daemon**

Bash attempts to determine when it is being run with its standard input connected to a network connection, as when executed by the remote shell daemon, usually **rshd**, or the secure shell daemon **sshd**. If Bash determines it is being run in this fashion, it reads and executes commands from ***~/.bashrc***, if that file exists and is readable. It will not do this if invoked as **sh**. The ```--norc``` option may be used to inhibit this behavior, and the ```--rcfile``` option may be used to force another file to be read, but neither **rshd** nor **sshd** generally invoke the shell with those options or allow them to be specified.

**Invoked with unequal effective and real UID/GIDs**

If Bash is started with the effective user (group) id not equal to the real user (group) id, and the ```-p``` option is not supplied, no startup files are read, shell functions are not inherited from the environment, the **SHELLOPTS**, **BASHOPTS**, **CDPATH**, and **GLOBIGNORE** variables, if they appear in the environment, are ignored, and the effective user id is set to the real user id. If the ```-p``` option is supplied at invocation, the startup behavior is the same, but the effective user id is not reset.

## Interactive Shells

### What is an Interactive Shell?

An **interactive shell** is one started without non-option arguments, unless ```-s``` is specified, without specifying the ```-c``` option, and whose input and error output are both connected to terminals (as determined by **isatty**(3)), or one started with the ```-i``` option.

An **interactive shell** generally reads from and writes to a user's terminal.

The ```-s``` invocation option may be used to set the **positional parameters** when an **interactive shell** is started.

### Is this Shell Interactive?

To determine within a startup script whether or not Bash is running interactively, test the value of the ```-``` special parameter. It contains **i** when the shell is interactive. For example:

```
case "$-" in
    *i*) echo This shell is interactive ;;
    *) echo This shell is not interactive ;;
esac
```

Alternatively, startup scripts may examine the variable **PS1**; it is unset in non-interactive shells, and set in interactive shells. Thus:

```
if [ -z "$PS1" ]; then
    echo This shell is not interactive
else
    echo This shell is interactive
fi
```

### Interactive Shell Behavior

When the shell is running interactively, it changes its behavior in several ways.

1. Startup files are read and executed as described in [Bash Startup Files](#bash-startup-files).

2. [Job Control](#job-control) is enabled by default. When job control is in effect, Bash ignores the keyboard-generated job control signals **SIGTTIN**, **SIGTTOU**, and **SIGTSTP**.

3. Bash expands and displays **PS1** before reading the first line of a command, and expands and displays **PS2** before reading the second and subsequent lines of a multi-line command.

4. Bash executes the value of the **PROMPT_COMMAND** variable as a command before printing the primary prompt, $PS1 (see [Bash Variables](#bash-variables)).

5. Readline (see [Command Line Editing](#command-line-editing)) is used to read commands from the user's terminal.

6. Bash inspects the value of the ```ignoreeof``` option to ```set -o``` instead of exiting immediately when it receives an **EOF** on its standard input when reading a command (see [The *set* Builtin](#the-em-set-em-builtin)).

7. Command history (see [Bash History Facilities](#bash-history-facilities)) and history expansion (see [History Interaction](#history-interaction)) are enabled by default. Bash will save the command history to the file named by **$HISTFILE** when a shell with history enabled exits.

8. Alias expansion (see [Aliases](#aliases)) is performed by default.

9. In the absence of any traps, Bash ignores **SIGTERM** (see [Signals](#signals)).

10. In the absence of any traps, **SIGINT** is caught and handled (see [Signals](#signals)). **SIGINT** will interrupt some shell builtins.

11. An **interactive login shell** sends a **SIGHUP** to all jobs on exit if the ```huponexit``` shell option has been enabled (see [Signals](#signals)).

12. The ```-n``` invocation option is ignored, and ```set -n``` has no effect (see [The *set* Builtin](#the-em-set-em-builtin)).

13. Bash will check for mail periodically, depending on the values of the **MAIL**, **MAILPATH**, and **MAILCHECK** shell variables (see [Bash Variables](#bash-variables)).

14. Expansion errors due to references to unbound shell variables after ```set -u``` has been enabled will not cause the shell to exit (see [The *set* Builtin](#the-em-set-em-builtin)).

15. The shell will not exit on expansion errors caused by *var* being unset or null in **${var:?word}** expansions (see [Shell Parameter Expansion](#shell-parameter-expansion)).

16. Redirection errors encountered by shell builtins will not cause the shell to exit.

17. When running in POSIX mode, a special builtin returning an error status will not cause the shell to exit (see [Bash POSIX Mode](#bash-posix-mode)).

18. A failed **exec** will not cause the shell to exit (see [Bourne Shell Builtins](#bourne-shell-builtins)).

19. Parser syntax errors will not cause the shell to exit.

20. Simple spelling correction for directory arguments to the **cd** builtin is enabled by default (see the description of the ```cdspell``` option to the **shopt** builtin in [The *shopt* Builtin](#the-em-shopt-em-builtin)).

21. The shell will check the value of the **TMOUT** variable and exit if a command is not read within the specified number of seconds after printing **$PS1** (see [Bash Variables](#bash-variables)).

## Bash Conditional Expressions

Conditional expressions are used by the ```[[``` compound command and the ```test``` and ```[``` builtin commands.

Expressions may be unary or binary. Unary expressions are often used to examine the status of a file. There are string operators and numeric comparison operators as well. If the *file* argument to one of the primaries is of the form **/dev/fd/N**, then file descriptor *N* is checked. If the *file* argument to one of the primaries is one of **/dev/stdin**, **/dev/stdout**, or **/dev/stderr**, file descriptor **0**, **1**, or **2**, respectively, is checked.

When used with ```[[```, the ```<``` and ```>``` operators sort lexicographically using the current locale. The **test** command uses ASCII ordering.

Unless otherwise specified, primaries that operate on files follow symbolic links and operate on the target of the link, rather than the link itself.

| Conditional_Expressions | Description |
| :---------------------- | :---------- |
| ```-a file```<br>```-e file``` | True if *file* exists. |
| ```-s file``` | True if *file* exists and has a size greater than zero. |
| ```-b file``` | True if *file* exists and is a block special file. |
| ```-c file``` | True if *file* exists and is a character special file. |
| ```-d file``` | True if *file* exists and is a directory. |
| ```-f file``` | True if *file* exists and is a regular file. |
| ```-h file```<br>```-L file``` | True if *file* exists and is a symbolic link. |
| ```-p file``` | True if *file* exists and is a named pipe (FIFO). |
| ```-S file``` | True if *file* exists and is a socket. |
| ```-g file``` | True if *file* exists and its set-group-id bit is set. |
| ```-u file``` | True if *file* exists and its set-user-id bit is set. |
| ```-k file``` | True if *file* exists and its *sticky* bit is set. |
| ```-r file``` | True if *file* exists and is readable. |
| ```-w file``` | True if *file* exists and is writable. |
| ```-x file``` | True if *file* exists and is executable. |
| ```-t fd``` | True if file descriptor *fd* is open and refers to a terminal. |
| ```-G file``` | True if *file* exists and is owned by the effective group id. |
| ```-O file``` | True if *file* exists and is owned by the effective user id. |
| ```-N file``` | True if *file* exists and has been modified since it was last read. |
| ```file1 -ef file2``` | True if *file1* and *file2* refer to the same device and inode numbers. |
| ```file1 -nt file2``` | True if *file1* is newer (according to modification date) than *file2*, or if *file1* exists and *file2* does not. |
| ```file1 -ot file2``` | True if *file1* is older than *file2*, or if *file2* exists and *file1* does not. |
| ```-o optname``` | True if the shell option ```optname``` is enabled. The list of options appears in the description of the ```-o``` option to the **set** builtin (see [The *set* Builtin](#the-em-set-em-builtin)). |
| ```-v varname``` | True if the shell variable *varname* is set (has been assigned a value). |
| ```-R varname``` | True if the shell variable *varname* is set and is a name reference. |
| ```-z string``` | True if the length of *string* is zero. |
| ```-n string```<br>```string``` | True if the length of *string* is non-zero. |
| ```string1 == string2```<br>```string1 = string2``` | True if the strings are equal. When used with the ```[[``` command, this performs pattern matching as described in [Conditional Constructs](#conditional-constructs)).<br>```=``` should be used with the test command for POSIX conformance. |
| ```string1 != string2``` | True if the strings are not equal. |
| ```string1 < string2``` | True if *string1* sorts before *string2* lexicographically. |
| ```string1 > string2``` | True if *string1* sorts after *string2* lexicographically. |
| ```arg1 OP arg2``` | **OP** is one of ```-eq```, ```-ne```, ```-lt```, ```-le```, ```-gt```, or ```-ge```. These arithmetic binary operators return true if *arg1* is equal to, not equal to, less than, less than or equal to, greater than, or greater than or equal to *arg2*, respectively. *arg1* and *arg2* may be positive or negative integers. |

<p/>

## Shell Arithmetic

The shell allows arithmetic expressions to be evaluated, as one of the shell expansions or by the **let** and the ```-i``` option to the **declare** builtins.

Evaluation is done in fixed-width integers with no check for overflow, though division by **0** is trapped and flagged as an error. The operators and their precedence, associativity, and values are the same as in the C language. The following list of operators is grouped into levels of equal-precedence operators. The levels are listed in order of decreasing precedence.

| Arithmetic_Expressions | Description |
| :--------------------- | :---------- |
| ```id++``` ```id--``` | variable post-increment and post-decrement |
| ```++id``` ```--id``` | variable pre-increment and pre-decrement |
| ```-``` ```+``` | unary minus and plus |
| ```!``` ```~``` | logical and bitwise negation |
| ```**``` | exponentiation |
| ```*``` ```/``` ```%``` | multiplication, division, remainder |
| ```+``` ```-``` | addition, subtraction |
| ```<<``` ```>>``` | left and right bitwise shifts |
| ```<=``` ```>=``` ```<``` ```>``` | comparison |
| ```==``` ```!=``` | equality and inequality |
| ```&``` | bitwise AND |
| ```^``` | bitwise exclusive OR |
| ```|``` | bitwise OR |
| ```&&``` | logical AND |
| ```||``` | logical OR |
| ```expr ? expr : expr``` | conditional operator |
| ```=``` ```*=``` ```/=``` ```%=``` ```+=``` ```-=``` ```<<=``` ```>>=``` ```&=``` ```^=``` ```|=``` | assignment |
| ```expr1 , expr2``` | comma |

<p/>

Shell variables are allowed as operands; parameter expansion is performed before the expression is evaluated. Within an expression, shell variables may also be referenced by name without using the parameter expansion syntax. A shell variable that is null or unset evaluates to **0** when referenced by name without using the parameter expansion syntax. The value of a variable is evaluated as an arithmetic expression when it is referenced, or when a variable which has been given the integer attribute using ```declare -i``` is assigned a value. A null value evaluates to **0**. A shell variable need not have its integer attribute turned on to be used in an expression.

Constants with a leading **0** are interpreted as octal numbers. A leading ```0x``` or ```0X``` denotes hexadecimal. Otherwise, numbers take the form **[*****base*****#]*****n***, where the optional ***base*** is a decimal number between **2** and **64** representing the arithmetic base, and ***n*** is a number in that base. If ***base#*** is omitted, then base **10** is used. When specifying ***n***, the digits greater than **9** are represented by the lowercase letters, the uppercase letters, ```@```, and ```_```, in that order. If ***base*** is less than or equal to **36**, lowercase and uppercase letters may be used interchangeably to represent numbers between **10** and **35**.

Operators are evaluated in order of precedence. Sub-expressions in parentheses are evaluated first and may override the precedence rules above.

## Aliases

**Aliases** allow a *string* to be substituted for a *word* when it is used as the **first word of a simple command**. The shell maintains a list of aliases that may be set and unset with the ```alias``` and ```unalias``` builtin commands, refer to [Bash Builtin Commands](#bash-builtin-commands) for details.

* The first word of each [simple command](#simple-commands), if unquoted, is checked to see if it has an alias. If so, that word is replaced by the text of the alias.

* The characters ```/``` ```$``` ``` ` ``` ```=``` and any of the shell [metacharacters](#metacharacter) or [quoting characters](#quoting) may not appear in an alias name. The replacement text may contain any valid shell input, including shell [metacharacters](#metacharacter).

* The **first word of the replacement text** is tested for aliases, but a word that is identical to an alias being expanded is **not** expanded a second time.

* If the **last character of the alias value** is a *blank*, then the next command word following the alias is also checked for alias expansion.

* Aliases are not expanded when the shell is not interactive, unless the shell option ```expand_aliases``` is set using ```shopt```,  refer to [The *shopt* Builtin](#the-em-shopt-em-builtin):

```
$ shopt -s expand_aliases
```

Bash always reads at least one complete line of input before executing any of the commands on that line. **Aliases are expanded when a command is read, not when it is executed**.

* Therefore, an alias definition appearing on the same line as another command does not take effect until the next line of input is read. The commands following the alias definition on that line are not affected by the new alias.

* Aliases are expanded when a function definition is read, not when the function is executed, because a function definition is itself a compound command. As a consequence, **aliases defined in a function are not available until after that function is executed**. To be safe, always put alias definitions on a separate line, and do not use alias in compound commands.

**For almost every purpose, shell functions are preferred over aliases**.

### Frequently Used Aliases

The following is some frequently used aliases:

```
# Basic
alias ll="ls --color=auto -lh"
alias lla="ls --color=auto -lha"
alias dusum="du -sh"

# Linux kernel
alias checkpatch="~/linux/scripts/checkpatch.pl -terse -file"

# find specified file in current directory
alias findf="find . -noignore_readdir_race -nowarn -name"

# find installed kernel, e.g.: findkernel "*3.15*"
alias findkernel="find /boot /var -ignore_readdir_race -nowarn -name"

# find specified keyword in header files (.h)
alias findh="find . -noignore_readdir_race -nowarn -name '*.h' | xargs grep --color -n -s"

# find specified keyword in source files (.c)
alias findc="find . -noignore_readdir_race -nowarn -name '*.c' | xargs grep --color -n -s"

# find specified keyword in header and source files (.h, .c)
alias findahc="find . -noignore_readdir_race -nowarn -name '*.[hc]' | xargs grep --color -n -s"

# find specified keyword in all kind of files
alias findaf="find . -noignore_readdir_race -nowarn -type f | xargs grep --color -n -s"

# remove tail spaces, used when "git commit" failed caused by pre-commit script
# usage: rmtailspace lib.c > lib.c.notailspace
alias rmtailspace="sed -e \"s/[ \t]*$//g\""

# clean git directory, build git, and install built git
alias cleangit="make distclean"
alias buildgit="make prefix=/usr all doc info"
alias installgit="sudo make prefix=/usr install install-doc install-html install-info"
```

## Arrays

Bash provides one-dimensional **indexed** and **associative array** variables. Any variable may be used as an **indexed array**; the **declare** builtin will explicitly declare an array. There is no maximum limit on the size of an array, nor any requirement that members be indexed or assigned contiguously. **Indexed arrays** are referenced using integers (including arithmetic expressions, see [Shell Arithmetic](#shell-arithmetic)) and are **zero-based**; **associative arrays** use arbitrary strings. Unless otherwise noted, **indexed array** indices must be nonnegative integers.

An **indexed array** is created automatically if any variable is assigned to using the syntax ```name[subscript]=value```. The *subscript* is treated as an **arithmetic expression** that must evaluate to a number. To explicitly declare an array, use ```declare -a name```. The syntax ```declare -a name[subscript]``` is also accepted; the *subscript* is ignored. **Associative arrays** are created using ```declare -A name```.

Attributes may be specified for an array variable using the **declare** and **readonly** builtins. Each attribute applies to all members of an array.

Arrays are assigned to using compound assignments of the form ```name=(value1 value2 ...)``` where each *value* is of the form ```[subscript]=string```. **Indexed array** assignments do not require anything but string. When assigning to indexed arrays, if the optional *subscript* is supplied, that index is assigned to; otherwise the index of the element assigned is the last index assigned to by the statement plus one. Indexing starts at **zero**.

When assigning to an **associative array**, the *subscript* is required.

This syntax is also accepted by the **declare** builtin. Individual array elements may be assigned to using the ```name[subscript]=value``` syntax introduced above.

When assigning to an **indexed array**, if name is subscripted by a negative number, that number is interpreted as relative to one greater than the maximum index of name, so negative indices count back from the end of the array, and an index of **-1** references the last element.

Any element of an array may be referenced using **${name[subscript]}**. The braces are required to avoid conflicts with the shell's filename expansion operators. If the *subscript* is ```@``` or ```*```, the word expands to all members of the array name. These subscripts differ only when the word appears within double quotes. If the word is double-quoted,

* **${name[\*]}** expands to a single word with the value of each array member separated by the first character of the **IFS** variable, and
* **${name[@]}** expands each element of name to a separate word.

When there are no array members, **${name[@]}** expands to nothing. If the double-quoted expansion occurs within a word, the expansion of the first parameter is joined with the beginning part of the original word, and the expansion of the last parameter is joined with the last part of the original word. This is analogous to the expansion of the special parameters ```@``` and ```*```. **${#name[subscript]}** expands to the length of **${name[subscript]}**. If *subscript* is ```@``` or ```*```, the expansion is the number of elements in the array. Referencing an array variable without a *subscript* is equivalent to referencing with a subscript of **0**. If the *subscript* used to reference an element of an **indexed array** evaluates to a number less than **zero**, it is interpreted as relative to one greater than the maximum index of the array, so negative indices count back from the end of the array, and an index of **-1** refers to the last element.

An array variable is considered set if a *subscript* has been assigned a value. The null string is a valid value.

It is possible to obtain the keys (indices) of an array as well as the values. **${!name[@]}** and **${!name[*]}** expand to the indices assigned in array variable name. The treatment when in double quotes is similar to the expansion of the special parameters ```@``` and ```*``` within double quotes.

The **unset** builtin is used to destroy arrays. ```unset name[subscript]``` destroys the array element at index *subscript*. Negative subscripts to indexed arrays are interpreted as described above. Care must be taken to avoid unwanted side effects caused by filename expansion. ```unset name```, where *name* is an array, removes the entire array. A subscript of ```*``` or ```@``` also removes the entire array.

The **declare**, **local**, and **readonly** builtins each accept a ```-a``` option to specify an **indexed array** and a ```-A``` option to specify an **associative array**. If both options are supplied, ```-A``` takes precedence. The **read** builtin accepts a ```-a``` option to assign a list of words read from the standard input to an array, and can read values from the standard input into individual array elements. The **set** and **declare** builtins display array values in a way that allows them to be reused as input.

***Examples:*** indexed array

```
chenwx@chenwx ~ $ ia1[1]=10
chenwx@chenwx ~ $ echo ${ia1[0]}

chenwx@chenwx ~ $ echo ${ia1[1]}
10

chenwx@chenwx ~ $ declare -a ia2
chenwx@chenwx ~ $ echo ${ia1[*]}

chenwx@chenwx ~ $ echo ${ia1[@]}

chenwx@chenwx ~ $ ia2=([0]=0 [1]=100 [2]=200)
chenwx@chenwx ~ $ echo ${ia2}
0
chenwx@chenwx ~ $ echo ${ia2[0]}
0
chenwx@chenwx ~ $ echo ${ia2[1]}
100
chenwx@chenwx ~ $ echo ${ia2[2]}
200
chenwx@chenwx ~ $ echo ${ia2[*]}
0 100 200
chenwx@chenwx ~ $ echo ${ia2[@]}
0 100 200

chenwx@chenwx ~ $ echo ${#ia2}
1
chenwx@chenwx ~ $ echo ${#ia2[0]}
1
chenwx@chenwx ~ $ echo ${#ia2[1]}
2
chenwx@chenwx ~ $ echo ${#ia2[2]}
3

chenwx@chenwx ~ $ echo ${#ia2[*]}
3
chenwx@chenwx ~ $ echo ${#ia2[@]}
3

chenwx@chenwx ~ $ echo ${ia2[-1]}
200
chenwx@chenwx ~ $ echo ${ia2[-2]}
10
chenwx@chenwx ~ $ echo ${ia2[-3]}
0
chenwx@chenwx ~ $ echo ${ia2[-4]}
bash: ia2: bad array subscript

chenwx@chenwx ~ $ echo ${!ia2[@]}
0 1 2
chenwx@chenwx ~ $ echo ${!ia2[*]}
0 1 2

chenwx@chenwx ~ $ unset ia2[1]
chenwx@chenwx ~ $ echo ${!ia2[*]}
0 2
chenwx@chenwx ~ $ unset ia2   
chenwx@chenwx ~ $ echo ${!ia2[*]}

chenwx@chenwx ~ $ echo ${ia2[0]}

chenwx@chenwx ~ $ echo ${ia2[1]}

chenwx@chenwx ~ $ echo ${ia2[2]}

```

***Examples:*** associative array

```
chenwx@chenwx ~ $ declare -A aa1
chenwx@chenwx ~ $ echo ${aa1[*]}

chenwx@chenwx ~ $ echo ${aa1[@]}

chenwx@chenwx ~ $ aa1=([0]=10 [1]=100 [2]=1000)
chenwx@chenwx ~ $ echo ${aa1}
10
chenwx@chenwx ~ $ echo ${aa1[0]}
10
chenwx@chenwx ~ $ echo ${aa1[1]}
100
chenwx@chenwx ~ $ echo ${aa1[2]}
1000
chenwx@chenwx ~ $ echo ${aa1[*]}
10 100 1000
chenwx@chenwx ~ $ echo ${aa1[@]}
10 100 1000

chenwx@chenwx ~ $ echo ${#aa1}
2
chenwx@chenwx ~ $ echo ${#aa1[0]}
2
chenwx@chenwx ~ $ echo ${#aa1[1]}
3
chenwx@chenwx ~ $ echo ${#aa1[2]}
4

chenwx@chenwx ~ $ echo ${#aa1[*]}
3
chenwx@chenwx ~ $ echo ${#aa1[@]}
3

chenwx@chenwx ~ $ echo ${aa1[-1]}

chenwx@chenwx ~ $ echo ${aa1[-2]}

chenwx@chenwx ~ $ echo ${aa1[-3]}

chenwx@chenwx ~ $ echo ${aa1[-4]}

chenwx@chenwx ~ $ echo ${!aa1[@]}
0 1 2
chenwx@chenwx ~ $ echo ${!aa1[*]}
0 1 2

chenwx@chenwx ~ $ unset aa1[1]
chenwx@chenwx ~ $ echo ${!aa1[*]}
0 2
chenwx@chenwx ~ $ unset aa1
chenwx@chenwx ~ $ echo ${!aa1[*]}

chenwx@chenwx ~ $ echo ${aa1[0]}

chenwx@chenwx ~ $ echo ${aa1[1]}

chenwx@chenwx ~ $ echo ${aa1[2]}

```

## The Directory Stack

The directory stack is a list of recently-visited directories. The **pushd** builtin adds directories to the stack as it changes the current directory, and the **popd** builtin removes specified directories from the stack and changes the current directory to the directory removed. The **dirs** builtin displays the contents of the directory stack.

The contents of the directory stack are also visible as the value of the **DIRSTACK** shell variable.

| Builtins | Description |
| :------- | :---------- |
| ```dirs``` | Format:<br>```dirs [-clpv] [+N | -N]```<br><br>Display the list of currently remembered directories. Directories are added to the list with the **pushd** command; the **popd** command removes directories from the list.<br><br>```-c``` Clears the directory stack by deleting all of the elements.<br>```-l``` Produces a listing using full pathnames; the default listing format uses a tilde to denote the home directory.<br>```-p``` Causes **dirs** to print the directory stack with one entry per line.<br>```-v``` Causes **dirs** to print the directory stack with one entry per line, prefixing each entry with its index in the stack.<br>```+N``` Displays the ***N***th directory (counting from the left of the list printed by **dirs** when invoked without options), starting with zero.<br>```-N``` Displays the ***N***th directory (counting from the right of the list printed by **dirs** when invoked without options), starting with zero. |
| ```pushd``` | Format:<br>```pushd [-n] [+N | -N | dir]```<br><br>Save the current directory on the top of the directory stack and then **cd** to *dir*. With no arguments, **pushd** exchanges the top two directories.<br><br>```-n``` Suppresses the normal change of directory when adding directories to the stack, so that only the stack is manipulated.<br>```+N``` Brings the ***N***th directory (counting from the left of the list printed by **dirs**, starting with zero) to the top of the list by rotating the stack.<br>```-N``` Brings the ***N***th directory (counting from the right of the list printed by **dirs**, starting with zero) to the top of the list by rotating the stack.<br>```dir``` Makes the current working directory be the top of the stack, making it the new current directory as if it had been supplied as an argument to the **cd** builtin. |
| ```popd``` | Format:<br>```popd [-n] [+N | -N]```<br><br>Remove the top entry from the directory stack, and **cd** to the new top directory. When no arguments are given, **popd** removes the top directory from the stack and performs a **cd** to the new top directory. The elements are numbered from **0** starting at the first directory listed with **dirs**; that is, ```popd``` is equivalent to ```popd +0```.<br>```-n``` Suppresses the normal change of directory when removing directories from the stack, so that only the stack is manipulated.<br>```+N``` Removes the ***N***th directory (counting from the left of the list printed by **dirs**), starting with zero.<br>```-N``` Removes the ***N***th directory (counting from the right of the list printed by **dirs**), starting with zero. |

<p/>

***Examples:***

```
chenwx@chenwx ~/blog $ dirs
~/blog

chenwx@chenwx ~/blog $ pushd ~/Downloads/
~/Downloads ~/blog
chenwx@chenwx ~/Downloads $ pushd /etc/       
/etc ~/Downloads ~/blog
chenwx@chenwx /etc $ pushd /usr/lib
/usr/lib /etc ~/Downloads ~/blog

chenwx@chenwx /usr/lib $ dirs -l
/usr/lib /etc /home/chenwx/Downloads /home/chenwx/blog
chenwx@chenwx /usr/lib $ dirs -p
/usr/lib
/etc
~/Downloads
~/blog
chenwx@chenwx /usr/lib $ dirs -v
 0  /usr/lib
 1  /etc
 2  ~/Downloads
 3  ~/blog

chenwx@chenwx /usr/lib $ popd
/etc ~/Downloads ~/blog
chenwx@chenwx /etc $ popd
~/Downloads ~/blog
chenwx@chenwx ~/Downloads $ popd
~/blog
```

## Controlling the Prompt

The value of the variable **PROMPT_COMMAND** is examined just before Bash prints each primary prompt. If **PROMPT_COMMAND** is set and has a non-null value, then the value is executed just as if it had been typed on the command line.

In addition, the following table describes the special characters which can appear in the prompt variables **PS1** to **PS4**:

| Characters | Description |
| :--------- | :---------- |
| ```\a``` | A bell character. |
| ```\d``` | The date, in "Weekday Month Date" format (e.g., "Tue May 26"). |
| ```\D{format}``` | The format is passed to **strftime**(3) and the result is inserted into the prompt string; an empty format results in a locale-specific time representation. The braces are required. |
| ```\e``` | An escape character. |
| ```\h``` | The hostname, up to the first ```.```. |
| ```\H``` | The hostname. |
| ```\j``` | The number of jobs currently managed by the shell. |
| ```\l``` | The basename of the shell’s terminal device name. |
| ```\n``` | A newline. |
| ```\r``` | A carriage return. |
| ```\s``` | The name of the shell, the basename of **$0** (the portion following the final slash). |
| ```\t``` | The time, in 24-hour HH:MM:SS format. |
| ```\T``` | The time, in 12-hour HH:MM:SS format. |
| ```\@``` | The time, in 12-hour am/pm format. |
| ```\A``` | The time, in 24-hour HH:MM format. |
| ```\u``` | The username of the current user. |
| ```\v``` | The version of Bash (e.g., 2.00) |
| ```\V``` | The release of Bash, version + patchlevel (e.g., 2.00.0) |
| ```\w``` | The current working directory, with **$HOME** abbreviated with a tilde (uses the **$PROMPT_DIRTRIM** variable). |
| ```\W``` | The basename of **$PWD**, with **$HOME** abbreviated with a tilde. |
| ```\!``` | The history number of this command. |
| ```\#``` | The command number of this command. |
| ```\$``` | If the effective uid is **0**, ```#```, otherwise ```$```. |
| ```\nnn``` | The character whose ASCII code is the octal value *nnn*. |
| ```\\``` | A backslash. |
| ```\[``` | Begin a sequence of non-printing characters. This could be used to embed a terminal control sequence into the prompt. |
| ```\]``` | End a sequence of non-printing characters. |

<p/>

The command number and the history number are usually different: the history number of a command is its position in the history list, which may include commands restored from the history file (see [Bash History Facilities](#bash-history-facilities)), while the command number is the position in the sequence of commands executed during the current shell session.

After the string is decoded, it is expanded via **parameter expansion**, **command substitution**, **arithmetic expansion**, and **quote removal**, subject to the value of the **promptvars** shell option (see [Bash Builtin Commands](#bash-builtin-commands)).

## The Restricted Shell

If Bash is started with the name **rbash**, or the ```--restricted``` or ```-r``` option is supplied at invocation, the shell becomes restricted. A restricted shell is used to set up an environment more controlled than the standard shell. A restricted shell behaves identically to bash with the exception that the following are disallowed or not performed:

* Changing directories with the **cd** builtin.

* Setting or unsetting the values of the **SHELL**, **PATH**, **ENV**, or **BASH_ENV** variables.

* Specifying command names containing slashes.

* Specifying a filename containing a slash as an argument to the ```.``` builtin command.

* Specifying a filename containing a slash as an argument to the ```-p``` option to the **hash** builtin command.

* Importing function definitions from the shell environment at startup.

* Parsing the value of **SHELLOPTS** from the shell environment at startup.

* Redirecting output using the ```>```, ```>|```, ```<>```, ```>&```, ```&>```, and ```>>``` redirection operators.

* Using the **exec** builtin to replace the shell with another command.

* Adding or deleting builtin commands with the ```-f``` and ```-d``` options to the **enable** builtin.

* Using the **enable** builtin command to enable disabled shell builtins.

* Specifying the ```-p``` option to the **command** builtin.

* Turning off restricted mode with ```set +r``` or ```set +o restricted```.

These restrictions are enforced after any startup files are read.

When a command that is found to be a shell script is executed (see [Shell Scripts](#shell-scripts)), **rbash** turns off any restrictions in the shell spawned to execute the script.

## Bash POSIX Mode

Starting Bash with the ```--posix``` command-line option or executing ```set -o posix``` while Bash is running will cause Bash to conform more closely to the POSIX standard by changing the behavior to match that specified by POSIX in areas where the Bash default differs.

When invoked as **sh**, Bash enters POSIX mode after reading the startup files.

The following list is what's changed when **POSIX mode** is in effect:

1. When a command in the hash table no longer exists, Bash will re-search **$PATH** to find the new location. This is also available with ```shopt -s checkhash```.

2. The message printed by the job control code and builtins when a job exits with a non-zero status is **Done(status)**.

3. The message printed by the job control code and builtins when a job is stopped is **Stopped(***signame***)**, where *signame* is, for example, **SIGTSTP**.

4. The **bg** builtin uses the required format to describe each job placed in the background, which does not include an indication of whether the job is the current or previous job.

5. Reserved words appearing in a context where reserved words are recognized do not undergo alias expansion.

6. The POSIX PS1 and PS2 expansions of ```!``` to the history number and ```!!``` to ```!``` are enabled, and parameter expansion is performed on the values of PS1 and PS2 regardless of the setting of the promptvars option.

7. The POSIX startup files are executed (**$ENV**) rather than the normal Bash files.

8. Tilde expansion is only performed on assignments preceding a command name, rather than on all assignment statements on the line.

9. The **command** builtin does not prevent builtins that take assignment statements as arguments from expanding them as assignment statements; when not in POSIX mode, assignment builtins lose their assignment statement expansion properties when preceded by **command**.

10. The default history file is ***~/.sh_history*** (this is the default value of **$HISTFILE**).

11. The output of ```kill -l``` prints all the signal names on a single line, separated by spaces, without the **SIG** prefix.

12. The **kill** builtin does not accept signal names with a **SIG** prefix.

13. Non-interactive shells exit if *filename* in ```. filename``` is not found.

14. Non-interactive shells exit if a syntax error in an arithmetic expansion results in an invalid expression.

15. Non-interactive shells exit if there is a syntax error in a script read with the ```.``` or ```source``` builtins, or in a string processed by the **eval** builtin.

16. Redirection operators do not perform filename expansion on the word in the redirection unless the shell is interactive.

17. Redirection operators do not perform word splitting on the word in the redirection.

18. Function names must be valid shell **name**s. That is, they may not contain characters other than letters, digits, and underscores, and may not start with a digit. Declaring a function with an invalid name causes a fatal syntax error in non-interactive shells.

19. Function names may not be the same as one of the POSIX special builtins.

20. POSIX special builtins are found before shell functions during command lookup.

21. The **time** reserved word may be used by itself as a command. When used in this way, it displays timing statistics for the shell and its completed children. The **TIMEFORMAT** variable controls the format of the timing information.

22. When parsing and expanding a **${. . .}** expansion that appears within double quotes, single quotes are no longer special and cannot be used to quote a closing brace or other special character, unless the operator is one of those defined to perform pattern removal. In this case, they do not have to appear as matched pairs.

23. The parser does not recognize **time** as a reserved word if the next token begins with a ```-```.

24. If a POSIX special builtin returns an error status, a non-interactive shell exits. The fatal errors are those listed in the POSIX standard, and include things like passing incorrect options, redirection errors, variable assignment errors for assignments preceding the command name, and so on.

25. A non-interactive shell exits with an error status if a variable assignment error occurs when no command name follows the assignment statements. A variable assignment error occurs, for example, when trying to assign a value to a readonly variable.

26. A non-interactive shell exits with an error status if a variable assignment error occurs in an assignment statement preceding a special builtin, but not with any other simple command.

27. A non-interactive shell exits with an error status if the iteration variable in a for statement or the selection variable in a select statement is a readonly variable.

28. Process substitution is not available.

29. While variable indirection is available, it may not be applied to the ```#``` and ```?``` special parameters.

30. Assignment statements preceding POSIX special builtins persist in the shell environment after the builtin completes.

31. Assignment statements preceding shell function calls persist in the shell environment after the function returns, as if a POSIX special builtin command had been executed.

32. The **export** and **readonly** builtin commands display their output in the format required by POSIX.

33. The **trap** builtin displays signal names without the leading **SIG**.

34. The **trap** builtin doesn't check the first argument for a possible signal specification and revert the signal handling to the original disposition if it is, unless that argument consists solely of digits and is a valid signal number. If users want to reset the handler for a given signal to the original disposition, they should use ```-``` as the first argument.

35. The ```.``` and ```source``` builtins do not search the current directory for the filename argument if it is not found by searching **PATH**.

36. Subshells spawned to execute command substitutions inherit the value of the ```-e``` option from the parent shell. When not in POSIX mode, Bash clears the ```-e``` option in such subshells.

37. Alias expansion is always enabled, even in non-interactive shells.

38. When the **alias** builtin displays alias definitions, it does not display them with a leading ```alias ``` unless the ```-p``` option is supplied.

39. When the **set** builtin is invoked without options, it does not display shell function names and definitions.

40. When the **set** builtin is invoked without options, it displays variable values without quotes, unless they contain shell metacharacters, even if the result contains nonprinting characters.

41. When the **cd** builtin is invoked in logical mode, and the pathname constructed from **$PWD** and the directory name supplied as an argument does not refer to an existing directory, **cd** will fail instead of falling back to physical mode.

42. The **pwd** builtin verifies that the value it prints is the same as the current directory, even if it is not asked to check the file system with the ```-P``` option.

43. When listing the history, the **fc** builtin does not include an indication of whether or not a history entry has been modified.

44. The default editor used by **fc** is **ed**.

45. The **type** and **command** builtins will not report a non-executable file as having been found, though the shell will attempt to execute such a file if it is the only so-named file found in **$PATH**.

46. The **vi** editing mode will invoke the **vi** editor directly when the ```v``` command is run, instead of checking **$VISUAL** and **$EDITOR**.

47. When the ```xpg_echo``` option is enabled, Bash does not attempt to interpret any arguments to **echo** as options. Each argument is displayed, after escape characters are converted.

48. The **ulimit** builtin uses a block size of 512 bytes for the ```-c``` and ```-f``` options.

49. The arrival of **SIGCHLD** when a trap is set on **SIGCHLD** does not interrupt the **wait** builtin and cause it to return immediately. The trap command is run once for each child that exits.

50. The **read** builtin may be interrupted by a signal for which a trap has been set. If Bash receives a trapped signal while executing **read**, the trap handler executes and **read** returns an exit status greater than 128.

There is other POSIX behavior that Bash does not implement by default even when in POSIX mode. Specifically:

1. The **fc** builtin checks **$EDITOR** as a program to edit history entries if **FCEDIT** is unset, rather than defaulting directly to **ed**. **fc** uses **ed** if **EDITOR** is unset.

2. As noted above, Bash requires the ```xpg_echo``` option to be enabled for the **echo** builtin to be fully conformant.

Bash can be configured to be POSIX-conformant by default, by specifying the ```--enablestrict-posix-default``` to **configure** when building (see [Optional Features](#optional-features)).

# Job Control

## Job Control Basics

Job control refers to the ability to selectively **stop** (**suspend**) the execution of processes and **continue** (**resume**) their execution at a later point. A user typically employs this facility via an interactive interface supplied jointly by the operating system kernel's terminal driver and Bash.

The shell associates a *job* with each pipeline. It keeps a table of currently executing jobs, which may be listed with the **jobs** command. When Bash starts a job asynchronously, it prints a line that looks like:

```
[1] 25647
```

indicating that this job is job number 1 and that the process ID of the last process in the pipeline associated with this job is 25647. **All of the processes in a single pipeline are members of the same job**. Bash uses the *job* abstraction as the basis for job control.

To facilitate the implementation of the user interface to job control, the operating system maintains the notion of a current terminal process group ID. Members of this process group (processes whose process group ID is equal to the current terminal process group ID) receive keyboard-generated signals such as **SIGINT**. These processes are said to be in the foreground. **Background processes are those whose process group ID differs from the terminal's; such processes are immune to keyboard-generated signals**. Only foreground processes are allowed to read from or, if the user so specifies with *stty tostop*, write to the terminal. Background processes which attempt to read from (write to when *stty tostop* is in effect) the terminal are sent a **SIGTTIN** (**SIGTTOU**) signal by the kernel’s terminal driver, which, unless caught, suspends the process.

If the operating system on which Bash is running supports job control, Bash contains facilities to use it. Typing the suspend character (typically ```^Z```, **Control-Z**) while a process is running causes that process to be stopped and returns control to Bash. Typing the delayed suspend character (typically ```^Y```, **Control-Y**) causes the process to be stopped when it attempts to read input from the terminal, and control to be returned to Bash. The user then manipulates the state of this job, using the **bg** command to continue it in the background, the **fg** command to continue it in the foreground, or the **kill** command to kill it. A ```^Z``` takes effect immediately, and has the additional side effect of causing pending output and typeahead to be discarded.

There are a number of ways to refer to a job in the shell. The character ```%``` introduces a job specification (*jobspec*).

Job number *n* may be referred to as ```%n```. The symbols ```%%``` and ```%+``` refer to the shell's notion of the current job, which is the last job stopped while it was in the foreground or started in the background. A single ```%``` (with no accompanying job specification) also refers to the current job. The previous job may be referenced using ```%-```. If there is only a single job, ```%+``` and ```%-``` can both be used to refer to that job. In output pertaining to jobs (e.g., the output of the **jobs** command), the current job is always flagged with a ```+```, and the previous job with a ```-```.

A job may also be referred to using a prefix of the name used to start it, or using a substring that appears in its command line. For example, ```%ce``` refers to a stopped *ce* job. Using ```%?ce```, on the other hand, refers to any job containing the string ```ce``` in its command line. If the prefix or substring matches more than one job, Bash reports an error.

Simply naming a job can be used to bring it into the foreground: ```%1``` is a synonym for ```fg %1```, bringing job 1 from the background into the foreground. Similarly, ```%1 &``` resumes job 1 in the background, equivalent to ```bg %1```.

The shell learns immediately whenever a job changes state. Normally, Bash waits until it is about to print a prompt before reporting changes in a job's status so as to not interrupt any other output. If the ```-b``` option to the **set** builtin is enabled, Bash reports such changes immediately. Any trap on **SIGCHLD** is executed for each child process that exits.

If an attempt to exit Bash is made while jobs are stopped, (or running, if the ```checkjobs``` option is enabled), the shell prints a warning message, and if the ```checkjobs``` option is enabled, lists the jobs and their statuses. The **jobs** command may then be used to inspect their status. If a second attempt to exit is made without an intervening command, Bash does not print another warning, and any stopped jobs are terminated.

## Job Control Builtins

| Builtins | Description |
| :------: | :---------- |
| **bg**   | Format:<br>```bg [jobspec ...]```<br><br>Resume each suspended job *jobspec* in the background, as if it had been started with ```&```. If *jobspec* is not supplied, the current job is used. The return status is **zero** unless it is run when job control is not enabled, or, when run with job control enabled, any *jobspec* was not found or specifies a job that was started without job control. |
| **fg**   | Format:<br>```fg [jobspec]```<br><br>Resume the job *jobspec* in the foreground and make it the current job. If *jobspec* is not supplied, the current job is used. The return status is that of the command placed into the foreground, or non-zero if run when job control is disabled or, when run with job control enabled, *jobspec* does not specify a valid job or *jobspec* specifies a job that was started without job control. |
| **jobs** | Formats:<br>```jobs [-lnprs] [jobspec]```<br>```jobs -x command [arguments]```<br><br>The first form lists the active jobs. The options have the following meanings:<br>```-l``` List process ids in addition to the normal information.<br>```-n``` Display information only about jobs that have changed status since the user was last notified of their status.<br>```-p``` List only the process id of the job’s process group leader.<br>```-r``` Display only running jobs.<br>```-s``` Display only stopped jobs.<br><br>If *jobspec* is given, output is restricted to information about that job. If *jobspec* is not supplied, the status of all jobs is listed.<br><br>If the ```-x``` option is supplied, *jobs* replaces any *jobspec* found in *command* or *arguments* with the corresponding process group id, and executes *command*, passing it *arguments*, returning its exit status. |
| **kill** | Formats:<br>```kill [-s sigspec] [-n signum] [-sigspec] jobspec or pid```<br>```kill -l [exit_status]```<br><br>Send a signal specified by *sigspec* or *signum* to the process named by job specification *jobspec* or process id *pid*. *sigspec* is either a case-insensitive signal name such as **SIGINT** (with or without the **SIG** prefix) or a signal number; *signum* is a signal number. If *sigspec* and *signum* are not present, **SIGTERM** is used.<br><br>The ```-l``` option lists the signal names. If any arguments are supplied when ```-l``` is given, the names of the signals corresponding to the arguments are listed, and the return status is zero.<br><br>Exit status is a number specifying a signal number or the exit status of a process terminated by a signal. The return status is zero if at least one signal was successfully sent, or non-zero if an error occurs or an invalid option is encountered. |
| **wait** | Format:<br>```wait [-n] [jobspec or pid ...]```<br><br>Wait until the child process specified by each process id *pid* or job specification *jobspec* exits and return the exit status of the last command waited for. If a job spec is given, all processes in the job are waited for. If no arguments are given, all currently active child processes are waited for, and the return status is zero. If the ```-n``` option is supplied, *wait* waits for any job to terminate and returns its exit status. If neither *jobspec* nor *pid* specifies an active child process of the shell, the return status is **127**. |
| **disown** | Format:<br>```disown [-ar] [-h] [jobspec ...]```<br><br>Without options, remove each *jobspec* from the table of active jobs. If the ```-h``` option is given, the job is not removed from the table, but is marked so that **SIGHUP** is not sent to the job if the shell receives a **SIGHUP**. If *jobspec* is not present, and neither the ```-a``` nor the ```-r``` option is supplied, the current job is used. If no *jobspec* is supplied, the ```-a``` option means to remove or mark all jobs; the ```-r``` option without a *jobspec* argument restricts operation to running jobs. |
| **suspend** | Format:<br>```suspend [-f]```<br><br>Suspend the execution of this shell until it receives a **SIGCONT** signal. **A login shell cannot be suspended**; the ```-f``` option can be used to override this and force the suspension. |

<p/>

When job control is not active, the **kill** and **wait** builtins do not accept *jobspec* arguments. They must be supplied process IDs.

## Job Control Variables

| Variable | Description |
| :------- | :---------- |
| **auto_resume** | This variable controls how the shell interacts with the user and job control.<br><br>If this variable exists then single word simple commands without redirections are treated as candidates for resumption of an existing job. There is no ambiguity allowed; if there is more than one job beginning with the string typed, then the most recently accessed job will be selected. The name of a stopped job, in this context, is the command line used to start it.<br><br>If this variable is set to the value ```exact```, the string supplied must match the name of a stopped job exactly; if set to ```substring```, the string supplied needs to match a substring of the name of a stopped job. The ```substring``` value provides functionality analogous to the ```%?``` job ID (see [Job Control Basics](#job-control-basics)).<br><br>If set to any other value, the supplied string must be a prefix of a stopped job’s name; this provides functionality analogous to the ```%``` job ID. |

<p/>

# Command Line Editing

Command line editing is provided by the **Readline** library, which is used by several different programs, including Bash. Command line editing is enabled by default when using an **interactive shell**, unless the ```--noediting``` option is supplied at shell invocation. Line editing is also used when using the ```-e``` option to the *read* builtin command. By default, the line editing commands are similar to those of **Emacs**. A **vi**-style line editing interface is also available. Line editing can be enabled at any time using the ```-o emacs``` or ```-o vi``` options to the *set* builtin command (see [The *set* Builtin](#the-em-set-em-builtin)), or disabled using the ```+o emacs``` or ```+o vi``` options to the *set* builtin.

## Introduction to Line Editing

|  Key  | Operation | Description |
| :---: | :-------- | :---------- |
| ```C-k``` | **Control-K** | The **k** key is pressed while the **Control** key is depressed. |
| ```M-k``` | **Meta-K** | The **Meta** key (if you have one) is depressed, and the **k** key is pressed. The **Meta** key is labeled **ALT** on many keyboards.<br><br>On keyboards with two keys labeled **ALT** (usually to either side of the space bar), the **ALT** on the left side is generally set to work as a **Meta** key. The **ALT** key on the right may also be configured to work as a **Meta** key or may be configured as some other modifier, such as a **Compose** key for typing accented characters.<br><br>**NOTE:** If you do not have a **Meta** or **ALT** key, or another key working as a **Meta** key, the identical keystroke can be generated by typing ```ESC``` first, and then typing ```k```. Either process is known as ***metafying*** the **k** key. |
| ```M-C-k``` | **Meta-Control-k** | The character produced by ***metafying*** **C-k**. <br><br>**NOTE:** If you do not have a **Meta** or **ALT** key, or another key working as a **Meta** key, the identical keystroke can be generated by typing ```ESC``` first, and then typing ```C-k```. |
| ```DEL``` | **Delete** |  |
| ```ESC``` | **Esc** |  |
| ```LFD``` | **LFD** or **C-j** | If your keyboard lacks a **LFD** key, typing **C-j** will produce the desired character. |
| ```SPC``` |  |  |
| ```RET``` | **Return** or **Enter**  | The **RET** key may be labeled **Return** or **Enter** on some keyboards. |
| ```TAB``` | **Tab** |  |

<p/>

## Readline Interaction

Often during an interactive session you type in a long line of text, only to notice that the first word on the line is misspelled. The **Readline** library gives you a set of commands for manipulating the text as you type it in, allowing you to just fix your typo, and not forcing you to retype the majority of the line. Using these editing commands, you move the cursor to the place that needs correction, and delete or insert the text of the corrections. Then, when you are satisfied with the line, you simply press **RET**. **You do not have to be at the end of the line to press RET; the entire line is accepted regardless of the location of the cursor within the line.**

### Readline Bare Essentials

|  Keys | Description |
| :---: | :---------- |
| ```C-b``` | Move back one character. |
| ```C-f``` | Move forward one character. |
| ```C-d``` | Delete the character **underneath** the cursor. |
| ```DEL```<br>```Backspace``` | Delete the character to the **left** of the cursor. Depending on your configuration, the **Backspace** key be set to delete the character to the **left** of the cursor and the **DEL** key set to delete the character **underneath** the cursor, like ```C-d```, rather than the character to the **left** of the cursor. |
| Printing characters | Insert the character into the line at the cursor. |
| ```C-_```<br>```C-x```<br>```C-u``` | Undo the last editing command. You can undo all the way back to an empty line. |

<p/>

### Readline Movement Commands

The above table describes the most basic keystrokes that you need in order to do editing of the input line. For your convenience, many other commands have been added in addition to ```C-b```, ```C-f```, ```C-d```, and ```DEL```. Here are some commands for moving more rapidly about the line.

|  Keys | Description |
| :---: | :---------- |
| ```C-a``` | Move to the start of the line. |
| ```C-e``` | Move to the end of the line. |
| ```M-b``` | Move backward a word.<br><br>**NOTE:** If you do not have a **Meta** or **ALT** key, or another key working as a **Meta** key, the identical keystroke can be generated by typing ```ESC``` first, and then typing ```b```. |
| ```M-f``` | Move forward a word, where a word is composed of letters and digits.<br><br>**NOTE:** If you do not have a **Meta** or **ALT** key, or another key working as a **Meta** key, the identical keystroke can be generated by typing ```ESC``` first, and then typing ```f```. |
| ```C-l``` | Clear the screen, reprinting the current line at the top. |

<p/>

Notice how ```C-f``` moves forward a **character**, while ```M-f``` moves forward a **word**. It is a loose convention that ***control*** **keystrokes operate on characters while meta keystrokes operate on words**.

### Readline Killing Commands

Killing text means to delete the text from the line, but to save it away for later use, usually by yanking (re-inserting) it back into the line. (**Cut** and **paste** are more recent jargon for **kill** and **yank**.)

If the description for a command says that it **kills** text, then you can be sure that you can get the text back in a different (or the same) place later.

When you use a kill command, the text is saved in a *kill-ring*. Any number of consecutive kills save all of the killed text together, so that when you yank it back, you get it all. The kill ring is not line specific; the text that you killed on a previously typed line is available to be yanked back later, when you are typing another line.

Here is the list of commands for killing text.

|  Keys | Description |
| :---: | :---------- |
| ```C-k``` | Kill the text from the current cursor position to the end of the line. |
| ```M-d``` | Kill from the cursor to the end of the current word, or, if between words, to the end of the next word. Word boundaries are the same as those used by ```M-f```.<br><br>**NOTE:** If you do not have a **Meta** or **ALT** key, or another key working as a **Meta** key, the identical keystroke can be generated by typing ```ESC``` first, and then typing ```d```. |
| ```M-DEL``` | Kill from the cursor the start of the current word, or, if between words, to the start of the previous word. Word boundaries are the same as those used by ```M-b```.<br><br>**NOTE:** If you do not have a **Meta** or **ALT** key, or another key working as a **Meta** key, the identical keystroke can be generated by typing ```ESC``` first, and then typing ```DEL```. |
| ```C-w``` | Kill from the cursor to the previous whitespace. This is different than ```M-DEL``` because the word boundaries differ. |

<p/>

Here is how to yank the text back into the line. Yanking means to copy the most-recently-killed text from the kill buffer.

|  Keys | Description |
| :---: | :---------- |
| ```C-y``` | Yank the most recently killed text back into the buffer at the cursor. |
| ```M-y``` | Rotate the kill-ring, and yank the new top. You can only do this if the prior command is ```C-y``` or ```M-y```.<br><br>**NOTE:** If you do not have a **Meta** or **ALT** key, or another key working as a **Meta** key, the identical keystroke can be generated by typing ```ESC``` first, and then typing ```y```. |

<p/>

### Readline Arguments

You can pass numeric arguments to Readline commands. Sometimes the argument acts as a repeat count, other times it is the *sign* of the argument that is significant. If you pass a negative argument to a command which normally acts in a forward direction, that command will act in a backward direction. For example, to kill text back to the start of the line, you might type ```M-- C-k```.

The general way to pass numeric arguments to a command is to type meta digits before the command. If the first *digit* typed is a minus sign (```-```), then the sign of the argument will be negative. Once you have typed one meta digit to get the argument started, you can type the remainder of the digits, and then the command. For example, to give the ```C-d``` command an argument of 10, you could type ```M-1 0 C-d```, which will delete the next ten characters on the input line.

### Searching for Commands in the History

Readline provides commands for searching through the command history (see [Bash History Facilities](#bash-history-facilities)) for lines containing a specified string. There are two search modes: **incremental** and **non-incremental**.

**Incremental searches** begin before the user has finished typing the search string. As each character of the search string is typed, Readline displays the next entry from the history matching the string typed so far. An incremental search requires only as many characters as needed to find the desired history entry. To search backward in the history for a particular string, type ```C-r```. Typing ```C-s``` searches forward through the history. The characters present in the value of the *isearch-terminators* variable (see [Readline Init File Syntax](#readline-init-file-syntax)) are used to terminate an incremental search. If that variable has not been assigned a value, the **ESC** and **C-J** characters will terminate an incremental search. ```C-g``` will abort an incremental search and restore the original line. When the search is terminated, the history entry containing the search string becomes the current line.

To find other matching entries in the history list, type ```C-r``` or ```C-s``` as appropriate. This will search backward or forward in the history for the next entry matching the search string typed so far. Any other key sequence bound to a Readline command will terminate the search and execute that command. For instance, a **RET** will terminate the search and accept the line, thereby executing the command from the history list. A movement command will terminate the search, make the last line found the current line, and begin editing.

Readline remembers the last incremental search string. If two ```C-r```s are typed without any intervening characters defining a new search string, any remembered search string is used.

**Non-incremental searches** read the entire search string before starting to search for matching history lines. The search string may be typed by the user or be part of the contents of the current line.

|  Keys | Description |
| :---: | :---------- |
| ```C-r``` | Incremental search **backward** in the history for a particular string.<br><br>The characters present in the value of the *isearch-terminators* variable (see [Readline Init File Syntax](#readline-init-file-syntax)) are used to terminate an incremental search. If that variable has not been assigned a value, the **ESC** and **C-J** characters will terminate an incremental search.<br><br>Readline remembers the last incremental search string. If two ```C-r```s are typed without any intervening characters defining a new search string, any remembered search string is used. |
| ```C-s``` | Incremental search **forward** in the history for a particular string.<br><br>The characters present in the value of the *isearch-terminators* variable (see [Readline Init File Syntax](#readline-init-file-syntax)) are used to terminate an incremental search. If that variable has not been assigned a value, the **ESC** and **C-J** characters will terminate an incremental search. |
| ```C-g``` | It aborts an incremental search and restore the original line. |

<p/>

***Examples:***

Input ```C-r``` and then type ```atom```, you probably get the following screen:

```
chenwx@chenwx ~ $
(reverse-i-search)`atom': atom _includes/footer.html
```

Then, you input ```ESC``` to terminate the incremental search:

```
chenwx@chenwx ~ $ atom _includes/footer.html
```

And then, you input ```Enter``` to execute the command if you satisfy with it.

## Readline Init File

Although the Readline library comes with a set of Emacs-like keybindings installed by default, it is possible to use a different set of keybindings. Any user can customize programs that use Readline by putting commands in an *inputrc* file, conventionally in his home directory. The name of this file is taken from the value of the shell variable **INPUTRC**. If that variable is unset, the default is ```~/.inputrc```. If that file does not exist or cannot be read, the ultimate default is ```/etc/inputrc```.

When a program which uses the Readline library starts up, the init file is read, and the key bindings are set.

In addition, the ```C-x C-r``` command re-reads this init file, thus incorporating any changes that you might have made to it.

### Readline Init File Syntax

There are only a few basic constructs allowed in the Readline init file. Blank lines are ignored. Lines beginning with a ```#``` are comments. Lines beginning with a ```$``` indicate conditional constructs. Other lines denote variable settings and key bindings. Refer to ***8.3.1 Readline Init File Syntax*** of **Bash Reference Manual v4.3** for details.

***Example:*** The ```bind -V``` command lists the current Readline variable names and values.

```
chenwx@chenwx ~ $ bind -V               
bind-tty-special-chars is set to `on'
blink-matching-paren is set to `on'
byte-oriented is set to `off'
colored-stats is set to `off'
completion-ignore-case is set to `off'
completion-map-case is set to `off'
convert-meta is set to `on'
disable-completion is set to `off'
echo-control-characters is set to `on'
enable-keypad is set to `off'
enable-meta-key is set to `on'
expand-tilde is set to `off'
history-preserve-point is set to `off'
horizontal-scroll-mode is set to `off'
input-meta is set to `on'
mark-directories is set to `on'
mark-modified-lines is set to `off'
mark-symlinked-directories is set to `off'
match-hidden-files is set to `on'
menu-complete-display-prefix is set to `off'
meta-flag is set to `on'
output-meta is set to `on'
page-completions is set to `on'
prefer-visible-bell is set to `on'
print-completions-horizontally is set to `off'
revert-all-at-newline is set to `off'
show-all-if-ambiguous is set to `off'
show-all-if-unmodified is set to `off'
show-mode-in-prompt is set to `off'
skip-completed-text is set to `off'
visible-stats is set to `off'
bell-style is set to `audible'
comment-begin is set to `#'
completion-display-width is set to `-1'
completion-prefix-display-length is set to `0'
completion-query-items is set to `100'
editing-mode is set to `emacs'
history-size is set to `500'
keymap is set to `emacs'
keyseq-timeout is set to `500'
```

***Example:*** The ```bind -v``` command displays Readline variable names and values in such a way that they can be used as input or in a Readline initialization file.

```
chenwx@chenwx ~ $ bind -v
set bind-tty-special-chars on
set blink-matching-paren on
set byte-oriented off
set colored-stats off
set completion-ignore-case off
set completion-map-case off
set convert-meta on
set disable-completion off
set echo-control-characters on
set enable-keypad off
set enable-meta-key on
set expand-tilde off
set history-preserve-point off
set horizontal-scroll-mode off
set input-meta on
set mark-directories on
set mark-modified-lines off
set mark-symlinked-directories off
set match-hidden-files on
set menu-complete-display-prefix off
set meta-flag on
set output-meta on
set page-completions on
set prefer-visible-bell on
set print-completions-horizontally off
set revert-all-at-newline off
set show-all-if-ambiguous off
set show-all-if-unmodified off
set show-mode-in-prompt off
set skip-completed-text off
set visible-stats off
set bell-style audible
set comment-begin #
set completion-display-width -1
set completion-prefix-display-length 0
set completion-query-items 100
set editing-mode emacs
set history-size 500
set keymap emacs
set keyseq-timeout 500
```

### Conditional Init Constructs

Readline implements a facility similar in spirit to the conditional compilation features of the C preprocessor which allows key bindings and variable settings to be performed as the result of tests. There are four parser directives used.

| Constructs | Description |
| :--------- | :---------- |
| ```$if```  | The construct allows bindings to be made based on the editing mode, the terminal being used, or the application using Readline. The text of the test extends to the end of the line; no characters are required to isolate it.<br><br>**mode**<br>The ```mode=``` form of the ```$if``` directive is used to test whether Readline is in **emacs** or **vi** mode. This may be used in conjunction with the ```set keymap``` command, for instance, to set bindings in the **emacs-standard** and **emacs-ctlx** keymaps only if Readline is starting out in **emacs** mode.<br><br>**term**<br>The ```term=``` form may be used to include terminal-specific key bindings, perhaps to bind the key sequences output by the terminal's function keys. The word on the right side of the ```=``` is tested against both the full name of the terminal and the portion of the terminal name before the first ```-```. This allows sun to match both sun and sun-cmd, for instance.<br><br>**application**<br>The *application* construct is used to include application-specific settings. Each program using the Readline library sets the application name, and you can test for a particular value. This could be used to bind key sequences to functions useful for a specific program. For instance, the following command adds a key sequence that quotes the current or previous word in Bash:<br>```$if Bash```<br>```# Quote the current or previous word```<br>```"\C-xq": "\eb\"\ef\""```<br>```$endif``` |
| ```$endif``` | This command terminates an ```$if``` command. |
| ```$else``` | Commands in this branch of the ```$if``` directive are executed if the test fails. |
| ```$include``` | This directive takes a single filename as an argument and reads commands and bindings from that file. For example, the following directive reads from */etc/inputrc*:<br>```$include /etc/inputrc``` |

## Bindable Readline Commands

This section describes Readline commands that may be bound to key sequences. You can list your key bindings by executing ```bind -P``` or, for a more terse format, suitable for an *inputrc* file, ```bind -p```. Command names without an accompanying key sequence are unbound by default.

In the following descriptions, *point* refers to the current cursor position, and *mark* refers to a cursor position saved by the *set-mark* command (see [Some Miscellaneous Commands](#some-miscellaneous-commands)). The text between the *point* and *mark* is referred to as the *region*.

***Example:*** List your key bindings by executing ```bind -P```.

```
chenwx@chenwx ~ $ bind -P

abort can be found on "\C-g", "\C-x\C-g", "\M-\C-g".
accept-line can be found on "\C-j", "\C-m".
alias-expand-line is not bound to any keys
arrow-key-prefix is not bound to any keys
backward-byte is not bound to any keys
backward-char can be found on "\C-b", "\M-OD", "\M-[D".
backward-delete-char can be found on "\C-h", "\C-?".
backward-kill-line can be found on "\C-x\C-?".
backward-kill-word can be found on "\M-\C-h", "\M-\C-?".
backward-word can be found on "\M-\M-[D", "\M-[1;5D", "\M-[5D", "\M-b".
beginning-of-history can be found on "\M-<".
beginning-of-line can be found on "\C-a", "\M-OH", "\M-[1~", "\M-[H".
call-last-kbd-macro can be found on "\C-xe".
capitalize-word can be found on "\M-c".
character-search can be found on "\C-]".
character-search-backward can be found on "\M-\C-]".
clear-screen can be found on "\C-l".
complete can be found on "\C-i", "\M-\M-".
complete-command can be found on "\M-!".
complete-filename can be found on "\M-/".
complete-hostname can be found on "\M-@".
complete-into-braces can be found on "\M-{".
complete-username can be found on "\M-~".
complete-variable can be found on "\M-$".
copy-backward-word is not bound to any keys
copy-forward-word is not bound to any keys
copy-region-as-kill is not bound to any keys
dabbrev-expand is not bound to any keys
delete-char can be found on "\C-d", "\M-[3~".
delete-char-or-list is not bound to any keys
delete-horizontal-space can be found on "\M-\\".
digit-argument can be found on "\M--", "\M-0", "\M-1", "\M-2", "\M-3", ...
display-shell-version can be found on "\C-x\C-v".
do-lowercase-version can be found on "\C-xA", "\C-xB", "\C-xC", "\C-xD", "\C-xE", ...
downcase-word can be found on "\M-l".
dump-functions is not bound to any keys
dump-macros is not bound to any keys
dump-variables is not bound to any keys
dynamic-complete-history can be found on "\M-\C-i".
edit-and-execute-command can be found on "\C-x\C-e".
emacs-editing-mode is not bound to any keys
end-kbd-macro can be found on "\C-x)".
end-of-history can be found on "\M->".
end-of-line can be found on "\C-e", "\M-OF", "\M-[4~", "\M-[F".
exchange-point-and-mark can be found on "\C-x\C-x".
forward-backward-delete-char is not bound to any keys
forward-byte is not bound to any keys
forward-char can be found on "\C-f", "\M-OC", "\M-[C".
forward-search-history can be found on "\C-s".
forward-word can be found on "\M-\M-[C", "\M-[1;5C", "\M-[5C", "\M-f".
glob-complete-word can be found on "\M-g".
glob-expand-word can be found on "\C-x*".
glob-list-expansions can be found on "\C-xg".
history-and-alias-expand-line is not bound to any keys
history-expand-line can be found on "\M-^".
history-search-backward is not bound to any keys
history-search-forward is not bound to any keys
history-substring-search-backward is not bound to any keys
history-substring-search-forward is not bound to any keys
insert-comment can be found on "\M-#".
insert-completions can be found on "\M-*".
insert-last-argument can be found on "\M-.", "\M-_".
kill-line can be found on "\C-k".
kill-region is not bound to any keys
kill-whole-line is not bound to any keys
kill-word can be found on "\M-d".
magic-space is not bound to any keys
menu-complete is not bound to any keys
menu-complete-backward is not bound to any keys
next-history can be found on "\C-n", "\M-OB", "\M-[B".
non-incremental-forward-search-history can be found on "\M-n".
non-incremental-forward-search-history-again is not bound to any keys
non-incremental-reverse-search-history can be found on "\M-p".
non-incremental-reverse-search-history-again is not bound to any keys
old-menu-complete is not bound to any keys
operate-and-get-next can be found on "\C-o".
overwrite-mode is not bound to any keys
possible-command-completions can be found on "\C-x!".
possible-completions can be found on "\M-=", "\M-?".
possible-filename-completions can be found on "\C-x/".
possible-hostname-completions can be found on "\C-x@".
possible-username-completions can be found on "\C-x~".
possible-variable-completions can be found on "\C-x$".
previous-history can be found on "\C-p", "\M-OA", "\M-[A".
print-last-kbd-macro is not bound to any keys
quoted-insert can be found on "\C-q", "\C-v", "\M-[2~".
re-read-init-file can be found on "\C-x\C-r".
redraw-current-line is not bound to any keys
reverse-search-history can be found on "\C-r".
revert-line can be found on "\M-\C-r", "\M-r".
self-insert can be found on " ", "!", "\"", "#", "$", ...
set-mark can be found on "\C-@", "\M- ".
shell-backward-kill-word is not bound to any keys
shell-backward-word is not bound to any keys
shell-expand-line can be found on "\M-\C-e".
shell-forward-word is not bound to any keys
shell-kill-word is not bound to any keys
skip-csi-sequence is not bound to any keys
start-kbd-macro can be found on "\C-x(".
tab-insert is not bound to any keys
tilde-expand can be found on "\M-&".
transpose-chars can be found on "\C-t".
transpose-words can be found on "\M-t".
tty-status is not bound to any keys
undo can be found on "\C-x\C-u", "\C-_".
universal-argument is not bound to any keys
unix-filename-rubout is not bound to any keys
unix-line-discard can be found on "\C-u".
unix-word-rubout can be found on "\C-w".
upcase-word can be found on "\M-u".
vi-append-eol is not bound to any keys
vi-append-mode is not bound to any keys
vi-arg-digit is not bound to any keys
vi-bWord is not bound to any keys
vi-back-to-indent is not bound to any keys
vi-backward-bigword is not bound to any keys
vi-backward-word is not bound to any keys
vi-bword is not bound to any keys
vi-change-case is not bound to any keys
vi-change-char is not bound to any keys
vi-change-to is not bound to any keys
vi-char-search is not bound to any keys
vi-column is not bound to any keys
vi-complete is not bound to any keys
vi-delete is not bound to any keys
vi-delete-to is not bound to any keys
vi-eWord is not bound to any keys
vi-editing-mode is not bound to any keys
vi-end-bigword is not bound to any keys
vi-end-word is not bound to any keys
vi-eof-maybe is not bound to any keys
vi-eword is not bound to any keys
vi-fWord is not bound to any keys
vi-fetch-history is not bound to any keys
vi-first-print is not bound to any keys
vi-forward-bigword is not bound to any keys
vi-forward-word is not bound to any keys
vi-fword is not bound to any keys
vi-goto-mark is not bound to any keys
vi-insert-beg is not bound to any keys
vi-insertion-mode is not bound to any keys
vi-match is not bound to any keys
vi-movement-mode is not bound to any keys
vi-next-word is not bound to any keys
vi-overstrike is not bound to any keys
vi-overstrike-delete is not bound to any keys
vi-prev-word is not bound to any keys
vi-put is not bound to any keys
vi-redo is not bound to any keys
vi-replace is not bound to any keys
vi-rubout is not bound to any keys
vi-search is not bound to any keys
vi-search-again is not bound to any keys
vi-set-mark is not bound to any keys
vi-subst is not bound to any keys
vi-tilde-expand is not bound to any keys
vi-yank-arg is not bound to any keys
vi-yank-to is not bound to any keys
yank can be found on "\C-y".
yank-last-arg can be found on "\M-.", "\M-_".
yank-nth-arg can be found on "\M-\C-y".
yank-pop can be found on "\M-y".
```

***Example:*** List your key bindings by executing ```bind -p``` for a more terse format, suitable for an *inputrc* file.

```
chenwx@chenwx ~ $ bind -p

"\C-g": abort
"\C-x\C-g": abort
"\M-\C-g": abort
"\C-j": accept-line
"\C-m": accept-line
# alias-expand-line (not bound)
# arrow-key-prefix (not bound)
# backward-byte (not bound)
"\C-b": backward-char
"\M-OD": backward-char
"\M-[D": backward-char
"\C-h": backward-delete-char
"\C-?": backward-delete-char
"\C-x\C-?": backward-kill-line
"\M-\C-h": backward-kill-word
"\M-\C-?": backward-kill-word
"\M-\M-[D": backward-word
"\M-[1;5D": backward-word
"\M-[5D": backward-word
"\M-b": backward-word
"\M-<": beginning-of-history
"\C-a": beginning-of-line
"\M-OH": beginning-of-line
"\M-[1~": beginning-of-line
"\M-[H": beginning-of-line
"\C-xe": call-last-kbd-macro
"\M-c": capitalize-word
"\C-]": character-search
"\M-\C-]": character-search-backward
"\C-l": clear-screen
"\C-i": complete
"\M-\M-": complete
"\M-!": complete-command
"\M-/": complete-filename
"\M-@": complete-hostname
"\M-{": complete-into-braces
"\M-~": complete-username
"\M-$": complete-variable
# copy-backward-word (not bound)
# copy-forward-word (not bound)
# copy-region-as-kill (not bound)
# dabbrev-expand (not bound)
"\C-d": delete-char
"\M-[3~": delete-char
# delete-char-or-list (not bound)
"\M-\\": delete-horizontal-space
"\M--": digit-argument
"\M-0": digit-argument
"\M-1": digit-argument
"\M-2": digit-argument
"\M-3": digit-argument
"\M-4": digit-argument
"\M-5": digit-argument
"\M-6": digit-argument
"\M-7": digit-argument
"\M-8": digit-argument
"\M-9": digit-argument
"\C-x\C-v": display-shell-version
"\C-xA": do-lowercase-version
"\C-xB": do-lowercase-version
"\C-xC": do-lowercase-version
"\C-xD": do-lowercase-version
"\C-xE": do-lowercase-version
"\C-xF": do-lowercase-version
"\C-xG": do-lowercase-version
"\C-xH": do-lowercase-version
"\C-xI": do-lowercase-version
"\C-xJ": do-lowercase-version
"\C-xK": do-lowercase-version
"\C-xL": do-lowercase-version
"\C-xM": do-lowercase-version
"\C-xN": do-lowercase-version
"\C-xO": do-lowercase-version
"\C-xP": do-lowercase-version
"\C-xQ": do-lowercase-version
"\C-xR": do-lowercase-version
"\C-xS": do-lowercase-version
"\C-xT": do-lowercase-version
"\C-xU": do-lowercase-version
"\C-xV": do-lowercase-version
"\C-xW": do-lowercase-version
"\C-xX": do-lowercase-version
"\C-xY": do-lowercase-version
"\C-xZ": do-lowercase-version
"\M-A": do-lowercase-version
"\M-B": do-lowercase-version
"\M-C": do-lowercase-version
"\M-D": do-lowercase-version
"\M-E": do-lowercase-version
"\M-F": do-lowercase-version
"\M-G": do-lowercase-version
"\M-H": do-lowercase-version
"\M-I": do-lowercase-version
"\M-J": do-lowercase-version
"\M-K": do-lowercase-version
"\M-L": do-lowercase-version
"\M-M": do-lowercase-version
"\M-N": do-lowercase-version
"\M-P": do-lowercase-version
"\M-Q": do-lowercase-version
"\M-R": do-lowercase-version
"\M-S": do-lowercase-version
"\M-T": do-lowercase-version
"\M-U": do-lowercase-version
"\M-V": do-lowercase-version
"\M-W": do-lowercase-version
"\M-X": do-lowercase-version
"\M-Y": do-lowercase-version
"\M-Z": do-lowercase-version
"\M-l": downcase-word
# dump-functions (not bound)
# dump-macros (not bound)
# dump-variables (not bound)
"\M-\C-i": dynamic-complete-history
"\C-x\C-e": edit-and-execute-command
# emacs-editing-mode (not bound)
"\C-x)": end-kbd-macro
"\M->": end-of-history
"\C-e": end-of-line
"\M-OF": end-of-line
"\M-[4~": end-of-line
"\M-[F": end-of-line
"\C-x\C-x": exchange-point-and-mark
# forward-backward-delete-char (not bound)
# forward-byte (not bound)
"\C-f": forward-char
"\M-OC": forward-char
"\M-[C": forward-char
"\C-s": forward-search-history
"\M-\M-[C": forward-word
"\M-[1;5C": forward-word
"\M-[5C": forward-word
"\M-f": forward-word
"\M-g": glob-complete-word
"\C-x*": glob-expand-word
"\C-xg": glob-list-expansions
# history-and-alias-expand-line (not bound)
"\M-^": history-expand-line
# history-search-backward (not bound)
# history-search-forward (not bound)
# history-substring-search-backward (not bound)
# history-substring-search-forward (not bound)
"\M-#": insert-comment
"\M-*": insert-completions
"\M-.": insert-last-argument
"\M-_": insert-last-argument
"\C-k": kill-line
# kill-region (not bound)
# kill-whole-line (not bound)
"\M-d": kill-word
# magic-space (not bound)
# menu-complete (not bound)
# menu-complete-backward (not bound)
"\C-n": next-history
"\M-OB": next-history
"\M-[B": next-history
"\M-n": non-incremental-forward-search-history
# non-incremental-forward-search-history-again (not bound)
"\M-p": non-incremental-reverse-search-history
# non-incremental-reverse-search-history-again (not bound)
# old-menu-complete (not bound)
"\C-o": operate-and-get-next
# overwrite-mode (not bound)
"\C-x!": possible-command-completions
"\M-=": possible-completions
"\M-?": possible-completions
"\C-x/": possible-filename-completions
"\C-x@": possible-hostname-completions
"\C-x~": possible-username-completions
"\C-x$": possible-variable-completions
"\C-p": previous-history
"\M-OA": previous-history
"\M-[A": previous-history
# print-last-kbd-macro (not bound)
"\C-q": quoted-insert
"\C-v": quoted-insert
"\M-[2~": quoted-insert
"\C-x\C-r": re-read-init-file
# redraw-current-line (not bound)
"\C-r": reverse-search-history
"\M-\C-r": revert-line
"\M-r": revert-line
" ": self-insert
"!": self-insert
"\"": self-insert
"#": self-insert
"$": self-insert
"%": self-insert
"&": self-insert
"'": self-insert
"(": self-insert
")": self-insert
"*": self-insert
"+": self-insert
",": self-insert
"-": self-insert
".": self-insert
"/": self-insert
"0": self-insert
"1": self-insert
"2": self-insert
"3": self-insert
"4": self-insert
"5": self-insert
"6": self-insert
"7": self-insert
"8": self-insert
"9": self-insert
...
```

### Commands For Moving

| Commands | Default | Description |
| :------- | :------ | :---------- |
| beginning-of-line | ```C-a``` | Move to the start of the current line. |
| end-of-line | ```C-e``` | Move to the end of the line. |
| forward-char | ```C-f``` | Move forward a character. |
| backward-char | ```C-b``` | Move back a character. |
| forward-word | ```M-f``` | Move forward to the end of the next word. Words are composed of letters and digits. |
| backward-word | ```M-b``` | Move back to the start of the current or previous word. Words are composed of letters and digits. |
| shell-forward-word | *Unbound* | Move forward to the end of the next word. Words are delimited by non-quoted shell metacharacters. |
| shell-backward-word | *Unbound* | Move back to the start of the current or previous word. Words are delimited by non-quoted shell metacharacters. |
| clear-screen | ```C-l``` | Clear the screen and redraw the current line, leaving the current line at the top of the screen. |
| redraw-current-line | *Unbound* | Refresh the current line. |

<p/>

### Commands For Manipulating The History

| Commands | Default | Description |
| :------- | :------ | :---------- |
| accept-line | ```Newline``` or ```Return``` | Accept the line regardless of where the cursor is. If this line is non-empty, add it to the history list according to the setting of the **HISTCONTROL** and **HISTIGNORE** variables. If this line is a modified history line, then restore the history line to its original state. |
| previous-history | ```C-p``` | Move **back** through the history list, fetching the previous command. |
| next-history | ```C-n``` | Move **forward** through the history list, fetching the next command. |
| beginning-of-history | ```M-<``` | Move to the first line in the history. |
| end-of-history | ```M->``` | Move to the end of the input history, i.e., the line currently being entered. |
| reverse-search-history | ```C-r``` | Search backward starting at the current line and moving **up** through the history as necessary. This is an incremental search. |
| forward-search-history | ```C-s``` | Search forward starting at the current line and moving **down** through the the history as necessary. This is an incremental search. |
| non-incremental-reverse-search-history | ```M-p``` | Search backward starting at the current line and moving **up** through the history as necessary using a non-incremental search for a string supplied by the user. |
| non-incremental-forward-search-history | ```M-n``` | Search forward starting at the current line and moving **down** through the the history as necessary using a non-incremental search for a string supplied by the user. |
| history-search-forward | *Unbound* | Search forward through the history for the string of characters between the start of the current line and the point. The search string must match at the beginning of a history line. This is a non-incremental search. |
| history-search-backward | *Unbound* | Search backward through the history for the string of characters between the start of the current line and the point. The search string must match at the beginning of a history line. This is a non-incremental search. |
| history-substr-search-forward | *Unbound* | Search forward through the history for the string of characters between the start of the current line and the point. The search string may match anywhere in a history line. This is a non-incremental search. |
| history-substr-search-backward | *Unbound* | Search backward through the history for the string of characters between the start of the current line and the point. The search string may match anywhere in a history line. This is a non-incremental search. |
| yank-nth-arg | ```M-C-y``` | Insert the first argument to the previous command (usually the second word on the previous line) at point. With an argument n, insert the nth word from the previous command (the words in the previous command begin with word 0). A negative argument inserts the nth word from the end of the previous command. Once the argument n is computed, the argument is extracted as if the ```!n``` history expansion had been specified. |
| yank-last-arg | ```M-.``` or ```M-_``` | Insert last argument to the previous command (the last word of the previous history entry). With a numeric argument, behave exactly like yank-nth-arg. Successive calls to yank-last-arg move back through the history list, inserting the last word (or the word specified by the argument to the first call) of each line in turn. Any numeric argument supplied to these successive calls determines the direction to move through the history. A negative argument switches the direction through the history (back or forward). The history expansion facilities are used to extract the last argument, as if the ```!$``` history expansion had been specified. |

<p/>

### Commands For Changing Text

| Commands | Default | Description |
| :------- | :------ | :---------- |
| end-of-file | usually ```C-d``` | The character indicating end-of-file as set, for example, by **stty**. If this character is read when there are no characters on the line, and point is at the beginning of the line, Readline interprets it as the end of input and returns EOF. |
| delete-char | ```C-d``` | Delete the character at point. If this function is bound to the same character as the tty EOF character, as ```C-d``` commonly is, see above for the effects. |
| backward-delete-char | ```Rubout``` | Delete the character behind the cursor. A numeric argument means to kill the characters instead of deleting them. |
| forward-backward-delete-char | *Unbound* | Delete the character under the cursor, unless the cursor is at the end of the line, in which case the character behind the cursor is deleted. |
| quoted-insert | ```C-q``` or ```C-v``` | Add the next character typed to the line verbatim. This is how to insert key sequences like ```C-q```, for example. |
| self-insert | ```a```, ```b```, ```A```, ```1```, ```!```, ... | Insert yourself. |
| transpose-chars | ```C-t``` | Drag the character before the cursor forward over the character at the cursor, moving the cursor forward as well. If the insertion point is at the end of the line, then this transposes the last two characters of the line. Negative arguments have no effect. |
| transpose-words | ```M-t``` | Drag the word before point past the word after point, moving point past that word as well. If the insertion point is at the end of the line, this transposes the last two words on the line. |
| upcase-word | ```M-u``` | Uppercase the current (or following) word. With a negative argument, uppercase the previous word, but do not move the cursor. |
| downcase-word | ```M-l``` | Lowercase the current (or following) word. With a negative argument, lowercase the previous word, but do not move the cursor. |
| capitalize-word | ```M-c``` | Capitalize the current (or following) word. With a negative argument, capitalize the previous word, but do not move the cursor. |
| overwrite-mode | *Unbound* | Toggle overwrite mode. With an explicit positive numeric argument, switches to overwrite mode. With an explicit non-positive numeric argument, switches to insert mode. This command affects only emacs mode; vi mode does overwrite differently. Each call to readline() starts in insert mode. In overwrite mode, characters bound to self-insert replace the text at point rather than pushing the text to the right. Characters bound to backward-delete-char replace the character before point with a space. |

<p/>

### Killing And Yanking

| Commands | Default | Description |
| :------- | :------ | :---------- |
| kill-line | ```C-k``` | Kill the text from point to the end of the line. |
| backward-kill-line | ```C-x Rubout``` | Kill backward to the beginning of the line. |
| unix-line-discard | ```C-u``` | Kill backward from the cursor to the beginning of the current line. |
| kill-whole-line | *Unbound* | Kill all characters on the current line, no matter where point is. |
| kill-word | ```M-d``` | Kill from point to the end of the current word, or if between words, to the end of the next word. Word boundaries are the same as forward-word. |
| backward-kill-word | ```M-DEL``` | Kill the word behind point. Word boundaries are the same as backward-word. |
| shell-kill-word | *Unbound* | Kill from point to the end of the current word, or if between words, to the end of the next word. Word boundaries are the same as shell-forward-word. |
| shell-backward-kill-word | *Unbound* | Kill the word behind point. Word boundaries are the same as shell-backwardword. |
| unix-word-rubout | ```C-w``` | Kill the word behind point, using white space as a word boundary. The killed text is saved on the *kill-ring*. |
| unix-filename-rubout | *Unbound* | Kill the word behind point, using white space and the slash character as the word boundaries. The killed text is saved on the *kill-ring*. |
| delete-horizontal-space | *Unbound* | Delete all spaces and tabs around point. |
| kill-region | *Unbound* | Kill the text in the current region. |
| copy-region-as-kill | *Unbound* | Copy the text in the region to the kill buffer, so it can be yanked right away. |
| copy-backward-word | *Unbound* | Copy the word before point to the kill buffer. The word boundaries are the same as backward-word. |
| copy-forward-word | *Unbound* | Copy the word following point to the kill buffer. The word boundaries are the same as forward-word. |
| yank | ```C-y``` | Yank the top of the kill ring into the buffer at point. |
| yank-pop | ```M-y``` | Rotate the kill-ring, and yank the new top. You can only do this if the prior command is yank or yank-pop. |

<p/>

### Specifying Numeric Arguments

| Commands | Default | Description |
| :------- | :------ | :---------- |
| digit-argument | ```M-0```, ```M-1```, ... ```M--``` | Add this digit to the argument already accumulating, or start a new argument. ```M--``` starts a negative argument. |
| universal-argument | *Unbound* | This is another way to specify an argument. If this command is followed by one or more digits, optionally with a leading minus sign, those digits define the argument. If the command is followed by digits, executing universal-argument again ends the numeric argument, but is otherwise ignored. As a special case, if this command is immediately followed by a character that is neither a digit or minus sign, the argument count for the next command is multiplied by four. The argument count is initially one, so executing this function the first time makes the argument count four, a second time makes the argument count sixteen, and so on. |

<p/>

### Letting Readline Type For You

| Commands | Default | Description |
| :------- | :------ | :---------- |
| complete | ```TAB``` | Attempt to perform completion on the text before point. The actual completion performed is application-specific. Bash attempts completion treating the text as a variable (if the text begins with ```$```), username (if the text begins with ```~```), hostname (if the text begins with ‘@’), or command (including aliases and functions) in turn. If none of these produces a match, filename completion is attempted. |
| possible-completions | ```M-?``` | List the possible completions of the text before point. When displaying completions, Readline sets the number of columns used for display to the value of completion-display-width, the value of the environment variable **COLUMNS**, or the screen width, in that order. |
| insert-completions | ```M-*``` | Insert all completions of the text before point that would have been generated by possible-completions. |
| menu-complete | *Unbound* | Similar to complete, but replaces the word to be completed with a single match from the list of possible completions. Repeated execution of menu-complete steps through the list of possible completions, inserting each match in turn. At the end of the list of completions, the bell is rung (subject to the setting of bell-style) and the original text is restored. An argument of *n* moves *n* positions forward in the list of matches; a negative argument may be used to move backward through the list. This command is intended to be bound to **TAB**, but is unbound by default. |
| menu-complete-backward | *Unbound* | Identical to menu-complete, but moves backward through the list of possible completions, as if menu-complete had been given a negative argument. |
| delete-char-or-list | *Unbound* | Deletes the character under the cursor if not at the beginning or end of the line (like delete-char). If at the end of the line, behaves identically to possible-completions. |
| complete-filename | ```M-/``` | Attempt filename completion on the text before point. |
| possible-filename-completions | ```C-x /``` | List the possible completions of the text before point, treating it as a filename. |
| complete-username | ```M-~``` | Attempt completion on the text before point, treating it as a username. |
| possible-username-completions | ```C-x ~``` | List the possible completions of the text before point, treating it as a username. |
| complete-variable | ```M-$``` | Attempt completion on the text before point, treating it as a shell variable. |
| possible-variable-completions | ```C-x $``` | List the possible completions of the text before point, treating it as a shell
variable. |
| complete-hostname | ```M-@``` | Attempt completion on the text before point, treating it as a hostname. |
| possible-hostname-completions | ```C-x @``` | List the possible completions of the text before point, treating it as a hostname. |
| complete-command | ```M-!``` | Attempt completion on the text before point, treating it as a command name. Command completion attempts to match the text against aliases, reserved words, shell functions, shell builtins, and finally executable filenames, in that order. |
| possible-command-completions | ```C-x !``` | List the possible completions of the text before point, treating it as a command name. |
| dynamic-complete-history | ```M-TAB``` | Attempt completion on the text before point, comparing the text against lines from the history list for possible completion matches. |
| dabbrev-expand | *Unbound* | Attempt menu completion on the text before point, comparing the text against lines from the history list for possible completion matches. |
| complete-into-braces | ```M-{``` | Perform filename completion and insert the list of possible completions enclosed within braces so the list is available to the shell. |

<p/>

### Keyboard Macros

| Commands | Default | Description |
| :------- | :------ | :---------- |
| start-kbd-macro | ```C-x (``` | Begin saving the characters typed into the current keyboard macro. |
| end-kbd-macro | ```C-x )``` | Stop saving the characters typed into the current keyboard macro and save the definition. |
| call-last-kbd-macro | ```C-x e``` | Re-execute the last keyboard macro defined, by making the characters in the macro appear as if typed at the keyboard. |
| print-last-kbd-macro | *Unbound* | Print the last keboard macro defined in a format suitable for the *inputrc* file. |

<p/>

### Some Miscellaneous Commands

| Commands | Default | Description |
| :------- | :------ | :---------- |
| re-read-init-file | ```C-x C-r``` | Read in the contents of the inputrc file, and incorporate any bindings or variable assignments found there. |
| abort | ```C-g``` | Abort the current editing command and ring the terminal’s bell (subject to the setting of bell-style). |
| do-uppercase-version | ```M-a```, ```M-b```, ```M-x```, ... | If the metafied character x is lowercase, run the command that is bound to the corresponding uppercase character. |
| prefix-meta | ```ESC``` | Metafy the next character typed. This is for keyboards without a meta key. Typing ```ESC f``` is equivalent to typing ```M-f```. |
| undo | ```C-_``` or ```C-x C-u``` | Incremental undo, separately remembered for each line. |
| revert-line | ```M-r``` | Undo all changes made to this line. This is like executing the undo command enough times to get back to the beginning. |
| tilde-expand | ```M-&``` | Perform tilde expansion on the current word. |
| set-mark | ```C-@``` | Set the mark to the point. If a numeric argument is supplied, the mark is set to that position. |
| exchange-point-and-mark | ```C-x C-x``` | Swap the point with the mark. The current cursor position is set to the saved position, and the old cursor position is saved as the mark. |
| character-search | ```C-]``` | A character is read and point is moved to the next occurrence of that character. A negative count searches for previous occurrences. |
| character-search-backward | ```M-C-]``` | A character is read and point is moved to the previous occurrence of that character. A negative count searches for subsequent occurrences. |
| skip-csi-sequence | *Unbound* | Read enough characters to consume a multi-key sequence such as those defined for keys like Home and End. Such sequences begin with a Control Sequence Indicator (CSI), usually ```ESC-[```. If this sequence is bound to "\e[", keys producing such sequences will have no effect unless explicitly bound to a readline command, instead of inserting stray characters into the editing buffer. This is unbound by default, but usually bound to ```ESC-[```. |
| insert-comment | ```M-#``` | Without a numeric argument, the value of the comment-begin variable is inserted at the beginning of the current line. If a numeric argument is supplied, this command acts as a toggle: if the characters at the beginning of the line do not match the value of comment-begin, the value is inserted, otherwise the characters in comment-begin are deleted from the beginning of the line. In either case, the line is accepted as if a newline had been typed. The default value of comment-begin causes this command to make the current line a shell  comment. If a numeric argument causes the comment character to be removed, the line will be executed by the shell. |
| dump-functions | *Unbound* | Print all of the functions and their key bindings to the Readline output stream. If a numeric argument is supplied, the output is formatted in such a way that it can be made part of an *inputrc* file. |
| dump-variables | *Unbound* | Print all of the settable variables and their values to the Readline output stream. If a numeric argument is supplied, the output is formatted in such a way that it can be made part of an inputrc file. |
| dump-macros | *Unbound* | Print all of the Readline key sequences bound to macros and the strings they output. If a numeric argument is supplied, the output is formatted in such a way that it can be made part of an *inputrc* file. |
| glob-complete-word | ```M-g``` | The word before point is treated as a pattern for pathname expansion, with an asterisk implicitly appended. This pattern is used to generate a list of matching file names for possible completions. |
| glob-expand-word | ```C-x *``` | The word before point is treated as a pattern for pathname expansion, and the list of matching file names is inserted, replacing the word. If a numeric argument is supplied, a ```*``` is appended before pathname expansion. |
| glob-list-expansions | ```C-x g``` | The list of expansions that would have been generated by glob-expand-word is displayed, and the line is redrawn. If a numeric argument is supplied, a ```*``` is appended before pathname expansion. |
| display-shell-version | ```C-x C-v``` | Display version information about the current instance of Bash. |
| shell-expand-line | ```M-C-e``` | Expand the line as the shell does. This performs alias and history expansion as well as all of the shell word expansions. |
| history-expand-line | ```M-^``` | Perform history expansion on the current line. |
| magic-space | *Unbound* | Perform history expansion on the current line and insert a space. |
| alias-expand-line | *Unbound* | Perform alias expansion on the current line. |
| history-and-alias-expand-line | *Unbound* | Perform history and alias expansion on the current line. |
| insert-last-argument | ```M-.``` or ```M-_``` | A synonym for yank-last-arg. |
| operate-and-get-next | ```C-o``` | Accept the current line for execution and fetch the next line relative to the current line from the history for editing. Any argument is ignored. |
| edit-and-execute-command | ```C-x C-e``` | Invoke an editor on the current command line, and execute the result as shell commands. Bash attempts to invoke **$VISUAL**, **$EDITOR**, and emacs as the editor, in that order. |

<p/>

## Readline vi Mode

While the Readline library does not have a full set of **vi** editing functions, it does contain enough to allow simple editing of the line. The Readline **vi** mode behaves as specified in the POSIX standard.

In order to switch interactively between **emacs** and **vi** editing modes, use the ```set -o emacs``` and ```set -o vi``` commands (see [The *set* Builtin](#the-em-set-em-builtin)). **The Readline default is emacs mode**.

When you enter a line in **vi** mode, you are already placed in **insertion** mode, as if you had typed an ***i***. Pressing **ESC** switches you into **command** mode, where you can edit the text of the line with the standard **vi** movement keys, move to previous history lines with ```k``` and subsequent lines with ```j```, and so forth.

## Programmable Completion

When word completion is attempted for an argument to a command for which a completion specification (a *compspec*) has been defined using the **complete** builtin (see [Programmable Completion Builtins](#programmable-completion-builtins)), the programmable completion facilities are invoked.

First, the command name is identified. If a *compspec* has been defined for that command, the *compspec* is used to generate the list of possible completions for the word. If the command word is the empty string (completion attempted at the beginning of an empty line), any *compspec* defined with the ```-E``` option to **complete** is used. If the command word is a full pathname, a *compspec* for the full pathname is searched for first. If no *compspec* is found for the full pathname, an attempt is made to find a *compspec* for the portion following the final slash. If those searches do not result in a *compspec*, any *compspec* defined with the ```-D``` option to **complete** is used as the default.

Once a *compspec* has been found, it is used to generate the list of matching words. If a *compspec* is not found, the default Bash completion described in [Letting Readline Type For You](#letting-readline-type-for-you) is performed.

First, the actions specified by the *compspec* are used. Only matches which are prefixed by the word being completed are returned. When the ```-f``` or ```-d``` option is used for filename or directory name completion, the shell variable **FIGNORE** is used to filter the matches.

Any completions specified by a filename expansion pattern to the ```-G``` option are generated next. The words generated by the pattern need not match the word being completed. The **GLOBIGNORE** shell variable is not used to filter the matches, but the **FIGNORE** shell variable is used.

Next, the string specified as the argument to the ```-W``` option is considered. The string is first split using the characters in the **IFS** special variable as delimiters. Shell quoting is honored. Each word is then expanded using brace expansion, tilde expansion, parameter and variable expansion, command substitution, and arithmetic expansion, as described in [Shell Expansions](#shell-expansions). The results are split using the rules described in [Word Splitting](#word-splitting). The results of the expansion are prefix-matched against the word being completed, and the matching words become the possible completions.

After these matches have been generated, any shell function or command specified with the ```-F``` and ```-C``` options is invoked. When the command or function is invoked, the **COMP_LINE**, **COMP_POINT**, **COMP_KEY**, and **COMP_TYPE** variables are assigned values as described in [Bash Variables](#bash-variables). If a shell function is being invoked, the **COMP_WORDS** and **COMP_CWORD** variables are also set. When the function or command is invoked, the first argument (**$1**) is the name of the command whose arguments are being completed, the second argument (**$2**) is the word being completed, and the third argument (**$3**) is the word preceding the word being completed on the current command line. No filtering of the generated completions against the word being completed is performed; the function or command has complete freedom in generating the matches.

Any function specified with ```-F``` is invoked first. The function may use any of the shell facilities, including the **compgen** and **compopt** builtins described in [Programmable Completion Builtins](#programmable-completion-builtins), to generate the matches. It must put the possible completions in the **COMPREPLY** array variable, one per array element.

Next, any command specified with the ```-C``` option is invoked in an environment equivalent to command substitution. It should print a list of completions, one per line, to the standard output. Backslash may be used to escape a newline, if necessary.

After all of the possible completions are generated, any filter specified with the ```-X``` option is applied to the list. The filter is a pattern as used for pathname expansion; a ```&``` in the pattern is replaced with the text of the word being completed. A literal ```&``` may be escaped with a backslash; the backslash is removed before attempting a match. Any completion that matches the pattern will be removed from the list. A leading ```!``` negates the pattern; in this case any completion not matching the pattern will be removed.

Finally, any prefix and suffix specified with the ```-P``` and ```-S``` options are added to each member of the completion list, and the result is returned to the Readline completion code as the list of possible completions.

If the previously-applied actions do not generate any matches, and the ```-o dirnames``` option was supplied to **complete** when the *compspec* was defined, directory name completion is attempted.

If the ```-o plusdirs``` option was supplied to **complete** when the compspec was defined, directory name completion is attempted and any matches are added to the results of the other actions.

By default, if a *compspec* is found, whatever it generates is returned to the completion code as the full set of possible completions. The default Bash completions are not attempted, and the Readline default of filename completion is disabled. If the ```-o bashdefault``` option was supplied to **complete** when the *compspec* was defined, the default Bash completions are attempted if the *compspec* generates no matches. If the ```-o default``` option was supplied to **complete** when the *compspec* was defined, Readline's default completion will be performed if the *compspec* (and, if attempted, the default Bash completions) generate no matches.

When a *compspec* indicates that directory name completion is desired, the programmable completion functions force Readline to append a slash to completed names which are symbolic links to directories, subject to the value of the *mark-directories* Readline variable, regardless of the setting of the *mark-symlinked-directories* Readline variable.

There is some support for dynamically modifying completions. This is most useful when used in combination with a default completion specified with ```-D```. It's possible for shell functions executed as completion handlers to indicate that completion should be retried by returning an exit status of **124**. If a shell function returns **124**, and changes the *compspec* associated with the command on which completion is being attempted (supplied as the first argument when the function is executed), programmable completion restarts from the beginning, with an attempt to find a new *compspec* for that command. This allows a set of completions to be built dynamically as completion is attempted, rather than being loaded all at once.

For instance, assuming that there is a library of *compspecs*, each kept in a file corresponding to the name of the command, the following default completion function would load completions dynamically:

```
_completion_loader()
{
    . "/etc/bash_completion.d/$1.sh" >/dev/null 2>&1 && return 124
}
complete -D -F _completion_loader -o bashdefault -o default
```

## Programmable Completion Builtins

Three builtin commands are available to manipulate the programmable completion facilities: one to specify how the arguments to a particular command are to be completed, and two to modify the completion as it is happening.

| Builtins | Description |
| :------- | :---------- |
| **compgen**  | Format:<br>```compgen [option] [word]```<br><br>Generate possible completion matches for *word* according to the *options*, which may be any option accepted by the **complete** builtin with the exception of ```-p``` and ```-r```, and write the matches to the standard output. When using the ```-F``` or ```-C``` options, the various shell variables set by the programmable completion facilities, while available, will not have useful values.<br><br>The matches will be generated in the same way as if the programmable completion code had generated them directly from a completion specification with the same flags. If *word* is specified, only those completions matching *word* will be displayed.<br><br>The return value is **true** unless an invalid option is supplied, or no matches were generated. |
| **complete** | Format #1:<br>```complete [-abcdefgjksuv] [-o comp-option] [-DE] [-A action] [-G globpat] [-W wordlist] [-F function] [-C command] [-X filterpat] [-P prefix] [-S suffix] name [name ...]```<br><br>Format #2:<br>```complete -pr [-DE] [name ...]```<br><br>Specify how arguments to each *name* should be completed.<br><br>If the ```-p``` option is supplied, or if no options are supplied, existing completion specifications are printed in a way that allows them to be reused as input.<br>The ```-r``` option removes a completion specification for each *name*, or, if no *names* are supplied, all completion specifications.<br><br>The ```-D``` option indicates that the remaining options and actions should apply to the **default command completion**; that is, completion attempted on a command for which no completion has previously been defined.<br>The ```-E``` option indicates that the remaining options and actions should apply to **empty command completion**; that is, completion attempted on a blank line.<br>The ```-D``` option takes precedence over ```-E```.<br><br>The process of applying these completion specifications when word completion is attempted is described in [Programmable Completion](#programmable-completion).<br><br>Other options, if specified, have the following meanings (see ***8.7 Programmable Completion Builtins*** of **Bash Reference Manual v4.3** for details). The arguments to the ```-G```, ```-W```, and ```-X``` options (and, if necessary, the ```-P``` and ```-S``` options) should be quoted to protect them from expansion before the **complete** builtin is invoked.<br><br>```-o comp-option```<br>The *comp-option* controls several aspects of the *compspec*'s behavior beyond the simple generation of completions. *comp-option* may be one of:<br>```bashdefault```: Perform the rest of the default Bash completions if the *compspec* generates no matches.<br>```default```: Use Readline's default filename completion if the *compspec* generates no matches.<br>```dirnames```: Perform directory name completion if the *compspec* generates no matches.<br>```filenames```: Tell Readline that the *compspec* generates filenames, so it can perform any filename-specific processing (like adding a slash to directory names quoting special characters, or suppressing trailing spaces). This option is intended to be used with shell functions specified with ```-F```.<br>```noquote```: Tell Readline not to quote the completed words if they are filenames (quoting filenames is the default).<br>```nospace```: Tell Readline not to append a space (the default) to words completed at the end of the line.<br>```plusdirs```: After any matches defined by the *compspec* are generated, directory name completion is attempted and any matches are added to the results of the other actions.<br><br>```-A action```<br>The *action* may be one of the following to generate a list of possible completions:<br>```alias```: Alias names. May also be specified as ```-a```.<br>```arrayvar```: Array variable names.<br>```binding```: Readline key binding names.<br>```builtin```: Names of shell builtin commands. May also be specified as ```-b```.<br>```command```: Command names. May also be specified as ```-c```.<br>```directory```: Directory names. May also be specified as ```-d```.<br>```disabled```: Names of disabled shell builtins.<br>```enabled```: Names of enabled shell builtins.<br>```export```: Names of exported shell variables. May also be specified as ```-e```.<br>```file```: File names. May also be specified as ```-f```.<br>```function```: Names of shell functions.<br>```group```: Group names. May also be specified as ```-g```.<br>```helptopic```: Help topics as accepted by the *help* builtin.<br>```hostname```: Hostnames, as taken from the file specified by the **HOSTFILE** shell variable.<br>```job```: Job names, if job control is active. May also be specified as ```-j```.<br>```keyword```: Shell reserved words. May also be specified as ```-k```.<br>```running```: Names of running jobs, if job control is active.<br>```service```: Service names. May also be specified as ```-s```.<br>```setopt```: Valid arguments for the ```-o``` option to the *set* builtin.<br>```shopt```: Shell option names as accepted by the *shopt* builtin.<br>```signal```： Signal names.<br>```stopped```： Names of stopped jobs, if job control is active.<br>```user```： User names. May also be specified as ```-u```.<br>```variable```：Names of all shell variables. May also be specified as ```-v```. <br><br>```-C command```<br>*command* is executed in a subshell environment, and its output is used as the possible completions.<br><br>```-F function```<br>The shell function *function* is executed in the current shell environment. When it is executed, **$1** is the name of the command whose arguments are being completed, **$2** is the word being completed, and **$3** is the word preceding the word being completed, as described in [Programmable Completion](#programmable-completion). When it finishes, the possible completions are retrieved from the value of the **COMPREPLY** array variable.<br><br>```-G globpat```<br>The filename expansion pattern globpat is expanded to generate the possible completions.<br><br>```-P prefix```<br>*prefix* is added at the beginning of each possible completion after all other options have been applied.<br><br>```-S suffix```<br>*suffix* is appended to each possible completion after all other options have been applied.<br><br>```-W wordlist```<br>The *wordlist* is split using the characters in the **IFS** special variable as delimiters, and each resultant word is expanded. The possible completions are the members of the resultant list which match the word being completed.<br><br>```-X filterpat```<br>*filterpat* is a pattern as used for filename expansion. It is applied to the list of possible completions generated by the preceding options and arguments, and each completion matching *filterpat* is removed from the list. A leading ```!``` in *filterpat* negates the pattern; in this case, any completion not matching *filterpat* is removed.<br><br>The return value is **true** unless an invalid option is supplied, an option other than ```-p``` or ```-r``` is supplied without a *name* argument, an attempt is made to remove a completion specification for a *name* for which no specification exists, or an error occurs adding a completion specification. |
| **compopt** | Format:<br>```compopt [-o option] [-DE] [+o option] [name]```<br><br>Modify completion options for each *name* according to the *options*, or for the currently-executing completion if no *names* are supplied.<br><br>If no *options* are given, display the completion options for each *name* or the current completion. The possible values of *option* are those valid for the **complete** builtin described above.<br><br>The ```-D``` option indicates that the remaining options should apply to the **default command completion**; that is, completion attempted on a command for which no completion has previously been defined.<br>The ```-E``` option indicates that the remaining options should apply to **empty command completion**; that is, completion attempted on a blank line.<br>The ```-D``` option takes precedence over ```-E```.<br><br>The return value is **true** unless an invalid option is supplied, an attempt is made to modify the options for a *name* for which no completion specification exists, or an output error occurs. |

<p/>

***Examples:***

```
chenwx@chenwx ~ $ complete
complete -F _minimal
complete -F _filedir_xspec freeamp
complete -F _service /etc/init.d/rc
complete -F _service /etc/init.d/sendsigs
complete -F _service service
complete -o filenames -d -X '.[^./]*' -F _loexp_ unopkg
complete -F _filedir_xspec bibtex
complete -F _longopt strip
complete -F _filedir_xspec chromium-browser
complete -F _filedir_xspec tex
complete -F _filedir_xspec zathura
complete -F _command time
complete -F _command do
complete -F _service /etc/init.d/cryptdisks
complete -c which
complete -F _service /etc/init.d/kmod
complete -o filenames -F _grub_mkconfig grub-mkconfig
...

chenwx@chenwx ~ $ compopt cd
compopt +o bashdefault +o default +o dirnames +o filenames -o nospace +o plusdirs cd

chenwx@chenwx ~ $ compopt ls
compopt +o bashdefault +o default +o dirnames +o filenames +o nospace +o plusdirs ls

chenwx@chenwx ~ $ compopt bcompare
bash: compopt: bcompare: no completion specification
```

## Programmable Completion Configuration

This section shows the programmable completion configuration on my laptop:

```
chenwx@chenwx ~ $ lsb_release -a
No LSB modules are available.
Distributor ID:	LinuxMint
Description:	Linux Mint 17 Qiana
Release:	17
Codename:	qiana

chenwx@chenwx ~ $ uname -a
Linux chenwx 4.2.0-19-generic #23~14.04.1-Ubuntu SMP Thu Nov 12 12:33:30 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux
```

First, the */etc/profile* will execute the code from file */etc/bash.bashrc*：

```
chenwx@chenwx ~ $ cat /etc/profile
# /etc/profile: system-wide .profile file for the Bourne shell (sh(1))
# and Bourne compatible shells (bash(1), ksh(1), ash(1), ...).

if [ "$PS1" ]; then
  if [ "$BASH" ] && [ "$BASH" != "/bin/sh" ]; then
    # The file bash.bashrc already sets the default PS1.
    # PS1='\h:\w\$ '
    if [ -f /etc/bash.bashrc ]; then
      . /etc/bash.bashrc
    fi
  else
    if [ "`id -u`" -eq 0 ]; then
      PS1='# '
    else
      PS1='$ '
    fi
  fi
fi
```

Second, the */etc/bash.bashrc* will execute the code from file */etc/bash_completion*:

```
...
# enable bash completion in interactive shells
if [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi
...
```

Then, the */etc/bash_completion* will execute code from */usr/share/bash-completion/bash_completion*:

```
chenwx@chenwx ~ $ cat /etc/bash_completion
. /usr/share/bash-completion/bash_completion
```

Finally, the */usr/share/bash-completion/bash_completion* contains the programmable completion configurations:

```
#                                                          -*- shell-script -*-
#
#   bash_completion - programmable completion functions for bash 4.1+
#
#   Copyright © 2006-2008, Ian Macdonald <ian@caliban.org>
#             © 2009-2013, Bash Completion Maintainers
#                     <bash-completion-devel@lists.alioth.debian.org>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2, or (at your option)
#   any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#   The latest version of this software can be obtained here:
#
#   http://bash-completion.alioth.debian.org/
#
#   RELEASE: 2.1

if [[ $- == *v* ]]; then
    BASH_COMPLETION_ORIGINAL_V_VALUE="-v"
else
    BASH_COMPLETION_ORIGINAL_V_VALUE="+v"
fi

if [[ ${BASH_COMPLETION_DEBUG-} ]]; then
    set -v
else
    set +v
fi

# Set the following to the location of the backwards compat completion dir.
#
: ${BASH_COMPLETION_COMPAT_DIR:=/etc/bash_completion.d}
readonly BASH_COMPLETION_COMPAT_DIR

# Blacklisted completions, causing problems with our code.
#
_blacklist_glob='@(acroread.sh)'

# Turn on extended globbing and programmable completion
shopt -s extglob progcomp

# A lot of the following one-liners were taken directly from the
# completion examples provided with the bash 2.04 source distribution

# Make directory commands see only directories
complete -d pushd

# start of section containing compspecs that can be handled within bash

# user commands see only users
complete -u write chfn groups slay w sux runuser

# bg completes with stopped jobs
complete -A stopped -P '"%' -S '"' bg

# other job commands
complete -j -P '"%' -S '"' fg jobs disown

# readonly and unset complete with shell variables
complete -v readonly unset

# set completes with set options
complete -A setopt set

# shopt completes with shopt options
complete -A shopt shopt

# helptopics
complete -A helptopic help

# unalias completes with aliases
complete -a unalias

# bind completes with readline bindings (make this more intelligent)
complete -A binding bind

# type and which complete on commands
complete -c command type which

# builtin completes on builtins
complete -b builtin

# start of section containing completion functions called by other functions

# Check if we're running on the given userland
# @param $1 userland to check for
_userland()
{
    local userland=$( uname -s )
    [[ $userland == @(Linux|GNU/*) ]] && userland=GNU
    [[ $userland == $1 ]]
}

# This function sets correct SysV init directories
#
_sysvdirs()
{
    sysvdirs=( )
    [[ -d /etc/rc.d/init.d ]] && sysvdirs+=( /etc/rc.d/init.d )
    [[ -d /etc/init.d ]] && sysvdirs+=( /etc/init.d )
    # Slackware uses /etc/rc.d
    [[ -f /etc/slackware-version ]] && sysvdirs=( /etc/rc.d )
}

# This function checks whether we have a given program on the system.
#
_have()
{
    # Completions for system administrator commands are installed as well in
    # case completion is attempted via `sudo command ...'.
    PATH=$PATH:/usr/sbin:/sbin:/usr/local/sbin type $1 &>/dev/null
}

# Backwards compatibility for compat completions that use have().
# @deprecated should no longer be used; generally not needed with dynamically
#             loaded completions, and _have is suitable for runtime use.
have()
{
    unset -v have
    _have $1 && have=yes
}

# This function checks whether a given readline variable
# is `on'.
#
_rl_enabled()
{
    [[ "$( bind -v )" = *$1+([[:space:]])on* ]]
}

# This function shell-quotes the argument
quote()
{
    local quoted=${1//\'/\'\\\'\'}
    printf "'%s'" "$quoted"
}

# @see _quote_readline_by_ref()
quote_readline()
{
    local quoted
    _quote_readline_by_ref "$1" ret
    printf %s "$ret"
} # quote_readline()


# This function shell-dequotes the argument
dequote()
{
    eval printf %s "$1" 2> /dev/null
}


# Assign variable one scope above the caller
# Usage: local "$1" && _upvar $1 "value(s)"
# Param: $1  Variable name to assign value to
# Param: $*  Value(s) to assign.  If multiple values, an array is
#            assigned, otherwise a single value is assigned.
# NOTE: For assigning multiple variables, use '_upvars'.  Do NOT
#       use multiple '_upvar' calls, since one '_upvar' call might
#       reassign a variable to be used by another '_upvar' call.
# See: http://fvue.nl/wiki/Bash:_Passing_variables_by_reference
_upvar()
{
    if unset -v "$1"; then           # Unset & validate varname
        if (( $# == 2 )); then
            eval $1=\"\$2\"          # Return single value
        else
            eval $1=\(\"\${@:2}\"\)  # Return array
        fi
    fi
}


# Assign variables one scope above the caller
# Usage: local varname [varname ...] &&
#        _upvars [-v varname value] | [-aN varname [value ...]] ...
# Available OPTIONS:
#     -aN  Assign next N values to varname as array
#     -v   Assign single value to varname
# Return: 1 if error occurs
# See: http://fvue.nl/wiki/Bash:_Passing_variables_by_reference
_upvars()
{
    if ! (( $# )); then
        echo "${FUNCNAME[0]}: usage: ${FUNCNAME[0]} [-v varname"\
            "value] | [-aN varname [value ...]] ..." 1>&2
        return 2
    fi
    while (( $# )); do
        case $1 in
            -a*)
                # Error checking
                [[ ${1#-a} ]] || { echo "bash: ${FUNCNAME[0]}: \`$1': missing"\
                    "number specifier" 1>&2; return 1; }
                printf %d "${1#-a}" &> /dev/null || { echo "bash:"\
                    "${FUNCNAME[0]}: \`$1': invalid number specifier" 1>&2
                    return 1; }
                # Assign array of -aN elements
                [[ "$2" ]] && unset -v "$2" && eval $2=\(\"\${@:3:${1#-a}}\"\) &&
                shift $((${1#-a} + 2)) || { echo "bash: ${FUNCNAME[0]}:"\
                    "\`$1${2+ }$2': missing argument(s)" 1>&2; return 1; }
                ;;
            -v)
                # Assign single value
                [[ "$2" ]] && unset -v "$2" && eval $2=\"\$3\" &&
                shift 3 || { echo "bash: ${FUNCNAME[0]}: $1: missing"\
                "argument(s)" 1>&2; return 1; }
                ;;
            *)
                echo "bash: ${FUNCNAME[0]}: $1: invalid option" 1>&2
                return 1 ;;
        esac
    done
}


# Reassemble command line words, excluding specified characters from the
# list of word completion separators (COMP_WORDBREAKS).
# @param $1 chars  Characters out of $COMP_WORDBREAKS which should
#     NOT be considered word breaks. This is useful for things like scp where
#     we want to return host:path and not only path, so we would pass the
#     colon (:) as $1 here.
# @param $2 words  Name of variable to return words to
# @param $3 cword  Name of variable to return cword to
#
__reassemble_comp_words_by_ref()
{
    local exclude i j line ref
    # Exclude word separator characters?
    if [[ $1 ]]; then
        # Yes, exclude word separator characters;
        # Exclude only those characters, which were really included
        exclude="${1//[^$COMP_WORDBREAKS]}"
    fi

    # Default to cword unchanged
    eval $3=$COMP_CWORD
    # Are characters excluded which were former included?
    if [[ $exclude ]]; then
        # Yes, list of word completion separators has shrunk;
        line=$COMP_LINE
        # Re-assemble words to complete
        for (( i=0, j=0; i < ${#COMP_WORDS[@]}; i++, j++)); do
            # Is current word not word 0 (the command itself) and is word not
            # empty and is word made up of just word separator characters to
            # be excluded and is current word not preceded by whitespace in
            # original line?
            while [[ $i -gt 0 && ${COMP_WORDS[$i]} == +([$exclude]) ]]; do
                # Is word separator not preceded by whitespace in original line
                # and are we not going to append to word 0 (the command
                # itself), then append to current word.
                [[ $line != [$' \t']* ]] && (( j >= 2 )) && ((j--))
                # Append word separator to current or new word
                ref="$2[$j]"
                eval $2[$j]=\${!ref}\${COMP_WORDS[i]}
                # Indicate new cword
                [[ $i == $COMP_CWORD ]] && eval $3=$j
                # Remove optional whitespace + word separator from line copy
                line=${line#*"${COMP_WORDS[$i]}"}
                # Start new word if word separator in original line is
                # followed by whitespace.
                [[ $line == [$' \t']* ]] && ((j++))
                # Indicate next word if available, else end *both* while and
                # for loop
                (( $i < ${#COMP_WORDS[@]} - 1)) && ((i++)) || break 2
            done
            # Append word to current word
            ref="$2[$j]"
            eval $2[$j]=\${!ref}\${COMP_WORDS[i]}
            # Remove optional whitespace + word from line copy
            line=${line#*"${COMP_WORDS[i]}"}
            # Indicate new cword
            [[ $i == $COMP_CWORD ]] && eval $3=$j
        done
        [[ $i == $COMP_CWORD ]] && eval $3=$j
    else
        # No, list of word completions separators hasn't changed;
        eval $2=\( \"\${COMP_WORDS[@]}\" \)
    fi
} # __reassemble_comp_words_by_ref()


# @param $1 exclude  Characters out of $COMP_WORDBREAKS which should NOT be
#     considered word breaks. This is useful for things like scp where
#     we want to return host:path and not only path, so we would pass the
#     colon (:) as $1 in this case.
# @param $2 words  Name of variable to return words to
# @param $3 cword  Name of variable to return cword to
# @param $4 cur  Name of variable to return current word to complete to
# @see __reassemble_comp_words_by_ref()
__get_cword_at_cursor_by_ref()
{
    local cword words=()
    __reassemble_comp_words_by_ref "$1" words cword

    local i cur index=$COMP_POINT lead=${COMP_LINE:0:$COMP_POINT}
    # Cursor not at position 0 and not leaded by just space(s)?
    if [[ $index -gt 0 && ( $lead && ${lead//[[:space:]]} ) ]]; then
        cur=$COMP_LINE
        for (( i = 0; i <= cword; ++i )); do
            while [[
                # Current word fits in $cur?
                ${#cur} -ge ${#words[i]} &&
                # $cur doesn't match cword?
                "${cur:0:${#words[i]}}" != "${words[i]}"
            ]]; do
                # Strip first character
                cur="${cur:1}"
                # Decrease cursor position
                ((index--))
            done

            # Does found word match cword?
            if [[ $i -lt $cword ]]; then
                # No, cword lies further;
                local old_size=${#cur}
                cur="${cur#"${words[i]}"}"
                local new_size=${#cur}
                index=$(( index - old_size + new_size ))
            fi
        done
        # Clear $cur if just space(s)
        [[ $cur && ! ${cur//[[:space:]]} ]] && cur=
        # Zero $index if negative
        [[ $index -lt 0 ]] && index=0
    fi

    local "$2" "$3" "$4" && _upvars -a${#words[@]} $2 "${words[@]}" \
        -v $3 "$cword" -v $4 "${cur:0:$index}"
}


# Get the word to complete and optional previous words.
# This is nicer than ${COMP_WORDS[$COMP_CWORD]}, since it handles cases
# where the user is completing in the middle of a word.
# (For example, if the line is "ls foobar",
# and the cursor is here -------->   ^
# Also one is able to cross over possible wordbreak characters.
# Usage: _get_comp_words_by_ref [OPTIONS] [VARNAMES]
# Available VARNAMES:
#     cur         Return cur via $cur
#     prev        Return prev via $prev
#     words       Return words via $words
#     cword       Return cword via $cword
#
# Available OPTIONS:
#     -n EXCLUDE  Characters out of $COMP_WORDBREAKS which should NOT be
#                 considered word breaks. This is useful for things like scp
#                 where we want to return host:path and not only path, so we
#                 would pass the colon (:) as -n option in this case.
#     -c VARNAME  Return cur via $VARNAME
#     -p VARNAME  Return prev via $VARNAME
#     -w VARNAME  Return words via $VARNAME
#     -i VARNAME  Return cword via $VARNAME
#
# Example usage:
#
#    $ _get_comp_words_by_ref -n : cur prev
#
_get_comp_words_by_ref()
{
    local exclude flag i OPTIND=1
    local cur cword words=()
    local upargs=() upvars=() vcur vcword vprev vwords

    while getopts "c:i:n:p:w:" flag "$@"; do
        case $flag in
            c) vcur=$OPTARG ;;
            i) vcword=$OPTARG ;;
            n) exclude=$OPTARG ;;
            p) vprev=$OPTARG ;;
            w) vwords=$OPTARG ;;
        esac
    done
    while [[ $# -ge $OPTIND ]]; do
        case ${!OPTIND} in
            cur)   vcur=cur ;;
            prev)  vprev=prev ;;
            cword) vcword=cword ;;
            words) vwords=words ;;
            *) echo "bash: $FUNCNAME(): \`${!OPTIND}': unknown argument" \
                1>&2; return 1
        esac
        let "OPTIND += 1"
    done

    __get_cword_at_cursor_by_ref "$exclude" words cword cur

    [[ $vcur   ]] && { upvars+=("$vcur"  ); upargs+=(-v $vcur   "$cur"  ); }
    [[ $vcword ]] && { upvars+=("$vcword"); upargs+=(-v $vcword "$cword"); }
    [[ $vprev && $cword -ge 1 ]] && { upvars+=("$vprev" ); upargs+=(-v $vprev
        "${words[cword - 1]}"); }
    [[ $vwords ]] && { upvars+=("$vwords"); upargs+=(-a${#words[@]} $vwords
        "${words[@]}"); }

    (( ${#upvars[@]} )) && local "${upvars[@]}" && _upvars "${upargs[@]}"
}


# Get the word to complete.
# This is nicer than ${COMP_WORDS[$COMP_CWORD]}, since it handles cases
# where the user is completing in the middle of a word.
# (For example, if the line is "ls foobar",
# and the cursor is here -------->   ^
# @param $1 string  Characters out of $COMP_WORDBREAKS which should NOT be
#     considered word breaks. This is useful for things like scp where
#     we want to return host:path and not only path, so we would pass the
#     colon (:) as $1 in this case.
# @param $2 integer  Index number of word to return, negatively offset to the
#     current word (default is 0, previous is 1), respecting the exclusions
#     given at $1.  For example, `_get_cword "=:" 1' returns the word left of
#     the current word, respecting the exclusions "=:".
# @deprecated  Use `_get_comp_words_by_ref cur' instead
# @see _get_comp_words_by_ref()
_get_cword()
{
    local LC_CTYPE=C
    local cword words
    __reassemble_comp_words_by_ref "$1" words cword

    # return previous word offset by $2
    if [[ ${2//[^0-9]/} ]]; then
        printf "%s" "${words[cword-$2]}"
    elif [[ "${#words[cword]}" -eq 0 || "$COMP_POINT" == "${#COMP_LINE}" ]]; then
        printf "%s" "${words[cword]}"
    else
        local i
        local cur="$COMP_LINE"
        local index="$COMP_POINT"
        for (( i = 0; i <= cword; ++i )); do
            while [[
                # Current word fits in $cur?
                "${#cur}" -ge ${#words[i]} &&
                # $cur doesn't match cword?
                "${cur:0:${#words[i]}}" != "${words[i]}"
            ]]; do
                # Strip first character
                cur="${cur:1}"
                # Decrease cursor position
                ((index--))
            done

            # Does found word matches cword?
            if [[ "$i" -lt "$cword" ]]; then
                # No, cword lies further;
                local old_size="${#cur}"
                cur="${cur#${words[i]}}"
                local new_size="${#cur}"
                index=$(( index - old_size + new_size ))
            fi
        done

        if [[ "${words[cword]:0:${#cur}}" != "$cur" ]]; then
            # We messed up! At least return the whole word so things
            # keep working
            printf "%s" "${words[cword]}"
        else
            printf "%s" "${cur:0:$index}"
        fi
    fi
} # _get_cword()


# Get word previous to the current word.
# This is a good alternative to `prev=${COMP_WORDS[COMP_CWORD-1]}' because bash4
# will properly return the previous word with respect to any given exclusions to
# COMP_WORDBREAKS.
# @deprecated  Use `_get_comp_words_by_ref cur prev' instead
# @see _get_comp_words_by_ref()
#
_get_pword()
{
    if [[ $COMP_CWORD -ge 1 ]]; then
        _get_cword "${@:-}" 1
    fi
}


# If the word-to-complete contains a colon (:), left-trim COMPREPLY items with
# word-to-complete.
# With a colon in COMP_WORDBREAKS, words containing
# colons are always completed as entire words if the word to complete contains
# a colon.  This function fixes this, by removing the colon-containing-prefix
# from COMPREPLY items.
# The preferred solution is to remove the colon (:) from COMP_WORDBREAKS in
# your .bashrc:
#
#    # Remove colon (:) from list of word completion separators
#    COMP_WORDBREAKS=${COMP_WORDBREAKS//:}
#
# See also: Bash FAQ - E13) Why does filename completion misbehave if a colon
# appears in the filename? - http://tiswww.case.edu/php/chet/bash/FAQ
# @param $1 current word to complete (cur)
# @modifies global array $COMPREPLY
#
__ltrim_colon_completions()
{
    if [[ "$1" == *:* && "$COMP_WORDBREAKS" == *:* ]]; then
        # Remove colon-word prefix from COMPREPLY items
        local colon_word=${1%"${1##*:}"}
        local i=${#COMPREPLY[*]}
        while [[ $((--i)) -ge 0 ]]; do
            COMPREPLY[$i]=${COMPREPLY[$i]#"$colon_word"}
        done
    fi
} # __ltrim_colon_completions()


# This function quotes the argument in a way so that readline dequoting
# results in the original argument.  This is necessary for at least
# `compgen' which requires its arguments quoted/escaped:
#
#     $ ls "a'b/"
#     c
#     $ compgen -f "a'b/"       # Wrong, doesn't return output
#     $ compgen -f "a\'b/"      # Good
#     a\'b/c
#
# See also:
# - http://lists.gnu.org/archive/html/bug-bash/2009-03/msg00155.html
# - http://www.mail-archive.com/bash-completion-devel@lists.alioth.\
#   debian.org/msg01944.html
# @param $1  Argument to quote
# @param $2  Name of variable to return result to
_quote_readline_by_ref()
{
    if [ -z "$1" ]; then
        # avoid quoting if empty
        printf -v $2 %s "$1"
    elif [[ $1 == \'* ]]; then
        # Leave out first character
        printf -v $2 %s "${1:1}"
    elif [[ $1 == ~* ]]; then
        # avoid escaping first ~
        printf -v $2 ~%q "${1:1}"
    else
        printf -v $2 %q "$1"
    fi

    # Replace double escaping ( \\ ) by single ( \ )
    # This happens always when argument is already escaped at cmdline,
    # and passed to this function as e.g.: file\ with\ spaces
    [[ ${!2} == *\\* ]] && printf -v $2 %s "${1//\\\\/\\}"

    # If result becomes quoted like this: $'string', re-evaluate in order to
    # drop the additional quoting.  See also: http://www.mail-archive.com/
    # bash-completion-devel@lists.alioth.debian.org/msg01942.html
    [[ ${!2} == \$* ]] && eval $2=${!2}
} # _quote_readline_by_ref()


# This function performs file and directory completion. It's better than
# simply using 'compgen -f', because it honours spaces in filenames.
# @param $1  If `-d', complete only on directories.  Otherwise filter/pick only
#            completions with `.$1' and the uppercase version of it as file
#            extension.
#
_filedir()
{
    local i IFS=$'\n' xspec

    _tilde "$cur" || return 0

    local -a toks
    local quoted x tmp

    _quote_readline_by_ref "$cur" quoted
    x=$( compgen -d -- "$quoted" ) &&
    while read -r tmp; do
        toks+=( "$tmp" )
    done <<< "$x"

    if [[ "$1" != -d ]]; then
        # Munge xspec to contain uppercase version too
        # http://thread.gmane.org/gmane.comp.shells.bash.bugs/15294/focus=15306
        xspec=${1:+"!*.@($1|${1^^})"}
        x=$( compgen -f -X "$xspec" -- $quoted ) &&
        while read -r tmp; do
            toks+=( "$tmp" )
        done <<< "$x"
    fi

    # If the filter failed to produce anything, try without it if configured to
    [[ -n ${COMP_FILEDIR_FALLBACK:-} && \
        -n "$1" && "$1" != -d && ${#toks[@]} -lt 1 ]] && \
        x=$( compgen -f -- $quoted ) &&
        while read -r tmp; do
            toks+=( "$tmp" )
        done <<< "$x"


    if [[ ${#toks[@]} -ne 0 ]]; then
        # 2>/dev/null for direct invocation, e.g. in the _filedir unit test
        compopt -o filenames 2>/dev/null
        COMPREPLY+=( "${toks[@]}" )
    fi
} # _filedir()


# This function splits $cur=--foo=bar into $prev=--foo, $cur=bar, making it
# easier to support both "--foo bar" and "--foo=bar" style completions.
# `=' should have been removed from COMP_WORDBREAKS when setting $cur for
# this to be useful.
# Returns 0 if current option was split, 1 otherwise.
#
_split_longopt()
{
    if [[ "$cur" == --?*=* ]]; then
        # Cut also backslash before '=' in case it ended up there
        # for some reason.
        prev="${cur%%?(\\)=*}"
        cur="${cur#*=}"
        return 0
    fi

    return 1
}

# Complete variables.
# @return  True (0) if variables were completed,
#          False (> 0) if not.
_variables()
{
    if [[ $cur =~ ^(\$\{?)([A-Za-z0-9_]*)$ ]]; then
        [[ $cur == *{* ]] && local suffix=} || local suffix=
        COMPREPLY+=( $( compgen -P ${BASH_REMATCH[1]} -S "$suffix" -v -- \
            "${BASH_REMATCH[2]}" ) )
        return 0
    fi
    return 1
}

# Initialize completion and deal with various general things: do file
# and variable completion where appropriate, and adjust prev, words,
# and cword as if no redirections exist so that completions do not
# need to deal with them.  Before calling this function, make sure
# cur, prev, words, and cword are local, ditto split if you use -s.
#
# Options:
#     -n EXCLUDE  Passed to _get_comp_words_by_ref -n with redirection chars
#     -e XSPEC    Passed to _filedir as first arg for stderr redirections
#     -o XSPEC    Passed to _filedir as first arg for other output redirections
#     -i XSPEC    Passed to _filedir as first arg for stdin redirections
#     -s          Split long options with _split_longopt, implies -n =
# @return  True (0) if completion needs further processing,
#          False (> 0) no further processing is necessary.
#
_init_completion()
{
    local exclude= flag outx errx inx OPTIND=1

    while getopts "n:e:o:i:s" flag "$@"; do
        case $flag in
            n) exclude+=$OPTARG ;;
            e) errx=$OPTARG ;;
            o) outx=$OPTARG ;;
            i) inx=$OPTARG ;;
            s) split=false ; exclude+== ;;
        esac
    done

    # For some reason completion functions are not invoked at all by
    # bash (at least as of 4.1.7) after the command line contains an
    # ampersand so we don't get a chance to deal with redirections
    # containing them, but if we did, hopefully the below would also
    # do the right thing with them...

    COMPREPLY=()
    local redir="@(?([0-9])<|?([0-9&])>?(>)|>&)"
    _get_comp_words_by_ref -n "$exclude<>&" cur prev words cword

    # Complete variable names.
    _variables && return 1

    # Complete on files if current is a redirect possibly followed by a
    # filename, e.g. ">foo", or previous is a "bare" redirect, e.g. ">".
    if [[ $cur == $redir* || $prev == $redir ]]; then
        local xspec
        case $cur in
            2'>'*) xspec=$errx ;;
            *'>'*) xspec=$outx ;;
            *'<'*) xspec=$inx ;;
            *)
                case $prev in
                    2'>'*) xspec=$errx ;;
                    *'>'*) xspec=$outx ;;
                    *'<'*) xspec=$inx ;;
                esac
                ;;
        esac
        cur="${cur##$redir}"
        _filedir $xspec
        return 1
    fi

    # Remove all redirections so completions don't have to deal with them.
    local i skip
    for (( i=1; i < ${#words[@]}; )); do
        if [[ ${words[i]} == $redir* ]]; then
            # If "bare" redirect, remove also the next word (skip=2).
            [[ ${words[i]} == $redir ]] && skip=2 || skip=1
            words=( "${words[@]:0:i}" "${words[@]:i+skip}" )
            [[ $i -le $cword ]] && cword=$(( cword - skip ))
        else
            i=$(( ++i ))
        fi
    done

    [[ $cword -le 0 ]] && return 1
    prev=${words[cword-1]}

    [[ ${split-} ]] && _split_longopt && split=true

    return 0
}

# Helper function for _parse_help and _parse_usage.
__parse_options()
{
    local option option2 i IFS=$' \t\n,/|'

    # Take first found long option, or first one (short) if not found.
    option=
    for i in $1; do
        case $i in
            ---*) break ;;
            --?*) option=$i ; break ;;
            -?*)  [[ $option ]] || option=$i ;;
            *)    break ;;
        esac
    done
    [[ $option ]] || return 0

    IFS=$' \t\n' # affects parsing of the regexps below...

    # Expand --[no]foo to --foo and --nofoo etc
    if [[ $option =~ (\[((no|dont)-?)\]). ]]; then
        option2=${option/"${BASH_REMATCH[1]}"/}
        option2=${option2%%[<{().[]*}
        printf '%s\n' "${option2/=*/=}"
        option=${option/"${BASH_REMATCH[1]}"/"${BASH_REMATCH[2]}"}
    fi

    option=${option%%[<{().[]*}
    printf '%s\n' "${option/=*/=}"
}

# Parse GNU style help output of the given command.
# @param $1  command; if "-", read from stdin and ignore rest of args
# @param $2  command options (default: --help)
#
_parse_help()
{
    eval local cmd=$( quote "$1" )
    local line
    { case $cmd in
        -) cat ;;
        *) LC_ALL=C "$( dequote "$cmd" )" ${2:---help} 2>&1 ;;
      esac } \
    | while read -r line; do

        [[ $line == *([ $'\t'])-* ]] || continue
        # transform "-f FOO, --foo=FOO" to "-f , --foo=FOO" etc
        while [[ $line =~ \
            ((^|[^-])-[A-Za-z0-9?][[:space:]]+)\[?[A-Z0-9]+\]? ]]; do
            line=${line/"${BASH_REMATCH[0]}"/"${BASH_REMATCH[1]}"}
        done
        __parse_options "${line// or /, }"

    done
}

# Parse BSD style usage output (options in brackets) of the given command.
# @param $1  command; if "-", read from stdin and ignore rest of args
# @param $2  command options (default: --usage)
#
_parse_usage()
{
    eval local cmd=$( quote "$1" )
    local line match option i char
    { case $cmd in
        -) cat ;;
        *) LC_ALL=C "$( dequote "$cmd" )" ${2:---usage} 2>&1 ;;
      esac } \
    | while read -r line; do

        while [[ $line =~ \[[[:space:]]*(-[^]]+)[[:space:]]*\] ]]; do
            match=${BASH_REMATCH[0]}
            option=${BASH_REMATCH[1]}
            case $option in
                -?(\[)+([a-zA-Z0-9?]))
                    # Treat as bundled short options
                    for (( i=1; i < ${#option}; i++ )); do
                        char=${option:i:1}
                        [[ $char != '[' ]] && printf '%s\n' -$char
                    done
                    ;;
                *)
                    __parse_options "$option"
                    ;;
            esac
            line=${line#*"$match"}
        done

    done
}

# This function completes on signal names (minus the SIG prefix)
# @param $1 prefix
_signals()
{
    local -a sigs=( $( compgen -P "$1" -A signal "SIG${cur#$1}" ) )
    COMPREPLY+=( "${sigs[@]/#${1}SIG/${1}}" )
}

# This function completes on known mac addresses
#
_mac_addresses()
{
    local re='\([A-Fa-f0-9]\{2\}:\)\{5\}[A-Fa-f0-9]\{2\}'
    local PATH="$PATH:/sbin:/usr/sbin"

    # Local interfaces
    # - ifconfig on Linux: HWaddr or ether
    # - ifconfig on FreeBSD: ether
    # - ip link: link/ether
    COMPREPLY+=( $( \
        { LC_ALL=C ifconfig -a || ip link show; } 2>/dev/null | sed -ne \
        "s/.*[[:space:]]HWaddr[[:space:]]\{1,\}\($re\)[[:space:]].*/\1/p" -ne \
        "s/.*[[:space:]]HWaddr[[:space:]]\{1,\}\($re\)[[:space:]]*$/\1/p" -ne \
        "s|.*[[:space:]]\(link/\)\{0,1\}ether[[:space:]]\{1,\}\($re\)[[:space:]].*|\2|p" -ne \
        "s|.*[[:space:]]\(link/\)\{0,1\}ether[[:space:]]\{1,\}\($re\)[[:space:]]*$|\2|p"
        ) )

    # ARP cache
    COMPREPLY+=( $( { arp -an || ip neigh show; } 2>/dev/null | sed -ne \
        "s/.*[[:space:]]\($re\)[[:space:]].*/\1/p" -ne \
        "s/.*[[:space:]]\($re\)[[:space:]]*$/\1/p" ) )

    # /etc/ethers
    COMPREPLY+=( $( sed -ne \
        "s/^[[:space:]]*\($re\)[[:space:]].*/\1/p" /etc/ethers 2>/dev/null ) )

    COMPREPLY=( $( compgen -W '${COMPREPLY[@]}' -- "$cur" ) )
    __ltrim_colon_completions "$cur"
}

# This function completes on configured network interfaces
#
_configured_interfaces()
{
    if [[ -f /etc/debian_version ]]; then
        # Debian system
        COMPREPLY=( $( compgen -W "$( sed -ne 's|^iface \([^ ]\{1,\}\).*$|\1|p'\
            /etc/network/interfaces )" -- "$cur" ) )
    elif [[ -f /etc/SuSE-release ]]; then
        # SuSE system
        COMPREPLY=( $( compgen -W "$( printf '%s\n' \
            /etc/sysconfig/network/ifcfg-* | \
            sed -ne 's|.*ifcfg-\(.*\)|\1|p' )" -- "$cur" ) )
    elif [[ -f /etc/pld-release ]]; then
        # PLD Linux
        COMPREPLY=( $( compgen -W "$( command ls -B \
            /etc/sysconfig/interfaces | \
            sed -ne 's|.*ifcfg-\(.*\)|\1|p' )" -- "$cur" ) )
    else
        # Assume Red Hat
        COMPREPLY=( $( compgen -W "$( printf '%s\n' \
            /etc/sysconfig/network-scripts/ifcfg-* | \
            sed -ne 's|.*ifcfg-\(.*\)|\1|p' )" -- "$cur" ) )
    fi
}

# Local IP addresses.
#
_ip_addresses()
{
    local PATH=$PATH:/sbin
    COMPREPLY+=( $( compgen -W \
        "$( { LC_ALL=C ifconfig -a || ip addr show; } 2>/dev/null |
            sed -ne 's/.*addr:\([^[:space:]]*\).*/\1/p' \
                -ne 's|.*inet[[:space:]]\{1,\}\([^[:space:]/]*\).*|\1|p' )" \
        -- "$cur" ) )
}

# This function completes on available kernels
#
_kernel_versions()
{
    COMPREPLY=( $( compgen -W '$( command ls /lib/modules )' -- "$cur" ) )
}

# This function completes on all available network interfaces
# -a: restrict to active interfaces only
# -w: restrict to wireless interfaces only
#
_available_interfaces()
{
    local cmd PATH=$PATH:/sbin

    if [[ ${1:-} == -w ]]; then
        cmd="iwconfig"
    elif [[ ${1:-} == -a ]]; then
        cmd="{ ifconfig || ip link show up; }"
    else
        cmd="{ ifconfig -a || ip link show; }"
    fi

    COMPREPLY=( $( eval $cmd 2>/dev/null | awk \
        '/^[^ \t]/ { if ($1 ~ /^[0-9]+:/) { print $2 } else { print $1 } }' ) )
    COMPREPLY=( $( compgen -W '${COMPREPLY[@]/%[[:punct:]]/}' -- "$cur" ) )
}

# Echo number of CPUs, falling back to 1 on failure.
_ncpus()
{
    local var=NPROCESSORS_ONLN
    [[ $OSTYPE == *linux* ]] && var=_$var
    local n=$( getconf $var 2>/dev/null )
    printf %s ${n:-1}
}

# Perform tilde (~) completion
# @return  True (0) if completion needs further processing,
#          False (> 0) if tilde is followed by a valid username, completions
#          are put in COMPREPLY and no further processing is necessary.
_tilde()
{
    local result=0
    if [[ $1 == \~* && $1 != */* ]]; then
        # Try generate ~username completions
        COMPREPLY=( $( compgen -P '~' -u "${1#\~}" ) )
        result=${#COMPREPLY[@]}
        # 2>/dev/null for direct invocation, e.g. in the _tilde unit test
        [[ $result -gt 0 ]] && compopt -o filenames 2>/dev/null
    fi
    return $result
}


# Expand variable starting with tilde (~)
# We want to expand ~foo/... to /home/foo/... to avoid problems when
# word-to-complete starting with a tilde is fed to commands and ending up
# quoted instead of expanded.
# Only the first portion of the variable from the tilde up to the first slash
# (~../) is expanded.  The remainder of the variable, containing for example
# a dollar sign variable ($) or asterisk (*) is not expanded.
# Example usage:
#
#    $ v="~"; __expand_tilde_by_ref v; echo "$v"
#
# Example output:
#
#       v                  output
#    --------         ----------------
#    ~                /home/user
#    ~foo/bar         /home/foo/bar
#    ~foo/$HOME       /home/foo/$HOME
#    ~foo/a  b        /home/foo/a  b
#    ~foo/*           /home/foo/*
#
# @param $1  Name of variable (not the value of the variable) to expand
__expand_tilde_by_ref()
{
    # Does $1 start with tilde (~)?
    if [[ ${!1} == \~* ]]; then
        # Does $1 contain slash (/)?
        if [[ ${!1} == */* ]]; then
            # Yes, $1 contains slash;
            # 1: Remove * including and after first slash (/), i.e. "~a/b"
            #    becomes "~a".  Double quotes allow eval.
            # 2: Remove * before the first slash (/), i.e. "~a/b"
            #    becomes "b".  Single quotes prevent eval.
            #       +-----1----+ +---2----+
            eval $1="${!1/%\/*}"/'${!1#*/}'
        else
            # No, $1 doesn't contain slash
            eval $1="${!1}"
        fi
    fi
} # __expand_tilde_by_ref()


# This function expands tildes in pathnames
#
_expand()
{
    # FIXME: Why was this here?
    #[ "$cur" != "${cur%\\}" ] && cur+="\\"

    # Expand ~username type directory specifications.  We want to expand
    # ~foo/... to /home/foo/... to avoid problems when $cur starting with
    # a tilde is fed to commands and ending up quoted instead of expanded.

    if [[ "$cur" == \~*/* ]]; then
        eval cur=$cur 2>/dev/null
    elif [[ "$cur" == \~* ]]; then
        cur=${cur#\~}
        COMPREPLY=( $( compgen -P '~' -u "$cur" ) )
        [[ ${#COMPREPLY[@]} -eq 1 ]] && eval COMPREPLY[0]=${COMPREPLY[0]}
        return ${#COMPREPLY[@]}
    fi
}

# This function completes on process IDs.
# AIX and Solaris ps prefers X/Open syntax.
[[ $OSTYPE == *@(solaris|aix)* ]] &&
_pids()
{
    COMPREPLY=( $( compgen -W '$( command ps -efo pid | sed 1d )' -- "$cur" ))
} ||
_pids()
{
    COMPREPLY=( $( compgen -W '$( command ps axo pid= )' -- "$cur" ) )
}

# This function completes on process group IDs.
# AIX and SunOS prefer X/Open, all else should be BSD.
[[ $OSTYPE == *@(solaris|aix)* ]] &&
_pgids()
{
    COMPREPLY=( $( compgen -W '$( command ps -efo pgid | sed 1d )' -- "$cur" ))
} ||
_pgids()
{
    COMPREPLY=( $( compgen -W '$( command ps axo pgid= )' -- "$cur" ))
}

# This function completes on process names.
# AIX and SunOS prefer X/Open, all else should be BSD.
[[ $OSTYPE == *@(solaris|aix)* ]] &&
_pnames()
{
    COMPREPLY=( $( compgen -X '<defunct>' -W '$( command ps -efo comm | \
        sed -e 1d -e "s:.*/::" -e "s/^-//" | sort -u )' -- "$cur" ) )
} ||
_pnames()
{
    # FIXME: completes "[kblockd/0]" to "0". Previously it was completed
    # to "kblockd" which isn't correct either. "kblockd/0" would be
    # arguably most correct, but killall from psmisc 22 treats arguments
    # containing "/" specially unless -r is given so that wouldn't quite
    # work either. Perhaps it'd be best to not complete these to anything
    # for now.
    # Not using "ps axo comm" because under some Linux kernels, it
    # truncates command names (see e.g. http://bugs.debian.org/497540#19)
    COMPREPLY=( $( compgen -X '<defunct>' -W '$( command ps axo command= | \
        sed -e "s/ .*//" -e "s:.*/::" -e "s/:$//" -e "s/^[[(-]//" \
            -e "s/[])]$//" | sort -u )' -- "$cur" ) )
}

# This function completes on user IDs
#
_uids()
{
    if type getent &>/dev/null; then
        COMPREPLY=( $( compgen -W '$( getent passwd | cut -d: -f3 )' -- "$cur" ) )
    elif type perl &>/dev/null; then
        COMPREPLY=( $( compgen -W '$( perl -e '"'"'while (($uid) = (getpwent)[2]) { print $uid . "\n" }'"'"' )' -- "$cur" ) )
    else
        # make do with /etc/passwd
        COMPREPLY=( $( compgen -W '$( cut -d: -f3 /etc/passwd )' -- "$cur" ) )
    fi
}

# This function completes on group IDs
#
_gids()
{
    if type getent &>/dev/null; then
        COMPREPLY=( $( compgen -W '$( getent group | cut -d: -f3 )' \
            -- "$cur" ) )
    elif type perl &>/dev/null; then
        COMPREPLY=( $( compgen -W '$( perl -e '"'"'while (($gid) = (getgrent)[2]) { print $gid . "\n" }'"'"' )' -- "$cur" ) )
    else
        # make do with /etc/group
        COMPREPLY=( $( compgen -W '$( cut -d: -f3 /etc/group )' -- "$cur" ) )
    fi
}

# Glob for matching various backup files.
#
_backup_glob='@(#*#|*@(~|.@(bak|orig|rej|swp|dpkg*|rpm@(orig|new|save))))'

# Complete on xinetd services
#
_xinetd_services()
{
    local xinetddir=/etc/xinetd.d
    if [[ -d $xinetddir ]]; then
        local restore_nullglob=$(shopt -p nullglob); shopt -s nullglob
        local -a svcs=( $( printf '%s\n' $xinetddir/!($_backup_glob) ) )
        $restore_nullglob
        COMPREPLY+=( $( compgen -W '${svcs[@]#$xinetddir/}' -- "$cur" ) )
    fi
}

# This function completes on services
#
_services()
{
    local sysvdirs
    _sysvdirs

    local restore_nullglob=$(shopt -p nullglob); shopt -s nullglob
    COMPREPLY=( $( printf '%s\n' ${sysvdirs[0]}/!($_backup_glob|functions) ) )
    $restore_nullglob

    COMPREPLY+=( $( systemctl list-units --full --all 2>/dev/null | \
        awk '$1 ~ /\.service$/ { sub("\\.service$", "", $1); print $1 }' ) )

    COMPREPLY=( $( compgen -W '${COMPREPLY[@]#${sysvdirs[0]}/}' -- "$cur" ) )
}

# This completes on a list of all available service scripts for the
# 'service' command and/or the SysV init.d directory, followed by
# that script's available commands
#
_service()
{
    local cur prev words cword
    _init_completion || return

    # don't complete past 2nd token
    [[ $cword -gt 2 ]] && return 0

    if [[ $cword -eq 1 && $prev == ?(*/)service ]]; then
        _services
        [[ -e /etc/mandrake-release ]] && _xinetd_services
    else
        local sysvdirs
        _sysvdirs
        COMPREPLY=( $( compgen -W '`sed -e "y/|/ /" \
            -ne "s/^.*\(U\|msg_u\)sage.*{\(.*\)}.*$/\2/p" \
            ${sysvdirs[0]}/${prev##*/} 2>/dev/null` start stop' -- "$cur" ) )
    fi
} &&
complete -F _service service
_sysvdirs
for svcdir in ${sysvdirs[@]}; do
    for svc in $svcdir/!($_backup_glob); do
        [[ -x $svc ]] && complete -F _service $svc
    done
done
unset svc svcdir sysvdirs

# This function completes on modules
#
_modules()
{
    local modpath
    modpath=/lib/modules/$1
    COMPREPLY=( $( compgen -W "$( command ls -RL $modpath 2>/dev/null | \
        sed -ne 's/^\(.*\)\.k\{0,1\}o\(\.[gx]z\)\{0,1\}$/\1/p' )" -- "$cur" ) )
}

# This function completes on installed modules
#
_installed_modules()
{
    COMPREPLY=( $( compgen -W "$( PATH="$PATH:/sbin" lsmod | \
        awk '{if (NR != 1) print $1}' )" -- "$1" ) )
}

# This function completes on user or user:group format; as for chown and cpio.
#
# The : must be added manually; it will only complete usernames initially.
# The legacy user.group format is not supported.
#
# @param $1  If -u, only return users/groups the user has access to in
#            context of current completion.
_usergroup()
{
    if [[ $cur = *\\\\* || $cur = *:*:* ]]; then
        # Give up early on if something seems horribly wrong.
        return
    elif [[ $cur = *\\:* ]]; then
        # Completing group after 'user\:gr<TAB>'.
        # Reply with a list of groups prefixed with 'user:', readline will
        # escape to the colon.
        local prefix
        prefix=${cur%%*([^:])}
        prefix=${prefix//\\}
        local mycur="${cur#*[:]}"
        if [[ $1 == -u ]]; then
            _allowed_groups "$mycur"
        else
            local IFS=$'\n'
            COMPREPLY=( $( compgen -g -- "$mycur" ) )
        fi
        COMPREPLY=( $( compgen -P "$prefix" -W "${COMPREPLY[@]}" ) )
    elif [[ $cur = *:* ]]; then
        # Completing group after 'user:gr<TAB>'.
        # Reply with a list of unprefixed groups since readline with split on :
        # and only replace the 'gr' part
        local mycur="${cur#*:}"
        if [[ $1 == -u ]]; then
            _allowed_groups "$mycur"
        else
            local IFS=$'\n'
            COMPREPLY=( $( compgen -g -- "$mycur" ) )
        fi
    else
        # Completing a partial 'usernam<TAB>'.
        #
        # Don't suffix with a : because readline will escape it and add a
        # slash. It's better to complete into 'chown username ' than 'chown
        # username\:'.
        if [[ $1 == -u ]]; then
            _allowed_users "$cur"
        else
            local IFS=$'\n'
            COMPREPLY=( $( compgen -u -- "$cur" ) )
        fi
    fi
}

_allowed_users()
{
    if _complete_as_root; then
        local IFS=$'\n'
        COMPREPLY=( $( compgen -u -- "${1:-$cur}" ) )
    else
        local IFS=$'\n '
        COMPREPLY=( $( compgen -W \
            "$( id -un 2>/dev/null || whoami 2>/dev/null )" -- "${1:-$cur}" ) )
    fi
}

_allowed_groups()
{
    if _complete_as_root; then
        local IFS=$'\n'
        COMPREPLY=( $( compgen -g -- "$1" ) )
    else
        local IFS=$'\n '
        COMPREPLY=( $( compgen -W \
            "$( id -Gn 2>/dev/null || groups 2>/dev/null )" -- "$1" ) )
    fi
}

# This function completes on valid shells
#
_shells()
{
    local shell rest
    while read -r shell rest; do
        [[ $shell == /* && $shell == "$cur"* ]] && COMPREPLY+=( $shell )
    done 2>/dev/null < /etc/shells
}

# This function completes on valid filesystem types
#
_fstypes()
{
    local fss

    if [[ -e /proc/filesystems ]]; then
        # Linux
        fss="$( cut -d$'\t' -f2 /proc/filesystems )
             $( awk '! /\*/ { print $NF }' /etc/filesystems 2>/dev/null )"
    else
        # Generic
        fss="$( awk '/^[ \t]*[^#]/ { print $3 }' /etc/fstab 2>/dev/null )
             $( awk '/^[ \t]*[^#]/ { print $3 }' /etc/mnttab 2>/dev/null )
             $( awk '/^[ \t]*[^#]/ { print $4 }' /etc/vfstab 2>/dev/null )
             $( awk '{ print $1 }' /etc/dfs/fstypes 2>/dev/null )
             $( [[ -d /etc/fs ]] && command ls /etc/fs )"
    fi

    [[ -n $fss ]] && COMPREPLY+=( $( compgen -W "$fss" -- "$cur" ) )
}

# Get real command.
# - arg: $1  Command
# - stdout:  Filename of command in PATH with possible symbolic links resolved.
#            Empty string if command not found.
# - return:  True (0) if command found, False (> 0) if not.
_realcommand()
{
    type -P "$1" > /dev/null && {
        if type -p realpath > /dev/null; then
            realpath "$(type -P "$1")"
        elif type -p greadlink > /dev/null; then
            greadlink -f "$(type -P "$1")"
        elif type -p readlink > /dev/null; then
            readlink -f "$(type -P "$1")"
        else
            type -P "$1"
        fi
    }
}

# This function returns the first argument, excluding options
# @param $1 chars  Characters out of $COMP_WORDBREAKS which should
#     NOT be considered word breaks. See __reassemble_comp_words_by_ref.
_get_first_arg()
{
    local i

    arg=
    for (( i=1; i < COMP_CWORD; i++ )); do
        if [[ "${COMP_WORDS[i]}" != -* ]]; then
            arg=${COMP_WORDS[i]}
            break
        fi
    done
}


# This function counts the number of args, excluding options
# @param $1 chars  Characters out of $COMP_WORDBREAKS which should
#     NOT be considered word breaks. See __reassemble_comp_words_by_ref.
_count_args()
{
    local i cword words
    __reassemble_comp_words_by_ref "$1" words cword

    args=1
    for i in "${words[@]:1:cword-1}"; do
        [[ "$i" != -* ]] && args=$(($args+1))
    done
}

# This function completes on PCI IDs
#
_pci_ids()
{
    COMPREPLY+=( $( compgen -W \
        "$( PATH="$PATH:/sbin" lspci -n | awk '{print $3}')" -- "$cur" ) )
}

# This function completes on USB IDs
#
_usb_ids()
{
    COMPREPLY+=( $( compgen -W \
        "$( PATH="$PATH:/sbin" lsusb | awk '{print $6}' )" -- "$cur" ) )
}

# CD device names
_cd_devices()
{
    COMPREPLY+=( $( compgen -f -d -X "!*/?([amrs])cd*" -- "${cur:-/dev/}" ) )
}

# DVD device names
_dvd_devices()
{
    COMPREPLY+=( $( compgen -f -d -X "!*/?(r)dvd*" -- "${cur:-/dev/}" ) )
}

# TERM environment variable values
_terms()
{
    COMPREPLY+=( $( compgen -W \
        "$( sed -ne 's/^\([^[:space:]#|]\{2,\}\)|.*/\1/p' /etc/termcap \
            2>/dev/null )" -- "$cur" ) )
    COMPREPLY+=( $( compgen -W "$( { toe -a 2>/dev/null || toe 2>/dev/null; } \
        | awk '{ print $1 }' | sort -u )" -- "$cur" ) )
}

# a little help for FreeBSD ports users
[[ $OSTYPE == *freebsd* ]] && complete -W 'index search fetch fetch-list
    extract patch configure build install reinstall deinstall clean
    clean-depends kernel buildworld' make

# This function provides simple user@host completion
#
_user_at_host()
{
    local cur prev words cword
    _init_completion -n : || return

    if [[ $cur == *@* ]]; then
        _known_hosts_real "$cur"
    else
        COMPREPLY=( $( compgen -u -- "$cur" ) )
    fi

    return 0
}
shopt -u hostcomplete && complete -F _user_at_host -o nospace talk ytalk finger

# NOTE: Using this function as a helper function is deprecated.  Use
#       `_known_hosts_real' instead.
_known_hosts()
{
    local cur prev words cword
    _init_completion -n : || return

    # NOTE: Using `_known_hosts' as a helper function and passing options
    #       to `_known_hosts' is deprecated: Use `_known_hosts_real' instead.
    local options
    [[ "$1" == -a || "$2" == -a ]] && options=-a
    [[ "$1" == -c || "$2" == -c ]] && options+=" -c"
    _known_hosts_real $options -- "$cur"
} # _known_hosts()

# Helper function for completing _known_hosts.
# This function performs host completion based on ssh's config and known_hosts
# files, as well as hostnames reported by avahi-browse if
# COMP_KNOWN_HOSTS_WITH_AVAHI is set to a non-empty value.  Also hosts from
# HOSTFILE (compgen -A hostname) are added, unless
# COMP_KNOWN_HOSTS_WITH_HOSTFILE is set to an empty value.
# Usage: _known_hosts_real [OPTIONS] CWORD
# Options:  -a             Use aliases
#           -c             Use `:' suffix
#           -F configfile  Use `configfile' for configuration settings
#           -p PREFIX      Use PREFIX
# Return: Completions, starting with CWORD, are added to COMPREPLY[]
_known_hosts_real()
{
    local configfile flag prefix
    local cur curd awkcur user suffix aliases i host
    local -a kh khd config

    local OPTIND=1
    while getopts "acF:p:" flag "$@"; do
        case $flag in
            a) aliases='yes' ;;
            c) suffix=':' ;;
            F) configfile=$OPTARG ;;
            p) prefix=$OPTARG ;;
        esac
    done
    [[ $# -lt $OPTIND ]] && echo "error: $FUNCNAME: missing mandatory argument CWORD"
    cur=${!OPTIND}; let "OPTIND += 1"
    [[ $# -ge $OPTIND ]] && echo "error: $FUNCNAME("$@"): unprocessed arguments:"\
    $(while [[ $# -ge $OPTIND ]]; do printf '%s\n' ${!OPTIND}; shift; done)

    [[ $cur == *@* ]] && user=${cur%@*}@ && cur=${cur#*@}
    kh=()

    # ssh config files
    if [[ -n $configfile ]]; then
        [[ -r $configfile ]] && config+=( "$configfile" )
    else
        for i in /etc/ssh/ssh_config ~/.ssh/config ~/.ssh2/config; do
            [[ -r $i ]] && config+=( "$i" )
        done
    fi

    # Known hosts files from configs
    if [[ ${#config[@]} -gt 0 ]]; then
        local OIFS=$IFS IFS=$'\n' j
        local -a tmpkh
        # expand paths (if present) to global and user known hosts files
        # TODO(?): try to make known hosts files with more than one consecutive
        #          spaces in their name work (watch out for ~ expansion
        #          breakage! Alioth#311595)
        tmpkh=( $( awk 'sub("^[ \t]*([Gg][Ll][Oo][Bb][Aa][Ll]|[Uu][Ss][Ee][Rr])[Kk][Nn][Oo][Ww][Nn][Hh][Oo][Ss][Tt][Ss][Ff][Ii][Ll][Ee][ \t]+", "") { print $0 }' "${config[@]}" | sort -u ) )
        IFS=$OIFS
        for i in "${tmpkh[@]}"; do
            # First deal with quoted entries...
            while [[ $i =~ ^([^\"]*)\"([^\"]*)\"(.*)$ ]]; do
                i=${BASH_REMATCH[1]}${BASH_REMATCH[3]}
                j=${BASH_REMATCH[2]}
                __expand_tilde_by_ref j # Eval/expand possible `~' or `~user'
                [[ -r $j ]] && kh+=( "$j" )
            done
            # ...and then the rest.
            for j in $i; do
                __expand_tilde_by_ref j # Eval/expand possible `~' or `~user'
                [[ -r $j ]] && kh+=( "$j" )
            done
        done
    fi

    if [[ -z $configfile ]]; then
        # Global and user known_hosts files
        for i in /etc/ssh/ssh_known_hosts /etc/ssh/ssh_known_hosts2 \
            /etc/known_hosts /etc/known_hosts2 ~/.ssh/known_hosts \
            ~/.ssh/known_hosts2; do
            [[ -r $i ]] && kh+=( "$i" )
        done
        for i in /etc/ssh2/knownhosts ~/.ssh2/hostkeys; do
            [[ -d $i ]] && khd+=( "$i"/*pub )
        done
    fi

    # If we have known_hosts files to use
    if [[ ${#kh[@]} -gt 0 || ${#khd[@]} -gt 0 ]]; then
        # Escape slashes and dots in paths for awk
        awkcur=${cur//\//\\\/}
        awkcur=${awkcur//\./\\\.}
        curd=$awkcur

        if [[ "$awkcur" == [0-9]*[.:]* ]]; then
            # Digits followed by a dot or a colon - just search for that
            awkcur="^$awkcur[.:]*"
        elif [[ "$awkcur" == [0-9]* ]]; then
            # Digits followed by no dot or colon - search for digits followed
            # by a dot or a colon
            awkcur="^$awkcur.*[.:]"
        elif [[ -z $awkcur ]]; then
            # A blank - search for a dot, a colon, or an alpha character
            awkcur="[a-z.:]"
        else
            awkcur="^$awkcur"
        fi

        if [[ ${#kh[@]} -gt 0 ]]; then
            # FS needs to look for a comma separated list
            COMPREPLY+=( $( awk 'BEGIN {FS=","}
            /^\s*[^|\#]/ {
            sub("^@[^ ]+ +", ""); \
            sub(" .*$", ""); \
            for (i=1; i<=NF; ++i) { \
            sub("^\\[", "", $i); sub("\\](:[0-9]+)?$", "", $i); \
            if ($i !~ /[*?]/ && $i ~ /'"$awkcur"'/) {print $i} \
            }}' "${kh[@]}" 2>/dev/null ) )
        fi
        if [[ ${#khd[@]} -gt 0 ]]; then
            # Needs to look for files called
            # .../.ssh2/key_22_<hostname>.pub
            # dont fork any processes, because in a cluster environment,
            # there can be hundreds of hostkeys
            for i in "${khd[@]}" ; do
                if [[ "$i" == *key_22_$curd*.pub && -r "$i" ]]; then
                    host=${i/#*key_22_/}
                    host=${host/%.pub/}
                    COMPREPLY+=( $host )
                fi
            done
        fi

        # apply suffix and prefix
        for (( i=0; i < ${#COMPREPLY[@]}; i++ )); do
            COMPREPLY[i]=$prefix$user${COMPREPLY[i]}$suffix
        done
    fi

    # append any available aliases from config files
    if [[ ${#config[@]} -gt 0 && -n "$aliases" ]]; then
        local hosts=$( sed -ne 's/^[ \t]*[Hh][Oo][Ss][Tt]\([Nn][Aa][Mm][Ee]\)\{0,1\}['"$'\t '"']\{1,\}\([^#*?]*\)\(#.*\)\{0,1\}$/\2/p' "${config[@]}" )
        COMPREPLY+=( $( compgen -P "$prefix$user" \
            -S "$suffix" -W "$hosts" -- "$cur" ) )
    fi

    # This feature is disabled because it does not scale to
    #  larger networks. See:
    # https://bugs.launchpad.net/ubuntu/+source/bash-completion/+bug/510591
    # https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=574950

    # Add hosts reported by avahi-browse, if desired and it's available.
    #if [[ ${COMP_KNOWN_HOSTS_WITH_AVAHI:-} ]] && \
        #type avahi-browse &>/dev/null; then
        # The original call to avahi-browse also had "-k", to avoid lookups
        # into avahi's services DB. We don't need the name of the service, and
        # if it contains ";", it may mistify the result. But on Gentoo (at
        # least), -k wasn't available (even if mentioned in the manpage) some
        # time ago, so...
        #COMPREPLY+=( $( compgen -P "$prefix$user" -S "$suffix" -W \
        #    "$( avahi-browse -cpr _workstation._tcp 2>/dev/null | \
        #         awk -F';' '/^=/ { print $7 }' | sort -u )" -- "$cur" ) )
    #fi

    # Add hosts reported by ruptime.
    COMPREPLY+=( $( compgen -W \
        "$( ruptime 2>/dev/null | awk '!/^ruptime:/ { print $1 }' )" \
        -- "$cur" ) )

    # Add results of normal hostname completion, unless
    # `COMP_KNOWN_HOSTS_WITH_HOSTFILE' is set to an empty value.
    if [[ -n ${COMP_KNOWN_HOSTS_WITH_HOSTFILE-1} ]]; then
        COMPREPLY+=(
            $( compgen -A hostname -P "$prefix$user" -S "$suffix" -- "$cur" ) )
    fi

    __ltrim_colon_completions "$prefix$user$cur"

    return 0
} # _known_hosts_real()
complete -F _known_hosts traceroute traceroute6 tracepath tracepath6 \
    fping fping6 telnet rsh rlogin ftp dig mtr ssh-installkeys showmount

# This meta-cd function observes the CDPATH variable, so that cd additionally
# completes on directories under those specified in CDPATH.
#
_cd()
{
    local cur prev words cword
    _init_completion || return

    local IFS=$'\n' i j k

    compopt -o filenames

    # Use standard dir completion if no CDPATH or parameter starts with /,
    # ./ or ../
    if [[ -z "${CDPATH:-}" || "$cur" == ?(.)?(.)/* ]]; then
        _filedir -d
        return 0
    fi

    local -r mark_dirs=$(_rl_enabled mark-directories && echo y)
    local -r mark_symdirs=$(_rl_enabled mark-symlinked-directories && echo y)

    # we have a CDPATH, so loop on its contents
    for i in ${CDPATH//:/$'\n'}; do
        # create an array of matched subdirs
        k="${#COMPREPLY[@]}"
        for j in $( compgen -d $i/$cur ); do
            if [[ ( $mark_symdirs && -h $j || $mark_dirs && ! -h $j ) && ! -d ${j#$i/} ]]; then
                j+="/"
            fi
            COMPREPLY[k++]=${j#$i/}
        done
    done

    _filedir -d

    if [[ ${#COMPREPLY[@]} -eq 1 ]]; then
        i=${COMPREPLY[0]}
        if [[ "$i" == "$cur" && $i != "*/" ]]; then
            COMPREPLY[0]="${i}/"
        fi
    fi

    return 0
}
if shopt -q cdable_vars; then
    complete -v -F _cd -o nospace cd
else
    complete -F _cd -o nospace cd
fi

# a wrapper method for the next one, when the offset is unknown
_command()
{
    local offset i

    # find actual offset, as position of the first non-option
    offset=1
    for (( i=1; i <= COMP_CWORD; i++ )); do
        if [[ "${COMP_WORDS[i]}" != -* ]]; then
            offset=$i
            break
        fi
    done
    _command_offset $offset
}

# A meta-command completion function for commands like sudo(8), which need to
# first complete on a command, then complete according to that command's own
# completion definition.
#
_command_offset()
{
    # rewrite current completion context before invoking
    # actual command completion

    # find new first word position, then
    # rewrite COMP_LINE and adjust COMP_POINT
    local word_offset=$1 i j
    for (( i=0; i < $word_offset; i++ )); do
        for (( j=0; j <= ${#COMP_LINE}; j++ )); do
            [[ "$COMP_LINE" == "${COMP_WORDS[i]}"* ]] && break
            COMP_LINE=${COMP_LINE:1}
            ((COMP_POINT--))
        done
        COMP_LINE=${COMP_LINE#"${COMP_WORDS[i]}"}
        ((COMP_POINT-=${#COMP_WORDS[i]}))
    done

    # shift COMP_WORDS elements and adjust COMP_CWORD
    for (( i=0; i <= COMP_CWORD - $word_offset; i++ )); do
        COMP_WORDS[i]=${COMP_WORDS[i+$word_offset]}
    done
    for (( i; i <= COMP_CWORD; i++ )); do
        unset COMP_WORDS[i]
    done
    ((COMP_CWORD -= $word_offset))

    COMPREPLY=()
    local cur
    _get_comp_words_by_ref cur

    if [[ $COMP_CWORD -eq 0 ]]; then
        local IFS=$'\n'
        compopt -o filenames
        COMPREPLY=( $( compgen -d -c -- "$cur" ) )
    else
        local cmd=${COMP_WORDS[0]} compcmd=${COMP_WORDS[0]}
        local cspec=$( complete -p $cmd 2>/dev/null )

        # If we have no completion for $cmd yet, see if we have for basename
        if [[ ! $cspec && $cmd == */* ]]; then
            cspec=$( complete -p ${cmd##*/} 2>/dev/null )
            [[ $cspec ]] && compcmd=${cmd##*/}
        fi
        # If still nothing, just load it for the basename
        if [[ ! $cspec ]]; then
            compcmd=${cmd##*/}
            _completion_loader $compcmd
            cspec=$( complete -p $compcmd 2>/dev/null )
        fi

        if [[ -n $cspec ]]; then
            if [[ ${cspec#* -F } != $cspec ]]; then
                # complete -F <function>

                # get function name
                local func=${cspec#*-F }
                func=${func%% *}

                if [[ ${#COMP_WORDS[@]} -ge 2 ]]; then
                    $func $cmd "${COMP_WORDS[${#COMP_WORDS[@]}-1]}" "${COMP_WORDS[${#COMP_WORDS[@]}-2]}"
                else
                    $func $cmd "${COMP_WORDS[${#COMP_WORDS[@]}-1]}"
                fi

                # restore initial compopts
                local opt
                while [[ $cspec == *" -o "* ]]; do
                    # FIXME: should we take "+o opt" into account?
                    cspec=${cspec#*-o }
                    opt=${cspec%% *}
                    compopt -o $opt
                    cspec=${cspec#$opt}
                done
            else
                cspec=${cspec#complete}
                cspec=${cspec%%$compcmd}
                COMPREPLY=( $( eval compgen "$cspec" -- '$cur' ) )
            fi
        elif [[ ${#COMPREPLY[@]} -eq 0 ]]; then
            # XXX will probably never happen as long as completion loader loads
            #     *something* for every command thrown at it ($cspec != empty)
            _minimal
        fi
    fi
}
complete -F _command aoss command do else eval exec ltrace nice nohup padsp \
    then time tsocks vsound xargs

_root_command()
{
    local PATH=$PATH:/sbin:/usr/sbin:/usr/local/sbin
    local root_command=$1
    _command
}
complete -F _root_command fakeroot gksu gksudo kdesudo really

# Return true if the completion should be treated as running as root
_complete_as_root()
{
    [[ $EUID -eq 0 || ${root_command:-} ]]
}

_longopt()
{
    local cur prev words cword split
    _init_completion -s || return

    case "${prev,,}" in
        --help|--usage|--version)
            return 0
            ;;
        --*dir*)
            _filedir -d
            return 0
            ;;
        --*file*|--*path*)
            _filedir
            return 0
            ;;
        --+([-a-z0-9_]))
            local argtype=$( $1 --help 2>&1 | sed -ne \
                "s|.*$prev\[\{0,1\}=[<[]\{0,1\}\([-A-Za-z0-9_]\{1,\}\).*|\1|p" )
            case ${argtype,,} in
                *dir*)
                    _filedir -d
                    return 0
                    ;;
                *file*|*path*)
                    _filedir
                    return 0
                    ;;
            esac
            ;;
    esac

    $split && return 0

    if [[ "$cur" == -* ]]; then
        COMPREPLY=( $( compgen -W "$( $1 --help 2>&1 | \
            sed -ne 's/.*\(--[-A-Za-z0-9]\{1,\}=\{0,1\}\).*/\1/p' | sort -u )" \
            -- "$cur" ) )
        [[ $COMPREPLY == *= ]] && compopt -o nospace
    elif [[ "$1" == @(mk|rm)dir ]]; then
        _filedir -d
    else
        _filedir
    fi
}
# makeinfo and texi2dvi are defined elsewhere.
complete -F _longopt a2ps awk base64 bash bc bison cat colordiff cp csplit \
    cut date df diff dir du enscript env expand fmt fold gperf \
    grep grub head indent irb ld ldd less ln ls m4 md5sum mkdir mkfifo mknod \
    mv netstat nl nm objcopy objdump od paste pr ptx readelf rm rmdir \
    sed seq sha{,1,224,256,384,512}sum shar sort split strip sum tac tail tee \
    texindex touch tr uname unexpand uniq units vdir wc who

declare -A _xspecs
_filedir_xspec()
{
    local cur prev words cword
    _init_completion || return

    _tilde "$cur" || return 0

    local IFS=$'\n' xspec=${_xspecs[${1##*/}]} tmp
    local -a toks

    toks=( $(
        compgen -d -- "$(quote_readline "$cur")" | {
        while read -r tmp; do
            printf '%s\n' $tmp
        done
        }
        ))

    # Munge xspec to contain uppercase version too
    # http://thread.gmane.org/gmane.comp.shells.bash.bugs/15294/focus=15306
    eval xspec="${xspec}"
    local matchop=!
    if [[ $xspec == !* ]]; then
        xspec=${xspec#!}
        matchop=@
    fi
    xspec="$matchop($xspec|${xspec^^})"

    toks+=( $(
        eval compgen -f -X "!$xspec" -- "\$(quote_readline "\$cur")" | {
        while read -r tmp; do
            [[ -n $tmp ]] && printf '%s\n' $tmp
        done
        }
        ))

    if [[ ${#toks[@]} -ne 0 ]]; then
        compopt -o filenames
        COMPREPLY=( "${toks[@]}" )
    fi
}

_install_xspec()
{
    local xspec=$1 cmd
    shift
    for cmd in $@; do
        _xspecs[$cmd]=$xspec
    done
    complete -F _filedir_xspec $@
}
# bzcmp, bzdiff, bz*grep, bzless, bzmore intentionally not here, see Debian: #455510
_install_xspec '!*.?(t)bz?(2)' bunzip2 bzcat pbunzip2 pbzcat lbunzip2 lbzcat
_install_xspec '!*.@(zip|[ejsw]ar|exe|pk3|wsz|zargo|xpi|s[tx][cdiw]|sx[gm]|o[dt][tspgfc]|od[bm]|oxt|epub|apk|do[ct][xm]|p[op]t[mx]|xl[st][xm])' unzip zipinfo
_install_xspec '*.Z' compress znew
# zcmp, zdiff, z*grep, zless, zmore intentionally not here, see Debian: #455510
_install_xspec '!*.@(Z|[gGd]z|t[ag]z)' gunzip zcat unpigz
_install_xspec '!*.Z' uncompress
# lzcmp, lzdiff intentionally not here, see Debian: #455510
_install_xspec '!*.@(tlz|lzma)' lzcat lzegrep lzfgrep lzgrep lzless lzmore unlzma
_install_xspec '!*.@(?(t)xz|tlz|lzma)' unxz xzcat
_install_xspec '!*.lrz' lrunzip
_install_xspec '!*.@(gif|jp?(e)g|miff|tif?(f)|pn[gm]|p[bgp]m|bmp|xpm|ico|xwd|tga|pcx)' ee
_install_xspec '!*.@(gif|jp?(e)g|tif?(f)|png|p[bgp]m|bmp|x[bp]m|rle|rgb|pcx|fits|pm|svg)' qiv
_install_xspec '!*.@(gif|jp?(e)g|tif?(f)|png|p[bgp]m|bmp|x[bp]m|rle|rgb|pcx|fits|pm|?(e)ps)' xv
_install_xspec '!*.@(@(?(e)ps|?(E)PS|pdf|PDF)?(.gz|.GZ|.bz2|.BZ2|.Z))' gv ggv kghostview
_install_xspec '!*.@(dvi|DVI)?(.@(gz|Z|bz2))' xdvi kdvi
_install_xspec '!*.dvi' dvips dviselect dvitype dvipdf advi dvipdfm dvipdfmx
_install_xspec '!*.[pf]df' acroread gpdf
_install_xspec '!*.@(pdf|fdf)?(.@(gz|xz|Z|bz2))' xpdf
_install_xspec '!*.@(?(e)ps|pdf)' kpdf
_install_xspec '!*.@(okular|@(?(e|x)ps|?(E|X)PS|[pf]df|[PF]DF|dvi|DVI|cb[rz]|CB[RZ]|djv?(u)|DJV?(U)|dvi|DVI|gif|jp?(e)g|miff|tif?(f)|pn[gm]|p[bgp]m|bmp|xpm|ico|xwd|tga|pcx|GIF|JP?(E)G|MIFF|TIF?(F)|PN[GM]|P[BGP]M|BMP|XPM|ICO|XWD|TGA|PCX|epub|EPUB|odt|ODT|fb?(2)|FB?(2)|mobi|MOBI|g3|G3|chm|CHM)?(.?(gz|GZ|bz2|BZ2)))' okular
_install_xspec '!*.pdf' epdfview
_install_xspec '!*.@(cb[rz7t]|djv?(u)|?(e)ps|pdf)' zathura
_install_xspec '!*.@(?(e)ps|pdf)' ps2pdf ps2pdf12 ps2pdf13 ps2pdf14 ps2pdfwr
_install_xspec '!*.texi*' makeinfo texi2html
_install_xspec '!*.@(?(la)tex|texi|dtx|ins|ltx|dbj)' tex latex slitex jadetex pdfjadetex pdftex pdflatex texi2dvi
_install_xspec '!*.mp3' mpg123 mpg321 madplay
_install_xspec '!*@(.@(mp?(e)g|MP?(E)G|wma|avi|AVI|asf|vob|VOB|bin|dat|divx|DIVX|vcd|ps|pes|fli|flv|FLV|fxm|FXM|viv|rm|ram|yuv|mov|MOV|qt|QT|wmv|mp[234]|MP[234]|m4[pv]|M4[PV]|mkv|MKV|og[agmvx]|OG[AGMVX]|t[ps]|T[PS]|m2t?(s)|M2T?(S)|wav|WAV|flac|FLAC|asx|ASX|mng|MNG|srt|m[eo]d|M[EO]D|s[3t]m|S[3T]M|it|IT|xm|XM)|+([0-9]).@(vdr|VDR))?(.part)' xine aaxine fbxine
_install_xspec '!*@(.@(mp?(e)g|MP?(E)G|wma|avi|AVI|asf|vob|VOB|bin|dat|divx|DIVX|vcd|ps|pes|fli|flv|FLV|fxm|FXM|viv|rm|ram|yuv|mov|MOV|qt|QT|wmv|mp[234]|MP[234]|m4[pv]|M4[PV]|mkv|MKV|og[agmvx]|OG[AGMVX]|t[ps]|T[PS]|m2t?(s)|M2T?(S)|wav|WAV|flac|FLAC|asx|ASX|mng|MNG|srt|m[eo]d|M[EO]D|s[3t]m|S[3T]M|it|IT|xm|XM|iso|ISO)|+([0-9]).@(vdr|VDR))?(.part)' kaffeine dragon
_install_xspec '!*.@(avi|asf|wmv)' aviplay
_install_xspec '!*.@(rm?(j)|ra?(m)|smi?(l))' realplay
_install_xspec '!*.@(mpg|mpeg|avi|mov|qt)' xanim
_install_xspec '!*.@(og[ag]|m3u|flac|spx)' ogg123
_install_xspec '!*.@(mp3|og[ag]|pls|m3u)' gqmpeg freeamp
_install_xspec '!*.fig' xfig
_install_xspec '!*.@(mid?(i)|cmf)' playmidi
_install_xspec '!*.@(mid?(i)|rmi|rcp|[gr]36|g18|mod|xm|it|x3m|s[3t]m|kar)' timidity
_install_xspec '!*.@(669|abc|am[fs]|d[bs]m|dmf|far|it|mdl|m[eo]d|mid?(i)|mt[2m]|okta|p[st]m|s[3t]m|ult|umx|wav|xm)' modplugplay modplug123
_install_xspec '*.@(o|so|so.!(conf|*/*)|a|[rs]pm|gif|jp?(e)g|mp3|mp?(e)g|avi|asf|ogg|class)' vi vim gvim rvim view rview rgvim rgview gview emacs xemacs sxemacs kate kwrite
_install_xspec '!*.@(zip|z|gz|tgz)' bzme
# konqueror not here on purpose, it's more than a web/html browser
_install_xspec '!*.@(?([xX]|[sS])[hH][tT][mM]?([lL]))' netscape mozilla lynx galeon dillo elinks amaya firefox mozilla-firefox iceweasel google-chrome chromium-browser epiphany
_install_xspec '!*.@(sxw|stw|sxg|sgl|doc?([mx])|dot?([mx])|rtf|txt|htm|html|?(f)odt|ott|odm)' oowriter
_install_xspec '!*.@(sxi|sti|pps?(x)|ppt?([mx])|pot?([mx])|?(f)odp|otp)' ooimpress
_install_xspec '!*.@(sxc|stc|xls?([bmx])|xlw|xlt?([mx])|[ct]sv|?(f)ods|ots)' oocalc
_install_xspec '!*.@(sxd|std|sda|sdd|?(f)odg|otg)' oodraw
_install_xspec '!*.@(sxm|smf|mml|odf)' oomath
_install_xspec '!*.odb' oobase
_install_xspec '!*.[rs]pm' rpm2cpio
_install_xspec '!*.aux' bibtex
_install_xspec '!*.po' poedit gtranslator kbabel lokalize
_install_xspec '!*.@([Pp][Rr][Gg]|[Cc][Ll][Pp])' harbour gharbour hbpp
_install_xspec '!*.[Hh][Rr][Bb]' hbrun
_install_xspec '!*.ly' lilypond ly2dvi
_install_xspec '!*.@(dif?(f)|?(d)patch)?(.@([gx]z|bz2|lzma))' cdiff
_install_xspec '!@(*.@(ks|jks|jceks|p12|pfx|bks|ubr|gkr|cer|crt|cert|p7b|pkipath|pem|p10|csr|crl)|cacerts)' portecle
_install_xspec '!*.@(mp[234c]|og[ag]|@(fl|a)ac|m4[abp]|spx|tta|w?(a)v|wma|aif?(f)|asf|ape)' kid3 kid3-qt
_install_xspec '!*.py' pyflakes
unset -f _install_xspec

# Minimal completion to use as fallback in _completion_loader.
_minimal()
{
    local cur prev words cword split
    _init_completion -s || return
    $split && return
    _filedir
}
# Complete the empty string to allow completion of '>', '>>', and '<'
# http://lists.gnu.org/archive/html/bug-bash/2012-01/msg00045.html
complete -F _minimal ''


# set up dynamic completion loading
_completion_loader()
{
    local compfile=./completions
    [[ $BASH_SOURCE == */* ]] && compfile="${BASH_SOURCE%/*}/completions"
    compfile+="/${1##*/}"

    # Avoid trying to source dirs; https://bugzilla.redhat.com/903540
    [[ -f "$compfile" ]] && . "$compfile" &>/dev/null && return 124

    # Need to define *something*, otherwise there will be no completion at all.
    complete -F _minimal "$1" && return 124
} &&
complete -D -F _completion_loader

# Function for loading and calling functions from dynamically loaded
# completion files that may not have been sourced yet.
# @param $1 completion file to load function from in case it is missing
# @param $2... function and its arguments
_xfunc()
{
    set -- "$@"
    local srcfile=$1
    shift
    declare -F $1 &>/dev/null || {
        local compdir=./completions
        [[ $BASH_SOURCE == */* ]] && compdir="${BASH_SOURCE%/*}/completions"
        . "$compdir/$srcfile"
    }
    "$@"
}

# source compat completion directory definitions
if [[ -d $BASH_COMPLETION_COMPAT_DIR && -r $BASH_COMPLETION_COMPAT_DIR && \
    -x $BASH_COMPLETION_COMPAT_DIR ]]; then
    for i in $(LC_ALL=C command ls "$BASH_COMPLETION_COMPAT_DIR"); do
        i=$BASH_COMPLETION_COMPAT_DIR/$i
        [[ ${i##*/} != @($_backup_glob|Makefile*|$_blacklist_glob) \
            && -f $i && -r $i ]] && . "$i"
    done
fi
unset i _blacklist_glob

# source user completion file
[[ ${BASH_SOURCE[0]} != ~/.bash_completion && -r ~/.bash_completion ]] \
    && . ~/.bash_completion
unset -f have
unset have

set $BASH_COMPLETION_ORIGINAL_V_VALUE
unset BASH_COMPLETION_ORIGINAL_V_VALUE

# ex: ts=4 sw=4 et filetype=sh
```

### Output of complete

Here is the output of *complete* builtin command according to above configuration:

```
chenwx@chenwx ~ $ complete
complete -F _minimal
complete -F _filedir_xspec freeamp
complete -F _service /etc/init.d/rc
complete -F _service /etc/init.d/sendsigs
complete -F _service service
complete -o filenames -d -X '.[^./]*' -F _loexp_ unopkg
complete -F _filedir_xspec bibtex
complete -F _longopt strip
complete -F _filedir_xspec chromium-browser
complete -F _filedir_xspec tex
complete -F _filedir_xspec zathura
complete -F _command time
complete -F _command do
complete -F _service /etc/init.d/cryptdisks
complete -c which
complete -F _service /etc/init.d/kmod
complete -o filenames -F _grub_mkconfig grub-mkconfig
complete -F _root_command gksudo
complete -F _longopt tail
complete -F _upstart_reload reload
complete -F _pacat pacat
complete -F _service /etc/init.d/virtualbox-guest-x11
complete -F _upstart_stop stop
complete -F _filedir_xspec lrunzip
complete -F _upstart_initctl initctl
complete -F _filedir_xspec amaya
complete -F _filedir_xspec hbpp
complete -F _longopt df
complete -F _command nice
complete -F _command else
complete -F _longopt enscript
complete -F _known_hosts traceroute6
complete -A binding bind
complete -F _filedir_xspec lzgrep
complete -F _known_hosts fping
complete -F _service /etc/init.d/unattended-upgrades
complete -F _filedir_xspec ggv
complete -F _command nohup
complete -u groups
complete -F _filedir_xspec lzless
complete -F _longopt bison
complete -o filenames -d -X '.[^./]*' -F _loexp_ loimpress
complete -F _filedir_xspec kdvi
complete -F _longopt indent
complete -F _command eval
complete -F _longopt vdir
complete -F _upstart_start start
complete -o filenames -d -X '.[^./]*' -F _loexp_ lobase
complete -F _filedir_xspec lbzcat
complete -F _service /etc/init.d/pidgin-ppa
complete -o filenames -F _grub_mkpasswd_pbkdf2 grub-mkpasswd-pbkdf2
complete -F _filedir_xspec lilypond
complete -F _command then
complete -F _service /etc/init.d/cron
complete -F _upstart_status status
complete -F _filedir_xspec sxemacs
complete -F _filedir_xspec epdfview
complete -F _longopt head
complete -F _command aoss
complete -F _pulseaudio pulseaudio
complete -o filenames -d -X '.[^./]*' -F _loexp_ localc
complete -F _longopt sha1sum
complete -F _filedir_xspec texi2dvi
complete -F _longopt fmt
complete -F _longopt du
complete -F _service /etc/init.d/single
complete -F _service /etc/init.d/samba
complete -F _filedir_xspec ps2pdf12
complete -F _filedir_xspec ee
complete -F _filedir_xspec lbunzip2
complete -o bashdefault -o default -o nospace -F __git_wrap__gitk_main gitk
complete -F _filedir_xspec ps2pdf13
complete -F _longopt rm
complete -F _service /etc/init.d/smbd
complete -F _service /etc/init.d/binfmt-support
complete -F _minimal compopt
complete -o filenames -F _grub_mkrescue grub-mkrescue
complete -o filenames -F _grub_set_entry grub-reboot
complete -F _filedir_xspec ps2pdf14
complete -F _filedir_xspec lzfgrep
complete -F _service /etc/init.d/friendly-recovery
complete -F _filedir_xspec hbrun
complete -F _filedir_xspec kbabel
complete -F _filedir_xspec rview
complete -F _filedir_xspec kaffeine
complete -F _longopt touch
complete -F _filedir_xspec xv
complete -F _longopt tee
complete -F _known_hosts traceroute
complete -F _service /etc/init.d/rsyslog
complete -F _service /etc/init.d/dns-clean
complete -F _filedir_xspec rgvim
complete -F _service /etc/init.d/urandom
complete -F _service /etc/init.d/networking
complete -F _service /etc/init.d/clamav-freshclam
complete -F _filedir_xspec oodraw
complete -F _filedir_xspec elinks
complete -F _longopt split
complete -F _service /etc/init.d/halt
complete -j -P '"%' -S '"' jobs
complete -F _axi_cache axi-cache
complete -F _filedir_xspec playmidi
complete -A helptopic help
complete -A stopped -P '"%' -S '"' bg
complete -o filenames -d -X '.[^./]*' -F _loexp_ libreoffice
complete -F _filedir_xspec xine
complete -F _filedir_xspec xpdf
complete -F _longopt pr
complete -F _service /etc/init.d/screen-cleanup
complete -F _pacat paplay
complete -F _longopt m4
complete -F _service /etc/init.d/grub-common
complete -F _filedir_xspec aviplay
complete -F _filedir_xspec latex
complete -F _longopt uname
complete -F _longopt tac
complete -o filenames -d -X '.[^./]*' -F _loexp_ lodraw
complete -F _longopt bc
complete -F _desktop_file_validate desktop-file-validate
complete -F _filedir_xspec rvim
complete -F _known_hosts tracepath
complete -F _filedir_xspec ogg123
complete -F _service /etc/init.d/mdm
complete -F _filedir_xspec ps2pdfwr
complete -o filenames -d -X '.[^./]*' -F _loexp_ lomath
complete -F _completion_loader -D
complete -F _filedir_xspec harbour
complete -F _filedir_xspec xemacs
complete -F _filedir_xspec unlzma
complete -F _longopt paste
complete -F _longopt mkdir
complete -F _longopt cp
complete -F _root_command really
complete -F _root_command kdesudo
complete -o filenames -d -X '.[^./]*' -F _loexp_ lowriter
complete -F _longopt a2ps
complete -F _filedir_xspec vi
complete -F _known_hosts mtr
complete -F _service /etc/init.d/pppd-dns
complete -v unset
complete -F _filedir_xspec gvim
complete -F _longopt dir
complete -F _service /etc/init.d/samba-ad-dc
complete -F _service /etc/init.d/sudo
complete -F _service /etc/init.d/cpufrequtils
complete -F _filedir_xspec kid3-qt
complete -F _filedir_xspec xanim
complete -F _pactl pactl
complete -F _filedir_xspec portecle
complete -F _longopt cut
complete -F _filedir_xspec oocalc
complete -F _filedir_xspec emacs
complete -F _service /etc/init.d/x11-common
complete -F _service /etc/init.d/cryptdisks-early
complete -F _filedir_xspec fbxine
complete -F _longopt sha384sum
complete -F _service /etc/init.d/reboot
complete -o filenames -F _quilt_completion quilt
complete -F _pacmd pacmd
complete -F _filedir_xspec kpdf
complete -F _longopt less
complete -F _service /etc/init.d/kerneloops
complete -F _command command
complete -F _filedir_xspec oomath
complete -F _filedir_xspec compress
complete -F _longopt texindex
complete -F _longopt env
complete -F _longopt csplit
complete -F _service /etc/init.d/umountroot
complete -F _filedir_xspec iceweasel
complete -F _filedir_xspec zcat
complete -F _filedir_xspec unzip
complete -F _longopt wc
complete -F _longopt sha256sum
complete -F _service /etc/init.d/virtualbox-guest-utils
complete -F _longopt mknod
complete -F _known_hosts rsh
complete -F _filedir_xspec modplug123
complete -F _filedir_xspec dvipdfm
complete -F _known_hosts dig
complete -F _service /etc/init.d/acpid
complete -F _cryptdisks cryptdisks_stop
complete -F _filedir_xspec oobase
complete -F _filedir_xspec zipinfo
complete -F _filedir_xspec epiphany
complete -v readonly
complete -F _root_command fakeroot
complete -o filenames -F _grub_editenv grub-editenv
complete -F _known_hosts fping6
complete -F _service /etc/init.d/rsync
complete -F _longopt units
complete -F _longopt md5sum
complete -F _longopt base64
complete -o nospace -F _cd cd
complete -F _service /etc/init.d/casper
complete -F _service /etc/init.d/anacron
complete -F _filedir_xspec galeon
complete -F _filedir_xspec bzme
complete -F _filedir_xspec xfig
complete -F _longopt mkfifo
complete -F _filedir_xspec xdvi
complete -F _longopt uniq
complete -F _openvpn /etc/init.d/openvpn
complete -F _longopt grep
complete -d pushd
complete -o filenames -F _grub_set_entry grub-set-default
complete -F _known_hosts rlogin
complete -F _filedir_xspec cdiff
complete -F _filedir_xspec rgview
complete -F _pon pon
complete -F _filedir_xspec oowriter
complete -F _command exec
complete -o nospace -F _user_at_host finger
complete -F _service /etc/init.d/busybox-syslogd
complete -u slay
complete -F _longopt ldd
complete -F _service /etc/init.d/brltty
complete -F _filedir_xspec netscape
complete -F _filedir_xspec acroread
complete -F _pacat parecord
complete -o filenames -F _grub_mkimage grub-mkimage
complete -F _filedir_xspec makeinfo
complete -F _longopt nl
complete -F _service /etc/init.d/lightdm
complete -F _longopt nm
complete -F _command xargs
complete -F _minimal findaf
complete -F _filedir_xspec kwrite
complete -F _filedir_xspec gview
complete -F _filedir_xspec qiv
complete -F _filedir_xspec bzcat
complete -F _longopt expand
complete -F _upstart_restart restart
complete -F _filedir_xspec pdftex
complete -F _filedir_xspec rpm2cpio
complete -F _longopt bash
complete -F _dkms dkms
complete -F _debconf_show debconf-show
complete -F _filedir_xspec view
complete -F _filedir_xspec unxz
complete -F _longopt sha512sum
complete -F _filedir_xspec ly2dvi
complete -F _filedir_xspec mozilla
complete -F _longopt objcopy
complete -u sux
complete -F _pasuspender pasuspender
complete -F _filedir_xspec modplugplay
complete -F _root_command gksu
complete -F _filedir_xspec pyflakes
complete -F _service /etc/init.d/irqbalance
complete -o bashdefault -o default -o nospace -F __git_wrap__git_main git
complete -F _filedir_xspec dillo
complete -F _filedir_xspec aaxine
complete -F _filedir_xspec dvipdfmx
complete -F _filedir_xspec advi
complete -F _longopt rmdir
complete -F _service /etc/init.d/console-setup
complete -F _filedir_xspec lzmore
complete -F _service /etc/init.d/bluetooth
complete -o default -o nospace -F _mvn mvnDebug
complete -o filenames -F _grub_setup grub-bios-setup
complete -F _service /etc/init.d/pulseaudio
complete -F _service /etc/init.d/procps
complete -F _service /etc/init.d/atd
complete -F _filedir_xspec poedit
complete -F _filedir_xspec firefox
complete -F _filedir_xspec gv
complete -F _longopt shasum
complete -F _service /etc/init.d/umountnfs.sh
complete -F _service /etc/init.d/rcS
complete -F _service /etc/init.d/cups-browsed
complete -F _filedir_xspec madplay
complete -F _longopt sort
complete -F _longopt ptx
complete -F _longopt colordiff
complete -F _service /etc/init.d/winbind
complete -o filenames -d -X '.[^./]*' -F _loexp_ lofromtemplate
complete -F _filedir_xspec gtranslator
complete -F _filedir_xspec jadetex
complete -F _longopt fold
complete -F _service /etc/init.d/avahi-daemon
complete -u write
complete -o filenames -d -X '.[^./]*' -F _loexp_ loweb
complete -F _filedir_xspec gpdf
complete -F _filedir_xspec kghostview
complete -F _command ltrace
complete -F _service /etc/init.d/speech-dispatcher
complete -F _filedir_xspec pbzcat
complete -F _known_hosts telnet
complete -A shopt shopt
complete -o filenames -F _grub_script_check grub-script-check
complete -F _longopt sum
complete -F _longopt od
complete -F _longopt irb
complete -F _filedir_xspec lzcat
complete -F _known_hosts showmount
complete -o nospace -F _user_at_host talk
complete -F _service /etc/init.d/lm-sensors
complete -F _cryptdisks cryptdisks_start
complete -F _longopt readelf
complete -F _longopt netstat
complete -F _service /etc/init.d/loadcpufreq
complete -F _filedir_xspec vim
complete -F _filedir_xspec dvips
complete -F _longopt date
complete -F _longopt cat
complete -j -P '"%' -S '"' disown
complete -o default -o nospace -F _mvn mvn
complete -F _longopt objdump
complete -F _longopt diff
complete -F _service /etc/init.d/cups
complete -o bashdefault -o default -F _hg hg
complete -F _filedir_xspec dvitype
complete -F _service /etc/init.d/busybox-klogd
complete -a unalias
complete -F _longopt sed
complete -F _longopt ld
complete -F _service /etc/init.d/nmbd
complete -F _complete compgen
complete -F _cmake cmake
complete -F _longopt mv
complete -F _filedir_xspec realplay
complete -F _longopt grub
complete -F _longopt gperf
complete -F _known_hosts ftp
complete -F _service /etc/init.d/fetchmail
complete -F _filedir_xspec gqmpeg
complete -F _filedir_xspec lzegrep
complete -o nospace -F _user_at_host ytalk
complete -F _service /etc/init.d/udev
complete -F _service /etc/init.d/dbus
complete -F _longopt shar
complete -F _known_hosts tracepath6
complete -F _inkscape inkscape
complete -F _filedir_xspec bunzip2
complete -o filenames -F _grub_probe grub-probe
complete -F _longopt sha224sum
complete -F _longopt awk
complete -F _minimal ll
complete -o filenames -F _grub_mkfont grub-mkfont
complete -F _filedir_xspec znew
complete -F _longopt who
complete -F _filedir_xspec lokalize
complete -F _filedir_xspec kate
complete -F _filedir_xspec dragon
complete -F _service /etc/init.d/hddtemp
complete -F _filedir_xspec pdflatex
complete -F _longopt ln
complete -F _minimal gedit
complete -F _ctest ctest
complete -o filenames -F _grub_install grub-install
complete -F _cpack cpack
complete -F _filedir_xspec mozilla-firefox
complete -F _complete complete
complete -F _filedir_xspec ooimpress
complete -F _filedir_xspec uncompress
complete -o default -F _pygmentize pygmentize
complete -F _longopt tr
complete -F _service /etc/init.d/bitlbee
complete -F _filedir_xspec unpigz
complete -F _service /etc/init.d/resolvconf
complete -A setopt set
complete -u chfn
complete -F _padsp padsp
complete -F _service /etc/init.d/saned
complete -F _filedir_xspec lynx
complete -F _filedir_xspec ps2pdf
complete -F _command vsound
complete -F _known_hosts ssh-installkeys
complete -F _longopt seq
complete -b builtin
complete -j -P '"%' -S '"' fg
complete -F _filedir_xspec mpg321
complete -F _filedir_xspec mpg123
complete -F _filedir_xspec pbunzip2
complete -u runuser
complete -F _poff poff
complete -F _filedir_xspec kid3
complete -F _filedir_xspec pdfjadetex
complete -F _filedir_xspec dvipdf
complete -F _service /etc/init.d/ondemand
complete -u w
complete -o filenames -F _make_kpkg make-kpkg
complete -F _filedir_xspec gharbour
complete -F _service /etc/init.d/killprocs
complete -c type
complete -F _filedir_xspec texi2html
complete -F _longopt unexpand
complete -F _update_initramfs update-initramfs
complete -F _filedir_xspec gunzip
complete -F _service /etc/init.d/rc.local
complete -o filenames -d -X '.[^./]*' -F _loexp_ loffice
complete -F _filedir_xspec google-chrome
complete -F _filedir_xspec okular
complete -F _service /etc/init.d/umountfs
complete -F _filedir_xspec slitex
complete -F _filedir_xspec xzcat
complete -F _service /etc/init.d/mintsystem
complete -F _filedir_xspec timidity
complete -F _filedir_xspec dviselect
complete -F _command tsocks
```

# Using History Interactively

## Bash History Facilities

When the ```-o history``` option to the **set** builtin is enabled (see [The *set* Builtin](#the-em-set-em-builtin)), the shell provides access to the command history, the list of commands previously typed.

| Variables | Description |
| :-------- | :---------- |
| **HISTSIZE**  | The value of the **HISTSIZE** shell variable is used as the number of commands to save in a history list. The text of the last **$HISTSIZE** commands (default **500**) is saved. |
| **HISTFILESIZE** | The maximum number of lines contained in the history file. Refer to variable **HISTFILE**. |
| **HISTFILE**  | When the shell starts up, the history is initialized from the file named by the **HISTFILE** variable (default ***~/.bash_history***). The file named by the value of **HISTFILE** is truncated, if necessary, to contain no more than the number of lines specified by the value of the **HISTFILESIZE** variable.<br><br>When a shell with history enabled exits, the last **$HISTSIZE** lines are copied from the history list to the file named by **$HISTFILE**. If the ```histappend``` option to the **set** builtin is enabled (see [The *set* Builtin](#the-em-set-em-builtin)), the lines are appended to the history file, otherwise the history file is overwritten.<br><br>If **HISTFILE** is unset, or if the history file is unwritable, the history is not saved.<br><br>After saving the history, the history file is truncated to contain no more than **$HISTFILESIZE** lines. If **HISTFILESIZE** is unset, or set to null, a non-numeric value, or a numeric value less than zero, the history file is not truncated. |
| **HISTTIMEFORMAT** | If the **HISTTIMEFORMAT** is set, the time stamp information associated with each history entry is written to the history file, marked with the history comment character. When the history file is read, lines beginning with the history comment character followed immediately by a digit are interpreted as timestamps for the previous history line. |
| **HISTCONTROL** | A colon-separated list of values controlling how commands are saved on the history list.<br><br>If the list of values includes ***ignorespace***, lines which begin with a space character are not saved in the history list.<br>A value of ***ignoredups*** causes lines which match the previous history entry to not be saved.<br>A value of ***ignoreboth*** is shorthand for ***ignorespace*** and ***ignoredups***.<br>A value of ***erasedups*** causes all previous lines matching the current line to be removed from the history list before that line is saved.<br>Any value not in the above list is ignored.<br><br>If **HISTCONTROL** is unset, or does not include a valid value, all lines read by the shell parser are saved on the history list, subject to the value of **HISTIGNORE**.<br><br>The second and subsequent lines of a multi-line compound command are not tested, and are added to the history regardless of the value of **HISTCONTROL**. |
| **HISTIGNORE** | A colon-separated list of patterns used to decide which command lines should be saved on the history list. Each pattern is anchored at the beginning of the line and must match the complete line (no implicit ```*``` is appended). Each pattern is tested against the line after the checks specified by **HISTCONTROL** are applied. In addition to the normal shell pattern matching characters, ```&``` matches the previous history line. ```&``` may be escaped using a backslash; the backslash is removed before attempting a match.<br><br>The second and subsequent lines of a multi-line compound command are not tested, and are added to the history regardless of the value of **HISTIGNORE**.<br><br>**HISTIGNORE** subsumes the function of **HISTCONTROL**. A pattern of ```&``` is identical to ***ignoredups***, and a pattern of ```[ ]*``` is identical to ***ignorespace***. Combining these two patterns, separating them with a colon, provides the functionality of ***ignoreboth***. |

## Bash History Builtins

Bash provides two builtin commands which manipulate the history list and history file.

| Builtins | Description |
| :------- | :---------- |
| ```fc``` | Formats:<br>```fc [-e ename] [-lnr] [first] [last]```<br>```fc -s [pat=rep] [command]```<br><br>The first form selects a range of commands from *first* to *last* from the history list and displays or edits and re-executes them. Both *first* and *last* may be specified as a ***string*** (to locate the most recent command beginning with that string) or as a ***number*** (an index into the history list, where a ***negative number*** is used as an offset from the current command number). If *last* is not specified it is set to *first*. If *first* is not specified it is set to the previous command for editing and **-16** for listing.<br><br>If the ```-l``` flag is given, the commands are listed on standard output. The ```-n``` flag suppresses the command numbers when listing. The ```-r``` flag reverses the order of the listing.<br><br>Otherwise, the editor given by *ename* is invoked on a file containing those commands. If *ename* is not given, the value of the following variable expansion is used: **${FCEDIT:-${EDITOR:-vi}}**. This says to use the value of the **FCEDIT** variable if set, or the value of the **EDITOR** variable if that is set, or **vi** if neither is set. When editing is complete, the edited commands are echoed and executed.<br><br>In the second form, *command* is re-executed after each instance of *pat* in the selected command is replaced by *rep*. *command* is intepreted the same as *first* above.<br><br>A useful alias to use with the *fc* command is ```r='fc -s'```, so that typing ```r cc``` runs the last command beginning with ```cc``` and typing ```r``` re-executes the last command. |
| ```history``` | Formats:<br>```history [n]```<br>```history -c```<br>```history -d offset```<br>```history [-anrw] [filename]```<br>```history -ps arg```<br><br>With no options, display the history list with line numbers. Lines prefixed with a ```*``` have been modified. An argument of *n* lists only the last *n* lines. If the shell variable **HISTTIMEFORMAT** is set and not null, it is used as a format string for *strftime* to display the time stamp associated with each displayed history entry. No intervening blank is printed between the formatted time stamp and the history line.<br><br>Options, if supplied, have the following meanings:<br>```-c``` Clear the history list. This may be combined with the other options to replace the history list completely.<br>```-d offset``` Delete the history entry at position *offset*. *offset* should be specified as it appears when the history is displayed.<br>```-a``` Append the new history lines (history lines entered since the beginning of the current Bash session) to the history file.<br>```-n``` Append the history lines not already read from the history file to the current history list. These are lines appended to the history file since the beginning of the current Bash session.<br>```-r``` Read the history file and append its contents to the history list.<br>```-w``` Write out the current history list to the history file.<br>```-p``` Perform history substitution on the *args* and display the result on the standard output, without storing the results in the history list.<br>```-s``` The *args* are added to the end of the history list as a single entry.<br><br>When any of the ```-a``` ```-n``` ```-r``` or ```-w``` options is used, if *filename* is given, then it is used as the history file. If not, then the value of the **HISTFILE** variable is used. |

<p/>

***Examples:***

```
chenwx@chenwx ~ $ fc -l -2
651	 cd
652	 gedit ~/Downloads/ex/ex.sh &

chenwx@chenwx ~ $ fc -ln -10 -9
	 cd
	 gedit ~/Downloads/ex/ex.sh &

chenwx@chenwx ~ $ history
  164  cd
  165  gedit ~/Downloads/ex/ex.sh &
  166  history

chenwx@chenwx ~ $ history 3
  165  gedit ~/Downloads/ex/ex.sh &
  166  history
  167  history 3
```

## History Expansion

The **History** library provides a **history expansion** feature that is similar to the history expansion provided by **csh**.

History expansion takes place in two parts:

1. The first is to determine which line from the history list should be used during substitution.
2. The second is to select portions of that line for inclusion into the current one.

The line selected from the history is called the **event**, and the portions of that line that are acted upon are called **words**. Various **modifiers** are available to manipulate the selected words.

The line is broken into words in the same fashion that Bash does, so that several words surrounded by quotes are considered one word.

History expansions are introduced by the appearance of the history expansion character, which is ```!``` by default. Only ```\``` and ```'``` may be used to escape the history expansion character.

Several shell options settable with the *shopt* builtin may be used to tailor the behavior of history expansion. Refer to [The *shopt* Builtin](#the-em-shopt-em-builtin):

* If the ```histverify``` shell option is enabled, and **Readline** is being used, history substitutions are not immediately passed to the shell parser. Instead, the expanded line is reloaded into the Readline editing buffer for further modification.

* If **Readline** is being used, and the ```histreedit``` shell option is enabled, a failed history expansion will be reloaded into the Readline editing buffer for correction.

* The ```-p``` option to the **history** builtin command may be used to see what a history expansion will do before using it.

* The ```-s``` option to the **history** builtin may be used to add commands to the end of the history list without actually executing them, so that they are available for subsequent recall. This is most useful in conjunction with **Readline**.

* The shell allows control of the various characters used by the history expansion mechanism with the ```histchars``` variable. The shell uses the history comment character to mark history timestamps when writing the history file.

***Format:***

```
<event-designator>[:<word-designator>][:<modifier1>[:<modifier2>...]]
```

### Event Designators

An event designator is a reference to a command line entry in the history list. Unless the reference is absolute, events are relative to the current position in the history list.

| Event_Designators | Description |
| :---------------- | :---------- |
| ```!``` | Start a history substitution, except when followed by a **space**, **tab**, **the end of the line**, ```=``` or ```(``` (when the *extglob* shell option is enabled using the *shopt* builtin). |
| ```!n``` | Refer to command line *n*. |
| ```!-n``` | Refer to the command *n* lines back. |
| ```!!``` | Refer to the previous command. This is a synonym for ```!-1```. |
| ```!string``` | Refer to **the most recent command** preceding the current position in the history list starting with *string*. |
| ```!?string[?]``` | Refer to **the most recent command** preceding the current position in the history list containing *string*. The trailing ```?``` may be omitted if the *string* is followed immediately by a newline. |
| ```^string1^string2^``` | Quick Substitution. Repeat the last command, replacing *string1* with *string2*. Equivalent to ```!!:s/string1/string2/```. |
| ```!#``` | The entire command line typed so far. |

<p/>

### Word Designators

Word designators are used to select desired words from the event. A ```:``` separates the **event specification** from the **word designator**. It may be omitted if the word designator begins with a ```^```, ```$```, ```*```, ```-```, or ```%```. Words are numbered from the beginning of the line, with the first word being denoted by **0** (zero). Words are inserted into the current line separated by single spaces. Here are the word designators:

| Word_Designators | Description |
| :--------------: | :---------- |
| ```0``` | The **0**th word. For many applications, this is the command word. |
| ```n``` | The **n**th word. E.g. ```!fi:2``` designates the second argument of the most recent command starting with the letters *fi*. |
| ```^``` | The first argument; that is, word **1**. |
| ```$``` | The last argument. E.g. ```!!:$``` designates the last argument of the preceding command, which may be shortened to ```!$```. |
| ```%``` | The word matched by the most recent ```?string?``` search. |
| ```x-y``` | A range of words; ```-y``` abbreviates ```0-y```. |
| ```*``` | All of the words, except the **0**th. This is a synonym for ```1-$```. It is not an error to use ```*``` if there is just one word in the event; the empty string is returned in that case. |
| ```x*``` | Abbreviates ```x-$```. |
| ```x-``` | Abbreviates ```x-$``` like ```x*```, but omits the last word. |

<p/>

If a **word designator** is supplied without an **event specification**, the previous command is used as the **event**.

<p/>

### Modifiers

After the optional **word designator**, you can add a sequence of one or more of the following modifiers, each preceded by a ```:```.

| Modifiers | Description |
| :-------: | :---------- |
| ```h``` | Remove a trailing pathname component, leaving only the head. |
| ```t``` | Remove all leading pathname components, leaving the tail. |
| ```r``` | Remove a trailing suffix of the form ```.suffix```, leaving the basename. |
| ```e``` | Remove all but the trailing suffix. |
| ```p``` | Print the new command but do not execute it. |
| ```q``` | Quote the substituted words, escaping further substitutions. |
| ```x``` | Quote the substituted words as with ```q```, but break into words at spaces, tabs, and newlines. |
| ```s/old/new/``` | Substitute new for the first occurrence of old in the event line. Any delimiter may be used in place of ```/```. The delimiter may be quoted in old and new with a single backslash. If ```&``` appears in new, it is replaced by old. A single backslash will quote the ```&```. The final delimiter is optional if it is the last character on the input line. |
| ```&``` | Repeat the previous substitution. |
| ```g```<br>```a``` | Cause changes to be applied over the entire **event** line. Used in conjunction with ```s```, as in ```gs/old/new/```, or with ```&```. |
| ```G``` | Apply the following ```s``` modifier once to each word in the **event**. |

<p/>

***Examples:***

```
chenwx@chenwx ~ $ history
  ...
  612  gedit ~/Downloads/ex/ex.sh &
```

```
chenwx@chenwx ~ $ ^gedit^vi^
vi ~/Downloads/ex/ex.sh &
[2] 12845

chenwx@chenwx ~ $ gedit ~/Downloads/ex/ex.sh !#:t:p
gedit ~/Downloads/ex/ex.sh ex.sh

chenwx@chenwx ~ $ !612:p
gedit ~/Downloads/ex/ex.sh &

chenwx@chenwx ~ $ !612:h:p
gedit ~/Downloads/ex
chenwx@chenwx ~ $ !612:h:t:p
ex
chenwx@chenwx ~ $ !612:t:p
ex.sh &
chenwx@chenwx ~ $ !612:t:r:p
ex
chenwx@chenwx ~ $ !612:t:e:p
.sh &
chenwx@chenwx ~ $ !612:t:q:p
'ex.sh &'
chenwx@chenwx ~ $ !612:t:s/sh/bash/:p
ex.bash &
chenwx@chenwx ~ $ !612:t:s/sh/bash/:&:p
ex.babash &

chenwx@chenwx ~ $ !612:1:h:p  
~/Downloads/ex
chenwx@chenwx ~ $ !612:1:h:t:p
ex
chenwx@chenwx ~ $ !612:1:t:p
ex.sh
chenwx@chenwx ~ $ !612:1:t:r:p
ex
chenwx@chenwx ~ $ !612:1:t:e:p
.sh
chenwx@chenwx ~ $ !612:1:t:q:p
'ex.sh'
chenwx@chenwx ~ $ !612:1:t:s/sh/bash/:p
ex.bash
chenwx@chenwx ~ $ !612:1:t:s/sh/bash/:&:p
ex.babash
```

# References

* [GNU Bash Official Site](https://www.gnu.org/software/bash/)
* [GNU Bash Reference Manual](https://www.gnu.org/software/bash/manual/)
