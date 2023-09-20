import mysql.connector
from mysql.connector import Error

class crud:
    def __init__(self):
        print("Inicializando la conexion con la base de datos")
        self.conexion = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="", 
            database="db_academico")
        if self.conexion.is_connected():
            print("Conexion exitosa")
        else:
            print("Error de conexion")

    def consultar(self, sql):
        cursor = self.conexion.cursor()
        cursor.execute(sql)
        return cursor.fetchall()