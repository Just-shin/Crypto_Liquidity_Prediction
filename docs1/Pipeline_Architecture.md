# Pipeline Architecture

###  **Model Pipeline**

```python
# Example Flow
df = load_data("coin_gecko_2022-03-16.csv")
df_clean = clean_data(df)
df_feat = feature_engineering(df_clean)
X_train, X_test, y_train, y_test = train_test_split(...)
model = RandomForestRegressor().fit(X_train, y_train)
metrics = evaluate_model(model, X_test, y_test)
```

---

### 🧱 Technologies

* Language: Python
* Libraries: pandas, sklearn, seaborn, matplotlib
* Optional:

  * Pipeline: `scikit-learn Pipeline` (for automation)
  * Deployment: Streamlit for front-end display

---

## 🧩 Pipeline Architecture Diagram (Textual)

```
                        ┌────────────────────┐
                        │   CoinGecko CSVs   │
                        └────────┬───────────┘
                                 │
                     ┌───────────▼────────────┐
                     │     Data Cleaning      │
                     └───────────┬────────────┘
                                 │
                    ┌────────────▼─────────────┐
                    │ Feature Engineering & EDA│
                    └────────────┬─────────────┘
                                 │
                     ┌───────────▼───────────┐
                     │  ML Model Training    │
                     └───────────┬───────────┘
                                 │
                    ┌────────────▼────────────┐
                    │   Evaluation & Results  │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │ Export / Visualization  │
                    └─────────────────────────┘
```

---

