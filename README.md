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
The key combination is up to you, of course.

```js
[
	// Toggle checkbox status of the item.
	// It cycles through the statuses given in the
	// `xit_toggle` setting.
	{ "keys": ["ctrl+shift+t"], "command": "xit_toggle" },

	// Set item status to checked [x]
	{ "keys": ["ctrl+shift+x"], "command": "xit_check" },
	
	// Set item status to open [ ]
	{ "keys": ["ctrl+shift+o"], "command": "xit_open" },

	// Set item status to ongoing [@]
	{ "keys": ["ctrl+shift+a"], "command": "xit_ongoing" },

	// Set item status to obsolete [~]
	{ "keys": ["ctrl+shift+n"], "command": "xit_obsolete" },
]
```

### Settings (Syntax Specific)

The following settings can be overriden via your syntax-specific `xit.sublime-settings` file.
The values are the default ones.

```js
{
	// Auto-save after toggling checkboxes (via the commands `xit_check`, etc.).
	"xit_auto_save": true,

	// The checkbox statuses that the `xit_toggle` command
	// should cycle through.
	"xit_toggle": ["[ ]", "[x]"],
}
```

### Syntax Highlighting / Colour overrides

The pre-defined syntax highlighting should look meaningful in most available colour schemes.

For [x]it! specific customisations, you can specify the following colour overrides:

- `markup.other.title.xit` For the item group title
- `markup.other.checkbox.open.xit` For an open checkbox: `[ ]`
- `markup.other.checkbox.checked.xit` For a checked checkbox: `[x]`
- `markup.other.checkbox.ongoing.xit` For an ongoing checkbox: `[@]`
- `markup.other.checkbox.obsolete.xit` For an obsolete checkbox: `[~]`
- `markup.other.priority.exclamation.xit` For the exclamation mark of the priority: `!`
- `markup.other.priority.dot.xit` For the dot of the priority: `.`
- `markup.other.description.xit` For the item description
- `markup.other.due_date.xit` For the due date within the description: `-> 2022-03-27`
- `markup.other.tag.name.xit` For a tag: `#example`
- `markup.other.tag.value.xit` For the value of a tag: `#example=value`

Additionally, you can reference the following meta scopes to make adjustments based on the item status:

- `meta.item.status.open.xit`
- `meta.item.status.checked.xit`
- `meta.item.status.ongoing.xit`
- `meta.item.status.obsolete.xit`

Please also [see here](resources/xit-dark.sublime-color-scheme.EXAMPLE) for a complete colouring example based on a dark scheme.
