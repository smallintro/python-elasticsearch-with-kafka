# python-elasticsearch-with-kafka
Python Restful service with elasticsearch and kafka integration

### 1. Server setup
    1.1 Download and install Java 1.8 or higher
    1.2 Download and install [Kafka Server](https://kafka.apache.org/downloads)
    1.3 Download and install [Elasticsearch Server](https://www.elastic.co/downloads/elasticsearch)

### 2. Client setup
    2.1 Download and install [Python](https://www.python.org/downloads/)

    2.2 Create and activate a python virtual environment
    > py -m venv eskafkavenv # can use any name in place of eskafkavenv

    2.3 Activate the created virtual environment
    > eskafkavenv\Scripts\activate

#### 3. Install python packages
    3.1 pip install kafka-python
    3.2 pip install urllib3
    3.3 pip install certifi
    3.4 pip install elasticsearch
Alternatively we can download the tar.gz package from the Download page and run command 
> py -m pip install .\<python-package-name>.tar.gz # replace the <python-package-name>

## 4. Start Kafka server
    4.1  Start Zookeeper node instance
    > linux$ bin/zookeeper-server-start.sh config/zookeeper.properties
    > windows$ bin\windows\zookeeper-server-start.bat config\zookeeper.properties

    4.2  Start Kafka server
    > linux$ bin/kafka-server-start.sh config/server.properties
    > windows$ bin\windows\kafka-server-start.bat config\server.properties
    
    4.3 Once kafka service is up create the kafka topic
    > bin/kafka-topic.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic kafka-message-topic
    
    4.4 consuming test message
    > bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic kafka-message-topic --from-beginning
    
    4.5 produce test message
    > bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic kafka-message-topic
    > Hello Listeners

## 5. Start Elasticsearch server
Elasticsearch is a distributed, real-time, search analysis platform.
Elasticsearch can store data in json format, and hence can be used as NoSQL database.
> bin/elasticsearch.bat

- index: An index is equivalent to database in relational database
- mapping: A mapping is equivalent to schema in relational database

## 6 Elasticsearch REST APIs
    6.1 Check elasticsearch is running
    > http://localhost:9200

    6.2 Index APIs
        6.2.1 Create an index with name articles
        > PUT http://localhost:9200/articles
    
        6.2.2 Query an index with name articles
        > GET http://localhost:9200/articles
    
        6.2.3 Delete an index with name articles
        > DELETE http://localhost:9200/articles

        6.2.4 Update Index with proper mappings
        > PUT http://localhost:9200/articles
        {
        "mappings": {
        "dynamic": "strict",
        "properties": {
        "author": {"type": "text"},
        "title": {"type": "text"},
        "publish_date": {"type": "date"}
                }
            }
        }

    6.3 Document APIs
        6.3.1 Add a document to index. Adding id at the end is optional while saving document
        > POST http://localhost:9200/articles/_doc/1
        {"author": "Sushil", "title": "Small intro to Elasticsearch using Python", "publish_date": "2021-11-14"}

        6.3.2 Get a document from index by id
        > GET http://localhost:9200/articles/_doc/1

        6.3.3 Get all documents from index
        > GET http://localhost:9200/articles/_doc/_search

        6.3.4 Delete a document
        > DELETE http://localhost:9200/_doc/1

