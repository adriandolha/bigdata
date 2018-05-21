# bigdata
Create a sample application to prove big data real time streaming.
We are going to generate facebook likes in real time. The data unit looks like:
FacebookLike = namedtuple('FacebookLike', [
    'user_id',
    'agent',
    'timestamp'
])

User = namedtuple('User', [
    'id',
    'name',
    'address'
])
Users were generated using python faker. You can find the users list at test/users.json 
The real-time data flow pipeline is the following:
1. Generate facebook likes and push them to kafka topic 'bdsample'. The facebook likes are generated using the following algorithm:
   * user_id - random id selector from the users list
   * agent - random browser agent using faker
   * timestamp - current timestamp
   To generate likes you need to run the test test.test_big_data.TestBigData#test_kafka. By default, it generates 1000000 likes with no delay. 
   For testing purposes, a sleep time (secs) can be provided and likes will be delayed.
2. Now that we have our likes in Kafka, we can start aggregating them using Spark Streaming. Spark allows to process data in windows 
   (secs, minutes, hours). We're going to take all the likes generated in one second, compute the total count and post to another topic ('likes-counts')
   the following: (second (1-60), total_likes). The code can be found at compute_jobs/likes_views.py
3. Using nodejs and chartio we can display likes-counts entries as they arrive. The code can be found at node/index.js
