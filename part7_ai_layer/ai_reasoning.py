# ai_reasoning.py
# This script shows how we combine our ML model predictions with an LLM (AI reasoning layer).
# Since we want to keep it simple, we simulate the LLM's output using simple python text mapping.
# No functions (def) are used in this script. Everything is flat and top-down.

import json

# Step 1: Assume our ML model from Part 3 outputted these results
predicted_score = 40
expected_engagement = 140
platform = "LinkedIn"
industry = "Tech"
content_type = "Reel"
topic = "Product Education"
ad_spend = 100.0

# Step 2: Create a prompt that we would send to an LLM (like Gemini or OpenAI)
# This prompt merges the raw marketing data with the ML prediction score
prompt = f"""
You are an expert AI Marketing Assistant. 
Analyze the following post proposal and the prediction from our Machine Learning model:

--- INPUT DATA ---
- Industry: {industry}
- Platform: {platform}
- Content Type: {content_type}
- Content Topic: {topic}
- Ad Spend: ${ad_spend}

--- ML MODEL PREDICTION ---
- Predicted Performance Score: {predicted_score}/100
- Expected Engagement: {expected_engagement} interactions

--- TASK ---
Generate a friendly, action-oriented content brief that the digital marketer can use. 
Explain why the ML model predicted this score and what they should write about.
Keep it under 3 paragraphs.
"""

print("--- THE PROMPT SENT TO THE LLM ---")
print(prompt)

# Step 3: Simulate the LLM's response
# In production, we would use: response = openai.ChatCompletion.create(...) or google.generativeai.generate_content(...)
# Here we simulate it with a clean template so anyone can run the script without paying for API keys.

llm_simulated_response = f"""
Subject: Marketing Insight & Action Plan for your upcoming {platform} post

Hi Campaign Team,

Our ML model has predicted a Performance Score of {predicted_score}/100 for your proposed {content_type} post on {platform} about "{topic}". This is a strong prediction, performing about 38% better than the company benchmark (average score 28.9).

Why did the model predict this?
- **LinkedIn Advantage**: LinkedIn is our highest-converting platform for B2B Tech clients, which drives up the score.
- **Reel Format**: Video reels are highly pushed by the algorithm, resulting in higher watch times and reach.
- **Paid Boost**: The ${ad_spend} ad spend ensures high visibility and improves lead conversion.

Suggested Next Steps (Human Action Required):
1. Write a script focusing on solving a common developer problem (since topic is Product Education).
2. Start the video with a strong hook in the first 3 seconds (e.g. "Stop wasting hours on...").
3. Include a clear call-to-action (CTA) pointing users to our landing page to convert them into leads.
"""

print("\n--- SIMULATED LLM REASONING LAYER OUTPUT ---")
print(llm_simulated_response)
