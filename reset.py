import csv
import os

import psycopg2

BASE_DIR = os.path.dirname(__file__)

conn = psycopg2.connect(database='wordpicker', user='postgres')
cursor = conn.cursor()

cursor.execute('CREATE TABLE sowpods (word VARCHAR UNIQUE)')

with open(os.path.join(BASE_DIR,'sowpods.txt')) as file:
  reader = csv.reader(file)
  for row in reader:
    word = row[0]
    cursor.execute('INSERT INTO sowpods (word) VALUES (%s)' % tosql(word))

conn.commit()
