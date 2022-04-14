import paho.mqtt.client as mqtt
import json
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)
        
# 새로운 클라이언트 생성
client = mqtt.Client()

# 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_subscribe(topic 구독),
# on_message(발행된 메세지가 들어왔을 때)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

# address : localhost, port: 1883 에 연결
client.connect('192.168.0.80', 1883)

client.publish('inTopic','1',1)

client.disconnect()