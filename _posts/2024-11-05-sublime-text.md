---
layout: post
title: "Sublime Text"
tag: Tools
toc: true
---

This article introduces the usage of Sublime Text.

<!--more-->

# Install Package Control

Press buttons ```Ctrl + Shift + P```, then input ```Install Package Control``` and enter ```Return``` to install Package Control.

Restart Sublime Text.

# Install GitHub Theme

```Preferences``` > ```Package Control``` > Input ```Install Package``` > Input ```GitHub Theme```

```Preferences``` > ```Select Theme...``` > Select ```GitHub Light```

```Preferences``` > ```Select Color Scheme...``` > Select ```GitHub Light```

# Install Chain of Command

```Preferences``` > ```Package Control``` > Input ```Install Package``` > Input ```Chain of Command```

```Preferences``` > ```Key Bindings``` > Input the following settings:

```
[
    {
        "keys": ["alt+f"],
        "command": "chain",
        "args": {
            "commands": [
                ["show_panel", {
                    "panel": "find_in_files",
                    "where": "<current file>",
                }],
            ]
        }
    }
]
```

Unselect ```Use Buffer``` to show results in the tab below current file.

Select ```Use Buffer``` to show results in a new tab ```Find Results```.

# Settings

```Preferences``` > ```Settings``` > Input the following settings in file ```Preferences.sublime-settings```:

```
{
	"font_size": 10,
	"line_numbers": true,
	"tab_size": 4,
	"translate_tabs_to_spaces": true,
	"word_wrap": "false",
	"auto_match_enabled": true,
	"highlight_line": true,
	"highlight_line_number": true,
	// "find_selected_text": true,
	"file_tab_style": "rounded",
	"highlight_modified_tabs": true,
	"enable_tab_scrolling": false,
	"show_encoding": true,
	"hot_exit": "disabled",
	"open_files_in_new_window": "always",
	"show_full_path": true,
	"index_files": false,
	"ignored_packages": ["Vintage"],
}
```

# References

* [Sublime Text](https://www.sublimetext.com/)
