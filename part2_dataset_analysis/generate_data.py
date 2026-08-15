# generate_data.py
# simple script to make 500+ rows of marketing data.
# written for college assignment.

import pandas as pd
import random

# lists of values to choose from
all_industries = ['Tech', 'Fashion', 'Finance', 'Food', 'Health']
all_platforms = ['Instagram', 'Facebook', 'LinkedIn', 'YouTube', 'TikTok']
all_types = ['Reel', 'Carousel', 'Image', 'Text', 'Video']
all_topics = ['Education', 'News', 'BehindScenes', 'Tutorial', 'Promo']

# list to store all rows
rows = []

# generate 550 rows
for i in range(550):
    ind = random.choice(all_industries)
    plat = random.choice(all_platforms)
    ctype = random.choice(all_types)
    topic = random.choice(all_topics)
    
    # reach based on platform
    if plat == 'YouTube' or plat == 'TikTok':
        reach = random.randint(10000, 30000)
    elif plat == 'Instagram':
        reach = random.randint(5000, 15000)
    else:
        reach = random.randint(1000, 5000)
        
    # impressions is just reach + some random views
    impressions = int(reach * random.uniform(1.2, 1.6))
    
    # ad spend (about 30% of posts have spend)
    if random.random() < 0.3:
        spend = random.randint(20, 250)
        # spend increases reach
        reach = int(reach * 1.4)
        impressions = int(impressions * 1.5)
    else:
        spend = 0
        
    # simple engagement calculations
    likes = int(impressions * random.uniform(0.01, 0.06))
    comments = int(likes * random.uniform(0.02, 0.10))
    clicks = int(impressions * random.uniform(0.01, 0.03))
    leads = int(clicks * random.uniform(0.05, 0.12))
    
    # basic score formula out of 100
    score = (likes * 0.1 + clicks * 0.4 + leads * 1.5)
    score = int(score) + random.randint(5, 15)
    
    # make sure score is between 10 and 100
    if score > 100:
        score = 100
    if score < 10:
        score = 10
        
    # create row dictionary
    row = {
        'Client': f"Client_{random.randint(1, 8)}",
        'Industry': ind,
        'Platform': plat,
        'Content Type': ctype,
        'Content Topic': topic,
        'Reach': reach,
        'Impressions': impressions,
        'Likes': likes,
        'Comments': comments,
        'Clicks': clicks,
        'Leads': leads,
        'Ad Spend': spend,
        'Performance Score': score
    }
    rows.append(row)

# convert list of dicts to dataframe
df = pd.DataFrame(rows)

# save dataframe to csv
df.to_csv('dataset.csv', index=False)
print("dataset.csv created successfully with 550 records!")
