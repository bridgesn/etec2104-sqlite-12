import sqlite3

conn = sqlite3.connect('scores.db')
curs = conn.cursor()
curs.execute('''create table if not exists scores (name, score)''')

def addScore( name, score ):
    curs.execute("""insert into scores values (?,?)""",(name, score))
    conn.commit()

def getScores():
    curs.execute("""select * from scores order by score""")
    return curs.fetchall()

def clearScores():
    curs.execute("""delete from scores""")
    conn.commit()
