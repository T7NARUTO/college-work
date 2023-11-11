import pymysql
import pandas as pd

db = pymysql.connect(
    host='localhost',
    database='ANNUAL_EXAM',
    user='root',
    passwd='root'
)
cur = db.cursor()

