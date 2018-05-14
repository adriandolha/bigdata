import logging
import uuid

from kafka_producer import get_producer, produce
from data_unit import *

logging.basicConfig(level=logging.DEBUG)


def create_facebook_likes_sample(count):
    print('Producing bd.kafka messages')
    producer = get_producer('bdsample')
    for _ in range(count):
        produce(producer, fake_facebook_like()._asdict())
        if (_ + 1) % 1000 == 0:
            print('Sent ' + _.__str__() + ' message')
