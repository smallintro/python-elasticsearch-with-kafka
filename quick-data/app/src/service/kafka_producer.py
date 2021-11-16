from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

bootstrap_servers = ['localhost:9092']
topic_name = 'python-kafka-topic'
group_id = 'kafka-group-id'

producer_str = None
producer_json = None
producer = None


def init_kafka_producer():
    global producer_str, producer_json, producer
    producer_str = KafkaProducer(bootstrap_servers=bootstrap_servers)
    producer_json = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                  value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest',
                             enable_auto_commit=True, group_id=group_id,
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))


def publish_str_message():
    future = producer_str.send(topic_name, b'Hello from kafka...')
    try:
        record_metadata = future.get(timeout=10)
        print(f"Message sent: {record_metadata}")
    except KafkaError as err:
        print(f"An exception happened {err}")


def publish_json_message():
    json_data = {'name': 'python-kafka-client', 'website': 'smallintro.github.io'}
    future = producer_json.send(topic_name, json_data)
    try:
        record_metadata = future.get(timeout=10)
        print(f"Message sent: {record_metadata}")
    except KafkaError as err:
        print(f"An exception happened {err}")


if __name__ == "__main__":
    publish_str_message()
    publish_json_message()
