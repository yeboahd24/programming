import sqlite3


conn = sqlite3.connect('owners.db')
curs = conn.cursor()

# curs.execute("""CREATE TABLE COMPANY(
# 				ID INT PRIMARY KEY NOT NULL,
# 				NAME TEXT NOT NULL,
# 				AGE INT NOT NULL,
# 				ADDRESS CHAR(50),
# 				SALARY REAL
# 				)""")
# curs.execute("INSERT INTO COMPANY VALUES (1, 'Paul',32, 'California', 20000.00)")
# curs.execute("INSERT INTO COMPANY VALUES (2, 'Allen',25, 'Texas', 15000.00)")
# curs.execute("INSERT INTO COMPANY VALUES (3, 'Linux',23, 'Canada', 50000.00)")
# curs.execute("INSERT INTO COMPANY VALUES (4, 'Teddy',45, 'Norway', 7000.00)")
# curs.execute("INSERT INTO COMPANY VALUES (5, 'Kim',34, 'California', 20000.00)")
# curs.execute("INSERT INTO COMPANY VALUES (6, 'Herson',36, 'Texas', 10000.00)")
# curs.execute("INSERT INTO COMPANY VALUES (7, 'James',40, 'California', 250000.00)")

# all_owners=curs.execute("SELECT * FROM COMPANY WHERE SALARY > 10000")
# all_owners=curs.execute("SELECT * FROM COMPANY")
# all_owners=curs.execute("SELECT * FROM COMPANY WHERE SALARY = 10000")
# all_owners=curs.execute("SELECT * FROM COMPANY WHERE SALARY > 10000 AND AGE >=20")
# all_owners=curs.execute("SELECT * FROM COMPANY WHERE NAME LIKE 'Li%' ")
# all_owners=curs.execute("SELECT * FROM COMPANY WHERE NAME GLOB 'Li*' ")
# all_owners=curs.execute("SELECT * FROM COMPANY WHERE SALARY > 10000")
# all_owners=curs.execute("SELECT * FROM COMPANY WHERE AGE NOT IN (23, 25)")

for x in all_owners:
	print(*x)

conn.commit()
conn.close()









