import paho.mqtt.client as mqtt

# -*- coding: utf-8 -*-

broker_address = "localhost"
client = mqtt.Client('Publicador_ejem1') #Creacion del cliente
client.connect(broker_address)
topic = "sensor/weight"

import random
value=random.randint(0,9)

client.publish(topic, value)