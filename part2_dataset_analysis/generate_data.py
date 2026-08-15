# generate_data.py
# this is a super simple script to make our marketing dataset.
# no def functions here, just a basic loop that generates random rows.

import pandas as pd
import numpy as np
import random

# lists of categories we will pick from randomly
industries = ['Tech', 'Fashion', 'Finance', 'Food', 'Health']
platforms = ['Instagram', 'Facebook', 'LinkedIn', 'YouTube', 'TikTok']
types = ['Reel', 'Carousel', 'Image', 'Text', 'Video']
topics = ['Education', 'News', 'BehindScenes', 'Tutorial', 'Promo']

# empty lists to hold our column data
col_client = []
col_industry = []
col_platform = []
col_type = []
col_topic = []
col_reach = []
col_impressions = []
col_likes = []
col_comments = []
col_clicks = []
col_leads = []
col_spend = []
col_score = []

# loop 550 times to generate 550 rows of data
for i in range(550):
    # pick random categories
    ind = random.choice(industries)
    plat = random.choice(platforms)
    ctype = random.choice(types)
    topic = random.choice(topics)
    
    # generate reach - youtube and tiktok get higher numbers
    if plat == 'YouTube' or plat == 'TikTok':
        reach = random.randint(8000, 20000)
    else:
        reach = random.randint(1000, 8000)
        
    # impressions are just reach times a small multiplier
    impressions = int(reach * random.uniform(1.1, 1.8))
    
    # ad spend - some are organic (0 spend), some have budget
    if random.random() < 0.4:
        spend = random.randint(10, 300)
        # spend boosts reach
        reach = int(reach * 1.5)
        impressions = int(impressions * 1.6)
    else:
        spend = 0
        
    # calculate engagements using simple percentages
    likes = int(impressions * random.uniform(0.02, 0.08))
    comments = int(likes * random.uniform(0.05, 0.15))
    clicks = int(impressions * random.uniform(0.01, 0.04))
    leads = int(clicks * random.uniform(0.05, 0.15))
    
    # calculate a simple performance score out of 100
    # higher likes, clicks, and leads make it higher. high spend lowers the ROI score.
    score_calc = (likes * 0.1 + clicks * 0.5 + leads * 2.0) - (spend * 0.05)
    score_calc = int(score_calc + random.randint(10, 30)) # add some random base
    
    # keep score between 0 and 100
    if score_calc > 100:
        score_calc = 100
    if score_calc < 0:
        score_calc = 0
        
    # append to our lists
    col_client.append(f"Client_{random.randint(1, 10)}")
    col_industry.append(ind)
    col_platform.append(plat)
    col_type.append(ctype)
    col_topic.append(topic)
    col_reach.append(reach)
    col_impressions.append(impressions)
    col_likes.append(likes)
    col_comments.append(comments)
    col_clicks.append(clicks)
    col_leads.append(leads)
    col_spend.append(spend)
    col_score.append(score_calc)

# put all lists into a dictionary to make a dataframe
data_dict = {
    'Client': col_client,
    'Industry': col_industry,
    'Platform': col_platform,
    'Content Type': col_type,
    'Content Topic': col_topic,
    'Reach': col_reach,
    'Impressions': col_impressions,
    'Likes': col_likes,
    'Comments': col_comments,
    'Clicks': col_clicks,
    'Leads': col_leads,
    'Ad Spend': col_spend,
    'Performance Score': col_score
}

df = pd.DataFrame(data_dict)

# save to csv file
df.to_csv('dataset.csv', index=False)
print("done! saved 550 rows to dataset.csv")
