# Fisheries Sustainability Data Harmonization Pipeline

## Overview

This project implements a reproducible data science pipeline for compiling, harmonizing, and analyzing fisheries datasets to assess sustainability trends.

## Objectives

- Compile fisheries datasets from open sources
- Harmonize multi-source data
- Perform sustainability analysis
- Identify trends and data gaps
- Generate reproducible workflows

## Pipeline Architecture

Raw Data → Cleaning → Harmonization → Sustainability Analysis → Visualization

## Folder Structure

scripts/ : data processing scripts  
notebooks/ : analysis notebooks  
results/ : figures and tables  
data/ : raw and processed datasets  

## How to Run

pip install -r requirements.txt
python run_pipeline.py


## Data Interpretation From Sustainability Indicators

***Stability Index*** <br>

The stability index quantifies temporal consistency in fisheries production. Regions showing high variability relative to average catch may indicate ecological stress or unstable harvesting patterns, making this a useful proxy for sustainability assessment.

***Catch Trend Index*** <br>

The catch trend index shows how the fish production has changed over time. We used the mean of latest three years as well as earliest three years to calculate this.

***Consumption Pressure*** <br>

The consumption pressure was used as a proxy indicator to understand how fisheries contribute to food systems versus industrial processing, allowing identification of regions where harvesting demand may impose higher sustainability stress.

***Overall Pipeline for Data Interpretation*** <br>

```
Raw Time Series
        ↓
Regional Separation
        ↓
Temporal Ordering
        ↓
Early vs Late Comparison
        ↓
Trend Indicator
        ↓
Integrated Sustainability Metrics
```

## Example Outputs

- Harmonized dataset
- Sustainability indicators
- Trend visualizations

## Plots and Analysis

Below are the plots that we have generated which help to analyse the better and identify the key regions with stress to their fishing outputs.

**The plot below maps fisheries across Catch Trend Index (log scale) and Stability Index, representing growth and temporal consistency, respectively.**

![alt text](https://github.com/arifbinazhar/fisheries-sustainability-pipeline/blob/main/results/figures/sustainability_landscape.png)


Above plot helps to visualise multiple trends including subset of fisheries that shows high growth but lower stability (Peru and Indonesia), suggesting potential sustainability risks linked to rapid expansion and fluctuating harvest levels.


**Based on higher value of stability index we were able to plot top countries which has a stable fish production (United Kingdom being the most stable region). **<br><br>
![alt text](https://github.com/arifbinazhar/fisheries-sustainability-pipeline/blob/main/results/figures/stable_regions.png)

**The graph below shows top 10 fish producing regions with respect to total catch. _Russia_ and _Japan_ turns out to be the largest fish producing regions.**
![alt text](https://github.com/arifbinazhar/fisheries-sustainability-pipeline/blob/main/results/figures/top_regions.png) <br>

__Russia emerges as the largest fisheries producer, contributing the highest cumulative catch among all analyzed regions.__ <br>
__Japan, China, and Peru also demonstrate consistently high production levels, reflecting their long-established and industrialized fisheries sectors.__







## Relevance

This pipeline demonstrates applied data science methods for sustainability analysis, including:

- Data harmonization
- Reproducible workflows
- Exploratory data analysis
- Sustainability indicator computation

## Author

Arif Bin Azhar
MSc Bioinformatics, Savitribai Phule Pune University
