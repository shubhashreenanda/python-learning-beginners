import psycopg2

connection = psycopg2.connect(database = "employeedb",
                              user = "admin",
                              password = "admin",
                              host = "127.0.0.1",
                              port = "5432")

print("Connected to employee database")
cursor = connection.cursor()
cursor.execute("update into employee (name,sal) values ('Anny',20000)")
connection.commit()
print("employee details updated")

connection.close()