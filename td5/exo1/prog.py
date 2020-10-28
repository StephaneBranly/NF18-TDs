import psycopg2
import csv


HOST = "*********"
USER = "*********"
PASSWORD = "*********"
DATABASE = "*********"

# Open connection

print("\nOpen connection")
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))


def createTable():
    print("\n\nCreate table")
    cur = conn.cursor()
    sql = "CREATE TABLE dpt2 (num int,nom varchar(250), population int)"
    cur.execute(sql)
    conn.commit()

def importFile():
    print("\n\nImport file")
    with open('dpt2.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        next(spamreader)
        for row in spamreader:
            cur = conn.cursor()
            sql = "INSERT INTO dpt2 VALUES ("+row[0]+",'"+row[1]+"',"+row[2]+")"
            cur.execute(sql)
            conn.commit()

def showData():
    print("\n\nTable dpt2 content :")
    cur = conn.cursor()
    sql = "SELECT * FROM dpt2"
    cur.execute(sql)
  # Fetch data line by line

    raw = cur.fetchone()
    empty = 0
    if(raw):
        max = raw[2]
        min = raw[2]
        empty = 1
    while raw:
        print ("[%s] - %s (%s)" % (raw[0], raw[1], raw[2]))
        if(raw[2]>max):
            max = raw[2]
        if(raw[2]<min):
            min = raw[2]
        raw = cur.fetchone()
    if(empty):
        print("\nNombre d'habitants de la ville la plus peuplee : %s") % (max)
        print("\nNombre d'habitants de la ville la moins peuplee : %s") % (min)

def addDpt():
    print("\n\nAdd a dpt :")
    nbr = input("Number > ")
    name = input("Name > ")
    pop = input("pop > ")
    cur = conn.cursor()
    sql = "INSERT INTO dpt2 VALUES ("+str(nbr)+",'"+name+"',"+str(pop)+")"
    print("\n"+sql)
    cur.execute(sql)
    conn.commit()

def deleteDpt():
    print("\n\nDelete a dpt :")
    nbr = input("Number > ")
    cur = conn.cursor()
    sql = "DELETE FROM dpt2 WHERE num="+str(nbr)
    cur.execute(sql)
    conn.commit()

def updateDpt():
    print("\n\nDelete a dpt :")
    nbr = input("Number of the dpt > ")
    newPop = input("Population of the dpt > ")
    cur = conn.cursor()
    sql = "UPDATE dpt2 SET population="+str(newPop)+" WHERE num="+str(nbr)
    cur.execute(sql)
    conn.commit()


def dropTable():
    print("\n\nDrop table")
    cur = conn.cursor()
    sql = "DROP TABLE dpt2"
    cur.execute(sql)
    conn.commit()

def action(c):
    if(c == 1):
        createTable()
    if(c == 2):
        importFile()
    if(c == 3):
        showData()
    if(c == 4):
        addDpt()
    if(c == 5):
        deleteDpt()
    if(c == 6):
        updateDpt()
    if(c == 7):
        dropTable()
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass



continuer = 1
while(continuer):
    print("\nWhat do you want ?")
    print("0 - Quit prog")
    print("1 - Create table")
    print("2 - Import file")
    print("3 - Show table")
    print("4 - Add dpt")
    print("5 - Delete dpt")
    print("6 - Update dpt")
    print("7 - Drop table\n")
    continuer=input("> ")
    action(continuer)
# Open a cursor to send SQL commands
#cur = conn.cursor()

# Execute a SQL INSERT command
#sql = "INSERT INTO t VALUES ('Hello',1)"
#cur.execute(sql)
# Commit (transactionnal mode is by default)
#conn.commit()

# Close connection




print("\nClose connection")
conn.close()
