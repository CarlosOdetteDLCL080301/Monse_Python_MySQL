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
    LAW_CAT_CD          = Column(VARCHAR(1))    #La maxima cadena encontrada fue de 1
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
data.shape
data = data.sample(10000).reset_index(drop=True)
data.head(2)
data.to_sql('nyc_arrests', con=engine, if_exists='append', index=False)

data = pd.read_csv('Ejemplos/Historic.csv')
data.shape
data = data.sample(10000).reset_index(drop=True)
data.head(2)
data.to_sql('nyc_arrests', con=engine, if_exists='append', index=False)