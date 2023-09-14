import sqlite3
import pandas as pd

conn = sqlite3.connect('database.db')
db_df = pd.read_sql_query("SELECT * FROM PostedJobs", conn)
db_df.to_excel('PostedJobs.xlsx', index=False)
conn.close()