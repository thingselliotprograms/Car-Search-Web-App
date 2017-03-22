from __future__ import print_function
import mysql.connector

import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, create_session
from sqlalchemy import func, distinct

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:soccer@localhost/elliot_edmunds')
metadata = MetaData(bind=engine)

class New_Models(Base):
    __table__ = Table('new_models', metadata, autoload=True)

class Vehicle_Info(Base):
    __table__ = Table('vehicle_info', metadata, autoload=True)

session = create_session(bind=engine)

models = session.query(New_Models).filter_by(maker='maserati').order_by('maker').all()

print (len(models))

for model in models:
    print (model.maker+" - "+model.model)

allstyles = session.query(Vehicle_Info).order_by('maker').all()

print (len(allstyles))

'''
print(engine.table_names())

conn = engine.connect()
result = conn.execute("Select maker, model From new_models order by maker")
for i in result:
    print ("Maker:", i['maker'], "Model:", i['model'])
conn.close()
'''

'''
cnx = mysql.connector.connect(user='root',password='soccer',host='localhost',database='elliot_edmunds')
cursor = cnx.cursor()

query = ("SELECT maker,model,model_year,model_id FROM new_models ORDER BY maker")

cursor.execute(query)

for maker,model,model_year,model_id in cursor:
    print (maker,model,model_year)

cursor.close()
cnx.close()
'''


'''

def checkVehicleInfo(querystr):
    hasInfo=0
    cnx = mysql.connector.connect(user='root',password='soccer',host='localhost',database='elliot_edmunds')
    cursor = cnx.cursor()
    cursor.execute(querystr)
    for maker,model in cursor:
        if maker!="":
            hasInfo=1
        else:
            pass
    cursor.close()
    cnx.close()


    return hasInfo


cnx = mysql.connector.connect(user='root',password='soccer',host='localhost',database='elliot_edmunds')
cursor = cnx.cursor()

query = ("SELECT maker,model,model_year,model_id FROM new_models ORDER BY maker")

cursor.execute(query)

for maker,model,model_year,model_id in cursor:
    print (maker,model,model_year)
    query2 = ("SELECT maker,model FROM vehicle_info WHERE model_id='"+str(model_id)+"'")
    print (query2)
    checkResult = checkVehicleInfo(query2)
    if checkResult==0:
        break
    else:
        print (checkResult)


cursor.close()
cnx.close()

'''
