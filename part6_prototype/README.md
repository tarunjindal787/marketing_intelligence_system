# Part 6: Build a Simple Prototype

I have created a basic working prototype using **Streamlit**. It takes inputs from a web page and runs our Random Forest model to predict performance scores and give tips.

### How to Run the App
To run it, open your terminal (like CMD or Powershell) and run this command:

```bash
streamlit run app.py
```

It will automatically open a new tab in your web browser at `http://localhost:8501`.

### What it does:
- **Drop-down Menus**: You can choose the Industry, Platform, Content Type, Content Topic, Posting Day, and Posting Time.
- **Budget Input**: You can enter how much money you want to spend on the post (Ad Spend).
- **Run Prediction**: Click the button, and it will load `rf_model.pkl` to calculate the performance score and estimated engagement.
- **Recommendations**: It gives simple rule-based recommendations on how to improve the score (e.g., advising you to use Reels or add some ad budget).
