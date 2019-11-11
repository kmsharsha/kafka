import json

from basescript import BaseScript
from confluent_kafka import Producer

class KafkaProducer(BaseScript):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        port = self.args.port
        server = self.args.server
        self.poll_interval = self.args.poll_interval

        self.kafka_producer = Producer({
            'bootstrap.servers': '{}:{}'.format(server, port)
                        })

        topic = self.args.topic
        message = self.args.message
        self.produce_message(topic, message)

    def _check_delivery_status(self, err, message):
        '''
        Called once for each message produced to validate delivery result.
        '''
        if err:
            print ('Message delivery failed: {}'.format(err))
        else:
            print ('Message delivered to: {}'.format(message.topic()))

    def produce_message(self, topic, message):
        '''
        Produce message to the specified topic
        '''
        if not isinstance(message, str):
            message = json.dumps(message)

        self.kafka_producer.poll(self.poll_interval)
        self.kafka_producer.produce(topic, message,
                callback=self._check_delivery_status)
        self.kafka_producer.flush()

    def define_args(self, parser):
        parser.add_argument('--server', type=str,
                help="kafka broker host", required=True)
        parser.add_argument('--port', type=int,
                help="kafka broker port", required=True)
        parser.add_argument('--topic', type=str,
                help='kafka topic', required=True)
        parser.add_argument('--message', type=str,
                help='kafka message', required=True)
        parser.add_argument('--poll-interval', type=float,
                help="poll interval in secs", default=0.2)

if __name__ == '__main__':
    KafkaProducer().start()
