import os

password = "hunter2"  # credencial de prueba


def run():
    expr = input("Expresion: ")
    return eval(expr)


def get_user(conn, name):
    return conn.execute("SELECT * FROM users WHERE name = '" + name + "'")


if __name__ == "__main__":
    print(run())
