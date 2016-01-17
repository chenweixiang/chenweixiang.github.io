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
2. Breaks the input into **words** and **operators**, obeying the [quoting rules](#quoting). These tokens are separated by [metacharacters](#definitions). [Alias expansion](#aliases) is performed by this step.
3. Parses the tokens into [simple commands](#simple-commands) and [compound commands](#compound-commands).
4. Performs the various [shell expansions](#shell-expansions), breaking the expanded tokens into lists of [filenames](#filename-expansion), commands and arguments.
5. Performs any necessary **redirections** and removes the redirection operators and their operands from the argument list.
6. Executes the command.
7. Optionally waits for the command to complete and collects its **exit status**.

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

A non-quoted backslash (```\```) is the Bash escape character. It preserves the literal value of the next character that follows, with the exception of *newline*. If a ```\newline``` pair appears, and the backslash itself is not quoted, the ```\newline``` is treated as a **line continuation**, that's, it is removed from the input stream and effectively ignored.

***Single Quotes*** (```'```)

Enclosing characters in single quotes (```'```) preserves the literal value of each character within the quotes.

A single quote may not occur between single quotes, even when preceded by a backslash.

***Double Quotes*** (```"```)

Enclosing characters in double quotes (```"```) preserves the literal value of all characters within the quotes, with the exception of ```$```, ```` ` ````, ```\```, and, when history expansion is enabled, ```!```.

A double quote may be quoted within double quotes by preceding it with a backslash.

| Characters | Description |
| :--------- | :---------- |
| ```$```    | A double-quoted string preceded by a dollar sign (```$```) will cause the string to be translated according to the current locale. If the current locale is *C* or *POSIX*, the dollar sign is ignored. If the string is translated and replaced, the replacement is double-quoted. |
| ```\```    | The backslash retains its special meaning only when followed by one of the following characters: ```$``` ``` ` ``` ```"``` ```\``` or *newline*. Within double quotes, backslashes that are followed by one of these characters are removed. Backslashes preceding characters without a special meaning are left unmodified. |
| ```!```    | If enabled, *history expansion* will be performed unless an ```!``` appearing in double quotes is escaped using a backslash. The backslash preceding the ```!``` is not removed. |
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

| --------Formats-------- | Parameter_expansions | Note |
| :-------| :------------------- | :--- |
| ```echo ${@:7}``` | 7 8 9 0 a b c d e f g h | |
| ```echo ${@:7:2}``` | 7 8 | |
| ```echo ${@:7:-2}``` | bash: -2: substring expression < 0 | |
| ```echo ${@: -1}``` | h | A negative *offset* is taken relative to one greater than the greatest positional parameter, so an offset of *-1* evaluates to the last positional parameter. |
| ```echo ${@: -7}``` | b c d e f g h | |
| ```echo ${@: -7:2}``` | b c | |
| ```echo ${@:0}``` | bash 1 2 3 4 5 6 7 8 9 0 a b c d e f g h | |
| ```echo ${@:0:2}``` | bash 1 | |

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

| ----------Formats---------- | Parameter_expansions | Note |
| :-------| :------------------- | :--- |
| ```echo $(ls -l *ml)``` | -rw-rw-r-- 1 chenwx chenwx 1299 Dec 9 22:04 _config.yml -rw-r--r-- 1 chenwx chenwx 1439 Nov 28 15:35 feed.xml -rw-rw-r-- 1 chenwx chenwx 54 Dec 1 07:30 index.html | |
| ```echo `ls -l *ml```` | -rw-rw-r-- 1 chenwx chenwx 1299 Dec 9 22:04 _config.yml -rw-r--r-- 1 chenwx chenwx 1439 Nov 28 15:35 feed.xml -rw-rw-r-- 1 chenwx chenwx 54 Dec 1 07:30 index.html | |

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
