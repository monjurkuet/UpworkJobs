import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Check if the table "PostedJobs" already exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='PostedJobs'")
table_exists = cursor.fetchone()

if not table_exists:
    # The table does not exist, so create it
    cursor.execute('''
    CREATE TABLE "PostedJobs" (
        "title" TEXT,
        "createdOn" TEXT,
        "amount" NUMERIC,
        "skillList" TEXT,
        "description" TEXT,
        "hourlyBudget" TEXT,
        "duration" TEXT,
        "engagement" TEXT,
        "enterpriseJob" INTEGER,
        "category" TEXT,
        "ciphertext" TEXT UNIQUE
    )''')
    # Commit the changes
    conn.commit()

# Close the connection
conn.close()
