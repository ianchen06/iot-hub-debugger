import time
import os

from azure.iot.device import IoTHubDeviceClient
from dotenv import load_dotenv

load_dotenv()

IOTHUB_CONNECTION_STRING = os.getenv("IOTHUB_CONNECTION_STRING")

client = IoTHubDeviceClient.create_from_connection_string(IOTHUB_CONNECTION_STRING)


def message_received_handler(message):
    print("Message received: {}".format(message))


client.on_message_received = message_received_handler

while True:
    print("Listening for messages...")
    time.sleep(10)
