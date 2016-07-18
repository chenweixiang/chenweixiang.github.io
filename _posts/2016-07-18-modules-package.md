---
layout: post
title: "Modules: Dynamic Modify User's Environment"
tag: Linux
toc: true
---

This article introduces the **Environment Modules** package, which provides for the dynamic modification of the user's environment via *modulefiles*.

<!--more-->

# Overview

The Environment Modules package provides for the dynamic modification of a user's environment via *modulefiles*.

Each *modulefile* contains the information needed to configure the shell for an application. Once the Modules package is initialized, the environment can be modified on a per-module basis using the module command which interprets *modulefiles*. Typically *modulefiles* instruct the module command to alter or set shell environment variables such as PATH, MANPATH, etc. *modulefiles* may be shared by many users on a system and users may have their own collection to supplement or replace the shared *modulefiles*.

Modules can be **loaded** and **unloaded** dynamically and atomically, in an clean fashion. All popular shells are supported, including *bash*, *ksh*, *zsh*, *sh*, *csh*, *tcsh*, as well as some scripting languages such as *perl* and *python*.

Modules are useful in managing different versions of applications. Modules can also be bundled into metamodules that will load an entire suite of different applications.

# module Command

**module** is a user interface to the Modules package. The Modules package provides for the dynamic modification of the user's environment via *modulefiles*.

Each *modulefile* contains the information needed to configure the shell for an application. Once the Modules package is initialized, the environment can be modified on a per-module basis using the **module** command which interprets *modulefiles*. Typically *modulefiles* instruct the **module** command to alter or set shell environment variables such as PATH, MANPATH, etc. *modulefiles* may be shared by many users on a system and users may have their own collection to supplement or replace the shared *modulefiles*.

The *modulefiles* are added to and removed from the current environment by the user. The environment changes contained in a *modulefile* can be summarized through the **module** command as well. If no arguments are given, a summary of the module usage and *sub-commands* are shown.

**module** command syntax:

```
module [ switches ] [ sub-command ] [ sub-command-args ]  
```

## Package Initialization

The Modules package and the **module** command are initialized when a shell-specific initialization script is sourced into the shell. The script creates the **module** command, either as an *alias* or shell function, creates Modules environment variables, and if enabled to do so, a snapshot of the environment is saved as either (if BEGINENV=1) *$HOME/.modulesbeginenv* or (if BEGINENV=99) whatever *$MODULESBEGINENV* points to.

The module alias or function executes the *modulecmd* program and has the shell evaluate the command's output. The first argument to *modulecmd* specifies the type of shell.

The initialization scripts are kept in *$MODULESHOME/init/\<shell\>* where *\<shell\>* is the name of the sourcing shell. The *sh*, *csh*, *tcsh*, *bash*, *ksh*, and *zsh* shells are supported by *modulecmd*. In addition, python and perl *shells* are supported, which writes the environment changes to *stdout* as python or perl code.

## modulecmd Startup

Upon invocation *modulecmd* sources rc files which contain global, user and modulefile specific setups. These files are interpreted as modulefiles. See modulefile(4) for detailed information.

Upon invocation of modulecmd module RC files are sourced in the following order:

* Global RC file as specified by *${MODULERCFILE}* or *${MODULESHOME}/etc/rc*
* User specific module RC file *${HOME}/.modulerc*
* All *.modulerc* and *.version* files found during *modulefile* seeking.

## switches

* **--help, -H**

    Give some helpful usage information, and terminates the command.

* **--version, -V**

    Lists the current version of the module command, and some configured option values. The command then terminates without further processing.

* **--force, -f**

    Force active dependency resolution. This will result in modules found on a *prereq* command inside a module file being load automatically. Unloading module files using this switch will result in all required modules which have been loaded automatically using the ```-f``` switch being unload. This switch is experimental at the moment.

* **--terse, -t**

    Display sub-commands *avail* and *list* output in short format.

* **--long, -l**

    Display sub-commands *avail* and *list* output in long format.

* **--human, -h**

    Display short output of the sub-commands *avail* and *list* commands in human readable format.

* **--verbose, -v**

    Enable verbose messages during module command execution.

* **--silent, -s**

    Disable verbose messages. Redirect *stderr* to */dev/null* if *stderr* is found not to be a *tty*. This is a useful option for module commands being written into *.cshrc*, *.login* or *.profile* files, because some remote shells (*rsh*) and remote execution commands (like *rdist*) get confused if there is output on *stderr*.

* **--create, -c**

    Create caches for *module avail* and *module apropos*. You must be granted write access to the *${MODULEHOME}/modulefiles/* directory if you try to invoke module with the ```-c``` option.

* **--icase, -i**

    Case insensitive module parameter evaluation. Currently only implemented for the *module apropos* command.

* **--userlvl \<lvl\>, -u \<lvl\>**

    Set the user level to the specified value. The argument of this option may be one of:

    * **novice**, nov Novice
    * **expert**, exp Experienced module user
    * **advanced**, adv Advanced module user
    <p/>

## sub-commands

* **help [modulefile...]**

    Print the usage of each sub-command. If an argument is given, print the Module-specific help information for the *modulefile*(s).

* **list**

    List loaded modules.

* **avail [path...]**

    List all available *modulefiles* in the current **MODULEPATH**. All directories in the **MODULEPATH** are recursively searched for files containing the *modulefile* magic cookie. If an *argument* is given, then each directory in the MODULEPATH is searched for *modulefiles* whose pathname match the argument. Multiple versions of an application can be supported by creating a subdirectory for the application containing *modulefiles* for each version.

* **show modulefile...**
  **display modulefile...**

    Display information about one or more *modulefiles*. The *display* sub-command will list the full path of the *modulefile*(s) and all (or most) of the environment changes the *modulefile*(s) will make if loaded. (It will not display any environment changes found within conditional statements.)

* **add modulefile...**
  **load modulefile...**

    Load *modulefile*(s) into the shell environment.

* **rm modulefile...**
  **unload modulefile...**

    Remove *modulefile*(s) from the shell environment.

* **clear**

    Force the Modules package to believe that no modules are currently loaded.

* **purge**

    Unload all loaded *modulefiles*.

* **swap [modulefile1] modulefile2**
  **switch [modulefile1] modulefile2**

    Switch loaded *modulefile1* with *modulefile2*. If *modulefile1* is not specified, then it is assumed to be the currently loaded module with the same root name as *modulefile2*.

* **use [-a|--append] directory...**

    Prepend one or more directories to the **MODULEPATH** environment variable. The *--append* flag will append the directory to **MODULEPATH**.

* **unuse directory...**

    Remove one or more directories from the **MODULEPATH** environment variable.

* **update**

    Attempt to reload all loaded *modulefiles*. The environment will be reconfigured to match the environment saved in *${HOME}/.modulesbeginenv* (if BEGINENV=1) or the file pointed at by *$MODULESBEGINEV* (if BEGINENV=99) and the *modulefiles* will be reloaded. This is only valid if modules was configured with *--enable-beginenv* (which defines BEGINENV), otherwise this will cause a warning. update will only change the environment variables that the *modulefiles* set.

* **refresh**

    Force a refresh of all non-persistent components of currently loaded modules. This should be used on derived shells where aliases need to be reinitialized but the environment variables have already been set by the currently loaded modules.

* **whatis [modulefile...]**

    Display the information set up by the module-whatis commands inside the specified *modulefile*(s). If no *modulefile* is specified, all *whatis* lines will be shown.

* **apropos string**
  **keyword string**

    Seeks through the *whatis* informations of all *modulefiles* for the specified string. All module-whatis informations matching the string will be displayed.

* **initlist**

    List all of the *modulefiles* loaded from the shell's initialization file.

* **initadd modulefile...**

    Add *modulefile*(s) to the shell's initialization file in the user's home directory. The startup files checked (in order) are:

    * csh - .modules, .cshrc(.ext), .csh_variables, and .login(.ext)
    * tcsh - .modules, .tcshrc, .cshrc(.ext), .csh_variables, and .login(.ext)
    * sh and ksh - .modules, .profile(.ext), and .kshenv(.ext)
    * bash - .modules, .bash_profile, .bash_login, .profile(.ext), and .bashrc(.ext)
    * zsh - .modules, .zcshrc(.ext), .zshenv(.ext), and .zlogin(.ext)
    <p/>

    If a *module load* line is found in any of these files, the *modulefile*(s) is(are) appended to any existing list of *modulefiles*. The *module load* line must be located in at least one of the files listed above for any of the *init* sub-commands to work properly. If the *module load* line is found in multiple shell initialization files, all of the lines are changed.

* **initrm modulefile...**

    Remove *modulefile*(s) from the shell's initialization files.

* **initclear**

    Clear all of the *modulefiles* from the shell's initialization files.

* **initprepend modulefile [modulefile...]**

    Does the same as *initadd* but prepends the given modules to the beginning of the list.

* **initswitch modulefile1 modulefile2**

    Switch *modulefile1* with *modulefile2* in the shell's initialization files.

# modulefiles

**modulefiles** are written in the Tool Command Language (Tcl) and are interpreted by **modulecmd**. *modulefiles* can use conditional statements. Thus the effect a *modulefile* will have on the environment may change depending upon the current state of the environment.

Environment variables are unset when unloading a *modulefile*. Thus, it is possible to **load** a *modulefile* and then **unload** it without having the environment variables return to their prior state.

Refer to [Manual page for the modulefile commands](http://modules.sourceforge.net/man/modulefile.html) for details.

# Environment

* **MODULESHOME**

    The location of the master Modules package file directory containing *module* command initialization scripts, the executable program **modulecmd**, and a directory containing a collection of master **modulefiles**.

* **MODULEPATH**

    The path that the **module** command searches when looking for *modulefiles*. Typically, it is set to a default value by the bootstrap procedure. **MODULEPATH** can be set using *module use* or by the module initialization script to search group or personal *modulefile* directories before or after the master *modulefile* directory.

* **LOADEDMODULES**

    A colon separated list of all loaded *modulefiles*.

* **\_LMFILES\_**

    A colon separated list of the full pathname for all loaded *modulefiles*.

* **MODULESBEGINENV**

    If modules has been configured (BEGINENV=99) to test for this environment variable, then if it exists, it is the name of the file to store the the initial shell environment. This environment variable will have embedded environment variables unrolled to one level. The contents of this variable is only used the first time *modules* is invoked.

* **\_MODULESBEGINENV\_**

    The filename of the file containing the initialization environment snapshot.

# Files

* **/usr/local/Modules/3.2.7**

    The MODULESHOME directory.

* **${MODULESHOME}/etc/rc**

    The system-wide *modules rc* file. The location of this file can be changed using the **MODULERCFILE** environment variable as described above.

* **${HOME}/.modulerc**

    The user specific *modules rc* file.

* **${MODULESHOME}/modulefiles**

    The directory for system-wide *modulefiles*. The location of the directory can be changed using the **MODULEPATH** environment variable as described above.

* **${MODULESHOME}/bin/modulecmd**

    The *modulefile* interpreter that gets executed upon each invocation of module.

* **${MODULESHOME}/init/\<shell\>**

    The Modules package initialization file sourced into the user's environment.

* **${MODULEPATH}/.moduleavailcache**

    File containing the cached list of all *modulefiles* for each directory in the **MODULEPATH** (only when the avail cache is enabled via the configure option ```--enable-cache``` which sets CACHE_AVAIL).

* **${MODULEPATH}/.moduleavailcachedir**

    File containing the names and modification times for all sub-directories with an avail cache.

* **${HOME}/.modulesbeginenv**

    A snapshot of the user's environment taken at Module initialization. This information is used by the module update sub-command (if BEGINENV=1).

* **$MODULESBEGINENV**
    If this defines a valid filename, it serves the same purpose as above (if BEGINENV=99).

# References

* [Environment Modules Project](http://modules.sourceforge.net/)
* [Manual page for the module command](http://modules.sourceforge.net/man/module.html)
* [Manual page for the modulefile commands](http://modules.sourceforge.net/man/modulefile.html)
* [Modules: Providing a Flexible User Environment](http://modules.sourceforge.net/docs/Modules-Paper.pdf)
* [Abstract Yourself With Modules](http://modules.sourceforge.net/docs/absmod.pdf)
