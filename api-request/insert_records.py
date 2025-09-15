import psycopg2
from api_request import mock_fetch_data

def connect_to_db():
    print("Connecting to PostgreSQL database...")
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5000",
            dbname="weather_db",
            user="admin",
            password="admin"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database connection failed: {e}")
        raise

def create_table(conn: psycopg2.extensions.connection):
    print("Creating table if not exists...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_descriptions TEXT,
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT
            );
        """)
        conn.commit()
        print("Table was created.")
    except psycopg2.Error as e:
        print(f"Failed to create table: {e}")
        # conn.rollback()
        raise
    
def insert_record(conn: psycopg2.extensions.connection, record: dict):
    print("Inserting record into the database...")
    try:
        weather = record['current']
        location = record['location']
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dev.raw_weather_data (city, temperature, weather_descriptions, wind_speed, time, inserted_at, utc_offset)
            VALUES (%s, %s, %s, %s, %s, NOW(), %s);
        """, (
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0],
            weather['wind_speed'],
            location['localtime'],
            location['utc_offset']
        ))
        conn.commit()
        print("Record was inserted.")
    except psycopg2.Error as e:
        print(f"Failed to insert record: {e}")
        # conn.rollback()
        raise
    
def main():
    try:
        conn = connect_to_db()
        data = mock_fetch_data()
        create_table(conn)
        insert_record(conn, data)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Database connection closed.")
