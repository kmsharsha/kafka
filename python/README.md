# Python - Confluent Kafka

Build Confluent Kafka based architectures in Python3

## Installation:

```
./setup.sh
```

## Example Run:

### Producer

```
python producer.py run --server <server> --port <port> --topic <topic> --message "message"
```

### Consumer

```
python consumer.py run --server <server> --port <port> --topic <topic> --group-id <group_id>
```
