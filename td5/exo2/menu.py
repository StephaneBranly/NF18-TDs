import psycopg2
from display import display


HOST = "*********"
USER = "*********"
PASSWORD = "*********"
DATABASE = "*********"
# Open connection

print("\nOpen connection")
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))

#init tables
"""
cur = conn.cursor()
sql = "CREATE TABLE etudiant(login CHAR(8) PRIMARY KEY,nom TEXT,prenom TEXT);"
cur.execute(sql)

cur = conn.cursor()
sql = "CREATE TABLE devoir(num INTEGER PRIMARY KEY,daterendu DATE UNIQUE NOT NULL,description TEXT NOT NULL);"
cur.execute(sql)

cur = conn.cursor()
sql = "CREATE TABLE note(etudiant CHAR(8) REFERENCES etudiant(login),devoir INTEGER REFERENCES devoir(num),valeur INTEGER NOT NULL,PRIMARY KEY(etudiant, devoir),CHECK (valeur BETWEEN 0 AND 20));"
cur.execute(sql)

cur = conn.cursor()
sql = "INSERT INTO etudiant(login, nom, prenom) VALUES ('bfrankli', 'Franklin', 'Benjamin');"
cur.execute(sql)

cur = conn.cursor()
sql = "INSERT INTO devoir(num, daterendu, description) VALUES (1, '10-05-2013','Structures de donnees en C');"
cur.execute(sql)

cur = conn.cursor()
sql = "INSERT INTO note(etudiant, devoir, valeur) VALUES ('bfrankli', 1, 15);"
cur.execute(sql)
"""


display()

conn.commit()
print("\nClose connection")
conn.close()
