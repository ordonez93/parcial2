from flask import flash
from mysql.connector import connection
from models import dataBases
import mysql.connector

def coneccion(host,user,password,database,port):
    DB=mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
    port=port
    )
    return DB


def getDatabases(DB):
    
    verbases = dataBases.getDatabases(DB)
    return verbases




def crearBase(DB,nombre):
   
    crear=dataBases.crearBase(DB,nombre)
    return crear
    
    



    