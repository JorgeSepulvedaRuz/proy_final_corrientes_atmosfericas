import csv
import logging
import os
import coloredlogs
import redis as redis
import json
import mariadb
from operator import or_
from dotenv import load_dotenv
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session
from modelos_p1 import DataJson #importo los json

Logger=logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')
load_dotenv()
#creo la sesión
engine=create_engine(os.getenv('DATABASE')) #desde env
sesion=Session(engine)
#conexión a redis
r=redis.Redis(host=os.getenv('REDIS_HOST'),
	          port=int(os.getenv('REDIS_PORT')),
	          password=os.getenv('REDIS_PASSWORD'),db=0)

#1.- crear tabla con los atributos del json
creacion = """create table P1_parte1
                (
                    id_personaje    int null,
                    nombre          varchar null,
                    signo_zodiaco   varchar null,
                    comida_favorita varchar null
                )"""

#2.- crear modelos de sql_alchemy
#se hizo corriendo "sqlacodegen mariadb://root:flor@localhost/c3basesp1 --noinflect --outfile modelos_p1.py


#3.- usando sqlalchemy lea data_json, parsee con oython
#e inserte en la tabla de la parte 1
datos_json = sesion.query(DataJson)
#iterar sobre los jsons
contador=1
for row in datos_json:
	#pasar a dict
	contador+=1
	get_json = json.loads(row)
	nuevo_dic = {'id_personaje':contador,
				 'signo_zodiaco':get_json[0],
				 'comida_favorita':get_json[1],
				 'nombre':get_json[2]}
	session.execute(insert(p1parte1).values())




#4.- haga un conteo agrupando por signo zodiacal


#5.- sqlacl

#6.- sqlacl

#7.-

#8.-

#9.-

#10.- te odio sqlalchemy :')