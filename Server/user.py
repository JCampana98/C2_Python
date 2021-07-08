import db

con = db.sql_connection()

cursor = con.cursor()


def check_user_existence(username):

    cursor.execute('''
        SELECT id, username FROM users
    ''')
    users = cursor.fetchall()

    # Check if given user exists in DB
    for user in users:
        if user[1] == username:
            return user[0]

    print("Usuario o contraseña incorrecta")
    return False


def login(username, password):

    id = check_user_existence(username)

    if id:
        cursor.execute('''
            SELECT username, password, name FROM users WHERE id = (?)
        ''', [id])
        user = cursor.fetchone()
        if user[1] == password:
            print("Bienvenido " + user[2])
            return user
        else:
            print("Usuario o contraseña incorrecta")
            return False
    else:
        return False


username = "JCapana"
password = "campna12"

login(username, password)
