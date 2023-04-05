import os, pandas
import plotly.graph_objects as go

dataframes = {}

for filename in os.listdir('SqueezeScanner\datasets'):
    #print(filename)
    symbol = filename.split(".")[0]
    #print(symbol)
    df = pandas.read_csv('SqueezeScanner\datasets/{}'.format(filename))
    if df.empty:
        continue

    df['20sma'] = df['Close'].rolling(window=20).mean()
    df['stddev'] = df['Close'].rolling(window=20).std()
    df['lower_band'] = df['20sma'] - (2 * df['stddev'])
    df['upper_band'] = df['20sma'] + (2 * df['stddev'])

    df['TR'] = abs(df['High'] - df['Low'])
    df['ATR'] = df['TR'].rolling(window=20).mean()

    df['lower_keltner'] = df['20sma'] - (df['ATR'] * 1.26)
    df['upper_keltner'] = df['20sma'] + (df['ATR'] * 1.26)

    def in_squeeze(df):
        return df['lower_band'] > df['lower_keltner'] and df['upper_band'] < df['upper_keltner']

    df['squeeze_on'] = df.apply(in_squeeze, axis=1)

    if df.iloc[-3]['squeeze_on'] and not df.iloc[-1]['squeeze_on']:
        print("{} is coming out the squeeze".format(symbol))