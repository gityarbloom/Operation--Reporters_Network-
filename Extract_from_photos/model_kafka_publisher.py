from confluent_kafka import Producer
import json


class KafkaPublisher:

    def __init__(self, kafka_config: dict):
        self.prod = Producer(kafka_config)

    @staticmethod
    def delivery_report(err, msg):
        if err:
            print(f"❌ Delivery failed: {err}")
        else:
            print(f"✅ Delivered to {msg.topic()} ")
            print(f"[{msg.partition()}] @ offset {msg.offset()}")

    def send_to_kafka(self, topic_name: str, data: dict):
        try:
            value = json.dumps(data).encode("utf-8")
            self.prod.produce(topic=topic_name, value=value, callback=self.delivery_report)
            self.prod.poll(0)
            return "\nSuccesful sending to kafka\n"
        except Exception as e:
            raise Exception(str(e))

    def close(self):
        self.prod.flush()





# class KafkaPublisher:

#     def __init__(self, kafka_config: dict):
#         self.kafka_config = kafka_config
#         self.prod = self.get_kafka_producer()

#     def get_kafka_producer(self):
#         kafka_producer = Producer(self.kafka_config)
#         return kafka_producer

#     @staticmethod
#     def delivery_report(err, msg):
#         if err:
#             print(f"❌ Delivery failed: {err}")
#         else:
#             print(f"✅ Delivered {msg.value().decode('utf-8')}")
#             print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")

#     def send_to_kafka(self, topic_name: str, data: dict):
#         try:
#             value = json.dumps(data).encode('utf-8')
#             self.prod.produce(topic=topic_name, value=value, callback=self.delivery_report)
#             self.prod.poll(0)
#         self.prod.poll(0)
#     except BufferError as e:
#         print(f"⚠ Queue full: {e}")