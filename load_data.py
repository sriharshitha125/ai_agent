# load_data.py
import pandas as pd
import sqlite3

# Connect to SQLite database (will create ecommerce.db if it doesn't exist)
conn = sqlite3.connect("ecommerce.db")

# Read each CSV and write it as a table in the database
print("📥 Loading ad_sales.csv...")
pd.read_csv("ad_sales.csv").to_sql("ad_sales", conn, if_exists="replace", index=False)

print("📥 Loading total_sales.csv...")
pd.read_csv("total_sales.csv").to_sql("total_sales", conn, if_exists="replace", index=False)

print("📥 Loading eligibility.csv...")
pd.read_csv("eligibility.csv").to_sql("eligibility", conn, if_exists="replace", index=False)

conn.close()
print("✅ All tables successfully written to ecommerce.db")
