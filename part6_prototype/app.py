# app.py
# simple streamlit web app for marketing intelligence tool.
# written like a basic college student project.

import streamlit as st
import pickle
import numpy as np

# load the raw model directly from the training folder
model = pickle.load(open('../part3_ml_model/model.pkl', 'rb'))

# mapping dictionaries
ind_map = {'Tech': 0, 'Fashion': 1, 'Finance': 2, 'Food': 3, 'Health': 4}
plat_map = {'Instagram': 0, 'Facebook': 1, 'LinkedIn': 2, 'YouTube': 3, 'TikTok': 4}
type_map = {'Reel': 0, 'Carousel': 1, 'Image': 2, 'Text': 3, 'Video': 4}
topic_map = {'Education': 0, 'News': 1, 'BehindScenes': 2, 'Tutorial': 3, 'Promo': 4}

st.title("Talknlock Content Predictor")
st.write("Enter details below to predict how well your post will perform:")

# select boxes for user input
col1, col2 = st.columns(2)
with col1:
    input_industry = st.selectbox("Select Industry", list(ind_map.keys()))
    input_platform = st.selectbox("Select Platform", list(plat_map.keys()))
    input_type = st.selectbox("Select Content Type", list(type_map.keys()))
with col2:
    input_topic = st.selectbox("Select Content Topic", list(topic_map.keys()))
    input_spend = st.number_input("Ad Spend ($)", min_value=0, max_value=500, value=0, step=10)

# when button is clicked
if st.button("Predict Performance Score"):
    # convert string values to numeric codes using our maps
    ind_val = ind_map[input_industry]
    plat_val = plat_map[input_platform]
    type_val = type_map[input_type]
    topic_val = topic_map[input_topic]
    
    # put features in a 2D array
    features = [[ind_val, plat_val, type_val, topic_val, input_spend]]
    
    # get prediction from the model
    score = model.predict(features)[0]
    score = int(round(score))
    
    # print prediction output
    st.write(f"### Predicted Performance Score: {score} / 100")
    
    # simple advice based on platform and type choice
    st.write("---")
    st.write("**Top Tips:**")
    if input_type != 'Reel' and input_platform in ['Instagram', 'TikTok']:
        st.write("- Changing format to Reel would get higher engagement on Instagram/TikTok.")
    elif input_spend == 0:
        st.write("- Try boosting this post with $20-$30 to increase reach.")
    else:
        st.write("- Good configuration! Ready to publish.")
