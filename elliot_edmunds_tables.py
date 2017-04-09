from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'elliot_edmunds'

TABLES = {}
TABLES['new_models'] = (
    "CREATE TABLE `new_models` ("
    "  `maker` varchar(30) NOT NULL,"
    "  `model` varchar(30) NOT NULL,"
    "  `model_year` int(4) NOT NULL,"
    "  `model_id` int(20) NOT NULL,"
    "  PRIMARY KEY (`model_id`)"
    ") ENGINE=InnoDB")



TABLES['vehicle_info'] = (
    "CREATE TABLE `vehicle_info` ("
    "  `maker` varchar(30) NOT NULL,"
    "  `model` varchar(30) NOT NULL,"
    "  `submodel_name` varchar(100),"
    "  `model_year` int NOT NULL,"
    "  `model_id` int NOT NULL,"
    "  `style_id` int NOT NULL,"
    "  `hp` int,"
    "  `cylinders` int,"
    "  `engine_size` int,"
    "  `torque` int,"
    "  `engine_type` varchar(20),"
    "  `trans_type` varchar(30),"
    "  `trans_num_speeds`varchar(40),"
    "  `drivenwheels` varchar(100),"
    "  `num_doors` varchar(10),"
    "  `price` int,"
    "  `detailed_name` varchar(255),"
    "  `mpg_hw` varchar(10),"
    "  `mpg_city` varchar(10),"
    "  PRIMARY KEY (`style_id`),"
    "  FOREIGN KEY (`model_id`) REFERENCES `new_models` (`model_id`)"
    ") ENGINE=InnoDB")



TABLES['vehicle_photos'] = (
    "CREATE TABLE `vehicle_photos` ("
    "  `style_id` int NOT NULL,"
    "  `FQ_URL` text,"
    "  `I_URL` text,"
    "  FOREIGN KEY (`style_id`) REFERENCES `vehicle_info` (`style_id`)"
    ") ENGINE=InnoDB")








cnx = mysql.connector.connect(user='elliotedmunds',host='elliot-edmunds-tutorial.cmzeemwmjhxe.us-east-2.rds.amazonaws.com',password='soccer3000')
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for name, ddl in TABLES.iteritems():
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

print ("I guess it worked")

cursor.close()
cnx.close()