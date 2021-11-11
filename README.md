# python-elasticsearch-with-kafka
Python Restful service with elasticsearch and kafka integration


1) Start Zookeeper node instance
   linux > bin/zookeeper-server-start.sh config/zookeeper.properties
   windows > bin\windows\zookeeper-server-start.bat config\zookeeper.properties

2) Start Kafka server
   linux > bin/kafka-server-start.sh config/server.properties
   windows > bin\windows\kafka-server-start.bat config\server.properties

3) Once kafka service is up create the kafka topic
> bin/kafka-topic.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic kafka-message-topic

4) consuming test message
> bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic kafka-message-topic --from-beginning

4) produce test message
> bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic kafka-message-topic
> Hello Listeners
