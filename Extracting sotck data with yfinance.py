pip install yfinance
pip install matplotlib
# !pip install pandas==1.3.3
import yfinance as yf
import pandas as pd

#Using the Ticker module we can create an object that will allow us to access functions to 
#extract data. To do this we need to provide the ticker symbol for the stock, here the 
#company is Apple and the ticker symbol is AAPL.

apple = yf.Ticker("AAPL")

#Now we can access functions and variables to extract the type of data we need. You can view #them and what they represent here https://aroussi.com/post/python-yahoo-finance.

#Using the attribute info we can extract information about the stock as a Python dictionary.

import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
apple_info

#Using the history() method we can get the share price of the stock over a certain period of #time. Using the period parameter we can set how far back from the present to get data. The #options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, #ytd, and max.

apple_share_price_data = apple.history(period="max")

#The format that the data is returned in is a Pandas DataFrame. With the Date as the index #the share Open, High, Low, Close, Volume, and Stock Splits are given for each day.

#We can reset the index of the DataFrame with the reset_index function. We also set the #inplace paramter to True so the change takes place to the DataFrame itself.

apple_share_price_data.reset_index(inplace=True)

#We can plot the Open price against the Date:

apple_share_price_data.plot(x="Date", y="Open")

#Using the variable dividends we can get a dataframe of the data. The period of the data is given by the period defined in the 'history` function.

apple.dividends

#We can plot the dividends overtime:

apple.dividends.plot()
 