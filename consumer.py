import json
from kafka import KafkaConsumer

# Initialize the consumer
consumer = KafkaConsumer(
    'server_health',   # <--- CORRECT NAME (matches producer.py)
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Listening for health metrics...")

# Loop and print messages as they arrive
for message in consumer:
    data = message.value
    print(f"Received: {data}")