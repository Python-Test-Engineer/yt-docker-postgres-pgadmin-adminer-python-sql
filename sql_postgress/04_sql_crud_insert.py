import psycopg2
import string
import random

# initializing size of string
N = 7


def get_random_string(N):
    # using random.choices()
    # generating random strings
    result = "".join(random.choices(string.ascii_uppercase + string.digits, k=N))
    # res2 = "".join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return result


# print result
# print("The generated random res1 : " + str(res1))
# print("The generated random res2 : " + str(res2))


try:
    connection = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="postgres",
        host="host.docker.internal",
        # host="postgres",
    )
    cursor = connection.cursor()
    for i in range(10):
        n1 = random.randint(5, 15)
        n2 = random.randint(3, 10)
        postgres_insert_query = """ INSERT into employee(name, state) VALUES (%s, %s)"""
        record_to_insert = (get_random_string(n1), get_random_string(n2))
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
