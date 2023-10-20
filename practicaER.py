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
#Establecemos los parametros para conectarnos
#La conexión se hace con el siguiente formato"mysql+pymysql://usuario:contraseña@host:puerto/nombre_de_la_base_de_datos"
engine = create_engine("mysql+pymysql://root:odette@127.0.0.1/monse")
Base = declarative_base()
#Damos las caracteristicas de la entidad de nuestra tabla de nuesta DB
class User(Base):
    __tablename__= "nyc_arrests"                #Asignamos un nombre a nuestra tabla
    ARREST_KEY          = Column(Integer(),primary_key=True)     #Definimos de tipo INT
    ARREST_DATE         = Column(VARCHAR(20))
    PD_CD               = Column(Integer())     #Definimos de tipo INT
    PD_DESC             = Column(VARCHAR(60))   #La maxima cadena encontrada fue de 54, pero se deja 60 para posibles casos
    KY_CD               = Column(Integer())     #Definimos de tipo INT
    OFNS_DESC           = Column(VARCHAR(100))   #La maxima cadena encontrada fue de 36, pero se deja 40 para posibles casos
    LAW_CODE            = Column(VARCHAR(15))   #La maxima cadena encontrada fue de 10, pero se deja 15 para posibles casos
    LAW_CAT_CD          = Column(VARCHAR(10))    #La maxima cadena encontrada fue de 1
    ARREST_BORO         = Column(VARCHAR(1))    #La maxima cadena encontrada fue de 1
    ARREST_PRECINCT     = Column(Integer())     #Definimos de tipo INT
    JURISDICTION_CODE   = Column(Integer())     #Definimos de tipo INT
    AGE_GROUP           = Column(VARCHAR(10))   #La maxima cadena encontrada fue de 10, pero se deja 15 para posibles casos
    PERP_SEX            = Column(VARCHAR(1))    #La maxima cadena encontrada fue de 1
    PERP_RACE           = Column(VARCHAR(45))   #La maxima cadena encontrada fue de 30, pero se deja 45 para posibles casos
    X_COORD_CD          = Column(Integer())     #Definimos de tipo INT
    Y_COORD_CD          = Column(Integer())     #Definimos de tipo INT
    Latitude            = Column(DOUBLE())      #Como se maneja punto decimal, usamos un double para "precisión"
    Longitude           = Column(DOUBLE())      #Como se maneja punto decimal, usamos un double para "precisión"
    Lon_Lat             = Column(VARCHAR(400))   #La maxima cadena encontrada fue de 45, pero se deja 50 para posibles casos

    #En caso de llamar esta función, retorna el nombre de la clase
    def __str__(self):
        return self.username
    
Session = sessionmaker(engine)
#Existe la sesión, pero aun no es utilizada 
session = Session()

#Si se ejecuta este código, se crean las tablas en la DB
Base.metadata.create_all(engine)

#Cargo los datos del archivo csv en un dataframe
data = pd.read_csv('Ejemplos/Date.csv')

##################################################################################
### PD_CD','PD_DESC','KY_CD'
##################################################################################
#Procesamos los datos para que no se repitan
ent_PD_DESC = data[['PD_CD','PD_DESC','KY_CD']].drop_duplicates().reset_index(drop=True)
#Agregamos un id a cada registro
#ent_PD_DESC.insert(0,'id_PD_DESC',ent_PD_DESC.index+1)
#Renombramos las columnas
ent_PD_DESC.columns = ['PD_CD','PD_DESC','KY_CD']
#Convertimos los datos a string
ent_PD_DESC['PD_DESC'] = ent_PD_DESC['PD_DESC'].map(str)
#Definiendo los tipos de datos
dtypes = [Integer, VARCHAR(100), Integer]
#Creamos una tabla en la DB con los datos del dataframe
# ent_PD_DESC.to_sql(
#     name='tbl_PD_DESC',
#     con=engine,
#     if_exists='replace',
#     index=5000,
#     dtype=dict(zip(ent_PD_DESC.columns, dtypes))
# )
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
#Definiendo los tipos de datos
dtypes = [Integer, VARCHAR(100)]
#Creamos una tabla en la DB con los datos del dataframe
# ent_LAW_Code.to_sql(
#     name='tbl_LAW_Code',
#     con=engine,
#     if_exists='replace',
#     index=5000,
#     dtype=dict(zip(ent_LAW_Code.columns, dtypes))
# )

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
#Definiendo los tipos de datos
dtypes = [Integer, VARCHAR(100)]
#Creamos una tabla en la DB con los datos del dataframe
# ent_AGE_GROUP.to_sql(
#     name='tbl_AGE_GROUP',
#     con=engine,
#     if_exists='replace',
#     index=5000,
#     dtype=dict(zip(ent_AGE_GROUP.columns, dtypes))
# )

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
#Definiendo los tipos de datos
dtypes = [Integer, VARCHAR(100)]
#Creamos una tabla en la DB con los datos del dataframe
# ent_PERP_RACE.to_sql(
#     name='tbl_PERP_RACE',
#     con=engine,
#     if_exists='replace',
#     index=5000,
#     dtype=dict(zip(ent_PERP_RACE.columns, dtypes))
# )

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
#Definiendo los tipos de datos
dtypes = [Integer, VARCHAR(100)]
# #Creamos una tabla en la DB con los datos del dataframe
# ent_OFNS_DESC.to_sql(
#     name='tbl_OFNS_DESC',
#     con=engine,
#     if_exists='replace',
#     index=5000,
#     dtype=dict(zip(ent_OFNS_DESC.columns, dtypes))
# )
print(data.head(2))
print(ent_LAW_Code.head())
entidadPrincipal = data.copy()
#Reescribimos los valores Nulos
entidadPrincipal['LAW_CAT_CD'] = entidadPrincipal['LAW_CAT_CD'].fillna("N/A").astype(str)
entidadPrincipal['AGE_GROUP'] = entidadPrincipal['AGE_GROUP'].fillna("S/F").astype(str)
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

print(entidadPrincipal.head(2))
print(ent_OFNS_DESC.head(2))
# ##################################################################################
# ### En caso de querer tener la tabla completa del CVS en la DB descomentar las siguientes lineas
# ##################################################################################
# data = data.sample(10000).reset_index(drop=True)
# data.to_sql('nyc_arrests', con=engine, if_exists='append', index=False)

# data = pd.read_csv('Ejemplos/Historic.csv')
# data.shape
# data = data.sample(10000).reset_index(drop=True)
# data.to_sql('nyc_arrests', con=engine, if_exists='append', index=False)