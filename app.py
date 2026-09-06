import streamlit as st
import pandas as pd
import joblib

# Load the trained model
loaded_model = joblib.load('linear_regression_model.sav')

st.title('Sales Prediction App')
st.write('Enter the advertising spends to predict sales.')

# Get user input for features
tv = st.slider('TV Spend', 0.0, 300.0, 100.0)
radio = st.slider('Radio Spend', 0.0, 50.0, 25.0)
newspaper = st.slider('Newspaper Spend', 0.0, 100.0, 20.0)

# Create a DataFrame for the input
input_data = pd.DataFrame([{
    'TV': tv,
    'Radio': radio,
    'Newspaper': newspaper
}])

# Make prediction
if st.button('Predict Sales'):
    prediction = loaded_model.predict(input_data)
    st.success(f'Predicted Sales: {prediction[0]:.2f}')
