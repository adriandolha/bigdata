from collections import namedtuple
import json
import unittest
import big_data_sampler
import data_unit
import uuid
from big_data_sampler import *


class LoadTestKafkaProducer(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_kafka(self):
        create_facebook_likes_sample(1000000)

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


if __name__ == '__main__':
    unittest.main()
