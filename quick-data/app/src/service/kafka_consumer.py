from kafka import KafkaConsumer
from kafka.errors import KafkaError
import json

bootstrap_servers = ['localhost:9092']
topic_name = 'python-kafka-topic'
group_id = 'python-kafka-group'

consumer_str = KafkaConsumer(topic_name, group_id=group_id, bootstrap_servers=bootstrap_servers)
consumer_json = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers,
                              value_deserializer=lambda m: json.loads(m.decode('utf-8')))

consumer = KafkaConsumer(topic_name, bootstrap_servers= bootstrap_servers, auto_offset_reset='earliest',
                         enable_auto_commit=True, group_id=group_id,
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))


def consume_str_message():
    for msg in consumer_str:
        print("Topic Name=%s,Message=%s" % (msg.topic, msg.value))


def consume_json_message():
    for msg in consumer_json:
        print("Topic Name=%s,Message=%s" % (msg.topic, msg.value))