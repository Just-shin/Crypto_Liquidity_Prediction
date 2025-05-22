# Pipeline Architecture

```text
Raw Data
   ↓
Preprocessing (scaling, nulls, encoding)
   ↓
Feature Engineering
   ↓
EDA
   ↓
Model Training & Validation
   ↓
Evaluation & Tuning
   ↓
Deployment Interface (Optional)
```
Each module is self-contained and can be iteratively improved.
