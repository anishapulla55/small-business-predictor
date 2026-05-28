import streamlit as st
import joblib 
import pandas as pd

#load trained model 
pipeline = joblib.load('loan_pipeline.pkl')

st.title('Small Business Loan Risk Prediction')

st.write('Enter business and loan information below:')

state = st.text_input("Business State", "VA")

bank_state = st.text_input("Bank State", "VA")

approval_fy = st.text_input("Approval Fiscal Year", "2006")

rev_line = st.selectbox("Revolving Credit Line", ["Y", "N"])

low_doc = st.selectbox("LowDoc Program", ["Y", "N"])

naics = st.number_input("NAICS Code", value=72)

term = st.number_input("Loan Term (Months)", value=84)

no_emp = st.number_input("Number of Employees", value=5)

new_exist = st.selectbox("Existing or New Business", [1, 2])

create_job = st.number_input("Jobs Created", value=0)

retained_job = st.number_input("Jobs Retained", value=0)

franchise = st.number_input("Franchise Code", value=0)

urban_rural = st.selectbox("Urban/Rural", [0, 1, 2])

disbursement = st.number_input("Disbursement Amount", value=50000.0)

gr_appv = st.number_input("Gross Approved Amount", value=50000.0)

sba_appv = st.number_input("SBA Guaranteed Amount", value=40000.0)

  
if st.button("Predict Risk"):

    input_data = pd.DataFrame([{
        "State": state,
        "BankState": bank_state,
        "NAICS": naics,
        "ApprovalFY": approval_fy,
        "Term": term,
        "NoEmp": no_emp,
        "NewExist": new_exist,
        "CreateJob": create_job,
        "RetainedJob": retained_job,
        "FranchiseCode": franchise,
        "UrbanRural": urban_rural,
        "RevLineCr": rev_line,
        "LowDoc": low_doc,
        "DisbursementGross": disbursement,
        "GrAppv": gr_appv,
        "SBA_Appv": sba_appv
    }])

    prediction = pipeline.predict(input_data)[0]

    probability = pipeline.predict_proba(input_data)[0][1]

    if probability < 0.3:
        risk = "High Risk"
    elif probability < 0.7:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    st.subheader("Prediction Result")

    st.write("Repayment Probability:", round(probability * 100, 2), "%")

    st.write("Risk Level:", risk)

    st.write(
        "Prediction:",
        "Likely Paid in Full" if prediction == 1 else "Likely Default"
    )