from collections import namedtuple
import json
import unittest
import HelloKafkaProducer
import DataUnit
import JsonUtils
import uuid

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
        print('Producing bd.kafka messages')
        producer = HelloKafkaProducer.BigDataSampler()
        for _ in range(100000):
            if (_ + 1) % 1000 == 0:
                print('Sent ' + _.__str__() + ' message')
            producer.send(key=uuid.uuid1().__str__(),value=DataUnit.fakeFacebookLike()._asdict())
        producer.close()

    def test_generate_users(self):
        with open('users.json', 'w') as outfile:
            users = []
            for _ in range(1000):
                users.append(DataUnit.fakeUser()._asdict())
            json.dump(users, outfile)
    def test_generate_facebook_likes(self):
        for _ in range(1000):
            DataUnit.fakeFacebookLike()
    def test_read_data(self):
        with open('/Users/lavi/Documents/Adi/data/users.json') as data:
            users = json.loads(data.read())
            print(users[0]['name'])

        users = DataUnit.getUsers()
        print(users)



if __name__ == '__main__':
    unittest.main()
