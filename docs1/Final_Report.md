# Final Report

---

## 🧾 Final Report Summary

**Project Title**: Cryptocurrency Liquidity Prediction for Market Stability.
**Date**: March 16–17, 2022
**Prepared By**: \[Justone Singh]

---

### 🎯 Objective

To analyze historical cryptocurrency data and build machine learning models that predict price or related trends based on features like market cap, volume, and historical performance.

---

### 📁 Dataset

* Source: [CoinGecko](https://www.coingecko.com)
* Files used:

  * `coin_gecko_2022-03-16.csv`
  * `coin_gecko_2022-03-17.csv`
* Features include:

  * Coin name, ticker, price, 1h/24h/7d changes, market cap, volume, etc.

---

### 🔍 EDA Findings

* Many coins had missing values, especially in volume and % change fields.
* Data skewed: applied log transforms to volume.
* Correlation seen between `market_cap`, `24h_volume`, and price metrics.
* Feature scaling applied using `StandardScaler`.

---

### 🛠 Models Implemented

1. **Linear Regression**

   * Simple baseline model
   * Fast but underfits non-linear patterns
2. **Random Forest Regressor**

   * Ensemble model with better performance
   * Tuned using `GridSearchCV`

---

### 📊 Evaluation Metrics

* **Mean Absolute Error (MAE)**
* **Mean Squared Error (MSE)**
* **R² Score**

> Results showed that Random Forest significantly outperformed Linear Regression in capturing trends from the volatility-heavy data.

---

### 🧱 Architecture Summary

* **Data ingestion** → Cleaning → EDA → Feature Engineering → ML Modeling → Evaluation → Export
* Modular design allows easy extension for:

  * New models
  * Real-time prediction
  * Dashboarding

---

### ✅ Conclusions

* Machine Learning can provide predictive insights for coin movements.
* Daily snapshot data has limitations; real-time data can enhance accuracy.
* Feature richness and regularization are key for better model performance.


---

