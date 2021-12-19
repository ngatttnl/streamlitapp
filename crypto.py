import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import plotly.express as px

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
    crypto_mapping = {"Bitcoin": "BTC-USD", "Ethereum": "ETH-USD"}

    st.title("Crypto Tracker")
    crypto_option = st.sidebar.selectbox(
        "Which Crypto do you want to visualize?", ("Bitcoin", "Ethereum")
    )

    start_date = st.sidebar.date_input("Start Date", date.today() - relativedelta(months=1))
    end_date = st.sidebar.date_input("End Date", date.today())

    data_interval = st.sidebar.selectbox(
        "Data Interval",
        (
            "1m",
            "2m",
            "5m",
            "15m",
            "30m",
            "60m",
            "90m",
            "1h",
            "1d",
            "5d",
            "1wk",
            "1mo",
            "3mo",
        ),
    )

    symbol_crypto = crypto_mapping[crypto_option]
    data_crypto = yf.Ticker(symbol_crypto)

    value_selector = st.sidebar.selectbox(
        "Value Selector", ("Open", "High", "Low", "Close", "Volume")
    )

    if st.sidebar.button("Generate"):
        crypto_hist = data_crypto.history(
            start=start_date, end=end_date, interval=data_interval
        )
        fig = px.line(crypto_hist, 
        x=crypto_hist.index, y=value_selector,
        labels={"x": "Date"})
        st.plotly_chart(fig)