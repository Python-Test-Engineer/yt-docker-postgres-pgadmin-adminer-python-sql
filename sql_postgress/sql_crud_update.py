import psycopg2


def updateTable(id, name):
    try:
        connection = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="postgres",
            host="host.docker.internal",
        )

        cursor = connection.cursor()

        print("Table Before updating record ")
       
        sql_select_query = """select * from employee where id = %s"""
        cursor.execute(sql_select_query, (id,))
        record = cursor.fetchone()
        print(record)

        # Update single record now
        sql_update_query = """Update employee set name = %s where id = %s"""
     
        cursor.execute(sql_update_query, (name, id))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from employee where id = %s"""
        cursor.execute(sql_select_query, (id,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


id = 2
name = "Craig"
updateTable(id, name)
