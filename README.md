# [x]it! for Sublime Text

This Sublime Package provides syntax-highlighting, shortcuts, and auto-completions for [[x]it!](https://xit.jotaen.net)

> ⚠️ **This package is not yet available via the Sublime Packager manager!**
> For now, you have to install it manually:
> 1. [Download this repository](https://github.com/jotaen/xit/archive/refs/heads/main.zip)
> 2. Unpack the downloaded `.zip` file
> 3. Rename the unzipped folder from `xit-main` to `xit`
> 4. In the Sublime Menu, click `Preferences` → `Browse Packages`
> 5. Move the `xit` folder to that location

## Features

- Syntax highlighting
	+ Provides meaningful colours for the Monokai and Mariana themes
- Shortcut commands for toggling the item status
- Smart completions for due dates
	+ Type e.g. `5w` and have auto-complete resolve it to the date in 5 weeks from now.
	  Works with `d` (days), `w` (weeks), `m` (months), and `y` (years), and any number prefix.
- Some sensible default settings (e.g. indentation style)

## Configuration

### Keybindings for commands

The following commands are available for you to put into your `Default.sublime-keymap` file.

```json
[
	// Toggle item status to checked [x]
	{ "keys": ["ctrl+shift+x"], "command": "xit_check" },
	
	// Toggle item status to open [ ]
	{ "keys": ["ctrl+shift+o"], "command": "xit_open" },

	// Toggle item status to ongoign [@]
	{ "keys": ["ctrl+shift+a"], "command": "xit_ongoing" },

	// Toggle item status to obsolete [~]
	{ "keys": ["ctrl+shift+n"], "command": "xit_obsolete" },
]
```

### Settings (Syntax Specific)

The following settings can be overriden via your syntax-specific `xit.sublime-settings` file.

```json
{
	// Auto-save after toggling checkboxes (via the command).
	// Default: true
	"xit_auto_save": true
}
```
