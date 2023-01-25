import json
import logging
from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

logging.basicConfig()

class Producer:
    bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094']
    num_partitions=3
    replication_factor=3

    def __init__(self, topic):
        try:
            admin = KafkaAdminClient(
                bootstrap_servers=self.bootstrap_servers,
                client_id="admin"
            )

            admin.create_topics([
                NewTopic(
                    name=topic,
                    num_partitions=self.num_partitions,
                    replication_factor=self.replication_factor
                )
            ])

            admin.close()

        except TopicAlreadyExistsError:
            logging.info("Topic already exits")

        self.topic = topic


    def send(self, message):
        producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            client_id="producer",
            value_serializer=lambda x: json.dumps(x).encode('utf-8'),
        )

        producer.send(topic=self.topic, value=message)
