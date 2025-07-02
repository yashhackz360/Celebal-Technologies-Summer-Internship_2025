import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import shap
import matplotlib.pyplot as plt

# Title
st.title("📉 Client Attrition Predictor")
st.markdown("Predict customer churn risk in real-time")

# Generate synthetic training data (in-memory, no file needed)
@st.cache_resource
def train_model():
    # Sample churn data (replace with real data in production)
    data = {
        'tenure': [12, 5, 30, 8, 24, 3, 15, 36, 9, 18],
        'monthly_charges': [70.5, 90.2, 45.0, 60.0, 85.0, 100.0, 55.0, 40.0, 75.0, 65.0],
        'total_charges': [846.0, 451.0, 1350.0, 480.0, 2040.0, 300.0, 825.0, 1440.0, 675.0, 1170.0],
        'contract_type': [0, 1, 2, 0, 1, 0, 1, 2, 0, 1],  # 0=Monthly, 1=1yr, 2=2yr
        'churn': [1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
    }
    df = pd.DataFrame(data)
    
    X = df.drop('churn', axis=1)
    y = df['churn']
    
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    return model

model = train_model()

# Input Section
st.sidebar.header("🔧 Input Options")
input_method = st.sidebar.radio("Choose input method:", ["Manual Entry", "Upload CSV"])

if input_method == "Manual Entry":
    st.subheader("📝 Enter Customer Details")
    col1, col2 = st.columns(2)
    
    with col1:
        tenure = st.number_input("Tenure (months)", min_value=0, max_value=120, value=12)
        monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, value=70.5)
    
    with col2:
        total_charges = st.number_input("Total Charges ($)", min_value=0.0, value=846.0)
        contract_type = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    
    # Preprocess input
    contract_mapping = {"Month-to-month": 0, "One year": 1, "Two year": 2}
    input_data = pd.DataFrame([[tenure, monthly_charges, total_charges, contract_mapping[contract_type]]],
                            columns=['tenure', 'monthly_charges', 'total_charges', 'contract_type'])

else:
    uploaded_file = st.file_uploader("📂 Upload Customer Data (CSV)", type=["csv"])
    if uploaded_file:
        input_data = pd.read_csv(uploaded_file)
        # Ensure column names match what model expects
        required_cols = ['tenure', 'monthly_charges', 'total_charges', 'contract_type']
        if not all(col in input_data.columns for col in required_cols):
            st.error(f"CSV must contain these columns: {required_cols}")
            st.stop()
        st.write("Preview:")
        st.dataframe(input_data.head())

# Prediction
if st.button("🔮 Predict Churn Risk") and 'input_data' in locals():
    try:
        # Make prediction
        prediction = model.predict(input_data)
        prediction_proba = model.predict_proba(input_data)
        
        # Display results
        st.subheader("📊 Prediction Results")
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Churn Probability", f"{prediction_proba[0][1] * 100:.2f}%")
        
        with col2:
            st.metric("Predicted Class", "🚨 Churn" if prediction[0] == 1 else "✅ Retained")
        
        # Explainability
        st.subheader("🤖 Model Insights")
        
        # Feature importance
        st.markdown("**Top Factors Influencing Prediction:**")
        feature_imp = pd.DataFrame({
            'Feature': input_data.columns,
            'Importance': model.feature_importances_
        }).sort_values('Importance', ascending=False)
        
        st.bar_chart(feature_imp.set_index('Feature'))
        
        # SHAP explanation (for single prediction)
        st.markdown("**How Each Feature Affected This Prediction:**")
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(input_data)
        
        fig, ax = plt.subplots()
        shap.decision_plot(explainer.expected_value[1], 
                          shap_values[1][0], 
                          input_data.iloc[0],
                          show=False)
        st.pyplot(fig)
        
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")

# Footer

st.caption("||  Celebal Summer Itnernship CT_CSI_DS_13 Week 7 Task  ||")
st.markdown("---")
st.caption("Yashwanth sai kasarabada || All rights reserved")
