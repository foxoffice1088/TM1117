import time
import Adafruit_DHT
import paho.mqtt.client as mqtt
import drivers
display = drivers.Lcd()
d_msg = None
Flag = False
number = False
def mqtt_on_message(client, userdata, msg):
    global d_msg
    d_msg = str(msg.payload.decode("utf-8"))
     # Decode the message
    

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

while not Flag:
    # Read the temperature
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if (d_msg == "T"):
        str1 = "T={:^8}".format(temperature)
        display.lcd_display_string(str1, 1)
        d_msg = ""
        time.sleep(2)
        display.lcd_clear()
    elif (d_msg == "H"):
        str1 = "H={:^8}".format(humidity)
        display.lcd_display_string(str1, 1)
        d_msg = ""
        time.sleep(2)
        display.lcd_clear()
    time.sleep(0.1)
    


