# Kafka

## data-producer.py
实现了一个kafka producer, 每秒钟从Google finance抓取一支股票的信息, 发送给Kafka

### Dependencies
googlefinance   https://pypi.python.org/pypi/googlefinance
kafka-python    https://github.com/dpkp/kafka-python
schedule        https://pypi.python.org/pypi/schedule

```sh
pip install -r kafka_requirements.txt
```

### Run
假如你的Kafka运行在一个叫做bigdata的docker-machine里面, 然后虚拟机的ip是192.168.99.100
```sh
python data-producer.py AAPL stock-analyzer 192.168.99.100:9092
```


## fast-data-producer.py
实现了一个kafka producer, 产生随机的股票价格, 发送给Kafka
由于会产生大量的数据, 请注意一定要设置隔离的开发环境

### Dependencies
confluent-kafka https://github.com/confluentinc/confluent-kafka-python

### Run
假如你的Kafka运行在一个叫做bigdata的docker-machine里面, 然后虚拟机的ip是192.168.99.100
```sh
python fast-data-producer.py stock-analyzer 192.168.99.100:9092
```

