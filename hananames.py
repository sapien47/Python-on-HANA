

import names
import pyhdb
connection = pyhdb.connect('localhost', 30015, 'SAPABAP1', 'Basis001')

print(connection.isconnected())


namelist = []
for i in  range(0,100):
    namelist.append(names.get_last_name())


print(namelist)
QUERY='CREATE COLUMN TABLE EMPLOYE (person_id int, lastname NVARCHAR(20))'

cursor = connection.cursor()
cursor.execute(QUERY)

for row in enumerate(namelist):
    try:
        cursor.execute("INSERT INTO  EMPLOYE (person_id, lastname) VALUES ({}, '{}')".format(*row))
    except Exception as exception:
        print(e)

connection.commit()