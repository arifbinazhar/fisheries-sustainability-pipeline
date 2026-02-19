"""
Sustainability Indicator Module

Computes fisheries sustainability indicators including:
- Catch Trend Index
- Catch Variability
- Stability Index
- Consumption Pressure Ratio

Author: Arif Bin Azhar
"""

import pandas as pd
import yaml
import os

# -----------------------------------
# Load configuration
# -----------------------------------
with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

harmonized_path = config["data"]["harmonized_path"]
metrics_path = config["data"]["metrics_path"]

os.makedirs(os.path.dirname(metrics_path), exist_ok=True)

# -----------------------------------
# Load harmonized dataset
# -----------------------------------
df = pd.read_csv(harmonized_path)

# -----------------------------------
# Group by location
# -----------------------------------
grouped = df.groupby("location")

metrics = grouped["catch"].agg([
    "mean",
    "std",
    "min",
    "max"
]).reset_index()

metrics.rename(columns={
    "mean": "avg_catch",
    "std": "catch_variability",
    "min": "min_catch",
    "max": "max_catch"
}, inplace=True)

# -----------------------------------
# Stability Index
# Higher = more stable fishery
# -----------------------------------
metrics["stability_index"] = (
    metrics["avg_catch"] /
    metrics["catch_variability"]
)

# -----------------------------------
# Catch Trend Index
# Compare latest vs earliest year
# -----------------------------------
trend_list = []

for loc, group in df.groupby("location"):
    group = group.sort_values("year")

    first = group.iloc[0]["catch"]
    last = group.iloc[-1]["catch"]

    # We try going through average so as we can understand more clearly the growth 
    first = group.head(3)["catch"].mean()
    last = group.tail(3)["catch"].mean()


    if first > 0:
        trend = last / first
    else:
        trend = None

    trend_list.append({
        "location": loc,
        "catch_trend_index": trend
    })

trend_df = pd.DataFrame(trend_list)

metrics = metrics.merge(trend_df, on="location")

# -----------------------------------
# Consumption Pressure Ratio
# -----------------------------------
pressure = df.groupby("location").agg({
    "direct_consumption": "mean",
    "fishmeal_and_fish_oil": "mean"
}).reset_index()

pressure["consumption_pressure"] = (
    pressure["direct_consumption"] /
    (pressure["fishmeal_and_fish_oil"] + 1)
)

metrics = metrics.merge(
    pressure[["location", "consumption_pressure"]],
    on="location"
)

# -----------------------------------
# Save Results
# -----------------------------------
metrics.to_csv(metrics_path, index=False)

print("✅ Sustainability metrics generated.")
print(metrics.head())
