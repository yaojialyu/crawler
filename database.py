#coding:utf8

import sqlite3

class Database(object):
    def __init__(self, dbFile):
        self.conn = sqlite3.connect(dbFile, isolation_level=None, check_same_thread = False) #让它自动commit，效率也有所提升. 多线程共用
        self.conn.execute('''CREATE TABLE IF NOT EXISTS
                            Webpage (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            url TEXT, 
                            pageSource TEXT,
                            keyword TEXT)''')

    def saveData(self, url, pageSource, keyword=''):
        sql='''INSERT INTO Webpage (url, pageSource, keyword) VALUES (?, ?, ?);'''
        self.conn.execute(sql, (url, pageSource, keyword) )

    def close(self):
        self.conn.close()

