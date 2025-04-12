"""
1-brew services start zookeeper
2-brew services start kafka
3-/opt/homebrew/Cellar/kafka/3.9.0/bin/kafka-topics --create --topic task-events --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
4-/opt/homebrew/Cellar/kafka/3.9.0/bin/kafka-console-consumer --topic task-events --from-beginning --bootstrap-server localhost:9092
5-in the root directory of your project: python kafka_producer.py
"""
import json

from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


def send_task_event(task_data):
    producer.send('task-events', task_data)
    producer.flush()
