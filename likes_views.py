import json

from dateutil import parser
from pykafka import KafkaClient
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


def push_likes_counts_to_kafka(status_counts):
    client = KafkaClient(hosts="localhost:9092")
    topic = client.topics[b'likes-counts']
    for status_count in status_counts:
        with topic.get_producer() as producer:
            producer.produce(json.dumps(status_count).encode('utf-8'))

if __name__ == "__main__":
    sc = SparkContext(appName='PythonStreamingDirectKafkaWordCount')
    ssc = StreamingContext(sc, 5)
    # noinspection PyDeprecation
    kvs = KafkaUtils.createDirectStream(ssc, ['bdsample'], {'metadata.broker.list': 'localhost:9092'})
    kvs.pprint()
    likes = kvs.map(lambda message: json.loads(message[1]))
    counts = likes.map(lambda fb: (parser.parse(fb['timestamp']).hour, 1)) \
        .reduceByKey(lambda a, b: a + b)

    counts.pprint()
    counts.foreachRDD(lambda rdd: rdd.foreachPartition(push_likes_counts_to_kafka))

    ssc.start()
    ssc.awaitTermination()
