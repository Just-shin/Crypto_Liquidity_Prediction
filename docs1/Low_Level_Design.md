# Low-Level Design (LLD)
---

### 1. **Data Schema (Coin Data)**

| Column      | Type   | Description                      |
| ----------- | ------ | -------------------------------- |
| coin        | string | Coin name                        |
| symbol      | string | Ticker symbol                    |
| price       | float  | Current market price             |
| 1h, 24h, 7d | float  | % price change over time periods |
| market\_cap | float  | Total market cap in USD          |
| 24h\_volume | float  | 24h trading volume               |

---

### 2. **Core Functions & Modules**

| Module             | Function Name           | Description               |
| ------------------ | ----------------------- | ------------------------- |
| `data_loader.py`   | `load_data()`           | Load raw CSVs             |
| `preprocessing.py` | `clean_data()`          | Handle nulls, types, dups |
| `eda.py`           | `generate_eda()`        | Summary stats and plots   |
| `features.py`      | `feature_engineering()` | Scaling, log-transforms   |
| `model.py`         | `train_model()`         | Train ML models           |
| `evaluate.py`      | `evaluate_model()`      | MSE, MAE, R²              |

---

