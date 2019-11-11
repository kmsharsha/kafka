# kafka - v0.3

In simple terms Apache Kafka is a data streaming platform to handle continous flow of data in real time with fault tolerence.

## Terminology:
### Producer:

- It is the application which sends data to kafka server .
- Data is called as message in Kafka.
- For kafka message is just a array of bytes.
- Kafka can have many producers. This can be setup based on our requirement.

### Consumer:

- Producer sends data to Kafka server and Consumer will get the data from Kafka server.

- They can get data from more than one producers.

- If consumer goes down for any reason, when it comes back up it will start reading messages from where it last left.

### Broker:

- The producer and consumer interact using the Broker as an agent.

### Cluster:

- Group of Brokers form a cluster.

### Topic:

- A topic is unique name for a data stream.
- It is similar to a category to differentiate between the type of data sent.
- When a data is send by the producer it creates a Topic and all the data is sent under this topic.
- The consumer’s subsrcibe to these topics to choose the data they want to recieve.

## Installation:

Install Confluent Kafka

```
./setup.sh
```
