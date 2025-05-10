from kafka import KafkaConsumer

TOPIC = "TEST_KAFKA"
BOOTSTRAP_SERVERS = 'localhost:9092'

consumer = KafkaConsumer(
    TOPIC, 
    bootstrap_servers=[BOOTSTRAP_SERVERS]
)
for msg in consumer:

    print(msg.value)