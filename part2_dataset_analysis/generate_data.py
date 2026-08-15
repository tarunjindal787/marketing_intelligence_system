# generate_data.py
# This script generates synthetic marketing data for our analysis and ML model.
# There are no functions (def) here, just a simple step-by-step script that anyone can read.

import pandas as pd
import numpy as np
import random

# Step 1: Set random seed for reproducibility so we always get the same data
np.random.seed(42)
random.seed(42)

# Step 2: Define categories for our dataset
industries = ['Tech', 'Fashion', 'Finance', 'Food & Beverage', 'Healthcare']
platforms = ['Instagram', 'Facebook', 'LinkedIn', 'YouTube', 'TikTok']
content_types = ['Reel', 'Carousel', 'Image', 'Text', 'Video']
topics = ['Product Education', 'Industry News', 'Behind the Scenes', 'Tutorial', 'Promo/Offer']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
times = ['9 AM', '12 PM', '3 PM', '6 PM', '9 PM', '12 AM']
clients = ['Client_A', 'Client_B', 'Client_C', 'Client_D', 'Client_E', 'Client_F', 'Client_G', 'Client_H', 'Client_I', 'Client_J']

# Step 3: Create lists to store our generated row data
data_rows = []

# Step 4: Loop 600 times to generate 600 rows (records)
for i in range(600):
    # Pick random categories
    client = random.choice(clients)
    industry = random.choice(industries)
    platform = random.choice(platforms)
    content_type = random.choice(content_types)
    topic = random.choice(topics)
    day = random.choice(days)
    time = random.choice(times)
    
    # Establish some rules for realistic reach and spend
    # YouTube and TikTok should generally have higher reach
    if platform == 'YouTube' or platform == 'TikTok':
        base_reach = random.randint(5000, 25000)
    elif platform == 'Instagram':
        base_reach = random.randint(2000, 12000)
    else:
        base_reach = random.randint(500, 5000)
        
    # Reach is also boosted by Industry (Tech and Fashion tend to go more viral)
    if industry == 'Tech' or industry == 'Fashion':
        base_reach = int(base_reach * 1.4)
        
    # Let's add some random variance to reach
    reach = int(base_reach * random.uniform(0.8, 1.2))
    
    # Impressions are always higher than reach (people seeing it multiple times)
    impressions = int(reach * random.uniform(1.2, 2.2))
    
    # Ad Spend: Some posts are organic (0 spend), some are paid (boosted posts)
    # 40% chance of being a paid post
    if random.random() < 0.40:
        ad_spend = round(random.uniform(20.0, 500.0), 2)
        # Paid posts get a big reach boost
        reach = int(reach * (1.0 + (ad_spend / 100.0)))
        impressions = int(impressions * (1.0 + (ad_spend / 80.0)))
    else:
        ad_spend = 0.0
        
    # Engagement metrics: likes, comments, shares, saves
    # Instagram and TikTok get more likes and saves
    # Facebook and LinkedIn get more shares and comments
    if platform == 'Instagram' or platform == 'TikTok':
        like_ratio = random.uniform(0.05, 0.12)
        save_ratio = random.uniform(0.02, 0.06)
        share_ratio = random.uniform(0.01, 0.03)
        comment_ratio = random.uniform(0.005, 0.02)
    elif platform == 'LinkedIn':
        like_ratio = random.uniform(0.02, 0.06)
        save_ratio = random.uniform(0.01, 0.03)
        share_ratio = random.uniform(0.03, 0.07) # LinkedIn loves resharing
        comment_ratio = random.uniform(0.01, 0.03)
    else:
        like_ratio = random.uniform(0.01, 0.05)
        save_ratio = random.uniform(0.005, 0.02)
        share_ratio = random.uniform(0.01, 0.04)
        comment_ratio = random.uniform(0.005, 0.015)
        
    likes = int(impressions * like_ratio)
    saves = int(impressions * save_ratio)
    shares = int(impressions * share_ratio)
    comments = int(impressions * comment_ratio)
    
    # Video views and watch time (mostly for video/reel content types)
    if content_type in ['Video', 'Reel'] or platform in ['YouTube', 'TikTok']:
        video_views = int(impressions * random.uniform(0.4, 0.8))
        watch_time_hours = round(video_views * random.uniform(0.05, 0.25), 2)
    else:
        video_views = 0
        watch_time_hours = 0.0
        
    # Clicks and Leads (conversions)
    # Clicks are based on impressions and platform (LinkedIn and Facebook have higher click rates)
    click_ratio = random.uniform(0.01, 0.04)
    if platform == 'LinkedIn' or platform == 'Facebook':
        click_ratio += 0.015
    clicks = int(impressions * click_ratio)
    
    # Leads are generated from clicks (conversion rate of clicks to leads is 2% to 8%)
    lead_ratio = random.uniform(0.02, 0.08)
    # B2B platform LinkedIn gets slightly better lead conversion
    if platform == 'LinkedIn':
        lead_ratio += 0.03
    leads = int(clicks * lead_ratio)
    
    # Revenue is generated from leads (each lead has a value)
    # Let's say each lead is worth around $80 to $150
    revenue = round(leads * random.uniform(80.0, 150.0), 2)
    
    # Step 5: Calculate a Performance Score (0 to 100)
    # This is our target variable for the machine learning model.
    # It is a weighted score of engagement rate, clicks, leads and ROI.
    engagement_score = (likes + comments * 2 + shares * 3 + saves * 2) / (impressions + 1) * 100
    click_score = (clicks / (impressions + 1)) * 500
    lead_score = (leads / (clicks + 1)) * 1000
    
    # Combine them and cap at 100
    perf_score = int(engagement_score * 0.4 + click_score * 0.3 + lead_score * 0.3)
    # Add random noise to make it realistic
    perf_score += random.randint(-5, 5)
    # Keep between 0 and 100
    perf_score = max(0, min(100, perf_score))
    
    # Append the row to our list
    data_rows.append({
        'Client': client,
        'Industry': industry,
        'Platform': platform,
        'Content Type': content_type,
        'Content Topic': topic,
        'Posting Day': day,
        'Posting Time': time,
        'Reach': reach,
        'Impressions': impressions,
        'Likes': likes,
        'Comments': comments,
        'Shares': shares,
        'Saves': saves,
        'Video Views': video_views,
        'Watch Time (Hours)': watch_time_hours,
        'Clicks': clicks,
        'Leads': leads,
        'Ad Spend': ad_spend,
        'Revenue': revenue,
        'Performance Score': perf_score
    })

# Step 6: Convert list of dicts to a pandas DataFrame
df = pd.DataFrame(data_rows)

# Step 7: Export to CSV
df.to_csv('dataset.csv', index=False)
print("Dataset created successfully with", len(df), "rows and saved to dataset.csv")
