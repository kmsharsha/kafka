#!/bin/bash

# GO

echo "Downloading go packages..."
wget https://dl.google.com/go/go1.11.4.linux-amd64.tar.gz

echo "Unpacking go packages..."
sudo tar -C /usr/local -xzvf go1.11.4.linux-amd64.tar.gz

echo "Updating go path..."
echo 'export GOROOT=/usr/local/go' >> ~/.bashrc
echo 'export PATH=$PATH:$GOROOT/bin' >> ~/.bashrc
source ~/.bashrc

echo "Removing downloaded tar file..."
rm go1.11.4.linux-amd64.tar.gz

echo "Checking go version..."
go version

# GO - Confluent_Kafka dependencies

echo "setting up kafka..."
git clone https://github.com/edenhill/librdkafka.git
cd librdkafka
./configure --prefix /usr
make
sudo make install
cd ..

go get -u gopkg.in/confluentinc/confluent-kafka-go.v1/kafka
