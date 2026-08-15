# explain_model.py
# This script explains how our Random Forest model makes predictions.
# We look at "Feature Importance" to understand which factors matter most.
# No functions (def) are used in this script. Everything is flat and top-down.

import pickle
import pandas as pd
import numpy as np

# Step 1: Load the trained model package we saved in Part 3
with open('../part3_ml_model/rf_model.pkl', 'rb') as f:
    model_package = pickle.load(f)

# Extract the model and mappings
rf_model = model_package['model']
industry_map = model_package['industry_map']
platform_map = model_package['platform_map']
type_map = model_package['type_map']
topic_map = model_package['topic_map']
day_map = model_package['day_map']
time_map = model_package['time_map']

# Step 2: Get Feature Importances from the Random Forest model
# Feature importance tells us how much each feature contributed to reducing error
importances = rf_model.feature_importances_
feature_names = ['Industry', 'Platform', 'Content Type', 'Content Topic', 'Posting Day', 'Posting Time', 'Ad Spend']

# Combine into a DataFrame to display nicely
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance (%)': (importances * 100).round(2)
}).sort_values(by='Importance (%)', ascending=False)

print("--- GLOBAL FEATURE IMPORTANCES ---")
print("These are the factors the model cares about most across all data:")
print(importance_df.to_string(index=False))

# Step 3: Explain a single prediction to a non-technical employee
# Let's say a marketing manager wants to test a specific post:
input_industry = 'Tech'
input_platform = 'LinkedIn'
input_content_type = 'Reel'
input_topic = 'Product Education'
input_day = 'Monday'
input_time = '6 PM'
input_spend = 100.0

# Map the inputs to numeric codes
industry_code = industry_map[input_industry]
platform_code = platform_map[input_platform]
type_code = type_map[input_content_type]
topic_code = topic_map[input_topic]
day_code = day_map[input_day]
time_code = time_map[input_time]

# Put features into the format expected by the model
feature_vector = np.array([[industry_code, platform_code, type_code, topic_code, day_code, time_code, input_spend]])

# Make prediction
predicted_score = rf_model.predict(feature_vector)[0]

print("\n--- INDIVIDUAL PREDICTION EXPLANATION ---")
print(f"Inputs:")
print(f"  - Industry: {input_industry}")
print(f"  - Platform: {input_platform}")
print(f"  - Content Type: {input_content_type}")
print(f"  - Content Topic: {input_topic}")
print(f"  - Posting Day: {input_day}")
print(f"  - Posting Time: {input_time}")
print(f"  - Ad Spend: ${input_spend}")
print(f"\nPredicted Performance Score: {round(predicted_score, 2)} / 100")

# Let's explain why this score happened in plain English
print("\nPlain English Explanation for Marketing Manager:")
print(f"1. The average post score in our company database is 28.9.")
print(f"2. Your predicted score is {round(predicted_score, 2)}, which is HIGHER than average.")
print(f"3. Why is it higher?")
print(f"   - **Platform Impact**: You chose LinkedIn, which is our top-performing platform on average.")
print(f"   - **Format Impact**: You chose a Reel (Video format), which has high user engagement.")
print(f"   - **Ad Spend**: You are spending ${input_spend}, which boosts visibility and leads.")
print(f"   - **Topic Impact**: 'Product Education' is a very strong topic in the Tech industry.")
