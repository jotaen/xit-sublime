# https://www.sublimetext.com/docs/api_reference.html

import re
import sublime
import sublime_plugin


BOX_PATTERN = re.compile('\[[ x~?]\]')
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

			# If the line starts with a box, modify it.
			box_candidate = sublime.Region(line.begin(), line.begin() + len(replacement))
			if BOX_PATTERN.match(view.substr(box_candidate)):
				view.replace(edit, box_candidate, replacement)


class XitCheckCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		modify_box(self.view, edit, '[x]')


class XitUncheckCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		modify_box(self.view, edit, '[ ]')


class XitObsoleteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		modify_box(self.view, edit, '[~]')


class XitQuestionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		modify_box(self.view, edit, '[?]')
