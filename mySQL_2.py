# To show all databases present in our mysql

import mysql.connector

conn = mysql.connector.connect(host = 'localhost',user='root',port='3307',password='anupMySQL')

mycursor = conn.cursor()
mycursor.execute('show databases')
for x in mycursor:
    print(x)


