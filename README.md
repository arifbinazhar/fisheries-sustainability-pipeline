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

***Stability Index***

The stability index quantifies temporal consistency in fisheries production. Regions showing high variability relative to average catch may indicate ecological stress or unstable harvesting patterns, making this a useful proxy for sustainability assessment.

***Catch Trend Index***
The catch trend index shows how the fish production has changed over time. We used the mean of latest three years as well as earliest three years to calculate this.

***Consumption Pressure***

The consumption pressure was used as a proxy indicator to understand how fisheries contribute to food systems versus industrial processing, allowing identification of regions where harvesting demand may impose higher sustainability stress.

***Overall Pipeline for Data Interpretation***

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

## Relevance

This pipeline demonstrates applied data science methods for sustainability analysis, including:

- Data harmonization
- Reproducible workflows
- Exploratory data analysis
- Sustainability indicator computation

## Author

Arif Bin Azhar
MSc Bioinformatics, Savitribai Phule Pune University
