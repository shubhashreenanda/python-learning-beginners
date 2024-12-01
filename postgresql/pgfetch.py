import psycopg2

connection = psycopg2.connect(database = "employeedb",
                              user = "admin",
                              password = "admin",
                              host = "127.0.0.1",
                              port = "5432")

print("Connected to employee database")
cursor = connection.cursor()
cursor.execute("select * from employee..")
rows = cursor.fetchall()
for row in rows:
    print("ID", row[0])
    print("Name", row[1])
    print("Salary", row[2])


connection.close()