import sqlite3

from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('dogapp.db')
        return con

    except Error:
        print(Error)


def sql_create_table(con):
    cursorObj = con.cursor()

    # Create tables..
    cursorObj.execute(
        "CREATE TABLE users("
        "id integer PRIMARY KEY, "
        "username text, "
        "password text, "
        "role text, "
        "name text, "
        "email text, "
        "phone text)")
    cursorObj.execute(
        "CREATE TABLE dogs("
        "id integer PRIMARY KEY, "
        "name text)")

    users = [
        [1, "admin", "admin", "admin", "Administrador", "admin.admin@gmail.com", "2604111111"],
        [2, "JCampana", "campana12", "user", "Julian Campana", "campana.jullian@gmail.com", "2604111111"],
        [3, "FLuna", "luna1234", "user", "Facundo Luna", "facundo.luna@gmail.com", "2604111111"],
        [4, "DCordoba", "cordoba12", "user", "Diego Cordoba", "cordoba.diego@gmail.com", "2604111111"]
    ]

    con.commit()

    dogs = [
        [1, "Pepito"],
        [2, "Samuel"],
        [3, "Belzebu"],
        [4, "Satan"]
    ]

    # Add data to tables.
    cursorObj.executemany(''' 
     INSERT INTO users(id, username, password, role, name, email, phone) VALUES(?,?,?,?,?,?,?)
     ''', users)

    cursorObj.executemany(''' 
     INSERT INTO dogs(id, name) VALUES(?,?)
     ''', dogs)

    con.commit()

