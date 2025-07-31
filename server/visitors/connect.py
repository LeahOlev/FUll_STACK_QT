#import pyodbc
#
#conn = pyodbc.connect(
#    'DRIVER={ODBC Driver 17 for SQL Server};'
#    'SERVER=localhost;'
#    'DATABASE=your_database;'
#    'UID=your_username;'
#    'PWD=your_password'
#)
#
#cursor = conn.cursor()
#cursor.execute("SELECT * FROM your_table")
#
#for row in cursor.fetchall():
#    print(row)
#
#cursor.close()
#conn.close()
#