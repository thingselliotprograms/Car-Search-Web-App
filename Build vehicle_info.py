from __future__ import print_function
import mysql.connector
from edmunds import edmunds
api = edmunds.Edmunds('fpbmqm5rcqz6strkpxkfy48q')

cnx = mysql.connector.connect(user='root',password='soccer',host='localhost',database='elliot_edmunds')
cursor = cnx.cursor()

allstylesdata=[]

query=("SELECT maker,model,model_year,model_id FROM new_models WHERE maker='alfa-romeo'")
cursor.execute(query)
for (maker,model,model_year,model_id) in cursor:
    makerstr = str(model_id)
    yearstr = str(model_year)
    print (maker,model,yearstr,makerstr)
    callString = '/api/vehicle/v2/'+maker+'/'+model+'/'+yearstr+'/styles'
    print (callString)
    response = api.make_call(callString,view='full')
    respDict = response;
    for i in respDict['styles']:
        makeset = i['make'];
        modelset = i['model'];
        submodelset = i['submodel'];
        yearset = i['year'];
        style = i['id'];
        engineset = i['engine'];
        transset = i['transmission'];
        drivenWh = i['drivenWheels'];
        numdoors = i['numOfDoors'];
        priceset = i['price'];
        mpgset = i['MPG'];
        detailedname = i['name'];
        mpgset = i['MPG'];
        print (makeset['name'],modelset['name'],submodelset['modelName'],yearset['year'],yearset['id'],style,engineset['horsepower'],engineset['cylinder'],engineset['size'],engineset['torque'],engineset['type'],transset['transmissionType'],transset['numberOfSpeeds'],drivenWh,numdoors,priceset['baseMSRP'],detailedname,mpgset['highway'],mpgset['city'])
        style_data = (makeset['name'],modelset['name'],submodelset['modelName'],yearset['year'],yearset['id'],style,engineset['horsepower'],engineset['cylinder'],engineset['size'],engineset['torque'],engineset['type'],transset['transmissionType'],transset['numberOfSpeeds'],drivenWh,numdoors,priceset['baseMSRP'],detailedname,mpgset['highway'],mpgset['city'])
        allstylesdata.append(style_data)

cursor.close()
cnx.close()

print ("first part done")
print (len(allstylesdata))

cnx = mysql.connector.connect(user='root',password='soccer',host='localhost',database='elliot_edmunds')
cursor = cnx.cursor()

add_style = ("INSERT INTO vehicle_info "
             "(maker, model, submodel_name, model_year, model_id, style_id, hp, cylinders, engine_size, torque, engine_type, trans_type, trans_num_speeds, drivenwheels, num_doors, price, detailed_name, mpg_hw, mpg_city) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

for i in allstylesdata:
    vehicle_style_data=i;
    cursor.execute(add_style,vehicle_style_data);

print ("done with second part")

cnx.commit()

cursor.close()
cnx.close()