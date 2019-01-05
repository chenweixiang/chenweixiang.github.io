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

**Install RVM**

Ruby Version Manager (RVM) is a command-line tool which allows you to easily install, manage, and work with multiple ruby environments from interpreters to sets of gems. Refer to [RVM](https://rvm.io/) and [Quick Guide of installing RVM](https://rvm.io/rvm/install).

```
$ gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
$ curl -sL https://deb.nodesource.com/setup | sudo bash -
```

**Install ruby-dev**

Ruby is a dynamic, open source programming language with a focus on simplicity and productivity. It has an elegant syntax that is natural to read and easy to write. Refer to [Ruby](https://www.ruby-lang.org/en/).

```
~ $ sudo apt-get install ruby-dev
```

**Install Node.js**

Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine. Node.js uses an event-driven, non-blocking I/O model that makes it lightweight and efficient. Node.js' package ecosystem, npm, is the largest ecosystem of open source libraries in the world. Refer to [Node.js](https://nodejs.org/).

```
~ $ curl -sL https://deb.nodesource.com/setup | sudo bash -
~ $ sudo apt-get install -y nodejs
```

**Install Jekyll**

Jekyll is a simple, blog-aware, static site generator. It takes a template directory containing raw text files in various formats, runs it through a converter (like Markdown) and our Liquid renderer, and spits out a complete, ready-to-publish static website suitable for serving with your favorite web server. Jekyll also happens to be the engine behind GitHub Pages, which means you can use Jekyll to host your project’s page, blog, or website from GitHub’s servers for free. Refer to [Jekyll](http://jekyllrb.com/).

```
~ $ sudo gem install jekyll
```

**Upgrade Jekyll**

```
# check current version of jekyll
chenwx@chenwx ~/work/blog $ jekyll -v
jekyll 3.0.1

# display local gems with version
chenwx@chenwx ~/work/blog $ gem list

# upgrade to the latest RubyGems
chenwx@chenwx ~/work/blog $ gem update --system

# display local gems with version after upgrade
chenwx@chenwx ~/work/blog $ gem list

# upgrade to the latest jekyll
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
* [Markdown Cheat Sheet](/docs/Markdown_cheat_sheet.pdf)

![Mindmap of Markdown Syntax](/assets/Markdown_Syntax.png)

# Github Post Structure

The ABOUT page has the following structure:

```
about.md
+-  layout: page
    +-  _layouts/page.html
        +-  layout: default
            +-  _layouts/default.html
```

The Main page has the following structure:

```
index.html
+-  layout: post_by_tag
    +-  _layouts/post_by_tag.html
        +-  layout: default
            +-  _layouts/default.html
```

Each post page has the following structure:

```
_posts/*.md
+-  layout: post
    +-  _layouts/post.html
        +-  layout: default
            +-  _layouts/default.html
        +-  include disqus_comment.html
            +-  _include/disqus_comment.html
```

And the layout has the following structure:

```
_layouts/default.html
+-  include head.html
    +-  <link rel="stylesheet" href="/css/gh-fork-ribbon.min.css">
        ...
    +-  <script src="/js/jquery-2.1.4.min.js"></script>
        ...
+-  include header.html
```

There are three types of CSS configurations:

```
css/main.css
+-  @import
        "base",                 // _sass/_base.scss
        "layout",               // _sass/_layout.scss
        "syntax-highlighting"   // _sass/_syntax-highlighting.scss
    ;
```

# Build GitHub Blogs Locally

Execute the following command to build GitHub blogs locally. In this way, the port number in *Server addess* comes from configuration file ```_config.yml``` if exist, otherwise, use default port number ```4000``` according to [Default Configuration](https://jekyllrb.com/docs/configuration/default/):

```
chenwx@chenwx:~/repo/blog $ jekyll s            
Configuration file: /media/chenwx/Work/repo/blog/_config.yml
            Source: /media/chenwx/Work/repo/blog
       Destination: /media/chenwx/Work/repo/blog/_site
 Incremental build: disabled. Enable with --incremental
      Generating...
                    done in 76.824 seconds.
 Auto-regeneration: enabled for '/media/chenwx/Work/repo/blog'
    Server address: http://127.0.0.1:4004/
  Server running... press ctrl-c to stop.
```

Or, specify the port number in command line by ```--port=<PortNumber>```:

```
henwx@chenwx:~/repo/blog $ jekyll s --port=4004
Configuration file: /media/chenwx/Work/repo/blog/_config.yml
            Source: /media/chenwx/Work/repo/blog
       Destination: /media/chenwx/Work/repo/blog/_site
 Incremental build: disabled. Enable with --incremental
      Generating...
                    done in 85.528 seconds.
 Auto-regeneration: enabled for '/media/chenwx/Work/repo/blog'
    Server address: http://127.0.0.1:4004/
  Server running... press ctrl-c to stop.
```

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

* [Using org to Blog with Jekyll](http://orgmode.org/worg/org-tutorials/org-jekyll.html)
* [Table of Contents plugin for Bootstrap](http://afeld.github.io/bootstrap-toc/)
* [Tocify](http://gregfranko.com/jquery.tocify.js/)
* [TOC](http://projects.jga.me/toc/)
