import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd



df = pd.read_csv("data/processed/harmonized_data.csv")
metrics = pd.read_csv("data/processed/sustainability_metrics.csv")

sns.set(style="whitegrid")


top10 = (
    metrics.sort_values("avg_catch", ascending=False)
    .head(10)["location"]
)

metrics["location_group"] = metrics["location"].apply(
    lambda x: x if x in list(top10) else "Other"
)

top_catch = (
    metrics.sort_values("catch_trend_index", ascending=False)
    .head(10)["location"]
)

plt.figure(figsize=(10,7))

sns.scatterplot(
    data=metrics,
    x="catch_trend_index",
    y="stability_index",
    hue="location_group",
    palette="Paired",    
    s=80
)

plt.title("Fishery Sustainability Landscape", fontsize=14)
plt.xlabel("Catch Trend Index")
plt.ylabel("Stability Index")
plt.savefig("results/figures/sustainablity_landscape.png")
plt.show()

metrics = pd.read_csv("data/processed/sustainability_metrics.csv")

#--------------------------------------
trend = df.groupby("year")["catch"].sum()

plt.figure(figsize=(10,6))
plt.plot(trend.index, trend.values)

plt.title("Global Fisheries Catch Trend Over Time")
plt.xlabel("Year")
plt.ylabel("Total Fish Catch (Tonnes)")
plt.tight_layout()

plt.savefig("results/figures/global_catch_trend.png")
plt.show()

#-----------------------------------------------

x = df[df["location"].str.lower() != "world"]
top_regions = (
    x.groupby("location")["catch"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))
top_regions.plot(kind="bar")

plt.title("Top 10 Fisheries Producing Regions")
plt.xlabel("Region")
plt.ylabel("Total Catch (Tonnes)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("results/figures/top_regions.png")
plt.show()

#------------------------------------------------

plt.figure(figsize=(8,6))

sns.histplot(
    metrics["catch_variability"],
    bins=30,
    kde=True
)

plt.title("Distribution of Catch Variability Across Regions")
plt.xlabel("Catch Variability")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("results/figures/catch_variability_distribution.png")
plt.show()

#---------------------------------------------------
plt.figure(figsize=(9,7))

sns.scatterplot(
    data=metrics,
    x="catch_trend_index",
    y="stability_index"
)

plt.axvline(1, linestyle="--")
plt.axhline(metrics["stability_index"].median(), linestyle="--")

plt.title("Fisheries Sustainability Landscape")
plt.xlabel("Catch Trend Index (Growth vs Decline)")
plt.ylabel("Stability Index")

plt.tight_layout()
plt.savefig("results/figures/sustainability_landscape.png")
plt.show()

plt.figure(figsize=(10,6))

sns.boxplot(
    y=metrics["consumption_pressure"]
)

plt.title("Distribution of Consumption Pressure")
plt.ylabel("Consumption Pressure Ratio")

plt.tight_layout()
plt.savefig("results/figures/consumption_pressure.png")
plt.show()

#-----------------------------------------------------
stable = metrics.sort_values(
    "stability_index",
    ascending=False
).head(15)

plt.figure(figsize=(10,7))

sns.barplot(
    data=stable,
    x="stability_index",
    y="location"
)

plt.title("Most Stable Fisheries Regions")
plt.xlabel("Stability Index")
plt.ylabel("Region")

plt.tight_layout()
plt.savefig("results/figures/stable_regions.png")
plt.show()


#---------------------unstable 
stable = metrics.sort_values(
    "stability_index",
    ascending=False
).tail(15)

plt.figure(figsize=(10,7))

sns.barplot(
    data=stable,
    x="stability_index",
    y="location"
)

plt.title("Most Unstable Fisheries Regions")
plt.xlabel("Stability Index")
plt.ylabel("Region")

plt.tight_layout()
plt.savefig("results/figures/unstable_regions.png")
plt.show()

#------------------------------------------------
plt.figure(figsize=(8,6))

sns.heatmap(
    metrics.drop(columns=["location"]).corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Between Sustainability Indicators")

plt.tight_layout()
plt.savefig("results/figures/indicator_correlation.png")
plt.show()


#----------------------------------------------------

