import streamlit as st
import pickle
import numpy as np

# Load the trained model
# Make sure your file is named correctly (e.g., 'model.pkl' not 'model.pk1')
with open('model.pk1', 'rb') as f:
    model = pickle.load(f)

# App title
st.title('Salary Prediction App')

# Input: Years of experience
exp = st.number_input(
    "Enter Experience (years):",
    min_value=0,
    max_value=50,
    value=1
)

# Predict button
if st.button("Predict"):
    try:
        # Predict salary
        result = model.predict(np.array([[exp]]))
        
        # Convert result to a Python scalar safely
        predicted_salary = int(result.item())
        
        st.success(f"Predicted Salary: ₹{predicted_salary}")
    except Exception as e:
        st.error(f"Error in prediction: {e}")