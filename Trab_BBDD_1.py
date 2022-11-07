#comenzando con el trabajo en la base de datos:
#Se crea el motor de la base de datos
url = "mysql://uqv0ak4ucfajzsmq:TnGQaMlLSX8s4lQIqxGs@bxyc0di49xjb9i6s8phk-mysql.services.clever-cloud.com:3306/bxyc0di49xjb9i6s8phk" #url de la bbdd
engine = create_engine(url, echo = False)

mysql_conec = engine.connect()

#Conexion con la base de datos mediante una variable llamada cursor
#Alclaracion: Se debe ejecutar siempre antes de consultas SQL

conec = mysql.connector.connect(
    host="bxyc0di49xjb9i6s8phk-mysql.services.clever-cloud.com", 
    user="uqv0ak4ucfajzsmq",
    passwd="TnGQaMlLSX8s4lQIqxGs",
    database="bxyc0di49xjb9i6s8phk",
    );
cursor = conec.cursor()