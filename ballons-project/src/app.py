"""
import eventlet
eventlet.monkey_patch()
#eventlet.monkey_patch(socket=True, select=True)
"""
from subscriber_mqtt import handle_mqtt_message, handle_subscribe, handle_unsubscribe_all, handle_connect
from models import Transaccion, UsuarioTransaccion
import json
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, send
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_mqtt import Mqtt

from forms import TransaccionForm, RegistrationForm


app = Flask(__name__)

# APP config
#app.debug = True

# SQLAlchemy,DataBases config
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://SA:sqlServer-01@localhost:1433/TUKYSENSOR?driver=ODBC Driver 17 for SQL Server'
# Conexion BD RAM
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)
#ma = Marshmallow(app)

# MQTT config
app.config['MQTT_BROKER_URL'] = 'localhost'  # use the free broker from HIVEMQ
app.config['MQTT_BROKER_PORT'] = 1883  # default port for non-tls connection
# set the username here if you need authentication for the broker
app.config['MQTT_USERNAME'] = ''
# set the password here if the broker demands authentication
app.config['MQTT_PASSWORD'] = ''
# set the time interval for sending a ping to the broker to 5 seconds
app.config['MQTT_KEEPALIVE'] = 5
# set TLS to disabled for testing purposes
app.config['MQTT_TLS_ENABLED'] = False
# Parameters for SSL enabled
# app.config['MQTT_BROKER_PORT'] = 8883
# app.config['MQTT_TLS_ENABLED'] = True
# app.config['MQTT_TLS_INSECURE'] = True
# app.config['MQTT_TLS_CA_CERTS'] = 'ca.crt'
#mqtt = Mqtt(app)


# SocketIO
#socketio = SocketIO(app)

# Bootstrap
#bootstrap = Bootstrap(app)


Peso = None
ID_Usuario = None
ID_Producto = None
IDTransaccion = None
ID_Balanza = None
fechahora = None


#db.create_all()
#t = Transaccion.query.all()
#ut = UsuarioTransaccion.query.all()
#ut_example = UsuarioTransaccion.query.get(1)
# print ut_example


@app.route("/", methods=["POST", "GET"])
def index():
    global Peso
    global ID_Usuario
    global ID_Producto
    global IDTransaccion
    global ID_Balanza
    global FechaHora
    form = TransaccionForm(request.form)
    form.peso.data = Peso
    form.id_balanza.data = ID_Balanza
    form.id_producto.data = ID_Producto
    form.id_transaccion.data = IDTransaccion
    form.id_usuario.data = ID_Usuario
    if request.method == 'POST' and form.validate():
        if form.tipo_peso.data == 'Peso Limpio':
            usuario_transaccion = UsuarioTransaccion(
                FechaHora, Peso, None, None, None, None, ID_Usuario, ID_Producto, None,  IDTransaccion, ID_Balanza)
        if form.tipo_peso.data == 'Peso Sucio':
            usuario_transaccion = UsuarioTransaccion(
                FechaHora, None, Peso, None, None, None, ID_Usuario, ID_Producto, None,  IDTransaccion, ID_Balanza)
        if form.tipo_peso.data == 'Scrap':
            usuario_transaccion = UsuarioTransaccion(
                FechaHora, None, None, None, None, Peso, ID_Usuario, ID_Producto, None,  IDTransaccion, ID_Balanza)
        transaccion = Transaccion(
            IDTransaccion, None, form.tipo_transaccion.data)
        db_session.add(usuario_transaccion)
        db_session.add(transaccion)
        flash('Transaccion Exitosa')
        # return redirect(url_for('login'))
    return render_template("index.html", form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

#socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=False)

print("el nombre es " + __name__)
if __name__ == "__main__":
    print("el nombre es " + __name__)
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    mqtt = Mqtt(app)
    socketio = SocketIO(app)
    bootstrap = Bootstrap(app)

    db.create_all()
    #t = Transaccion.query.all()
    #ut = UsuarioTransaccion.query.all()
    #ut_example = UsuarioTransaccion.query.get(1)
    #print ut_example
    
    """
    client = mqtt.client
    client.on_message = handle_mqtt_message
    client.subscribe = handle_connect
    client.loop_start() 
    """
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=False)

else:
    
    print("el nombre es " + __name__)
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    mqtt = Mqtt(app)
    socketio = SocketIO(app)
    bootstrap = Bootstrap(app)

    db.create_all()
    t = Transaccion.query.all()
    ut = UsuarioTransaccion.query.all()
    #ut_example = UsuarioTransaccion.query.get(1)
    #print ut_example

    """
    client = mqtt.client
    client.on_message = handle_mqtt_message
    client.subscribe = handle_connect
    client.loop_start()
    """ 
    app.run(host='0.0.0.0', port=5000, use_reloader=False, debug=True)
    