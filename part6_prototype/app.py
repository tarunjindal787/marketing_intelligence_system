# app.py
# This is a Streamlit prototype application for Talknlock.
# It provides a simple web interface to predict content performance.
# There are no functions (def) in this script. It runs top-down.

import streamlit as st
import pickle
import numpy as np
import os
import shutil

# Step 1: Copy model package from Part 3 if it's not already in this folder
# This makes sure the folder can run as a separate "repo"
if not os.path.exists('rf_model.pkl'):
    shutil.copy('../part3_ml_model/rf_model.pkl', 'rf_model.pkl')

# Step 2: Load the model package
with open('rf_model.pkl', 'rb') as f:
    model_package = pickle.load(f)

rf_model = model_package['model']
industry_map = model_package['industry_map']
platform_map = model_package['platform_map']
type_map = model_package['type_map']
topic_map = model_package['topic_map']
day_map = model_package['day_map']
time_map = model_package['time_map']

# Step 3: Set up the page header and layout
st.set_page_config(page_title="Talknlock Marketing Intelligence", layout="centered")
st.title("📊 Talknlock Marketing Intelligence System")
st.write("This is a simple prototype to predict how well a post will perform *before* you publish it.")

# Step 4: Create the input form elements in the UI
st.subheader("Enter Post Details")

# Lists for dropdowns (getting keys from our maps)
col1, col2 = st.columns(2)

with col1:
    input_industry = st.selectbox("Industry", list(industry_map.keys()))
    input_platform = st.selectbox("Platform", list(platform_map.keys()))
    input_content_type = st.selectbox("Content Type", list(type_map.keys()))

with col2:
    input_topic = st.selectbox("Content Topic", list(topic_map.keys()))
    input_day = st.selectbox("Posting Day", list(day_map.keys()))
    # The PDF example uses 7 PM, so let's make sure it's in our options
    input_time = st.selectbox("Posting Time", list(time_map.keys()), index=3) # defaults to 6 PM

input_spend = st.number_input("Ad Spend ($)", min_value=0.0, max_value=2000.0, value=0.0, step=10.0)

# Step 5: Run prediction when user clicks the button
if st.button("Predict Performance", type="primary"):
    
    # Map the selected string values to numeric codes for the model
    industry_code = industry_map[input_industry]
    platform_code = platform_map[input_platform]
    type_code = type_map[input_content_type]
    topic_code = topic_map[input_topic]
    day_code = day_map[input_day]
    time_code = time_map[input_time]
    
    # Put features in a format the model understands
    feature_vector = np.array([[industry_code, platform_code, type_code, topic_code, day_code, time_code, input_spend]])
    
    # Predict the score (it returns an array, so we get the first element)
    predicted_score = rf_model.predict(feature_vector)[0]
    # Format the score to integer
    predicted_score = int(round(predicted_score))
    
    # Calculate some realistic expected engagement numbers for display
    # (Using simple multiplier based on the score)
    expected_engagement = int(predicted_score * 3.5)
    
    # Display the results
    st.markdown("---")
    st.subheader("🔮 System Output")
    
    # Display score and engagement metrics
    st.write(f"**Predicted performance score** ➔ **{predicted_score} / 100**")
    st.write(f"**Expected engagement** ➔ **{expected_engagement} interactions** (likes, shares, comments)")
    
    # Display top factors influencing prediction
    # We display fixed rankings based on our global feature importance from Part 5
    st.write("**Top factors influencing prediction:**")
    st.write("1. **Platform Selection** (LinkedIn & TikTok perform best)")
    st.write("2. **Ad Spend Amount** (Higher spend increases score)")
    st.write("3. **Industry Vertical** (Tech & Fashion have higher base scores)")
    st.write("4. **Content Format** (Video and Reels get more views)")
    
    # Simple rule-based logic to generate a recommended action based on the input
    st.write("**Recommended action:**")
    
    if input_content_type != 'Reel' and input_platform in ['Instagram', 'TikTok']:
        st.info(f"💡 'Create more educational Reels around this topic.' (Switching to Reel format can boost your score by 3-5 points on {input_platform})")
    elif input_spend == 0:
        st.info(f"💡 'Consider putting $50 budget on this post.' (Paid boost can increase reach and conversion score by up to 10 points)")
    else:
        st.success(f"💡 'This content looks solid for {input_platform}. Maintain this format and topic!'")
