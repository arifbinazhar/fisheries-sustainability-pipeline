import pandas as pd
import yaml

with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

harmonized_path = config["data"]["harmonized_path"]
metrics_path = config["data"]["metrics_path"]

df = pd.read_csv(harmonized_path)

metrics = df.groupby("species")["catch"].agg(["mean", "std"])

metrics["stability_index"] = metrics["mean"] / metrics["std"]

metrics.to_csv(metrics_path)

print("Sustainability metrics saved.")
