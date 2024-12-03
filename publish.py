import paho.mqtt.publish as publish
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

mqtt_topic_id = os.getenv("MQTT_TOPIC_ID")

if not mqtt_topic_id:
    raise ValueError("MQTT_TOPIC_ID is not set in the environment variables.")


BROKER = "test.mosquitto.org"
TOPIC = f'BRE/calculateWinterSupplementInput/{mqtt_topic_id}'

test_data = {
    "id": "test123456",
    "numberOfChildren": 3,
    "familyComposition": "single",
    "familyUnitInPayForDecember": True,
}

publish.single(TOPIC, json.dumps(test_data), hostname=BROKER)
print(f"Test data published to {TOPIC}")
