import os
import yfinance as yf

with open('SqueezeScanner\snp.csv') as f:
    lines = f.read().splitlines()
    for symbol in lines:
        print(symbol)
        data = yf.download(symbol, start="2023-01-30", end="2023-04-04")
        data.to_csv("SqueezeScanner\datasets/{}.csv".format(symbol))