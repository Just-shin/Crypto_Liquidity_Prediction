
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Liquidity Ratio Predictor", page_icon="💧")
st.title("💧 Liquidity Ratio Predictor")

with st.form("input_form"):
    coin = st.selectbox("Coin", ["Bitcoin", "Ethereum", "Tether", "Other"])
    price = st.number_input("Price", min_value=0.0)
    pct_change_1h = st.number_input("1h % Change", value=0.0, step=0.01)
    pct_change_24h = st.number_input("24h % Change", value=0.0, step=0.01)
    pct_change_7d = st.number_input("7d % Change", value=0.0, step=0.01)
    volume_24h = st.number_input("24h Volume (in USD)", min_value=0.0)
    market_cap = st.number_input("Market Cap (in USD)", min_value=0.0)
    submitted = st.form_submit_button("Predict")

if submitted:
    # Calculate volatility_score as in your notebook
    volatility_score = np.std([pct_change_1h, pct_change_24h, pct_change_7d])

    # DataFrame with features in expected order (including liquidity_ratio placeholder)
    X_input = pd.DataFrame([[price, pct_change_1h, pct_change_24h, pct_change_7d, volume_24h, market_cap, volatility_score]],
                       columns=["price", "1h", "24h", "7d", "24h_volume", "mkt_cap", "volatility_score"])


    # Scale and predict
    X_scaled = scaler.transform(X_input)
    prediction = model.predict(X_scaled)

    st.success(f"💧 Predicted Liquidity Ratio: {prediction[0]:.4f}")

