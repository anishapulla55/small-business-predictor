import streamlit as st
import joblib 
import pandas as pd

#load trained model 
model = joblib.load('loan_risk_model.pkl')

st.title('Small BusinessLoan Risk Prediction')

st.write('Enter business and loan information below:')

# Collect user input
term = st.number_input('Loan Term (months)', min_value=1)
no_of_employees = st.number_input('Number of Employees', min_value=0)
disbursement = st.number_input('Disbursement Amount', min_value=0.0)

#prediction button
if st.button('Predict Risk'):
    # Create a DataFrame for the input
    input_data = pd.DataFrame({
        'Term': [term],
        'NoEmp': [no_of_employees],
        'DisbursementGross': [disbursement]
    })
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    probability = model.predict_proba(input_data)[0][1]  # Probability of being high risk

    if prediction < 0.3:
        risk = "High Risk"
    elif prediction < 0.7:
        risk = "Medium Risk"
    else:
        risk = "Low Risk" 
    
    st.subheader('Prediction Result')

    st.write("RepaymentProbability:", round(probability * 100, 2), "%")

    st.write("Risk Level:", risk)

    st.write("Prediction:", "Likely Paid in Full" if prediction==1 else "Likely Default")
    