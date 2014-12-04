import sublime, sublime_plugin

class DegooglerCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		# replace " with 
		dq_edit = self.view.begin_edit()
		dq_list = []
		dq_regions = self.view.find_all("\"", sublime.LITERAL, " ", dq_list)
		for pos, region in zip(dq_regions, dq_list):
			self.view.replace(dq_edit, pos, region)
		self.view.end_edit(dq_edit)

		# replace ` with "
		td_edit = self.view.begin_edit()
		td_list = []
		td_regions = self.view.find_all("`", sublime.LITERAL, "\"", td_list)
		for pos, region in zip(td_regions, td_list):
			self.view.replace(td_edit, pos, region)
		self.view.end_edit(td_edit)

		# replace NaN with 0
		na_edit = self.view.begin_edit()
		na_list = []
		na_regions = self.view.find_all("NaN", sublime.LITERAL , "0", na_list)
		for pos, region in zip(na_regions, na_list):
			self.view.replace(na_edit, pos, region)
		self.view.end_edit(na_edit)

