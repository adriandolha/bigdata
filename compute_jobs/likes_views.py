import json
import logging
# logging.basicConfig(level=logging.DEBUG)

from dateutil import parser
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from big_data_kafka.kafka_producer import produce, get_producer


def push_likes_counts_to_kafka(fb_likes):
    producer = get_producer('likes-counts')
    producer.start()
    for fb_like in fb_likes:
        print('FB like:')
        print(fb_like)
        produce(producer, fb_like)
    # produce_messages(producer, fb_likes)
    producer.stop()


if __name__ == "__main__":
    sc = SparkContext(appName='PythonStreamingDirectKafkaWordCount')
    ssc = StreamingContext(sc, 30)
    # noinspection PyDeprecation
    kvs = KafkaUtils.createDirectStream(ssc, ['bdsample'], {'metadata.broker.list': 'localhost:9092'})
    kvs.pprint()
    print('Running KAFKA JOB')
    likes = kvs.map(lambda message: json.loads(message[1]))
    counts = likes.map(lambda fb: (parser.parse(fb['timestamp']).hour, 1)) \
        .reduceByKey(lambda a, b: a + b)

    counts.pprint()
    counts.foreachRDD(lambda rdd: rdd.foreachPartition(push_likes_counts_to_kafka))

    ssc.start()
    ssc.awaitTermination()
