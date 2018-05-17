import json
from pykafka import KafkaClient

client = KafkaClient(zookeeper_hosts="localhost:2181")


def get_producer(topic):
    return client.topics[bytes(topic, 'utf8')].get_producer()


def start(producer):
    producer.start()


def stop(producer):
    producer.start()


def produce(producer, message):
    producer.produce(json.dumps(message).encode('utf-8'))


def produce_from_generator(topic, message_generator):
    producer = get_producer(topic)
    producer.start()
    for message in message_generator():
        produce(producer, message)
    producer.start()
