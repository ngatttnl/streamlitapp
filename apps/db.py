# DB
import sqlite3
from sqlite3 import Error
# Functions
from urllib.request import pathname2url
from sqlalchemy import create_engine

#engine = create_engine('sqlite:///stock.db')
def connect():
	conn = sqlite3.connect('stock.db', check_same_thread=False)
	c = conn.cursor()
	return c

def create_table():
	c = connect()
	c.execute('CREATE TABLE IF NOT EXISTS stock(name TEXT PRIMARY KEY, value TEXT)')
	c.close()

def add(name, value):
	conn = sqlite3.connect('stock.db', check_same_thread=False)
	c = conn.cursor()
	c.execute('INSERT INTO stock(name, value) VALUES (?,?)',(name, value))
	conn.commit()
	c.close()

def view_all():
	conn = sqlite3.connect('stock.db', check_same_thread=False)
	c = conn.cursor()
	data = ""
	try:
		c.execute('SELECT * FROM stock')
		data = c.fetchall()
	except:
		create_table()
	c.close()
	return data

def get_by_value(value):
	conn = sqlite3.connect('stock.db', check_same_thread=False)
	c = conn.cursor()
	c.execute('SELECT * FROM stock WHERE value="{}"'.format(value))
	data = c.fetchall()
	c.close()
	return data
def get_stockname():
	conn = sqlite3.connect('stock.db', check_same_thread=False)
	c = conn.cursor()
	c.execute('SELECT name, (value || ":" || name) as exchange FROM stock')
	data = c.fetchall()
	c.close()
	return data

def delete_wrong():
	conn = sqlite3.connect('stock.db', check_same_thread=False)
	c = conn.cursor()
	c.execute('drop table stock')
    #c.execute('DELETE FROM stock WHERE name=""')
	conn.commit()
	c.close()

def delete(name):
	conn = sqlite3.connect('stock.db', check_same_thread=False)
	c = conn.cursor()
	c.execute('DELETE FROM stock WHERE name="{}"'.format(name))
	conn.commit()
	c.close()

def edit(name, exchange):
	conn = sqlite3.connect('stock.db', check_same_thread=False)
	c = conn.cursor()
	c.execute('UPDATE stock set value ="{}" WHERE name="{}"'.format(exchange, name))
	conn.commit()
	c.close()

#Post
def create_table_post():
	conn = sqlite3.connect('stock.db')
	c = conn.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS POST(ID INTEGER PRIMARY KEY AUTOINCREMENT, topic TEXT, content TEXT)')
	c.close()

def add_post(topic, content):
	conn = sqlite3.connect('stock.db')
	c = conn.cursor()
	c.execute('INSERT INTO post(topic, content) VALUES (?,?)',(topic, content))
	conn.commit()
	c.close()

def view_all_post():
	conn = sqlite3.connect('stock.db')
	c = conn.cursor()
	data = ""
	try:
		c.execute('SELECT * FROM post')
		data = c.fetchall()
	except:
		create_table_post()
		print("Can't open database")
	c.close()
	return data

def view_all_topic():
	conn = sqlite3.connect('stock.db')
	c = conn.cursor()
	data = ""
	try:
		c.execute('SELECT topic FROM post')
		data = c.fetchall()
	except:
		create_table_post()
		#print("Can't open database")
	c.close()
	return data

def get_by_id_post(id):
	conn = sqlite3.connect('stock.db', check_same_thread=False)
	c = conn.cursor()
	c.execute('SELECT * FROM POST WHERE id="{}"'.format(id))
	data = c.fetchall()
	c.close()
	return data

def delete_wrong_post():
	conn = sqlite3.connect('stock.db', check_same_thread=False)
	c = conn.cursor()
	c.execute('drop table POST')
    #c.execute('DELETE FROM stock WHERE name=""')
	conn.commit()
	c.close()

def delete_post(id):
	conn = sqlite3.connect('stock.db', check_same_thread=False)
	c = conn.cursor()
	c.execute('DELETE FROM POST WHERE name="{}"'.format(id))
	conn.commit()
	c.close()

def edit_post(content, topic, id):
	conn = sqlite3.connect('stock.db')
	c = conn.cursor()
	c.execute('UPDATE POST set content =?, topic = ? WHERE id=?', (content, topic, id))
	conn.commit()
	c.close()


