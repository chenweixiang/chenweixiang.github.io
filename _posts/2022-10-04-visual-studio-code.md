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

# Seach: Exclude

![vscode-20](/assets/vscode_20.png)

# VSCode Remote-SSH

VSCode Remote-SSH from Windows to Linux Server:

1st, generate ```id_isa_<XXX>``` and ```id_isa_<XXX>.pub``` on Windows by executing the following commands in MobaXterm:

```
ssh-keygen -t rsa
```

2nd, copy the files ```id_isa_<XXX>``` and ```id_isa_<XXX>.pub``` to the folder ```C:\User\<Your-Account-on-Windows>\.ssh\``` on Windows.

3rd, change properties of the file ```id_isa_<XXX>``` on Windows. That's, keep your accout only in ```Group or user names``` field:

![vscode-10](/assets/vscode_10.png)

4th, copy content of the file ```id_isa_<XXX>.pub``` from Windows to the file ```/home/<Your-Account-on-Linux-Server>/.ssh/authorized_keys``` on Linux server.

5th, install VSCode extension ```Remote-SSH``` on Windows.

6th, add VSCode SSH configuration file ```C:\User\<Your-Account-on-Windows>\.ssh\config``` on Windows:

```
Host <Linux-Server-Name>
  HostName <Linux-Server-IP>
  User <Your-Account-on-Linux-Server>
  PreferredAuthentications publickey
  IdentityFile "C:\User\<Your-Account-on-Windows>\.ssh\id_rsa_XXX"
```

![vscode-11](/assets/vscode_11.png)

7th, to move the folder ```remote.SSH.serverInstallPath``` on a larger disk on Linux server, set it in VSCode settings ```remote.SSH.serverInstallPath``` on Windows:

![vscode-13](/assets/vscode_13.png)

8th, it is no need to input password anymore when VSCode on Windows connecting to the Linux server.

# Open Editors: Sort Order

![vscode-09](/assets/vscode_09.png)

# Remote-explorer: Folder Sort Order

![vscode-14](/assets/vscode_14.png)

# Fix Ctrl+Shift+F not work issue

与微软拼音输入法的简繁切换快捷键冲突，取消微软拼音输入法的简繁切换快捷键即可:

Win键 > 设置 > 时间和语言 > 语言 > 首选语言: 中文 > 选项 > 键盘: 微软拼音 > 选项 > 按键 > 快捷键: 简体/繁体中文输入切换

![vscode-12](/assets/vscode_12.png)

# Fix Go to Definition not work issue

Install extension **C/C++** to SSH remote:

![vscode-21](/assets/vscode_21.png)

Then, the **Go to Definition** can be used:

![vscode-22](/assets/vscode_22.png)

# Turn on Rulers

![vscode-15](/assets/vscode_15.png)

# Upload and download files

![vscode-16](/assets/vscode_16.png)

![vscode-17](/assets/vscode_17.png)

# Window: Title

![vscode-18](/assets/vscode_18.png)

![vscode-19](/assets/vscode_19.png)

# Extensions

* C/C++
* Remote Development
* GitLens

* Drawio
* Markdown All in One

![vscode-23](/assets/vscode_23.png)

# References

* [Visual Studio Code](https://code.visualstudio.com/)
