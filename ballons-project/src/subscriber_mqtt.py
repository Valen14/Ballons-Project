
from app import mqtt,socketio,json
import time, datetime

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('t')

@socketio.on('subscribe')
def handle_subscribe(json_str):
    data = json.loads(json_str)
    mqtt.subscribe(data['topic'])

@socketio.on('unsubscribe_all')
def handle_unsubscribe_all():
    mqtt.unsubscribe_all()

@socketio.on('publish')
def handle_publish(json_str):
    data = json.loads(json_str)
    mqtt.publish(data['topic'], data['message'])

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    global Peso
    global ID_Usuario
    global ID_Producto
    global IDTransaccion
    global ID_Balanza
    global FechaHora
    '''
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    socketio.emit('mqtt_message', data=data)
    print('Received message on topic {}: {}'.format(message.topic, message.payload.decode()))
    '''
    print("Mensaje recibido=", str(message.payload.decode("utf-8")))
    dato = str(message.payload.decode("utf-8"))
    dato_parceado = dato.split(":")
    tiempo = time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime())
    print(tiempo)
    Peso = dato_parceado[0]
    ID_Usuario = dato_parceado[1]
    ID_Producto = dato_parceado[2]
    IDTransaccion = dato_parceado[3]
    ID_Balanza = dato_parceado[4]
    FechaHora = time.localtime
    '''
    db.session.add(Transaccion(IDTransaccion, None, 'None'))
    db.session.add(UsuarioTransaccion(FechaHora, None, None, None, None, None, ID_Usuario, ID_Producto, None,  IDTransaccion, ID_Balanza))
    print(db.session.new)
    db.session.commit()
    '''

@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    print(level, buf)
    