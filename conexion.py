import pymysql
try:
    con = pymysql.connect(host='localhost', user='root', password='', db='peliculas')
    print("Base de datos conectada")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Error en la conexion ", e)
    