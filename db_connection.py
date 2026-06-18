# db_connection.py

#import mysql.connector

#def get_connection():
#    conn = mysql.connector.connect(
 #       host="localhost",
  #      user="root",
   #     password="khushi@2004",
    #    database="marketplace_analytics"
   # )
    #return conn 
    
import pandas as pd
    
students= pd.read_csv("data/students.csv")
jobs= pd.read_csv("data/jobs.csv")
companies= pd.read_csv("data/companies.csv")
interviews= pd.read_csv("data/interviews.csv")
    
    