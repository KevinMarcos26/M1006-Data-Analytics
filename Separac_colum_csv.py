#Separando las columnas del CSV en dataframes individuales (de acuerdo a las distintas tablas)

#Corresponde a la tabla "RECORRIDO"
#Aclaracion: Esta tabla es la unica que contiene todos los registros del CSV original

df_recorrido = pd.DataFrame(df_limpio, columns = ['id_recorrido', 'id_usuario', 'id_estacion_origen', 'id_estacion_destino', 'duracion_recorrido'])
df_recorrido = df_recorrido.drop_duplicates(['id_recorrido'])

df_recorrido.to_csv("recorrido.csv")
df_recorrido.head()

#Corresponde a la tabla "USUARIO"
#Aclaracion: Solo se utiliza los id sin repetir, porque son los unicos que se necesitan y se pueden utilizar en la tabla con id "primary key" de MySQL

df_usuario = pd.DataFrame(df_limpio, columns = ['id_usuario', 'modelo_bicicleta'])

#Se eliminan los id duplicados
df_usuario = df_usuario.drop_duplicates(['id_usuario'])

df_usuario.to_csv("usuario.csv")

#Corresponde a la tabla "ESTACION_ORIGEN"
#Aclaracion: Solo se utiliza los id sin repetir, porque son los unicos que se necesitan y se pueden en utilizar en la tabla con id "primary key" de MySQL

df_estacion_origen = pd.DataFrame(df_limpio, columns = ['id_estacion_origen', 'nombre_estacion_origen', 'direccion_estacion_origen', 'long_estacion_origen', 'lat_estacion_origen', 'fecha_origen_recorrido' ])

#Se eliminan los id duplicados
df_estacion_origen = df_estacion_origen.drop_duplicates(['id_estacion_origen'])

df_estacion_destino.to_csv("destino.csv")