# https://qiita.com/EkatoPgm/items/2aea68188d053047cfb6
# PythonistaのUI実装で遊ぶ[画面遷移]
#
# notification.get_scheduled() の動きが記事掲載時とことなっているため関連箇所を改造


import ui
from alarmlist import AlarmList
import sys

import alarm_list_table	# alarm_list_table.tbl

a = AlarmList()
nv = ui.NavigationView(a.v) # ロードしたviewをNavigationViewに埋め込み
nv.height = 500             # nvのサイズ調整もしないと表示が崩れる
nv.width = 500
nv.name = 'Alarm'

nv.present('sheet')

'''
alarm_main.py -(import)- alarmlist.py -(import)- datepick.py -(import)- soundselect.py .(import). alarmlist.py
                               |                       |                    |
                            (import)                (import)             (import)             
                               |                       |                    |
                               +-----------------------+--------------------+
                                                       |
                                                alarm_list_table.py
'''
