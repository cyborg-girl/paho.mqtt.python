## subscriber printing messages to JSON file:

import paho.mqtt.client as mqtt
import os


def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    data = str(msg.payload)
    data = data.replace('[', '')
    data = data.replace(']', '')
    data = data.replace(';', ',')
    print data
    with open('C:/Users/Me/Desktop/2018/testfile1.js', 'a') as log_file:
        log_file.write(data + ",")
        log_file.write('\n')


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


mqttc = mqtt.Client("subscriber1", clean_session=True)
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
mqttc.connect("10.255.99.99", 1883, 60)
mqttc.subscribe("/TOPICS/RPI/#", 0)


mqttc.loop_forever()
