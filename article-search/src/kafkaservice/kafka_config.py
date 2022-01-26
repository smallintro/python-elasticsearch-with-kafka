from kafka import KafkaProducer
from kafka import KafkaConsumer
import json

bootstrap_servers = ['Win11Home.localdomain:9092']
default_topic = 'python-kafka-topic'
group_id = 'kafka-group-id'

_text_producer = None
_text_consumer = None
_producer = None
_consumer = None


def init_kafka_producer():
    global _text_producer, _producer
    _text_producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    _producer = KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    print(f"init_kafka_producer finished")


def init_kafka_consumer(topic_name=default_topic):
    global _text_consumer, _consumer
    _text_consumer = KafkaConsumer(topic_name, group_id=group_id, bootstrap_servers=bootstrap_servers)
    _consumer = KafkaConsumer(topic_name, group_id=group_id, bootstrap_servers=bootstrap_servers,
                              auto_offset_reset='earliest', enable_auto_commit=True,
                              value_deserializer=lambda x: json.loads(x.decode('utf-8')),
                              max_poll_interval_ms=1000000)
    print(f"init_kafka_consumer finished")


def producer():
    global _producer
    if _producer is None:
        init_kafka_producer()
    return _producer


def text_producer():
    global _text_producer
    if _text_producer is None:
        init_kafka_producer()
    return _text_producer


def consumer():
    global _consumer
    if _consumer is None:
        init_kafka_consumer()
    return _consumer


def text_consumer():
    global _text_consumer
    if _text_consumer is None:
        init_kafka_consumer()
    return _text_consumer
