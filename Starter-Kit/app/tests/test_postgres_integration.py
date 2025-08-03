import psycopg2
import os

def get_conn():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=os.getenv("POSTGRES_PORT", 5432),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "postgres"),
        dbname=os.getenv("POSTGRES_DB", "postgres"),
    )

def test_insert_user():
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            # Create table if not exists
            cur.execute("""
                CREATE TABLE IF NOT EXISTS "user" (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50),
                    last_name VARCHAR(50)
                )
            """)
            conn.commit()

            # Insert user
            cur.execute("""
                INSERT INTO "user" (first_name, last_name)
                VALUES (%s, %s)
                RETURNING id
            """, ("John", "Doe"))
            inserted_id = cur.fetchone()[0]
            conn.commit()

            # Query inserted user
            cur.execute("SELECT first_name, last_name FROM \"user\" WHERE id = %s", (inserted_id,))
            user = cur.fetchone()

            assert user == ("John", "Doe")
    finally:
        conn.close()
