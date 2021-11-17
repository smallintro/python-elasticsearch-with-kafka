from kafka.errors import KafkaError
import config.kafka_config as kfk


def on_send_success(record_metadata):
    print(f"[Message sent]::::: : {record_metadata}")


def on_send_error(exe):
    print('Exception while publish_message: %s' % str(exe))


def publish_str_message(msg_data, topic_name=kfk.default_topic):
    try:
        future = kfk.text_producer().send(topic_name, msg_data.encode('UTF-8'))
        record_metadata = future.get(timeout=60)
        print(f"Message sent: {record_metadata}")
    except KafkaError as err:
        print('Error while publish_str_message: %s' % str(err))
    except Exception as ex:
        print('Exception while publish_message: %s' % str(ex))


def publish_message(msg_data, topic_name=kfk.default_topic):
    try:
        kfk.producer().send(topic_name, msg_data).add_callback(on_send_success).add_errback(on_send_error)
    except KafkaError as err:
        print('Error while publish_message: %s' % str(err))
    except Exception as ex:
        print('Exception while publish_message: %s' % str(ex))


'''if __name__ == "__main__":
    str_data = b'Hello from kafka topic publisher'
    json_data = {'name': 'article.elasticsearch', 'message': 'python.kafka.client.started'}
    publish_str_message(str_data)
    publish_message(json_data)'''
