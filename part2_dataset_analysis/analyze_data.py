# analyze_data.py
# This script performs exploratory data analysis (EDA) on the synthetic dataset.
# It prints descriptive statistics and saves 3 plots.
# No functions (def) are used here, just straight sequential code.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset we generated in the previous step
df = pd.read_csv('dataset.csv')

# Step 2: Set styling for our charts
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 10, 'figure.titlesize': 14})

# Step 3: Print basic info about the dataset to see what we have
print("--- DATASET OVERVIEW ---")
print("Total rows:", len(df))
print("\nFirst 3 rows of the data:")
print(df.head(3))
print("\nSummary statistics of numerical columns:")
print(df.describe().round(2))

# Step 4: Perform Group Analysis - Platform Performance
# Let's find which platform gets the highest average Performance Score
platform_groups = df.groupby('Platform')['Performance Score'].mean().sort_values(ascending=False)
print("\n--- PERFORMANCE BY PLATFORM ---")
print(platform_groups.round(2))

# Create a bar plot for Platform Performance and save it
plt.figure(figsize=(8, 5))
sns.barplot(x=platform_groups.index, y=platform_groups.values, palette="Blues_d")
plt.title('Average Performance Score by Platform')
plt.xlabel('Platform')
plt.ylabel('Avg Performance Score (0-100)')
plt.tight_layout()
plt.savefig('platform_performance.png')
plt.close()
print("Saved platform_performance.png")

# Step 5: Perform Group Analysis - Industry Performance
# Let's find which industry performs best on average
industry_groups = df.groupby('Industry')['Performance Score'].mean().sort_values(ascending=False)
print("\n--- PERFORMANCE BY INDUSTRY ---")
print(industry_groups.round(2))

# Create a bar plot for Industry Performance and save it
plt.figure(figsize=(8, 5))
sns.barplot(x=industry_groups.index, y=industry_groups.values, palette="Greens_d")
plt.title('Average Performance Score by Industry')
plt.xlabel('Industry')
plt.ylabel('Avg Performance Score (0-100)')
plt.tight_layout()
plt.savefig('industry_performance.png')
plt.close()
print("Saved industry_performance.png")

# Step 6: Perform Group Analysis - Content Type & Topic
# Let's check which Content Type gets the best results
content_type_groups = df.groupby('Content Type')['Performance Score'].mean().sort_values(ascending=False)
print("\n--- PERFORMANCE BY CONTENT TYPE ---")
print(content_type_groups.round(2))

# Step 7: Correlation Analysis
# We want to see which numeric variables (like Reach, Ad Spend, Clicks) relate to the Performance Score
numeric_cols = ['Reach', 'Impressions', 'Likes', 'Comments', 'Shares', 'Saves', 'Clicks', 'Leads', 'Ad Spend', 'Revenue', 'Performance Score']
correlation_matrix = df[numeric_cols].corr()
print("\n--- CORRELATION WITH PERFORMANCE SCORE ---")
print(correlation_matrix['Performance Score'].sort_values(ascending=False).round(3))

# Create a correlation heatmap and save it
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap of Marketing Metrics')
plt.tight_layout()
plt.savefig('correlation_matrix.png')
plt.close()
print("Saved correlation_matrix.png")

# Step 8: Identify Anomalies (Simple Rule)
# Let's search for posts that had high ad spend but very low performance score (less than 20)
low_performers_high_spend = df[(df['Ad Spend'] > 150) & (df['Performance Score'] < 20)]
print("\n--- ANOMALY CHECK: High Spend, Low Performance ---")
print("Number of high-spend low-performance posts found:", len(low_performers_high_spend))
if len(low_performers_high_spend) > 0:
    print(low_performers_high_spend[['Client', 'Platform', 'Ad Spend', 'Performance Score']].head(5))

print("\nExploratory Data Analysis script finished running successfully!")
