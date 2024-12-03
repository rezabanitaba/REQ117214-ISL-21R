import json
import paho.mqtt.client as mqtt
from rules_engine.engine import RulesEngine
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# initialize MQTT client
mqtt_client = mqtt.Client()

# MQTT config
BROKER = "test.mosquitto.org"
PORT = 1883
INPUT_TOPIC = "BRE/calculateWinterSupplementInput/"
OUTPUT_TOPIC = "BRE/calculateWinterSupplementOutput/"

def on_message(client, userdata, message):
    try:
        print(f"Received message on topic {message.topic}: {message.payload.decode()}")  # Debugging
        input_data = json.loads(message.payload.decode())
        mqtt_topic_id = message.topic.split("/")[-1]

        result = RulesEngine.calculate_supplement(input_data)

        client.publish(f"{OUTPUT_TOPIC}{mqtt_topic_id}", json.dumps(result))
        print(f"Processed: {result}")

    except Exception as e:
        print(f"Error processing message: {e}")


def main():
    # Get topic ID from env file
    mqtt_topic_id = os.getenv("MQTT_TOPIC_ID")
    if not mqtt_topic_id:
        raise ValueError("MQTT_TOPIC_ID is not set in the .env file.")
    
    mqtt_client.on_message = on_message

    mqtt_client.connect(BROKER, PORT)
    mqtt_client.subscribe(f"{INPUT_TOPIC}{mqtt_topic_id}")

    print("Connection established. Listening for incoming messages...")
    mqtt_client.loop_forever()

if __name__ == "__main__":
    main()
