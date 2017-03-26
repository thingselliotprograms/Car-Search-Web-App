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
    count = 0
    for maker in makers:
        count+=1
    return render_template("carmodellist.html",makers=makers,count=count)

@carapp.route('/mainsite/<maker>/', methods=['GET','POST'])
def makerStyles(maker):
    styles = session.query(Vehicle_Info).filter_by(maker = maker).all()
    return render_template("makerstylelist.html",styles=styles)



if __name__ == '__main__':
    carapp.debug = True
    carapp.run(host = '0.0.0.0', port= 5000)