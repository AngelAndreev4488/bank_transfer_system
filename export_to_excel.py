import sqlite3
import pandas as pd
import os

# 🔍 Locate your database
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "bank.db")

# 📥 Connect and read data
conn = sqlite3.connect(db_path)
query = "SELECT * FROM accounts"
df = pd.read_sql_query(query, conn)
conn.close()

# 📤 Export to Excel
excel_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "bank_accounts.xlsx")
df.to_excel(excel_path, index=False)

print(f"✅ Exported {len(df)} accounts to Excel at: {excel_path}")
