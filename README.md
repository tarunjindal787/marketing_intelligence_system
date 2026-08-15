# Talknlock Marketing Intelligence System - AI/ML Assignment

Hello! This is my complete submission folder for the Talknlock AI/ML assignment. 

I've structured this project as a series of modular folders (like separate repos) for every part of the assignment. 
As requested, **none of the Python scripts use custom functions (`def`)**. They are all written top-down, step-by-step, with lots of `#` comments explaining what every block does so it is very easy to explain to anyone.

---

## Folder Structure

Here is where everything is located:

- [**part1_business_discovery/**](file:///E:/BLEND/marketing_intelligence_system/part1_business_discovery/README.md): Analysis of 3 major agency problems, comparing AI/ML vs. simple automation and SQL.
- [**part2_dataset_analysis/**](file:///E:/BLEND/marketing_intelligence_system/part2_dataset_analysis/): 
  - `generate_data.py`: Creates our synthetic dataset of 600 records.
  - `analyze_data.py`: Performs statistical analysis and outputs charts.
  - `dataset.csv`: The generated dataset.
  - Plots generated: `platform_performance.png`, `industry_performance.png`, `correlation_matrix.png`.
- [**part3_ml_model/**](file:///E:/BLEND/marketing_intelligence_system/part3_ml_model/):
  - `train_model.py`: Trains a Decision Tree and a Random Forest model, and saves the best model.
  - `rf_model.pkl`: The saved model package.
- [**part4_model_evaluation/**](file:///E:/BLEND/marketing_intelligence_system/part4_model_evaluation/README.md): Details on model comparison, baseline performance, features selected, data leakage, and production risks.
- [**part5_explainability/**](file:///E:/BLEND/marketing_intelligence_system/part5_explainability/):
  - `explain_model.py`: Extracts feature importances and prints a plain-English explanation for a single prediction.
- [**part6_prototype/**](file:///E:/BLEND/marketing_intelligence_system/part6_prototype/):
  - `app.py`: The interactive Streamlit prototype.
- [**part7_ai_layer/**](file:///E:/BLEND/marketing_intelligence_system/part7_ai_layer/):
  - `ai_reasoning.py`: Demonstrates the AI/LLM reasoning layer prompt and output.
- [**part8_production_architecture/**](file:///E:/BLEND/marketing_intelligence_system/part8_production_architecture/README.md): High-level system design with a Mermaid architecture diagram.
- [**part9_business_case/**](file:///E:/BLEND/marketing_intelligence_system/part9_business_case/README.md): Financial calculations, hours saved, and CEO investment decision.
- [**part10_future_vision/**](file:///E:/BLEND/marketing_intelligence_system/part10_future_vision/README.md): 12-month building roadmap and 3-year AI department vision.

Other important documents:
- [**technical_report.md**](file:///E:/BLEND/marketing_intelligence_system/technical_report.md): The full 15-page comprehensive report combining all answers.
- [**final_question.md**](file:///E:/BLEND/marketing_intelligence_system/final_question.md): My 500-word answer to the final question (Why you should trust me to build this department).

---

## How to Run the Code

To run these scripts, make sure you have `pandas`, `sklearn`, `matplotlib`, `seaborn`, and `streamlit` installed. You can install them by running:
```bash
pip install pandas scikit-learn matplotlib seaborn streamlit
```

### 1. Generate the data
```bash
cd part2_dataset_analysis
python generate_data.py
```

### 2. Analyze the data
```bash
python analyze_data.py
```

### 3. Train the machine learning models
```bash
cd ../part3_ml_model
python train_model.py
```

### 4. Run explainability check
```bash
cd ../part5_explainability
python explain_model.py
```

### 5. Run the interactive web prototype (Streamlit)
```bash
cd ../part6_prototype
streamlit run app.py
```

### 6. Run the AI layer reasoning simulation
```bash
cd ../part7_ai_layer
python ai_reasoning.py
```
