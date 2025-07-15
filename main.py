import os
import sqlite3
from models.accounts import Account
from utils.transaction_handler import transfer_funds

# 👉 Set absolute DB path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "bank.db")
print("Running from:", BASE_DIR)


# 🔧 Ensure DB and table exist
def initialize_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            balance REAL DEFAULT 0
        )
    """)
    conn.commit()
    # Show existing tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("Tables in DB:", cursor.fetchall())
    conn.close()


def read_admin_password():
    pass_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts", "admin_pass.txt")
    with open(pass_path, "r") as f:
        return f.read().strip()


def menu():
    while True:
        print("\n📋 Choose an option:")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Transfer Funds")
        print("4. Exit")
        print("5. List All Accounts (ONLY FOR ADMIN)")

        choice = input("➡️ Enter choice (1-5): ")

        if choice == "1":
            name = input("👤 Enter account name: ")
            acc = Account(name)
            acc.create_account()

        elif choice == "2":
            acc_id = int(input("🔍 Enter account ID: "))
            balance = Account.get_balance(acc_id)
            if balance is not None:
                print(f"💰 Balance for account {acc_id}: {balance:.2f}")
            else:
                print("❌ Account not found.")

        elif choice == "3":
            sender = int(input("💸 Sender ID: "))
            receiver = int(input("💸 Receiver ID: "))
            amount = float(input("💰 Amount: "))
            transfer_funds(sender, receiver, amount)

        elif choice == "4":
            print("👋 Exiting. Have a great day!")
            break

        elif choice == "5":
            entered = input("🔐 Enter admin password: ")
            actual = read_admin_password()
            if entered != actual:
                print("❌ Unauthorized access.")
                continue

            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, balance FROM accounts")
            accounts = cursor.fetchall()
            conn.close()

            print("\n📇 All Accounts:")
            for acc in accounts:
                print(f"🆔 ID: {acc[0]}, 👤 Name: {acc[1]}, 💰 Balance: {acc[2]:.2f}")

        else:
            print("⚠️ Invalid choice. Try again.")


menu()
