import requests
import pandas as pd
from datetime import datetime
from config import connect_sheet

# ==========================================================
# Configuration
# ==========================================================

# Official CoinGecko IDs for the selected cryptocurrencies
ALLOWED_COINS = {
    "bitcoin",
    "ethereum",
    "tether",
    "ripple",       # XRP
    "binancecoin",  # BNB
    "usd-coin",     # USDC
    "solana"
}


# ==========================================================
# Data Fetching and Processing
# ==========================================================

def get_crypto_data():
    """
    Fetches cryptocurrency market data from the CoinGecko API,
    filters only the selected assets,
    cleans and formats the data using Pandas,
    and returns a ready-to-use DataFrame.
    """

    # CoinGecko public API endpoint for market snapshots
    url = "https://api.coingecko.com/api/v3/coins/markets"

    # API request parameters
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,  # Fetch more than needed to guarantee coverage
        "page": 1
    }

    # Send request to CoinGecko
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    # Convert API response to DataFrame
    df = pd.DataFrame(data)

    # Filter only the allowed cryptocurrencies using official IDs
    df = df[df["id"].isin(ALLOWED_COINS)]

    # Select relevant columns for reporting
    df = df[
        [
            "name",
            "symbol",
            "current_price",
            "market_cap",
            "price_change_percentage_24h"
        ]
    ]

    # Rename columns to business-friendly labels
    df.columns = [
        "Asset",
        "Symbol",
        "Price (USD)",
        "Market Cap (USD)",
        "24h Change (%)"
    ]

    # Data cleaning and standardization
    df["Asset"] = df["Asset"].str.title()
    df["Symbol"] = df["Symbol"].str.upper()

    df["Price (USD)"] = df["Price (USD)"].round(2)
    df["Market Cap (USD)"] = df["Market Cap (USD)"].astype(int)
    df["24h Change (%)"] = df["24h Change (%)"].round(2)

    # Add timestamp to track data refresh time
    df["Last Update"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Sort data by market capitalization (descending)
    df = df.sort_values(by="Market Cap (USD)", ascending=False)

    return df


# ==========================================================
# Google Sheets Update Logic
# ==========================================================

def update_sheet():
    """
    Updates Google Sheets with:
    - A Summary tab containing the latest market snapshot
    - A History tab that stores all historical updates (append-only)
    """

    # Connect to Google Sheets using service account credentials
    base_sheet = connect_sheet()
    spreadsheet = base_sheet.spreadsheet

    # Fetch and prepare cryptocurrency data
    df = get_crypto_data()

    # -------------------------------
    # HISTORY WORKSHEET (Append-only)
    # -------------------------------
    try:
        history_ws = spreadsheet.worksheet("History")
    except:
        # Create History worksheet if it does not exist
        history_ws = spreadsheet.add_worksheet(
            title="History",
            rows="1000",
            cols="20"
        )
        # Add header row
        history_ws.append_row(df.columns.tolist())

    # Append each row to preserve historical tracking
    for _, row in df.iterrows():
        history_ws.append_row(row.tolist())

    # -------------------------------
    # SUMMARY WORKSHEET (Overwrite)
    # -------------------------------
    try:
        summary_ws = spreadsheet.worksheet("Summary")
    except:
        # Create Summary worksheet if it does not exist
        summary_ws = spreadsheet.add_worksheet(
            title="Summary",
            rows="100",
            cols="20"
        )

    # Clear and overwrite summary with the latest snapshot
    summary_ws.clear()
    summary_ws.append_row(df.columns.tolist())
    summary_ws.append_rows(df.values.tolist())

    print("✅ Google Sheets updated successfully with filtered crypto data")


# ==========================================================
# Script Entry Point
# ==========================================================

if __name__ == "__main__":
    update_sheet()
