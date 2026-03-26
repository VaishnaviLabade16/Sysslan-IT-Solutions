# Level 5: Advanced Analysis and Visualization
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

# 🔹 Task 5.1: Pivot Table (station-wise train count)
pivot = pd.pivot_table(
    df,
    index="Station_Name",
    values="Train_No",
    aggfunc="count"
)

print("\nPivot Table:\n", pivot)

# 🔹 Task 5.2: Cross Tab (station vs train)
cross = pd.crosstab(df["Station_Name"], df["Train_No"])

print("\nCross Tab:\n", cross)

# 🔹 Task 5.3: Visualization (Top 10 stations from pivot)

top_pivot = pivot.sort_values(by="Train_No", ascending=False).head(10)

top_pivot.plot(kind="bar")
plt.title("Top 10 Stations (Pivot Analysis)")
plt.xlabel("Station Name")
plt.ylabel("Train Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
