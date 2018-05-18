import json
from pykafka import KafkaClient

client = KafkaClient(zookeeper_hosts="spark-vm01:2181")


def get_producer(topic):
    return client.topics[bytes(topic, 'utf8')].get_producer()


def start(producer):
    producer.start()


def stop(producer):
    producer.start()


def produce(producer, message):
    producer.produce(json.dumps(message).encode('utf-8'))


def produce_messages(producer, messages):
    print('Sending messages:')
    print(messages)
    for message in messages:
        print('Sending message:')
        message_json = json.dumps(message).encode('utf-8')
        print(message_json)
        producer.produce(message_json)


def produce_from_generator(topic, message_generator):
    producer = get_producer(topic)
    producer.start()
    for message in message_generator():
        produce(producer, message)
    producer.stop()
