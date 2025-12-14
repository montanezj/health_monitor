import json
import os
import time
import psycopg2
from kafka import KafkaConsumer

# Kafka Configuration
kafka_host = os.getenv('KAFKA_BROKER', 'localhost:9092')
topic_name = 'server_health'

# Database Configuration
db_host = "db" # The name of the service in docker-compose
db_name = "health_monitor"
db_user = "user"
db_pass = "password"

# 1. Wait for Kafka to Start
print("Waiting for Kafka...")
time.sleep(10)

# 2. Connect to Kafka
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=kafka_host,
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# 3. Connect to Database (Retry loop)
conn = None
while conn is None:
    try:
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_pass
        )
        print("Connected to Database!")
    except psycopg2.OperationalError:
        print("Waiting for Database...")
        time.sleep(2)

cursor = conn.cursor()

# 4. Create Table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS server_stats (
        id SERIAL PRIMARY KEY,
        server_id VARCHAR(50),
        cpu_usage INT,
        temperature INT,
        timestamp FLOAT
    );
""")
conn.commit()

# 5. Consume and Save
print("Listening for messages and saving to DB...")
for message in consumer:
    data = message.value

    # Insert into DB
    cursor.execute("""
        INSERT INTO server_stats (server_id, cpu_usage, temperature, timestamp)
        VALUES (%s, %s, %s, %s)
    """, (data['server_id'], data['cpu_usage'], data['temperature'], data['timestamp']))

    conn.commit()
    print(f"Saved to DB: {data}")