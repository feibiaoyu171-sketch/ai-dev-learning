"""第 4 周：用 Python 连 MySQL，把数据查出来。

跑之前：
1. 激活虚拟环境（提示符前面要有 (venv)）
2. pip install pymysql
3. 把下面的 password 换成你设的 MySQL 密码
"""

import pymysql

conn = pymysql.connect(
    host="localhost",        # 数据库在本机
    user="root",             # 用户名
    password="1712971580wdsj!",   # 换成你的密码
    database="bathymetry"    # 连哪个库
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM points")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
