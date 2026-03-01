import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# -----------------------------------
# Load data
# -----------------------------------
df = pd.read_csv("data/processed/harmonized_data.csv")
metrics = pd.read_csv("data/processed/sustainability_metrics.csv")

sns.set(style="whitegrid")

# -----------------------------------
# Remove aggregated entries
# -----------------------------------
metrics = metrics[
    metrics["location"].str.lower() != "world"
]

# -----------------------------------
# Select Top 10 locations by average catch
# -----------------------------------
top10 = (
    metrics.sort_values("avg_catch", ascending=False)
    .head(10)["location"]
    .tolist()
)

# -----------------------------------
# Create grouped coloring variable
# -----------------------------------
metrics["location_group"] = metrics["location"].apply(
    lambda x: x if x in top10 else "Other"
)

# -----------------------------------
# Create figure
# -----------------------------------
plt.figure(figsize=(10, 7))

sns.scatterplot(
    data=metrics,
    x="catch_trend_index",
    y="stability_index",
    hue="location_group",
    palette="tab10",
    s=90,
    edgecolor="black"
)

# 🔹 Log scale to reduce extreme distortion
plt.xscale("log")

# -----------------------------------
# Reference lines
# -----------------------------------
plt.axvline(1, linestyle="--", color="gray", alpha=0.6)
plt.axhline(
    metrics["stability_index"].median(),
    linestyle="--",
    color="gray",
    alpha=0.6
)

# -----------------------------------
# Labels
# -----------------------------------
plt.title("Fishery Sustainability Landscape", fontsize=14)
plt.xlabel("Catch Trend Index (log scale)")
plt.ylabel("Stability Index")

plt.legend(
    title="Top Fisheries Regions",
    bbox_to_anchor=(1.05, 1),
    loc="upper left"
)

plt.tight_layout()

# -----------------------------------
# Save
# -----------------------------------
plt.savefig(
    "results/figures/sustainability_landscape.png",
    dpi=300
)

plt.show()