import requests

API_KEY = "994YASJB7J9YEJUG" #get api key

api_url="https://www.alphavantage.co/" #get api url


def get_stock_market_data(symbol,is_timeseries):

    query=f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

    response=requests.get(api_url+query)
    data=response.json()

    # Check if API returned valid stock data
    if "Time Series (Daily)" not in data and "Meta Data" not in data:
        print("Invalid stock symbol. Please enter a valid one like IBM, AMZN, GOOGL.")
        return
    
    for key,value in data.items():
        if is_timeseries:   
            print(key,value)
        else:
            if key == "Time Series (Daily)":
                continue
            print(key,value)


symbol=input("Enter the symbol of the company for which you want the data(e.g. IBM,AMZN,GOGL etc or lowercases also): ")
is_timeseries=False
get_stock_market_data(symbol,is_timeseries)