# [x]it! for Sublime Text

This Sublime Package provides syntax-highlighting, shortcuts, and auto-completions for [[x]it! files](https://xit.jotaen.net).

![[x]it! demo](resources/xit-demo.png)

## Features

- Syntax highlighting
- Shortcut commands for toggling the item status
- Smart completions for due dates
	+ Type e.g. `5w` and have auto-complete resolve it to the date in 5 weeks from now.
	  Works with `d` (days), `w` (weeks), `m` (months), and `y` (years), and any number prefix.
- Some sensible default settings (e.g. indentation style)

## Configuration

### Keybindings for Commands

The following commands are available for you to put into your `Default.sublime-keymap` file.

```js
[
	// Toggle item status to checked [x]
	{ "keys": ["ctrl+shift+x"], "command": "xit_check" },
	
	// Toggle item status to open [ ]
	{ "keys": ["ctrl+shift+o"], "command": "xit_open" },

	// Toggle item status to ongoing [@]
	{ "keys": ["ctrl+shift+a"], "command": "xit_ongoing" },

	// Toggle item status to obsolete [~]
	{ "keys": ["ctrl+shift+n"], "command": "xit_obsolete" },
]
```

### Settings (Syntax Specific)

The following settings can be overriden via your syntax-specific `xit.sublime-settings` file.

```js
{
	// Auto-save after toggling checkboxes (via the commands `xit_check`, etc.).
	// Default: true
	"xit_auto_save": true,
}
```

### Syntax Highlighting / Colour overrides

The pre-defined syntax highlighting should look meaningful in most available colour schemes.

For [x]it! specific customisations, you can specify the following colour overrides:

-

Please also [see here](resources/Monokai.sublime-color-scheme) for a complete example for the Monokai scheme.
