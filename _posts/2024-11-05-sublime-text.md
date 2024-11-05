---
layout: post
title: "Sublime Text"
tag: Tools
toc: true
---

This article introduces the usage of Sublime Text.

<!--more-->

# Settings

Preferences.sublime-settings

```
{
	"color_scheme": "GitHub Light.sublime-color-scheme",
	"font_size": 10,
	"line_numbers": true,
	"tab_size": 4,
	"translate_tabs_to_spaces": true,
	"word_wrap": "false",
	"auto_match_enabled": true,
	"highlight_line": true,
	"highlight_line_number": true,
	// "find_selected_text": true,
	"theme": "GitHub Light.sublime-theme",
	"file_tab_style": "rounded",
	"highlight_modified_tabs": true,
	"enable_tab_scrolling": false,
	"show_encoding": true,
	"hot_exit": "disabled",
	"open_files_in_new_window": "always",
	"show_full_path": true,
	"index_files": false,
	"ignored_packages": ["Vintage",],
}
```

# Install Package Control

Press buttons ```Ctrl + Shift + P```, then input ```Install Package Control``` and press ```Return``` to install Package Control.

Restart Sublime Text.

# Install GitHub Theme

Preferences > Package Control > Install Package > GitHub Theme

Preferences > Select Theme... > GitHub Light

Preferences > Select Color Scheme... > GitHub Light

# Install Chain of Command

Preferences > Package Control > Install Package > Chain of Command

Preferences > Key Bindings

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

Select "Use Buffer" to show results in a new tab "Find Results".

Unselect "Use Buffer" to show results in the tab below current file.

# References

* [Sublime Text](https://www.sublimetext.com/)
