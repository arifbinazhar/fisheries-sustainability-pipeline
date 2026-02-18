import pandas as pd
import yaml

with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

cleaned_path = config["data"]["cleaned_path"]
harmonized_path = config["data"]["harmonized_path"]

df = pd.read_csv(cleaned_path)

df["location"] = df["location"].str.title()

df["species"] = df["species"].str.lower()

df.to_csv(harmonized_path, index=False)

print("Harmonized data saved.")
