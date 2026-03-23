# Level 2: Simple Data Processing

import pandas as pd
df = pd.read_csv("Dataset1.csv")

# Task 2.1: Standardize schedule fields (arrival & departure times)
df["Arrival_time"] = pd.to_datetime(df["Arrival_time"], errors='coerce')
df["Departure_Time"] = pd.to_datetime(df["Departure_Time"], errors='coerce')

# Task 2.2: Compute total journey duration for each train
journey = df.groupby("Train_No").agg({
    "Arrival_time": "min",
    "Departure_Time": "max"
})

journey["Duration"] = journey["Departure_Time"] - journey["Arrival_time"]

print("\nJourney Duration:\n", journey)

# Task 2.3:  Classify routes as short, medium, or long
def classify(d):
    if pd.isnull(d):
        return "Unknown"
    
    hours = d.total_seconds() / 3600
    
    if hours < 5:
        return "Short"
    elif hours < 12:
        return "Medium"
    else:
        return "Long"

journey["Route_Type"] = journey["Duration"].apply(classify)

print("\nRoute Type:\n", journey)

# Task 2.4: Generate station-wise train frequency counts
freq = df["Station_Name"].value_counts()

print("\nStation Frequency:\n", freq)