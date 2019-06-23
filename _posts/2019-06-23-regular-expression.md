---
layout: post
title:  "Regular Expression"
tag: Linux
toc: true
---

This article introduces the regular expression.

<!--more-->

# Overview

According to [Regular Expression on Wikipedia](https://en.wikipedia.org/wiki/Regular_expression):

A **regular expression**, **regex** or **regexp** (sometimes called a **rational expression**) is a sequence of characters that define a *search pattern*. Usually such patterns are used by string searching algorithms for *find* or *find and replace* operations on strings, or for input validation. It is a technique developed in theoretical computer science and formal language theory.

The concept arose in the 1950s when the American mathematician *Stephen Cole Kleene* formalized the description of a [regular language](https://en.wikipedia.org/wiki/Regular_language). The concept came into common use with Unix text-processing utilities. Since the 1980s, different syntaxes for writing regular expressions exist, one being the **POSIX standard** and another, widely used, being the **Perl syntax**.

Regular expressions are used in search engines, search and replace dialogs of word processors and text editors, in text processing utilities such as <a href="{{ site.base-url }}/2015/12/02/gnu-sed.html">sed</a> and <a href="{{ site.base-url }}/2016/06/13/gnu-awk.html">AWK</a> and in lexical analysis. Many programming languages provide regex capabilities either built-in or via libraries.

# Standards

The IEEE POSIX standard has three sets of compliance:

* **BRE** (Basic Regular Expressions)
* **ERE** (Extended Regular Expressions)
* **SRE** (Simple Regular Expressions)

SRE is deprecated, in favor of BRE, as both provide backward compatibility.

BRE and ERE work together. ERE adds ```?```, ```+```, and ```|```, and it removes the need to escape the metacharacters ```( )``` and ```{ }```, which are required in BRE. Furthermore, as long as the POSIX standard syntax for regexes is adhered to, there can be, and often is, additional syntax to serve specific (yet POSIX compliant) applications. Although POSIX.2 leaves some implementation specifics undefined, BRE and ERE provide a *standard* which has since been adopted as the default syntax of many tools, where the choice of BRE or ERE modes is usually a supported option. For example, GNU grep has the following options: ```grep -E``` for ERE, and ```grep -G``` for BRE (the default), and ```grep -P``` for Perl regexes.

Perl regexes have become a de facto standard, having a rich and powerful set of atomic expressions. Perl has no *basic* or *extended* levels. As in POSIX EREs, ```( )``` and ```{ }``` are treated as metacharacters unless escaped; other metacharacters are known to be literal or symbolic based on context alone. Additional functionality includes *lazy matching*, *backtracking*, *named capture groups*, and *recursive patterns*.

## POSIX BRE

In the POSIX standard, Basic Regular Syntax (**BRE**) requires that the metacharacters ```( )``` and ```{ }``` be designated ```\( \)``` and ```\{ \}```, whereas Extended Regular Syntax (**ERE**) does not.

| Metacharacter | Description |
| :-----------: | :---------- |
| ```^```       | Matches the starting position within the string. In line-based tools, it matches the starting position of any line. |
| ```.```       | Matches any single character (many applications exclude newlines, and exactly which characters are considered newlines is flavor-, character-encoding-, and platform-specific, but it is safe to assume that the line feed character is included). Within POSIX bracket expressions, the dot character matches a literal dot. For example, ```a.c``` matches ```abc```, etc., but ```[a.c]``` matches only ```a```, ```.```, or ```c```. |
| ```[ ]```      | A bracket expression. Matches a single character that is contained within the brackets. For example, ```[abc]``` matches ```a```, ```b```, or ```c```. ```[a-z]``` specifies a range which matches any lowercase letter from ```a``` to ```z```. These forms can be mixed: ```[abcx-z]``` matches ```a```, ```b```, ```c```, ```x```, ```y```, or ```z```, as does ```[a-cx-z]```. The ```-``` character is treated as a literal character if it is the last or the first (after the ```^```, if present) character within the brackets: ```[abc-]```, ```[-abc]```. Note that backslash escapes are not allowed. The ```]``` character can be included in a bracket expression if it is the first (after the ```^```) character: ```[]abc]```. |
| ```[^ ]```    | Matches a single character that is not contained within the brackets. For example, ```[^abc]``` matches any character other than ```a```, ```b```, or ```c```. ```[^a-z]``` matches any single character that is not a lowercase letter from ```a``` to ```z```. Likewise, literal characters and ranges can be mixed. |
| ```$```       | Matches the ending position of the string or the position just before a string-ending newline. In line-based tools, it matches the ending position of any line. |
| ```( )```     | Defines a marked subexpression. The string matched within the parentheses can be recalled later (see the next entry, ```\n```). A marked subexpression is also called a block or capturing group. BRE mode requires ```\( \)```. |
| ```\n```      | Matches what the *n*th marked subexpression matched, where *n* is a digit from 1 to 9. This construct is vaguely defined in the POSIX.2 standard. Some tools allow referencing more than nine capturing groups. |
| ```*```       | Matches the preceding element zero or more times. For example, ```ab*c``` matches ```ac```, ```abc```, ```abbbc```, etc. ```[xyz]*``` matches *empty*, ```x```, ```y```, ```z```, ```zx```, ```zyx```, ```xyzzy```, and so on. ```(ab)*``` matches *empty*, ```ab```, ```abab```, ```ababab```, and so on. |
| ```{m,n}```   | Matches the preceding element at least *m* and not more than *n* times. For example, ```a{3,5}``` matches only ```aaa```, ```aaaa```, and ```aaaaa```. This is not found in a few older instances of regexes. BRE mode requires ```\{m,n\}```. |

<p/>

## POSIX ERE

The meaning of metacharacters escaped with a backslash is reversed for some characters in the POSIX Extended Regular Expression (**ERE**) syntax. With this syntax, a backslash causes the metacharacter to be treated as a literal character. So, for example, ```\( \)``` is now ```( )``` and ```\{ \}``` is now ```{ }```. Additionally, support is removed for ```\n``` backreferences and the following metacharacters are added:

| Metacharacter | Description |
| :-----------: | :---------- |
| ```?```       | Matches the preceding element zero or one time. For example, ```ab?c``` matches only ```ac``` or ```abc```. |
| ```+```       | Matches the preceding element one or more times. For example, ```ab+c``` matches ```abc```, ```abbc```, ```abbbc```, and so on, but not ```ac```. |
| ```|```       | The choice (also known as alternation or set union) operator matches either the expression before or the expression after the operator. For example, ```abc|def``` matches ```abc``` or ```def```. |

<p/>

POSIX Extended Regular Expressions (**ERE**) can often be used with modern Unix utilities by including the command line flag ```-E```.

## Perl and PCRE

Because of its expressive power and (relative) ease of reading, many other utilities and programming languages have adopted syntax similar to Perl's — for example, **Java**, **JavaScript**, **Julia**, **Python**, **Ruby**, **Qt**, Microsoft's **.NET Framework**, and **XML Schema**. Some languages and tools such as **Boost** and **PHP** support multiple regex flavors. Perl-derivative regex implementations are not identical and usually implement a subset of features found in Perl 5.0, released in 1994. Perl sometimes does incorporate features initially found in other languages, for example, Perl 5.10 implements syntactic extensions originally developed in **PCRE** (Perl Compatible Regular Expressions) and Python.

# Tutorials

* [RegExr](https://regexr.com/)
* [Regular-Expressions](https://www.regular-expressions.info/)
* [Regular Expression Tutorial on Runoob](http://www.runoob.com/regexp/regexp-syntax.html)

# References

* [Regular Expression on Wikipedia](https://en.wikipedia.org/wiki/Regular_expression)

