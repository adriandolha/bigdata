from kafka import KafkaProducer
import logging
import json
import Topics
logging.basicConfig(level=logging.DEBUG)
import os
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
from confluent_kafka import Producer
class BigDataSampler:
    def __init__(self):
        self.producer = Producer({'bootstrap.servers': 'localhost:9092'})
    def send(self, key=None, value=None):
        self.producer.produce(Topics.Topics.BD_SAMPLE.value, key=key,
                                       value=json.dumps(value).encode('utf-8'))
        self.producer.flush()
    def close(self):
        print('Closed producer.')