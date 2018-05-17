import logging
import uuid

from kafka_producer import get_producer, produce_from_generator
from data_unit import *

logging.basicConfig(level=logging.DEBUG)


def create_facebook_likes_sample(count):
    print('Producing bd.kafka messages')
    produce_from_generator('bdsample', lambda: generate_likes(count))


def generate_likes(count):
    for _ in range(count):
        yield fake_facebook_like()._asdict()
