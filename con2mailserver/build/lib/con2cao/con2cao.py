import pyodbc
import time
import mysql.connector as connector
import datetime
import logging
import os


class Con2cao():
    
    def __init__(self):        
        self.is_alive = True
        self.pg_conn = None
        self.pg_cur = None
        self.pg_conn_str = None
        self.main()
    def reconnect_to_pgsql(self):
        attempts = 0
        while self.is_alive and attempts < 10:
            try:
                self.pg_conn = pyodbc.connect(self.pg_conn_str, autocommit=True)
                self.pg_cur = self.pg_conn.cursor()
                logging.info("Reconnected to PostgreSQL")
                break
            except pyodbc.Error as e:
                attempts += 1
                
                time.sleep(5)

    def execute_query(self, sql):
        for i in range(10):
            try:
                self.pg_cur=self.pg_cur.execute(sql)
                return self.pg_cur
                
            except Exception as e:
                if "syntax error" not in str(e):
                    if i < 9:        
                        logging.error(f"Error executing query: {e}. This is {i+1} times. Retrying in 3 seconds...")
                        time.sleep(3)
                        self.reconnect_to_pgsql()                
                    else:
                        logging.error(f"Error executing query: {e}. Giving up after 10 attempts.")
                else:
                    logging.error(f"Error executing query: {e}.")
                     
    def main(self):
        
        self.pg_conn_str = (
            r'DRIVER={PostgreSQL ANSI(x64)};'
            r'SERVER=127.0.0.1;'
            r'DATABASE=cao50001;'
            r'UID=postgres;'
            r'PWD=111111;'
            r'PORT=5432;'
            r'charset=SQL_ASCII;'
            r'set stament_timeout=6000000;'
        )
        self.reconnect_to_pgsql()
        
class Con2fuxi():
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect_to_mysql()
    def connect_to_mysql(self):
        try:
            self.conn = connector.connect(
                host='127.0.0.1',  # replace with your server name
                user='bertsu',  # replace with your username
                password='tzj0125',  # replace with your password
                database='fuxi',  # replace with your database name
                port=3306  # replace with your port, MySQL default port is 3306
            )
            print("Connection established")
            self.cursor=self.conn.cursor()
            
            
        except connector.Error as err:
            print("Unable to connect to the mysql database")
            print(err)
            return None
    def commit(self):
        self.conn.commit()
        
def convert_pg_type_to_mysql_type(pg_type):
    if pg_type in ['integer', 'bigint', 'smallint']:
        return 'INT'
    elif pg_type in ['character varying']:
        return 'VARCHAR(60)'
    elif pg_type in ['text']:
        return 'TEXT(255)'
    elif pg_type in ['timestamp without time zone']:
        return 'VARCHAR(18)'
    else:
        return 'VARCHAR(255)'
    

    