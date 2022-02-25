import sqlite3

#Creamos conexion a Base de Datos

class ConexionDB:
    def __init__(self):
        self.baseDatos = 'dataBase/dbhistorial.db'
        self.conexion = sqlite3.connect(self.baseDatos)
        self.cursor = self.conexion.cursor()
    
    def cerrarConexion(self):
        self.conexion.commit()
        self.conexion.close()