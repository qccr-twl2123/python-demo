#!/usr/bin/python
# -*- coding: UTF-8 -*-


import pandas as pd
import MySQLdb

db = MySQLdb.connect(host='localhost',port=3308, user='root', passwd='123456', db='uber')
df = pd.read_sql("select * from driver", con=db)
print df
db.close()

'''
1.报错信息 
raise ImportError("Missing required dependencies {0}".format(missing_dependencies))
ImportError: Missing required dependencies ['numpy']

将anaconda 路径添加到path下面 
D:\ProgramData\Anaconda3\Library\bin
'''
