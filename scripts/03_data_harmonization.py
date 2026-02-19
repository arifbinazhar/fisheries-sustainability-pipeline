"""
Data Harmonization Module

Standardizes fisheries datasets across spatial and temporal
dimensions to enable sustainability analysis.

Author: Arif Bin Azhar
"""


import pandas as pd
import yaml
import os

# -------------------------------
# Load configuration
# -------------------------------
with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

cleaned_path = config["data"]["raw_path"]
harmonized_path = config["data"]["harmonized_path"]

os.makedirs(os.path.dirname(harmonized_path), exist_ok=True)

# -------------------------------
# Load cleaned dataset
# -------------------------------
df = pd.read_csv(cleaned_path)

# -------------------------------
# Rename required columns
# -------------------------------
df = df.rename(columns={
    "Entity": "location",
    "Year": "year",
    "total_fish_catch": "catch",
    "fish_catch_direct_consumption": "direct_consumption",
    "fishmeal_and_fish_oil": "fishmeal_and_fish_oil",
    "fish_other_uses": "other_usage"
})

# -------------------------------
# Keep ONLY required columns
# -------------------------------
required_columns = [
    "location",
    "year",
    "catch",
    "direct_consumption",
    "fishmeal_and_fish_oil",
    "other_usage"
]

df = df[required_columns]

# -------------------------------
# Harmonization Steps
# -------------------------------

# Standardize location names
df["location"] = df["location"].str.strip().str.title()

# Ensure numeric types
numeric_cols = [
    "catch",
    "direct_consumption",
    "fishmeal_and_fish_oil",
    "other_usage"
]

df[numeric_cols] = df[numeric_cols].apply(
    pd.to_numeric, errors="coerce"
)

# Remove missing critical values
df = df.dropna(subset=["location", "year", "catch"])

# Convert year datatype
df["year"] = df["year"].astype(int)

# Sort dataset
df = df.sort_values(["location", "year"])

# -------------------------------
# Save harmonized dataset
# -------------------------------
df.to_csv(harmonized_path, index=False)

print("✅ Harmonized dataset saved successfully.")
print(df.head())
