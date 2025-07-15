import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "bank.db")


def transfer_funds(sender_id, receiver_id, amount):
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("BEGIN TRANSACTION")

        # Fetch sender balance
        sender_balance = conn.execute(
            "SELECT balance FROM accounts WHERE id = ?", (sender_id,)
        ).fetchone()
        if not sender_balance:
            raise Exception("Sender account not found.")
        if sender_balance[0] < amount:
            raise Exception("Insufficient funds.")

        # Fetch receiver balance (optional but nice for confirmation)
        receiver_exists = conn.execute(
            "SELECT id FROM accounts WHERE id = ?", (receiver_id,)
        ).fetchone()
        if not receiver_exists:
            raise Exception("Receiver account not found.")

        # Perform balance updates
        conn.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, sender_id)
        )
        conn.execute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, receiver_id)
        )

        conn.commit()
        print(f"✅ Transferred {amount:.2f} from Account {sender_id} to Account {receiver_id}")

    except Exception as e:
        conn.rollback()
        print(f"❌ Transaction failed: {e}")
    finally:
        conn.close()
