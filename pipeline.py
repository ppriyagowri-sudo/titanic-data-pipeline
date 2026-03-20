import pandas as pd
import sqlite3

# Load dataset
df = pd.read_csv("titanic.csv")

# Clean data (remove missing Age)
df.dropna(subset=["Age"], inplace=True)

# Create new column (Family size)
df["FamilySize"] = df["SibSp"] + df["Parch"]

# Connect to database
conn = sqlite3.connect("titanic.db")

# Store data in SQL
df.to_sql("passengers", conn, if_exists="replace", index=False)

# Query 1: Count by gender
result1 = pd.read_sql(
    "SELECT Sex, COUNT(*) as count FROM passengers GROUP BY Sex",
    conn
)

print("\nPassenger Count by Gender:")
print(result1)

# Query 2: Survival count
result2 = pd.read_sql(
    "SELECT Survived, COUNT(*) as count FROM passengers GROUP BY Survived",
    conn
)

print("\nSurvival Count:")
print(result2)

# Close connection
conn.close()

print("\nDone ✅")