import json
from pykafka import KafkaClient

client = KafkaClient(hosts="localhost:9092")


def get_producer(topic):
    return client.topics[bytes(topic, 'utf8')].get_producer()


def produce(producer, message):
    producer.produce(json.dumps(message).encode('utf-8'))
