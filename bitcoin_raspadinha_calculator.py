import yfinance as yf
from datetime import datetime, timedelta

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
    
    # Calculate the value of the accumulated Bitcoin at the current price
    current_price = btc_data['Adj Close'].iloc[-1]
    total_value = total_bitcoin * current_price
    
    return total_value

# Step 1: Gather User Inputs
rasp_per_week = int(input("How many Raspadinhas do you buy per week? "))
rasp_cost = float(input("What is the average cost of a Raspadinha? (in Euros) "))
years = int(input("For how many years do you want to calculate? "))

# Step 2: Calculate Total Money Spent
total_spent = rasp_per_week * rasp_cost * 52 * years

# Calculate dates
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today().replace(year=datetime.today().year - years)).strftime('%Y-%m-%d')

# Step 3: Simulate Weekly Investments in Bitcoin
investment_value = calculate_weekly_investment_value(rasp_per_week, rasp_cost, start_date, end_date)

# Display the results
print(f"Total money spent on Raspadinhas over {years} years: €{total_spent:.2f}")
print(f"Potential value if invested in Bitcoin weekly: €{investment_value:.2f}")


