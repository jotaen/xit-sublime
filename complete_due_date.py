# https://www.sublimetext.com/docs/api_reference.html

import re
import sublime
import sublime_plugin
import datetime
import calendar


SHORTCUT_PATTERN = re.compile('.*((\d+)([dwmy]))$')


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


def complete(trigger, value, details):
	return sublime.CompletionItem(
		trigger,
		annotation='-> '+value,
		completion='-> '+value,
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=(sublime.KIND_ID_AMBIGUOUS, '☑', '[x]it!'),
		details=details,
	)


class XitEventListener(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		# Only offer due dates within description scope.
		if not view.match_selector(locations[0], 'meta.description.xit'):
			return

		cursor = view.line(view.sel()[0])
		preceding_text = view.substr(cursor)

		# If the user didn’t provide a pattern, offer some defaults.
		match = SHORTCUT_PATTERN.search(preceding_text)
		if not match:
			fragment = datetime.datetime.now().strftime('%Y-%m-')
			return sublime.CompletionList([
				complete(fragment, fragment, 'Insert date fragment'),
				complete('3d', expand(3, 'd'), 'Pre-compute due date from pattern'),
				complete('1w', expand(1, 'w'), 'Pre-compute due date from pattern'),
				complete('2w', expand(2, 'w'), 'Pre-compute due date from pattern'),
				complete('1m', expand(1, 'm'), 'Pre-compute due date from pattern'),
			])

		# Otherwise, expand the pattern.
		pattern = match.group(1)
		count = int(match.group(2))
		qualifier = match.group(3)
		due_date = expand(count, qualifier)

		return sublime.CompletionList([
			complete(pattern, due_date, 'Pre-compute due date from pattern'),
		])
