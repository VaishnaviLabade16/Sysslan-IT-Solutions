#Level 1:- Basic Data Review

import pandas as pd
df = pd.read_csv("Dataset1.csv")

# Task 1.1: Overview of dataset
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Column Names:", df.columns)

# Task 1.2: List trains with start & end stations
train_routes = df.groupby("Train_No")["Station_Name"].agg(["first", "last"])
print("\nTrain Routes:\n", train_routes)

# Task 1.3: Number of stops per train
stops = df.groupby("Train_No")["Station_Name"].count()
print("\nStops per train:\n", stops)

# Task 1.4:  Max & Min stops
print("\nMax stops train:", stops.idxmax(), stops.max())
print("Min stops train:", stops.idxmin(), stops.min())