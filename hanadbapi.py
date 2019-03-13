import os
from hdbcli import dbapi
import getopt
import sys
import csv
from datetime import datetime
import json
import random

SCHEMA = 'SAPHANADB'
TABLE = 'T000'
ROWS = 2000
now= datetime.now()
now_string = now.strftime('%Y-%m-%d')
print(now_string)
DATE = now_string
FILE = r'C:\Users\farid.brahimi\Documents\Python\hana\exceptions.json'
with open(FILE) as f:
    EXCEPTION=json.load(f)



def RandomDec(p,s):
    return random.randint(0, 10**p)-1/(10**s)

def getval(coldef, schema, table, exception):
    return RandomDec(coldef[2],coldef[2])




connection = dbapi.connect(
    address='35.182.78.78',
    port=30015,
    user='SYSTEM',
    password='Ch3mh@na'
)
# csvout =  open("data/"+SCHEMA+"."+TABLE+"_"+DATE+".csv", "w", newline ="")


if connection.isconnected():
    print("Conexion established")
else:
    print("Error de conexion")

curr = connection.cursor()


QRY= " SELECT COLUMN_NAME, DATA_TYPE_NAME, LENGTH, SCALE "
QRY += " FROM TABLE_COLUMNS WHERE SCHEMA_NAME ='"
QRY += SCHEMA + "' AND TABLE_NAME ='"
QRY += TABLE + "' ORDER BY POSITION ASC"

curr.execute(QRY)
results = curr.fetchall()

argv = sys.argv[0:]

print(results)
T0 = datetime.now()
print("==================================", TABLE, "Debut", T0)
for x in range(ROWS):
    if x % (ROWS/20) == 0:
        print(SCHEMA, TABLE, x/ROWS*100, '%')
        defVal = lambda p: getval(p, SCHEMA, TABLE, EXCEPTION)
        rowval = list(map(defVal, results))



# for column in results:
#     print(column)

