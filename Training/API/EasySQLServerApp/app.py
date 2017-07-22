import pyodbc

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=DESKTOP-V1MD90G\SQLEXPRESS;'
    r'DATABASE=Remi;'
    r'Trusted_Connection=yes;'
    )

cursor = conn.cursor()
cursor.execute('SELECT TOP 10 * FROM [dbo].[JobExecutions];')
for entry in cursor:
    print(entry)
