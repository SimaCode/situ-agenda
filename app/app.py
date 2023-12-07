# app.py
# Aplicación Flask para gestionar citas médicas.
# Incluye modelos para usuarios, profesionales y pacientes, así como funcionalidades de registro, login y citas.

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate

# Configuración de la aplicación Flask
app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY']='situ_clave_secreta'

# Configuración de extensiones
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app, supports_credentials=True)

# Configuración de gestión de usuarios
login_manager = LoginManager(app)
login_manager.login_view = None

# Definición del modelo de usuario base
class User(UserMixin, db.Model):
    # Modelo base para usuarios
    # Atributos: id, name, last_name, email, number, password, role
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80))
    role = db.Column(db.String(20))
    __mapper_args__ = {
        'polymorphic_identity':'user',
        'polymorphic_on':role
    }

# Modelo para profesionales
class Profesional(User):
    # Modelo para profesionales que hereda de User
    # Atributos adicionales: especialidad
    __tablename__ = 'profesional'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    especialidad = db.Column(db.String(50))
    __mapper_args__ = {
        'polymorphic_identity':'profesional',
    }

# Modelo para pacientes
class Paciente(User):
    # Modelo para pacientes que hereda de User
    # Atributos adicionales: comuna, direccion
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    comuna = db.Column(db.String(50))
    direccion = db.Column(db.String(120))
    __mapper_args__ = {
        'polymorphic_identity':'paciente',
    }

# Modelo para disponibilidades
class Disponibilidad(db.Model):
    # Modelo para representar disponibilidades
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('user.id'))
    fecha = db.Column(db.String(50))
    hora_inicio = db.Column(db.String(50))
    hora_fin = db.Column(db.String(50))
    estado = db.Column(db.String(50))

# Modelo para citas
class Cita(db.Model):
    # Modelo para representar citas
    id = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    id_profesional = db.Column(db.Integer, db.ForeignKey('profesional.id'))
    id_disponibilidad = db.Column(db.Integer, db.ForeignKey('disponibilidad.id'))
    estado = db.Column(db.String(50))

# Función para cargar un usuario desde la base de datos utilizando su ID.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ruta restful para registrar un usuario
@app.route('/api/register', methods=['POST'])
def register():
    # Recibe datos JSON y crea un nuevo usuario en la base de datos.
    if request.method == 'POST':
        name = request.json['name']
        last_name = request.json['last_name']
        email = request.json['email']
        password = request.json['password']
        role = request.json['role']

        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({'message': 'El Email ya existe, prueba otro'}), 400

        if role == 'profesional':
            especialidad = request.json['especialidad']
            new_user = Profesional(name=name, last_name=last_name, email=email, password=password, role=role, especialidad=especialidad)
        elif role == 'paciente':
            comuna = request.json['comuna']
            direccion = request.json['direccion']
            new_user = Paciente(name=name, last_name=last_name, email=email, password=password, role=role, comuna=comuna, direccion=direccion)
        else:
            return jsonify({'message': 'Role not recognized'}), 400

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created!'}), 201

# ruta restful login
@app.route('/api/login', methods=['POST'])
def login():
    # Verifica las credenciales del usuario y realiza el login si son válidas.
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.password == password:
            return jsonify({'message': 'Login failed!'}), 401

        login_user(user)
        return jsonify({'message': 'Login successful!'}), 200
    
# ruta restful logout
@app.route('/api/logout')
@login_required
def logout():
    # Realiza el logout del usuario logeado.
    logout_user()
    return jsonify({'message': 'Logout successful!'}), 200

# ruta restful para obtener todas las disponibilidades
@app.route('/api/disponibilidad', methods=['GET'])
@login_required
def get_disponibilidades():
    # Filtra las disponibilidades y agrega información del usuario/profesional asociado.
    disponibilidades = Disponibilidad.query.all()
    output = []
    for disponibilidad in disponibilidades:
        disponibilidad_data = {}
        disponibilidad_data['id'] = disponibilidad.id
        profesional = Profesional.query.get(disponibilidad.id_usuario)
        if profesional is None:
            continue
        disponibilidad_data['id_profesional'] = profesional.id
        disponibilidad_data['nombre_usuario'] = profesional.name + " " + profesional.last_name
        disponibilidad_data['especialidad'] = profesional.especialidad
        disponibilidad_data['fecha'] = disponibilidad.fecha
        disponibilidad_data['hora_inicio'] = disponibilidad.hora_inicio
        disponibilidad_data['hora_fin'] = disponibilidad.hora_fin
        disponibilidad_data['estado'] = disponibilidad.estado
        output.append(disponibilidad_data)
    return jsonify({'disponibilidades': output})

# ruta restful para crear una disponibilidad
@app.route('/api/disponibilidad', methods=['POST'])
@login_required
def create_disponibilidad():
    # Crea una nueva disponibilidad en la base de datos.
    if request.method == 'POST':
        id_usuario = current_user.id
        fecha = request.json['fecha']
        hora_inicio = request.json['hora_inicio']
        hora_fin = request.json['hora_fin']
        estado = "disponible"

        new_disponibilidad = Disponibilidad(id_usuario=id_usuario, fecha=fecha, hora_inicio=hora_inicio,hora_fin=hora_fin , estado=estado)
        db.session.add(new_disponibilidad)
        db.session.commit()

        return jsonify({'message': 'Disponibilidad created!'}), 201
    
# ruta restful para obtener las disponibilidades del usuario logeado (profesional)
@app.route('/api/disponibilidad/usuario', methods=['GET'])
@login_required
def get_disponibilidades_usuario():
    # Filtra las disponibilidades del usuario logeado.
    id_usuario = current_user.id
    disponibilidades = Disponibilidad.query.filter_by(id_usuario=id_usuario)
    output = []
    for disponibilidad in disponibilidades:
        disponibilidad_data = {}
        disponibilidad_data['id'] = disponibilidad.id
        disponibilidad_data['id_usuario'] = disponibilidad.id_usuario
        disponibilidad_data['fecha'] = disponibilidad.fecha
        disponibilidad_data['hora_inicio'] = disponibilidad.hora_inicio
        disponibilidad_data['hora_fin'] = disponibilidad.hora_fin
        disponibilidad_data['estado'] = disponibilidad.estado
        output.append(disponibilidad_data)
    return jsonify({'disponibilidades': output})

# ruta restful para eliminar una disponibilidad
@app.route('/api/disponibilidad/<id>', methods=['DELETE'])
@login_required
def delete_disponibilidad(id):
    # Elimina una disponibilidad de la base de datos.
    disponibilidad = Disponibilidad.query.get(id)
    if not disponibilidad:
        return jsonify({'message': 'No disponibilidad found!'}), 404
    db.session.delete(disponibilidad)
    db.session.commit()
    return jsonify({'message': 'Disponibilidad deleted!'}), 200

# ruta restful para crear una cita
@app.route('/api/cita', methods=['POST'])
@login_required
def create_cita():
    # Crea una nueva cita y cambia el estado de la disponibilidad asociada.
    if request.method == 'POST':
        id_paciente = current_user.id
        id_profesional = request.json['id_profesional']
        id_disponibilidad = request.json['id_disponibilidad']
        estado = "pendiente"

        new_cita = Cita(id_paciente=id_paciente, id_profesional=id_profesional, id_disponibilidad=id_disponibilidad, estado=estado)
        db.session.add(new_cita)
        db.session.commit()

        # cambiar estado de la disponibilidad
        disponibilidad = Disponibilidad.query.get(id_disponibilidad)
        disponibilidad.estado = "ocupado"
        db.session.commit()

        return jsonify({'message': 'Cita created!'}), 201
    
# ruta restful que recibe el id de un cita y devuelve la informacion del paciente asociado
@app.route('/api/cita/<id_disponibilidad>', methods=['GET'])
@login_required
def get_cita(id_disponibilidad):
    cita = Cita.query.filter_by(id_disponibilidad=id_disponibilidad).first()
    if not cita:
        return jsonify({'message': 'No cita found!'}), 404
    paciente = Paciente.query.get(cita.id_paciente)
    if not paciente:
        return jsonify({'message': 'No paciente found!'}), 404
    paciente_data = {}
    paciente_data['id'] = paciente.id
    paciente_data['name'] = paciente.name
    paciente_data['last_name'] = paciente.last_name
    paciente_data['email'] = paciente.email
    paciente_data['comuna'] = paciente.comuna
    paciente_data['direccion'] = paciente.direccion
    return jsonify({'paciente': paciente_data})

# Ejecutar la aplicación
if __name__ == '__main__':
    # Crear la base de datos y ejecutar la aplicación
    with app.app_context():
        db.create_all()

    app.run(debug=True,port=4000)