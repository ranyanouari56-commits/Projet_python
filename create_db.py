import MySQLdb
import sys

try:
   
    db = MySQLdb.connect(host="localhost", user="root", passwd="")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ecowatt CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    print("Database 'ecowatt' verified/created successfully.")
    db.close()
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
