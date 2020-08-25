#! python3
# Python program to insert a row of data into postgre.
# Insert data into public.high_score table.

import psycopg2
from config import config

def insert_score(player_name, score):
    # Insert a new vendor into the vendors table.
    sql = """INSERT INTO high_score(player_name, score)
             VALUES(%s, %s) ;"""
    conn = None
    try:
        # Read database configuration.
        params = config()
        # Connect to the PostgreSQL database.
        conn = psycopg2.connect(**params)
        # Create a new cursor.
        cur = conn.cursor()
        # Execute the INSERT statement.
        cur.execute(sql, (player_name, score,))
        # Commit the changes to the database.
        conn.commit()
        # Close communication with the database.
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
    return 0

if __name__ == "__main__":
    insert_score("Test", 123)