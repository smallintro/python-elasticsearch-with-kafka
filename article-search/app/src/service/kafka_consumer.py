from kafka.errors import KafkaError
import config.kafka_config as kfk


def consume_str_message():
    try:
        for msg in kfk.text_consumer():
            print("\n[Message received]::::: %s" % (msg.topic, msg.value))
    except KafkaError as err:
        print('Error while consume_message: %s' % str(err))
    except Exception as ex:
        print('Exception while consume_message: %s' % str(ex))


def consume_message():
    try:
        for msg in kfk.consumer():
            print("\n[Message received]::::: Topic=%s, Message=%s\n" % (msg.topic, msg.value))
    except KafkaError as err:
        print('Error while consume_message: %s' % str(err))
    except Exception as ex:
        print('Exception while consume_message: %s' % str(ex))


'''if __name__ == "__main__":
    consume_str_message()
    consume_message()'''
