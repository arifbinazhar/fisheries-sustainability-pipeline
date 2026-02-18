import pandas as pd
import yaml

with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

raw_path = config["data"]["raw_path"]
cleaned_path = config["data"]["cleaned_path"]

df = pd.read_csv(raw_path)

df.columns = df.columns.str.lower().str.strip()

df = df.drop_duplicates()

df = df.dropna()

df.to_csv(cleaned_path, index=False)

print("Cleaned data saved.")
