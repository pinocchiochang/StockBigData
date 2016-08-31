# - read from kafka
# - do average
# - save data back

import atexit
import sys
import logging
import json
import time


from kafka import KafkaProducer
from kafka.errors import KafkaError
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

kafka_broker = '192.168.99.100:9092'
kafka_topic = 'stock-analyzer'
new_topic = 'test'

logger_format = '%(asctime)-15s %(message)s'
logging.basicConfig(format = logger_format)
logger = logging.getLogger('data-storage')
logger.setLevel(logging.INFO)

def process(timeobj, rdd):
	# - do average 
	num_of_records = rdd.count()
	if num_of_records == 0:
		return

	# - sum up all the price in this rdd
	# - for each rdd record, do sth (take out the LastTradePrice, json)
	# - for all the rdd record, sum up -> reduce
	price_sum = rdd.map(lambda record: float(json.loads(record[1].decode('utf-8'))[0].get('LastTradePrice'))).reduce(lambda a, b: a+b)
	# print(price_sum)
	# print(num_of_records)
	average = price_sum / num_of_records
	logger.info('Received records from Kafka, average price is %f' % average)
	current_time = time.time()
	data = json.dumps({'timestamp': current_time, 'average': average})

	# - new topic name: averagePrice
	kafka_producer.send(new_topic, value=data, timestamp_ms=time.time())

def shutdown_hook(producer):
	logger.info('preparing to shutdown, waiting for producer to flush msg')
	producer.flush(10)
	logger.info('producer flush finished')
	try:
		producer.close()
	except Exception:
		logger.warn('producer failed to close')
	logger.info('producer closed')


if __name__ == '__main__':

	# - sys.argv is an array
	# - sys.argv[0] stream-process.py
	# - sys.argv[1] broker location
	# - sys.argv[2] topic
	if (len(sys.argv) != 4):
		print("Not enough argument [kafka broker location], [kafka topic location], [kafka new topic location]")
		exit(1)

	sc = SparkContext("local[2]", "StockAveragePrice")
	sc.setLogLevel('ERROR')    # - DEBUG, INFO, WARNING, ERROR

	ssc = StreamingContext(sc, 5)

	kafka_broker, kafka_topic, new_topic = sys.argv[1:]

	# - setup a kafka stream
	# print(kafka_topic)
	# print(kafka_broker)
	directKafkaStream = KafkaUtils.createDirectStream(ssc, [kafka_topic], {'metadata.broker.list': kafka_broker})
	directKafkaStream.foreachRDD(process)

	kafka_producer = KafkaProducer(bootstrap_servers = kafka_broker)

	atexit.register(shutdown_hook, kafka_producer)
 
	ssc.start()
	ssc.awaitTermination()
