import MySQLdb
import sys

try:
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="ecowatt", port=3306, connect_timeout=5)
    print("Connection successful")
    db.close()
except Exception as e:
    print(f"Connection failed: {e}")
    sys.exit(1)
