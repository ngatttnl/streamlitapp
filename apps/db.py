# DB
import sqlite3
from sqlite3 import Error
# Functions
from urllib.request import pathname2url
from sqlalchemy import create_engine

#engine = create_engine('sqlite:///stock.db')
conn = sqlite3.connect('stock.db', check_same_thread=False)
c = conn.cursor()



def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS stock(name TEXT PRIMARY KEY, value TEXT)')

def add(name, value):
	c.execute('INSERT INTO stock(name, value) VALUES (?,?)',(name, value))
	conn.commit()

def view_all():
    data = ""
    try:
        c.execute('SELECT * FROM stock')
        data = c.fetchall()
    except:
        create_table()
    return data

def get_by_value(value):
	c.execute('SELECT * FROM stock WHERE value="{}"'.format(value))
	data = c.fetchall()
	return data
def get_stockname():
	c.execute('SELECT name, (value || ":" || name) as exchange FROM stock')
	data = c.fetchall()
	return data

def delete_wrong():
	c.execute('drop table stock')
    #c.execute('DELETE FROM stock WHERE name=""')
	conn.commit()

def delete(name):
	c.execute('DELETE FROM stock WHERE name="{}"'.format(name))
	conn.commit()

def edit(name, exchange):
	c.execute('UPDATE stock set value ="{}" WHERE name="{}"'.format(exchange, name))
	conn.commit()


