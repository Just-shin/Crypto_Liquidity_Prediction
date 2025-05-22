# High-Level Design (HLD)


---

### 🎯 **Objective**

Design a data pipeline to perform **cryptocurrency analysis** using historical CoinGecko data, apply preprocessing, and train regression models to estimate price behavior or trends.

---

###  **System Components**

1. **Data Ingestion Layer**

   * Source: CoinGecko CSV snapshots
   * Manual uploads or automated scheduler (cron/job)

2. **Preprocessing Layer**

   * Handle missing values
   * Clean & standardize data
   * Feature engineering

3. **EDA & Insights Layer**

   * Data profiling (EDA scripts)
   * Visualization: Seaborn, Matplotlib

4. **Modeling Layer**

   * Train/Test split
   * ML Models:

     * Linear Regression
     * Random Forest Regressor
   * Evaluation: RMSE, MAE, R²

5. **Output Layer**

   * Store results (CSV, JSON, or DB)
   * Generate visual insights
   * Optionally serve as a dashboard (Streamlit)

---

### 🔄 Data Flow

```plaintext
[CSV Files] → [Data Cleaning] → [EDA & Stats] → [ML Model Training] → [Evaluation] → [Output Reports]
```

---

