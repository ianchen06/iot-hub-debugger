# Azure IoT Hub Debugger

Print IoT Hub messages in the terminal

## Getting Started

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Cloud to Device

```
export IOTHUB_CONNECTION_STRING=<your-iot-hub-connection-string>

python ./app.py
```

### Device to Cloud

```

```

## References:

- [device to cloud]('https://github.com/Azure/azure-sdk-for-python/blob/azure-eventhub_5.12.0/sdk/eventhub/azure-eventhub/samples/sync_samples/recv.py')
