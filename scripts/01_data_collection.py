import pandas as pd
import os

url = "https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Global%20fish%20catch%20by%20end%20use%20(FishStat%20via%20SeaAroundUs)/Global%20fish%20catch%20by%20end%20use%20(FishStat%20via%20SeaAroundUs).csv"

df = pd.read_csv(url)

os.makedirs("data/raw", exist_ok=True)

df.to_csv("data/raw/fisheries_raw.csv", index=False)

print("Dataset downloaded successfully.")
print(df.head())
print(df.shape)
print(df.columns)
print(df.head())
