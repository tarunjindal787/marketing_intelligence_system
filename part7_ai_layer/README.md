# Part 7: AI Layer

Traditional Machine Learning is great at numbers (predicting scores, classification, regression). But it cannot talk or write. This is where an LLM (Large Language Model) comes in to build a complete system.

Here is how we combine them:
`Marketing Data ➔ ML Model (Predicts Score) ➔ LLM Reasoning (Writes Recommendation) ➔ Human Review`

---

### 1. Traditional ML vs. LLM (What does what?)
We shouldn't use an LLM for everything. Here is a clean division:

| Task | Handled By | Why? |
|---|---|---|
| **Predicting the score** | **Traditional ML** (Random Forest) | It is fast, cheap, works with numerical data, and has 0 risk of "hallucinating" numbers. |
| **Finding correlations** | **Traditional ML / Code** | Math is exact. Traditional statistics are reliable and reproducible. |
| **Explaining the prediction** | **LLM** | Can take the feature importance numbers and write a friendly email to the manager explaining it. |
| **Writing content recommendations**| **LLM** | Can write actual post captions, suggest hooks, or brainstorm video scripts based on the topic. |
| **Summarising reports** | **LLM** | Can take a huge table of client metrics and write a 1-page executive summary for the client. |

---

### 2. How the LLM adds value
- **Analyse client feedback**: An LLM can read client emails or feedback forms, label the sentiment, and group complaints into categories (e.g. "pricing", "slow response").
- **Generate content insights**: LLMs can study top-performing posts and spot common linguistic hooks or styling choices.
- **Client-friendly reports**: Instead of sending a client a boring Excel sheet, the LLM can generate a report saying: "Hey, we grew your clicks by 15% this month! The best post was our video on product education which drove 22 leads."

This shows how using a hybrid system (ML for numbers, LLM for text) is much stronger than using just one of them.
