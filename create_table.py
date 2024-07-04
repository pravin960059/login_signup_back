import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
con = mysql.connector.connect(host=DATABASE_HOST,
port=DATABASE_PORT,
database=DATABASE_NAME ,
user=DATABASE_USER,
password=DATABASE_PASSWORD )
cursor = con.cursor()
# Create the login table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY,First_name VARCHAR(255) NOT NULL,Last_name VARCHAR(255) NOT NULL,Username VARCHAR(255) UNIQUE NOT NULL,Email VARCHAR(255) UNIQUE NOT NULL,password VARCHAR(255) NOT NULL)")
# Create the question table
cursor.execute("CREATE TABLE IF NOT EXISTS code (id INT AUTO_INCREMENT PRIMARY KEY,Question_name varchar(255) NOT NULL,code TEXT NOT NULL,Question_number varchar(255) NOT NULL)")
# Create the timestamp table
cursor.execute("CREATE TABLE IF NOT EXISTS timestamp (username VARCHAR(255) NOT NULL,date_time VARCHAR(255) NOT NULL)")