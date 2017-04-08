from __future__ import print_function

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
carapp = Flask(__name__)

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

@carapp.route('/')
@carapp.route('/mainsite/')
def mainsite():
    makers = session.query(Vehicle_Info.maker).distinct().order_by(Vehicle_Info.maker)
    hpstyles = session.query(Vehicle_Info).order_by(Vehicle_Info.hp.desc()).limit(100)
    count = 0
    for maker in makers:
        count+=1
    return render_template("carmodellist.html",makers=makers,count=count,hpstyles=hpstyles)

@carapp.route('/_add_numbers')
def add_numbers():
    response= {}
    styles = session.query(Vehicle_Info.model).distinct().filter_by(maker = 'Maserati')
    for i in styles:
        response[i.model]=i.model
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    response["result"]=(a+b)
    response["car"]="Maserati Models"
    return jsonify(response)

@carapp.route('/modelssamepage')
def models_same_page():
    response = {}
    makerjson = request.args.get('maker')
    styles = session.query(Vehicle_Info.model).distinct().filter_by(maker = makerjson)
    for i in styles:
        response[i.model]=i.model
    print (response)
    return jsonify(response);

@carapp.route('/modelstyles')
def models_styles():
    response = {}
    makerjson = request.args.get('maker')
    modeljson = request.args.get('model')
    print (makerjson,modeljson)
    styles = session.query(Vehicle_Info).filter(Vehicle_Info.maker == makerjson).filter(Vehicle_Info.model == modeljson).all()
    for i in styles:
        inner = parse_styles(i)
        response[i.style_id]=inner
    return jsonify(response)

@carapp.route('/orderbyqualities')
def order_by_qualities():
    q1 = request.args.get('quality1')
    q2 = request.args.get('quality2')
    q3 = request.args.get('quality3')
    #set up query object, always bringing up largest result.
    #If we get a low quality, multiply by 1/column value
    pq = parse_qualities(q1,q2,q3)
    mult = 1
    for q in pq:
        if q=="High Price":
            mult*=Vehicle_Info.price
        elif q=="Low Price":
            mult*=(1/Vehicle_Info.price)
        elif q=="High Horsepower":
            mult*=Vehicle_Info.hp
        elif q=="Low Horsepower":
            mult*=(1/Vehicle_Info.hp)
        elif q=="High MPG - Highway":
            mult*=Vehicle_Info.mpg_hw
        elif q=="Low MPG - Highway":
            mult*=(1/Vehicle_Info.mpg_hw)
        elif q=="High MPG - City":
            mult*=Vehicle_Info.mpg_city
        elif q=="Low MPG - City":
            mult*=(1/Vehicle_Info.mpg_city)
        elif q=="Torque":
            mult*=Vehicle_Info.torque
        elif q=="Cylinders":
            mult*=Vehicle_Info.cylinders
        elif q=="Number of Wheels":
            mult*=(1/Vehicle_Info.drivenwheels)
        elif q=="Number of Wheels":
            mult*=Vehicle_Info.num_doors
        elif q=="Engine Size":
            mult*=Vehicle_Info.engine_size

    styles = session.query(Vehicle_Info).order_by((mult).desc()).limit(200)
    modelsfound=[]
    response=[]
    for i in styles:
        if len(modelsfound)<26:
            if i.model in modelsfound:
                pass
            else:
                modelsfound.append(i.model)
                response.append(parse_styles(i))

    return jsonify(response)

@carapp.route('/mainsite/<maker>/', methods=['GET','POST'])
def makerStyles(maker):
    styles = session.query(Vehicle_Info.model).distinct().filter_by(maker = maker)
    return render_template("makerstylelist.html",styles=styles)


def parse_styles(i):
    inner = {}
    inner['maker'] = i.maker
    inner['model'] = i.model
    inner['submodel_name'] = i.submodel_name
    inner['model_year']=i.model_year
    inner['style_id'] = i.style_id
    inner['hp'] = i.hp
    inner['cylinders']=i.cylinders
    inner['engine_size']=i.engine_size
    inner['torque']=i.torque
    inner['engine_type']=i.engine_type
    inner['trans_type']=i.trans_type
    inner['trans_num_speeds']=i.trans_num_speeds
    inner['drivenwheels']=i.drivenwheels
    inner['num_doors']=i.num_doors
    inner['price']=i.price
    inner['detailed_name']=i.detailed_name
    inner['mpg_hw']=i.mpg_hw
    inner['mpg_city']=i.mpg_city
    return inner
        


def parse_qualities(q1,q2,q3):
    response = []
    response.append(q1)
    if (q2!="None")and(q2!=q1):
        response.append(q2)
    if (q3!="None")and(q3!=q1)and(q3!=q2):
        response.append(q3)
    return response




if __name__ == '__main__':
    carapp.debug = True
    carapp.run(host = '0.0.0.0', port= 5000)