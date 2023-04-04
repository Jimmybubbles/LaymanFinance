import os
import pandas as pd

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame

from sqlalchemy import create_engine

#alpaca keys

# Create a database engine
db_engine = create_engine('')