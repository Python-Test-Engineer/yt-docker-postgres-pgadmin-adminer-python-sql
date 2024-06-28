Set up of Docker with Postgress, PgAdmin and Adminer with Python CRUD.

Combines PgAdmin and Adminer for DB viewing.

Ensure Docker is running.

Create venv and pip install requirments.


### Tested: 28JUN2024

If you ever unable to login to PgAdmin when you have been able to do so before, delete all images/vols/containers for this set up and reclone repo. This happened to me and doing the afore mentioned solved the issue.

Python SQL worked fine.

### Other Docker compose files

I have added a `docker-compose-named-volume.yml` if you prefer this to having the data saved in the project with a bound mount volume.

[YouTube](https://youtu.be/mipRKPHwlBkI)

https://youtu.be/mipRKPHwlBk

NOTE
```
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="host.docker.internal", !!! localhost etc don't seem to work...
)
```

### PgAdmin

<img src="./images/register-server-1.png"  width="500" >

<img src="./images/register-server-2.png"  width="500" >


<!-- ![PAGE](./images/register-server-1.png ) -->


- http://localhost:5050/
- admin@email.com
- admin

register-server

page-1 use any name
page-2:
      - POSTGRES_DB=postgres # optional
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres

run docker-compose up in terminal ->

 ✔ Network postgres_default       Created                                                                                 
 ✔ Container postgres-pg-admin-1  Created                                                                                 
 ✔ Container postgres-postgres-1  Created                                                                                 
 ✔ Container postgres-adminer-1   Created     

### Adminer

admininer login on port http://localhost:8080

password and most variables are `postgres`. You can change them as you wish.

<img src="./images/adminer-login.png"  width="500" >
