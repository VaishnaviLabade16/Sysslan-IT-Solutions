# Level 6: Final Capstone System
import pandas as pd
df = pd.read_csv("cleaned_data.csv")

# Convert time
df["Arrival_time"] = pd.to_datetime(df["Arrival_time"], errors='coerce')
df["Departure_Time"] = pd.to_datetime(df["Departure_Time"], errors='coerce')

source = input("Enter Source Station Code: ")
destination = input("Enter Destination Station Code: ")

found = False

for train in df["Train_No"].unique():
    train_data = df[df["Train_No"] == train]
    
    # reset index for safe access
    train_data = train_data.reset_index(drop=True)
    
    stations = train_data["Station_Code"].tolist()
    
    if source in stations and destination in stations:
        if stations.index(source) < stations.index(destination):
            
            source_row = train_data[train_data["Station_Code"] == source].iloc[0]
            dest_row = train_data[train_data["Station_Code"] == destination].iloc[0]
            
            duration = dest_row["Arrival_time"] - source_row["Departure_Time"]
            
            print("\nTrain No:", train)
            print("Estimated Duration:", duration)
            
            found = True

if not found:
    print("\nNo direct trains found.")