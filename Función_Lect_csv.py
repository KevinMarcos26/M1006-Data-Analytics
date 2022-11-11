LECTURA CSV
#Hace lectura del CSV y lo retorna en un dataframe

def lectura_csv():
  path = '/content/NewFolder/trips_2021.csv'
  df = pd.read_csv(path, header=0)
  print("read ok")
  return(df)

LIMPIEZA CSV
#Se eliminan las filas con columnas vacias
df_limpio = lectura_csv().dropna(axis = 0)
