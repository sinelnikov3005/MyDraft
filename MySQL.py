import mysql.connector

mydb = mysql.connector.connect(user="root", password="30051993", host="127.0.0.1", auth_plugin='mysql_native_password')

print(mydb)
# mycursor = mydb.cursor()
