# *Aclaracion!!!!: * Las tablas se crean con datos de tipo caracteres alfabeticos, para evitar incompativilidades en la carga de datos a la base de datos. Igualmente se debe 
# convertir a string cada dato al momento de agregar registros en la base de datos. Luego se deben reconvertir al momento de calcular estadisticas y demas.

#Creacion de tabla "RECORRIDO":
cursor.execute('CREATE TABLE RECORRIDO(pk_id_recorrido varchar(40) primary key, fk_id_usuario varchar(40), fk_id_estacion_origen varchar(40), fk_id_estacion_destino varchar(40), duracion_recorrido varchar(40))')
conec.close() 

#Creacion de tabla "USUARIO":
cursor.execute('CREATE TABLE USUARIO(pk_id_usuario VARCHAR(40) primary key, modelo_bici VARCHAR(30))')
conec.close()

#Creacion de tabla "ESTACION_ORIGEN"
#ACALARACION: 
#latitud, longitud y fecha se guardan en la tabla en formato string

cursor.execute('CREATE TABLE ESTACION_ORIGEN(pk_id_estacion_origen INTEGER primary key, nombre_estacion_origen VARCHAR(35), direccion_estacion_origen VARCHAR(50), longitud_estacion_origen VARCHAR(35), latitud_estacion_origen VARCHAR(35), fecha_origen_recorrido VARCHAR(35))')
conec.close()

#Creacion de tabla "ESTACION_DESTINO"

cursor.execute('CREATE TABLE ESTACION_DESTINO(pk_id_estacion_destino INTEGER primary key, nombre_estacion_destino VARCHAR(35), direccion_estacion_destino VARCHAR(50), longitud_estacion_destino VARCHAR(35), latitud_estacion_destino VARCHAR(35), fecha_destino_recorrido VARCHAR(35))')
conec.close()

#Se le asigna la relacion de las claves foraneas de la tabla "RECORRIDO" con sus correspondiente tabla

#fk_id_usuario
cursor.execute('ALTER TABLE RECORRIDO ADD FOREIGN KEY(fk_id_usuario) REFERENCES USUARIO(pk_id_usuario)')
#fk_id_estacion_origen
cursor.execute('ALTER TABLE RECORRIDO ADD FOREIGN KEY(fk_id_estacion_origen) REFERENCES ESTACION_ORIGEN(pk_id_estacion_origen)')
#fk_id_estacion_destino
cursor.execute('ALTER TABLE RECORRIDO ADD FOREIGN KEY(fk_id_estacion_destino) REFERENCES ESTACION_DESTINO(pk_id_estacion_destino)')
conec.close()

# --- Inserción de datos de las columnas del CSV a las correspondientes tablas de la base de datos -----
#Pasar datos desde CSV a sus correspondiente tablas

#1)Recorrido
db = "bxyc0di49xjb9i6s8phk"
table = "RECORRIDOS"
path = "/content/recorrido.csv"

url = "mysql://uqv0ak4ucfajzsmq:TnGQaMlLSX8s4lQIqxGs@bxyc0di49xjb9i6s8phk-mysql.services.clever-cloud.com:3306/bxyc0di49xjb9i6s8phk"

engine = create_engine(url, echo = False)

df = pd.read_csv(path)

print ("Lectura correcta")

df.to_sql(name = table, con = engine, index = False)

#2)Usuario
db = "bxyc0di49xjb9i6s8phk"
table = "USUARIO"
path = "/content/usuario.csv"

url = "mysql://uqv0ak4ucfajzsmq:TnGQaMlLSX8s4lQIqxGs@bxyc0di49xjb9i6s8phk-mysql.services.clever-cloud.com:3306/bxyc0di49xjb9i6s8phk"

engine = create_engine(url, echo = False)

df = pd.read_csv(path)

print ("lectura correcta")

df.to_sql(name = table, con = engine, index = False)

#3)Origen
db = "bxyc0di49xjb9i6s8phk"
table = "ESTACION_ORIGEN"
path = "/content/origen.csv"

url = "mysql://uqv0ak4ucfajzsmq:TnGQaMlLSX8s4lQIqxGs@bxyc0di49xjb9i6s8phk-mysql.services.clever-cloud.com:3306/bxyc0di49xjb9i6s8phk"

engine = create_engine(url, echo = False)

df = pd.read_csv(path)

print ("Lectura correcta")

df.to_sql(name = table, con = engine, index = False)

#4)Destino
db = "bxyc0di49xjb9i6s8phk"
table = "ESTACION_DESTINO"
path = "/content/destino.csv"

url = "mysql://uqv0ak4ucfajzsmq:TnGQaMlLSX8s4lQIqxGs@bxyc0di49xjb9i6s8phk-mysql.services.clever-cloud.com:3306/bxyc0di49xjb9i6s8phk"

engine = create_engine(url, echo = False)

df = pd.read_csv(path)

print ("Lectura correcta")

df.to_sql(name = table, con = engine, index = False)