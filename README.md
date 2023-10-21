# Ejercicio solicitado
Utilice los datos adjuntos (contiene 2 archivos cvs, uno para la historia y otro más reciente, la suma
de ambos es el total de datos) para generar el diagrama ER e impleméntalo en MySQL.
Agregué como entregables:
1. El código python de creación de sus entidades.
2. Un pantallazo de su diagrama ER en MySQL Workbench
3. El código SQL de creación de llaves primaria y relaciones.
*__NOTA__: los archivos utilizados no se encuentran en este repositorio, ya que tenian un peso que no soporta GitHub, presiona [DESCARGAR](https://comunidadunammx-my.sharepoint.com/:f:/r/personal/carlosodettedlcl01_comunidad_unam_mx/Documents/Archivos%20para%20el%20ejercicio%20CVS?csf=1&web=1&e=kXABzS)*

## Ejecutar programas
Para cubrir con los requisitos de este ejercicio es necesario ejecutar unicamente los siguientes archivos:
- practicaER.py
- relaciones.sql

Si se quiere ver desde el inicio el diagrama Entidad - Relacional que se genera al ejecutar todo, se puede ver desde e archivo *Final.mwb*

## Como ejecutar
### 1. Primero ejecutar el archivo python
El programa esta diseñado de manera que solo requiera presionar **Ejecutar**, directamente en el archivo "*practicaER.py*"
#### Consideraciones importantes
1. Se cambio el nombre de las CVS, ya que generaba un error, entonces la solución rapida fue dicho cambio
2. Cuando se descarga los cvs, es necesario que sean almacenados en ***./Ejemplos***, ya que se diseño el programa para que se mantenga en ese directorio
3. Tener instalados la bibliotecas utilizadas
    - *Pandas*
    - *SQLAlchemy*

    En caso de no tener instalados, ejecuta los siguientes comandos
    - SQLAlchemy 2.0.22
        
        ***¿Que es SQLAlchemy?***

        SQLAlchemy es el kit de herramientas SQL de Python y el Mapeador de Objetos Relacionales que brinda a los desarrolladores de aplicaciones el poder y la flexibilidad completos de SQL. SQLAlchemy proporciona un conjunto completo de patrones de persistencia de nivel empresarial bien conocidos, diseñados para un acceso eficiente y de alto rendimiento a bases de datos, adaptados a un lenguaje de dominio simple y pythonico.

        **INSTALAR BIBLIOTECA**
        ~~~
        pip install SQLAlchemy
        ~~~
    - Pandas

        ***¿Que es pandas?***

        Pandas es un paquete de Python que proporciona estructuras de datos rápidas, flexibles y expresivas diseñadas para hacer que trabajar con datos "relacionales" o "etiquetados" sea fácil e intuitivo. Su objetivo es ser el bloque de construcción de alto nivel fundamental para realizar análisis de datos prácticos del mundo real en Python. Además, tiene el objetivo más amplio de convertirse en la herramienta de análisis/manipulación de datos de código abierto más potente y flexible disponible en cualquier idioma. Ya está bien encaminado hacia este objetivo.

        **INSTALAR BIBLIOTECA** 
        ~~~
        pip install pandas
        ~~~
4. Otro elemento importante, es establecer correctamente el enlace a la base de datos, entonces es vital modificar la linea 44 de codigo, la cual recibe una cadena de caracteres que tiene el siguiente formato *mysql+pymysql://usuario:contraseña@host:puerto/nombre_de_la_base_de_datos*, el cual cada parte significa: 
    * sql+pymysql://: Esto indica el motor de base de datos que se utilizará. En este caso, se está utilizando MySQL como el motor de base de datos, y el controlador (driver) subyacente que se utilizará es PyMySQL, una biblioteca de Python que proporciona una interfaz para MySQL.
    Es normal si nos da un error de no encontrar instalado la biblioteca pymysql, entonces con el siguiente comando lo instalamos:
        ~~~
        pip install pymysql
        ~~~
    * usuario: Debes reemplazar esto con el nombre de usuario de la base de datos que deseas utilizar. Este es el nombre de usuario con el que te autenticarás en la base de datos.
    * contraseña: Aquí se debe proporcionar la contraseña correspondiente al usuario que se mencionó anteriormente. Esta contraseña se utiliza para autenticarse en la base de datos.
    * host: Debes especificar la dirección o el nombre del servidor donde se encuentra la base de datos MySQL a la que deseas conectarte. Puede ser una dirección IP o un nombre de host.
    * puerto: Este es el número de puerto en el que el servidor de la base de datos MySQL está escuchando. El valor predeterminado para MySQL es 3306.
    * nombre_de_la_base_de_datos: Aquí debes proporcionar el nombre de la base de datos a la que deseas conectarte. SQLAlchemy utilizará esta base de datos una vez que se haya establecido la conexión.

5. Si ya ejecutaste una vez, el programa se ejecuto correctamente o se corrompio en el proceso, si intentas ejecutarlo una vez más no te dará acceso por que ya existe la tabla que se intenta crear, para repetir el programa, antes tienes que ejecutar el archivo *ScriptVisualizar.sql*, para reiniciar todo y repetir.

    **NOTA: Se acualizará para que se automatice este proceso**

5. Ejecutar este programa no es rapido, ya que el procesamiento de texto plano y en dimensiones grandes toma su tiempo, en mi caso, con mi computadora, finaliza este programa aproximadamente en 5 minutos.

### 2. Ejecutar archivo en MySQL
El programa esta diseñado de manera que solo requiera presionar **⚡**(*Execute the select portion or eveything, if there is no selection*), directamente en el archivo "*Relaciones_tablas.py*"
#### Consideraciones importantes
1. Tener previamente creado la base de datos, en el diseño del programa se diseñó para que trabaje en el DB nombrado como "monse". En caso de no tener uno creado, te muestro un ejemplo de como hacerlo

    ```
    -- Creamos nuestro database
    CREATE DATABASE montse;
    -- Comprobamos que se creo correctamente nuestra DB, se mostraran todas las DB existentes
    show databases;
    -- Utilizamos nuestro DB creado para trabajar todo en él
    use montse;
    ```    

2. Ejecutar despues de que se ejecuto el programa en python, si no simplemente no creara nada, ya que las entidades aun no existen.
3. Existe la posibilidad de que el programa se interrumpa a pesar de tener el script, se encuentra funcionando correctamente, el error que posiblemente se mostrará es "*Error Code: 2013. Lost connection to MySQL server during query	30.015 sec*", por defecto MySQL WorkBench, esta configurado para que solo trabaje 30 segundos en un Query, pero al ser mucha información se demorá mas tiempo de lo normal con las entidades pequeñas. Para solucionar esto es configurarlo, el cual es dirigirse a ***Edit > Preferences > SQL Editor > MySQL Session > DBMS connection read timeout interval (in seconds)***, cambiar el valor que tiene, por uno apropiado para la magnitud, en mi caso lo deje con "30 segundos".
4. Si ya ejecutaste una vez, el programa se ejecutó correctamente o se corrompió en el proceso, si intentas ejecutarlo una vez más no te dará acceso por que ya existe la tabla que se intenta crear, para repetir el programa, antes tienes que ejecutar el archivo *ScriptVisualizar.sql*, para reiniciar todo.

### Obtener el diagrama entidad - relacional
El diagrama se puede ver desde ahora, solo se necesita ejecutar el archivo *final.mwb*, sin embargo si se quiere obtener desde cero, antes se tuvo que ejecutar los pasos anteriores.
#### Pasos para obtener el diagraa ER
1. Ejecutar las intrucciones pasadas.
2. Fijarse a la barra de instrucciones, presionamos la pestaña **Database > Reverse Engineer**
3. Se despliega una nueva ventana, dejamos los valores sin modificar nada y presionamos **Next**, ingresamos nuestras contraseña root.
4. Cuando se actualice la ventana con ***Connect to DBMS and Fetch Information***, solo presionamos en *Next*.
5. Cuando se actualice a ***Select the schemas you want to include***, seleccionamos nuestra base de datos a la que queremos obtener el diagrama de Entidad Relacional, en nuestro caso es Montse.
5. En ***Retrieve and Reverse Engineer Schema Objects***, solo presionamos **Next**.
6. En ***Select Objects to Reverse Engineer***, seleccionamos todos los checkbox y presionamos **Execute >**.
7. En ***Reverse Engineering Progress***, solo esperamos que termine, para poder presionar **Next**.
8. Una vez estando en ***Reverse Engineering Results***, presionamos **Finish**. 
10. Y así obtenemos nuestro diagrama Entidad.
cuando tenemos el diagrama generado y podemos procesarlo como exportarlo, en un PNG, en nuestro caso se ve así...

(IMAGEN)