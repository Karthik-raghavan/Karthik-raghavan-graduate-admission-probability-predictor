import pandas as pd
import requests
import mysql.connector
from mysql.connector import Error
import os 

def collect_data_from_csv(csv_file_path):
    """Load data from csv file"""
    if os.path.exists(csv_file_path):
        data = pd.read_csv(csv_file_path)
        print("Data Loaded successfully from csv")
        return data
    else:
        print(f'CSV file not found {csv_file_path}')
        return None
    
def collect_data_from_mysql(host, user, password, database, query):
    """Load data from MySQL Database"""
    try:
        connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        if connection.is_connected():
            print("Connected to MySQL Database")
            data = pd.read_sql_query(query, connection)
            print("Data loaded successfully from MySQL Database")
            return data
    except Error as E:
        print(f"Error while connecting to MySQL: {E}")
        return None
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")


def main():
    #Example paths and parameters
    csv_file_path = r"data\raw\education_admission.csv" #Path to csv file

    #MySQL connection parameters
    mysql_host = 'localhost' # MySQL server host
    mysql_user = 'karthikraghavan' # MySQL username
    mysql_password = 'karthikraghavan' # MySQL password
    mysql_database = 'education' # MySQL database name
    mysql_query = 'SELECT * FROM education_data;' # Example SQL query

    #Collect Data
    csv_data = collect_data_from_csv(csv_file_path)
    mysql_data = collect_data_from_mysql(mysql_host, mysql_user, mysql_password, mysql_database, mysql_query)

    #Combine or process collected data as needed
    if csv_data is not None:
        print("CSV Data Sample")
        print(csv_data.head())

    if mysql_data is not None:
        print("MySQL Data Sample:")
        print(mysql_data.head())


if __name__ == "__main__":
    main()