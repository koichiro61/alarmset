import ui
from datepick import Datepick
import notification
from datetime import datetime
import alarm_list_table	# alarm_list_table.tbl をモジュール間で共有

class AlarmList(object):
	def __init__(self):
		self.v = ui.load_view()
		self.v['button1'].action = self.tap_new_button
		
		l = alarm_list_table.tbl.list_date_time()
		self.ds = ui.ListDataSource(l)
		self.v['tableview1'].data_source = self.ds
	
	def tap_new_button(self, sender):
		d = Datepick()
		# 画面を遷移させる
		sender.superview.navigation_view.push_view(d.v)

