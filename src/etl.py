import os
import csv
import glob
import psycopg2
import pandas as pd
from sql_queries import *
from create_tables import *
import sys
from datetime import datetime

sys.path.insert(0, '../src')
sys.path.insert(0, '../data')


def process_csv_file(cur, conn, filepath, table, script):
    ''' 
     - This function:
        - opens a csv file and inserts required information into final table of a db
    
    Args: 
        cur (object): psycopg2 cursor to execute PostgreSQL command in a db session
        filepath (str): filepath to a folder containing song files
        table (str): table name
        script (object): script to insert data
    
    Returns:
         None
    '''
    a = table
    print(f'ETL Step - Loading Data Processing to {a}: ' + str(datetime.now()))
    
    # open file
    with open (filepath, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader) # Skip the header row
        for row in reader:
             # insert records
            cur.execute(script, row)
            row
            conn.commit()
    
    print(f'ETL Step - Load Data Processing to {a} table completed: ' + str(datetime.now()))

     

def main():
    ## Initiate Connection
    print('ETL Step - Creating Postgresql Connection: ' + str(datetime.now()))
    conn = psycopg2.connect("host=127.0.0.1 port=15432 dbname=liquidity_db user=student password=student")
    cur = conn.cursor()
    print('ETL Step - Postgresql Connection Created: ' + str(datetime.now()))

    print('ETL Step - Cleaning all final tables: ' + str(datetime.now()))
    truncate_tables(cur, conn)
    print('ETL Step - All final tables cleaned: ' + str(datetime.now()))

    ## Load data to db
    process_csv_file(cur, conn, filepath='../data/raw/data_ads.csv', table='ads', script=ads_table_insert)

    process_csv_file(cur, conn, filepath='../data/raw/data_categories.csv',  table='categories', script=categories_table_insert)
    
    process_csv_file(cur, conn, filepath='../data/raw/data_segments.csv', table='segments',  script=segments_table_insert)

    process_csv_file(cur, conn, filepath='../data/raw/data_replies.csv', table='replies', script=replies_table_insert)

    conn.close()


if __name__ == "__main__":
    main()