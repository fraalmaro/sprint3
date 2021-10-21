from wtforms import Form, StringField,IntegerField, PasswordField, BooleanField, SubmitField, validators, TextAreaField, SelectField,PasswordField, DateField, HiddenField
from flask import  sessions, session

class Formulario_Contacto(Form):
    nombre = StringField('Nombre y Apellido', 
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=25)
    ] )
    correo = StringField('E-mail',
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=25) 
    ])
    mensaje = TextAreaField('Mensaje',
    [
        validators.DataRequired('Campo Requerido para contacto')
    ])
    enviar = SubmitField('Enviar')

#yefferson comentarios
class Crear_Comentario(Form):
    mensaje = TextAreaField('Comentario',[validators.DataRequired('Campo Requerido ')])
    actividad =  HiddenField('id actividad')
    userlogueado = HiddenField('userlogueado')
    enviar = SubmitField('Enviar')

class listar_actividad(Form):
    listaactividades = SelectField(u'Lista de asignaturas', default=("Seleccionar"))

    enviar = SubmitField('buscar')


#Franklin
class info_Docente(Form):  
    # ape="datos_form[5]" # ced="datos_form[6]" # em="atos_form[7]"...... 
    #StringField(label=None, validators=None, filters=tuple(), description='', id=None, default=None, widget=None, render_kw=None, _form=None, _name=None, _prefix='', _translations=None, _meta=None)
    #                *              *                                                       *                               *
    nombre = StringField('Nombres',  
        [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=40),  
        ],
        #default=nomb
        #render_kw={"placeholder": "you@example.com"},
    )
    apellido = StringField('Apellidos', 
        [ 
            validators.DataRequired('Campo Requerido para contacto'), 
            validators.Length(min=8,max=40),  
        ],
        #default=ape
        
    )
    correo = StringField('E-mail',
        [ 
            validators.DataRequired('Campo Requerido para contacto'), 
            validators.Length(min=8,max=25), 
        ],  
        #default=em,
    )
    cedula = IntegerField('Número de Cedula',
        [
            validators.DataRequired('Ingrese su nùmero de cedula')
        ],
        #default=ced
    )
    codigo_usuario = IntegerField('codigo de usuario',
        
        #   default=cod_user
    )
    pregrado = StringField('Pregrado', 
        [ 
            validators.DataRequired('Campo Requerido para contacto'), 
            validators.Length(min=8,max=40)
        ], 
        #default=preg
    )
    postgrado = StringField('Postgrado', 
        [ 
            validators.DataRequired('Campo Requerido para contacto'), 
            validators.Length(min=8,max=40)
        ],
        #default=post
     )
    asignatura = SelectField('Asignatura', choices=[('a1', 'Asignatura 1'), ('a2', 'Asignatura 2'), ('a3', 'Asignatura 3')])
 
    
    
    
    guardar = SubmitField('Guardar')

#Gabriel
class Formulario_Ingresar(Form):
    usuario = StringField('Usuario', 
    [ 
        validators.DataRequired('Campo Requerido para ingresar'), 
        validators.Length(min=8,max=10)
    ] )
    contrasena = PasswordField('Contraseña',
    [ 
        validators.DataRequired('Campo Requerido para ingresar'), 
        validators.Length(min=8,max=25) 
    ])
    recordar = BooleanField('Recordar Usuario')
    
    login = SubmitField('Login')

class info_Estudiante(Form):
    nombre = StringField('Nombre',
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=40)
    ] )
    apellido = StringField('Apellidos', 
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=40),  
    ])
    facultad = StringField('Facultad', 
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=40)
    ] )
    carrera = StringField('Carrera', 
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=40)
    ] )
    correo = StringField('Correo Electrónico',
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=25) 
    ])
    cedula = IntegerField('Número de Cedula',
    [
        validators.DataRequired('Ingrese su nùmero de cedula')
    ])
    telefono = IntegerField('Telefono/Celular', 
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=40)
    ] )
    codigo = IntegerField('ID Estudiante', 
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=40)
    ] )
    fechaNac = DateField('Fecha de Nacimiento', 
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
    ] )
    pregrado = StringField('Programa', 
        [ 
            validators.DataRequired('Campo Requerido para contacto'), 
            validators.Length(min=8,max=40)
        ])

    # language = SelectField(u'Asignatura', choices=[('a1', 'Asignatura 1'), ('a2', 'Asignatura 2'), ('a3', 'Asignatura 3')])
    guardar = SubmitField('Guardar')

#Claudio
class crear_Actividad(Form):
    nombreActividad = StringField('Nombre de la actividad', 
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=25)
    ] )
    fechaEntrega = StringField('Fecha de Entrega',
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=25) 
    ])
    descripcion = TextAreaField('Descripción de la actividad',
    [
        validators.DataRequired('Campo Requerido para contacto')
    ])
    tipoActividad = SelectField(u'Tipo de Actividad', choices=[('tp1', 'Taller'), ('tp2', 'Quiz'), ('tp3', 'Parcial'), ('tp4', 'ensayo'), ('tp5', 'otros')])
    asignatura = SelectField(u'Asignatura', choices=[('a1', 'Asignatura 1'), ('a2', 'Asignatura 2'), ('a3', 'Asignatura 3')])
    curso = SelectField(u'Curso', choices=[('c1', 'Curso 1'), ('c2', 'Curso 2'), ('c3', 'Curso 3')])
    enviar = SubmitField('Crear Actividad')

#Lennin
class registrar_Estudiante(Form):
    nombre = StringField('Nombre completo', 
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=40)
    ] )
    apellidos = StringField('Apellidos', 
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=40)
    ] )
    codigo = StringField('ID Estudiante', 
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=40)
    ] )
    correo = StringField('Correo Electrónico',
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=25) 
    ])
    programa = SelectField(u'Programa', choices=[('p1', 'Programa 1'), ('p2', 'Programa 2'), ('p3', 'Programa 3')])
    guardar = SubmitField('Guardar')

class registrar_Docente(Form):
    nombre = StringField('Nombre completo', 
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=40)
    ] )
    apellidos = StringField('Apellidos', 
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=40)
    ] )
    codigo = StringField('ID Estudiante', 
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=40)
    ] )
    correo = StringField('Correo Electrónico',
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=25) 
    ])
    materia = SelectField(u'Materia', choices=[('m1', 'Materia 1'), ('m2', 'Materia 2'), ('m3', 'Materia 3')])
    guardar = SubmitField('Guardar')