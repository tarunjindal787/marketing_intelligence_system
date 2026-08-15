# train_model.py
# trains a decision tree to predict performance score.
# written like a simple college assignment.

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

# load the data directly from the analysis folder
df = pd.read_csv('../part2_dataset_analysis/dataset.csv')

# dictionaries to map text to numbers
ind_map = {'Tech': 0, 'Fashion': 1, 'Finance': 2, 'Food': 3, 'Health': 4}
plat_map = {'Instagram': 0, 'Facebook': 1, 'LinkedIn': 2, 'YouTube': 3, 'TikTok': 4}
type_map = {'Reel': 0, 'Carousel': 1, 'Image': 2, 'Text': 3, 'Video': 4}
topic_map = {'Education': 0, 'News': 1, 'BehindScenes': 2, 'Tutorial': 3, 'Promo': 4}

# mapping values using .map
df['Industry'] = df['Industry'].map(ind_map)
df['Platform'] = df['Platform'].map(plat_map)
df['Content Type'] = df['Content Type'].map(type_map)
df['Content Topic'] = df['Content Topic'].map(topic_map)

# choose inputs and output
features = ['Industry', 'Platform', 'Content Type', 'Content Topic', 'Ad Spend']
X = df[features]
y = df['Performance Score']

# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train a decision tree regressor
model = DecisionTreeRegressor(max_depth=4, random_state=42)
model.fit(X_train, y_train)

# make predictions on test set and check error
preds = model.predict(X_test)
error = mean_absolute_error(y_test, preds)

print("Decision Tree Model Trained!")
print("MAE Error on test set:", round(error, 2))

# save the raw model to file
pickle.dump(model, open('model.pkl', 'wb'))
print("Saved model to model.pkl")
