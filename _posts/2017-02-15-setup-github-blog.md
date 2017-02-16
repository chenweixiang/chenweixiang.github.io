---
layout: post
title:  "Setup GitHub Blog"
tag: Tools
toc: true
---

This article introduces how to setup Github blogs on Linux and Markdown syntax.

<!--more-->

# Install Packages

## Install Jekyll on Linux

1) Install RVM

Ruby Version Manager (RVM) is a command-line tool which allows you to easily install, manage, and work with multiple ruby environments from interpreters to sets of gems. Refer to [RVM](https://rvm.io/) and [Quick Guide of installing RVM](https://rvm.io/rvm/install).

```
$ gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
$ curl -sL https://deb.nodesource.com/setup | sudo bash -
```

2) Install ruby-dev

Ruby is a dynamic, open source programming language with a focus on simplicity and productivity. It has an elegant syntax that is natural to read and easy to write. Refer to [Ruby](https://www.ruby-lang.org/en/).

```
~ $ sudo apt-get install ruby-dev
```

3) Install Node.js

Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine. Node.js uses an event-driven, non-blocking I/O model that makes it lightweight and efficient. Node.js' package ecosystem, npm, is the largest ecosystem of open source libraries in the world. Refer to [Node.js](https://nodejs.org/).

```
~ $ curl -sL https://deb.nodesource.com/setup | sudo bash -
~ $ sudo apt-get install -y nodejs
```

4) Install Jekyll

Jekyll is a simple, blog-aware, static site generator. It takes a template directory containing raw text files in various formats, runs it through a converter (like Markdown) and our Liquid renderer, and spits out a complete, ready-to-publish static website suitable for serving with your favorite web server. Jekyll also happens to be the engine behind GitHub Pages, which means you can use Jekyll to host your project’s page, blog, or website from GitHub’s servers for free. Refer to [Jekyll](http://jekyllrb.com/).

```
~ $ sudo gem install jekyll
```

5) Upgrade Jekyll

```
chenwx@chenwx ~/work/blog $ jekyll -v
jekyll 3.0.1

chenwx@chenwx ~/work/blog $ gem update jekyll
Updating installed gems
Updating jekyll
Fetching: public_suffix-2.0.5.gem (100%)
Successfully installed public_suffix-2.0.5
Fetching: addressable-2.5.0.gem (100%)
Successfully installed addressable-2.5.0
Fetching: colorator-1.1.0.gem (100%)
Successfully installed colorator-1.1.0
Fetching: forwardable-extended-2.6.0.gem (100%)
Successfully installed forwardable-extended-2.6.0
Fetching: pathutil-0.14.0.gem (100%)
Successfully installed pathutil-0.14.0
Fetching: jekyll-3.3.1.gem (100%)
Successfully installed jekyll-3.3.1
Parsing documentation for public_suffix-2.0.5
Installing ri documentation for public_suffix-2.0.5
Installing darkfish documentation for public_suffix-2.0.5
Parsing documentation for addressable-2.5.0
Installing ri documentation for addressable-2.5.0
Installing darkfish documentation for addressable-2.5.0
Parsing documentation for colorator-1.1.0
Installing ri documentation for colorator-1.1.0
Installing darkfish documentation for colorator-1.1.0
Parsing documentation for forwardable-extended-2.6.0
Installing ri documentation for forwardable-extended-2.6.0
Installing darkfish documentation for forwardable-extended-2.6.0
Parsing documentation for pathutil-0.14.0
Installing ri documentation for pathutil-0.14.0
Installing darkfish documentation for pathutil-0.14.0
Parsing documentation for jekyll-3.3.1
Installing ri documentation for jekyll-3.3.1
Installing darkfish documentation for jekyll-3.3.1
Done installing documentation for public_suffix, addressable, colorator, forwardable-extended, pathutil, jekyll after 8 seconds
Parsing documentation for addressable-2.5.0
Parsing documentation for colorator-1.1.0
Parsing documentation for forwardable-extended-2.6.0
Parsing documentation for jekyll-3.3.1
Parsing documentation for pathutil-0.14.0
Parsing documentation for public_suffix-2.0.5
Done installing documentation for addressable, colorator, forwardable-extended, jekyll, pathutil, public_suffix after 4 seconds
Gems updated: addressable colorator forwardable-extended jekyll pathutil public_suffix

chenwx@chenwx ~/work/blog $ jekyll -v
jekyll 3.3.1
```

## Setup Blog Directory

Create local directory for blogs:

```
~ $ jekyll new blogs
~ $ cd blogs/
~/blogs $ jekyll serve    # => Now browse to http://localhost:4000
```

Refer to [Jekyll Directory Structure](http://jekyllrb.com/docs/structure/).

# Markdown Syntax

Refer to the following sites for Markdown syntex:

* [Markdown Syntax](http://www.markdown.cn)
* [Markdown on DaringFireball](http://daringfireball.net/projects/markdown/)

![Mindmap of Markdown Syntax](/assets/Markdown_Syntax.png)

# References

* [RVM](https://rvm.io/)
* [Quick Guide of installing RVM](https://rvm.io/rvm/install)
* [Ruby](https://www.ruby-lang.org/en/)
* [Node.js](https://nodejs.org/)
* [Markdown](http://www.markdown.cn)

* [Atom](https://atom.io)
* [Atom on GitHub](https://github.com/atom/atom)

* [MarkdownPad for Windowns](http://markdownpad.com)
* [MarkPad for Windowns](http://code52.org/DownmarkerWPF)
* [ReText (for Linux)](http://sourceforge.net/p/retext/home/ReText)
* [Markable.in](http://markable.in)
* [Dillinger.io](http://dillinger.io)
