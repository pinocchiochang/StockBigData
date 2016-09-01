# - read from a kafka topic
# - publish data to redis PUB

from kafka import KafkaConsumer
from kafka.errors import KafkaError

import argparse
import atexit
import logging

# - pip install redis
import redis

topic = ''
kafka_broker = ''
redis_channel = ''
redis_host = ''
redis_port = ''

logger_format = '%(asctime)-15s %(message)s'
logging.basicConfig(format = logger_format)
logger = logging.getLogger('redis-publisher')
logger.setLevel(logging.INFO)



if __name__ == '__main__':
	# - setup arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('topic', help = 'the kafka topic to consumer from')
	parser.add_argument('kafka_broker', help = 'location of kafka broker')
	parser.add_argument('redis_channel', help = 'the redis channel')
	parser.add_argument('redis_host', help = 'the ip/url of redis_host')
	parser.add_argument('redis_port', help = 'the port of redis')

	# - parse arguments
	args = parser.parse_args()
	topic = args.topic
	kafka_broker = args.kafka_broker
	redis_channel = args.redis_channel
	redis_host = args.redis_host
	redis_port = args.redis_port

	# - setup kafka consumer
	kafka_consumer = KafkaConsumer(topic, bootstrap_servers = kafka_broker)

	# - setup redis client
	redis_client = redis.StrictRedis(host=redis_host, port=redis_port)

	# - setup proper shutdown hook
	# atexit.register(shutdown_hook, kafka_consumer)

	for msg in kafka_consumer:
		logger.info('Received new data from kafka %s' % str(msg))
		redis_client.publish(redis_channel, msg.value)
