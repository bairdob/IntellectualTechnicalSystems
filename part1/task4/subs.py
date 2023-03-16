import random
from paho.mqtt import client as mqtt_client

broker = 'localhost'
port = 1883
topic = "test/topic"
client_id = f'python-mqtt-{random.randint(0, 100)}'


def connect_mqtt() -> mqtt_client:

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def movingAverage(v: list, t: int=2) -> float:
    return v[t] * 0.6 + v[t-1] * 0.3 + v[t-2] * 0.1

def subscribe(client: mqtt_client):

    def on_message(client, userdata, msg):
        l.append(float(msg.payload.decode()))
        l.pop(0)
        print(movingAverage(l))
        # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    l = [0]*3
    run()
