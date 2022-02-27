from email import message
from turtle import title
from .conexion import ConexionDB
from tkinter import messagebox

# Creamos las funciones para manejar los datos proporcionados

def guardarDatoPaciente(persona):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Persona (nombre, apellido, dni, fechaNacimiento, 
        edad, antecedentes, email, telefono, activo) VALUES
            ('{persona.nombre}','{persona.apellido}','{persona.dni}','{persona.fechaNacimiento}',
            '{persona.edad}','{persona.antecedentes}','{persona.email}','{persona.telefono}',1)"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar paciente'
        mensaje = 'Paciente registrado exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registrar paciente'
        mensaje = 'Error al registrar paciente'
        messagebox.showerror(title, mensaje)

def listar():
    conexion = ConexionDB()

    listaPersona = []
    sql = 'SELECT * FROM Persona WHERE activo = 1'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Los registros no existe'
        messagebox.showwarning(title, mensaje)
    return listaPersona

def buscarPaciente(where):
    conexion = ConexionDB()
    listaPersona = []
    sql = f'SELECT * FROM Persona {where}'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Los registros no existe'
        messagebox.showwarning(title, mensaje)
    return listaPersona

def eliminarPaciente(idPersona):
    conexion = ConexionDB
    sql = f"""UPDATE Persona SET activo = 0 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar'
        mensaje = 'Los registros han sido eliminados'
        messagebox.showwarning(title, mensaje)
    except:
        title = 'Eliminar'
        mensaje = 'Ocurrió un error al intentar eliminar el registro'
        messagebox.showwarning(title, mensaje)

# Creamos la clase persona para manejar los datos del paciente

class Persona:
    def __init__(self, nombre, apellido, dni, fechaNacimiento, edad, antecedentes, email, telefono):
        self.idPersona = None
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fechaNacimiento = fechaNacimiento
        self.edad = edad
        self.antecedentes = antecedentes
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f'Persona[{self.nombre},{self.apellido},{self.dni},{self.fechaNacimiento},{self.edad},{self.antecedentes},{self.email},{self.telefono}]'
