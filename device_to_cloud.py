import os
from azure.eventhub import EventHubConsumerClient

CONNECTION_STR = os.environ["EVENT_HUB_CONN_STR"]
EVENTHUB_NAME = os.environ["EVENT_HUB_NAME"]

consumer_client = EventHubConsumerClient.from_connection_string(
    conn_str=CONNECTION_STR,
    consumer_group="$Default",
    eventhub_name=EVENTHUB_NAME,
)


def on_event(partition_context, event):
    print("Received event from partition: {}.".format(partition_context.partition_id))
    print("Event properties: {}".format(event.properties))
    print("Event body: {}".format(event.body_as_str()))


try:
    with consumer_client:
        consumer_client.receive(
            on_event=on_event,
            starting_position="-1",  # "-1" is from the beginning of the partition.
        )
except KeyboardInterrupt:
    print("Stopped receiving.")
