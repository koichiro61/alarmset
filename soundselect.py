import ui
import console
from datetime import datetime
import notification
import alarm_list_table	# alarm_list_table.tbl
#from alarmlist import AlarmList

class SoundSelect(object):
	def __init__(self, date):
		self.v = ui.load_view()
		self.date = date
		self.v['button1'].action = self.tap_ok_button
		
	def tap_ok_button(self, sender):
		from alarmlist import AlarmList	# 循環 import 回避のためにここで import 
		sounds = ['drums:Drums_01','drums:Drums_02','drums:Drums_03']
		selected = self.v['tableview1'].selected_row[1]

		now = datetime.now()  # 現在時刻を取得
		delay = self.date - now  # 設定時刻との差分
		nid = notification.schedule('test notify', delay=delay.total_seconds(), sound_name=sounds[selected])
		alarm_list_table.tbl.add(nid, self.date)
		alarm_list_table.tbl.synchronize()
		
		a = AlarmList()
		sender.superview.navigation_view.push_view(a.v)

