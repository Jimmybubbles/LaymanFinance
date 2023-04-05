import pandas as pd
import config

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame

from sqlalchemy import create_engine


#alpaca keys
APIKEY = config.API_KEY
APISECRET = config.SECRET_KEY

# Create a database engine
db_engine = create_engine('sqlite:///C:/sqlite/layman.db', echo=False)

# Create a data client to fetch historical data
data_client = StockHistoricalDataClient(APIKEY, APISECRET)

# Set Parameters this is where you need to loop through the symbols list

symbols=['OPRA']


start_date = pd.to_datetime("2022-01-01").tz_localize('America/New_York')

request_parameters = StockBarsRequest(
    symbol_or_symbols=symbols,
    timeframe=TimeFrame.Day,
    start=start_date,
    end=None,
    adjustment="raw"
)

# Fetch data and convert it to a dataframe
daily_bars = data_client.get_stock_bars(request_parameters).df

# Set option for row display - want to see all the row data.
# pd.set_option('display.max_rows', None)

# None will show all rows


print(daily_bars)

# Have to get the stock data into a sqldb next.

# # Write dataframe to sql db (name the db daily_data)
daily_bars.to_sql('daily_data', con=db_engine)

# # Verify the columns/keys which were created
db_engine.execute("SELECT * FROM daily_data").keys()

# # Read database to see if it worked
db_engine.execute("SELECT * FROM daily_data").fetchall()



