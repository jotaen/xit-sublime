# https://www.sublimetext.com/docs/api_reference.html

import re
import sublime
import sublime_plugin


BOX_PATTERN = re.compile('\[[ x~@]\]')
INDENT_SEQUENCE = '    '


def modify_box(view, edit, replacement):
	# Iterate through all selections (there might be
	# multiple, due to multi-cursor-action), and all
	# their lines.
	for sel in view.sel():
		lines = view.split_by_newlines(view.line(sel))
		for i, line in enumerate(lines):

			# The first line of a selection is a special case,
			# because the cursor might be placed in a subsequent
			# description line. Therefore, we have to travel up,
			# until we find the line that contains the corresponding
			# box.
			if i == 0:
				while True:
					indent_candidate = sublime.Region(line.begin(), line.begin() + len(INDENT_SEQUENCE))
					if view.substr(indent_candidate) == INDENT_SEQUENCE:
						line = view.line(line.begin()-1)
					else:
						break

			# If the line doesn’t start with a box, return.
			box_candidate = sublime.Region(line.begin(), line.begin() + len(replacement))
			if not BOX_PATTERN.match(view.substr(box_candidate)):
				return

			# Replace status.
			view.replace(edit, box_candidate, replacement)

			# Auto-save, if enabled, and if there is a backing file.
			settings = sublime.load_settings('xit.sublime-settings')
			if settings.get('xit_auto_save'):
				def save():
					if view.file_name():
						view.run_command('save')
				sublime.set_timeout(save, 0)  # Needs to be queued apparently.


class _XitCommand(sublime_plugin.TextCommand):
	def is_enabled(self):
		return self.view.syntax().scope == 'source.xit'


class XitCheckCommand(_XitCommand):
	def run(self, edit):
		modify_box(self.view, edit, '[x]')


class XitUncheckCommand(_XitCommand):
	def run(self, edit):
		modify_box(self.view, edit, '[ ]')


class XitObsoleteCommand(_XitCommand):
	def run(self, edit):
		modify_box(self.view, edit, '[~]')


class XitOngoingCommand(_XitCommand):
	def run(self, edit):
		modify_box(self.view, edit, '[@]')
