# https://www.pg4e.com/code/swapi.py
# https://www.pg4e.com/code/myutils.py

# If needed:
# https://www.pg4e.com/code/hidden-dist.py
# copy hidden-dist.py to hidden.py
# edit hidden.py and put in your credentials

# python3 swapi.py
# Pulls data from the swapi.py4e.com API and puts it into our swapi table

import psycopg2
import hidden
import time
import myutils
import requests
import json

def summary(cur) :
    total = myutils.queryValue(cur, 'SELECT COUNT(*) FROM swapi;')
    todo = myutils.queryValue(cur, 'SELECT COUNT(*) FROM swapi WHERE status IS NULL;')
    good = myutils.queryValue(cur, 'SELECT COUNT(*) FROM swapi WHERE status = 200;')
    error = myutils.queryValue(cur, 'SELECT COUNT(*) FROM swapi WHERE status != 200;')
    print(f'Total={total} todo={todo} good={good} error={error}')

# Load the secrets
secrets = hidden.secrets()

conn = psycopg2.connect(host=secrets['host'],
        port=secrets['port'],
        database=secrets['database'],
        user=secrets['user'],
        password=secrets['pass'],
        connect_timeout=3)

cur = conn.cursor()

defaulturl = 'https://swapi.py4e.com/api/films/1/'
print('If you want to restart the spider, run')
print('DROP TABLE IF EXISTS swapi CASCADE;')
print(' ')

sql = '''
CREATE TABLE IF NOT EXISTS swapi
(id serial, url VARCHAR(2048) UNIQUE, status INTEGER, body JSONB,
created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(), updated_at TIMESTAMPTZ);
'''
print(sql)
cur.execute(sql)

# Check to see if we have urls in the table
cur.execute('SELECT url FROM swapi WHERE status IS NULL ORDER BY RANDOM() LIMIT 1;')
row = cur.fetchone()
if row is None :
    cur.execute('INSERT INTO swapi (url, status) VALUES (%s, %s) RETURNING id', (defaulturl, None))
    conn.commit()
    time.sleep(1)

many = 0
while True:
    if many < 1 :
        sval = input('How many urls:')
        if len(sval) < 1: break
        many = int(sval)

    cur.execute('SELECT id, url FROM swapi WHERE status IS NULL ORDER BY RANDOM() LIMIT 1;')
    row = cur.fetchone()
    if row is None :
        print('No remaining urls to read')
        break

    id = row[0]
    url = row[1]
    print(id, url)

    try:
        response = requests.get(url, timeout=10)
        status = response.status_code
        body = response.text
    except Exception as e:
        print('Failed to retrieve', url, e)
        status = -1
        body = ''
        continue

    sql = 'UPDATE swapi SET status=%s, body=%s WHERE id=%s'
    cur.execute(sql, (status, body, id))
    conn.commit()
    time.sleep(1)
    many = many - 1

summary(cur)

cur.close()
conn.close()
