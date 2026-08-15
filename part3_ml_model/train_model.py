# train_model.py
# simple script to train a decision tree model to predict post score.
# no def functions, just simple steps.

import pandas as pd
import numpy as np
import shutil
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

# copy the dataset csv here to keep it independent
shutil.copy('../part2_dataset_analysis/dataset.csv', 'dataset.csv')
print("Copied dataset.csv")

# load the dataset
df = pd.read_csv('dataset.csv')

# mapping categories to simple numbers so the math model can use them
industry_map = {'Tech': 0, 'Fashion': 1, 'Finance': 2, 'Food': 3, 'Health': 4}
platform_map = {'Instagram': 0, 'Facebook': 1, 'LinkedIn': 2, 'YouTube': 3, 'TikTok': 4}
type_map = {'Reel': 0, 'Carousel': 1, 'Image': 2, 'Text': 3, 'Video': 4}
topic_map = {'Education': 0, 'News': 1, 'BehindScenes': 2, 'Tutorial': 3, 'Promo': 4}

# apply the mappings
df['Industry_code'] = df['Industry'].map(industry_map)
df['Platform_code'] = df['Platform'].map(platform_map)
df['Type_code'] = df['Content Type'].map(type_map)
df['Topic_code'] = df['Content Topic'].map(topic_map)

# select inputs and target
# we want to predict "Performance Score" using the codes and ad spend
features = ['Industry_code', 'Platform_code', 'Type_code', 'Topic_code', 'Ad Spend']
X = df[features]
y = df['Performance Score']

# split data: 80% to train the model, 20% to test it
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train a Decision Tree model (it is like a simple flowchart of rules)
model = DecisionTreeRegressor(max_depth=4, random_state=42)
model.fit(X_train, y_train)

# check how accurate the model is on test data
predictions = model.predict(X_test)
error = mean_absolute_error(y_test, predictions)

print(f"Model trained successfully!")
print(f"Average error (MAE): {round(error, 2)} points (out of 100)")

# save the model and mappings to a file so our web app can load them
model_package = {
    'model': model,
    'industry_map': industry_map,
    'platform_map': platform_map,
    'type_map': type_map,
    'topic_map': topic_map
}

with open('model.pkl', 'wb') as f:
    pickle.dump(model_package, f)

print("Saved model and mappings to model.pkl")
