import time
import json
import random
from kafka import KafkaProducer

import os
# specific to docker environment
kafka_host = os.getenv('KAFKA_BROKER', 'localhost:9092')
producer = KafkaProducer(
    bootstrap_servers=[kafka_host],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

def generate_sensor_data(server_id):
    """Generates fake data: CPU usage and Temperature"""
    return {
        "server_id": f"server-{server_id}",
        "cpu_usage": random.randint(10, 100),
        "temperature": random.randint(35, 95), # Celsius
        "timestamp": time.time()
    }

print("--- Data Center Simulation Started ---")
try:
    while True:
        # Simulate 5 servers reporting in
        for i in range(1, 6):
            data = generate_sensor_data(i)
            # Send data to the topic 'server_health'
            producer.send('server_health', value=data)
            print(f"Sent: {data}")

        time.sleep(2) # Wait 2 seconds before next batch
except KeyboardInterrupt:
    print("Stopping simulation...")