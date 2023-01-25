import json
import uuid
import logging
from kafka import KafkaConsumer
from db.db import get_collection
from pymongo.errors import DuplicateKeyError

logging.basicConfig()

class Consumer():
    bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094']

    def __init__(self, topic):
        self.topic = topic
        self.group = "transaction_consumers"
        self.collection = get_collection(topic)

        self.consumer = KafkaConsumer(
            self.topic,
            client_id=uuid.uuid4(),
            group_id = self.group,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            consumer_timeout_ms=1000,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )



    def read(self):
        try:
            while True:
                for message in self.consumer:
                    print(f'New transaction: {message.value["_id"]}')
                    self.collection.insert_one(message.value)
        except KeyboardInterrupt as exc:
            self.consumer.close()
            raise KeyboardInterrupt from exc


    def read_all(self):
        return [message.value for message in self.consumer]
