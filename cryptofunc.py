from typing import Counter
from numpy import array, percentile
import pandas as pd
from binance.client import Client
import csv
from django.http import JsonResponse
import ccxt
import pandas_ta as ta

from datetime import date, datetime
from django.utils import timezone

client = Client()
info = client.get_exchange_info()

coins = ['BAKEUSDT', 'ADAUSDT', 'BATUSDT', 'BTCUSDT', 'BTTUSDT', 'ENJUSDT', 'ETHUSDT', 'XRPUSDT', 'NEARUSDT', 'OGNUSDT', 'KAVAUSDT', 'ZILUSDT', 'FTMUSDT', 'WINUSDT']


def get_all_coins():
    all_pairs = pd.DataFrame(client.get_ticker())
    all_pairs['priceChangePercent'] = all_pairs['priceChangePercent'].astype(float)
    relev = all_pairs[all_pairs.symbol.str.contains('USDT')]
    
    non_lev = relev[~((relev.symbol.str.contains('UP')) | (relev.symbol.str.contains('DOWN')) | (relev.symbol.str.contains('BEAR')) | (relev.symbol.str.contains('BULL')))]
    
    df = pd.DataFrame(non_lev)
    return df
    


def get_indicators(inputSymbol): 
    symbol = inputSymbol[0:(len(inputSymbol) - 4)] + "/USDT"
    price = 0
    try:
        exchange = ccxt.binance()
        bars = exchange.fetch_ohlcv(symbol, timeframe='1d', limit=500)
        df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])

        adx = df.ta.adx()
        macd = df.ta.macd(fast=14, slow=28)
        rsi = df.ta.rsi()

        df = pd.concat([df, adx, macd, rsi], axis=1)
        last_row = df.iloc[-1]
        
        if last_row['ADX_14'] >= 25:
            if last_row['DMP_14'] > last_row['DMN_14']:
                message = f"UPTREND: RSI = {last_row['RSI_14']:.2f}, ADX = {last_row['ADX_14']:.2f}"
            if last_row['DMN_14'] > last_row['DMP_14']:
                message = f"DOWNTREND: RSI = {last_row['RSI_14']:.2f}, ADX = {last_row['ADX_14']:.2f}"

        if last_row['ADX_14'] < 25:
            message = f"SIDEWAY: RSI = {last_row['RSI_14']:.2f}, ADX = {last_row['ADX_14']:.2f}"
        price = last_row['close']
    except:
        price = 0
        message= "Not enough data for indicators"
    
    return message


def coinstream():
    # prices = client.get_all_tickers()

    # for price in prices:
    #     print(price)

    csvfile = open('2020_15minutes.csv', 'w', newline='') 
    candlestick_writer = csv.writer(csvfile, delimiter=',')

    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2020", "12 Jul, 2020")
    #candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2020", "12 Jul, 2020")
    #candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2017", "12 Jul, 2020")

    for candlestick in  candlesticks:
        candlestick[0] = candlestick[0] / 1000
        candlestick_writer.writerow(candlestick)
    csvfile.close()

def get_top_symbol():
    all_pairs = pd.DataFrame(client.get_ticker())
    all_pairs['priceChangePercent'] = all_pairs['priceChangePercent'].astype(float)
    relev = all_pairs[all_pairs.symbol.str.contains('USDT')]
    non_lev = relev[~((relev.symbol.str.contains('UP')) | (relev.symbol.str.contains('DOWN')))]
    top_symbol = non_lev[non_lev.priceChangePercent == non_lev.priceChangePercent.max()]
    top_symbol = top_symbol.symbol.values[0]
    return top_symbol

def get_top_symbols():
    all_pairs = pd.DataFrame(client.get_ticker())
    all_pairs['priceChangePercent'] = all_pairs['priceChangePercent'].astype(float)
    relev = all_pairs[all_pairs.symbol.str.contains('USDT')]
    
    non_lev = relev[~((relev.symbol.str.contains('UP')) | (relev.symbol.str.contains('DOWN')))]
    top_symbol = non_lev[non_lev.priceChangePercent > 10]
    df = pd.DataFrame(top_symbol)
    symbols = df['symbol'].astype(str).values.flatten().tolist()
    return symbols
    
def get_top_coins():
    all_pairs = pd.DataFrame(client.get_ticker())
    all_pairs['priceChangePercent'] = all_pairs['priceChangePercent'].astype(float)
    relev = all_pairs[all_pairs.symbol.str.contains('USDT')]
    
    non_lev = relev[~((relev.symbol.str.contains('UP')) | (relev.symbol.str.contains('DOWN')))]
    top_symbol = non_lev[non_lev.priceChangePercent > 10]
    
    df = pd.DataFrame(top_symbol)
    df = df.loc[:, ['symbol', 'priceChangePercent', 'lastPrice' ]]
    df.sort_values(by=['priceChangePercent'], inplace=True, ascending=False)
    return df
def get_all_mycoins():
    coins = ['ADAUSDT', 'BATUSDT', 'BTCUSDT', 'BTTUSDT', 'ENJUSDT', 'ETHUSDT', 'XRPUSDT', 'NEARUSDT', 'OGNUSDT', 'KAVAUSDT', 'ZILUSDT', 'FTMUSDT', 'WINUSDT']
    
    klines={}
    
    returns, symbols, prices = [], [], []

    for symbol in coins:
        frame = pd.DataFrame(client.get_historical_klines(symbol, '1m', '120 min ago UTC'))
        price = frame[4].astype(float)[0]
        
        cumret = ((frame[4].astype(float).pct_change() + 1).cumprod()).iloc[-1] 
        is_buy = False
        if cumret > 1:
            is_buy = True
        
        prices.append(price)
        returns.append(is_buy)
        symbols.append(symbol)
    d = {'symbol': symbols, 'price': prices, 'ret': returns}
    retdf = pd.DataFrame(data=d)
    return retdf

def strategy (coin):
    frame = pd.DataFrame(client.get_historical_klines(coin, '1m', '5 m ago UTC'))
    
    is_buy=False
    cumpod = ((frame[4].astype(float).pct_change() + 1).cumprod()).iloc[-1]
    if cumpod > 1:
        is_buy = True
    
    return is_buy

def tr(data):
    data['previous_close'] = data['close'].shift(1)
    data['high-low'] = abs(data['high'] - data['low'])
    data['high-pc'] = abs(data['high'] - data['previous_close'])
    data['low-pc'] = abs(data['low'] - data['previous_close'])

    tr = data[['high-low', 'high-pc', 'low-pc']].max(axis=1)

    return tr

def atr(data, period):
    data['tr'] = tr(data)
    atr = data['tr'].rolling(period).mean()

    return atr

def supertrend(df, period=7, atr_multiplier=3):
    hl2 = (df['high'] + df['low']) / 2
    df['atr'] = atr(df, period)
    df['upperband'] = hl2 + (atr_multiplier * df['atr'])
    df['lowerband'] = hl2 - (atr_multiplier * df['atr'])
    df['in_uptrend'] = True

    for current in range(1, len(df.index)):
        previous = current - 1

        if df['close'][current] > df['upperband'][previous]:
            df['in_uptrend'][current] = True
        elif df['close'][current] < df['lowerband'][previous]:
            df['in_uptrend'][current] = False
        else:
            df['in_uptrend'][current] = df['in_uptrend'][previous]

            if df['in_uptrend'][current] and df['lowerband'][current] < df['lowerband'][previous]:
                df['lowerband'][current] = df['lowerband'][previous]

            if not df['in_uptrend'][current] and df['upperband'][current] > df['upperband'][previous]:
                df['upperband'][current] = df['upperband'][previous]
        
    return df