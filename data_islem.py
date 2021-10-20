# Arda Mavi - ardamavi.com
import sqlite3

def set_sql_connect(database_name):
    return sqlite3.connect(database_name)

def set_sql_cursor(database_connect):
    return database_connect.cursor()

def set_connect_and_cursor():
    vt = set_sql_connect('mb2.db')
    db = set_sql_cursor(vt)

    return vt, db

def close_connect(vt):
    if vt:
        vt.commit()
        vt.close

def tablo_yarat(table_name, columns):
    vt, db = set_connect_and_cursor()
    db.execute("CREATE TABLE IF NOT EXISTS {0}({1})".format(table_name, columns))
    close_connect(vt)

def veri_al(sql_komut):
    vt, db = set_connect_and_cursor()
    db.execute(sql_komut)
    gelen_veri = db.fetchall()
    close_connect(vt)
    return gelen_veri

def data_ekle(table, eklenecek_sutun, eklenecek):
    vt, db = set_connect_and_cursor()
    db.execute("INSERT INTO '{0}'({1}) VALUES {2}".format(table, eklenecek_sutun, eklenecek))
    # eklenecek_sutun örnek: 'sütun1','sütun2'
    # eklenecek örnek: data1, data2
    close_connect(vt)

def data_guncelle(table, nerden, nasil):
    vt, db = set_connect_and_cursor()
    db.execute("UPDATE {0} SET {2} WHERE {1}".format(table, nerden, nasil))
    close_connect(vt)
    

vt, db = set_connect_and_cursor()

test = "id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, LastName TEXT,Department TEXT, BirthDay TEXT"

tablo_yarat("Murat",test)

close_connect(vt)