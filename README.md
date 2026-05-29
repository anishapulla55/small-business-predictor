Small Business Loan Risk Predictor 

A deployed machine learning web application that predicts the repayment risk of SBA small business loans using historical financial and business data.

Overview 
This project uses a Random Forest classification model trained on real-world SBA loan data to estimate whether a loan is likely to be paid in full or default. 
The application includes: 
- End-to-end machine learning pipeline
- Automated preprocessing and encoding
- Class imbalance handling
- Risk probability scoring
- Interactive Streamlit web application
- Public cloud deployment

Technologies Used 
- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib

Machine Learning Workflow

1.) Cleaned and preprocessed SBA loan dataset 

2.) Handled categorical and numerical features using pipelines 

3.) Built a preprocessing + model pipeline using ColumnTransformer 

4.) Trained a Random Forest classifier 

5.) Evaluated model performance using classification metrics 

6.) Deployed the model as an interactive web application 


Model Performance 
* Accuracy: ~86%
* Default Recall: ~83%
The model was optimied to better identify risky loans rather than maximizing raw accuracy alone.

Live Demo
https://small-business-predictor-dg9teazs9dftz9xgxhbvxn.streamlit.app/

<img width="1573" height="1305" alt="image" src="https://github.com/user-attachments/assets/e8253b04-9d98-4f02-aba5-9738fb5a2dfd" />

<img width="609" height="449" alt="image" src="https://github.com/user-attachments/assets/4a879b20-2b87-4e94-bb9d-758cd6447b10" />


Future Improvements
* Additional model experimentation
* Feature importance visualizations
* Explainable AI integrations
* Historical trend dashboards
* Threashold optimization for risk-sensitive predictions

Author: Anisha Pulla 
