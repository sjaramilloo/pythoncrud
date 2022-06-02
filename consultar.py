import pymysql
try:
    con = pymysql.connect(host='localhost', user='root', password='', db='peliculas')
    try:
        with con.cursor() as cursor:
            cursor.execute("SELECT  id, titulo, anio FROM peliculas;")

            peliculas = cursor.fetchall()

            for pelicula in peliculas:
                print(pelicula)
    finally:
        con.close()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Error en la consulta ", e)
