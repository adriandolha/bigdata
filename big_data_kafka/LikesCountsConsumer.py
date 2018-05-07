import json
import codecs
from confluent_kafka import Consumer, KafkaError
from collections import namedtuple
import logging
from flask_socketio import SocketIO

logging.basicConfig(level=logging.DEBUG)

class LikesCountsConsumer:
    def __init__(self):
        self.settings = {
            'bootstrap.servers': 'localhost:9092',
            'group.id': 'big.data.samples',
            'client.id': 'client-1',
            'enable.auto.commit': True,
            'session.timeout.ms': 6000,
            'default.topic.config': {'auto.offset.reset': 'smallest'}
        }
        self.consumer = Consumer(self.settings)
        self.reader = codecs.getreader("utf-8")
        self.consumer.subscribe(['likes-counts'])
    def start(self, socketio: SocketIO):
        try:
            while True:
                msg = self.consumer.poll(0.1)
                if msg is None:
                    continue
                elif not msg.error():
                    message = (msg.value())
                    messageText = message.decode('utf-8')
                    print('Received message: {0}'.format(messageText))
                    item = json.loads(messageText, object_hook=lambda d: namedtuple('item', d.keys())(*d.values()))
                    logging.info(item)
                    socketio.emit('hello','test')
                    socketio.emit('likes',messageText)
                elif msg.error().code() == KafkaError._PARTITION_EOF:
                    print('End of partition reached {0}/{1}'
                          .format(msg.topic(), msg.partition()))
                else:
                    print('Error occured: {0}'.format(msg.error().str()))

        except KeyboardInterrupt:
            pass

        finally:
            self.consumer.close()