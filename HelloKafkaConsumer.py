from kafka import KafkaConsumer
import json
import DataUnit
import codecs
from confluent_kafka import Consumer, KafkaError
from collections import namedtuple
settings = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'big.data.samples',
    'client.id': 'client-1',
    'enable.auto.commit': True,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'}
}
consumer = Consumer(settings)
reader = codecs.getreader("utf-8")
# consumer.subscribe(['bdsample','likes-counts'])
consumer.subscribe(['likes-counts'])
try:
    while True:
        msg = consumer.poll(0.1)
        if msg is None:
            continue
        elif not msg.error():
            message = (msg.value())
            messageText = message.decode('utf-8')
            print('Received message: {0}'.format(messageText))
            item = json.loads(messageText, object_hook=lambda d: namedtuple('item', d.keys())(*d.values()))

        elif msg.error().code() == KafkaError._PARTITION_EOF:
            print('End of partition reached {0}/{1}'
                  .format(msg.topic(), msg.partition()))
        else:
            print('Error occured: {0}'.format(msg.error().str()))

except KeyboardInterrupt:
    pass

finally:
    consumer.close()