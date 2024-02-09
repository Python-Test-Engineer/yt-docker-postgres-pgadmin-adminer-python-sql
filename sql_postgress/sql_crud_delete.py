import psycopg2


def deleteData(id):
    try:
        connection = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="postgres",
            host="host.docker.internal",
        )

        cursor = connection.cursor()

        # Update single record now
        sql_delete_query = """Delete from employee where id = %s"""
        cursor.execute(sql_delete_query, (id,))
        connection.commit()
        count = cursor.rowcount
        print(count, f"Record {id} deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

for i in range(17): 
    deleteData(i)
    