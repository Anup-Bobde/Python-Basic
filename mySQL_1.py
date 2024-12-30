# Python-MySQL Databse Connectivity(Here we have to install mysql.connector by pip install mysql-connector-python  

import mysql.connector

conn=mysql.connector.connect(host='localhost',user='root',port='3307',password='anupMySQL')  
if conn.is_connected():
    print('Connection Established')

print(conn)

# Above we mention port='3307' because our mysql is on 3307 port instead of 3306 port
