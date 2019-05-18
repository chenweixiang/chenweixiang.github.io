---
layout: post
title:  "Scientific Computing"
tag: Programming
toc: true
---

This article introduces the scientific computing software, including [Scilab](#scilab), [SciPy](#scipy) and etc.

<!--more-->

# Overview

According to [Scientific Computing](https://en.wikiversity.org/wiki/Scientific_computing):

Scientific computing is the science of solving problems with computers. The problems themselves usually arise from other disciplines such as mathematics, engineering, biology, physics, chemistry and other natural sciences. As a consequence, scientific computing is interdisciplinary by nature. The dividing line between scientific computing and the sciences from which its problems originate is best described by what scientific computing is *not* -- and what it *is*.

* Computing PI to 22.4 trillion digits is *not* scientific computing. Developing algorithms to efficiently compute PI to any precision *is* scientific computing.
* Running a Molecular dynamics simulation with 1,000,000 atoms for 100 nanoseconds is *not* scientific computing. Developing models and algorithms to efficiently simulate large particle systems *is* scientific computing.
* Computing the eigenvalues of a 1,000 x 1,000 dense, complex matrix is *not* scientific computing. Developing efficient and accurate methods to determine the eigevalues of any large, dense, complex matrix *is* scientific computing.
* Running an all-against-all sequence alignment of every genome known is *not* scientific computing. Developing realistic and efficient models for sequence evolution *is* scientific computing.

The line between scientific computing and the sciences from which its problems are derived is drawn between interest in the *methods* used to solve problems and the *solution* of the problems themselves. In other words, all scientists use computers, but very few do scientific computation.

# MATLAB

Millions of engineers and scientists worldwide use [MATLAB](https://ww2.mathworks.cn/en/products/matlab.html) to analyze and design the systems and products transforming our world. The matrix-based MATLAB language is the world’s most natural way to express computational mathematics. Built-in graphics make it easy to visualize and gain insights from data. The desktop environment invites experimentation, exploration, and discovery. These MATLAB tools and capabilities are all rigorously tested and designed to work together.

MATLAB helps you take your ideas beyond the desktop. You can run your analyses on larger data sets, and scale up to clusters and clouds. MATLAB code can be integrated with other languages, enabling you to deploy algorithms and applications within web, enterprise, and production systems.

* [MATLAB Documentation](https://ww2.mathworks.cn/help/matlab/index.html)

# Mathematica

[Wolfram Mathematica](https://www.wolfram.com/mathematica/) is a modern technical computing system spanning most areas of technical computing - including neural networks, machine learning, image processing, geometry, data science, visualizations, and others. The system is used in many technical, scientific, engineering, mathematical, and computing fields. It was conceived by *Stephen Wolfram* and is developed by Wolfram Research of Champaign, Illinois. The Wolfram Language is the programming language used in Mathematica.[9]

# FreeMat

[FreeMat](http://freemat.sourceforge.net/) is a free environment for rapid engineering and scientific prototyping and data processing. It is similar to commercial systems such as MATLAB from Mathworks, and IDL from Research Systems, but is Open Source. FreeMat is available under the GPL license.

# Scilab

[Scilab](https://www.scilab.org/) is a free and open source software for engineers & scientists, with a long history (first release in 1994) and a growing community (100 000 downloads every months worldwide).

* [Scilab Tutorials](https://www.scilab.org/tutorials)
* [From Matlab to Scilab](https://wiki.scilab.org/MatlabToScilab)
* [An Introduction to Scilab from a Matlab User's Point of View](/docs/An_Introduction_to_Scilab_from_a_Matlab_User_Point_of_View.pdf)
* [Comparison of SCILAB Syntax and Functions to MATLAB](/docs/Comparison_of_SCILAB_Syntax_and_Functions_to_MATLAB.pdf)

# GNU Octave

[GNU Octave](https://www.gnu.org/software/octave/) is a high-level language primarily intended for numerical computations. It is typically used for such problems as solving linear and nonlinear equations, numerical linear algebra, statistical analysis, and for performing other numerical experiments. It may also be used as a batch-oriented language for automated data processing.

The current version of Octave executes in a graphical user interface (GUI). The GUI hosts an Integrated Development Environment (IDE) which includes a code editor with syntax highlighting, built-in debugger, documentation browser, as well as the interpreter for the language itself. A command-line interface (CLI) for Octave is also available.

GNU Octave is freely redistributable software. You may redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation. The GPL is included in this manual, see Copying.

[This manual](https://octave.org/doc/interpreter/) provides comprehensive documentation on how to install, run, use, and extend GNU Octave. Additional chapters describe how to report bugs and help contribute code.

# Gnuplot

[Gnuplot](http://www.gnuplot.info/) is a portable command-line driven graphing utility for Linux, OS/2, MS Windows, OSX, VMS, and many other platforms. The source code is copyrighted but freely distributed (i.e., you don't have to pay for it). It was originally created to allow scientists and students to visualize mathematical functions and data interactively, but has grown to support many non-interactive uses such as web scripting. It is also used as a plotting engine by third-party applications like Octave. Gnuplot has been supported and under active development since 1986.

# SciPy

[SciPy](https://www.scipy.org/) is a free and open-source Python library used for scientific computing and technical computing.

SciPy contains modules for optimization, linear algebra, integration, interpolation, special functions, FFT, signal and image processing, ODE solvers and other tasks common in science and engineering.

SciPy builds on the [NumPy](http://www.numpy.org/) array object and is part of the NumPy stack which includes tools like [Matplotlib](https://matplotlib.org/), [pandas](http://pandas.pydata.org/) and [SymPy](https://www.sympy.org/en/index.html), and an expanding set of scientific computing libraries. This NumPy stack has similar users to other applications such as MATLAB, GNU Octave, and Scilab. The NumPy stack is also sometimes referred to as the SciPy stack.

SciPy is also a family of conferences for users and developers of these tools: SciPy (in the United States), EuroSciPy (in Europe) and SciPy.in (in India). Enthought originated the SciPy conference in the United States and continues to sponsor many of the international conferences as well as host the SciPy website.

The SciPy library is currently distributed under the BSD license, and its development is sponsored and supported by an open community of developers. It is also supported by NumFOCUS, a community foundation for supporting reproducible and accessible science.

* [SciPy Home Page](https://www.scipy.org/)
* [Scipy Documentation](https://scipy.org/docs.html)
* [Numpy and Scipy Documentation](https://docs.scipy.org/doc/)
* [SciPy Cookbook](https://scipy-cookbook.readthedocs.io/)
* [Scipy library main repository](https://github.com/scipy/scipy/)
* [Code of Conduct](https://scipy.github.io/devdocs/dev/conduct/code_of_conduct.html)

## Install SciPy via pip

Refer to <a href="{{ site.base-url }}/2017/03/09/python.html#install-pip">Install pip</a> to know how to install pip.

Then, install package **setuptools**, **tkinter** and **wheel** in Python 3.x, which is used when installing SciPy packages later:

```
chenwx@chenwx:~ $ sudo apt-get install python3-setuptools
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Suggested packages:
  python-setuptools-doc
The following NEW packages will be installed:
  python3-setuptools
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 248 kB of archives.
After this operation, 1319 kB of additional disk space will be used.
Get:1 http://mirrors.aliyun.com/ubuntu bionic/main amd64 python3-setuptools all 39.0.1-2 [248 kB]
Fetched 248 kB in 1s (184 kB/s)        
Selecting previously unselected package python3-setuptools.
(Reading database ... 295047 files and directories currently installed.)
Preparing to unpack .../python3-setuptools_39.0.1-2_all.deb ...
Unpacking python3-setuptools (39.0.1-2) ...
Setting up python3-setuptools (39.0.1-2) ...

chenwx@chenwx:~/repo/blog $ sudo apt-get install python3-tk
[sudo] password for chenwx:       
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following package was automatically installed and is no longer required:
  python-pkg-resources
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  blt libtcl8.6 libtk8.6 tk8.6-blt2.5
Suggested packages:
  blt-demo tcl8.6 tk8.6 tix python3-tk-dbg
The following NEW packages will be installed:
  blt libtcl8.6 libtk8.6 python3-tk tk8.6-blt2.5
0 upgraded, 5 newly installed, 0 to remove and 0 not upgraded.
Need to get 2252 kB of archives.
After this operation, 9233 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://mirror.nforce.com/pub/linux/ubuntu bionic/main amd64 libtcl8.6 amd64 8.6.8+dfsg-3 [881 kB]
Get:2 http://mirror.nforce.com/pub/linux/ubuntu bionic/main amd64 libtk8.6 amd64 8.6.8-4 [693 kB]
Get:3 http://mirror.nforce.com/pub/linux/ubuntu bionic/main amd64 tk8.6-blt2.5 amd64 2.5.3+dfsg-4 [572 kB]
Get:4 http://mirror.nforce.com/pub/linux/ubuntu bionic/main amd64 blt amd64 2.5.3+dfsg-4 [4944 B]
Get:5 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/main amd64 python3-tk amd64 3.6.7-1~18.04 [100 kB]
Fetched 2252 kB in 2s (1270 kB/s)
Selecting previously unselected package libtcl8.6:amd64.
(Reading database ... 295073 files and directories currently installed.)
Preparing to unpack .../libtcl8.6_8.6.8+dfsg-3_amd64.deb ...
Unpacking libtcl8.6:amd64 (8.6.8+dfsg-3) ...
Selecting previously unselected package libtk8.6:amd64.
Preparing to unpack .../libtk8.6_8.6.8-4_amd64.deb ...
Unpacking libtk8.6:amd64 (8.6.8-4) ...
Selecting previously unselected package tk8.6-blt2.5.
Preparing to unpack .../tk8.6-blt2.5_2.5.3+dfsg-4_amd64.deb ...
Unpacking tk8.6-blt2.5 (2.5.3+dfsg-4) ...
Selecting previously unselected package blt.
Preparing to unpack .../blt_2.5.3+dfsg-4_amd64.deb ...
Unpacking blt (2.5.3+dfsg-4) ...
Selecting previously unselected package python3-tk:amd64.
Preparing to unpack .../python3-tk_3.6.7-1~18.04_amd64.deb ...
Unpacking python3-tk:amd64 (3.6.7-1~18.04) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...
Setting up libtcl8.6:amd64 (8.6.8+dfsg-3) ...
Setting up libtk8.6:amd64 (8.6.8-4) ...
Setting up tk8.6-blt2.5 (2.5.3+dfsg-4) ...
Setting up blt (2.5.3+dfsg-4) ...
Setting up python3-tk:amd64 (3.6.7-1~18.04) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...

chenwx@chenwx:~/repo/blog $ python3 -m pip install wheel
Collecting wheel
  Downloading https://files.pythonhosted.org/packages/bb/10/44230dd6bf3563b8f227dbf344c908d412ad2ff48066476672f3a72e174e/wheel-0.33.4-py2.py3-none-any.whl
Installing collected packages: wheel
Successfully installed wheel-0.33.4
```

Now, it's time to install SciPy via pip in Python 3.x, refer to [Install SciPy Packages](https://www.scipy.org/install.html):

```
chenwx@chenwx:~ $ python3 -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
...

chenwx@chenwx:~ $ python3 -m pip show numpy scipy matplotlib ipython jupyter pandas sympy nose
Name: numpy
Version: 1.16.3
Summary: NumPy is the fundamental package for array computing with Python.
Home-page: https://www.numpy.org
Author: Travis E. Oliphant et al.
Author-email: None
License: BSD
Location: /home/chenwx/.local/lib/python3.6/site-packages
Requires:
---
Name: scipy
Version: 1.3.0
Summary: SciPy: Scientific Library for Python
Home-page: https://www.scipy.org
Author: None
Author-email: None
License: BSD
Location: /home/chenwx/.local/lib/python3.6/site-packages
Requires: numpy
---
Name: matplotlib
Version: 3.0.3
Summary: Python plotting package
Home-page: http://matplotlib.org
Author: John D. Hunter, Michael Droettboom
Author-email: matplotlib-users@python.org
License: PSF
Location: /home/chenwx/.local/lib/python3.6/site-packages
Requires: python-dateutil, kiwisolver, cycler, pyparsing, numpy
---
Name: ipython
Version: 7.5.0
Summary: IPython: Productive Interactive Computing
Home-page: https://ipython.org
Author: The IPython Development Team
Author-email: ipython-dev@python.org
License: BSD
Location: /home/chenwx/.local/lib/python3.6/site-packages
Requires: prompt-toolkit, traitlets, backcall, pygments, jedi, pickleshare, decorator, setuptools, pexpect
---
Name: jupyter
Version: 1.0.0
Summary: Jupyter metapackage. Install all the Jupyter components in one go.
Home-page: http://jupyter.org
Author: Jupyter Development Team
Author-email: jupyter@googlegroups.org
License: BSD
Location: /home/chenwx/.local/lib/python3.6/site-packages
Requires: qtconsole, jupyter-console, ipywidgets, notebook, nbconvert, ipykernel
---
Name: pandas
Version: 0.24.2
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /home/chenwx/.local/lib/python3.6/site-packages
Requires: numpy, python-dateutil, pytz
---
Name: sympy
Version: 1.4
Summary: Computer algebra system (CAS) in Python
Home-page: https://sympy.org
Author: SymPy development team
Author-email: sympy@googlegroups.com
License: BSD
Location: /home/chenwx/.local/lib/python3.6/site-packages
Requires: mpmath
---
Name: nose
Version: 1.3.7
Summary: nose extends unittest to make testing easier
Home-page: http://readthedocs.org/docs/nose/
Author: Jason Pellerin
Author-email: jpellerin+nose@gmail.com
License: GNU LGPL
Location: /home/chenwx/.local/lib/python3.6/site-packages
Requires:
```

It's recommended to use an user install, using the ```--user``` flag to pip (note: do not use sudo pip, which can cause problems). This installs packages for your local user, and does not write to the system directories.

## Signal Processing via SciPy

* [Signal Processing (scipy.signal)](https://docs.scipy.org/doc/scipy/reference/signal.html)
* [Signal Processing via SciPy](https://scipy-cookbook.readthedocs.io/items/idx_signal_processing.html)

# Gmsh

[Gmsh](http://gmsh.info/) is a free 3D finite element mesh generator with a built-in CAD engine and post-processor. Its design goal is to provide a fast, light and user-friendly meshing tool with parametric input and advanced visualization capabilities. Gmsh is built around four modules: geometry, mesh, solver and post-processing. The specification of any input to these modules is done either interactively using the graphical user interface, in ASCII text files using Gmsh's own scripting language (.geo files), or using the C++, C, Python or Julia API.

# Rebol

[Rebol](http://www.rebol.com/) is a lightweight programming language. Rebol's unique design makes it more productive than other language technologies. The leverage comes from Rebol's unique blend of domain specific sub-languages called dialects.

# References

* [MATLAB](https://ww2.mathworks.cn/en/products/matlab.html)
* [Mathematica](https://www.wolfram.com/mathematica/)
* [Scilab](https://www.scilab.org/)
* [FreeMat](http://freemat.sourceforge.net/)
* [GNU Octave](https://www.gnu.org/software/octave/)
* [Gnuplot](http://www.gnuplot.info/)
* [SciPy](https://www.scipy.org/)
* [Gmsh](http://gmsh.info/)
* [Rebol](http://www.rebol.com/)

* [List of numerical-analysis software](https://en.wikipedia.org/wiki/List_of_numerical-analysis_software)
* [Comparison of numerical-analysis software](https://en.wikipedia.org/wiki/Comparison_of_numerical-analysis_software)
* [Comparison of statistical packages](https://en.wikipedia.org/wiki/Comparison_of_statistical_packages)
