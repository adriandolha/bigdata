from kafka import KafkaConsumer
import json
import data_unit
import codecs
from pykafka import KafkaClient, SimpleConsumer
from collections import namedtuple
def default_consumer(msg):
    message = (msg.value())
    messageText = message.decode('utf-8')
    print('Received message: {0}'.format(messageText))
    item = json.loads(messageText, object_hook=lambda d: namedtuple('item', d.keys())(*d.values()))

def consume(topic, consumer):
    client = KafkaClient(hosts="localhost:9092")
    topic = client.topics[b'likes-counts']
    consumer = topic.get_simple_consumer()
    while True:
        for msg in consumer:
            if msg is not None:
                consume(msg)

# try:
#     while True:
#         msg = consumer.poll(0.1)
#         if msg is None:
#             continue
#         elif not msg.error():
#             message = (msg.value())
#             messageText = message.decode('utf-8')
#             print('Received message: {0}'.format(messageText))
#             item = json.loads(messageText, object_hook=lambda d: namedtuple('item', d.keys())(*d.values()))
#
#         elif msg.error().code() == KafkaError._PARTITION_EOF:
#             print('End of partition reached {0}/{1}'
#                   .format(msg.topic(), msg.partition()))
#         else:
#             print('Error occured: {0}'.format(msg.error().str()))
#
# except KeyboardInterrupt:
#     pass
#
# finally:
#     consumer.close()