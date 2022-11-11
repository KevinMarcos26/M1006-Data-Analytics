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

#Saber promedio de duracion de viajes

from pandas.core.series import FillnaOptions
sql="select round(AVG(`duracion_recorrido`)/60) from RECORRIDOS"

cursor.execute(sql)
for fila in cursor:
  print(fila)

conec.close()

#Saber estaciones de partida u origen

from pandas.core.series import FillnaOptions
sql="SELECT COUNT(DISTINCT `nombre_estacion_origen`) FROM ESTACION_ORIGEN"

cursor.execute(sql)
for fila in cursor:
  print(fila)
  
conec.close()

#SABER ESTACIONES DE DESTINO
from pandas.core.series import FillnaOptions
sql="SELECT COUNT(DISTINCT `nombre_estacion_destino`) FROM ESTACION_DESTINO"

cursor.execute(sql)
for fila in cursor:
  print(fila)

conec.close()

#SABER CANTIDAD DE MODELOS DE BICICLETAS UTILIZADAS
from pandas.core.series import FillnaOptions
sql="SELECT COUNT(DISTINCT `modelo_bicicleta`) FROM USUARIO"

cursor.execute(sql)
for fila in cursor:
  print(fila)

conec.close()

#SABER MODELOS DE BICICLETAS UTILIZADAS
from pandas.core.series import FillnaOptions
sql="SELECT DISTINCT `modelo_bicicleta` FROM USUARIO"

cursor.execute(sql)
for fila in cursor:
  print(fila)

conec.close()

#SABER ESTACION DE ORIGEN MAS y MENOS UTILIZADA
from pandas.core.series import FillnaOptions
sql="SELECT id_estacion_origen, COUNT( id_estacion_origen ) AS total FROM  RECORRIDOS GROUP BY id_estacion_origen ORDER BY total DESC"

cursor.execute(sql)
for fila in cursor:
  print(fila)

conec.close()

#SABER ESTACION DE DESTINO MAS Y MENOS UTILIZADA
from pandas.core.series import FillnaOptions
sql="SELECT id_estacion_destino, COUNT( id_estacion_destino ) AS total FROM  RECORRIDOS GROUP BY id_estacion_destino ORDER BY total DESC"

cursor.execute(sql)
for fila in cursor:
  print(fila)

conec.close()
