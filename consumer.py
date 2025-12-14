import json
from kafka import KafkaConsumer

import os
kafka_host = os.getenv('KAFKA_BROKER', 'localhost:9092')
consumer = KafkaConsumer(
    'server_health',
    bootstrap_servers=kafka_host,
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Listening for health metrics...")

# Loop and print messages as they arrive
for message in consumer:
    data = message.value
    print(f"Received: {data}")