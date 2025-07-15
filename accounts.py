import sqlite3
import os

# Resolve path to shared bank.db at project root
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "bank.db")


class Account:
    def __init__(self, name):
        self.name = name

    def create_account(self):
        print("accounts.py DB path:", db_path)  # Debug check

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO accounts(name, balance) VALUES (?, ?)",
            (self.name, 0.0)
        )

        conn.commit()
        conn.close()
        print(f"✅ Account '{self.name}' created with balance 0.0")

    @staticmethod
    def get_balance(account_id):
        print("accounts.py DB path (get_balance):", db_path)  # Debug check

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT balance FROM accounts WHERE id = ?",
            (account_id,)
        )
        result = cursor.fetchone()

        conn.close()
        return result[0] if result else None
