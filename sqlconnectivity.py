import pymysql

# con = pymysql.connect(host='127.0.0.1', user='root', password='admin', db='db1', port=3306)
con = pymysql.connect(host='localhost', user='root', password='admin', db='db1')
cur = con.cursor()
cur.execute("select* from tbl")
rows = cur.fetchall()
print(rows)
con.close()


