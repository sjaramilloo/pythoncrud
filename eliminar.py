import pymysql
try:
    con = pymysql.connect(host='localhost', user='root', password='', db='peliculas')
    try:
        with con.cursor() as cursor:
            consulta = "DELETE FROM peliculas WHERE anio = %s;"
            anio_nuevo = 2020 
            cursor.execute(consulta,(anio))
        con.commit()
    finally:
        con.close()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Error en la conexion ", e)
    