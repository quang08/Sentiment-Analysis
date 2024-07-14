import streamlit as st
import time
import psycopg2
from psycopg2 import OperationalError
import logging

logging.basicConfig(level=logging.INFO)

DB_HOST="postgres"
DB_NAME="postgres"
DB_USER="postgres"
DB_PASSWORD="postgres"
DB_PORT="5432"

def fetch_data():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sentences")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        return rows
    except OperationalError as e:
        st.err(f"OperationalError: {e}")
        return []
    except Exception as e:
        return []

def main():
    st.title("Sentence Dashboard")
    st.write("Here's your sentiment analysis on sentence data: ")

    unique_id = set() # keep track of unique IDs to avoid duplicate display of data

    while True:
        data = fetch_data()
        if data:
            for row in data:
                id = row[0]
                if id in unique_id:
                    continue # Checks if the ID of the row (id = row[0]) is already in unique_id; if so, skips displaying the row.
                st.write(row)
                unique_id.add(id)
        else:
            st.write("")
        time.sleep(5)

if __name__ == "__main__":
    main()