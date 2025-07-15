import sqlite3
import os


def initialize_db():
    # Always locate the path dynamically
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sql_path = os.path.join(base_dir, "setup_sql.txt")
    db_path = os.path.join(base_dir, "..", "bank.db")  # Go up one level to root

    # Read SQL file
    with open(sql_path, "r") as f:
        sql = f.read()
        print("SQL Loaded:", sql)

    # Connect and initialize the DB
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executescript(sql)
    conn.commit()

    # Debug check
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("Tables in DB:", cursor.fetchall())

    conn.close()
    print("Database initialized!")


if __name__ == "__main__":
    initialize_db()
