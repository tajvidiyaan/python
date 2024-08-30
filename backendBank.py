import sqlite3

def connect():
    con =sqlite3.connect("bank.db")
    curs = con.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS bank(id INTEGER PRIMARY KEY, Name text, Phone INTEGER, Number INTEGER, Code INTEGER)")
    con.commit()
    con.close()

def insert(Name, Code, Number, Phone):
    con =sqlite3.connect("bank.db")
    curs = con.cursor()
    curs.execute("INSERT INTO bank VALUES (null,?,?,?,?)",(Name, Code, Number, Phone))
    con.commit()
    con.close()

def view():
    con =sqlite3.connect("bank.db")
    curs = con.cursor()
    curs.execute("SELECT * FROM bank")
    rows = curs.fetchall()
    con.close()
    return rows

def search(Name="", Code="", Number="", Phone=""):
    con =sqlite3.connect("bank.db")
    curs = con.cursor()
    curs.execute("SELECT * FROM bank WHERE Name=? OR Code=? OR  Number=? OR Phone=?",(Name, Code, Number, Phone))
    rows = curs.fetchall()
    con.close()
    return rows


def delete(id):
    # delete something from book.db where id is equal to something.
    curs.execute("DELETE FROM book WHERE id=?", (id,))
    con.commit()
    # conn.close()



def update(id , Name, Code, Number, Phone):
    con = sqlite3.connect("bank.db")
    curs = con.cursor()
    curs.execute("UPDATE bank SET Number=?, Code=? Number=?, Phone=? WHERE id=?",(Name, Code, Number, Phone, id))
    con.commit()
    con.close()



# connect()
#
# insert("mahtab",25,2,4554)
# print(view())
