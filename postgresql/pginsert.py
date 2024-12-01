import psycopg2

connection = psycopg2.connect(database = "employeedb",
                              user = "admin",
                              password = "admin",
                              host = "127.0.0.1",
                              port = "5432")

print("Connected to employee database")
cursor = connection.cursor()
cursor.execute("insert into employee (name,sal) values ('Bharath',20000)")
connection.commit()
print("employee created")

connection.close()