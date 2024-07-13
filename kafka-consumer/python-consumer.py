from kafka import KafkaConsumer
import json
from nltk.sentiment.vader import SentimentItensityAnalyzer
import psycopg2
import nltk # natural language toolkit

nltk.download('vader_lexicon') #  downloads the lexicon (dictionary) needed for the VADER sentiment analysis tool
analyzer = SentimentItensityAnalyzer()

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname = 'postgres',
    user='postgres',
    password='postgres',
    host='postgres',
    port='5432'
)

cur = conn.cursor()

# Connect to Kafka
broker = 'kafka:9093'
topic = 'sentence'

consumer = KafkaConsumer(topic,
                         bootstrap_servers=broker,
                         value_deserializer=lambda m: json.loads(m.decode('utf-8'))
                        )

# Consume messages using a loop
for message in consumer:
    data = message.value
    print(data)
    scores = analyzer.polarity_scores(data['sentence'])
    print(scores['compound'])

    # Insert data into Postgres
    cur.execute("INSERT INTO sentences (sentence, sentiment) VALUES (%s, %s)", data['sentence'], scores['compound'])
    conn.commit()

