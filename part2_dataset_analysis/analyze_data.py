# analyze_data.py
# simple data analysis script using pandas and matplotlib.
# made for college lab submission.

import pandas as pd
import matplotlib.pyplot as plt

# load data from csv file
df = pd.read_csv('dataset.csv')

# print shape and first 5 rows
print("Rows and Columns:", df.shape)
print("\nFirst few rows:")
print(df.head())

# print descriptive stats of numerical columns
print("\nDataset Summary Stats:")
print(df.describe())

# calculate mean score by platform and print it
platform_scores = df.groupby('Platform')['Performance Score'].mean()
print("\nMean Scores by Platform:")
print(platform_scores)

# make and save a simple bar chart of platform scores
plt.figure()
platform_scores.plot(kind='bar', color='blue')
plt.title('Avg Score by Platform')
plt.ylabel('Score')
plt.tight_layout()
plt.savefig('platform_performance.png')
plt.close()
print("\nSaved platform_performance.png")

# calculate mean score by industry and print it
industry_scores = df.groupby('Industry')['Performance Score'].mean()
print("\nMean Scores by Industry:")
print(industry_scores)

# make and save a simple bar chart of industry scores
plt.figure()
industry_scores.plot(kind='bar', color='green')
plt.title('Avg Score by Industry')
plt.ylabel('Score')
plt.tight_layout()
plt.savefig('industry_performance.png')
plt.close()
print("Saved industry_performance.png")

# print correlation of columns
print("\nCorrelation matrix of columns:")
print(df.corr(numeric_only=True))
