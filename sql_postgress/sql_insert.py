# importing psycopg2 module
import psycopg2


# Connect to existing database
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="host.docker.internal",
)

# creating a cursor object
cursor = conn.cursor()

# list that contain records to be inserted into table
data = [
    ("Babita", "Bihar"),
    ("Anushka", "Hyderabad"),
    ("Anamika", "Banglore"),
    ("Sanaya", "Pune"),
    ("Radha", "Chandigarh"),
]

# inserting record into employee table
for d in data:
    cursor.execute("INSERT into employee(name, state) VALUES (%s, %s)", d)

print("List has been inserted to employee table successfully...")

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
