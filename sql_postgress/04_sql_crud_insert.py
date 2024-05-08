import psycopg2

try:
    connection = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="postgres",
        host="host.docker.internal",
    )
    cursor = connection.cursor()

    postgres_insert_query = """ INSERT into employee(name, state) VALUES (%s, %s)"""
    record_to_insert = ("ZZ", "ZZ")
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
