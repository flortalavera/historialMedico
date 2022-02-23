import tkinter as tk

class Frame(tk.Frame):
    def __init__(self, root):

        super().__init__(root, width=900, height=550)
        self.root = root
        self.pack()
        self.config(bg='#CDD8FF')
        self.camposPaciente()

    def camposPaciente(self):
        #LABELS
        self.lblNombre = tk.Label(self, text='Nombre: ')
        self.lblNombre.config(font=('SANZ',15,'bold'), bg='#CDD8FF')
        self.lblNombre.grid(column=0, row=0, padx=10, pady=5)

        self.lblApellido = tk.Label(self, text='Apellido: ')
        self.lblApellido.config(font=('SANZ',15,'bold'), bg='#CDD8FF')
        self.lblApellido.grid(column=0, row=1, padx=10, pady=5)

        self.lblDni = tk.Label(self, text='DNI: ')
        self.lblDni.config(font=('SANZ',15,'bold'), bg='#CDD8FF')
        self.lblDni.grid(column=0, row=2, padx=10, pady=5)

        self.lblFechNacimiento = tk.Label(self, text='Fecha de Nacimiento: ')
        self.lblFechNacimiento.config(font=('SANZ',15,'bold'), bg='#CDD8FF')
        self.lblFechNacimiento.grid(column=0, row=3, padx=10, pady=5)

        self.lblEdad = tk.Label(self, text='Edad: ')
        self.lblEdad.config(font=('SANZ',15,'bold'), bg='#CDD8FF')
        self.lblEdad.grid(column=0, row=4, padx=10, pady=5)

        self.lblAntecedentes = tk.Label(self, text='Antecedentes: ')
        self.lblAntecedentes.config(font=('SANZ',15,'bold'), bg='#CDD8FF')
        self.lblAntecedentes.grid(column=0, row=5, padx=10, pady=5)

        self.lblEmail = tk.Label(self, text='Email: ')
        self.lblEmail.config(font=('SANZ',15,'bold'), bg='#CDD8FF')
        self.lblEmail.grid(column=0, row=6, padx=10, pady=5)

        self.lblTelefono = tk.Label(self, text='Telefono: ')
        self.lblTelefono.config(font=('SANZ',15,'bold'), bg='#CDD8FF')
        self.lblTelefono.grid(column=0, row=7, padx=10, pady=5)

        #ENTRYS
        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable =self.svNombre)
        self.entryNombre.config(width=50, font=('SANZ',15))
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5,columnspan=2)

        self.svApellido = tk.StringVar()
        self.entryApellido = tk.Entry(self, textvariable =self.svApellido)
        self.entryApellido.config(width=50, font=('SANZ',15))
        self.entryApellido.grid(column=1, row=1, padx=10, pady=5,columnspan=2)

        self.svDni = tk.StringVar()
        self.entryDni = tk.Entry(self, textvariable =self.svDni)
        self.entryDni.config(width=50, font=('SANZ',15))
        self.entryDni.grid(column=1, row=2, padx=10, pady=5,columnspan=2)

        self.svFechNacimiento = tk.StringVar()
        self.entryFechNacimiento = tk.Entry(self, textvariable =self.svFechNacimiento)
        self.entryFechNacimiento.config(width=50, font=('SANZ',15))
        self.entryFechNacimiento.grid(column=1, row=3, padx=10, pady=5,columnspan=2)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable =self.svEdad)
        self.entryEdad.config(width=50, font=('SANZ',15))
        self.entryEdad.grid(column=1, row=4, padx=10, pady=5,columnspan=2)

        self.svAntecedentes = tk.StringVar()
        self.entryAntecedentes = tk.Entry(self, textvariable =self.svAntecedentes)
        self.entryAntecedentes.config(width=50, font=('SANZ',15))
        self.entryAntecedentes.grid(column=1, row=5, padx=10, pady=5,columnspan=2)

        self.svEmail = tk.StringVar()
        self.entryEmail = tk.Entry(self, textvariable =self.svEmail)
        self.entryEmail.config(width=50, font=('SANZ',15))
        self.entryEmail.grid(column=1, row=6, padx=10, pady=5,columnspan=2)

        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable =self.svTelefono)
        self.entryTelefono.config(width=50, font=('SANZ',15))
        self.entryTelefono.grid(column=1, row=7, padx=10, pady=5,columnspan=2)

        #BUTTONS
        self.btnNuevo = tk.Button(self, text='Nuevo')
        self.btnNuevo.config(width=20, font=('SANZ',13,'bold'), fg='#FCFDFE', bg='#277B9B', cursor='hand2', activebackground='#72B2FA')
        self.btnNuevo.grid(column=0,row=8, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text='Guardar')
        self.btnGuardar.config(width=20, font=('SANZ',13,'bold'), fg='#FCFDFE', bg='#2AD20F', cursor='hand2', activebackground='#6CF756')
        self.btnGuardar.grid(column=1,row=8, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text='Cancelar')
        self.btnCancelar.config(width=20, font=('SANZ',13,'bold'), fg='#FCFDFE', bg='#EA2A1A', cursor='hand2', activebackground='#F35F53')
        self.btnCancelar.grid(column=2,row=8, padx=10, pady=5)