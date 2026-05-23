from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["healthcare_survey"]
collection = db["participants"]

# Fetch data
data = list(collection.find())

print("Records found:", len(data))  # ✅ DEBUG

clean_data = []

for item in data:
    clean_data.append({
        "Age": item.get("age"),
        "Gender": item.get("gender"),
        "Income": item.get("income"),
        "Utilities": item.get("expenses", {}).get("utilities", 0),
        "Entertainment": item.get("expenses", {}).get("entertainment", 0),
        "School Fees": item.get("expenses", {}).get("school_fees", 0),
        "Shopping": item.get("expenses", {}).get("shopping", 0),
        "Healthcare": item.get("expenses", {}).get("healthcare", 0)
    })

# Create DataFrame
df = pd.DataFrame(clean_data)

print(df)  # ✅ DEBUG

# Save CSV
df.to_csv("survey_data.csv", index=False)

print("✅ CSV Exported Successfully")