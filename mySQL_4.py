# Insert values in student table of pythondb database

import mysql.connector

conn = mysql.connector.connect(host = 'localhost',user='root',port='3307',password='anupMySQL',database='pythondb')

mycursor = conn.cursor()

sql = 'insert into student (name,branch,id) values(%s,%s,%s)'
#val = ('john','cse',56)  # for only insertion of 1 row

# if user want to create multiple value then you can create list 
val = [('john','cse','56'),('mike','IT','78'),('tyson','me','80')]
#mycursor.execute(sql,val)  # for only execution of 1 row
mycursor.executemany(sql,val)
conn.commit()
print(mycursor.rowcount,'record inserted')
