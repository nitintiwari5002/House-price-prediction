import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("house_price_model.pkl")

# Streamlit UI
st.title("🏠 House Price Prediction")

st.write("Enter the details of the house:")

overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
gr_liv_area = st.number_input("Above Ground Living Area (sq ft)", 500, 5000, 1500)
garage_cars = st.slider("Garage Capacity (cars)", 0, 4, 1)
total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", 0, 3000, 800)
full_bath = st.slider("Number of Full Bathrooms", 0, 5, 2)

# Button to predict
if st.button("Predict Price"):
    # Create input dataframe
    new_data = pd.DataFrame([{
        "OverallQual": overall_qual,
        "GrLivArea": gr_liv_area,
        "GarageCars": garage_cars,
        "TotalBsmtSF": total_bsmt_sf,
        "FullBath": full_bath
    }])
    
    # Make prediction
    prediction_usd = model.predict(new_data)[0]
    
    # Convert to INR (example rate: 1 USD = 83 INR)
    exchange_rate = 83
    prediction_inr = prediction_usd * exchange_rate
    
    st.success(f"Predicted House Price: ₹{prediction_inr:,.2f}")
