#!/bin/bash

echo "Installing java version 1.8 for KafkaZookeeper"
sudo apt-get install openjdk-8-jdk

echo "Adding confluent PublicKey"
wget -qO - https://packages.confluent.io/deb/3.3/archive.key | sudo apt-key add -

echo "Adding the repository to your /etc/apt/sources.list"
sudo add-apt-repository "deb [arch=amd64] https://packages.confluent.io/deb/3.3 stable main"

echo "Updating packages and installing Kafka"
sudo apt-get update && sudo apt-get install confluent-platform-oss-2.11

echo "Starting Confluent"
confluent start

echo "Status of Confluent"
confluent status

echo "Isntalling confluent kafka"
pip install confluent-kafka

echo "Installing kafka[avro]"
pip install confluent-kafka[avro]

echo "Installing dependencies"
pip install --no-binary :all: confluent-kafka
