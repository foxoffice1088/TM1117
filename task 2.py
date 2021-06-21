import time
import Adafruit_DHT
import paho.mqtt.client as mqtt

def mqtt_on_message(client, userdata, msg):
    d_msg = str(msg.payload.decode("utf-8")) # Decode the message
    print("Received message on topic %s : %s" % (msg.topic, d_msg))

mqtt_broker = "ia.ic.polyu.edu.hk" # Broker
mqtt_port = 1883 # Default
mqtt_qos = 1
mqtt_topic = "iot/18022197D"

mqtt_client = mqtt.Client("iot-18022197D") # Create a Client Instance
mqtt_client.connect(mqtt_broker, mqtt_port) # Establish a connection to a broker
mqtt_client.subscribe(mqtt_topic, mqtt_qos)
print("Connect to MQTT broker")
mqtt_client.on_message = mqtt_on_message
mqtt_client.loop_start()

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN) # Read the temperature
    mqtt_client.publish(mqtt_topic, temperature, mqtt_qos) # Publish a message
    print("Publishing message %s to topic %s" % (temperature, mqtt_topic))
    time.sleep(2)