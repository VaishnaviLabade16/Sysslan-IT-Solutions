import pandas as pd

# load dataset
df = pd.read_csv("Dataset1.csv")

# show first 5 rows
print(df.head())

# show column names
print(df.columns)