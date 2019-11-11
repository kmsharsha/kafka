#!/bin/bash

echo "Installing pip3..."
sudo apt install python3-pip

echo "Upgrading pip..."
pip3 install --upgrade pip

# Python3 - Confluent kafka

echo "Isntalling confluent kafka..."
pip3 install confluent-kafka

echo "Installing kafka[avro]..."
pip3 install confluent-kafka[avro]

echo "Installing dependencies..."
pip3 install --no-binary :all: confluent-kafka

# python3 - BaseScript

echo "Installing basescript"
pip3 install basescript
