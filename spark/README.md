# Spark

## stream-process.py

### Dependencies
pyspark         http://spark.apache.org/docs/latest/api/python/

kafka-python    https://github.com/dpkp/kafka-python


### Run
This project is running in a docker-machine
```sh
spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.0.0.jar stream-processing.py stock-analyzer average-stock-price `docker-machine ip bigdata`:9092
```
