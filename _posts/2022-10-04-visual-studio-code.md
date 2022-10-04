---
layout: post
title: "Visual Studio Code"
tag: Tools
toc: true
---

This article introduces some useful configurations of Visual Studio Code.

<!--more-->

# Enable Command Center

Right click on ```Menu Bar``` and select ```Command Center``` to enable it:

![vscode-01](/assets/vscode_01.png)

# Export / Import Settings Profiles

In ```Command Center```, input ```> export``` and select ```Settings Profiles: Export...``` to export current settings to specified file:

![vscode-02](/assets/vscode_02.png)

In ```Command Center```, input ```> import``` and select ```Settings Profiles: Import...``` to import settings from specified file:

![vscode-03](/assets/vscode_03.png)

# Show Line Numbers in Search Results

Select ```Settings > Search > Show Line Numbers```:

![vscode-04](/assets/vscode_04.png)

# Disable Error Squiggles

Set ```Settings > C/C++ > C_Cpp: Error Squiggles``` to ```Disabled```:

![vscode-05](/assets/vscode_05.png)

# Search

Use ```Show Search Modes...``` in right side of ```Command Center```:

![vscode-06](/assets/vscode_06.png)

![vscode-07](/assets/vscode_07.png)

to:

| Options | Comments |
| :------ | :------- |
| ```... Go to File``` | Search specified file |
| ```: Go to Line/Column``` | Go to specified line in current file |
| ```@ Go to Symbol in Editor``` | Search specified symbol in current file |
| ```# Go to Symbol in Workspace``` | Search specified symbol in workspace |

![vscode-08](/assets/vscode_08.png)

Search in current file:

* ```Ctrl + F```, then input keywords
* Select keywords in current file, then ```Ctrl + F```

Search in workspace:

* ```Ctrl + Shift + F```, then input keywords
* Select keywords in current file, then ```Ctrl + Shift + F```
* Select keywords in current file, then select ```Find All References``` in right-click menu

# Extensions

* Drawio
* Markdown All in One

# References

* [Visual Studio Code](https://code.visualstudio.com/)
