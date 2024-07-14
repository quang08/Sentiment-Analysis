import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import psycopg2
from kafka import KafkaConsumer
import json 

nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()


# Connect to Postgres
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="postgres",
    port="5432"
)

cur = conn.cursor()

# Consume from Kafka
broker = 'kafka:9092'
topic = 'sentence'

consumer = KafkaConsumer(topic, bootstrap_servers=broker, value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# Read messages
for message in consumer:
    data = message.value
    print(data)
    scores = analyzer.polarity_scores(data['sentence'])
    print(scores['compound'])

    #Insert to Postgres
    cur.execute("INSERT INTO sentences (sentence, sentiment) VALUES (%s, %s)", (data['sentence'], scores['compound']))
    conn.commit()