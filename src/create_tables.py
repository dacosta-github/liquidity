import psycopg2
from sql_queries import create_table_queries, drop_table_queries, truncate_table_queries
import sys
from datetime import datetime

sys.path.insert(0, '../src')
sys.path.insert(0, '../data')


def create_database():
    """
    - This function:
        - creates and connects to the db 
        - returns the connection and cursor to db
    
    Args:
        None

    Returns:
        cur (object): psycopg2 cursor object to execute PostgreSQL command in a db session
        conn (object): psycopg2 connection object to db
    """
    
    # connect to default database postgres_db
    conn = psycopg2.connect("host=127.0.0.1 port=15432 dbname=postgres_db user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create liquidity_db database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS liquidity_db")
    cur.execute("CREATE DATABASE liquidity_db WITH ENCODING 'utf8' TEMPLATE template0")
    cur.execute("GRANT CONNECT ON DATABASE liquidity_db TO public;")
    cur.execute("REVOKE CONNECT ON DATABASE liquidity_db FROM public;")

    # close connection to default database
    conn.close()    
    
    # connect to liquidity_db database
    conn = psycopg2.connect("host=127.0.0.1 port=15432 dbname=liquidity_db user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    - This function: 
        - drops each table using the queries in drop_table_queries list (from sql_queries.py)
    
    Args:
        cur (object): psycopg2 cursor object to execute PostgreSQL command in a db session
        conn (object): psycopg2 connection object to sparkify db
    
    Returns:
        None
    """

    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    - This function:
        - creates each table using the queries in create_table_queries list (from sql_queries.py)
    
    Args:
        cur: psycopg2 cursor object to execute PostgreSQL command in a db session
        conn: psycopg2 connection object to db
    
    Returns:
        None
    """

    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def truncate_tables(cur, conn):
    """
    - This function: 
        - truncs each table using the queries in truncate_table_queries list (from sql_queries.py)
    
    Args:
        cur (object): psycopg2 cursor object to execute PostgreSQL command in a db session
        conn (object): psycopg2 connection object to sparkify db
    
    Returns:
        None
    """

    for query in truncate_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - This function: 
        - drops (if exists) and creates the db
        - establishes connection with the db and gets cursor to it 
        - drops all the tables
        - creates all tables needed
        - closes the connection

    Args:
        None
    
    Returns:
        None
    """
    print('Creating database: ' + str(datetime.now()))
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    print('Process executed with success. Database created: ' + str(datetime.now()))
    conn.close()


if __name__ == "__main__":
    main()