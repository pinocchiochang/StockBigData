from googlefinance import getQuotes
from kafka import KafkaProducer
from kafka.errors import KafkaError, KafkaTimeoutError

import time
import atexit
import argparse
import logging
import json
import schedule

topic_name = ''
kafka_broker = ''

logger_format = '%(asctime)-15s %(message)s'
logging.basicConfig(format = logger_format)
logger = logging.getLogger('data-producer')
logger.setLevel(logging.INFO)

# - TRACE DEBUG INFO WARN ERROR

def fetch_price(producer, symbol):
	price = json.dumps(getQuotes(symbol));
	logger.debug('Get stock price %s', price)
	try:
		producer.send(topic = topic_name, value = price, timestamp_ms = time.time())
	except Exception:
		logger.warn('Failed to send msg to kafka')
	looger.debug('Successfully Sent data to Kafka')

def shutdown_hook(producer):
	looger.info('preparing to shutdown, waiting for producer to flush msg')
	producer.flush(10)
	logger.info('producer flush finished')
	try:
		producer.close()
	except Exception:
		logger.warn('producer failed to close')
	logger.info('producer closed')

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('symbol', help = 'the stock symbol')
	parser.add_argument('topic_name', help = 'the kafka topic to push to')
	parser.add_argument('kafka_broker', help = 'location of kafka broker')

	args = parser.parse_args()
	symbol = args.symbol
	topic_name = args.topic_name
	kafka_broker = args.kafka_broker

	producer = kafkaProducer(bootstrap_servers = kafka_broker)

	# - schedule and run every second
	schedule.every(1).second.do()(fetch_price, producer, symbol)
    
	# - register shutdown hook
	atexit.register(shutdown_hook, producer)

    # - kick start
	while True:
		schedule.run_pending()
		time.sleep(1)

    # fetch_price(producer, symbol)

