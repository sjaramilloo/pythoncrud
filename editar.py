import pymysql
try:
    con = pymysql.connect(host='localhost', user='root', password='', db='peliculas')
    try:
        with con.cursor() as cursor:
            consulta = "UPDATE peliculas SET titulo = %s WHERE id = %s;"
            titulo_nuevo = "La francesa"
            id_nuevo = 2
            cursor.execute(consulta, (titulo_nuevo, id_nuevo))
        con.commit()
    finally:
        con.close()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Error en la conexion ", e)
    