import paho.mqtt.publish as publish

# Définissez les détails du serveur MQTT
MQTT_SERVER = "broker.hivemq.com"
MQTT_PORT = 1883

# Définissez le sujet MQTT et le message à publier
MQTT_TOPIC = "apptest"
MQTT_MSG = "Hello World!"

# Publiez le message MQTT
publish.single(MQTT_TOPIC, MQTT_MSG, hostname=MQTT_SERVER, port=MQTT_PORT)

print("Message publié: Sujet - '{}', Message - '{}'".format(MQTT_TOPIC, MQTT_MSG))
