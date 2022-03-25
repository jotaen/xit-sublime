# https://www.sublimetext.com/docs/api_reference.html

import re
import sublime
import sublime_plugin
import datetime
import calendar


EXPAND_PATTERN = re.compile('.*-> ((\d+)([dwmy]))$')


def add_months(date, months):
    month = date.month - 1 + months
    year = date.year + month // 12
    month = month % 12 + 1
    day = min(date.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)


def expand(count, qualifier):
	result = datetime.datetime.now()
	if qualifier == 'd':
		result += datetime.timedelta(days=count)
	elif qualifier == 'w':
		result += datetime.timedelta(weeks=count)
	elif qualifier == 'm':
		result = add_months(result, count)
	elif qualifier == 'y':
		result = add_months(result, count*12)
	return result.strftime('%Y-%m-%d')


class ExpandDueDateCommand(sublime_plugin.TextCommand):
	def is_enabled(self):
		cursor = self.view.sel()[0]
		line = self.view.line(cursor)
		match = EXPAND_PATTERN.search(self.view.substr(line))
		if not match:
			return False

		self._cmd_pattern = match.group(1)
		count = int(match.group(2))
		qualifier = match.group(3)
		self._cmd_due_date = expand(count, qualifier)
		return True

	def run(self, edit):
		cursor = self.view.sel()[0]
		line = self.view.line(cursor)
		region = sublime.Region(cursor.begin() - len(self._cmd_pattern), cursor.begin())
		self.view.replace(edit, region, self._cmd_due_date)
