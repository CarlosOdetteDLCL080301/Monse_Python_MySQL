"""
Utilice los datos adjuntos (contiene 2 archivos cvs, uno para la historia y otro más reciente, la suma
de ambos es el total de datos) para generar el diagrama ER e impleméntalo en MySQL.
Agregué como entregables:
1.- El código python de creación de sus entidades.
2.- Un pantallazo de su diagrama ER en MySQL Workbench
3.- El código SQL de creación de llaves primaria y relaciones.
"""
#Importamos las funciones necesarias para el codigo
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, VARCHAR, DATETIME, VARCHAR,DOUBLE, create_engine
import pandas as pd
import datetime
hora_actual = datetime.datetime.now()
hora_formateada = hora_actual.strftime("%Y-%m-%d %H:%M:%S")
print("Hora de inicio del programa:", hora_formateada)
#Creamos un programa para que fusione los dos archivos csv
def fusionar_csv(archivo1, archivo2, archivo_salida):
    try:
        # Cargar los dos archivos CSV en DataFrames
        df1 = pd.read_csv(archivo1)
        df2 = pd.read_csv(archivo2)

        # Fusionar los DataFrames
        resultado = pd.concat([df1, df2], ignore_index=True)

        # Guardar el resultado en un nuevo archivo CSV
        resultado.to_csv(archivo_salida, index=False)
        print(f'Fusión exitosa. Los datos se han guardado en "{archivo_salida}".')

    except Exception as e:
        print(f'Error al fusionar los archivos CSV: {str(e)}')

# Se cambio el nombre de los archivos para que se pudieran leer, ya que generaban error
archivo1 = 'Ejemplos/Date.csv'
archivo2 = 'Ejemplos/Historic.csv'
# Es el nombre que va a tener el archivo fusionado
archivo_salida = 'Ejemplos/Total.csv'
fusionar_csv(archivo1, archivo2, archivo_salida)

#Establecemos los parametros para conectarnos
#La conexión se hace con el siguiente formato"mysql+pymysql://usuario:contraseña@host:puerto/nombre_de_la_base_de_datos"
engine = create_engine("mysql+pymysql://root:odette@127.0.0.1/monse")
Base = declarative_base()

#Cargo los datos del archivo csv en un dataframe
data = pd.read_csv('Ejemplos/Total.csv')

##################################################################################
### PD_CD','PD_DESC','KY_CD'
##################################################################################
#Procesamos los datos para que no se repitan
ent_PD_DESC = data[['PD_CD','PD_DESC','KY_CD']].drop_duplicates().reset_index(drop=True)
# Rellenar los valores nulos en la columna 'PD_CD' con 9999999
ent_PD_DESC['PD_CD'].fillna(9999999, inplace=True)
ent_PD_DESC['KY_CD'].fillna(9999999, inplace=True)
#Renombramos las columnas
ent_PD_DESC.columns = ['PD_CD','PD_DESC','KY_CD']
#Convertimos los datos a string
ent_PD_DESC['PD_DESC'] = ent_PD_DESC['PD_DESC'].map(str)
#agregaremos un registro para los valores nulos
nuevoRegistro = [9999999,'N/A',9999999]
ent_PD_DESC.loc[len(ent_PD_DESC)] = nuevoRegistro
#Eliminamos los registros duplicados de la columna 'PD_CD'
ent_PD_DESC = ent_PD_DESC.drop_duplicates(subset=['PD_CD'])
#Definiendo los tipos de datos
dtypes = [Integer, VARCHAR(100), Integer]
#Creamos una tabla en la DB con los datos del datafram
ent_PD_DESC.to_sql(
    name='tbl_PD_DESC',
    con=engine,
    if_exists='replace',
    index=5000,
    dtype=dict(zip(ent_PD_DESC.columns, dtypes))
)

##################################################################################
### LAW_CODE
##################################################################################
#Procesamos los datos para que no se repitan
ent_LAW_Code = data[['LAW_CODE']].drop_duplicates().reset_index(drop=True)
#Agregamos un id a cada registro
ent_LAW_Code.insert(0,'id_LAW_CODE',ent_LAW_Code.index+1)
#Renombramos las columnas
ent_LAW_Code.columns = ['id_LAW_CODE','LAW_CODE']
#Convertimos los datos a string
ent_LAW_Code['LAW_CODE'] = ent_LAW_Code['LAW_CODE'].map(str)
ent_LAW_Code['id_LAW_CODE'].fillna(9999999, inplace=True)
#agregaremos un registro para los valores nulos
nuevoRegistro = [9999999,'N/A']
ent_LAW_Code.loc[len(ent_LAW_Code)] = nuevoRegistro
#Definiendo los tipos de datos
dtypes = [Integer, VARCHAR(100)]
#Creamos una tabla en la DB con los datos del dataframe
ent_LAW_Code.to_sql(
    name='tbl_LAW_Code',
    con=engine,
    if_exists='replace',
    index=5000,
    dtype=dict(zip(ent_LAW_Code.columns, dtypes))
)

##################################################################################
### AGE_GROUP
##################################################################################
#Procesamos los datos para que no se repitan
ent_AGE_GROUP = data[['AGE_GROUP']].drop_duplicates().reset_index(drop=True)
#Agregamos un id a cada registro
ent_AGE_GROUP.insert(0,'id_AGE_GROUP',ent_AGE_GROUP.index+1)
#Renombramos las columnas
ent_AGE_GROUP.columns = ['id_AGE_GROUP','AGE_GROUP']
#Convertimos los datos a string
ent_AGE_GROUP['AGE_GROUP'] = ent_AGE_GROUP['AGE_GROUP'].map(str)
#agregaremos un registro para los valores nulos
nuevoRegistro = [9999999,'N/A']
ent_AGE_GROUP.loc[len(ent_AGE_GROUP)] = nuevoRegistro
#Definiendo los tipos de datos
dtypes = [Integer, VARCHAR(100)]
#Creamos una tabla en la DB con los datos del dataframe
ent_AGE_GROUP.to_sql(
    name='tbl_AGE_GROUP',
    con=engine,
    if_exists='replace',
    index=5000,
    dtype=dict(zip(ent_AGE_GROUP.columns, dtypes))
)

##################################################################################
### PERP_RACE
##################################################################################
#Procesamos los datos para que no se repitan
ent_PERP_RACE = data[['PERP_RACE']].drop_duplicates().reset_index(drop=True)
#Agregamos un id a cada registro
ent_PERP_RACE.insert(0,'id_PERP_RACE',ent_PERP_RACE.index+1)
#Renombramos las columnas
ent_PERP_RACE.columns = ['id_PERP_RACE','PERP_RACE']
#Convertimos los datos a string
ent_PERP_RACE['PERP_RACE'] = ent_PERP_RACE['PERP_RACE'].map(str)
#agregaremos un registro para los valores nulos
nuevoRegistro = [9999999,'N/A']
ent_PERP_RACE.loc[len(ent_PERP_RACE)] = nuevoRegistro
#Definiendo los tipos de datos
dtypes = [Integer, VARCHAR(100)]
#Creamos una tabla en la DB con los datos del dataframe
ent_PERP_RACE.to_sql(
    name='tbl_PERP_RACE',
    con=engine,
    if_exists='replace',
    index=5000,
    dtype=dict(zip(ent_PERP_RACE.columns, dtypes))
)

##################################################################################
### OFNS_DESC
##################################################################################
#Procesamos los datos para que no se repitan
ent_OFNS_DESC = data[['OFNS_DESC']].drop_duplicates().reset_index(drop=True)
#Agregamos un id a cada registro
ent_OFNS_DESC.insert(0,'id_OFNS_DESC',ent_OFNS_DESC.index+1)
#Renombramos las columnas
ent_OFNS_DESC.columns = ['id_OFNS_DESC','OFNS_DESC']
#Convertimos los datos a string
ent_OFNS_DESC['OFNS_DESC'] = ent_OFNS_DESC['OFNS_DESC'].map(str)
ent_OFNS_DESC['id_OFNS_DESC'].fillna(9999999, inplace=True)
#agregaremos un registro para los valores nulos
nuevoRegistro = [9999999,'N/A']
ent_OFNS_DESC.loc[len(ent_OFNS_DESC)] = nuevoRegistro
#Definiendo los tipos de datos
dtypes = [Integer, VARCHAR(100)]
# #Creamos una tabla en la DB con los datos del dataframe
ent_OFNS_DESC.to_sql(
    name='tbl_OFNS_DESC',
    con=engine,
    if_exists='replace',
    index=5000,
    dtype=dict(zip(ent_OFNS_DESC.columns, dtypes))
)
entidadPrincipal = data.copy()
#Reescribimos los valores Nulos
entidadPrincipal['LAW_CAT_CD'] = entidadPrincipal['LAW_CAT_CD'].fillna("N/A").astype(str)
entidadPrincipal['AGE_GROUP'] = entidadPrincipal['AGE_GROUP'].fillna("S/F").astype(str)
entidadPrincipal['PD_CD'].fillna(9999999, inplace=True)
entidadPrincipal['X_COORD_CD'].fillna(9999999, inplace=True)
entidadPrincipal['Y_COORD_CD'].fillna(9999999, inplace=True)
entidadPrincipal['Latitude'].fillna(9999999, inplace=True)
entidadPrincipal['Longitude'].fillna(9999999, inplace=True)
entidadPrincipal['Lon_Lat'] = entidadPrincipal['Lon_Lat'].fillna("N/A").astype(str)

#Hacemos un Join de los demas Dataframe
entidadPrincipal = entidadPrincipal.merge(ent_LAW_Code, how='left', on='LAW_CODE')
entidadPrincipal = entidadPrincipal.merge(ent_AGE_GROUP, how='left', on='AGE_GROUP')
entidadPrincipal = entidadPrincipal.merge(ent_PERP_RACE, how='left', on='PERP_RACE')
entidadPrincipal = entidadPrincipal.merge(ent_OFNS_DESC, how='left', on='OFNS_DESC')
#Eliminamos las columnas que no sirven ahora para nuestra tabla principal
entidadPrincipal.drop('PD_DESC',axis=1,inplace=True)
entidadPrincipal.drop('KY_CD',axis=1,inplace=True)
entidadPrincipal.drop('OFNS_DESC',axis=1,inplace=True)
entidadPrincipal.drop('LAW_CODE',axis=1,inplace=True)
entidadPrincipal.drop('AGE_GROUP',axis=1,inplace=True)
entidadPrincipal.drop('PERP_RACE',axis=1,inplace=True)
# Limpiamos los null de la tabla resultante
entidadPrincipal['id_LAW_CODE'].fillna(9999999, inplace=True)
entidadPrincipal['id_OFNS_DESC'].fillna(9999999, inplace=True)
# Creamos la tabla resultante
#Antes de crear la tabla, debemos definir los tipos de datos, entonces copiamos las columnas y le asignamos un tipo de dato
#           ARREST_KEY, ARREST_DATE,    PD_CD,      LAW_CAT_CD,     ARREST_BORO,    ARREST_PRECINCT,    JURISDICTION_CODE,  PERP_SEX,       X_COORD_CD, Y_COORD_CD,     Latitude,       Longitude,  Lon_Lat     id_LAW_CODE     id_AGE_GROUP    id_PERP_RACE    id_OFNS_DESC
dtypes = [  Integer,    VARCHAR(20),    Integer,    VARCHAR(10),    VARCHAR(10),    Integer,            Integer,            VARCHAR(10),    Integer,     Integer,       DOUBLE,         DOUBLE,    VARCHAR(400),    Integer,        Integer,        Integer,        Integer]
#Creamos una tabla en la DB con los datos del dataframe
entidadPrincipal.to_sql(
    name='tbl_principal',
    con=engine,
    if_exists='replace',
    index=5000,
    dtype=dict(zip(entidadPrincipal.columns, dtypes))
)

hora_final = datetime.datetime.now()
hora_formateada = hora_final.strftime("%Y-%m-%d %H:%M:%S")

print("Hora de finalización del programa:", hora_formateada)