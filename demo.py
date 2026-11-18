import ast
import os

password = os.environ.get("DEMO_PASSWORD", "")


def run():
    expr = input("Expresion: ")
    return ast.literal_eval(expr)


def get_user(conn, name):
    return conn.execute("SELECT * FROM users WHERE name = '" + name + "'")


if __name__ == "__main__":
    print(run())
