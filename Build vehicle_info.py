from __future__ import print_function
import mysql.connector
from edmunds import edmunds
api = edmunds.Edmunds({your api key})

cnx = mysql.connector.connect(user='root',password='soccer',host='localhost',database='elliot_edmunds')
cursor = cnx.cursor()

allstylesdata=[] #this will hold the cursor data sets for each style of each model queried from new_models

query=("SELECT maker,model,model_year,model_id FROM new_models WHERE maker='audi' AND model_year=2016")
cursor.execute(query)
for (maker,model,model_year,model_id) in cursor:
    makerstr = str(model_id)
    yearstr = str(model_year)
    callString = '/api/vehicle/v2/'+maker+'/'+model+'/'+yearstr+'/styles' #build Edmunds API call string
    response = api.make_call(callString,view='full') #query Edmunds 
    respDict = response;
    #loop over each style found for the model response
    for i in respDict['styles']: 
        makeset = i['make'];
        modelset = i['model'];
        submodelset = i['submodel'];
        yearset = i['year'];
        style = i['id'];
        try:
            engineset = i['engine'];
            try:
                engineset_torque = engineset['torque'];
            except:
                engineset['torque']=""
        except:
            engineset = {
                "horsepower":0,
                "cylinder":0,
                "size":0,
                "torque":0,
                "type":""
                }

        try:
            transset = i['transmission'];
        except:
            transset = {
                "transmissionType":"",
                "numberOfSpeeds":""
                }
        try:
            drivenWh = i['drivenWheels'];
        except:
            drivenWh = "";
        try:
            numdoors = i['numOfDoors'];
        except:
            numdoors = "";
        try:
            priceset = i['price'];
        except:
            priceset = "";
        try:
            mpgset = i['MPG'];
        except:
            mpgset = {
                "highway":"",
                "city":""
                }
        detailedname = i['name'];
        print (makeset['name'],modelset['name'],submodelset['modelName'],yearset['year'],yearset['id'],style,engineset['horsepower'],engineset['cylinder'],engineset['size'],engineset['torque'],engineset['type'],transset['transmissionType'],transset['numberOfSpeeds'],drivenWh,numdoors,priceset['baseMSRP'],detailedname,mpgset['highway'],mpgset['city'])
        style_data = (makeset['name'],modelset['name'],submodelset['modelName'],yearset['year'],yearset['id'],style,engineset['horsepower'],engineset['cylinder'],engineset['size'],engineset['torque'],engineset['type'],transset['transmissionType'],transset['numberOfSpeeds'],drivenWh,numdoors,priceset['baseMSRP'],detailedname,mpgset['highway'],mpgset['city'])
        allstylesdata.append(style_data)


#have to close connector before we insert into vehicle_info
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
