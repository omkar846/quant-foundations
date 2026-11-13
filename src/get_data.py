
from pathlib import Path
import pandas as pd
import yfinance as yf

# Locate the project's data folder
DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(exist_ok=True)

# Download NIFTY 50 daily prices
df = yf.download(
    "^NSEI",
    start="2010-01-01",
    auto_adjust=False,
    progress=False
)

# Check whether data was downloaded
if df.empty:
    raise ValueError("No data downloaded. Check the ticker or connection.")

# Handle possible multi-level column names
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

# Keep closing prices
prices = df[["Close"]].dropna().reset_index()

# Standardise column names
prices = prices.rename(columns={
    "Date": "date",
    "Close": "close"
})

# Save raw data
output_file = DATA_DIR / "nifty50.csv"
prices.to_csv(output_file, index=False)

print("Rows downloaded:", len(prices))
print("First date:", prices["date"].min())
print("Last date:", prices["date"].max())
print("Saved to:", output_file)
