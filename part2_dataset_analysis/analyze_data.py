# analyze_data.py
# simple script to run some basic stats and save 2 plots.
# no def functions, just simple steps.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load our generated dataset
df = pd.read_csv('dataset.csv')

# print some basic info about the dataset
print("Total records:", len(df))
print("\nAverage scores by Platform:")
print(df.groupby('Platform')['Performance Score'].mean().round(2))

print("\nAverage scores by Industry:")
print(df.groupby('Industry')['Performance Score'].mean().round(2))

# save plot 1: Platform vs Performance
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='Platform', y='Performance Score', errorbar=None)
plt.title('Average Score by Platform')
plt.tight_layout()
plt.savefig('platform_performance.png')
plt.close()
print("\nSaved platform_performance.png")

# save plot 2: Industry vs Performance
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='Industry', y='Performance Score', errorbar=None)
plt.title('Average Score by Industry')
plt.tight_layout()
plt.savefig('industry_performance.png')
plt.close()
print("Saved industry_performance.png")

# check correlations with score
print("\nCorrelation with Performance Score:")
numeric_df = df.select_dtypes(include=['number'])
print(numeric_df.corr()['Performance Score'].round(3))
