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
