import sqlite3
import csv
from pprint import pprint

sqlite_file = "sanjose.db"
conn = sqlite3.connect(sqlite_file)
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS nodes')

cur.execute('''
    Create Table nodes(id INTEGER, lat REAL, lon REAL, user TEXT, uid INTEGER, version TEXT, changeset INTEGER, timestamp TEXT)
''')
with open('nodes.csv','r',encoding = 'utf-8') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['lat'], i['lon'], i['user'], i['uid'], i['version'], i['changeset'], i['timestamp']) for i in dr]
cur.executemany("INSERT INTO nodes(id, lat, lon, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)


cur.execute('DROP TABLE IF EXISTS nodes_tags')

cur.execute('''
    Create Table nodes_tags( id INTEGER, key TEXT, value TEXT, type TEXT)
''')
with open('nodes_tags.csv','r', encoding = 'utf-8') as ndt:
    dr = csv.DictReader(ndt)
    to_db = [(i['id'], i['key'], i['value'], i['type'],) for i in dr]
	
cur.executemany("INSERT INTO nodes_tags(id, key , value, type) VALUES (?, ?, ?, ?);", to_db)


cur.execute('DROP TABLE IF EXISTS ways')

cur.execute('''
    Create Table ways( id INTEGER, user TEXT, uid INTEGER, version TEXT, changeset INTEGER, timestamp TEXT )
''')
with open('ways.csv','r', encoding = 'utf-8') as wys:
    dr = csv.DictReader(wys)
    to_db = [(i['id'], i['user'], i['uid'], i['version'], i['changeset'], i['timestamp']) for i in dr]
	
cur.executemany("INSERT INTO ways(id, user , uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?);", to_db)


cur.execute('DROP TABLE IF EXISTS ways_tags')

cur.execute('''
    Create Table ways_tags( id INTEGER, key TEXT, value TEXT, type TEXT)
''')
with open('ways_tags.csv','r', encoding = 'utf-8') as ndt:
    dr = csv.DictReader(ndt)
    to_db = [(i['id'], i['key'], i['value'], i['type'],) for i in dr]
	
cur.executemany("INSERT INTO ways_tags(id, key , value, type) VALUES (?, ?, ?, ?);", to_db)


cur.execute('DROP TABLE IF EXISTS ways_nodes')

cur.execute('''
    Create Table ways_nodes( id INTEGER, node_id INTEGER, position INTEGER)
''')
with open('ways_nodes.csv','r', encoding = 'utf-8') as ndt:
    dr = csv.DictReader(ndt)
    to_db = [(i['id'], i['node_id'], i['position'],) for i in dr]
	
cur.executemany("INSERT INTO ways_nodes(id, node_id , position) VALUES (?, ?, ?);", to_db)


conn.commit()
