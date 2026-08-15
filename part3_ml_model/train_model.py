# train_model.py
# This script trains a machine learning model to predict the content performance score.
# We compare two models: a simple Decision Tree and a Random Forest.
# There are no functions (def) in this script. Everything runs top-down.

import pandas as pd
import numpy as np
import shutil
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Step 1: Copy dataset.csv from the analysis folder to this folder
# This makes this folder a self-contained "repo"
shutil.copy('../part2_dataset_analysis/dataset.csv', 'dataset.csv')
print("Copied dataset.csv locally.")

# Step 2: Load the copied dataset
df = pd.read_csv('dataset.csv')

# Step 3: Define simple mappings for categorical columns
# We do not use complex encoders, just simple dictionaries so anyone can understand the mapping
industry_map = {'Tech': 0, 'Fashion': 1, 'Finance': 2, 'Food & Beverage': 3, 'Healthcare': 4}
platform_map = {'Instagram': 0, 'Facebook': 1, 'LinkedIn': 2, 'YouTube': 3, 'TikTok': 4}
type_map = {'Reel': 0, 'Carousel': 1, 'Image': 2, 'Text': 3, 'Video': 4}
topic_map = {'Product Education': 0, 'Industry News': 1, 'Behind the Scenes': 2, 'Tutorial': 3, 'Promo/Offer': 4}
day_map = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
time_map = {'9 AM': 0, '12 PM': 1, '3 PM': 2, '6 PM': 3, '9 PM': 4, '12 AM': 5}

# Step 4: Apply the mappings to create numeric columns for the model
df['Industry_code'] = df['Industry'].map(industry_map)
df['Platform_code'] = df['Platform'].map(platform_map)
df['ContentType_code'] = df['Content Type'].map(type_map)
df['Topic_code'] = df['Content Topic'].map(topic_map)
df['Day_code'] = df['Posting Day'].map(day_map)
df['Time_code'] = df['Posting Time'].map(time_map)

# Step 5: Define features (inputs) and target (output)
# We want to predict "Performance Score" using category codes and the ad spend
feature_cols = ['Industry_code', 'Platform_code', 'ContentType_code', 'Topic_code', 'Day_code', 'Time_code', 'Ad Spend']
X = df[feature_cols]
y = df['Performance Score']

# Step 6: Split data into Training set (80%) and Test set (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Data split completed: 80% train, 20% test.")

# Step 7: Train Model 1 (Simple Decision Tree Regressor)
# Decision Trees are simple and easy to understand because they use tree-like splits
dt_model = DecisionTreeRegressor(max_depth=5, random_state=42)
dt_model.fit(X_train, y_train)

# Evaluate Model 1
y_pred_dt = dt_model.predict(X_test)
mae_dt = mean_absolute_error(y_test, y_pred_dt)
r2_dt = r2_score(y_test, y_pred_dt)
print("\n--- MODEL 1: DECISION TREE RESULTS ---")
print("Mean Absolute Error (MAE):", round(mae_dt, 3))
print("R-squared (R2 Score):", round(r2_dt, 3))

# Step 8: Train Model 2 (Random Forest Regressor)
# Random Forest is a collection of many decision trees, which usually makes it more accurate
rf_model = RandomForestRegressor(n_estimators=100, max_depth=6, random_state=42)
rf_model.fit(X_train, y_train)

# Evaluate Model 2
y_pred_rf = rf_model.predict(X_test)
mae_rf = mean_absolute_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)
print("\n--- MODEL 2: RANDOM FOREST RESULTS ---")
print("Mean Absolute Error (MAE):", round(mae_rf, 3))
print("R-squared (R2 Score):", round(r2_rf, 3))

# Step 9: Establish Baseline Performance
# A simple baseline is to always predict the average Performance Score of the training data
baseline_preds = np.full(shape=y_test.shape, fill_value=y_train.mean())
mae_baseline = mean_absolute_error(y_test, baseline_preds)
r2_baseline = r2_score(y_test, baseline_preds)
print("\n--- BASELINE RESULTS (Always predict average) ---")
print("Mean Absolute Error (MAE):", round(mae_baseline, 3))
print("R-squared (R2 Score):", round(r2_baseline, 3))

# Step 10: Save the best model (Random Forest) and our mapping files
# We pack the model and the mapping dictionaries together in a single dict so they are easy to load later
best_model_package = {
    'model': rf_model,
    'industry_map': industry_map,
    'platform_map': platform_map,
    'type_map': type_map,
    'topic_map': topic_map,
    'day_map': day_map,
    'time_map': time_map
}

# Open a file in write-binary mode and save
with open('rf_model.pkl', 'wb') as f:
    pickle.dump(best_model_package, f)
print("\nBest model (Random Forest) and mappings saved to rf_model.pkl")
