from pymysql import connect,cursors

conn =connect(host='47.94.81.27',
              port=3306,
              user='paperbook',
              password='D72S54ZHDNmC3wHt',
              db='paperbook',
              charset='utf8',
              cursorclass=cursors.DictCursor)
try:
    with conn.cursor() as cursor:
        sql = 'SELECT * FROM aper_author'
        cursor.execute(sql)
        rel = cursor.fetchone()
        print(rel)
finally:
    conn.close()