#!/bin/sh

# Start Zookeeper
docker run -d --name zookeeper -p 2181:2181 zookeeper:3.4.9

# Start Kafka
docker run -d --name kafka -p 9092:9092 --link zookeeper:zookeeper \
    -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \
    -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
    -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 confluentinc/cp-kafka:latest

# Start Kafka UI
docker run -d --name kafka-ui -p 8080:8080 \
    --link zookeeper:zookeeper \
    --link kafka:kafka \
    -e KAFKA_CLUSTERS_0_NAME=local \
    -e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=kafka:9092 \
    -e KAFKA_CLUSTERS_0_ZOOKEEPER=zookeeper:2181 \
    provectuslabs/kafka-ui:latest
