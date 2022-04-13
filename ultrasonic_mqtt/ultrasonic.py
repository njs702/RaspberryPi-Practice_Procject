import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)

def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    print(str(msg.payload.decode("utf-8")))
    dist = float(str(msg.payload.decode("utf-8")))
    if 40 <= dist and dist <= 110:
        client.publish('inTopic','1',1)
        client.loop_stop()
        client.disconnect()

# 새로운 클라이언트 생성
client = mqtt.Client()

# 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_subscribe(topic 구독),
# on_message(발행된 메세지가 들어왔을 때)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# address : localhost, port: 1883 에 연결
client.connect('192.168.0.80', 1883)
# outTopic topic 구독해서 메세지 받아옴
client.subscribe('outTopic', 1)
client.loop_forever()