import mysql.connector
database = mysql.connector.connect(
    host='localhost',
    passwd='mysql',
    user='root'
)
# cursor object
curserObject = database.cursor()

# create database
curserObject.execute('CREATE DATABASE CRM')
print('All Done')
