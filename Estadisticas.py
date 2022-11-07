# Obteniendo estadisticas
# Encontrar bases de datos

cursor.execute("show databases")
for db in cursor:
  print(db)

conec.close()
# ---------------------------------

#Encontrar tablas 

cursor.execute("show tables")
for tbl in cursor:
  print(tbl)
conec.close() 
# ---------------------------------

#Mostrar todas las filas

sql="select * from bicicletas"
cursor.execute(sql)

for fila in cursor:
  print(fila)

conec.close()
# --------------------------------

#Saber numero de registros

from pandas.core.series import FillnaOptions}
sql="select count(*) from bicicletas"
cursor.execute(sql)

for fila in cursor:
  print(fila)

conec.close()
# --------------------------------

#Saber promedio de duracion de viajes

from pandas.core.series import FillnaOptions
sql="select round(AVG(`duracion_recorrido`)/60) from bicicletas"

cursor.execute(sql)
for fila in cursor:
  print(fila)

conec.close()
# -------------------------------

#Saber estaciones de partida u origen

from pandas.core.series import FillnaOptions
sql="SELECT COUNT(DISTINCT `nombre_estacion_origen`) FROM bicicletas"

cursor.execute(sql)
for fila in cursor:
  print(fila)
  
conec.close()
# --------------------------------

#SABER ESTACIONES DE DESTINO
from pandas.core.series import FillnaOptions
sql="SELECT COUNT(DISTINCT `nombre_estacion_destino`) FROM bicicletas"

cursor.execute(sql)
for fila in cursor:
  print(fila)

conec.close()
# -------------------------------
#SABER CANTIDAD DE MODELOS DE BICICLETAS UTILIZADAS
from pandas.core.series import FillnaOptions
sql="SELECT COUNT(DISTINCT `modelo_bicicleta`) FROM bicicletas"

cursor.execute(sql)
for fila in cursor:
  print(fila)

conec.close()
# -------------------------------
#SABER MODELOS DE BICICLETAS UTILIZADAS
from pandas.core.series import FillnaOptions
sql="SELECT DISTINCT `modelo_bicicleta` FROM bicicletas"

cursor.execute(sql)
for fila in cursor:
  print(fila)

conec.close()
# -------------------------------

"""INFORME

Analisís de información de base de datos online

El gobierno de la Ciudad de Buenos Aires recolecta datos acerca del uso de los servicios de bicicletas públicas denominado ecobici y publica 
parte de ellos.

Para este ejemplo usaremos los viajes de la base de datos del 2021. Nuestro objetivo es conocer más acerca del uso que le dan los usuarios 
al sistema,para ver las posibilidades de emplear dicho sistema en otras jurisdicciones, por lo cual se desea 
extraer la siguiente información:

1) ¿Cuál es la duración promedio de cada viaje? (Los datos están en segundos) 
2)¿A qué hora del día se realizaron más viajes? (por ejemplo: de 16hs a 17hs) 
3)¿Cuántas estaciones diferentes fueron utilizadas? 
4)Para cada estación utilizada como inicio de un viaje, ver la cantidad de viajes que iniciaron en la misma. 
5) Efectuar visualizaciones de los insights generados en la presente investigación"""