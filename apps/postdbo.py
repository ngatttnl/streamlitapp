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
	c.execute('CREATE TABLE IF NOT EXISTS POST(ID INTEGER PRIMARY KEY AUTOINCREMENT, topic TEXT, content TEXT)')

def add(topic, content):
    
    c.execute('INSERT INTO post(name, value) VALUES (?,?)',(topic, content))
    
    conn.commit()

def view_all():
    data = ""
    try:
        c.execute('SELECT topic, content FROM post')
        data = c.fetchall()
    except:
        #create_table()
        print("Can't open database")
    return data

def get_by_id(id):
	c.execute('SELECT * FROM POST WHERE id="{}"'.format(id))
	data = c.fetchall()
	return data

def delete_wrong():
	c.execute('drop table POST')
    #c.execute('DELETE FROM stock WHERE name=""')
	conn.commit()

def delete(id):
	c.execute('DELETE FROM POST WHERE name="{}"'.format(id))
	conn.commit()

def edit(content, id):
	c.execute('UPDATE POST set content ="{}" WHERE id="{}"'.format(content, id))
	conn.commit()


