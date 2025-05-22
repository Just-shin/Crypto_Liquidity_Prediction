# 🧾 Final Report Summary

**Project Title**: Cryptocurrency Liquidity Prediction for Market Stability.
**Date**: March 16–17, 2022
**Prepared By**: \[Justone Singh]

---

### 🎯 Objective

To analyze and model historical cryptocurrency data to predict trends and prices using statistical and machine learning methods.

---

### 📁 Dataset Overview

* **Source**: CoinGecko (CSV snapshots)
* **Files Used**:

  * `coin_gecko_2022-03-16.csv`
  * `coin_gecko_2022-03-17.csv`
* **Features**: Coin name, ticker, price, % change (1h, 24h, 7d), market cap, 24h volume, etc.

---

### 🔍 Exploratory Data Analysis (EDA)

* **Missing Values**: Imputed using column mean
* **Outliers**: Mitigated using log-transform (e.g., `24h_volume_log`)
* **Correlation**: High between market cap, volume, and price
* **Skewness**: Corrected in volume using `np.log1p()`

---

### 🛠️ Models Implemented

#### 🔹 Linear Regression

* **Pros**: Fast, interpretable baseline
* **Cons**: Underfits nonlinear patterns

#### 🔹 Random Forest Regressor

* **Pros**: Captures nonlinear interactions, handles feature variance well
* **Tuning**: Used `GridSearchCV` for hyperparameter optimization

---

### 📊 Model Performance

| Model                   | MAE   | MSE   | R² Score |
| ----------------------- | ----- | ----- | -------- |
| Linear Regression       | 0.127 | 0.032 | 0.74     |
| Random Forest Regressor | 0.069 | 0.015 | 0.89     |

> **Insight**: The Random Forest Regressor outperformed Linear Regression in all metrics, showing better generalization and predictive accuracy.

---

### 🧱 System Architecture

* **Pipeline**: CSV Ingestion → Cleaning → Feature Engineering → Modeling → Evaluation → Report Generation
* **Tools**: Python, pandas, seaborn, scikit-learn, matplotlib
* **Modularity**: Pipeline can be automated or adapted for real-time data ingestion (e.g., with  Streamlit)

---

### ✅ Key Conclusions

* Feature engineering (e.g., log transforms) significantly improved model accuracy.
* Ensemble models like Random Forest are more effective for complex, volatile data like crypto.
* The current design is scalable for additional models or data sources.


---

