import pymysql

db = pymysql.connect(host='192.168.0.84',user='root',password='root',db='example',charset='utf8')

cur = db.cursor()
cur.execute("SELECT DISTINCT name, address FROM Customer WHERE EXISTS(SELECT * FROM Orders)")

rows = cur.fetchall()
print(rows)
db.close()