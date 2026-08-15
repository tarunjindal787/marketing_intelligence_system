# Part 4: Model Evaluation

Here is the evaluation details for our machine learning model. I wanted to make sure we don't just say "it works" but actually understand how it performs and what are the limitations.

### 1. Model Comparison
We compared two models against a simple baseline:

| Model | Mean Absolute Error (MAE) | R-squared ($R^2$ Score) |
|---|---|---|
| **Baseline** (Always predict average) | 6.681 | -0.001 |
| **Decision Tree Regressor** | 5.694 | 0.340 |
| **Random Forest Regressor** | **5.487** | **0.414** |

- **Winner**: The **Random Forest** is the best model. It explains about 41.4% of the variance ($R^2 = 0.414$) which is pretty good for marketing data, since human behavior is very noisy. Its error is also the lowest (5.48 points out of 100).
- **Why we selected Random Forest**: It combines 100 different decision trees, which helps reduce overfitting compared to a single decision tree. It also handles categorical features well once mapped.

---

### 2. Features Used and Excluded
- **Features Used**: `Industry`, `Platform`, `Content Type`, `Content Topic`, `Posting Day`, `Posting Time`, and `Ad Spend`. These are all known *before* the post is published, which makes them perfect for predicting future performance.
- **Features Excluded & Why**: We excluded `Reach`, `Impressions`, `Likes`, `Comments`, `Shares`, and `Saves`.
  - *Reason*: These are **target leakage**. If we knew how many likes a post got, we wouldn't need a model to predict its performance! These metrics are only known *after* the post has been published. Using them in training would make our model look 99% accurate in testing but completely useless in real life.

---

### 3. How we split the Dataset
We split the data using an 80/20 train-test split:
- **80% Training (480 rows)**: Used by the model to learn patterns.
- **20% Testing (120 rows)**: Held out and used only to evaluate how the model performs on unseen data.
- We used a random state of 42 so that the split is always the same.

---

### 4. Metrics Selected & Why
We used **Mean Absolute Error (MAE)** and **R-squared ($R^2$)**:
- **MAE**: This tells us how many points off our predictions are on average. Our MAE of 5.48 means if we predict a performance score of 80, the real score is usually between 74.5 and 85.5. It's very easy to explain to non-technical managers.
- **R-squared**: This tells us what % of the variance the model explains. A score of 0.414 means we explain 41% of the variation, while 59% is still due to other factors (like creative quality or copywriting).

---

### 5. Overfitting & Underfitting
- To prevent overfitting, we set `max_depth = 6` for the Random Forest. Without this limit, the trees would grow too deep, memorising the training set but failing on the test set.
- We are not underfitting because our test scores are significantly better than the baseline model.

---

### 6. What could go wrong in Production (Limitations & Risks)
- **Data Drift**: If a new platform becomes popular (like a new social app) or the algorithm changes, the model's old training data will become outdated, and predictions will get worse.
- **Creative Quality**: The model cannot "see" the image or video. A post with a amazing visual will do better than a post with a ugly image, even if they have the same platform, topic, and posting time. The model cannot capture this.
- **Out of Bound Ad Spend**: If someone enters $10,000 ad spend, but the training data only goes up to $500, the model might make weird predictions because trees don't extrapolate well.
