from basescript import BaseScript
from confluent_kafka import Consumer

class KafkaConsumer(BaseScript):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        port = self.args.port
        server = self.args.server
        group_id = self.args.group_id
        self.poll_interval = self.args.poll_interval

        self.kafka_consumer = Consumer({
            'bootstrap.servers': '{}:{}'.format(server, port),
            'group.id': group_id,
            'auto.offset.reset': 'earliest'
                        })

        topic = self.args.topic
        self.kafka_consumer.subscribe([topic])
        self.consume_message()

    def consume_message(self):
        while True:
            message = self.kafka_consumer.poll(self.poll_interval)
            if not message:
                continue

            if message.error():
                print("Consumer error: {}".format(message.error()))
                continue

            print(message.value().decode())

    def define_args(self, parser):
        parser.add_argument('--server', type=str,
                help="kafka broker host", required=True)
        parser.add_argument('--port', type=int,
                help="kafka broker port", required=True)
        parser.add_argument('--topic', type=str,
                help="kafka topic", required=True)
        parser.add_argument('--group-id', type=str,
                help="consumer group-id", required=True)
        parser.add_argument('--poll-interval', type=float,
                help="poll interval in secs", default=0.2)

if __name__ == '__main__':
    KafkaConsumer().start()
