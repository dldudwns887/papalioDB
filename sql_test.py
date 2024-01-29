

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='5482asas', db='kbo_baseball', charset='utf8')

curs = conn.cursor()

sql = 'select 년도,팀_이름,선수_이름 from 선수 where 팀_이름 = "한화" and 년도 = 2018  '

curs.execute(sql)

data = curs.fetchall()

print(data)


conn.close()



