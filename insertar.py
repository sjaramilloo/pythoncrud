from tkinter import INSERT
import pymysql
try:
    con = pymysql.connect(host='localhost', user='root', password='', db='peliculas')
    try:
        with con.cursor() as cursor:
            consulta = "INSERT INTO peliculas (titulo, anio) VALUES (%s, %s);"
            cursor.execute(consulta, ("Top Gun", 2022))
            cursor.execute(consulta, ("Lo Meteme", 1990))
            cursor.execute(consulta, ("IT", 2020))
        con.commit()
    finally:
        con.close()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Error en la consulta", e)