#! Python3
# Python program for querying data in PostgreSQL.
# Query data from public.high_score table

import psycopg2
from config import config

def query_all_tables(table_name):
    # Query all data in table vendors.
    conn = None
    rows_number = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT * FROM {} ORDER BY SCORE DESC, TIME_CREATED ASC LIMIT 10'.format(table_name))
        result = cur.fetchall()
        print(result)
        rows_number = cur.rowcount
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
    print("\nRows affected: {}".format(rows_number))
    return rows_number

if __name__ == "__main__":
    query_all_tables("high_score")
    