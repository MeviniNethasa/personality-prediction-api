# Personality Predictor Engine (AI/ML Intern Task)

An end-to-end Machine Learning pipeline and live web service built to predict whether an individual leans toward an Introvert or Extrovert profile based on behavioral habits.

*   **Interactive Web UI:** https://mevininethasa-personality-predictor.hf.space


## Summary

1.  **Data Cleaning:** Handled missing features using robust imputation rules (column **median** for numeric attributes to prevent outlier distortion; column **mode** for categorical attributes).
2.  **Model Selection:** Evaluated competing Random Forest and XGBoost architectures.
3.  **Production Champion:** Selected **Random Forest** as the production model after it achieved a top classification **Accuracy of 91.90%** and a balanced **92.15% F1-score**.
4.  **Interpretability:** Extracted feature importances proving that psychological indicators like `Stage_fear` and `Time_spent_Alone` drive the model's choices.
5.  **Deployment:** Served via **FastAPI** and hosted live on **Hugging Face Spaces** using a custom Docker container configuration.
6.  **Presentation Layer:** Added a responsive frontend user interface (`index.html`) at the root URL to allow convenient manual form testing.
