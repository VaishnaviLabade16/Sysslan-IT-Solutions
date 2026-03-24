# Level 3: Data Quality Checks

import pandas as pd
df = pd.read_csv("Dataset1.csv")

# Convert time (IMPORTANT before sorting)
df["Arrival_time"] = pd.to_datetime(df["Arrival_time"], errors='coerce')
df["Departure_Time"] = pd.to_datetime(df["Departure_Time"], errors='coerce')

# Task 3.1: Handle missing values
print("Missing values before:\n", df.isnull().sum())

df = df.dropna()

print("\nMissing values after:\n", df.isnull().sum())

# Task 3.2: Remove duplicates
print("\nDuplicates before:", df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicates after:", df.duplicated().sum())

# Task 3.3: Sort data (correct station order)
df = df.sort_values(by=["Train_No", "Arrival_time"])

# Task 3.4: Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\n Cleaned data saved as cleaned_data.csv")