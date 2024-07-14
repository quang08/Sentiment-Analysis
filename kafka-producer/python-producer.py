import time
from faker import Faker
from kafka import KafkaProducer 
from json import dumps
import schedule

topic = 'sentence'
broker = 'kafka:9092'

def gen_data():
    faker = Faker()
    producer = KafkaProducer(bootstrap_servers=broker, value_serializer=lambda x:dumps(x).encode('utf-8'))

    data = {'sentence': faker.sentence()}
    print(data)

    producer.send(topic=topic, value=data)

    producer.flush()


if __name__ == '__main__':
    schedule.every(5).seconds.do(gen_data) # run every 5 seconds but does not run automatically

    while True: # to run the scheduled task
        schedule.run_pending() # executes any pending scheduled tasks.
        time.sleep(0.5)
