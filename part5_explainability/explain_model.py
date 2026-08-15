# explain_model.py
# simple script to explain the model predictions.
# written like a basic college assignment.

import pickle

# load the raw model from pickle
model = pickle.load(open('../part3_ml_model/model.pkl', 'rb'))

# mapping dicts
ind_map = {'Tech': 0, 'Fashion': 1, 'Finance': 2, 'Food': 3, 'Health': 4}
plat_map = {'Instagram': 0, 'Facebook': 1, 'LinkedIn': 2, 'YouTube': 3, 'TikTok': 4}
type_map = {'Reel': 0, 'Carousel': 1, 'Image': 2, 'Text': 3, 'Video': 4}
topic_map = {'Education': 0, 'News': 1, 'BehindScenes': 2, 'Tutorial': 3, 'Promo': 4}

# print feature importance values
features = ['Industry', 'Platform', 'Content Type', 'Content Topic', 'Ad Spend']
importances = model.feature_importances_

print("--- Feature Importances ---")
for i in range(len(features)):
    importance_percent = round(importances[i] * 100, 2)
    print(f"{features[i]}: {importance_percent}%")

# test prediction for a single post
test_industry = 'Tech'
test_platform = 'LinkedIn'
test_type = 'Reel'
test_topic = 'Education'
test_spend = 50.0

# convert strings to codes using the maps
ind_val = ind_map[test_industry]
plat_val = plat_map[test_platform]
type_val = type_map[test_type]
topic_val = topic_map[test_topic]

# make prediction
test_row = [[ind_val, plat_val, type_val, topic_val, test_spend]]
prediction = model.predict(test_row)[0]

print("\n--- Test Post prediction ---")
print("Input details: Tech, LinkedIn, Reel, Education, $50 Spend")
print(f"Predicted Score: {round(prediction, 2)} / 100")
