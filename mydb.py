import mysql.connector

from decouple import config


dataBase = mysql.connector.connect(
    host=config('DB_HOST'),
    user=config('DB_USER'),
    passwd=config('DB_PASSWORD'),
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE mojabaza")

print("Database created successfully")