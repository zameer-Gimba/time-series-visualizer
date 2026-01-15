# time-series-visualizer
# Time Series Visualization – freeCodeCamp Forum Page Views

This project analyzes daily page view traffic from the freeCodeCamp forum using time-series visualization techniques.  
The goal is to explore long-term trends, yearly patterns, and seasonal behavior through clear and interpretable plots.

The repository is structured to separate data handling, visualization logic, and results, making it easy to extend or reuse in future analysis.



## Dataset

The dataset contains daily page view counts for the freeCodeCamp forum between **May 2016 and December 2019**.

- Source: freeCodeCamp (via UCI / open data projects)
- File: `fcc-forum-pageviews.csv`
- Columns:
  - `date` — date of observation
  - `value` — number of page views



## Data Cleaning

Before visualization, the data is cleaned by:
- Parsing the `date` column as a datetime index
- Removing extreme outliers by excluding the top and bottom 2.5% of page view values

This ensures the plots reflect meaningful patterns rather than noise.



## Visualizations

The following plots are generated from the cleaned dataset:

### 1. Line Plot – Daily Page Views
Shows the overall trend in daily forum activity over time.

### 2. Bar Plot – Average Monthly Page Views
Displays average page views per month, grouped by year, highlighting yearly and monthly patterns.

### 3. Box Plots – Trend and Seasonality
- **Year-wise box plot**: illustrates long-term trends
- **Month-wise box plot**: highlights seasonal variation across months




## Usage


1. Install dependencies:
```bash
pip install -r requirements.txt

2. Run the test script to generate all visualizations:
python tests/test_visualizer.py


