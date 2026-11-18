import ast
import os

password = os.environ.get("DEMO_PASSWORD", "")


def run():
    expr = input("Expresion (literal de Python): ")
    try:
        return ast.literal_eval(expr)
    except (ValueError, SyntaxError):
        print("Entrada invalida: se espera un literal de Python")
        raise SystemExit(1)


def get_user(conn, name):
    return conn.execute("SELECT * FROM users WHERE name = ?", (name,))


if __name__ == "__main__":
    print(run())
