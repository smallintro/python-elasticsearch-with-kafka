from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

bootstrap_servers = ['localhost:9092']
topic_name = 'python-kafka-topic'

producer_str = KafkaProducer(bootstrap_servers=bootstrap_servers)
producer_json = KafkaProducer(bootstrap_servers=bootstrap_servers,
                              value_serializer=lambda v: json.dumps(v).encode('utf-8'))


def publish_message():
    future = producer_str.send(topic_name, b'Hello from kafka...')
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError as err:
        print(f"An exception happened {err}")


def publish_json():
    json_data = {'name': 'python-kafka-client', 'website': 'smallintro.github.io'}
    producer_json.send(topic_name, json_data)
