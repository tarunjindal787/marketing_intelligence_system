# ai_reasoning.py
# this script shows how the ML prediction is combined with an LLM prompt.
# we use template printing so it runs without needing active API keys.
# no def functions, just simple steps.

# Step 1: Mock output variables from our ML model (model.pkl)
predicted_score = 98
expected_engagement = 313
platform = "LinkedIn"
industry = "Tech"
content_type = "Reel"
topic = "Education"
ad_spend = 50.0

# Step 2: Build a prompt we would send to an LLM (like Gemini or GPT)
prompt = f"""
You are an AI Marketing Assistant. 
Analyze this post idea and our ML model prediction:

- Industry: {industry}
- Platform: {platform}
- Content Type: {content_type}
- Topic: {topic}
- Ad Spend: ${ad_spend}

ML Prediction:
- Predicted Performance Score: {predicted_score}/100
- Expected Engagement: {expected_engagement} interactions

Write a short, friendly content plan for the marketer. 
Explain why the score is high/low and what they should write about.
Keep it under 3 paragraphs.
"""

print("--- PROMPT WE SEND TO THE LLM ---")
print(prompt)

# Step 3: Simulated response returned by the LLM
simulated_llm_response = f"""
Hey Team,

Your upcoming post on {platform} about "{topic}" is predicted to score a very high {predicted_score}/100. 

Why is it so high?
- **LinkedIn Boost**: LinkedIn has strong click rates for Tech content.
- **Video Format**: Using a Reel format keeps viewers watching longer.
- **Budget**: Spending ${ad_spend} on ads guarantees a larger initial audience.

Suggested Next Steps:
1. Write a short script that explains a common tech problem in the first 5 seconds.
2. Put the link to our website in the comments to drive conversions.
"""

print("\n--- SIMULATED LLM RESPONSE ---")
print(simulated_llm_response)
