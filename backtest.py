import yfinance as yf
from datetime import datetime

# Function to fetch historical Bitcoin data on a weekly basis
def fetch_weekly_bitcoin_data(start_date, end_date):
    # Download weekly historical Bitcoin data from Yahoo Finance
    btc_data = yf.download('BTC-USD', start=start_date, end=end_date, interval='1wk')
    return btc_data

# Function to simulate weekly investments in Bitcoin
def calculate_weekly_investment_value(rasp_per_week, rasp_cost, start_date, end_date):
    # Fetch weekly Bitcoin data
    btc_data = fetch_weekly_bitcoin_data(start_date, end_date)
    
    total_bitcoin = 0.0
    weekly_investment = rasp_per_week * rasp_cost
    
    # Loop through each week and simulate the purchase of Bitcoin
    for index, row in btc_data.iterrows():
        weekly_bitcoin_bought = weekly_investment / row['Adj Close']
        total_bitcoin += weekly_bitcoin_bought
        print(f"Week: {index.date()}, Price: {row['Adj Close']:.2f}, Bitcoin Bought: {weekly_bitcoin_bought:.6f}, Total Bitcoin: {total_bitcoin:.6f}")
    
    # Calculate the value of the accumulated Bitcoin at the current price
    current_price = btc_data['Adj Close'].iloc[-1]
    total_value = total_bitcoin * current_price
    
    print(f"\nTotal Bitcoin Accumulated: {total_bitcoin:.6f} BTC")
    print(f"Current Bitcoin Price: €{current_price:.2f}")
    print(f"Total Value of Investment: €{total_value:.2f}")
    
    return total_value

# Inputs for Backtesting
rasp_per_week = 4  # Number of Raspadinhas per week
rasp_cost = 5      # Average cost per Raspadinha (in Euros)
years = 1          # Number of years

# Calculate dates
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today().replace(year=datetime.today().year - years)).strftime('%Y-%m-%d')

# Run the backtest
investment_value = calculate_weekly_investment_value(rasp_per_week, rasp_cost, start_date, end_date)

# Output the results
print(f"\nTotal money spent on Raspadinhas over {years} years: €{rasp_per_week * rasp_cost * 52 * years:.2f}")
print(f"Potential value if invested in Bitcoin: €{investment_value:.2f}")
