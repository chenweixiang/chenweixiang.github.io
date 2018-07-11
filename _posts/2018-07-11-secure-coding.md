---
layout: post
title: "Secure Coding"
tag: Programming
toc: true
---

This article introduces the secure coding.

<!--more-->

# Secure Coding related Taxonomies

* [Seven Pernicious Kingdoms: A Taxonomy of Software Security Errors](/docs/Seven_Pernicious_Kingdoms_A_Taxonomy_of_Software_Security_Errors.pdf)
* [A Taxonmy of Computer Program Security Flaws](/docs/A_Taxonmy_of_Computer_Program_Security_Flaws.pdf)
* [A Taxonmy of Security Faults in the Unix Operating System](/docs/A_Taxonmy_of_Security_Faults_in_the_Unix_Operating_System.pdf)

# Code Analysis Tools

There are many different types of tools and technologies that can be used for improving the software security properties. This is done by pinpointing possible weaknesses. The following grouping of tools is quite common:

* [Static source analysis tools](#static-code-analysis-tools)
* [Dynamic analysis tools](#dynamic-analysis-tools)
* Tools for system hardening and fuzzy testing

These tools are mainly used in different phases of the software development life cycle. Static analysis is performed while software is designed, sometimes for code fragments that won't even compile. Dynamic analysis tools are run mainly in the test environment where the system under test is a "prototype version of production", i.e. a test environment. VA tools are used in the real environment, as they also verify issues with the system configuration. Note that there are test tools that cover partly multiple areas. For example the **CodeChecker** does static code analysis, but it also compiles the code and simulates it, thus performs checks that are dynamic by nature.

## Static Code Analysis Tools

**BitDefender**, together with researchers from Alexandru Ioan Cuza University, have done a study about static code analysis tools, and how the tools can find vulnerabilities in the C/C++ code. The analysis consists of e.g. CLANG, CppCheck and [CodeSonar](https://www.grammatech.com/products/codesonar), check [the study report](/docs/A_Comparison_of_Static_Analysis_Tools_for_Vulnerability_Detection_in_C_C++_Code.pdf).

* Wikipedia list of [static analysis tools](https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis)
* OWASP page for [static code analysis](https://www.owasp.org/index.php/Static_Code_Analysis)

## Dynamic Analysis Tools

# References

* [Seven Pernicious Kingdoms: A Taxonomy of Software Security Errors](/docs/Seven_Pernicious_Kingdoms_A_Taxonomy_of_Software_Security_Errors.pdf)
* [A Taxonmy of Computer Program Security Flaws](/docs/A_Taxonmy_of_Computer_Program_Security_Flaws.pdf)
* [A Taxonmy of Security Faults in the Unix Operating System](/docs/A_Taxonmy_of_Security_Faults_in_the_Unix_Operating_System.pdf)
* [CodeSonar](https://www.grammatech.com/products/codesonar)
* [Static Analysis Tools](https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis)
* [Static Code Analysis](https://www.owasp.org/index.php/Static_Code_Analysis)
