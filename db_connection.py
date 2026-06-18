# db_connection.py

import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="khushi@2004",
        database="marketplace_analytics"
    )
    return conn