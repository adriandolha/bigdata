import logging

from big_data_kafka.kafka_producer import produce_from_generator
from data_unit import *
import time
logging.basicConfig(level=logging.DEBUG)


def create_facebook_likes_sample(count, sleep_time=0):
    print('Producing bd.kafka messages')
    produce_from_generator('bdsample', lambda: generate_likes(count, sleep_time))


def generate_likes(count, sleep_time):
    for _ in range(count):
        if sleep_time != 0:
            time.sleep(sleep_time)
        yield fake_facebook_like()._asdict()
