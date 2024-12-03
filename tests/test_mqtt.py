from unittest.mock import MagicMock
import paho.mqtt.client as mqtt
from main import on_message

def test_mqtt():
    mock_client = MagicMock(spec=mqtt.Client)

    # simulate example incoming message
    input_topic = "BRE/calculateWinterSupplementInput/test123"
    input_payload = '{"id": "test123456", "numberOfChildren": 3, "familyComposition": "single", "familyUnitInPayForDecember": true}'
    message = MagicMock()
    message.topic = input_topic
    message.payload.decode.return_value = input_payload

    # call on_message handler
    on_message(mock_client, None, message)

    # Assert the correct output is published
    expected_topic = "BRE/calculateWinterSupplementOutput/test123"
    expected_payload = '{"id": "test123456", "isEligible": true, "baseAmount": 60.0, "childrenAmount": 60.0, "supplementAmount": 120.0}'
    mock_client.publish.assert_called_with(expected_topic, expected_payload)

