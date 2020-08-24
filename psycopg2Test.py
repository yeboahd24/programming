import psycopg2 # importing the Postgresql.

# Establishing the database.
conn = psycopg2.connect(database="postgres",
	                    user = "postgres",
	                    host = "localhost",
	                    password = "example", # Note you need your correct password here.
	                    port = "5432")



cur = conn.cursor()  # The cursor allow you to execute database queries.

cur.execute("""CREATE TABLE STUDENTS (
				id INT NOT NULL,
				name TEXT NOT NULL,
				index TEXT NOT NULL

				)""")

cur.execute("""INSERT INTO STUDENTS(id, name, index)
				VALUES(1, 'lINUX', 'UED356712')""")

cur.execute("""INSERT INTO STUDENTS(id, name, index)
				VALUES(2, 'PARROT', 'UED356778')""")

cur.execute("SELECT * FROM STUDENTS")

rows = cur.fetchall()

for row in rows:
	print(f'ID: {row[0]}')
	print(f'NAME: {row[1]}')
	print(f'INDEX: {row[2]}')

conn.commit()
conn.close()