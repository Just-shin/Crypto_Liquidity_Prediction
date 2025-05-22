1. 📁 Dataset Overview:
-Shape: (rows, columns)
-Columns:
*  coin, symbol, price, 1h, 24h, 7d, market_cap, 24h_volume, etc.
-Data Types:
*  Mixed types: object, float64, int64

2.  Missing Values:
Checked with df.isnull().sum()
-Imputation Strategy:
*  Numeric columns: Filled with column-wise mean
*  Categorical columns: Assumed to be minimal or dropped

3.  Data Cleaning:
*  Duplicates: Checked with df.duplicated().sum()
*  NaNs: Analyzed and replaced
*  Type conversions: Ensured consistency in numerical fields

4.  Descriptive Statistics:
*  df.describe() showed:
*  Wide variance in market_cap, volume, price
*  Volatility captured in % change columns: 1h, 24h, 7d
*  Feature 24h_volume_log was created using np.log1p() for better scale

5.  Distribution Analysis:
*  Histograms and KDE plots (via seaborn) used to examine:
*  Price distribution (skewed)
*  Volume and market cap (log-normal like)
*  Outliers handled implicitly by log transformations

6.  Correlation Analysis:
*  Pearson correlation heatmap used
*  Strong correlations noted between:
-  market_cap and volume
-  Some volatility measures (1h, 24h, 7d)

7.  Feature Engineering:
*  New columns:
-  24h_volume_log: np.log1p(df["24h_volume"])

*  Scaling:
-  Applied StandardScaler to normalize numerical features

8.  Observations:
*  Some coins like stablecoins (e.g., USDT) showed minimal price change
*  High volatility observed in smaller market-cap coins
*  Consistent patterns in volume vs. market cap correlation
