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

# Scilab

[Scilab](https://www.scilab.org/) is a free and open source software for engineers & scientists, with a long history (first release in 1994) and a growing community (100 000 downloads every months worldwide).

* [Scilab Tutorials](https://www.scilab.org/tutorials)
* [From Matlab to Scilab](https://wiki.scilab.org/MatlabToScilab)
* [An Introduction to Scilab from a Matlab User's Point of View](/docs/An_Introduction_to_Scilab_from_a_Matlab_User_Point_of_View.pdf)
* [Comparison of SCILAB Syntax and Functions to MATLAB](/docs/Comparison_of_SCILAB_Syntax_and_Functions_to_MATLAB.pdf)

## Install Scilab

Install Scilab via Linux package manager:

```
chenwx@chenwx:~ $ sudo apt install scilab
[sudo] password for chenwx:       
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following package was automatically installed and is no longer required:
  python-pkg-resources
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  ant ant-optional antlr bwidget fop java-wrappers javahelp2 junit libactivation-java libaec0 libantlr-java
  libaopalliance-java libapache-pom-java libargs4j-java libarpack2 libatinject-jsr330-api-java
  libavalon-framework-java libbatik-java libbsf-java libcdi-api-java libcodemodel-java libcommons-cli-java
  libcommons-codec-java libcommons-compress-java libcommons-io-java libcommons-lang3-java libcommons-logging-java
  libcommons-parent-java libdom4j-java libdtd-parser-java libecj-java libfastinfoset-java libflexdock-java
  libfontbox-java libfop-java libfreehep-export-java libfreehep-graphics2d-java libfreehep-graphicsio-emf-java
  libfreehep-graphicsio-java libfreehep-graphicsio-tests-java libfreehep-io-java libfreehep-swing-java
  libfreehep-util-java libgeronimo-annotation-1.3-spec-java libgeronimo-interceptor-3.0-spec-java libgluegen2-jni
  libgluegen2-rt-java libguava-java libguice-java libhdf5-100 libhttpclient-java libhttpcore-java
  libistack-commons-java libjas-plotter-java libjaxb-api-java libjaxb-java libjaxen-java libjaxp1.3-java
  libjdom1-java libjeuclid-core-java libjgoodies-common-java libjgoodies-looks-java libjgraphx-java
  libjlatexmath-fop-java libjlatexmath-java libjogl2-java libjogl2-jni libjrosetta-java libjsoup-java libjsr305-java
  liblaf-plugin-java liblucene4.10-java libmatio4 libmaven-file-management-java libmaven-parent-java
  libmaven-resolver-java libmaven-shared-io-java libmaven-shared-utils-java libmaven3-core-java
  libnb-org-openide-util-java libnb-org-openide-util-lookup-java libplexus-archiver-java libplexus-cipher-java
  libplexus-classworlds-java libplexus-component-annotations-java libplexus-interpolation-java libplexus-io-java
  libplexus-sec-dispatcher-java libplexus-utils-java libplexus-utils2-java libregexp-java librelaxng-datatype-java
  librngom-java libsaxon-java libsisu-guice-java libsisu-inject-java libsisu-ioc-java libsisu-plexus-java
  libskinlf-java libslf4j-java libsnappy-java libsnappy-jni libstax-ex-java libstreambuffer-java libsz2
  libtablelayout-java libtxw2-java libwagon-http-java libwagon-provider-api-java libxalan2-java libxerces2-java
  libxml-commons-external-java libxml-commons-resolver1.1-java libxmlgraphics-commons-java libxsom-java libxz-java
  scilab-cli scilab-data scilab-full-bin scilab-include scilab-minimal-bin tcl tcl8.6 tk tk8.6
Suggested packages:
  ant-doc default-jdk | java-compiler | java-sdk javacc junit4 jython libbcel-java libcommons-net-java libmail-java
  libjdepend-java libjsch-java liblog4j1.2-java liboro-java fop-doc javahelp2-doc junit-doc libaopalliance-java-doc
  libatinject-jsr330-api-java-doc libavalon-framework-java-doc librhino-java bsh rhino libcommons-io-java-doc
  libcommons-lang3-java-doc libcommons-logging-java-doc libexcalibur-logkit-java libdom4j-java-doc libmsv-java
  libxpp2-java libxpp3-java libdtd-parser-java-doc ecj libflexdock-java-doc libflexdock-java-demo libgluegen2-doc
  libasm-java libcglib-java libxom-java libjdom1-java-doc libjgoodies-common-java-doc libjlatexmath-java-doc
  libjogl2-java-doc libjsoup-java-doc libjsr305-java-doc liblaf-plugin-java-doc libmaven-file-management-java-doc
  libmaven-shared-io-java-doc libmaven-shared-utils-java-doc liblogback-java libplexus-cipher-java-doc
  libplexus-classworlds-java-doc libplexus-interpolation-java-doc libplexus-sec-dispatcher-java-doc
  libplexus-utils-java-doc libplexus-utils2-java-doc libsaxon-java-doc testng libosgi-compendium-java
  libosgi-core-java libskinlf-java-demo libxalan2-java-doc libxsltc-java libxerces2-java-doc
  libxml-commons-resolver1.1-java-doc libxmlgraphics-commons-java-doc scilab-doc-fr scilab-doc-pt-br scilab-doc-ja
  gfortran scilab-swt scilab-scimax scilab-plotlib scilab-ann tcl-tclreadline
Recommended packages:
  icc-profiles-free libjansi-java libasm-java libcglib-java scilab-doc scilab-sivp
The following NEW packages will be installed:
  ant ant-optional antlr bwidget fop java-wrappers javahelp2 junit libactivation-java libaec0 libantlr-java
  libaopalliance-java libapache-pom-java libargs4j-java libarpack2 libatinject-jsr330-api-java
  libavalon-framework-java libbatik-java libbsf-java libcdi-api-java libcodemodel-java libcommons-cli-java
  libcommons-codec-java libcommons-compress-java libcommons-io-java libcommons-lang3-java libcommons-logging-java
  libcommons-parent-java libdom4j-java libdtd-parser-java libecj-java libfastinfoset-java libflexdock-java
  libfontbox-java libfop-java libfreehep-export-java libfreehep-graphics2d-java libfreehep-graphicsio-emf-java
  libfreehep-graphicsio-java libfreehep-graphicsio-tests-java libfreehep-io-java libfreehep-swing-java
  libfreehep-util-java libgeronimo-annotation-1.3-spec-java libgeronimo-interceptor-3.0-spec-java libgluegen2-jni
  libgluegen2-rt-java libguava-java libguice-java libhdf5-100 libhttpclient-java libhttpcore-java
  libistack-commons-java libjas-plotter-java libjaxb-api-java libjaxb-java libjaxen-java libjaxp1.3-java
  libjdom1-java libjeuclid-core-java libjgoodies-common-java libjgoodies-looks-java libjgraphx-java
  libjlatexmath-fop-java libjlatexmath-java libjogl2-java libjogl2-jni libjrosetta-java libjsoup-java libjsr305-java
  liblaf-plugin-java liblucene4.10-java libmatio4 libmaven-file-management-java libmaven-parent-java
  libmaven-resolver-java libmaven-shared-io-java libmaven-shared-utils-java libmaven3-core-java
  libnb-org-openide-util-java libnb-org-openide-util-lookup-java libplexus-archiver-java libplexus-cipher-java
  libplexus-classworlds-java libplexus-component-annotations-java libplexus-interpolation-java libplexus-io-java
  libplexus-sec-dispatcher-java libplexus-utils-java libplexus-utils2-java libregexp-java librelaxng-datatype-java
  librngom-java libsaxon-java libsisu-guice-java libsisu-inject-java libsisu-ioc-java libsisu-plexus-java
  libskinlf-java libslf4j-java libsnappy-java libsnappy-jni libstax-ex-java libstreambuffer-java libsz2
  libtablelayout-java libtxw2-java libwagon-http-java libwagon-provider-api-java libxalan2-java libxerces2-java
  libxml-commons-external-java libxml-commons-resolver1.1-java libxmlgraphics-commons-java libxsom-java libxz-java
  scilab scilab-cli scilab-data scilab-full-bin scilab-include scilab-minimal-bin tcl tcl8.6 tk tk8.6
0 upgraded, 126 newly installed, 0 to remove and 0 not upgraded.
Need to get 112 MB of archives.
After this operation, 220 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 ant all 1.10.5-3~18.04 [2075 kB]
Get:2 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 ant-optional all 1.10.5-3~18.04 [378 kB]
Get:3 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libantlr-java all 2.7.7+dfsg-9.2 [452 kB]
Get:4 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 antlr all 2.7.7+dfsg-9.2 [5088 B]
Get:5 http://mirror.nforce.com/pub/linux/ubuntu bionic/main amd64 tk8.6 amd64 8.6.8-4 [12.3 kB]
Get:6 http://mirror.nforce.com/pub/linux/ubuntu bionic/main amd64 tcl8.6 amd64 8.6.8+dfsg-3 [14.4 kB]
Get:7 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 tcl amd64 8.6.0+9 [5146 B]
Get:8 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 tk amd64 8.6.0+9 [3178 B]
Get:9 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 bwidget all 1.9.12-1 [175 kB]
Get:10 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 java-wrappers all 0.3 [9560 B]
Get:11 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libavalon-framework-java all 4.2.0-10 [71.3 kB]
Get:12 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libjaxp1.3-java all 1.3.05-5 [226 kB]
Get:13 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libxml-commons-external-java all 1.4.01-3 [240 kB]
Get:14 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libxml-commons-resolver1.1-java all 1.2-9 [91.1 kB]
Get:15 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libxerces2-java all 2.11.0-8 [1344 kB]
Get:16 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libxalan2-java all 2.7.2-1 [3302 kB]
Get:17 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libapache-pom-java all 18-1 [4720 B]
Get:18 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libcommons-parent-java all 43-1 [10.8 kB]
Get:19 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libcommons-io-java all 2.6-2 [198 kB]
Get:20 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libcommons-logging-java all 1.2-2 [60.3 kB]
Get:21 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libxmlgraphics-commons-java all 2.2-1 [616 kB]
Get:22 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libbatik-java all 1.10-2~18.04 [3883 kB]
Get:23 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libbsf-java all 1:2.4.0-5build1 [71.2 kB]
Get:24 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libfontbox-java all 1:1.8.16-2~18.04 [211 kB]
Get:25 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libfop-java all 1:2.1-7 [9454 kB]
Get:26 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 fop all 1:2.1-7 [12.3 kB]
Get:27 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 javahelp2 all 2.0.05.ds1-9 [877 kB]
Get:28 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 junit all 3.8.2-9 [108 kB]
Get:29 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libactivation-java all 1.2.0-1ubuntu1 [84.8 kB]
Get:30 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libaec0 amd64 0.3.2-2 [18.1 kB]
Get:31 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libargs4j-java all 2.33-1 [138 kB]
Get:32 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libarpack2 amd64 3.5.0+real-2 [89.7 kB]
Get:33 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libatinject-jsr330-api-java all 1.0+ds1-5 [5348 B]
Get:34 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libgeronimo-interceptor-3.0-spec-java all 1.0.1-4fakesync [8616 B]
Get:35 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libcdi-api-java all 1.2-2 [54.5 kB]
Get:36 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libjaxen-java all 1.1.6-3 [214 kB]
Get:37 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libdom4j-java all 2.1.0-2 [309 kB]
Get:38 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libmaven-shared-utils-java all 3.3.0-1~18.04 [149 kB]
Get:39 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libcommons-cli-java all 1.4-1 [53.8 kB]
Get:40 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libcommons-lang3-java all 3.8-1~18.04.2 [479 kB]
Get:41 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libgeronimo-annotation-1.3-spec-java all 1.0-1 [10.7 kB]
Get:42 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libaopalliance-java all 20070526-6 [9084 B]
Get:43 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libjsr305-java all 0.1~+svn49-10 [26.5 kB]
Get:44 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libguava-java all 19.0-1 [2028 kB]
Get:45 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libguice-java all 4.0-4 [853 kB]
Get:46 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libmaven-parent-java all 31-2~18.04 [5196 B]
Get:47 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libplexus-utils2-java all 3.0.24-3 [246 kB]
Get:48 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libwagon-provider-api-java all 3.0.0-2 [48.2 kB]
Get:49 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libmaven-resolver-java all 1.3.1-1~18.04 [549 kB]
Get:50 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libplexus-cipher-java all 1.7-3 [15.1 kB]
Get:51 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libplexus-classworlds-java all 2.5.2-2 [49.3 kB]
Get:52 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libplexus-component-annotations-java all 1.7.1-7 [6596 B]
Get:53 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libplexus-interpolation-java all 1.24-1 [73.4 kB]
Get:54 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libplexus-sec-dispatcher-java all 1.4-3 [28.0 kB]
Get:55 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libslf4j-java all 1.7.25-3 [141 kB]
Get:56 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libsisu-inject-java all 0.3.2-2 [346 kB]
Get:57 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libsisu-plexus-java all 0.3.3-3 [182 kB]
Get:58 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libmaven3-core-java all 3.6.0-1~18.04.1 [1465 kB]
Get:59 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libplexus-utils-java all 1:1.5.15-5 [209 kB]
Get:60 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libmaven-shared-io-java all 3.0.0-3 [33.3 kB]
Get:61 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libmaven-file-management-java all 3.0.0-1 [35.1 kB]
Get:62 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libcommons-compress-java all 1.18-1~18.04 [531 kB]
Get:63 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libplexus-io-java all 3.1.1-1~18.04 [64.8 kB]
Get:64 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libsnappy-jni amd64 1.1.4-1 [6996 B]
Get:65 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libsnappy-java all 1.1.4-1 [67.2 kB]
Get:66 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libxz-java all 1.8-1 [134 kB]
Get:67 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libplexus-archiver-java all 3.5-2 [166 kB]
Get:68 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libsisu-guice-java all 4.2.0-1 [785 kB]
Get:69 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libsisu-ioc-java all 2.3.0-11 [492 kB]
Get:70 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libhttpcore-java all 4.4.9-1 [605 kB]
Get:71 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libcommons-codec-java all 1.11-1 [271 kB]
Get:72 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libhttpclient-java all 4.5.5-1 [720 kB]
Get:73 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libjsoup-java all 1.10.2-2 [337 kB]
Get:74 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libwagon-http-java all 3.0.0-2 [45.6 kB]      
Get:75 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libistack-commons-java all 3.0.6-3~18.04 [144 kB]
Get:76 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libcodemodel-java all 2.6+jaxb2.3.0.1-7~18.04 [163 kB]
Get:77 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libdtd-parser-java all 1.2~svn20110404-1 [62.4 kB]
Get:78 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libecj-java all 3.16.0-1~18.04 [1781 kB]
Get:79 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libjaxb-api-java all 2.3.1-1~18.04 [119 kB]
Get:80 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libstax-ex-java all 1.7.8-3~18.04.1 [41.0 kB]
Get:81 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libstreambuffer-java all 1.5.4-1 [71.9 kB]    
Get:82 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 librelaxng-datatype-java all 1.0+ds1-3 [11.7 kB]
Get:83 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libxsom-java all 2.3.0.1-7~18.04 [396 kB]
Get:84 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libfastinfoset-java all 1.2.12-3 [343 kB]     
Get:85 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libflexdock-java all 1.2.4-1 [393 kB]         
Get:86 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libnb-org-openide-util-lookup-java all 10.0-2~18.04.1 [72.6 kB]
Get:87 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libnb-org-openide-util-java all 10.0-2~18.04.1 [159 kB]
Get:88 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libfreehep-util-java all 2.0.2-7 [49.3 kB]    
Get:89 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libfreehep-swing-java all 2.0.3-5 [191 kB]    
Get:90 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libfreehep-export-java all 2.1.1-4 [21.8 kB]  
Get:91 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libfreehep-graphics2d-java all 2.1.1-6 [123 kB]
Get:92 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libfreehep-io-java all 2.0.2-6 [62.4 kB]      
Get:93 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libfreehep-graphicsio-java all 2.1.1-5 [177 kB]
Get:94 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libtablelayout-java all 20090826-4 [20.6 kB]  
Get:95 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libjas-plotter-java all 2.2.6+dfsg1-4 [607 kB]
Get:96 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libfreehep-graphicsio-tests-java all 2.1.1+dfsg1-5 [103 kB]
Get:97 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libjdom1-java all 1.1.3-2~18.04 [156 kB]
Get:98 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libfreehep-graphicsio-emf-java all 2.1.1-emfplus+dfsg1-4 [188 kB]
Get:99 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libgluegen2-jni amd64 2.3.2-7~18.04 [10.4 kB]
Get:100 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libgluegen2-rt-java all 2.3.2-7~18.04 [323 kB]
Get:101 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libsz2 amd64 0.3.2-2 [5114 B]                
Get:102 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libhdf5-100 amd64 1.10.0-patch1+docs-4 [1256 kB]
Get:103 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 librngom-java all 2.3.0.1-7~18.04 [288 kB]
Get:104 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libtxw2-java all 2.3.0.1-7~18.04 [134 kB]
Get:105 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libjaxb-java all 2.3.0.1-7~18.04 [1968 kB]
Get:106 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libjeuclid-core-java all 3.1.9-4 [645 kB]    
Get:107 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libjgoodies-common-java all 1.8.1-2 [35.8 kB]
Get:108 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libjgoodies-looks-java all 2.7.0-3~18.04 [255 kB]
Get:109 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libjgraphx-java all 2.1.0.7-1 [764 kB]       
Get:110 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libjlatexmath-java all 1.0.7-1 [990 kB]      
Get:111 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libjlatexmath-fop-java all 1.0.7-1 [25.2 kB]
Get:112 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libjogl2-jni amd64 2.3.2+dfsg-8~18.04 [151 kB]
Get:113 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 libjogl2-java all 2.3.2+dfsg-8~18.04 [3160 kB]
Get:114 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libjrosetta-java all 1.0.4-4 [56.1 kB]       
Get:115 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libmatio4 amd64 1.5.11-1 [94.2 kB]
Get:116 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libregexp-java all 1.5-4 [36.6 kB]
Get:117 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libsaxon-java all 1:6.5.5-12 [574 kB]
Get:118 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 liblaf-plugin-java all 7.3+dfsg3-4~18.04.1 [28.6 kB]
Get:119 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 libskinlf-java all 6.7-10 [284 kB]
Get:120 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 scilab-data all 6.0.1-7ubuntu1~18.04 [31.2 MB]
Get:121 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 scilab-minimal-bin amd64 6.0.1-7ubuntu1~18.04 [4018 kB]
Get:122 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 scilab-include amd64 6.0.1-7ubuntu1~18.04 [229 kB]
Get:123 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 scilab-cli all 6.0.1-7ubuntu1~18.04 [502 kB]
Get:124 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 liblucene4.10-java all 4.10.4+dfsg-3 [21.1 MB]
Get:125 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 scilab-full-bin amd64 6.0.1-7ubuntu1~18.04 [1983 kB]
Get:126 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/universe amd64 scilab all 6.0.1-7ubuntu1~18.04 [76.6 kB]
Fetched 112 MB in 1min 40s (1120 kB/s)
Extracting templates from packages: 100%
Selecting previously unselected package ant.
(Reading database ... 295476 files and directories currently installed.)
Preparing to unpack .../000-ant_1.10.5-3~18.04_all.deb ...
Unpacking ant (1.10.5-3~18.04) ...
Selecting previously unselected package ant-optional.
Preparing to unpack .../001-ant-optional_1.10.5-3~18.04_all.deb ...
Unpacking ant-optional (1.10.5-3~18.04) ...
Selecting previously unselected package libantlr-java.
Preparing to unpack .../002-libantlr-java_2.7.7+dfsg-9.2_all.deb ...
Unpacking libantlr-java (2.7.7+dfsg-9.2) ...
Selecting previously unselected package antlr.
Preparing to unpack .../003-antlr_2.7.7+dfsg-9.2_all.deb ...
Unpacking antlr (2.7.7+dfsg-9.2) ...
Selecting previously unselected package tk8.6.
Preparing to unpack .../004-tk8.6_8.6.8-4_amd64.deb ...
Unpacking tk8.6 (8.6.8-4) ...
Selecting previously unselected package tcl8.6.
Preparing to unpack .../005-tcl8.6_8.6.8+dfsg-3_amd64.deb ...
Unpacking tcl8.6 (8.6.8+dfsg-3) ...
Selecting previously unselected package tcl.
Preparing to unpack .../006-tcl_8.6.0+9_amd64.deb ...
Unpacking tcl (8.6.0+9) ...
Selecting previously unselected package tk.
Preparing to unpack .../007-tk_8.6.0+9_amd64.deb ...
Unpacking tk (8.6.0+9) ...
Selecting previously unselected package bwidget.
Preparing to unpack .../008-bwidget_1.9.12-1_all.deb ...
Unpacking bwidget (1.9.12-1) ...
Selecting previously unselected package java-wrappers.
Preparing to unpack .../009-java-wrappers_0.3_all.deb ...
Unpacking java-wrappers (0.3) ...
Selecting previously unselected package libavalon-framework-java.
Preparing to unpack .../010-libavalon-framework-java_4.2.0-10_all.deb ...
Unpacking libavalon-framework-java (4.2.0-10) ...
Selecting previously unselected package libjaxp1.3-java.
Preparing to unpack .../011-libjaxp1.3-java_1.3.05-5_all.deb ...
Unpacking libjaxp1.3-java (1.3.05-5) ...
Selecting previously unselected package libxml-commons-external-java.
Preparing to unpack .../012-libxml-commons-external-java_1.4.01-3_all.deb ...
Unpacking libxml-commons-external-java (1.4.01-3) ...
Selecting previously unselected package libxml-commons-resolver1.1-java.
Preparing to unpack .../013-libxml-commons-resolver1.1-java_1.2-9_all.deb ...
Unpacking libxml-commons-resolver1.1-java (1.2-9) ...
Selecting previously unselected package libxerces2-java.
Preparing to unpack .../014-libxerces2-java_2.11.0-8_all.deb ...
Unpacking libxerces2-java (2.11.0-8) ...
Selecting previously unselected package libxalan2-java.
Preparing to unpack .../015-libxalan2-java_2.7.2-1_all.deb ...
Unpacking libxalan2-java (2.7.2-1) ...
Selecting previously unselected package libapache-pom-java.
Preparing to unpack .../016-libapache-pom-java_18-1_all.deb ...
Unpacking libapache-pom-java (18-1) ...
Selecting previously unselected package libcommons-parent-java.
Preparing to unpack .../017-libcommons-parent-java_43-1_all.deb ...
Unpacking libcommons-parent-java (43-1) ...
Selecting previously unselected package libcommons-io-java.
Preparing to unpack .../018-libcommons-io-java_2.6-2_all.deb ...
Unpacking libcommons-io-java (2.6-2) ...
Selecting previously unselected package libcommons-logging-java.
Preparing to unpack .../019-libcommons-logging-java_1.2-2_all.deb ...
Unpacking libcommons-logging-java (1.2-2) ...
Selecting previously unselected package libxmlgraphics-commons-java.
Preparing to unpack .../020-libxmlgraphics-commons-java_2.2-1_all.deb ...
Unpacking libxmlgraphics-commons-java (2.2-1) ...
Selecting previously unselected package libbatik-java.
Preparing to unpack .../021-libbatik-java_1.10-2~18.04_all.deb ...
Unpacking libbatik-java (1.10-2~18.04) ...
Selecting previously unselected package libbsf-java.
Preparing to unpack .../022-libbsf-java_1%3a2.4.0-5build1_all.deb ...
Unpacking libbsf-java (1:2.4.0-5build1) ...
Selecting previously unselected package libfontbox-java.
Preparing to unpack .../023-libfontbox-java_1%3a1.8.16-2~18.04_all.deb ...
Unpacking libfontbox-java (1:1.8.16-2~18.04) ...
Selecting previously unselected package libfop-java.
Preparing to unpack .../024-libfop-java_1%3a2.1-7_all.deb ...
Unpacking libfop-java (1:2.1-7) ...
Selecting previously unselected package fop.
Preparing to unpack .../025-fop_1%3a2.1-7_all.deb ...
Unpacking fop (1:2.1-7) ...
Selecting previously unselected package javahelp2.
Preparing to unpack .../026-javahelp2_2.0.05.ds1-9_all.deb ...
Unpacking javahelp2 (2.0.05.ds1-9) ...
Selecting previously unselected package junit.
Preparing to unpack .../027-junit_3.8.2-9_all.deb ...
Unpacking junit (3.8.2-9) ...
Selecting previously unselected package libactivation-java.
Preparing to unpack .../028-libactivation-java_1.2.0-1ubuntu1_all.deb ...
Unpacking libactivation-java (1.2.0-1ubuntu1) ...
Selecting previously unselected package libaec0:amd64.
Preparing to unpack .../029-libaec0_0.3.2-2_amd64.deb ...
Unpacking libaec0:amd64 (0.3.2-2) ...
Selecting previously unselected package libargs4j-java.
Preparing to unpack .../030-libargs4j-java_2.33-1_all.deb ...
Unpacking libargs4j-java (2.33-1) ...
Selecting previously unselected package libarpack2:amd64.
Preparing to unpack .../031-libarpack2_3.5.0+real-2_amd64.deb ...
Unpacking libarpack2:amd64 (3.5.0+real-2) ...
Selecting previously unselected package libatinject-jsr330-api-java.
Preparing to unpack .../032-libatinject-jsr330-api-java_1.0+ds1-5_all.deb ...
Unpacking libatinject-jsr330-api-java (1.0+ds1-5) ...
Selecting previously unselected package libgeronimo-interceptor-3.0-spec-java.
Preparing to unpack .../033-libgeronimo-interceptor-3.0-spec-java_1.0.1-4fakesync_all.deb ...
Unpacking libgeronimo-interceptor-3.0-spec-java (1.0.1-4fakesync) ...
Selecting previously unselected package libcdi-api-java.
Preparing to unpack .../034-libcdi-api-java_1.2-2_all.deb ...
Unpacking libcdi-api-java (1.2-2) ...
Selecting previously unselected package libjaxen-java.
Preparing to unpack .../035-libjaxen-java_1.1.6-3_all.deb ...
Unpacking libjaxen-java (1.1.6-3) ...
Selecting previously unselected package libdom4j-java.
Preparing to unpack .../036-libdom4j-java_2.1.0-2_all.deb ...
Unpacking libdom4j-java (2.1.0-2) ...
Selecting previously unselected package libmaven-shared-utils-java.
Preparing to unpack .../037-libmaven-shared-utils-java_3.3.0-1~18.04_all.deb ...
Unpacking libmaven-shared-utils-java (3.3.0-1~18.04) ...
Selecting previously unselected package libcommons-cli-java.
Preparing to unpack .../038-libcommons-cli-java_1.4-1_all.deb ...
Unpacking libcommons-cli-java (1.4-1) ...
Selecting previously unselected package libcommons-lang3-java.
Preparing to unpack .../039-libcommons-lang3-java_3.8-1~18.04.2_all.deb ...
Unpacking libcommons-lang3-java (3.8-1~18.04.2) ...
Selecting previously unselected package libgeronimo-annotation-1.3-spec-java.
Preparing to unpack .../040-libgeronimo-annotation-1.3-spec-java_1.0-1_all.deb ...
Unpacking libgeronimo-annotation-1.3-spec-java (1.0-1) ...
Selecting previously unselected package libaopalliance-java.
Preparing to unpack .../041-libaopalliance-java_20070526-6_all.deb ...
Unpacking libaopalliance-java (20070526-6) ...
Selecting previously unselected package libjsr305-java.
Preparing to unpack .../042-libjsr305-java_0.1~+svn49-10_all.deb ...
Unpacking libjsr305-java (0.1~+svn49-10) ...
Selecting previously unselected package libguava-java.
Preparing to unpack .../043-libguava-java_19.0-1_all.deb ...
Unpacking libguava-java (19.0-1) ...
Selecting previously unselected package libguice-java.
Preparing to unpack .../044-libguice-java_4.0-4_all.deb ...
Unpacking libguice-java (4.0-4) ...
Selecting previously unselected package libmaven-parent-java.
Preparing to unpack .../045-libmaven-parent-java_31-2~18.04_all.deb ...
Unpacking libmaven-parent-java (31-2~18.04) ...
Selecting previously unselected package libplexus-utils2-java.
Preparing to unpack .../046-libplexus-utils2-java_3.0.24-3_all.deb ...
Unpacking libplexus-utils2-java (3.0.24-3) ...
Selecting previously unselected package libwagon-provider-api-java.
Preparing to unpack .../047-libwagon-provider-api-java_3.0.0-2_all.deb ...
Unpacking libwagon-provider-api-java (3.0.0-2) ...
Selecting previously unselected package libmaven-resolver-java.
Preparing to unpack .../048-libmaven-resolver-java_1.3.1-1~18.04_all.deb ...
Unpacking libmaven-resolver-java (1.3.1-1~18.04) ...
Selecting previously unselected package libplexus-cipher-java.
Preparing to unpack .../049-libplexus-cipher-java_1.7-3_all.deb ...
Unpacking libplexus-cipher-java (1.7-3) ...
Selecting previously unselected package libplexus-classworlds-java.
Preparing to unpack .../050-libplexus-classworlds-java_2.5.2-2_all.deb ...
Unpacking libplexus-classworlds-java (2.5.2-2) ...
Selecting previously unselected package libplexus-component-annotations-java.
Preparing to unpack .../051-libplexus-component-annotations-java_1.7.1-7_all.deb ...
Unpacking libplexus-component-annotations-java (1.7.1-7) ...
Selecting previously unselected package libplexus-interpolation-java.
Preparing to unpack .../052-libplexus-interpolation-java_1.24-1_all.deb ...
Unpacking libplexus-interpolation-java (1.24-1) ...
Selecting previously unselected package libplexus-sec-dispatcher-java.
Preparing to unpack .../053-libplexus-sec-dispatcher-java_1.4-3_all.deb ...
Unpacking libplexus-sec-dispatcher-java (1.4-3) ...
Selecting previously unselected package libslf4j-java.
Preparing to unpack .../054-libslf4j-java_1.7.25-3_all.deb ...
Unpacking libslf4j-java (1.7.25-3) ...
Selecting previously unselected package libsisu-inject-java.
Preparing to unpack .../055-libsisu-inject-java_0.3.2-2_all.deb ...
Unpacking libsisu-inject-java (0.3.2-2) ...
Selecting previously unselected package libsisu-plexus-java.
Preparing to unpack .../056-libsisu-plexus-java_0.3.3-3_all.deb ...
Unpacking libsisu-plexus-java (0.3.3-3) ...
Selecting previously unselected package libmaven3-core-java.
Preparing to unpack .../057-libmaven3-core-java_3.6.0-1~18.04.1_all.deb ...
Unpacking libmaven3-core-java (3.6.0-1~18.04.1) ...
Selecting previously unselected package libplexus-utils-java.
Preparing to unpack .../058-libplexus-utils-java_1%3a1.5.15-5_all.deb ...
Unpacking libplexus-utils-java (1:1.5.15-5) ...
Selecting previously unselected package libmaven-shared-io-java.
Preparing to unpack .../059-libmaven-shared-io-java_3.0.0-3_all.deb ...
Unpacking libmaven-shared-io-java (3.0.0-3) ...
Selecting previously unselected package libmaven-file-management-java.
Preparing to unpack .../060-libmaven-file-management-java_3.0.0-1_all.deb ...
Unpacking libmaven-file-management-java (3.0.0-1) ...
Selecting previously unselected package libcommons-compress-java.
Preparing to unpack .../061-libcommons-compress-java_1.18-1~18.04_all.deb ...
Unpacking libcommons-compress-java (1.18-1~18.04) ...
Selecting previously unselected package libplexus-io-java.
Preparing to unpack .../062-libplexus-io-java_3.1.1-1~18.04_all.deb ...
Unpacking libplexus-io-java (3.1.1-1~18.04) ...
Selecting previously unselected package libsnappy-jni.
Preparing to unpack .../063-libsnappy-jni_1.1.4-1_amd64.deb ...
Unpacking libsnappy-jni (1.1.4-1) ...
Selecting previously unselected package libsnappy-java.
Preparing to unpack .../064-libsnappy-java_1.1.4-1_all.deb ...
Unpacking libsnappy-java (1.1.4-1) ...
Selecting previously unselected package libxz-java.
Preparing to unpack .../065-libxz-java_1.8-1_all.deb ...
Unpacking libxz-java (1.8-1) ...
Selecting previously unselected package libplexus-archiver-java.
Preparing to unpack .../066-libplexus-archiver-java_3.5-2_all.deb ...
Unpacking libplexus-archiver-java (3.5-2) ...
Selecting previously unselected package libsisu-guice-java.
Preparing to unpack .../067-libsisu-guice-java_4.2.0-1_all.deb ...
Unpacking libsisu-guice-java (4.2.0-1) ...
Selecting previously unselected package libsisu-ioc-java.
Preparing to unpack .../068-libsisu-ioc-java_2.3.0-11_all.deb ...
Unpacking libsisu-ioc-java (2.3.0-11) ...
Selecting previously unselected package libhttpcore-java.
Preparing to unpack .../069-libhttpcore-java_4.4.9-1_all.deb ...
Unpacking libhttpcore-java (4.4.9-1) ...
Selecting previously unselected package libcommons-codec-java.
Preparing to unpack .../070-libcommons-codec-java_1.11-1_all.deb ...
Unpacking libcommons-codec-java (1.11-1) ...
Selecting previously unselected package libhttpclient-java.
Preparing to unpack .../071-libhttpclient-java_4.5.5-1_all.deb ...
Unpacking libhttpclient-java (4.5.5-1) ...
Selecting previously unselected package libjsoup-java.
Preparing to unpack .../072-libjsoup-java_1.10.2-2_all.deb ...
Unpacking libjsoup-java (1.10.2-2) ...
Selecting previously unselected package libwagon-http-java.
Preparing to unpack .../073-libwagon-http-java_3.0.0-2_all.deb ...
Unpacking libwagon-http-java (3.0.0-2) ...
Selecting previously unselected package libistack-commons-java.
Preparing to unpack .../074-libistack-commons-java_3.0.6-3~18.04_all.deb ...
Unpacking libistack-commons-java (3.0.6-3~18.04) ...
Selecting previously unselected package libcodemodel-java.
Preparing to unpack .../075-libcodemodel-java_2.6+jaxb2.3.0.1-7~18.04_all.deb ...
Unpacking libcodemodel-java (2.6+jaxb2.3.0.1-7~18.04) ...
Selecting previously unselected package libdtd-parser-java.
Preparing to unpack .../076-libdtd-parser-java_1.2~svn20110404-1_all.deb ...
Unpacking libdtd-parser-java (1.2~svn20110404-1) ...
Selecting previously unselected package libecj-java.
Preparing to unpack .../077-libecj-java_3.16.0-1~18.04_all.deb ...
Unpacking libecj-java (3.16.0-1~18.04) ...
Selecting previously unselected package libjaxb-api-java.
Preparing to unpack .../078-libjaxb-api-java_2.3.1-1~18.04_all.deb ...
Unpacking libjaxb-api-java (2.3.1-1~18.04) ...
Selecting previously unselected package libstax-ex-java.
Preparing to unpack .../079-libstax-ex-java_1.7.8-3~18.04.1_all.deb ...
Unpacking libstax-ex-java (1.7.8-3~18.04.1) ...
Selecting previously unselected package libstreambuffer-java.
Preparing to unpack .../080-libstreambuffer-java_1.5.4-1_all.deb ...
Unpacking libstreambuffer-java (1.5.4-1) ...
Selecting previously unselected package librelaxng-datatype-java.
Preparing to unpack .../081-librelaxng-datatype-java_1.0+ds1-3_all.deb ...
Unpacking librelaxng-datatype-java (1.0+ds1-3) ...
Selecting previously unselected package libxsom-java.
Preparing to unpack .../082-libxsom-java_2.3.0.1-7~18.04_all.deb ...
Unpacking libxsom-java (2.3.0.1-7~18.04) ...
Selecting previously unselected package libfastinfoset-java.
Preparing to unpack .../083-libfastinfoset-java_1.2.12-3_all.deb ...
Unpacking libfastinfoset-java (1.2.12-3) ...
Selecting previously unselected package libflexdock-java.
Preparing to unpack .../084-libflexdock-java_1.2.4-1_all.deb ...
Unpacking libflexdock-java (1.2.4-1) ...
Selecting previously unselected package libnb-org-openide-util-lookup-java.
Preparing to unpack .../085-libnb-org-openide-util-lookup-java_10.0-2~18.04.1_all.deb ...
Unpacking libnb-org-openide-util-lookup-java (10.0-2~18.04.1) ...
Selecting previously unselected package libnb-org-openide-util-java.
Preparing to unpack .../086-libnb-org-openide-util-java_10.0-2~18.04.1_all.deb ...
Unpacking libnb-org-openide-util-java (10.0-2~18.04.1) ...
Selecting previously unselected package libfreehep-util-java.
Preparing to unpack .../087-libfreehep-util-java_2.0.2-7_all.deb ...
Unpacking libfreehep-util-java (2.0.2-7) ...
Selecting previously unselected package libfreehep-swing-java.
Preparing to unpack .../088-libfreehep-swing-java_2.0.3-5_all.deb ...
Unpacking libfreehep-swing-java (2.0.3-5) ...
Selecting previously unselected package libfreehep-export-java.
Preparing to unpack .../089-libfreehep-export-java_2.1.1-4_all.deb ...
Unpacking libfreehep-export-java (2.1.1-4) ...
Selecting previously unselected package libfreehep-graphics2d-java.
Preparing to unpack .../090-libfreehep-graphics2d-java_2.1.1-6_all.deb ...
Unpacking libfreehep-graphics2d-java (2.1.1-6) ...
Selecting previously unselected package libfreehep-io-java.
Preparing to unpack .../091-libfreehep-io-java_2.0.2-6_all.deb ...
Unpacking libfreehep-io-java (2.0.2-6) ...
Selecting previously unselected package libfreehep-graphicsio-java.
Preparing to unpack .../092-libfreehep-graphicsio-java_2.1.1-5_all.deb ...
Unpacking libfreehep-graphicsio-java (2.1.1-5) ...
Selecting previously unselected package libtablelayout-java.
Preparing to unpack .../093-libtablelayout-java_20090826-4_all.deb ...
Unpacking libtablelayout-java (20090826-4) ...
Selecting previously unselected package libjas-plotter-java.
Preparing to unpack .../094-libjas-plotter-java_2.2.6+dfsg1-4_all.deb ...
Unpacking libjas-plotter-java (2.2.6+dfsg1-4) ...
Selecting previously unselected package libfreehep-graphicsio-tests-java.
Preparing to unpack .../095-libfreehep-graphicsio-tests-java_2.1.1+dfsg1-5_all.deb ...
Unpacking libfreehep-graphicsio-tests-java (2.1.1+dfsg1-5) ...
Selecting previously unselected package libjdom1-java.
Preparing to unpack .../096-libjdom1-java_1.1.3-2~18.04_all.deb ...
Unpacking libjdom1-java (1.1.3-2~18.04) ...
Selecting previously unselected package libfreehep-graphicsio-emf-java.
Preparing to unpack .../097-libfreehep-graphicsio-emf-java_2.1.1-emfplus+dfsg1-4_all.deb ...
Unpacking libfreehep-graphicsio-emf-java (2.1.1-emfplus+dfsg1-4) ...
Selecting previously unselected package libgluegen2-jni.
Preparing to unpack .../098-libgluegen2-jni_2.3.2-7~18.04_amd64.deb ...
Unpacking libgluegen2-jni (2.3.2-7~18.04) ...
Selecting previously unselected package libgluegen2-rt-java.
Preparing to unpack .../099-libgluegen2-rt-java_2.3.2-7~18.04_all.deb ...
Unpacking libgluegen2-rt-java (2.3.2-7~18.04) ...
Selecting previously unselected package libsz2:amd64.
Preparing to unpack .../100-libsz2_0.3.2-2_amd64.deb ...
Unpacking libsz2:amd64 (0.3.2-2) ...
Selecting previously unselected package libhdf5-100:amd64.
Preparing to unpack .../101-libhdf5-100_1.10.0-patch1+docs-4_amd64.deb ...
Unpacking libhdf5-100:amd64 (1.10.0-patch1+docs-4) ...
Selecting previously unselected package librngom-java.
Preparing to unpack .../102-librngom-java_2.3.0.1-7~18.04_all.deb ...
Unpacking librngom-java (2.3.0.1-7~18.04) ...
Selecting previously unselected package libtxw2-java.
Preparing to unpack .../103-libtxw2-java_2.3.0.1-7~18.04_all.deb ...
Unpacking libtxw2-java (2.3.0.1-7~18.04) ...
Selecting previously unselected package libjaxb-java.
Preparing to unpack .../104-libjaxb-java_2.3.0.1-7~18.04_all.deb ...
Unpacking libjaxb-java (2.3.0.1-7~18.04) ...
Selecting previously unselected package libjeuclid-core-java.
Preparing to unpack .../105-libjeuclid-core-java_3.1.9-4_all.deb ...
Unpacking libjeuclid-core-java (3.1.9-4) ...
Selecting previously unselected package libjgoodies-common-java.
Preparing to unpack .../106-libjgoodies-common-java_1.8.1-2_all.deb ...
Unpacking libjgoodies-common-java (1.8.1-2) ...
Selecting previously unselected package libjgoodies-looks-java.
Preparing to unpack .../107-libjgoodies-looks-java_2.7.0-3~18.04_all.deb ...
Unpacking libjgoodies-looks-java (2.7.0-3~18.04) ...
Selecting previously unselected package libjgraphx-java.
Preparing to unpack .../108-libjgraphx-java_2.1.0.7-1_all.deb ...
Unpacking libjgraphx-java (2.1.0.7-1) ...
Selecting previously unselected package libjlatexmath-java.
Preparing to unpack .../109-libjlatexmath-java_1.0.7-1_all.deb ...
Unpacking libjlatexmath-java (1.0.7-1) ...
Selecting previously unselected package libjlatexmath-fop-java.
Preparing to unpack .../110-libjlatexmath-fop-java_1.0.7-1_all.deb ...
Unpacking libjlatexmath-fop-java (1.0.7-1) ...
Selecting previously unselected package libjogl2-jni.
Preparing to unpack .../111-libjogl2-jni_2.3.2+dfsg-8~18.04_amd64.deb ...
Unpacking libjogl2-jni (2.3.2+dfsg-8~18.04) ...
Selecting previously unselected package libjogl2-java.
Preparing to unpack .../112-libjogl2-java_2.3.2+dfsg-8~18.04_all.deb ...
Unpacking libjogl2-java (2.3.2+dfsg-8~18.04) ...
Selecting previously unselected package libjrosetta-java.
Preparing to unpack .../113-libjrosetta-java_1.0.4-4_all.deb ...
Unpacking libjrosetta-java (1.0.4-4) ...
Selecting previously unselected package libmatio4:amd64.
Preparing to unpack .../114-libmatio4_1.5.11-1_amd64.deb ...
Unpacking libmatio4:amd64 (1.5.11-1) ...
Selecting previously unselected package libregexp-java.
Preparing to unpack .../115-libregexp-java_1.5-4_all.deb ...
Unpacking libregexp-java (1.5-4) ...
Selecting previously unselected package libsaxon-java.
Preparing to unpack .../116-libsaxon-java_1%3a6.5.5-12_all.deb ...
Unpacking libsaxon-java (1:6.5.5-12) ...
Selecting previously unselected package liblaf-plugin-java.
Preparing to unpack .../117-liblaf-plugin-java_7.3+dfsg3-4~18.04.1_all.deb ...
Unpacking liblaf-plugin-java (7.3+dfsg3-4~18.04.1) ...
Selecting previously unselected package libskinlf-java.
Preparing to unpack .../118-libskinlf-java_6.7-10_all.deb ...
Unpacking libskinlf-java (6.7-10) ...
Selecting previously unselected package scilab-data.
Preparing to unpack .../119-scilab-data_6.0.1-7ubuntu1~18.04_all.deb ...
Unpacking scilab-data (6.0.1-7ubuntu1~18.04) ...
Selecting previously unselected package scilab-minimal-bin.
Preparing to unpack .../120-scilab-minimal-bin_6.0.1-7ubuntu1~18.04_amd64.deb ...
Unpacking scilab-minimal-bin (6.0.1-7ubuntu1~18.04) ...
Selecting previously unselected package scilab-include.
Preparing to unpack .../121-scilab-include_6.0.1-7ubuntu1~18.04_amd64.deb ...
Unpacking scilab-include (6.0.1-7ubuntu1~18.04) ...
Selecting previously unselected package scilab-cli.
Preparing to unpack .../122-scilab-cli_6.0.1-7ubuntu1~18.04_all.deb ...
Unpacking scilab-cli (6.0.1-7ubuntu1~18.04) ...
Selecting previously unselected package liblucene4.10-java.
Preparing to unpack .../123-liblucene4.10-java_4.10.4+dfsg-3_all.deb ...
Unpacking liblucene4.10-java (4.10.4+dfsg-3) ...
Selecting previously unselected package scilab-full-bin.
Preparing to unpack .../124-scilab-full-bin_6.0.1-7ubuntu1~18.04_amd64.deb ...
Unpacking scilab-full-bin (6.0.1-7ubuntu1~18.04) ...
Selecting previously unselected package scilab.
Preparing to unpack .../125-scilab_6.0.1-7ubuntu1~18.04_all.deb ...
Unpacking scilab (6.0.1-7ubuntu1~18.04) ...
Setting up libjlatexmath-java (1.0.7-1) ...
Setting up libslf4j-java (1.7.25-3) ...
Setting up libplexus-classworlds-java (2.5.2-2) ...
Setting up libantlr-java (2.7.7+dfsg-9.2) ...
Setting up libargs4j-java (2.33-1) ...
Setting up libaec0:amd64 (0.3.2-2) ...
Setting up libjaxp1.3-java (1.3.05-5) ...
Setting up tk8.6 (8.6.8-4) ...
Setting up libhttpcore-java (4.4.9-1) ...
Processing triggers for mime-support (3.60ubuntu1) ...
Processing triggers for desktop-file-utils (0.23+linuxmint5) ...
Setting up libfontbox-java (1:1.8.16-2~18.04) ...
Setting up libjsoup-java (1.10.2-2) ...
Setting up libplexus-cipher-java (1.7-3) ...
Setting up libsnappy-jni (1.1.4-1) ...
Setting up libxml-commons-external-java (1.4.01-3) ...
Setting up libdtd-parser-java (1.2~svn20110404-1) ...
Setting up antlr (2.7.7+dfsg-9.2) ...
Setting up java-wrappers (0.3) ...
Setting up libplexus-interpolation-java (1.24-1) ...
Setting up libactivation-java (1.2.0-1ubuntu1) ...
Setting up libplexus-component-annotations-java (1.7.1-7) ...
Setting up libregexp-java (1.5-4) ...
Setting up libplexus-utils2-java (3.0.24-3) ...
Setting up libwagon-provider-api-java (3.0.0-2) ...
Setting up scilab-include (6.0.1-7ubuntu1~18.04) ...
Setting up libjsr305-java (0.1~+svn49-10) ...
Setting up libjogl2-jni (2.3.2+dfsg-8~18.04) ...
Setting up libxml-commons-resolver1.1-java (1.2-9) ...
Setting up libgluegen2-jni (2.3.2-7~18.04) ...
Setting up libnb-org-openide-util-lookup-java (10.0-2~18.04.1) ...
Setting up libecj-java (3.16.0-1~18.04) ...
Setting up libxz-java (1.8-1) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...
Setting up libgeronimo-interceptor-3.0-spec-java (1.0.1-4fakesync) ...
Setting up libavalon-framework-java (4.2.0-10) ...
Setting up libmaven-resolver-java (1.3.1-1~18.04) ...
Setting up ant (1.10.5-3~18.04) ...
Setting up javahelp2 (2.0.05.ds1-9) ...
Processing triggers for doc-base (0.10.8) ...
Processing 1 added doc-base file...
Registering documents with scrollkeeper...
Setting up libjaxen-java (1.1.6-3) ...
Setting up libjrosetta-java (1.0.4-4) ...
Setting up libsnappy-java (1.1.4-1) ...
Setting up tcl8.6 (8.6.8+dfsg-3) ...
Setting up libtablelayout-java (20090826-4) ...
Setting up libapache-pom-java (18-1) ...
Setting up scilab-data (6.0.1-7ubuntu1~18.04) ...
Setting up junit (3.8.2-9) ...
Setting up libarpack2:amd64 (3.5.0+real-2) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for shared-mime-info (1.9-2) ...
Setting up libatinject-jsr330-api-java (1.0+ds1-5) ...
Setting up libmaven-parent-java (31-2~18.04) ...
Setting up liblucene4.10-java (4.10.4+dfsg-3) ...
Processing triggers for gnome-menus (3.13.3-11ubuntu1.1) ...
Setting up libflexdock-java (1.2.4-1) ...
Processing triggers for hicolor-icon-theme (0.17-2) ...
Setting up libaopalliance-java (20070526-6) ...
Setting up liblaf-plugin-java (7.3+dfsg3-4~18.04.1) ...
Setting up libgeronimo-annotation-1.3-spec-java (1.0-1) ...
Setting up libjgoodies-common-java (1.8.1-2) ...
Setting up librelaxng-datatype-java (1.0+ds1-3) ...
Setting up libsaxon-java (1:6.5.5-12) ...
Setting up libcommons-cli-java (1.4-1) ...
Setting up libplexus-sec-dispatcher-java (1.4-3) ...
Setting up libsz2:amd64 (0.3.2-2) ...
Setting up libdom4j-java (2.1.0-2) ...
Setting up libnb-org-openide-util-java (10.0-2~18.04.1) ...
Setting up libjgoodies-looks-java (2.7.0-3~18.04) ...
Setting up libhdf5-100:amd64 (1.10.0-patch1+docs-4) ...
Setting up ant-optional (1.10.5-3~18.04) ...
Setting up libjaxb-api-java (2.3.1-1~18.04) ...
Setting up libxsom-java (2.3.0.1-7~18.04) ...
Setting up libstax-ex-java (1.7.8-3~18.04.1) ...
Setting up tcl (8.6.0+9) ...
Setting up libguava-java (19.0-1) ...
Setting up libgluegen2-rt-java (2.3.2-7~18.04) ...
Setting up libcommons-parent-java (43-1) ...
Setting up libxerces2-java (2.11.0-8) ...
Setting up libcdi-api-java (1.2-2) ...
Setting up libfreehep-io-java (2.0.2-6) ...
Setting up libxalan2-java (2.7.2-1) ...
Setting up tk (8.6.0+9) ...
Setting up libjgraphx-java (2.1.0.7-1) ...
Setting up libplexus-utils-java (1:1.5.15-5) ...
Setting up libfreehep-util-java (2.0.2-7) ...
Setting up libbsf-java (1:2.4.0-5build1) ...
Setting up libjdom1-java (1.1.3-2~18.04) ...
Setting up bwidget (1.9.12-1) ...
Setting up libcommons-compress-java (1.18-1~18.04) ...
Setting up libcommons-lang3-java (3.8-1~18.04.2) ...
Setting up librngom-java (2.3.0.1-7~18.04) ...
Setting up libfreehep-graphics2d-java (2.1.1-6) ...
Setting up libstreambuffer-java (1.5.4-1) ...
Setting up libsisu-guice-java (4.2.0-1) ...
Setting up libfreehep-swing-java (2.0.3-5) ...
Setting up libjogl2-java (2.3.2+dfsg-8~18.04) ...
Setting up libcommons-codec-java (1.11-1) ...
Setting up libsisu-ioc-java (2.3.0-11) ...
Setting up libjas-plotter-java (2.2.6+dfsg1-4) ...
Setting up libmatio4:amd64 (1.5.11-1) ...
Setting up libcommons-io-java (2.6-2) ...
Setting up libguice-java (4.0-4) ...
Setting up libcommons-logging-java (1.2-2) ...
Setting up libmaven-shared-utils-java (3.3.0-1~18.04) ...
Setting up libfastinfoset-java (1.2.12-3) ...
Setting up libfreehep-export-java (2.1.1-4) ...
Setting up libskinlf-java (6.7-10) ...
Setting up libfreehep-graphicsio-java (2.1.1-5) ...
Setting up libsisu-inject-java (0.3.2-2) ...
Setting up libhttpclient-java (4.5.5-1) ...
Setting up scilab-minimal-bin (6.0.1-7ubuntu1~18.04) ...
Setting up libxmlgraphics-commons-java (2.2-1) ...
Setting up libplexus-io-java (3.1.1-1~18.04) ...
Setting up libfreehep-graphicsio-tests-java (2.1.1+dfsg1-5) ...
Setting up scilab-cli (6.0.1-7ubuntu1~18.04) ...
Setting up libfreehep-graphicsio-emf-java (2.1.1-emfplus+dfsg1-4) ...
Setting up libsisu-plexus-java (0.3.3-3) ...
Setting up libwagon-http-java (3.0.0-2) ...
Setting up libbatik-java (1.10-2~18.04) ...
Setting up libjeuclid-core-java (3.1.9-4) ...
Setting up libplexus-archiver-java (3.5-2) ...
Setting up libfop-java (1:2.1-7) ...
Setting up libmaven3-core-java (3.6.0-1~18.04.1) ...
Setting up libmaven-shared-io-java (3.0.0-3) ...
Setting up fop (1:2.1-7) ...
Setting up libmaven-file-management-java (3.0.0-1) ...
Setting up libjlatexmath-fop-java (1.0.7-1) ...
Setting up libistack-commons-java (3.0.6-3~18.04) ...
Setting up libcodemodel-java (2.6+jaxb2.3.0.1-7~18.04) ...
Setting up libtxw2-java (2.3.0.1-7~18.04) ...
Setting up libjaxb-java (2.3.0.1-7~18.04) ...
Setting up scilab-full-bin (6.0.1-7ubuntu1~18.04) ...
Setting up scilab (6.0.1-7ubuntu1~18.04) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...

```

## Scilab Commands

```
chenwx@chenwx:~ $ scilab -h
Usage:
scilab <arguments>
scilab-cli <arguments>
scilab-adv-cli <arguments>

  Possible arguments are:
  -display Display: for use under Xwindow systems to set a specific X server display.
  -d Display      : equivalent to -display Display.
  -e Instruction  : execute the scilab instruction given in Instruction argument.
                    -e and -f arguments are mutually exclusive.
  -f File         : execute the scilab script given in File argument.
                    -e and -f arguments are mutually exclusive.
  -quit           : force scilab exit after execution of script from -e or -f argument.
                    this flag is ignored if it is not used with -e or -f argument.
  -l Lang         : set the current language. Lang can be equal to fr or en.
  -nb             : do not display Scilab loading on start.
  -ns             : do not execute scilab.start startup file. This argument will disable many features in Scilab (Only use if you know what you are doing).
  -nouserstartup  : do not execute the user startup files SCIHOME/.scilab or SCIHOME/scilab.ini.
  -noatomsautoload: do not load ATOMS installed module.
  -nw             : start Scilab without dedicated Scilab Window.
  -nwni           : start Scilab without the GUI, graphic and help features (batch mode). This argument disables the need of Java.
  -nogui          : See -nwni
  -nocolor        : Remove the color in the cli and adv-cli modes
  -args           : accept all extra arguments and make them available through sciargs
  -version        : print product version and exit.
  -h/--help       : display help about this command.
  --texmacs       : reserved for TeXMacs.
  -scihome dir    : Force SCIHOME to given dir.

Developer arguments:
  -debug          : Start Scilab under gdb (Unix/linux only).
                    define the variable SCILAB_GDB_OPT to add custom arguments to gdb.
  -debug-kdbg     : Start Scilab under kdbg (Unix/linux only).
  -profiling      : Start Scilab under valgrind (Unix/linux only).
                    define the variable SCILAB_VALGRIND_OPT to add custom arguments to
                    valgrind (and override the existing valgrind arguments).
  -profiling-visu : Start Scilab under callgrind (Unix/linux only).
                    define the variable SCILAB_VALGRIND_OPT to add custom arguments to
                    callgrind (and override the existing callgrind arguments).
  -disable-exception-catching : Disable Scilab exception catching system.

  --parse-file File : Only parse File argument without execution and exit.
  --parse-trace     : Display bison state machine evolution.
  --AST-trace       : Display ASCII-art AST to be human readable.
  --pretty-print    : Display pretty-printed code, standard Scilab syntax.

Developer Timer arguments:
  --AST-timed      : Time each AST node.
  --timed          : Time global execution.

Developer Debug arguments:
  --no-exec        : Only do Lexing/parsing do not execute instructions.
  --context-dump   : Display context status.
  --exec-verbose   : Display command before execute it.
  --timeout delay  : Kill the Scilab process after a delay (s, m, h, d).

      All these arguments can be retrieved by the Scilab function sciargs.

  Several environment variables can be declared:
  SCIVERBOSE               Provides debugging information of the startup
  JAVA_HOME                Declares which Java Virtual Machine to use
  SCI_DISABLE_TK           Disables Tk (but not Tcl) features
  SCI_JAVA_ENABLE_HEADLESS Runs Java Headless VM (without GUI; Windows and Linux only)
  SCI_DISABLE_EXCEPTION_CATCHING Disable the catch by Scilab of exception (segfault, ...)
```

# SciPy

[SciPy](https://www.scipy.org/) is a free and open-source Python library used for scientific computing and technical computing.

SciPy contains modules for optimization, linear algebra, integration, interpolation, special functions, FFT, signal and image processing, ODE solvers and other tasks common in science and engineering.

SciPy builds on the [NumPy](http://www.numpy.org/) array object and is part of the NumPy stack which includes tools like [Matplotlib](https://matplotlib.org/), [pandas](http://pandas.pydata.org/) and [SymPy](https://www.sympy.org/en/index.html), and an expanding set of scientific computing libraries. This NumPy stack has similar users to other applications such as MATLAB, GNU Octave, and Scilab. The NumPy stack is also sometimes referred to as the SciPy stack.

SciPy is also a family of conferences for users and developers of these tools: SciPy (in the United States), EuroSciPy (in Europe) and SciPy.in (in India). Enthought originated the SciPy conference in the United States and continues to sponsor many of the international conferences as well as host the SciPy website.

SciPy library is currently distributed under the BSD license, and its development is sponsored and supported by an open community of developers. It is also supported by [NumFOCUS](https://numfocus.org/), a community foundation for supporting reproducible and accessible science.

* [SciPy Home Page](https://www.scipy.org/)
* [Scipy Documentation](https://scipy.org/docs.html)
* [Numpy and Scipy Documentation](https://docs.scipy.org/doc/)
* [SciPy Cookbook](https://scipy-cookbook.readthedocs.io/)
* [Scipy library main repository](https://github.com/scipy/scipy/)
* [Code of Conduct](https://scipy.github.io/devdocs/dev/conduct/code_of_conduct.html)

Note that **Python 3** is recommended for scientific computing because [Python 2.7 is end of life, and will not be maintained past January 1, 2020](https://pythonclock.org/).

## Install SciPy via pip

Refer to <a href="{{ site.base-url }}/2017/03/09/python.html#install-pip">Install pip</a> to know how to install pip.

Install package **setuptools** in Python 3.x, which is used when installing SciPy packages later:

```
# pip3 install setuptools
chenwx@chenwx:~ $ python3 -m pip install setuptools
Collecting setuptools
  Using cached https://files.pythonhosted.org/packages/ec/51/f45cea425fd5cb0b0380f5b0f048ebc1da5b417e48d304838c02d6288a1e/setuptools-41.0.1-py2.py3-none-any.whl
Installing collected packages: setuptools
Successfully installed setuptools-41.0.1
```

Install package **wheel** in Python 3.x, which is used when installing SciPy packages later:

```
# pip3 install wheel
chenwx@chenwx:~ $ python3 -m pip install wheel
Collecting wheel
  Downloading https://files.pythonhosted.org/packages/bb/10/44230dd6bf3563b8f227dbf344c908d412ad2ff48066476672f3a72e174e/wheel-0.33.4-py2.py3-none-any.whl
Installing collected packages: wheel
Successfully installed wheel-0.33.4
```

Install package **python3-tk** in Python 3.x:

```
chenwx@chenwx:~ $ sudo apt-get install python3-tk
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
```

Install the header files and static libraries **python3-dev** for Python3:

```
chenwx@chenwx:~ $ sudo apt install python3-dev
[sudo] password for chenwx:       
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  dh-python libpython3-dev libpython3.6-dev python3.6-dev
The following NEW packages will be installed:
  dh-python libpython3-dev libpython3.6-dev python3-dev python3.6-dev
0 upgraded, 5 newly installed, 0 to remove and 0 not upgraded.
Need to get 45.4 MB of archives.
After this operation, 77.1 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://mirror.nforce.com/pub/linux/ubuntu bionic/main amd64 dh-python all 3.20180325ubuntu2 [89.2 kB]
Get:2 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/main amd64 libpython3.6-dev amd64 3.6.7-1~18.04 [44.8 MB]
Get:3 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/main amd64 libpython3-dev amd64 3.6.7-1~18.04 [7328 B]
Get:4 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/main amd64 python3.6-dev amd64 3.6.7-1~18.04 [508 kB]
Get:5 http://mirror.nforce.com/pub/linux/ubuntu bionic-updates/main amd64 python3-dev amd64 3.6.7-1~18.04 [1288 B]
Fetched 45.4 MB in 29s (1541 kB/s)
Selecting previously unselected package dh-python.
(Reading database ... 308671 files and directories currently installed.)
Preparing to unpack .../dh-python_3.20180325ubuntu2_all.deb ...
Unpacking dh-python (3.20180325ubuntu2) ...
Selecting previously unselected package libpython3.6-dev:amd64.
Preparing to unpack .../libpython3.6-dev_3.6.7-1~18.04_amd64.deb ...
Unpacking libpython3.6-dev:amd64 (3.6.7-1~18.04) ...
Selecting previously unselected package libpython3-dev:amd64.
Preparing to unpack .../libpython3-dev_3.6.7-1~18.04_amd64.deb ...
Unpacking libpython3-dev:amd64 (3.6.7-1~18.04) ...
Selecting previously unselected package python3.6-dev.
Preparing to unpack .../python3.6-dev_3.6.7-1~18.04_amd64.deb ...
Unpacking python3.6-dev (3.6.7-1~18.04) ...
Selecting previously unselected package python3-dev.
Preparing to unpack .../python3-dev_3.6.7-1~18.04_amd64.deb ...
Unpacking python3-dev (3.6.7-1~18.04) ...
Setting up libpython3.6-dev:amd64 (3.6.7-1~18.04) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Setting up python3.6-dev (3.6.7-1~18.04) ...
Setting up dh-python (3.20180325ubuntu2) ...
Setting up libpython3-dev:amd64 (3.6.7-1~18.04) ...
Setting up python3-dev (3.6.7-1~18.04) ...
```

Install module **vtk** and **mayavi** for 3D plotting:

```
chenwx@chenwx:~ $ export LC_ALL=C.UTF-8

# pip3 install vtk
chenwx@chenwx:~ $ python3 -m pip install vtk
Collecting vtk
  Using cached https://files.pythonhosted.org/packages/22/f5/30e11e1ad21701e1cd185b046979107930419a74a5602c6b899dc8523fe4/vtk-8.1.2-cp36-cp36m-manylinux1_x86_64.whl
Installing collected packages: vtk
Successfully installed vtk-8.1.2

# pip3 install mayavi
chenwx@chenwx:~ $ python3 -m pip install mayavi
Collecting mayavi
  Using cached https://files.pythonhosted.org/packages/83/9e/293ba57353ed258c2f64d54bf00ca1447c1f38f4eb60d0e762ddec57bf51/mayavi-4.6.2.tar.bz2
Collecting apptools (from mayavi)
Collecting envisage (from mayavi)
Collecting numpy (from mayavi)
  Using cached https://files.pythonhosted.org/packages/c1/e2/4db8df8f6cddc98e7d7c537245ef2f4e41a1ed17bf0c3177ab3cc6beac7f/numpy-1.16.3-cp36-cp36m-manylinux1_x86_64.whl
Collecting pyface>=6.0.0 (from mayavi)
Collecting pygments (from mayavi)
  Using cached https://files.pythonhosted.org/packages/6e/00/c5cb5fc7c047da4af049005d0146b3a961b1a25d9cefbbe24bf0882a11ad/Pygments-2.4.0-py2.py3-none-any.whl
Collecting traits>=4.6.0 (from mayavi)
Collecting traitsui>=6.0.0 (from mayavi)
Collecting vtk (from mayavi)
  Using cached https://files.pythonhosted.org/packages/22/f5/30e11e1ad21701e1cd185b046979107930419a74a5602c6b899dc8523fe4/vtk-8.1.2-cp36-cp36m-manylinux1_x86_64.whl
Collecting configobj (from apptools->mayavi)
Collecting six (from traits>=4.6.0->mayavi)
  Using cached https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Building wheels for collected packages: mayavi
  Running setup.py bdist_wheel for mayavi ... done
  Stored in directory: /home/chenwx/.cache/pip/wheels/59/49/db/14986f88cce0c66019c64ed57d47536c510efa999e504f378e
Successfully built mayavi
Installing collected packages: six, traits, pyface, traitsui, configobj, apptools, envisage, numpy, pygments, vtk, mayavi
Successfully installed apptools-4.4.0 configobj-5.0.6 envisage-4.7.2 mayavi-4.6.2 numpy-1.16.3 pyface-6.1.0 pygments-2.4.0 six-1.12.0 traits-5.1.1 traitsui-6.1.0 vtk-8.1.2
```

Install **wxPython** in Python 3.x:

```
chenwx@chenwx:~ $ pip3 install -U -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-16.04  wxPython

Collecting wxPython
  Downloading https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-16.04/wxPython-4.0.4-cp36-cp36m-linux_x86_64.whl (104.4MB)
    100% |################################| 104.4MB 10kB/s
Collecting six (from wxPython)
  Using cached https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Collecting Pillow (from wxPython)
  Using cached https://files.pythonhosted.org/packages/d2/c2/f84b1e57416755e967236468dcfb0fad7fd911f707185efc4ba8834a1a94/Pillow-6.0.0-cp36-cp36m-manylinux1_x86_64.whl
Installing collected packages: six, Pillow, wxPython
Successfully installed Pillow-6.0.0 six-1.12.0 wxPython-4.0.4

chenwx@chenwx:~ $ python3 -m pip show wxPython
Name: wxPython
Version: 4.0.4
Summary: Cross platform GUI toolkit for Python, "Phoenix" version
Home-page: http://wxPython.org/
Author: Robin Dunn
Author-email: robin@alldunn.com
License: wxWindows Library License (https://opensource.org/licenses/wxwindows.php)
Location: /home/chenwx/.local/lib/python3.6/site-packages
Requires: six, Pillow

chenwx@chenwx:~ $ pip3 show wxPython
Name: wxPython
Version: 4.0.4
Summary: Cross platform GUI toolkit for Python, "Phoenix" version
Home-page: http://wxPython.org/
Author: Robin Dunn
Author-email: robin@alldunn.com
License: wxWindows Library License (https://opensource.org/licenses/wxwindows.php)
Location: /home/chenwx/.local/lib/python3.6/site-packages
Requires: Pillow, six
```

[IPython](http://ipython.org/) is a powerful interactive shell, which can be installed via the following command.

* [IPython Documentation (old version)](http://ipython.org/ipython-doc/dev/index.html)
* [IPython Documentation (stable version)](https://ipython.readthedocs.io/en/stable/)

```
chenwx@chenwx:~ $ sudo apt install ipython3
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  python3-decorator python3-ipython python3-ipython-genutils python3-pickleshare python3-prompt-toolkit
  python3-pygments python3-simplegeneric python3-traitlets python3-wcwidth
The following NEW packages will be installed:
  ipython3 python3-decorator python3-ipython python3-ipython-genutils python3-pickleshare python3-prompt-toolkit
  python3-pygments python3-simplegeneric python3-traitlets python3-wcwidth
0 upgraded, 10 newly installed, 0 to remove and 0 not upgraded.
Need to get 1246 kB of archives.
After this operation, 6751 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 python3-decorator all 4.1.2-1 [9364 B]
Get:2 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 python3-pickleshare all 0.7.4-2 [6904 B]
Get:3 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 python3-wcwidth all 0.1.7+dfsg1-1 [14.7 kB]
Get:4 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 python3-prompt-toolkit all 1.0.15-1 [163 kB]
Get:5 http://mirror.nforce.com/pub/linux/ubuntu bionic/main amd64 python3-pygments all 2.2.0+dfsg-1 [574 kB]
Get:6 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 python3-simplegeneric all 0.8.1-1 [11.5 kB]
Get:7 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 python3-ipython-genutils all 0.2.0-1 [20.9 kB]
Get:8 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 python3-traitlets all 4.3.2-1 [59.1 kB]
Get:9 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 python3-ipython all 5.5.0-1 [381 kB]
Get:10 http://mirror.nforce.com/pub/linux/ubuntu bionic/universe amd64 ipython3 all 5.5.0-1 [5304 B]
Fetched 1246 kB in 2s (797 kB/s)
Selecting previously unselected package python3-decorator.
(Reading database ... 307965 files and directories currently installed.)
Preparing to unpack .../0-python3-decorator_4.1.2-1_all.deb ...
Unpacking python3-decorator (4.1.2-1) ...
Selecting previously unselected package python3-pickleshare.
Preparing to unpack .../1-python3-pickleshare_0.7.4-2_all.deb ...
Unpacking python3-pickleshare (0.7.4-2) ...
Selecting previously unselected package python3-wcwidth.
Preparing to unpack .../2-python3-wcwidth_0.1.7+dfsg1-1_all.deb ...
Unpacking python3-wcwidth (0.1.7+dfsg1-1) ...
Selecting previously unselected package python3-prompt-toolkit.
Preparing to unpack .../3-python3-prompt-toolkit_1.0.15-1_all.deb ...
Unpacking python3-prompt-toolkit (1.0.15-1) ...
Selecting previously unselected package python3-pygments.
Preparing to unpack .../4-python3-pygments_2.2.0+dfsg-1_all.deb ...
Unpacking python3-pygments (2.2.0+dfsg-1) ...
Selecting previously unselected package python3-simplegeneric.
Preparing to unpack .../5-python3-simplegeneric_0.8.1-1_all.deb ...
Unpacking python3-simplegeneric (0.8.1-1) ...
Selecting previously unselected package python3-ipython-genutils.
Preparing to unpack .../6-python3-ipython-genutils_0.2.0-1_all.deb ...
Unpacking python3-ipython-genutils (0.2.0-1) ...
Selecting previously unselected package python3-traitlets.
Preparing to unpack .../7-python3-traitlets_4.3.2-1_all.deb ...
Unpacking python3-traitlets (4.3.2-1) ...
Selecting previously unselected package python3-ipython.
Preparing to unpack .../8-python3-ipython_5.5.0-1_all.deb ...
Unpacking python3-ipython (5.5.0-1) ...
Selecting previously unselected package ipython3.
Preparing to unpack .../9-ipython3_5.5.0-1_all.deb ...
Unpacking ipython3 (5.5.0-1) ...
Setting up python3-pickleshare (0.7.4-2) ...
Setting up python3-simplegeneric (0.8.1-1) ...
Setting up python3-wcwidth (0.1.7+dfsg1-1) ...
Setting up python3-ipython-genutils (0.2.0-1) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Setting up python3-decorator (4.1.2-1) ...
Setting up python3-traitlets (4.3.2-1) ...
Setting up python3-pygments (2.2.0+dfsg-1) ...
Setting up python3-prompt-toolkit (1.0.15-1) ...
Setting up python3-ipython (5.5.0-1) ...
Setting up ipython3 (5.5.0-1) ...

chenwx@chenwx:~ $ which ipython3
/usr/bin/ipython3

chenwx@chenwx:~ $ ipython3 --version
7.5.0

chenwx@chenwx:~ $ ipython3 -h
=========
 IPython
=========

Tools for Interactive Computing in Python
=========================================

    A Python shell with automatic history (input and output), dynamic object
    introspection, easier configuration, command completion, access to the
    system shell and more.  IPython can also be embedded in running programs.

Usage

    ipython [subcommand] [options] [-c cmd | -m mod | file] [--] [arg] ...

    If invoked with no options, it executes the file and exits, passing the
    remaining arguments to the script, just as if you had specified the same
    command with python. You may need to specify `--` before args to be passed
    to the script, to prevent IPython from attempting to parse them. If you
    specify the option `-i` before the filename, it will enter an interactive
    IPython session after running the script, rather than exiting. Files ending
    in .py will be treated as normal Python, but files ending in .ipy can
    contain special IPython syntax (magic commands, shell expansions, etc.).

    Almost all configuration in IPython is available via the command-line. Do
    `ipython --help-all` to see all available options.  For persistent
    configuration, look into your `ipython_config.py` configuration file for
    details.

    This file is typically installed in the `IPYTHONDIR` directory, and there
    is a separate configuration directory for each profile. The default profile
    directory will be located in $IPYTHONDIR/profile_default. IPYTHONDIR
    defaults to to `$HOME/.ipython`.  For Windows users, $HOME resolves to
    C:\Users\YourUserName in most instances.

    To initialize a profile with the default configuration file, do::

      $> ipython profile create

    and start editing `IPYTHONDIR/profile_default/ipython_config.py`

    In IPython's documentation, we will refer to this directory as
    `IPYTHONDIR`, you can change its default location by creating an
    environment variable with this name and setting it to the desired path.

    For more information, see the manual available in HTML and PDF in your
    installation, or online at https://ipython.org/documentation.html.

Subcommands
-----------

Subcommands are launched as `ipython cmd [args]`. For information on using
subcommand 'cmd', do: `ipython cmd -h`.

profile
    Create and manage IPython profiles.
kernel
    Start a kernel without an attached frontend.
locate
    print the path to the IPython dir
history
    Manage the IPython history database.
qtconsole
    DEPRECATED, Will be removed in IPython 6.0 : Launch the Jupyter Qt Console.
notebook
    DEPRECATED, Will be removed in IPython 6.0 : Launch the Jupyter HTML Notebook Server.
console
    DEPRECATED, Will be removed in IPython 6.0 : Launch the Jupyter terminal-based Console.
nbconvert
    DEPRECATED, Will be removed in IPython 6.0 : Convert notebooks to/from other formats.
trust
    DEPRECATED, Will be removed in IPython 6.0 : Sign notebooks to trust their potentially unsafe contents at load.
kernelspec
    DEPRECATED, Will be removed in IPython 6.0 : Manage Jupyter kernel specifications.
install-nbextension
    DEPRECATED, Will be removed in IPython 6.0 : Install Jupyter notebook extension files

Options
-------

Arguments that take values are actually convenience aliases to full
Configurables, whose aliases are listed on the help line. For more information
on full configurables, see '--help-all'.

--debug
    set log level to logging.DEBUG (maximize logging output)
--quiet
    set log level to logging.CRITICAL (minimize logging output)
--init
    Initialize profile with default config files.  This is equivalent
    to running `ipython profile create <profile>` prior to startup.
--autoindent
    Turn on autoindenting.
--no-autoindent
    Turn off autoindenting.
--automagic
    Turn on the auto calling of magic commands. Type %%magic at the
    IPython  prompt  for  more information.
--no-automagic
    Turn off the auto calling of magic commands.
--pdb
    Enable auto calling the pdb debugger after every exception.
--no-pdb
    Disable auto calling the pdb debugger after every exception.
--pprint
    Enable auto pretty printing of results.
--no-pprint
    Disable auto pretty printing of results.
--color-info
    IPython can display information about objects via a set of functions,
    and optionally can use colors for this, syntax highlighting
    source code and various other elements. This is on by default, but can cause
    problems with some pagers. If you see such problems, you can disable the
    colours.
--no-color-info
    Disable using colors for info related things.
--nosep
    Eliminate all spacing between prompts.
--pylab
    Pre-load matplotlib and numpy for interactive use with
    the default matplotlib backend.
--matplotlib
    Configure matplotlib for interactive use with
    the default matplotlib backend.
--autoedit-syntax
    Turn on auto editing of files with syntax errors.
--no-autoedit-syntax
    Turn off auto editing of files with syntax errors.
--simple-prompt
    Force simple minimal prompt using `raw_input`
--no-simple-prompt
    Use a rich interactive prompt with prompt_toolkit
--banner
    Display a banner upon starting IPython.
--no-banner
    Don't display a banner upon starting IPython.
--confirm-exit
    Set to confirm when you try to exit IPython with an EOF (Control-D
    in Unix, Control-Z/Enter in Windows). By typing 'exit' or 'quit',
    you can force a direct exit without any confirmation.
--no-confirm-exit
    Don't prompt the user when exiting.
--term-title
    Enable auto setting the terminal title.
--no-term-title
    Disable auto setting the terminal title.
--classic
    Gives IPython a similar feel to the classic Python prompt.
--quick
    Enable quick startup with no config files.
-i
    If running code from the command line, become interactive afterwards.
    It is often useful to follow this with `--` to treat remaining flags as
    script arguments.
--profile-dir=<Unicode> (ProfileDir.location)
    Default: ''
    Set the profile location directly. This overrides the logic used by the
    `profile` option.
--profile=<Unicode> (BaseIPythonApplication.profile)
    Default: 'default'
    The IPython profile to use.
--ipython-dir=<Unicode> (BaseIPythonApplication.ipython_dir)
    Default: ''
    The name of the IPython directory. This directory is used for logging
    configuration (through profiles), history storage, etc. The default is
    usually $HOME/.ipython. This option can also be specified through the
    environment variable IPYTHONDIR.
--log-level=<Enum> (Application.log_level)
    Default: 30
    Choices: (0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL')
    Set the log level by value or name.
--config=<Unicode> (BaseIPythonApplication.extra_config_file)
    Default: ''
    Path to an extra config file to load.
    If specified, load this config file in addition to any other IPython config.
--autocall=<Enum> (InteractiveShell.autocall)
    Default: 0
    Choices: (0, 1, 2)
    Make IPython automatically call any callable object even if you didn't type
    explicit parentheses. For example, 'str 43' becomes 'str(43)' automatically.
    The value can be '0' to disable the feature, '1' for 'smart' autocall, where
    it is not applied if there are no more arguments on the line, and '2' for
    'full' autocall, where all callable objects are automatically called (even
    if no arguments are present).
--colors=<CaselessStrEnum> (InteractiveShell.colors)
    Default: 'Neutral'
    Choices: ['Neutral', 'NoColor', 'LightBG', 'Linux']
    Set the color scheme (NoColor, Neutral, Linux, or LightBG).
--logfile=<Unicode> (InteractiveShell.logfile)
    Default: ''
    The name of the logfile to use.
--logappend=<Unicode> (InteractiveShell.logappend)
    Default: ''
    Start logging to the given file in append mode. Use `logfile` to specify a
    log file to **overwrite** logs to.
-c <Unicode> (InteractiveShellApp.code_to_run)
    Default: ''
    Execute the given command string.
-m <Unicode> (InteractiveShellApp.module_to_run)
    Default: ''
    Run the module as a script.
--ext=<Unicode> (InteractiveShellApp.extra_extension)
    Default: ''
    dotted module name of an IPython extension to load.
--gui=<CaselessStrEnum> (InteractiveShellApp.gui)
    Default: None
    Choices: ['glut', 'gtk', 'gtk2', 'gtk3', 'osx', 'pyglet', 'qt', 'qt4', 'qt5', 'tk', 'wx', 'gtk2', 'qt4']
    Enable GUI event loop integration with any of ('glut', 'gtk', 'gtk2',
    'gtk3', 'osx', 'pyglet', 'qt', 'qt4', 'qt5', 'tk', 'wx', 'gtk2', 'qt4').
--pylab=<CaselessStrEnum> (InteractiveShellApp.pylab)
    Default: None
    Choices: ['auto', 'agg', 'gtk', 'gtk3', 'inline', 'ipympl', 'nbagg', 'notebook', 'osx', 'pdf', 'ps', 'qt', 'qt4', 'qt5', 'svg', 'tk', 'widget', 'wx']
    Pre-load matplotlib and numpy for interactive use, selecting a particular
    matplotlib backend and loop integration.
--matplotlib=<CaselessStrEnum> (InteractiveShellApp.matplotlib)
    Default: None
    Choices: ['auto', 'agg', 'gtk', 'gtk3', 'inline', 'ipympl', 'nbagg', 'notebook', 'osx', 'pdf', 'ps', 'qt', 'qt4', 'qt5', 'svg', 'tk', 'widget', 'wx']
    Configure matplotlib for interactive use with the default matplotlib
    backend.
--cache-size=<Int> (InteractiveShell.cache_size)
    Default: 1000
    Set the size of the output cache.  The default is 1000, you can change it
    permanently in your config file.  Setting it to 0 completely disables the
    caching system, and the minimum value accepted is 3 (if you provide a value
    less than 3, it is reset to 0 and a warning is issued).  This limit is
    defined because otherwise you'll spend more time re-flushing a too small
    cache than working

To see all available configurables, use `--help-all`

Examples
--------

    ipython --matplotlib       # enable matplotlib integration
    ipython --matplotlib=qt    # enable matplotlib integration with qt4 backend

    ipython --log-level=DEBUG  # set logging to DEBUG
    ipython --profile=foo      # start with profile foo

    ipython profile create foo # create profile foo w/ default config files
    ipython help profile       # show the help for the profile subcmd

    ipython locate             # print the path to the IPython directory
    ipython locate profile foo # print the path to the directory for profile `foo`

chenwx@chenwx:~ $ ipython3   
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: print('Hello world')
Hello world
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

## SciPy Organization

SciPy is organized into subpackages covering different scientific computing domains. These are summarized in the following table, refer to [Scipy (development version) Reference Guide](http://scipy.github.io/devdocs/):

| Subpackage | Description |
| :--------- | :---------- |
| [scipy.cluster](https://docs.scipy.org/doc/scipy/reference/cluster.html) | Clustering algorithms |
| [scipy.constants](https://docs.scipy.org/doc/scipy/reference/constants.html) | Physical and mathematical constants |
| [scipy.fftpack](https://docs.scipy.org/doc/scipy/reference/fftpack.html) | Fast Fourier Transform routines |
| [scipy.integrate](https://docs.scipy.org/doc/scipy/reference/integrate.html) | Integration and ordinary differential equation solvers |
| [scipy.interpolate](https://docs.scipy.org/doc/scipy/reference/interpolate.html) | Interpolation and smoothing splines |
| [scipy.io](https://docs.scipy.org/doc/scipy/reference/io.html) | Input and Output |
| [scipy.linalg](https://docs.scipy.org/doc/scipy/reference/linalg.html) | Linear algebra |
| [scipy.misc](https://docs.scipy.org/doc/scipy/reference/misc.html) | Various utilities that don’t have another home. |
| [scipy.ndimage](https://docs.scipy.org/doc/scipy/reference/ndimage.html) | N-dimensional image processing |
| [scipy.odr](https://docs.scipy.org/doc/scipy/reference/odr.html) | Orthogonal distance regression |
| [scipy.optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html) | Optimization and root-finding routines |
| [scipy.signal](https://docs.scipy.org/doc/scipy/reference/signal.html) | Signal processing |
| [scipy.sparse](https://docs.scipy.org/doc/scipy/reference/sparse.html) | Sparse matrices and associated routines |
| [scipy.spatial](https://docs.scipy.org/doc/scipy/reference/spatial.html) | Spatial data structures and algorithms |
| [scipy.special](https://docs.scipy.org/doc/scipy/reference/special.html) | Special functions |
| [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html) | Statistical distributions and functions |

<p/>

SciPy sub-packages need to be imported separately, for example:

```
>>> from scipy import linalg, optimize
```

Because of their ubiquitousness, some of the functions in these subpackages are also made available in the **scipy** namespace to ease their use in interactive sessions and programs. In addition, many basic array functions from **numpy** are also available at the top-level of the scipy package. Before looking at the sub-packages individually, we will first look at some of these common functions.

**Finding Documentation**

SciPy and NumPy have documentation versions in both HTML and PDF format available at [here](https://docs.scipy.org/), that cover nearly all available functionality. However, this documentation is still work-in-progress and some parts may be incomplete or sparse. As we are a volunteer organization and depend on the community for growth, your participation - everything from providing feedback to improving the documentation and code - is welcome and actively encouraged.

Python's documentation strings are used in SciPy for on-line documentation. There are two methods for reading them and getting help. One is Python's command help in the **pydoc** module. Entering this command with no arguments (i.e. ```>>> help```) launches an interactive help session that allows searching through the keywords and modules available to all of Python. Secondly, running the command ```help(obj)``` with an object as the argument displays that object's calling signature, and documentation string.

```
chenwx@chenwx:~ $ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> help
Type help() for interactive help, or help(object) for help about object.
>>>
>>> from scipy import signal
>>>
>>> help()

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help>
help> scipy.signal
Help on package scipy.signal in scipy:

NAME
    scipy.signal

DESCRIPTION
    =======================================
    Signal processing (:mod:`scipy.signal`)
    =======================================

    Convolution
    ===========
    ...

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>>
>>> help(signal)
Help on package scipy.signal in scipy:

NAME
    scipy.signal

DESCRIPTION
    =======================================
    Signal processing (:mod:`scipy.signal`)
    =======================================

    Convolution
    ===========
    ...
```

The **pydoc** method of help is sophisticated but uses a pager to display the text. Sometimes this can interfere with the terminal you are running the interactive session within. A numpy/scipy-specific help system is also available under the command ```numpy.info```. The signature and documentation string for the object passed to the help command are printed to standard output (or to a writeable object passed as the third argument). The second keyword argument of numpy.info defines the maximum width of the line for printing. If a module is passed as the argument to help then a list of the functions and classes defined in that module is printed. For example:

```
>>> import numpy as np
>>> import matplotlib as mpl
>>> import matplotlib.pyplot as plt
>>> from scipy import linalg, optimize

>>> np.info(optimize.fmin)
 fmin(func, x0, args=(), xtol=0.0001, ftol=0.0001, maxiter=None, maxfun=None,
      full_output=0, disp=1, retall=0, callback=None)

Minimize a function using the downhill simplex algorithm.

Parameters
----------
func : callable func(x,*args)
    The objective function to be minimized.
x0 : ndarray
    Initial guess.
args : tuple
    Extra arguments passed to func, i.e. ``f(x,*args)``.
callback : callable
    Called after each iteration, as callback(xk), where xk is the
    current parameter vector.

Returns
-------
xopt : ndarray
    Parameter that minimizes function.
fopt : float
    Value of function at minimum: ``fopt = func(xopt)``.
iter : int
    Number of iterations performed.
funcalls : int
    Number of function calls made.
warnflag : int
    1 : Maximum number of function evaluations made.
    2 : Maximum number of iterations reached.
allvecs : list
    Solution at each iteration.

Other parameters
----------------
xtol : float
    Relative error in xopt acceptable for convergence.
ftol : number
    Relative error in func(xopt) acceptable for convergence.
maxiter : int
    Maximum number of iterations to perform.
maxfun : number
    Maximum number of function evaluations to make.
full_output : bool
    Set to True if fopt and warnflag outputs are desired.
disp : bool
    Set to True to print convergence messages.
retall : bool
    Set to True to return list of solutions at each iteration.

Notes
-----
Uses a Nelder-Mead simplex algorithm to find the minimum of function of
one or more variables.
```

Another useful command is ```dir```, which can be used to look at the namespace of a module or package.

```
chenwx@chenwx:~ $ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>   
>>> import scipy
>>> dir(scipy)
['ALLOW_THREADS', 'AxisError', 'BUFSIZE', 'CLIP', 'ComplexWarning', 'DataSource', 'ERR_CALL', 'ERR_DEFAULT', 'ERR_IGNORE', 'ERR_LOG', 'ERR_PRINT', 'ERR_RAISE', 'ERR_WARN', 'FLOATING_POINT_SUPPORT', 'FPE_DIVIDEBYZERO', 'FPE_INVALID', 'FPE_OVERFLOW', 'FPE_UNDERFLOW', 'False_', 'Inf', 'Infinity', 'LowLevelCallable', 'MAXDIMS', 'MAY_SHARE_BOUNDS', 'MAY_SHARE_EXACT', 'MachAr', 'ModuleDeprecationWarning', 'NAN', 'NINF', 'NZERO', 'NaN', 'PINF', 'PZERO', 'RAISE', 'RankWarning', 'SHIFT_DIVIDEBYZERO', 'SHIFT_INVALID', 'SHIFT_OVERFLOW', 'SHIFT_UNDERFLOW', 'ScalarType', 'TooHardError', 'True_', 'UFUNC_BUFSIZE_DEFAULT', 'UFUNC_PYVALS_NAME', 'VisibleDeprecationWarning', 'WRAP', '_UFUNC_API', '__SCIPY_SETUP__', '__all__', '__builtins__', '__cached__', '__config__', '__doc__', '__file__', '__loader__', '__name__', '__numpy_version__', '__package__', '__path__', '__spec__', '__version__', '_add_newdoc_ufunc', '_arg', '_distributor_init', '_lib', 'absolute', 'absolute_import', 'add', 'add_docstring', 'add_newdoc', 'add_newdoc_ufunc', 'alen', 'all', 'allclose', 'alltrue', 'amax', 'amin', 'angle', 'any', 'append', 'apply_along_axis', 'apply_over_axes', 'arange', 'arccos', 'arccosh', 'arcsin', 'arcsinh', 'arctan', 'arctan2', 'arctanh', 'argmax', 'argmin', 'argpartition', 'argsort', 'argwhere', 'around', 'array', 'array2string', 'array_equal', 'array_equiv', 'array_repr', 'array_split', 'array_str', 'asanyarray', 'asarray', 'asarray_chkfinite', 'ascontiguousarray', 'asfarray', 'asfortranarray', 'asmatrix', 'asscalar', 'atleast_1d', 'atleast_2d', 'atleast_3d', 'average', 'bartlett', 'base_repr', 'binary_repr', 'bincount', 'bitwise_and', 'bitwise_not', 'bitwise_or', 'bitwise_xor', 'blackman', 'block', 'bmat', 'bool8', 'bool_', 'broadcast', 'broadcast_arrays', 'broadcast_to', 'busday_count', 'busday_offset', 'busdaycalendar', 'byte', 'byte_bounds', 'bytes0', 'bytes_', 'c_', 'can_cast', 'cast', 'cbrt', 'cdouble', 'ceil', 'cfloat', 'char', 'character', 'chararray', 'choose', 'clip', 'clongdouble', 'clongfloat', 'column_stack', 'common_type', 'compare_chararrays', 'complex128', 'complex256', 'complex64', 'complex_', 'complexfloating', 'compress', 'concatenate', 'conj', 'conjugate', 'convolve', 'copy', 'copysign', 'copyto', 'corrcoef', 'correlate', 'cos', 'cosh', 'count_nonzero', 'cov', 'cross', 'csingle', 'ctypeslib', 'cumprod', 'cumproduct', 'cumsum', 'datetime64', 'datetime_as_string', 'datetime_data', 'deg2rad', 'degrees', 'delete', 'deprecate', 'deprecate_with_doc', 'diag', 'diag_indices', 'diag_indices_from', 'diagflat', 'diagonal', 'diff', 'digitize', 'disp', 'divide', 'division', 'divmod', 'dot', 'double', 'dsplit', 'dstack', 'dtype', 'e', 'ediff1d', 'einsum', 'einsum_path', 'emath', 'empty', 'empty_like', 'equal', 'errstate', 'euler_gamma', 'exp', 'exp2', 'expand_dims', 'expm1', 'extract', 'eye', 'fabs', 'fastCopyAndTranspose', 'fft', 'fill_diagonal', 'find_common_type', 'finfo', 'fix', 'flatiter', 'flatnonzero', 'flexible', 'flip', 'fliplr', 'flipud', 'float128', 'float16', 'float32', 'float64', 'float_', 'float_power', 'floating', 'floor', 'floor_divide', 'fmax', 'fmin', 'fmod', 'format_float_positional', 'format_float_scientific', 'format_parser', 'frexp', 'frombuffer', 'fromfile', 'fromfunction', 'fromiter', 'frompyfunc', 'fromregex', 'fromstring', 'full', 'full_like', 'fv', 'gcd', 'generic', 'genfromtxt', 'geomspace', 'get_array_wrap', 'get_include', 'get_printoptions', 'getbufsize', 'geterr', 'geterrcall', 'geterrobj', 'gradient', 'greater', 'greater_equal', 'half', 'hamming', 'hanning', 'heaviside', 'histogram', 'histogram2d', 'histogram_bin_edges', 'histogramdd', 'hsplit', 'hstack', 'hypot', 'i0', 'identity', 'ifft', 'iinfo', 'imag', 'in1d', 'index_exp', 'indices', 'inexact', 'inf', 'info', 'infty', 'inner', 'insert', 'int0', 'int16', 'int32', 'int64', 'int8', 'int_', 'int_asbuffer', 'intc', 'integer', 'interp', 'intersect1d', 'intp', 'invert', 'ipmt', 'irr', 'is_busday', 'isclose', 'iscomplex', 'iscomplexobj', 'isfinite', 'isfortran', 'isin', 'isinf', 'isnan', 'isnat', 'isneginf', 'isposinf', 'isreal', 'isrealobj', 'isscalar', 'issctype', 'issubclass_', 'issubdtype', 'issubsctype', 'iterable', 'ix_', 'kaiser', 'kron', 'lcm', 'ldexp', 'left_shift', 'less', 'less_equal', 'lexsort', 'linspace', 'little_endian', 'load', 'loads', 'loadtxt', 'log', 'log10', 'log1p', 'log2', 'logaddexp', 'logaddexp2', 'logical_and', 'logical_not', 'logical_or', 'logical_xor', 'logn', 'logspace', 'long', 'longcomplex', 'longdouble', 'longfloat', 'longlong', 'lookfor', 'ma', 'mafromtxt', 'mask_indices', 'mat', 'math', 'matmul', 'matrix', 'maximum', 'maximum_sctype', 'may_share_memory', 'mean', 'median', 'memmap', 'meshgrid', 'mgrid', 'min_scalar_type', 'minimum', 'mintypecode', 'mirr', 'mod', 'modf', 'moveaxis', 'msort', 'multiply', 'nan', 'nan_to_num', 'nanargmax', 'nanargmin', 'nancumprod', 'nancumsum', 'nanmax', 'nanmean', 'nanmedian', 'nanmin', 'nanpercentile', 'nanprod', 'nanquantile', 'nanstd', 'nansum', 'nanvar', 'nbytes', 'ndarray', 'ndenumerate', 'ndfromtxt', 'ndim', 'ndindex', 'nditer', 'negative', 'nested_iters', 'newaxis', 'nextafter', 'nonzero', 'not_equal', 'nper', 'npv', 'number', 'obj2sctype', 'object0', 'object_', 'ogrid', 'ones', 'ones_like', 'outer', 'packbits', 'pad', 'partition', 'percentile', 'pi', 'piecewise', 'place', 'pmt', 'poly', 'poly1d', 'polyadd', 'polyder', 'polydiv', 'polyfit', 'polyint', 'polymul', 'polysub', 'polyval', 'positive', 'power', 'ppmt', 'print_function', 'printoptions', 'prod', 'product', 'promote_types', 'ptp', 'put', 'put_along_axis', 'putmask', 'pv', 'quantile', 'r_', 'rad2deg', 'radians', 'rand', 'randn', 'random', 'rank', 'rate', 'ravel', 'ravel_multi_index', 'real', 'real_if_close', 'rec', 'recarray', 'recfromcsv', 'recfromtxt', 'reciprocal', 'record', 'remainder', 'repeat', 'require', 'reshape', 'resize', 'result_type', 'right_shift', 'rint', 'roll', 'rollaxis', 'roots', 'rot90', 'round_', 'row_stack', 's_', 'safe_eval', 'save', 'savetxt', 'savez', 'savez_compressed', 'sctype2char', 'sctypeDict', 'sctypeNA', 'sctypes', 'searchsorted', 'select', 'set_numeric_ops', 'set_printoptions', 'set_string_function', 'setbufsize', 'setdiff1d', 'seterr', 'seterrcall', 'seterrobj', 'setxor1d', 'shape', 'shares_memory', 'short', 'show_config', 'show_numpy_config', 'sign', 'signbit', 'signedinteger', 'sin', 'sinc', 'single', 'singlecomplex', 'sinh', 'size', 'sometrue', 'sort', 'sort_complex', 'source', 'spacing', 'split', 'sqrt', 'square', 'squeeze', 'stack', 'std', 'str0', 'str_', 'string_', 'subtract', 'sum', 'swapaxes', 'take', 'take_along_axis', 'tan', 'tanh', 'tensordot', 'test', 'tile', 'timedelta64', 'trace', 'tracemalloc_domain', 'transpose', 'trapz', 'tri', 'tril', 'tril_indices', 'tril_indices_from', 'trim_zeros', 'triu', 'triu_indices', 'triu_indices_from', 'true_divide', 'trunc', 'typeDict', 'typeNA', 'typecodes', 'typename', 'ubyte', 'ufunc', 'uint', 'uint0', 'uint16', 'uint32', 'uint64', 'uint8', 'uintc', 'uintp', 'ulonglong', 'unicode', 'unicode_', 'union1d', 'unique', 'unpackbits', 'unravel_index', 'unsignedinteger', 'unwrap', 'ushort', 'vander', 'var', 'vdot', 'vectorize', 'version', 'void', 'void0', 'vsplit', 'vstack', 'where', 'who', 'zeros', 'zeros_like']
```

## Signal Processing via SciPy

* [Python Scientific Lecture Notes](http://scipy-lectures.org/index.html)
* [Fourier Transforms (scipy.fftpack)](https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html)
* [Signal Processing (scipy.signal)](https://docs.scipy.org/doc/scipy/reference/signal.html)
* [Signal Processing via SciPy](https://scipy-cookbook.readthedocs.io/items/idx_signal_processing.html)

For brevity and convenience, we will often assume that the main packages (numpy, scipy, and matplotlib) have been imported as:

```
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
```

# R

[R](https://www.r-project.org/) is a programming language and free software environment for statistical computing and graphics supported by the R Foundation for Statistical Computing. The R language is widely used among statisticians and data miners for developing statistical software and data analysis. Polls, data mining surveys, and studies of scholarly literature databases show substantial increases in popularity in recent years. As of May 2019, R ranks 21st in the [TIOBE index](https://www.tiobe.com/tiobe-index/), a measure of popularity of programming languages.

A GNU package, source code for the R software environment is written primarily in C, Fortran and R itself, and is freely available under the GNU General Public License. Pre-compiled binary versions are provided for various operating systems. Although R has a command line interface, there are several graphical user interfaces, such as [RStudio](https://www.rstudio.com/), an integrated development environment.

# Mathematica

[Wolfram Mathematica](https://www.wolfram.com/mathematica/) is a modern technical computing system spanning most areas of technical computing - including neural networks, machine learning, image processing, geometry, data science, visualizations, and others. The system is used in many technical, scientific, engineering, mathematical, and computing fields. It was conceived by *Stephen Wolfram* and is developed by Wolfram Research of Champaign, Illinois. The Wolfram Language is the programming language used in Mathematica.[9]

# FreeMat

[FreeMat](http://freemat.sourceforge.net/) is a free environment for rapid engineering and scientific prototyping and data processing. It is similar to commercial systems such as MATLAB from Mathworks, and IDL from Research Systems, but is Open Source. FreeMat is available under the GPL license.

# GNU Octave

[GNU Octave](https://www.gnu.org/software/octave/) is a high-level language primarily intended for numerical computations. It is typically used for such problems as solving linear and nonlinear equations, numerical linear algebra, statistical analysis, and for performing other numerical experiments. It may also be used as a batch-oriented language for automated data processing.

The current version of Octave executes in a graphical user interface (GUI). The GUI hosts an Integrated Development Environment (IDE) which includes a code editor with syntax highlighting, built-in debugger, documentation browser, as well as the interpreter for the language itself. A command-line interface (CLI) for Octave is also available.

GNU Octave is freely redistributable software. You may redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation. The GPL is included in this manual, see Copying.

[This manual](https://octave.org/doc/interpreter/) provides comprehensive documentation on how to install, run, use, and extend GNU Octave. Additional chapters describe how to report bugs and help contribute code.

# Gnuplot

[Gnuplot](http://www.gnuplot.info/) is a portable command-line driven graphing utility for Linux, OS/2, MS Windows, OSX, VMS, and many other platforms. The source code is copyrighted but freely distributed (i.e., you don't have to pay for it). It was originally created to allow scientists and students to visualize mathematical functions and data interactively, but has grown to support many non-interactive uses such as web scripting. It is also used as a plotting engine by third-party applications like Octave. Gnuplot has been supported and under active development since 1986.

# Gmsh

[Gmsh](http://gmsh.info/) is a free 3D finite element mesh generator with a built-in CAD engine and post-processor. Its design goal is to provide a fast, light and user-friendly meshing tool with parametric input and advanced visualization capabilities. Gmsh is built around four modules: geometry, mesh, solver and post-processing. The specification of any input to these modules is done either interactively using the graphical user interface, in ASCII text files using Gmsh's own scripting language (.geo files), or using the C++, C, Python or Julia API.

# Rebol

[Rebol](http://www.rebol.com/) is a lightweight programming language. Rebol's unique design makes it more productive than other language technologies. The leverage comes from Rebol's unique blend of domain specific sub-languages called dialects.

# References

* [MATLAB](https://ww2.mathworks.cn/en/products/matlab.html)
* [Scilab](https://www.scilab.org/)
* [SciPy](https://www.scipy.org/)
* [R](https://www.r-project.org/)
* [Mathematica](https://www.wolfram.com/mathematica/)
* [FreeMat](http://freemat.sourceforge.net/)
* [GNU Octave](https://www.gnu.org/software/octave/)
* [Gnuplot](http://www.gnuplot.info/)
* [Gmsh](http://gmsh.info/)
* [Rebol](http://www.rebol.com/)

* [List of numerical-analysis software](https://en.wikipedia.org/wiki/List_of_numerical-analysis_software)
* [Comparison of numerical-analysis software](https://en.wikipedia.org/wiki/Comparison_of_numerical-analysis_software)
* [Comparison of statistical packages](https://en.wikipedia.org/wiki/Comparison_of_statistical_packages)
