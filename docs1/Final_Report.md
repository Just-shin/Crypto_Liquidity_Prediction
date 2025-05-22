# Final Report

## Summary of Findings
The most important features affecting liquidity were:
- Price volatility.
- Liquidity prediction is strongly correlated with [e.g., 24h volume and price volatility].

## Model Performance
- Best Model: [RandomForestRegressor]
- Metrics:
  - MAE: [0.0374]
  - RMSE: [0.1681]
  - R² Score: [0.7706]
  - Tuned R² Score: [0.8069167158009142]

## Key Insights
- Liquidity is influenced by volatility and trading volume.
- The model is sensitive to anomalies, so future work should explore drift detection.
