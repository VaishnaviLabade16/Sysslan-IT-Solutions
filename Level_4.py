# Level 4: Basic Analysis and Visualization
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

# Convert time again (important)
df["Arrival_time"] = pd.to_datetime(df["Arrival_time"], errors='coerce')
df["Departure_Time"] = pd.to_datetime(df["Departure_Time"], errors='coerce')

# Task 4.1: Average journey duration
journey = df.groupby("Train_No").agg({
    "Arrival_time": "min",
    "Departure_Time": "max"
})

journey["Duration"] = journey["Departure_Time"] - journey["Arrival_time"]

avg_duration = journey["Duration"].mean()
print("\nAverage Journey Duration:", avg_duration)

# Task 4.2: Top stations (high traffic)
top_stations = df["Station_Name"].value_counts().head(10)

print("\nTop 10 Stations:\n", top_stations)

# Task 4.3: Visualization (Bar Graph)

top_stations.plot(kind="bar")
plt.title("Top 10 High Traffic Stations")
plt.xlabel("Station Name")
plt.ylabel("Number of Trains")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()