import sqlite3

con = sqlite3.connect('users.db', check_same_thread=False)
sql = con.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER, name TEXT, tel TEXT UNIQUE);')

def register(tg_id, name, num): #Регистрация пользователя
    sql.execute('INSERT INTO users VALUES (?, ?, ?);', (tg_id, name, num))
    con.commit()

def check_user(tg_id):
    if sql.execute("SELECT * FROM users WHERE id=?", (tg_id,)).fetchone():
        return True
    else:
        return False

def get_name(tg_id):
    name = sql.execute("SELECT name FROM users WHERE id=?", (tg_id,)).fetchone()[0]
    return name