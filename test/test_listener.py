from kafka import KafkaConsumer

TOPIC = "TEST_KAFKA"
BOOTSTRAP_SERVERS = '192.168.111.71:9092'

consumer = KafkaConsumer(
    TOPIC, 
    bootstrap_servers=[BOOTSTRAP_SERVERS]
)
for msg in consumer:

    print(f"[Listener] Kafka received: {msg.value}")
