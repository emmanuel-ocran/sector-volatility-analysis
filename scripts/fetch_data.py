# import packages
import yfinance as yf
import pandas as pd
import os

# Sector to ticker mapping
sector_tickers = {
    "Technology": ["AAPL", "MSFT", "NVDA", "AMD"],
    "Energy": ["XOM", "CVX", "COP", "HAL"],
    "Healthcare": ["JNJ", "PFE", "UNH", "MRK"],
    "Financials": ["JPM", "BAC", "WFC", "GS"],
    "Consumer Discretionary": ["AMZN", "TSLA", "HD", "MCD"],
    "Utilities": ["NEE", "DUK", "SO", "AEP"]
}

# Date range
start_date = "2018-06-01"
end_date = "2025-06-01"

# Function to download 
def download_and_save_sector_data(sector_name, tickers, output_dir="data"):
    print(f"Fetching data for {sector_name}...")

    try:
        df = yf.download(tickers, start=start_date, end=end_date, progress=False,  auto_adjust=False)

        # If multiple tickers, extract 'Adj Close' from MultiIndex
        if isinstance(df.columns, pd.MultiIndex):
            df = df['Adj Close']
        else:
            df = df[['Adj Close']].rename(columns={'Adj Close': tickers[0]})

        # Reshape and add sector column
        df = df.reset_index().melt(id_vars='Date', var_name='Ticker', value_name='Close')
        df['Sector'] = sector_name

        # Save
        os.makedirs(output_dir, exist_ok=True)
        filename = f"{sector_name.lower().replace(' ', '_')}.csv"
        df.to_csv(os.path.join(output_dir, filename), index=False)

        print(f"Saved to: {filename}")
    except Exception as e:
        print(f" {sector_name}: {e}")

# Function to run batch download
def run_batch_download():
    for sector, tickers in sector_tickers.items():
        download_and_save_sector_data(sector, tickers)

# Fetch data for each sector
run_batch_download()