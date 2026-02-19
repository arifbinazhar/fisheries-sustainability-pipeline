import pandas as pd 
df = read_csv("data/raw/fisheries_raw.csv", index=False)

df = df.rename(columns={
    "Entity": "location",
    "Year": "year",
    "Fish catch": "catch",
    "End use": "use_type"
})
