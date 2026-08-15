# app.py
# simple web app for talknlock content performance prediction.
# no def functions, just simple streamlit code.

import streamlit as st
import pickle
import numpy as np
import os
import shutil

# copy the model file here if it isn't already here
if not os.path.exists('model.pkl'):
    shutil.copy('../part3_ml_model/model.pkl', 'model.pkl')

# load the model and mappings
with open('model.pkl', 'rb') as f:
    package = pickle.load(f)

model = package['model']
industry_map = package['industry_map']
platform_map = package['platform_map']
type_map = package['type_map']
topic_map = package['topic_map']

# set up web page title
st.set_page_config(page_title="Talknlock AI App", layout="centered")
st.title("📊 Talknlock Content Predictor")
st.write("This is a simple prototype to predict how well a post will perform.")

st.subheader("Select post details:")

# dropdown selectors for the user
col1, col2 = st.columns(2)
with col1:
    input_industry = st.selectbox("Industry", list(industry_map.keys()))
    input_platform = st.selectbox("Platform", list(platform_map.keys()))
    input_type = st.selectbox("Content Type", list(type_map.keys()))
with col2:
    input_topic = st.selectbox("Content Topic", list(topic_map.keys()))
    input_spend = st.number_input("Ad Spend ($)", min_value=0, max_value=1000, value=0, step=10)

# predict when button is clicked
if st.button("Predict Score", type="primary"):
    # map select strings to numbers for the model
    ind_code = industry_map[input_industry]
    plat_code = platform_map[input_platform]
    type_code = type_map[input_type]
    topic_code = topic_map[input_topic]
    
    # create feature list
    features = np.array([[ind_code, plat_code, type_code, topic_code, input_spend]])
    
    # get prediction score
    score = model.predict(features)[0]
    score = int(round(score))
    
    # estimate engagement
    engagement = int(score * 3.2)
    
    # print results to page
    st.markdown("---")
    st.subheader("🔮 System Output")
    st.write(f"**Predicted performance score** ➔ **{score} / 100**")
    st.write(f"**Expected engagement** ➔ **{engagement} interactions** (likes, comments, clicks)")
    
    # print top factors influencing the score
    st.write("**Top factors influencing prediction:**")
    st.write("1. **Platform Selection** (LinkedIn and TikTok have higher reach)")
    st.write("2. **Ad Spend** (Paid posts get a boost in visibility)")
    st.write("3. **Industry Vertical** (Certain products get easier engagement)")
    
    # simple tip based on input content type
    st.write("**Recommended action:**")
    if input_type != 'Reel' and input_platform in ['Instagram', 'TikTok']:
        st.info("💡 Tip: Try changing your content type to 'Reel' for Instagram/TikTok to boost engagement!")
    elif input_spend == 0:
        st.info("💡 Tip: Adding a small budget (like $20-$50) can significantly boost reach and score!")
    else:
        st.success("💡 Content parameters look solid! Proceed with publishing.")
