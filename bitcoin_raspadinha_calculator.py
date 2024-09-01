from flask import Flask, render_template, request, jsonify
import yfinance as yf
from datetime import datetime

app = Flask(__name__)

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
    
    return total_bitcoin, total_value

# Home route to serve the main page
@app.route('/')
def index():
    return render_template('index.html')

# API route to calculate the potential investment value
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()  # Get the JSON data from the request
    rasp_per_week = int(data['raspPerWeek'])
    rasp_cost = float(data['raspCost'])
    years = int(data['years'])

    # Calculate total money spent
    total_spent = rasp_per_week * rasp_cost * 52 * years
    print(f"Total money spent: €{total_spent}")

    # Calculate dates
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today().replace(year=datetime.today().year - years)).strftime('%Y-%m-%d')
    print(f"Start Date: {start_date}, End Date: {end_date}")

    # Simulate weekly investments in Bitcoin
    total_bitcoin, investment_value = calculate_weekly_investment_value(rasp_per_week, rasp_cost, start_date, end_date)
    print(f"Calculated Investment Value: €{investment_value}")
    print(f"Total Bitcoin Accumulated: {total_bitcoin} BTC")

    # Print the results to the terminal
    print(f"\n--- Calculation Results ---")
    print(f"Total money spent on Raspadinhas: €{total_spent:.2f}")
    print(f"Total Bitcoin accumulated: {total_bitcoin:.6f} BTC")
    print(f"Potential value if invested in Bitcoin: €{investment_value:.2f}")
    print(f"----------------------------\n")

    # Return the results as a JSON response
    return jsonify({
        'totalSpent': total_spent,
        'investmentValue': investment_value,
        'totalBitcoin': total_bitcoin
    })

if __name__ == '__main__':
    app.run(debug=True)

