# -*- coding: utf-8 -*-
import datetime,time
import paho.mqtt.client as mqtt # import the client1

broker_address = "localhost"
broker_port = 1883
topic = "topic"


from app import db,ma
from models import Transaccion,UsuarioTransaccion


Peso=None
ID_Usuario=None
ID_Producto=None
ID_Transaccion=None
ID_Balanza=None
fechahora=None 

def on_message(client, userdata, message):
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
    db.session.add(Transaccion(IDTransaccion, None, 'None'))
    db.session.add(UsuarioTransaccion(FechaHora, None, None, None, None, None, ID_Usuario, ID_Producto, None,  IDTransaccion, ID_Balanza))
    print(db.session.new)
    db.session.commit()
    

client = mqtt.Client("Subscriptor_ejem1")
client.on_message = on_message 
client.connect(broker_address) 
#client.loop_start() # Inicio del bucle
client.subscribe(topic)
#time.sleep(10) # Paramos el hilo para recibir mensajes.
#client.loop_stop() # Fin del bucle
client.loop_forever()