import pandas as pd
import yaml

with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

raw_path = config["data"]["raw_path"]

df = pd.read_csv(raw_path)

print("Raw data loaded:")
print(df.head())
