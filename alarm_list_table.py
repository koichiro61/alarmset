import notification

class alarm_list_table:

	def __init__(self):
		self.number = 0
		self.alarm_date_time =  {}	# alarm_date_time[notification id]
	
	def add(self, id, date_time):
		self.alarm_date_time[id] = date_time
		self.number += 1
		
	def delete(self, id):
		try:
			del self.alarm_date_time[id]
			self.number -= 1
		except KeyError:
			pass
	
	def synchronize(self):	# 表示のためのリストを os に登録されている notification list と同期させる
		nl_set = set(notification.get_scheduled())	# スケジュール登録時にとられた UUIDのリストを集合化
		notification_id_done = set(self.alarm_date_time) - nl_set # 表示用リストあって OS登録リストにないもの得る
		for i in notification_id_done:	# os登録リストにないものを削除することで同期をとる
			self.delete(i)
		#print(self.list_date_time())
			
	def list_date_time(self):	# 登録済みアラーム時刻のリスト取り出し
		l = []
		for d in sorted(list(self.alarm_date_time.values())):
			l.append(d.strftime('%a %b %d %H %M'))
		return l
			

tbl = alarm_list_table()	#このモジュールをimportしたモジュール間で共有されるインスタンス


		
