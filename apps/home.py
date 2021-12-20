import streamlit as st
from binance.client import Client
import pandas as pd
#from apps import cryptofunc

client = Client()
info = client.get_exchange_info()

def app():
    st.header('**Selected Price**')

    # Load market data from Binance API
    all_pairs = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')
    relev = all_pairs[all_pairs.symbol.str.contains('USDT')]
    
    df = relev[~((relev.symbol.str.contains('UP')) | (relev.symbol.str.contains('DOWN')) | (relev.symbol.str.contains('BEAR')) | (relev.symbol.str.contains('BULL')))]
    
    # Widget (Cryptocurrency selection box) 
    col1_selection = st.selectbox('Crypto', df.symbol, list(df.symbol).index('BTCUSDT') )
    # Custom function for rounding values
    def round_value(input_value):
        if input_value.values > 1:
            a = float(round(input_value, 2))
        else:
            a = float(round(input_value, 8))
        return a

    col1, col2, col3 = st.columns(3)

    # DataFrame of selected Cryptocurrency
    col1_df = df[df.symbol == col1_selection]

    # Apply a custom function to conditionally round values
    col1_price = round_value(col1_df.weightedAvgPrice)
    

    # Select the priceChangePercent column
    col1_percent = f'{float(col1_df.priceChangePercent)}%'
    
    # Create a metrics price box
    col1.metric(col1_selection, col1_price, col1_percent)
    
    st.header('**All Price**')
    st.dataframe(df)
    
    