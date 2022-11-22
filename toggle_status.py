# https://www.sublimetext.com/docs/api_reference.html

import re
import sublime
import sublime_plugin


BOX_PATTERN = re.compile('\[[ x~@?]\]')
BOX_LENGTH = 3
INDENT_SEQUENCE = '    '


def set_status(view, edit, replaceBy):
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
			checkbox_region = sublime.Region(line.begin(), line.begin() + BOX_LENGTH)
			checkbox = view.substr(checkbox_region)
			if not BOX_PATTERN.match(checkbox):
				return

			# Replace status.
			replacement = replaceBy(checkbox)
			view.replace(edit, checkbox_region, replacement)

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
		set_status(self.view, edit, lambda _: '[x]')


class XitOpenCommand(_XitCommand):
	def run(self, edit):
		set_status(self.view, edit, lambda _: '[ ]')


class XitObsoleteCommand(_XitCommand):
	def run(self, edit):
		set_status(self.view, edit, lambda _: '[~]')


class XitOngoingCommand(_XitCommand):
	def run(self, edit):
		set_status(self.view, edit, lambda _: '[@]')


class XitInQuestionCommand(_XitCommand):
	def run(self, edit):
		set_status(self.view, edit, lambda _: '[?]')


class XitToggleCommand(_XitCommand):
	def _load_toggles(self):
		self._toggles = None
		settings = sublime.load_settings('xit.sublime-settings')
		toggles = settings.get('xit_toggle')

		# Setting value must be a non-empty list.
		if not isinstance(toggles, list) or len(toggles) == 0:
			return None

		# List must be checkboxes as string.
		for t in toggles:
			if (not isinstance(t, str)) or (not len(t) == 3) or (not BOX_PATTERN.match(t)):
				return None

		self._toggles = toggles

	def _cycle(self, status):
		# Find current status, or make it fall back to first.
		try:
			i = self._toggles.index(status)
		except ValueError:
			i = -1

		# Return next status in the “ring”.
		try:
			return self._toggles[i+1]
		except IndexError:
			return self._toggles[0]

	def run(self, edit):
		self._load_toggles()
		if not self._toggles:
			return
		set_status(self.view, edit, self._cycle)
