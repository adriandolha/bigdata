import uuid
import json
import random
from collections import namedtuple
import datetime
from faker import Faker
from faker_web import WebProvider

FacebookLike = namedtuple('FacebookLike', [
    'userId',
    'agent',
    'timestamp'
])

User = namedtuple('User', [
    'id',
    'name',
    'address'
])
def fakeUser():
    fake = Faker()
    return User(id=uuid.uuid1().__str__(),
                name=fake.name(),
                address=fake.address())


def getUsers() -> list:
    users = []
    with open('/Users/lavi/Documents/Adi/data/users.json') as data:
        users = json.loads(data.read(), object_hook=lambda d: namedtuple('User', d.keys())(*d.values()))
    print('done')
    return users

users = getUsers()
def getRandomUserId():
    return users[random.randint(0, len(users) - 1)].id

def fakeFacebookLike():
    fake = Faker()
    fake.add_provider(WebProvider)
    like = FacebookLike(
        userId=getRandomUserId(),
        agent=fake.user_agent(),
        timestamp=datetime.datetime.now().__str__())
    return like
