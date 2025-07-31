# import pyodbc
#
# # פרטי החיבור
# server = 'שם_השרת'
# database = 'שם_המאגר'
# username = 'שם_המשתמש'
# password = 'סיסמה'
#
# # יצירת חיבור
# connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
# connection = pyodbc.connect(connection_string)
#
# # יצירת אובייקט קורסור
# cursor = connection.cursor()
#
# # ביצוע שאילתת SELECT
# cursor.execute('SELECT * FROM שם_הטבלה')
#
# # שליפת התוצאות
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
#
# # סגירת החיבור
# cursor.close()
# connection.close()

import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost:5000;'
    'DATABASE=QuickTrip;'
    'UID=heni;'
    'PWD=heni90949'
)

cursor = conn.cursor()
cursor.execute('SELECT * FROM attractions')
for row in cursor:
    print(row)

