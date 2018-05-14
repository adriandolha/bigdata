import json
import logging
from collections import namedtuple

from flask_socketio import SocketIO
from kafka_consumer import consume
logging.basicConfig(level=logging.DEBUG)


def consume_likes(socketio: SocketIO):
    consume('likes-counts', lambda msg: __consume_likes(msg, socketio))


def __consume_likes(msg, socketio):
    message = (msg.value())
    messageText = message.decode('utf-8')
    print('Received message: {0}'.format(messageText))
    item = json.loads(messageText, object_hook=lambda d: namedtuple('item', d.keys())(*d.values()))
    logging.info(item)
    socketio.emit('hello', 'test')
    socketio.emit('likes', messageText)