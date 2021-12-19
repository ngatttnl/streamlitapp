import streamlit as st
import pandas as pd
from apps import cryptofunc

def app():
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

    st.markdown("""
  <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
    <a class="navbar-brand" href="https://thanhnga.herokuapp.com" target="_blank">Thanh Nga</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://www.youtube.com/channel/UCmcQhRJ6P9kF0cvtrEdDEoQ" target="_blank">YouTube</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://twitter.com/ngattt_tb" target="_blank">Twitter</a>
        </li>
      </ul>
    </div>
  </nav>
  """, unsafe_allow_html=True)

    st.header('**Selected Price**')

    # Load market data from Binance API
    df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

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
    
    