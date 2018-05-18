import cProfile

import pytest

import data_unit
from big_data_sampler import *


def test_kafka():
    create_facebook_likes_sample(1)


class TestBigData(object):

    def test_upper(self):
        assert 'foo'.upper() == 'FOO'

    def test_split(self):
        s = 'hello world'
        assert s.split() == ['hello', 'world']
        # check that s.split fails when the separator is not a string
        with pytest.raises(TypeError):
            s.split(2)

    def test_kafka(self):
        create_facebook_likes_sample(10000000, 3)

    def test_kafka_profile(self):
        cProfile.run("""
from collections import namedtuple
import json
import unittest
import big_data_sampler
import data_unit
import uuid
from big_data_sampler import *
create_facebook_likes_sample(1000)       
""", 'test.prof', 'tottime')

    def test_generate_users(self):
        with open('users.json', 'w') as outfile:
            users = []
            for _ in range(1000):
                users.append(data_unit.fake_user()._asdict())
            json.dump(users, outfile)

    def test_generate_facebook_likes(self):
        for _ in range(1000):
            data_unit.fake_facebook_like()

    def test_read_data(self):
        with open('/Users/lavi/Documents/Adi/data/users.json') as data:
            users = json.loads(data.read())
            print(users[0]['name'])

        users = data_unit.get_users()
        print(users)
