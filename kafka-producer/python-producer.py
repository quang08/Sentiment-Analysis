import time
from faker import Faker
from kafka import KafkaProducer 
from json import dumps

topic = 'sentence'
broker = 'kafka:9093'

def gen_data():
    faker = Faker()
    producer = KafkaProducer(bootstrap_server=broker, value_serializer=lambda x:dumps(x).encode('utf-8'))

    data = {'sentence': faker.sentence()}
    print(data)

    producer.send(topic=topic, value=data)

    producer.flush()


if __name__ == '__main__':
    time.sleep(5)
    gen_data()
