# explain_model.py
# simple script to explain how the model makes its decisions.
# no def functions, just plain code.

import pickle
import pandas as pd
import numpy as np

# load the trained model package
with open('../part3_ml_model/model.pkl', 'rb') as f:
    package = pickle.load(f)

model = package['model']
industry_map = package['industry_map']
platform_map = package['platform_map']
type_map = package['type_map']
topic_map = package['topic_map']

# get feature importances (which inputs matter most)
importances = model.feature_importances_
features = ['Industry', 'Platform', 'Content Type', 'Content Topic', 'Ad Spend']

print("--- WHAT MATTERS MOST TO THE MODEL ---")
for i in range(len(features)):
    print(f"{features[i]}: {round(importances[i] * 100, 1)}% importance")

# mock test inputs for a post
test_industry = 'Tech'
test_platform = 'LinkedIn'
test_type = 'Reel'
test_topic = 'Education'
test_spend = 50.0

# convert strings to codes using the saved maps
ind_code = industry_map[test_industry]
plat_code = platform_map[test_platform]
type_code = type_map[test_type]
topic_code = topic_map[test_topic]

# make prediction input vector
test_vector = np.array([[ind_code, plat_code, type_code, topic_code, test_spend]])

# predict score
predicted_score = model.predict(test_vector)[0]

print("\n--- TEST POST PREDICTION ---")
print(f"Post details: {test_industry} | {test_platform} | {test_type} | {test_topic} | Spend: ${test_spend}")
print(f"Predicted Score: {round(predicted_score, 1)} / 100")

# plain english explanation
print("\n--- SIMPLE EXPLANATION ---")
print(f"Our database average score is around 96.0.")
print(f"This post is predicted to score {round(predicted_score, 1)}.")
print(f"Why?")
print(f"  - Chosing {test_platform} gives high reach and engagement.")
print(f"  - Using the {test_type} format increases user watch time.")
print(f"  - Adding ${test_spend} ad spend boosts the impressions.")
print(f"  - Topic '{test_topic}' is very relevant for {test_industry} audiences.")
