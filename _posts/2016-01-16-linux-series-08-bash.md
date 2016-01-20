---
layout: post
title: "Linux Series #8: GNU Bash"
tags: [Linux, Programming language]
toc: true
---

This article introduces the GNU Bash in detail.

<!--more-->

# GNU Bash

Here is [GNU Bash official site](https://www.gnu.org/software/bash/), and here is [Bash Reference Manual](https://www.gnu.org/software/bash/manual/). The GNU Bash releases following versions:

| GNU Bash Version | Release Date |
| :--------------: | :----------: |
| 2.02.1           | 24 Jul 1998  |
| 2.03             | 20 Feb 1999  |
| 2.04b5           | 24 Feb 2000  |
| 2.04             | 21 Mar 2000  |
| 2.05             | 09 Apr 2001  |
| 2.05a            | 16 Nov 2001  |
| 2.05b            | 18 Jul 2002  |
| 3.0              | 30 Jul 2004  |
| 3.2              | 13 Nov 2007  |
| 4.0              | 17 Mar 2009  |
| 4.1              | 29 Jan 2010  |
| 4.2              | 10 May 2011  |
| 4.3              | 26 Feb 2014  |

<p/>

The GNU Bash Git repository is located [here](http://savannah.gnu.org/git/?group=bash). Run following command to get a copy of the GNU Bash source code from repository:

    $ git clone git://git.savannah.gnu.org/bash.git

or, browse sources repository online [here](http://git.savannah.gnu.org/cgit/bash.git).

# Bash Operation

The following is a brief description of the shell's operation when it reads and executes a command. Basically, the shell does the following:

1. Reads its input from a **shell script**, from a **string** supplied as an argument to the ```-c``` invocation option, or from **the user’s terminal**.
2. Breaks the input into **words** and **operators**, obeying the quoting rules described in [Quoting](#quoting). These tokens are separated by [metacharacters](#definitions). [Alias expansion](#aliases) is performed by this step.
3. Parses the tokens into [simple commands](#simple-commands) and [compound commands](#compound-commands).
4. Performs the various [shell expansions](#shell-expansions), breaking the expanded tokens into lists of [filenames](#filename-expansion), commands and arguments.
5. Performs any necessary **redirections** and removes the redirection operators and their operands from the argument list.
6. [Executes the command](#executing-commands).
7. Optionally waits for the command to complete and collects its [exit status](#exit-status).

# Definitions

***Control Operator***

A token that performs a control function. It is a *newline* or one of the following: ```||``` ```&&``` ```&``` ```;``` ```;;``` ```|``` ```|&``` ```(``` ```)```

***Metacharacter***

A ***metacharacter*** is a character that, when unquoted, separates words.
A ***metacharacter*** is a ***blank*** or one of the following characters: ```|``` ```&``` ```;``` ```(``` ```)``` ```<``` ```>```

***Comments***

In a non-interactive shell, or an interactive shell in which the ```interactive_comments``` option to the ```shopt``` builtin is enabled, a word beginning with ```#``` causes that word and all remaining characters on that line to be ignored. An interactive shell without the ```interactive_comments``` option enabled does not allow comments. The ```interactive_comments``` option is **on** by default in interactive shells.

# Quoting

***Escape Character*** (```\```)

A non-quoted backslash (```\```) is the Bash escape character. It preserves the literal value of the next character that follows, with the exception of ***newline***. If a ```\newline``` pair appears, and the backslash itself is not quoted, the ```\newline``` is treated as a **line continuation**, that's, it is removed from the input stream and effectively ignored.

***Single Quotes*** (```'```)

Enclosing characters in single quotes (```'```) preserves the literal value of each character within the quotes. ***A single quote may not occur between single quotes, even when preceded by a backslash***.

***Double Quotes*** (```"```)

Enclosing characters in double quotes (```"```) preserves the literal value of all characters within the quotes, with the exception of ```$```, ```` ` ````, ```\```, and, when history expansion is enabled, ```!```. ***A double quote may be quoted within double quotes by preceding it with a backslash***.

| Characters | Description |
| :--------- | :---------- |
| ```$```    | The characters ```$``` and ``` ` ``` retain their special meaning within double quotes, refer to the following sections in [Shell Expansions](#shell-expansions):<br>[Parameter and variable expansion](#parameter-and-variable-expansion)<br>[Arithmetic expansion](#arithmetic-expansion)<br>[Command Substitution](#command-substitution)<br>[Filename Expansion](#filename-expansion) |
| ``` ` ```    | The characters ```$``` and ``` ` ``` retain their special meaning within double quotes, refer to the following sections in [Shell Expansions](#shell-expansions):<br>[Command Substitution](#command-substitution) |
| ```\```    | The backslash retains its special meaning only when followed by one of the following characters: ```$``` ``` ` ``` ```"``` ```\``` or ***newline***. Within double quotes, backslashes that are followed by one of these characters are removed. Backslashes preceding characters without a special meaning are left unmodified. |
| ```!```    | If enabled, **history expansion** will be performed unless an ```!``` appearing in double quotes is escaped using a backslash. The backslash preceding the ```!``` is not removed. |
| ```*```    | ```*``` has special meaning when in double quotes, refer to [Shell Parameter Expansion](#shell-parameter-expansion). |
| ```@```    | ```@``` has special meaning when in double quotes, refer to [Shell Parameter Expansion](#shell-parameter-expansion). |

<p/>

***ANSI-C Quoting***

Words of the form ```$'string'``` are treated specially. The word expands to *string*, with backslash-escaped characters replaced as specified by the **ANSI C standard**. Backslash escape sequences, if present, are decoded as following table. The expanded result is single-quoted, as if the dollar sign had not been present.

| Sequences | Description |
| :-------- | :---------- |
| ```\a```  | alert (bell) |
| ```\b```  | backspace |
| ```\e```<br>```\E``` | an escape character (not ANSI C) |
| ```\f```  | form feed |
| ```\n```  | newline |
| ```\r```  | carriage return |
| ```\t```  | horizontal tab |
| ```\v```  | vertical tab |
| ```\\```  | backslash |
| ```\'```  | single quote |
| ```\"```  | double quote |
| ```\nnn``` | the eight-bit character whose value is the octal value *nnn* (one to three digits) |
| ```\xHH``` | the eight-bit character whose value is the hexadecimal value *HH* (one or two hex digits) |
| ```\uHHHH``` | the Unicode (ISO/IEC 10646) character whose value is the hexadecimal value *HHHH* (one to four hex digits) |
| ```\UHHHHHHHH``` | the Unicode (ISO/IEC 10646) character whose value is the hexadecimal value *HHHHHHHH* (one to eight hex digits) |
| ```\cx``` | a control-x character |

<p/>

***Locale-Specific Translation***

```$"string"```

A **double-quoted** *string* preceded by a dollar sign (```$```) will cause the *string* to be translated according to the current locale. If the current locale is ***C*** or ***POSIX***, the dollar sign is ignored. If the *string* is translated and replaced, the replacement is double-quoted.

Refer to [How to add localization support to your bash scripts](http://mywiki.wooledge.org/BashFAQ/098).

# Aliases

**Aliases** allow a *string* to be substituted for a *word* when it is used as the ***first word of a simple command***. The shell maintains a list of aliases that may be set and unset with the ```alias``` and ```unalias``` builtin commands.

* The first word of each *simple command*, if unquoted, is checked to see if it has an alias. If so, that word is replaced by the text of the alias.

* The characters ```/``` ```$``` ``` ` ``` ```=``` and any of the shell ***metacharacters*** or ***quoting characters*** may not appear in an alias name. The replacement text may contain any valid shell input, including shell ***metacharacters***.

* The ***first word of the replacement text*** is tested for aliases, but a word that is identical to an alias being expanded is ***not*** expanded a second time.

* If the ***last character of the alias value*** is a *blank*, then the next command word following the alias is also checked for alias expansion.

* Aliases are not expanded when the shell is not interactive, unless the shell option ```expand_aliases``` is set using ```shopt```.

Bash always reads at least one complete line of input before executing any of the commands on that line. ***Aliases are expanded when a command is read, not when it is executed***.

* Therefore, an alias definition appearing on the same line as another command does not take effect until the next line of input is read. The commands following the alias definition on that line are not affected by the new alias.

* Aliases are expanded when a function definition is read, not when the function is executed, because a function definition is itself a compound command. As a consequence, ***aliases defined in a function are not available until after that function is executed***. To be safe, always put alias definitions on a separate line, and do not use alias in compound commands.

For almost every purpose, shell functions are preferred over aliases.

Refer to [Bash Builtin Commands](#bash-builtin-commands) for details about syntax of each Bash builtins.

# Bash Commands

## Simple Commands

A simple command is just a sequence of words separated by *blanks*, terminated by one of the shell's ***control operators***. The first word generally specifies a command to be executed, with the rest of the words being that command's arguments.

Simple commands have formats:
```command```
```command ;```
```command &```

## Pipelines

A ***pipeline*** is a sequence of ***simple commands*** separated by one of the control operators ```|``` or ```|&```. The output of each command in the pipeline is connected via a pipe to the input of the next command.

Pipelines have formats:
```[time [-p]] [!] command1 [ | command2 ] ...```

```[time [-p]] [!] command1 [ |& command2 ] ...```
```[time [-p]] [!] command1 [ 2>&1 | command2 ] ...```

If ```|&``` is used, *command1*'s standard error, in addition to its standard output, is connected to *command2*'s standard input through the pipe; it is shorthand for ```2>&1 |```.

If the reserved word ```!``` precedes the pipeline, the exit status is the logical negation of the exit status.

## Lists

A list is a sequence of one or more ***pipelines*** separated by one of the operators ```;```, ```&```, ```&&```, or ```||```, and optionally terminated by one of ```;```, ```&```, or a *newline*. Of these list operators, ```&&``` and ```||``` have equal precedence, followed by ```;``` and ```&```, which have equal precedence.

Lists of commands have formats:

```pipeline-command1 ; pipeline-command2```
```pipeline-command1 ; pipeline-command2 ;```
```pipeline-command1 ; pipeline-command2 &```

```pipeline-command1 & pipeline-command2```
```pipeline-command1 & pipeline-command2 ;```
```pipeline-command1 & pipeline-command2 &```

```pipeline-command1 && pipeline-command2```
```pipeline-command1 && pipeline-command2 ;```
```pipeline-command1 && pipeline-command2 &```

```pipeline-command1 || pipeline-command2```
```pipeline-command1 || pipeline-command2 ;```
```pipeline-command1 || pipeline-command2 &```

```pipeline-command1 && pipeline-command2 ; pipeline-command3 || pipeline-command4 & ```

Commands separated by a ```;``` are executed sequentially; the shell waits for each command to terminate in turn. The return status is the exit status of the last command executed.

If a command is terminated by the control operator ```&```, the shell executes the command asynchronously in a ***subshell***. This is known as executing the command in the ***background***. The shell does not wait for the command to finish, and the return status is 0 (true).

```command1 && command2```

*command2* is executed if, and only if, *command1* returns an exit status of zero. The return status of AND lists is the exit status of the last command executed in the list.

```command1 || command2```

*command2* is executed if, and only if, *command1* returns a non-zero exit status. The return status of OR lists is the exit status of the last command executed in the list.

## Compound Commands

Compound commands are the shell programming constructs.

### Looping Constructs

***until***

```
until test-commands; do consequent-commands; done
```

```
until test-commands
do
    consequent-commands
done
```

Execute *consequent-commands* as long as *test-commands* has an exit status which is ***not zero***.

The return status is the exit status of the last command executed in *consequent-commands*, or zero if none was executed.

***while***

```
while test-commands; do consequent-commands; done
```

```
while test-commands
do
    consequent-commands
done
```

Execute *consequent-commands* as long as *test-commands* has an exit status of ***zero***.

The return status is the exit status of the last command executed in *consequent-commands*, or zero if none was executed.

***for***

```
for name [ [in [words ...] ] ; ] do commands; done
```

```
for name [ [in [words ...] ] ; ]
do
    commands
done
```

Expand *words*, and execute *commands* once for each member in the resultant list, with *name* bound to the current member.

If ```in words``` is not present, the *for* command executes the *commands* once for each positional parameter that is set, as if ```in "$@"``` had been specified.

The return status is the exit status of the last command that executes. If there are no items in the expansion of *words*, no commands are executed, and the return status is zero.

```
for (( expr1 ; expr2 ; expr3 )) ; do commands ; done
```

```
for (( expr1 ; expr2 ; expr3 ))
do
    commands
done
```

First, the arithmetic expression *expr1* is evaluated. The arithmetic expression *expr2* is then evaluated repeatedly until it evaluates to ***zero***. Each time *expr2* evaluates to a ***non-zero*** value, *commands* are executed and the arithmetic expression *expr3* is evaluated. If any expression is omitted, it behaves as if it evaluates to ***1***.

The return value is the exit status of the last command in commands that is executed, or *false* if any of the expressions is invalid.

***break***

***continue***

### Conditional Constructs

***if***

```
if test-commands; then
  consequent-commands;
[elif more-test-commands; then
  more-consequents;]
[else alternate-consequents;]
fi
```

The *test-commands* list is executed, and if its return status is ***zero***, the *consequent-commands* list is executed. If *test-commands* returns a ***non-zero*** status, each *elif* list is executed in turn, and if its exit status is ***zero***, the corresponding *more-consequents* is executed and the command completes. If *else alternate-consequents* is present, and the final command in the final *if* or *elif* clause has a ***non-zero*** exit status, then *alternate-consequents* is executed.

The return status is the exit status of the last command executed, or zero if no condition tested true.

***case***

```
case word in
    [ [(] pattern1 [| pattern2]...) command-list ;; ]
    ...
    [ [(] pattern1 [| pattern2]...) command-list ;& ]
    ...
    [ [(] pattern1 [| pattern2]...) command-list ;;& ]
    ...
    [ [()] *) always-match-command-list ;; ]
esac
```

*case* will selectively execute the *command-list* corresponding to the first pattern that matches *word*. The ```|``` is used to separate multiple patterns, and the ```)``` operator terminates a pattern list. A list of patterns and an associated command-list is known as a *clause*.

Each *clause* must be terminated with ```;;```, ```;&```, or ```;;&```:

* If the ```;;``` operator is used, no subsequent matches are attempted after the first pattern match.

* Using ```;&``` in place of ```;;``` causes execution to continue with the *command-list* associated with the next clause, if any.

* Using ```;;&``` in place of ```;;``` causes the shell to test the patterns in the next clause, if any, and execute any associated *command-list* on a successful match.

It’s a common idiom to use ```*``` as the final pattern to define the default case, since that pattern will always match.

The return status is zero if no pattern is matched. Otherwise, the return status is the exit status of the *command-list* executed.

***select***

```
select name [in words ...]; do commands; done
```

```
select name [in words ...]
do
    commands
done
```

If the ```in words``` is omitted, the positional parameters are printed, as if ```in "$@"``` had been specified.

The *commands* are executed after each selection until a *break* command is executed, at which point the select command completes.

***(( expression ))***

```
(( expression ))
```

The arithmetic *expression* is evaluated. If the value of the *expression* is ***non-zero***, the return status is ***0***; otherwise the return status is ***1***. This is exactly equivalent to ```let "expression"``` for a full description of the ```let``` builtin.

***[[ expression ]]***

```
[[ expression ]]
```

Return a status of 0 or 1 depending on the evaluation of the conditional expression *expression*.

Word splitting and filename expansion are not performed on the words between the [[ and ]]; tilde expansion, parameter and variable expansion, arithmetic expansion, command substitution, process substitution, and quote removal are performed. Conditional operators such as ```-f``` must be unquoted to be recognized as primaries.

### Command Grouping

When commands are grouped, redirections may be applied to the entire command list.

***( list )***

```
( list )
```

Placing a list of commands between parentheses causes a subshell environment to be created, and each of the commands in list to be executed in that ***subshell***. Since the *list* is executed in a subshell, variable assignments do not remain in effect after the subshell completes.

***{ list; }***

```
{ list; }
```

Placing a list of commands between curly braces causes the list to be executed in the ***current shell context***. No subshell is created. The semicolon (or newline) following list is required.

**[NOTE]**
In addition to the creation of a subshell, there is a subtle difference between these two constructs due to historical reasons. The braces are reserved words, so they must be separated from the list by *blanks* or other shell *metacharacters*. The parentheses are operators, and are recognized as separate tokens by the shell even if they are not separated from the list by whitespace.

The exit status of both of these constructs is the exit status of *list*.

# Shell Expansions

Expansion is performed on the command line after it has been split into tokens, refer to *step 4* in [Bash Operation](#bash-operation). There are seven kinds of expansion performed from ***higher priority*** to ***lower priority***:

1. ***Brace expansion***
2. ***Tilde expansion***
3. ***Parameter and variable expansion***
4. ***Arithmetic expansion***
5. ***Command substitution***
6. ***Process Substitution*** (on systems that support *named pipes (FIFOs)* or the */dev/fd* method of naming open files)
7. ***Word splitting***
8. ***Filename expansion***

## Brace expansion

***Format #1:***
[*preamble*]**{****str1****,**[*str2***,**[*str3***,***...*]]**}**[*postscript*]

* Brace expansions may be nested.

***Format #2:***
**{***x***..***y*[**..***incr*]**}**

* Both x and y must be of the same type.
* The default increment *incr* is 1 or -1 as appropriate.

***Examples:***

| Brace_pattern | Brace_expansions | Note |
| :------------ | :--------------- | :--- |
| ```a{b,c,d}e``` | abe ace ade | Format #1  |
| ```a{b,c,{e,f}}g``` | abg acg aeg afg | Format #1 |
| ```{a..e}```  | a b c d e | Format #2. *x* and *y* are single characters. The default increment is 1 or -1 as appropriate. |
| ```{a..e..2}``` | a c e | Format #2. *x* and *y* are single characters. |
| ```{e..a..2}``` | e c a | Format #2. *x* and *y* are single characters. |
| ```{e..a..-2}``` | e c a | Format #2. *x* and *y* are single characters. |
| ```{1..5}```  | 1 2 3 4 5 | Format #2. *x* and *y* are either integers. The default increment is 1 or -1 as appropriate. |
| ```{5..1}```  | 5 4 3 2 1 | Format #2. *x* and *y* are either integers. The default increment is 1 or -1 as appropriate. |
| ```{1..5..2}``` | 1 3 5 | Format #2. *x* and *y* are either integers |
| ```{5..1..2}``` | 5 3 1 | Format #2. *x* and *y* are either integers |
| ```{5..1..-2}``` | 5 3 1 | Format #2. *x* and *y* are either integers |
| ```{01..5..2}``` | 01 03 05 | Format #2. Prefixed with **0** to force each term to have the same width. |
| ```{01..12..2}``` | 01 03 05 07 09 11 |  Format #2. Prefixed with **0** to force each term to have the same width. |

<p/>

## Tilde expansion

| Tilde_prefixes | Tilde_expansions | Note |
| :------------- | :--------------- | :--- |
| ```~```        | The value of $HOME | |
| ```~/foo```    | $HOME/foo | |
| ```~fred/foo``` | The subdirectory *foo* of the home directory of the user ***fred*** | |
| ```~+/foo```   | $PWD/foo | |
| ```~-/foo```   | ${OLDPWD-'~-'}/foo | |
| ```~N```       | The string that would be displayed by ```dirs +N``` | If the tilde-prefix, sans the tilde, consists of a number without a leading ***+*** or ***-***, ***+*** is assumed. |
| ```~+N```      | The string that would be displayed by ```dirs +N``` | |
| ```~-N```      | The string that would be displayed by ```dirs -N``` | |

<p/>

## Parameter and variable expansion

The **$** character introduces parameter expansion, command substitution, or arithmetic expansion.

***Format #1:***
**${***parameter***}**

* The value of parameter is substituted.

***Format #2:***
**${***parameter***:-***word***}**

* If *parameter* is unset or null, the expansion of *word* is substituted. Otherwise, the value of *parameter* is substituted.

***Format #3:***
**${***parameter***:=***word***}**

* If *parameter* is unset or null, the expansion of *word* is assigned to *parameter*. The value of *parameter* is then substituted.
* Positional parameters and special parameters may not be assigned to in this way.

***Format #4:***
**${***parameter***:?***word***}**

* If *parameter* is null or unset, the expansion of *word* is written to the standard error and the shell, if it is not interactive, exits. Otherwise, the value of *parameter* is substituted.

***Format #5:***
**${***parameter***:+***word***}**

* If *parameter* is null or unset, nothing is substituted, otherwise the expansion of *word* is substituted.

***Format #6:***
**${***parameter***:***offset***}**
**${***parameter***:***offset***:***length***}**

* This is referred to as **Substring Expansion**.
* It expands to up to *length* characters of the value of *parameter* starting at the character specified by *offset*. If *length* is omitted, it expands to the substring of the value of *parameter* starting at the character specified by *offset* and extending to the end of the value. *length* and *offset* are arithmetic expressions.
* If *offset* evaluates to a number ***less than zero***, the value is used as an *offset* in characters from the end of the value of *parameter*. If *length* evaluates to a number ***less than zero***, it is interpreted as an *offset* in characters from the end of the value of *parameter* rather than a number of characters, and the expansion is the characters between *offset* and that result.
* Note that a negative *offset* must be separated from the colon by at least one space to avoid being confused with the **:-** expansion.

***Examples of format #6:***
```$ string=01234567890abcdefgh```

| Formats | Parameter_expansions | Note |
| :-------| :------------------- | :--- |
| ```echo ${string:7}``` | 7890abcdefgh | |
| ```echo ${string:7:2}``` | 78 | |
| ```echo ${string:7:-2}``` | 7890abcdef | |
| ```echo ${string: -7}``` | bcdefgh | |
| ```echo ${string: -7:2}``` | bc | |
| ```echo ${string: -7:-2}``` | bcdef | |

<p/>

***Examples of format #6:***
```$ set -- 01234567890abcdefgh```

| Formats | Parameter_expansions | Note |
| :-------| :------------------- | :--- |
| ```echo ${1:7}``` | 7890abcdefgh | |
| ```echo ${1:7:2}``` | 78 | |
| ```echo ${1:7:-2}``` | 7890abcdef | |
| ```echo ${1: -7}``` | bcdefgh | |
| ```echo ${1: -7:2}``` | bc | |
| ```echo ${1: -7:-2}``` | bcdef | |

<p/>

***Examples of format #6:***
```$ set -- 1 2 3 4 5 6 7 8 9 0 a b c d e f g h```

| Formats | Parameter_expansions |
| :-------| :------------------- |
| ```echo ${@:7}``` | 7 8 9 0 a b c d e f g h |
| ```echo ${@:7:2}``` | 7 8 |
| ```echo ${@:7:-2}``` | bash: -2: substring expression < 0 |
| ```echo ${@: -1}``` | h<br><br>A negative *offset* is taken relative to one greater than the greatest positional<br>parameter, so an offset of *-1* evaluates to the last positional parameter. |
| ```echo ${@: -7}``` | b c d e f g h |
| ```echo ${@: -7:2}``` | b c |
| ```echo ${@:0}``` | bash 1 2 3 4 5 6 7 8 9 0 a b c d e f g h |
| ```echo ${@:0:2}``` | bash 1 |

<p/>

***Examples of format #6:***
```$ array=(0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h)```

| Formats | Parameter_expansions | Note |
| :-------| :------------------- | :--- |
| ```echo ${array[@]:7}``` | 7 8 9 0 a b c d e f g h | |
| ```echo ${array[@]:7:2}``` | 7 8 | |
| ```echo ${array[@]:7:-2}``` | bash: -2: substring expression < 0 | |
| ```echo ${array[@]:0}``` | 0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h | |
| ```echo ${array[@]:0:2}``` | 0 1 | |

<p/>

***Format #7:***
**${!***prefix***@}**
**${!***prefix****}**

* Expands to the names of variables whose names begin with *prefix*, separated by the first character of the *IFS* special variable. When ‘@’ is used and the expansion appears within double quotes, each variable name expands to a separate word.

***Examples of format #7:***
```$ string1=01234567890abcdefgh```
```$ string2=abcdefghijk01234567```

| Formats | Parameter_expansions | Note |
| :-------| :------------------- | :--- |
| ```echo ${!strin*}``` | string1 string2 | |
| ```echo ${!strin@}``` | string1 string2 | |

<p/>

***Format #8:***
**${!**name**[@]}**
**${!**name**[*]}**

* If *name* is an array variable, expands to the list of array indices (keys) assigned in *name*. If *name* is not an array, expands to 0 if *name* is set and null otherwise. When *@* is used and the expansion appears within double quotes, each key expands to a separate word.

***Examples of format #8:***
```$ array1=(0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h)```
```$ array2=(a b c d e f g h i j k 0 1 2 3 4 5 6 7)```

| Formats | Parameter_expansions | Note |
| :-------| :------------------- | :--- |
| ```echo ${!strin*}``` | string1 string2 | |
| ```echo ${!strin@}``` | string1 string2 | |

<p/>

***Format #9***
**${#***parameter***}**

* The length in characters of the expanded value of *parameter* is substituted.

* If parameter is ***** or **@**, the value substituted is the number of positional parameters.

* If *parameter* is an array name subscripted by ***** or **@**, the value substituted is the number of elements in the array.

***Examples of format #9:***
```$ string=01234567890abcdefgh```
```$ set -- 0 1 2 3 4 5 6 7 8 9```
```$ array=(0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h)```

| Formats | Parameter_expansions | Note |
| :-------| :------------------- | :--- |
| ```echo ${#string}``` | 19 | |
| ```echo ${#*}``` | 10 | positional parameters |
| ```echo ${#@}``` | 10 | positional parameters |
| ```echo ${#array[*]}``` | 19 | array |
| ```echo ${#array[@]}``` | 19 | array |

<p/>

***Format #10:***
**${***parameter***#***word***}**
**${***parameter***##***word***}**

* The *word* is expanded to produce a pattern just as in filename expansion. If the pattern matches the beginning of the expanded value of *parameter*, then the result of the expansion is the expanded value of *parameter* with the shortest matching pattern (the **#** case) or the longest matching pattern (the **##** case) deleted.

* If *parameter* is **@** or *****, the pattern removal operation is applied to each positional parameter in turn, and the expansion is the resultant list.

* If *parameter* is an array variable subscripted with **@** or *****, the pattern removal operation is applied to each member of the array in turn, and the expansion is the resultant list.

***Examples of format #10:***
```$ string=012345012345abcdeabcde```
```$ set -- 0 1 2 3 4 5 6 7 8 9```
```$ array=(0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h)```

| Formats | Parameter_expansions | Note |
| :-------| :------------------- | :--- |
| ```echo ${string#012*5}``` | 012345abcdeabcde | |
| ```echo ${string##012*5}``` | abcdeabcde | |
| ```echo ${string##012*5}``` | abcdeabcde | |
| ```echo ${string#012?5}``` | 012345abcdeabcde | |
| ```echo ${string##012?5}``` | 012345abcdeabcde | |
| ```echo ${*#5}``` | 0 1 2 3 4 6 7 8 9 | positional parameters |
| ```echo ${array[*]#b}``` | 0 1 2 3 4 5 6 7 8 9 0 a c d e f g h | array |
| ```echo ${array[@]#b}``` | 0 1 2 3 4 5 6 7 8 9 0 a c d e f g h | array |

<p/>

***Format #11:***
**${***parameter***%***word***}**
**${***parameter***%%***word***}**

* The *word* is expanded to produce a pattern just as in filename expansion. If the pattern matches a trailing portion of the expanded value of *parameter*, then the result of the expansion is the value of parameter with the shortest matching pattern (the **%** case) or the longest matching pattern (the **%%** case) deleted.

* If *parameter* is **@** or *****, the pattern removal operation is applied to each positional parameter in turn, and the expansion is the resultant list.

* If *parameter* is an array variable subscripted with **@** or *****, the pattern removal operation is applied to each member of the array in turn, and the expansion is the resultant list.

***Examples of format #11:***
```$ string=012345012345abcdeabcde```
```$ set -- 0 1 2 3 4 5 6 7 8 9```
```$ array=(0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h)```

| Formats | Parameter_expansions | Note |
| :-------| :------------------- | :--- |
| ```echo ${string%abc*e}``` | 012345012345abcde | |
| ```echo ${string%%abc*e}``` | 012345012345 | |
| ```echo ${string%abc?de}``` | 012345012345abcde | |
| ```echo ${string%%abc?de}``` | 012345012345abcde | |
| ```echo ${*%8}``` | 0 1 2 3 4 5 6 7 9 | positional parameters |
| ```echo ${array[*]%b}``` | 0 1 2 3 4 5 6 7 8 9 0 a c d e f g h | array |
| ```echo ${array[@]%%b}``` | 0 1 2 3 4 5 6 7 8 9 0 a c d e f g h | array |

<p/>

***Format #12:***
**${***parameter***/***pattern***/***string***}**

* The *pattern* is expanded to produce a pattern just as in filename expansion. *parameter* is expanded and the longest match of *pattern* against its value is replaced with *string*.

* If *pattern* begins with **/**, all matches of *pattern* are replaced with *string*. Normally only the first match is replaced.

* If pattern begins with **#**, it must match at the beginning of the expanded value of *parameter*. If *pattern* begins with **%**, it must match at the end of the expanded value of *parameter*.

* If *string* is null, matches of *pattern* are deleted and the **/** following *pattern* may be omitted.

* If *parameter* is **@** or *****, the substitution operation is applied to each positional parameter in turn, and the expansion is the resultant list.

* If *parameter* is an array variable subscripted with **@** or *****, the substitution operation is applied to each member of the array in turn, and the expansion is the resultant list.

***Examples of format #12:***
```$ string=012345012345abcdeabcde```
```$ set -- 0 1 2 3 4 5 6 7 8 9```
```$ array=(0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h)```

| Formats | Parameter_expansions | Note |
| :-------| :------------------- | :--- |
| ```echo ${string/abc/xyz}``` | 012345012345xyzdeabcde | |
| ```echo ${string//abc/xyz}``` | 012345012345xyzdexyzde | |
| ```echo ${string/#012/xyz}``` | xyz345012345abcdeabcde | |
| ```echo ${string/%cde/xyz}``` | 012345012345abcdeabxyz | |
| ```echo ${string/cde/}``` | 012345012345abcdeab | |
| ```echo ${*/2/x}``` | 0 1 x 3 4 5 6 7 8 9 | positional parameters |
| ```echo ${@/2/x}``` | 0 1 x 3 4 5 6 7 8 9 | positional parameters |
| ```echo ${*/2/}``` | 0 1 3 4 5 6 7 8 9 | positional parameters |
| ```echo ${@/2/}``` | 0 1 3 4 5 6 7 8 9 | positional parameters |
| ```echo ${array[*]/a/x}``` | 0 1 2 3 4 5 6 7 8 9 0 x b c d e f g h | array |
| ```echo ${array[@]/a/x}``` | 0 1 2 3 4 5 6 7 8 9 0 x b c d e f g h | array |
| ```echo ${array[*]/a/}``` | 0 1 2 3 4 5 6 7 8 9 0 b c d e f g h | array |
| ```echo ${array[@]/a/}``` | 0 1 2 3 4 5 6 7 8 9 0 b c d e f g h | array |

<p/>

***Format #13:***
**${***parameter***^***pattern***}**
**${***parameter***^^***pattern***}**
**${***parameter***,***pattern***}**
**${***parameter***,,***pattern***}**

* This expansion modifies the case of alphabetic characters in *parameter*. The *pattern* is expanded to produce a *pattern* just as in filename expansion. Each character in the expanded value of *parameter* is tested against *pattern*, and, if it matches the *pattern*, its case is converted.

* The *pattern* should not attempt to match more than one character.

* The **^** operator converts lowercase letters matching pattern to uppercase; the **,** operator converts matching uppercase letters to lowercase.

* The **^^** and **,,** expansions convert each matched character in the expanded value; the **^** and **,** expansions match and convert only the first character in the expanded value.

* If *parameter* is **@** or *****, the case modification operation is applied to each positional parameter in turn, and the expansion is the resultant list.

* If *parameter* is an array variable subscripted with **@** or *****, the case modification operation is applied to each member of the array in turn, and the expansion is the resultant list.

***Examples of format #13:***
```$ string=abcdeABCDEabcdeABCDE```
```$ set -- ABCDEabcdeABCDEabcde```
```$ array=(A B C D E a b c d e A B C D E a b c d e)```

| Formats | Parameter_expansions | Note |
| :-------| :------------------- | :--- |
| ```echo ${string^a}``` | AbcdeABCDEabcdeABCDE | |
| ```echo ${string^^a}``` | AbcdeABCDEAbcdeABCDE | |
| ```echo ${string,A}``` | abcdeABCDEabcdeABCDE | |
| ```echo ${string,,A}``` | abcdeaBCDEabcdeaBCDE | |
| ```echo ${*^a}``` | ABCDEabcdeABCDEabcde | positional parameters |
| ```echo ${*^^a}``` | ABCDEAbcdeABCDEAbcde | positional parameters |
| ```echo ${@^a}``` | ABCDEabcdeABCDEabcde | positional parameters |
| ```echo ${@^^a}``` | ABCDEAbcdeABCDEAbcde | positional parameters |
| ```echo ${*,A}``` | aBCDEabcdeABCDEabcde | positional parameters |
| ```echo ${*,,A}``` | aBCDEabcdeaBCDEabcde | positional parameters |
| ```echo ${@,A}``` | aBCDEabcdeABCDEabcde | positional parameters |
| ```echo ${@,,A}``` | aBCDEabcdeaBCDEabcde | positional parameters |
| ```echo ${array[*]^a}``` | A B C D E A b c d e A B C D E A b c d e | array |
| ```echo ${array[*]^^a}``` | A B C D E A b c d e A B C D E A b c d e | array |
| ```echo ${array[@]^a}``` | A B C D E A b c d e A B C D E A b c d e | array |
| ```echo ${array[@]^^a}``` | A B C D E A b c d e A B C D E A b c d e | array |
| ```echo ${array[*],A}``` | a B C D E a b c d e a B C D E a b c d e | array |
| ```echo ${array[*],,A}``` | a B C D E a b c d e a B C D E a b c d e | array |
| ```echo ${array[@],A}``` | a B C D E a b c d e a B C D E a b c d e | array |
| ```echo ${array[@],,A}``` | a B C D E a b c d e a B C D E a b c d e | array |

<p/>

## Arithmetic expansion

***Format:***
**$((** *expression* **))**

* Arithmetic expansion allows the evaluation of an arithmetic expression and the substitution of the result.

* The *expression* is treated as if it were within double quotes, but a double quote inside the parentheses is not treated specially.

* All tokens in the *expression* undergo [parameter and variable expansion](#parameter-and-variable-expansion), [command substitution](#command-substitution), and **quote removal**. The result is treated as the arithmetic expression to be evaluated.

* Arithmetic expansions may be nested.

* If the *expression* is invalid, Bash prints a message indicating failure to the standard error and no substitution occurs.

***Examples:***

| Formats | Parameter_expansions | Note |
| :-------| :------------------- | :--- |
| ```echo $(( 1+2 ))``` | 3 | |

## Command Substitution

***Format:***
**$(***command***)**
**\`***command***\`**

* Command substitution allows the output of a command to replace the command itself.

* Bash performs the expansion by executing *command* and replacing the *command* substitution with the standard output of the *command*, ***with any trailing newlines deleted***. Embedded newlines are not deleted, but they may be removed during word splitting.

* The command substitution ```$(cat file)``` can be replaced by the equivalent but faster ```$(< file)```.

***Examples:***

| Formats | Parameter_expansions |
| :-------| :------------------- |
| ```echo $(ls -l *ml)``` | -rw-rw-r-- 1 chenwx chenwx 1299 Dec 9 22:04 _config.yml -rw-r--r-- 1 chenwx chenwx 1439 Nov 28 15:35 feed.xml -rw-rw-r-- 1 chenwx chenwx 54 Dec 1 07:30 index.html |
| ```echo `ls -l *ml```` | -rw-rw-r-- 1 chenwx chenwx 1299 Dec 9 22:04 _config.yml -rw-r--r-- 1 chenwx chenwx 1439 Nov 28 15:35 feed.xml -rw-rw-r-- 1 chenwx chenwx 54 Dec 1 07:30 index.html |

<p/>

## Process Substitution

***Format:***

**<(***list***)**
**>(***list***)**

* Process substitution is supported on systems that support named pipes (FIFOs) or the /dev/fd method of naming open files.

* If the ```>(list)``` form is used, writing to the file will provide input for list. If the ```<(list)``` form is used, the file passed as an argument should be read to obtain the output of list.

* Note that no space may appear between the < or > and the left parenthesis, otherwise the construct would be interpreted as a redirection.

* When available, process substitution is performed simultaneously with **parameter and variable expansion**, **command substitution**, and **arithmetic expansion**.

## Word Splitting

The shell scans the results of **parameter expansion**, **command substitution**, and **arithmetic expansion** that did not occur within double quotes for word splitting.

The shell treats each character of ```$IFS``` as a delimiter, and splits the results of the other expansions into words using these characters as field terminators. If the value of ```$IFS``` is null, no word splitting occurs.

Note that if no expansion occurs, no splitting is performed.

## Filename Expansion

After word splitting, unless the ```-f``` option has been set, Bash scans each word for the characters **\***, **?**, and **[**. If one of these characters appears, then the word is regarded as a pattern, and replaced with an alphabetically sorted list of filenames matching the pattern.

* If no matching filenames are found, and the shell option ```nullglob``` is disabled, the word is left unchanged. If the ```nullglob``` option is set, and no matches are found, the word is removed.

* If the shell option ```failglob``` is set, and no matches are found, an error message is printed and the command is not executed.

* If the shell option ```nocaseglob``` is enabled, the match is performed without regard to the case of alphabetic characters.

When a pattern is used for filename expansion, the character ```.``` at the start of a filename or immediately following a slash must be matched explicitly, unless the shell option ```dotglob``` is set. When matching a filename, the slash character must always be matched explicitly. In other cases, the ```.``` character is not treated specially.

The shell variable ```GLOBIGNORE``` may be used to restrict the set of filenames matching a pattern.

* If ```GLOBIGNORE``` is set, each matching filename that also matches one of the patterns in ```GLOBIGNORE``` is removed from the list of matches. The filenames ```.``` and ```..``` are always ignored when ```GLOBIGNORE``` is set and not null. However, setting ```GLOBIGNORE``` to a non-null value has the effect of enabling the ```dotglob``` shell option, so all other filenames beginning with a ```.``` will match.

* To get the old behavior of ignoring filenames beginning with a ```.```, make ```.*``` one of the patterns in ```GLOBIGNORE```. The ```dotglob``` option is disabled when ```GLOBIGNORE``` is unset.

| Special_Pattern_Character | Description |
| :------------------------ | :---------- |
| ```*```                   | Matches any string, including the null string.<br><br>When the ```globstar``` shell option is enabled, and ```*``` is used in a filename expansion context, two adjacent ```*```s used as a single pattern will match all files and zero or more directories and subdirectories. If followed by a ```/```, two adjacent ```*```s will match only directories and subdirectories. |
| ```?```                   | Matches any single character. |
| ```[...]```<br><br>```[a-z]```<br><br>```[!...]```<br>```[^...]```<br><br>```[-...]```<br>```[...-]```<br><br>```[]...]```<br><br>```[:class:]```<br><br>```[=c=]```<br><br>```[.symbol.]``` | Matches any one of the enclosed characters.<br><br>A pair of characters separated by a hyphen ```-``` denotes a range expression; any character that falls between those two characters, inclusive, using the current locale's collating sequence and character set, is matched.<br><br>If the first character following the ```[``` is a ```!``` or a ```^``` then any character not enclosed is matched.<br><br>A ```-``` may be matched by including it as the first or last character in the set.<br><br>A ```]``` may be matched by including it as the first character in the set.<br><br>Within **[** and **]**, character classes can be specified using the syntax **[:***class***:]**, where *class* is one of the following classes defined in the POSIX standard:<br>```alnum``` ```alpha``` ```ascii``` ```blank``` ```cntrl``` ```digit``` ```graph```<br>```lower``` ```print``` ```punct``` ```space``` ```upper``` ```word``` ```xdigit```<br>A character class matches any character belonging to that class. The ```word``` character class matches **letters**, **digits**, and the character **_**.<br><br>Within **[** and **]**, an *equivalence class* can be specified using the syntax **[=***c***=]**, which matches all characters with the same collation weight as the character *c*.<br><br>Within **[** and **]**, the syntax **[.***symbol***.]** matches the collating symbol *symbol*.<br><br>The sorting order of characters in range expressions is determined by the current locale and the values of the ```LC_COLLATE``` and ```LC_ALL``` shell variables, if set. |
| ```?(pattern-list)``` | Matches **zero or one** occurrence of the given patterns if the shell option ```extglob``` is enabled using the ```shopt``` builtin. A *pattern-list* is a list of one or more patterns separated by a ```|```. |
| ```*(pattern-list)```<br>```+(pattern-list)``` | Matches **zero or more** occurrences of the given patterns if the shell option ```extglob``` is enabled using the ```shopt``` builtin. A *pattern-list* is a list of one or more patterns separated by a ```|```. |
| ```@(pattern-list)``` | Matches **one** of the given patterns if the shell option ```extglob``` is enabled using the ```shopt``` builtin. A *pattern-list* is a list of one or more patterns separated by a ```|```. |
| ```!(pattern-list)``` | Matches anything except one of the given patterns if the shell option ```extglob``` is enabled using the ```shopt``` builtin. A *pattern-list* is a list of one or more patterns separated by a ```|```. |

<p/>

# Redirections

Redirection allows commands' file handles to be duplicated, opened, closed, made to refer to different files, and can change the files the command reads from and writes to. Redirection may also be used to modify file handles in the current shell execution environment.

The following redirection operators may precede or appear anywhere **within a simple command** or may **follow a command**.

Redirections are processed in the order they appear, from left to right.

The word following the redirection operator in the following descriptions, unless otherwise noted, is subjected to **brace expansion**, **tilde expansion**, **parameter expansion**, **command substitution**, **arithmetic expansion**, **quote removal**, **filename expansion**, and **word splitting**.

A failure to open or create a file causes the redirection to fail.

Redirections using file descriptors greater than 9 should be used with care, as they may conflict with file descriptors the shell uses internally.

Bash handles several filenames specially when they are used in redirections, as described in the following table:

| Special_Filenames | Descriptions |
| :---------------- | :----------- |
| ```ls > dirlist 2>&1``` | Directs both standard output (file descriptor 1) and standard error (file descriptor 2) to the file *dirlist*.  Note that the order of redirections is significant. |
| ```ls 2>&1 > dirlist``` | Directs only the standard output to file *dirlist*, because the standard error was made a copy of the standard output before the standard output was redirected to *dirlist*. |
| ```/dev/fd/fd``` | If *fd* is a valid integer, file descriptor *fd* is duplicated. |
| ```/dev/stdin``` | File descriptor 0 is duplicated. |
| ```/dev/stdout``` | File descriptor 1 is duplicated. |
| ```/dev/stderr``` | File descriptor 2 is duplicated. |
| ```/dev/tcp/host/port``` | If *host* is a valid hostname or Internet address, and *port* is an integer port number or service name, Bash attempts to open the corresponding **TCP socket**. |
| ```/dev/udp/host/port``` | If *host* is a valid hostname or Internet address, and *port* is an integer port number or service name, Bash attempts to open the corresponding **UDP socket**. |

<p/>

Redirection operators:

| Redirections | Descriptions |
| :----------- | :----------- |
| ```[n]<word``` | Redirection of input causes the file whose name results from the expansion of *word* to be opened for reading on file descriptor *n*, or the standard input (file descriptor **0**) if *n* is not specified. |
| ```[n]>[|]word``` | Redirection of output causes the file whose name results from the expansion of *word* to be opened for writing on file descriptor *n*, or the standard output (file descriptor **1**) if *n* is not specified. If the file does not exist it is created; if it does exist it is truncated to zero size.<br><br>If the redirection operator is ```>```, and the ```noclobber``` option to the **set** builtin has been enabled, the redirection will fail if the file whose name results from the expansion of *word* exists and is a regular file.<br><br>If the redirection operator is ```>|```, or the redirection operator is ```>``` and the ```noclobber``` option is not enabled, the redirection is attempted even if the file named by *word* exists.  |
| ```[n]>>word``` | Redirection of output in this fashion causes the file whose name results from the expansion of *word* to be opened for appending on file descriptor *n*, or the standard output (file descriptor **1**) if *n* is not specified. If the file does not exist it is created. |
| ```&>word```<br>```>word 2>&1```<br><br>```>&word``` | This construct allows both the standard output (file descriptor **1**) and the standard error output (file descriptor **2**) to be redirected to the file whose name is the expansion of *word*.<br><br>The form ```&>word``` is preferred, which is semantically equivalent to ```>word 2>&1```.<br><br>When using the form ```>&word```, *word* may not expand to a number or -. If it does, other redirection operators apply for compatibility reasons. |

# Executing Commands

## Simple Command Expansion

When a simple command is executed, the shell performs the following expansions, assignments, and redirections, from left to right.

1. The words that the parser has marked as **variable assignments** (those preceding the command name) and **redirections** are saved for later processing.
2. The words that are not **variable assignments** or **redirections** are expanded (see [Shell Expansions](#shell-expansions)). If any words remain after expansion, the first word is taken to be the name of the command and the remaining words are the arguments.
3. Redirections are performed as described in [Redirections](#redirections).
4. The text after the ```=``` in each variable assignment undergoes **tilde expansion**, **parameter expansion**, **command substitution**, **arithmetic expansion**, and **quote removal** before being assigned to the variable.
5. If no command name results, the **variable assignments** affect the current shell environment. Otherwise, the variables are added to the environment of the executed command and do not affect the current shell environment. If any of the assignments attempts to assign a value to a readonly variable, an error occurs, and the command exits with a non-zero status.

If no command name results, **redirections** are performed, but do not affect the current shell environment. A redirection error causes the command to exit with a non-zero status.

If there is a command name left after expansion, execution proceeds as described below. Otherwise, the command exits. If one of the expansions contained a command substitution, the exit status of the command is the exit status of the last command substitution performed. If there were no command substitutions, the command exits with a status of zero.

## Command Search and Execution

The following figure shows the command search and execution:

![Command Search and Execution](/assets/Executing_Commands.png)

## Exit Status

The exit status of an executed command is the value returned by the ***waitpid*** system call or equivalent function. Exit statuses fall ***between 0*** and ***255***, though, as explained below, the shell may use values above ***125*** specially. Exit statuses from **shell builtins** and **compound commands** are also limited to this range. Under certain circumstances, the shell will use special values to indicate specific failure modes.

For the shell's purposes, **a command which exits with a zero exit status has succeeded**. **A non-zero exit status indicates failure**. This seemingly counter-intuitive scheme is used so there is one well-defined way to indicate success and a variety of ways to indicate various failure modes.

* If a command is found but is not executable, the return status is ***126***.

* If a command is not found, the child process created to execute it returns a status of ***127***.

* If a command terminates on a **fatal signal** whose number is *N*, Bash uses the value **128+***N* as the exit status.

* If a command fails because of an error during expansion or redirection, the exit status is ***greater than zero***.

The exit status is used by the Bash conditional commands and some of the list constructs.

All of the Bash **builtins** return an exit status of zero if they succeed and a non-zero status on failure, so they may be used by the conditional and list constructs. All **builtins** return an exit status of ***2*** to indicate incorrect usage.

Check the special parameter **$?** to get the exit status of the most recently executed foreground pipeline.

| Exit_values | Description |
| :---------: | :---------- |
| **0**       | The command is executed successfully. |
| **2**       | All **builtins** return an exit status of ***2*** to indicate incorrect usage. |
| **126**     | If a command is found but is not executable, the return status is ***126***. |
| **127**     | If a command is not found, the child process created to execute it returns a status of ***127***. |
| **128+***N* | If a command terminates on a **fatal signal** whose number is *N*, Bash uses the value **128+***N* as the exit status. |

<p/>

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
| ```bind```    | Format:<br>```bind [-m keymap] [-lpsvPSVX]```<br>```bind [-m keymap] [-q function] [-u function] [-r keyseq]```<br>```bind [-m keymap] -f filename```<br>```bind [-m keymap] -x keyseq:shell-command```<br>```bind [-m keymap] keyseq:function-name```<br>```bind readline-command```<br><br>Display current Readline key and function bindings, bind a key sequence to a Readline function or macro, or set a Readline variable. Each non-option argument is a command as it would appear in a Readline initialization file, but each binding or command must be passed as a separate argument.<br><br>```bind -p```<br>```"\C-x\C-r":re-read-init-file```.<br><br>The return status is zero unless an invalid option is supplied or an error occurs. |
| ```builtin``` | Format:<br>```builtin [shell-builtin [args]]```<br><br>Run a shell builtin, passing it *args*, and return its exit status. This is useful when defining a shell function with the same name as a shell builtin, retaining the functionality of the builtin within the function. The return status is non-zero if *shell-builtin* is not a shell builtin command. |
| ```caller```  | Format:<br>```caller [expr]```<br><br>Returns the context of any active subroutine call (a shell function or a script executed with the . or source builtins).<br><br>Without *expr*, *caller* displays the line number and source filename of the current subroutine call. If a non-negative integer is supplied as *expr*, *caller* displays the line number, subroutine name, and source file corresponding to that position in the current execution call stack. This extra information may be used, for example, to print a stack trace. The current frame is frame 0.<br><br>The return value is 0 unless the shell is not executing a subroutine call or *expr* does not correspond to a valid position in the call stack. |
| ```command``` | Format:<br>```command [-pVv] command [arguments ...]```<br><br>Runs *command* with *arguments* ignoring any shell function named *command*. Only shell builtin commands or commands found by searching the **PATH** are executed. If there is a shell function named *ls*, running ```command ls``` within the function will execute the external command *ls* instead of calling the function recursively. The ```-p``` option means to use a default value for PATH that is guaranteed to find all of the standard utilities. The return status in this case is 127 if command cannot be found or an error occurred, and the exit status of command otherwise.<br><br>If either the ```-V``` or ```-v``` option is supplied, a description of command is printed. The ```-v``` option causes a single word indicating the command or file name used to invoke command to be displayed; the ```-V``` option produces a more verbose description. In this case, the return status is zero if command is found, and non-zero if not. |
| ```declare``` | Format:<br>```declare [-aAfFgilnrtux] [-p] [name[=value] ...]```<br><br>Declare variables and give them attributes. If no names are given, then display the values of variables instead. |
| ```echo```    | Format:<br>```echo [-neE] [arg ...]```<br><br>Output the args, separated by spaces, terminated with a newline.<br><br>The return status is 0 unless a write error occurs.<br><br>If ```-n``` is specified, the trailing newline is suppressed.<br>If the ```-e``` option is given, interpretation of the backslash-escaped characters is enabled.<br>The ```-E``` option disables the interpretation of these escape characters, even on systems where they are interpreted by default.<br><br>The ```xpg_echo``` shell option may be used to dynamically determine whether or not echo expands these escape characters by default. echo does not interpret ```--``` to mean the end of options. |
| ```enable```  | Format:<br>```enable [-a] [-dnps] [-f filename] [name ...]```<br><br>Enable and disable builtin shell commands. Disabling a builtin allows a disk command which has the same name as a shell builtin to be executed without specifying a full pathname, even though the shell normally searches for builtins before disk commands.<br><br>If ```-n``` is used, the names become disabled. Otherwise names are enabled.<br><br>If the ```-p``` option is supplied, or no name arguments appear, a list of shell builtins is printed. With no other arguments, the list consists of all enabled shell builtins. The ```-a``` option means to list each builtin with an indication of whether or not it is enabled.<br><br>The return status is zero unless a name is not a shell builtin or there is an error loading a new builtin from a shared object. |
| ```help```    | Format:<br>```help [-dms] [pattern]```<br><br>Display helpful information about builtin commands. If *pattern* is specified, *help* gives detailed help on all commands matching pattern, otherwise a list of the builtins is printed.<br><br>The return status is zero unless no command matches pattern. |
| ```let```     | Format:<br>```let expression [expression ...]```<br><br>The *let* builtin allows arithmetic to be performed on shell variables. Each expression is evaluated according to the rules given [Shell Arithmetic](). If the last *expression* evaluates to 0, let returns 1; otherwise 0 is returned. |
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

# Invoking Bash

Formats:
```bash [long-opt] [-ir] [-abefhkmnptuvxdBCDHP] [-o option] [-O shopt_option] [argument ...]```
```bash [long-opt] -s [-abefhkmnptuvxdBCDHP] [-o option] [-O shopt_option] [argument ...]```
```bash [long-opt] [-abefhkmnptuvxdBCDHP] [-o option] [-O shopt_option] -c string [argument ...]```

All of the single-character options used with the *set* builtin can be used as options when the shell is invoked.

These options must appear on the command line before the single-character options to be recognized:

| long_opt | Description |
| :---------- | :---------- |
| ```--debugger``` | Arrange for the debugger profile to be executed before the shell starts. Turns on extended debugging mode (see the *shopt* builtin for a description of the *extdebug* option). |
| ```--dump-po-strings``` | A list of all double-quoted strings preceded by **$** is printed on the standard output in the GNU *gettext* PO (portable object) file format. Equivalent to ```-D``` except for the output format. |
| ```--dump-strings``` | Equivalent to ```-D```. |
| ```--init-file filename```<br>```--rcfile filename``` | Execute commands from *filename* (instead of ```~/.bashrc```) in an interactive shell. |
| ```--login``` | Equivalent to ```-l```. |
| ```--noprofile``` | Don't load the system-wide startup file ```/etc/profile``` or any of the personal initialization files ```~/.bash_profile```, ```~/.bash_login```, or ```~/.profile``` when Bash is invoked as a **login shell**. |
| ```--noediting``` | Do not use the GNU Readline library to read command lines when the shell is **interactive**. |
| ```--norc``` | Don't read the ```~/.bashrc``` initialization file in an **interactive shell**. ***This is on by default if the shell is invoked as*** ```sh```. |
| ```--posix``` | Change the behavior of Bash where the default operation differs from the POSIX standard to match the standard. This is intended to make Bash behave as a strict superset of that standard. Refer to [Bash POSIX Mode](https://www.gnu.org/software/bash/manual/bash.html#Bash-POSIX-Mode). |
| ```--restricted``` | Make the shell a **restricted shell**. Refer to [The Restricted Shell](https://www.gnu.org/software/bash/manual/bash.html#The-Restricted-Shell). |
| ```--verbose``` | Equivalent to ```-v```. Print shell input lines as they're read. |
| ```--version``` | Show version information for this instance of Bash on the standard output and exit successfully. |
| ```--help``` | Display a usage message on standard output and exit successfully.<br><br>Type ```bash -c "help set"``` for more information about shell options.<br>Type ```bash -c help``` for more information about shell builtin commands. |

<p/>

There are several single-character options that may be supplied at invocation which are not available with the *set* builtin.

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

If arguments remain after option processing, and neither the ```-c``` nor the ```-s``` option has been supplied, the first argument is assumed to be the name of a file containing shell commands. When Bash is invoked in this fashion, **$0** is set to the name of the file, and the positional parameters are set to the remaining arguments. Bash reads and executes commands from this file, then exits. Bash's exit status is the exit status of the last command executed in the script. If no commands are executed, the exit status is 0.

# Shell Functions

Definition of shell functions:

```
func-name ()
    compound-command [ redirections ]
    ...

func-name ()
{
    compound-command [ redirections ]
    ...
}
```

```
function func-name [()]
    compound-command [ redirections ]
    ...

function func-name [()]
{
    compound-command [ redirections ]
    ...
}
```

Invoking of shell functions:

```
func-name "param1" "param2" ...
```

A function definition may be deleted using the ```-f``` option to the ```unset``` builtin.

The exit status of a function definition is zero unless a syntax error occurs or a readonly function with the same name already exists. When executed, the exit status of a function is the exit status of the last command executed in the body.

The special parameter ***#*** that expands to the number of positional parameters is updated to reflect the change. Special parameter 0 is unchanged.

The first element of the FUNCNAME variable is set to the name of the function while the function is executing.

Variables local to the function may be declared with the ```local``` builtin. These variables are visible only to the function and the commands it invokes.

# References

[Bash Reference Manual](https://www.gnu.org/software/bash/manual/)
