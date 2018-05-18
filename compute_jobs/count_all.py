# logging.basicConfig(level=logging.DEBUG)

from pyspark import SparkContext

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

    count = sc.textFile("hdfs://spark-vm01:9000/likes/part-*").count()
    print("Total count:")
    print(count)
