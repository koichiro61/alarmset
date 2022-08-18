import ui
from soundselect import SoundSelect
from datetime import datetime
class Datepick(object):

	def __init__(self):
		self.v = ui.load_view()
		self.v['button1'].action = self.tap_ok_button

	def tap_ok_button(self, sender):
		# DatePickerの時刻を取得
		date = sender.superview['datepicker1'].date
		s = SoundSelect(date)
		sender.superview.navigation_view.push_view(s.v)

