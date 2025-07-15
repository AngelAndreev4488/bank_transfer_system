import sqlite3
import os
import random
from faker import Faker

fake = Faker()

# ✅ Path to bank.db
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "bank.db")


def seed_accounts(n=1000):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 🚫 Safeguard: Create status table if needed
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS seeding_status (
            done INTEGER
        )
    """)

    # 🔍 Check if data has already been seeded
    cursor.execute("SELECT done FROM seeding_status")
    result = cursor.fetchone()
    if result and result[0] == 1:
        print("🚫 Seeding already done. Skipping.")
        conn.close()
        return

    # ✅ Proceed with account generation
    for _ in range(n):
        name = fake.name()
        balance = round(random.uniform(100.0, 10000.0), 2)
        cursor.execute("INSERT INTO accounts(name, balance) VALUES (?, ?)", (name, balance))

    # 🛑 Mark seeding as complete
    cursor.execute("INSERT INTO seeding_status(done) VALUES (1)")
    conn.commit()
    conn.close()

    print(f"✅ Inserted {n} accounts into the bank.")


if __name__ == "__main__":
    seed_accounts()
