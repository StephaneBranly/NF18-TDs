import psycopg2

HOST = "*********"
USER = "*********"
PASSWORD = "*********"
DATABASE = "*********"

# Open connection

conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))


def display():
    login = "test"
    while(login != 0):
        try:
            login = input("\n\nEntrez le login de l'etudiant recherche (entrez 0 pour sortir) : ")
        except SyntaxError:
            pass
            login=0
        if(login!=0):
            displayStudent(login)

def displayStudent(login):
    cur = conn.cursor()
    sql = "SELECT * FROM etudiant WHERE login='%s'" % (login)
    cur.execute(sql)
    raw = cur.fetchone()
    if(raw):
        print("Notes de l'etudiant %s %s (%s)") % (raw[2], raw[1], login)
        displayNotes(login)
        displayAverage(login)
    else:
        print("Etudiant inconnu")

def displayNotes(login):
    cur = conn.cursor()
    sql = "SELECT * FROM note INNER JOIN devoir ON note.devoir = devoir.num WHERE etudiant='%s' ORDER BY daterendu ASC" % (login)
    cur.execute(sql)
    raw = cur.fetchone()
    while(raw):
        print("- %s [%s] - %s") % (raw[5], raw[4], raw[2])
        raw = cur.fetchone()

def displayAverage(login):
    cur = conn.cursor()
    sql = "SELECT AVG(valeur) FROM note WHERE etudiant='%s'" % (login)
    cur.execute(sql)
    raw = cur.fetchone()
    print("* Moyenne : %s") % (raw[0])
