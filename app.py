import streamlit as st
from multiapp import MultiApp
from apps import binancescreener, home, coinmarket, datadownload, crypto, gainer, mlapp, themes, modelper, binanceprice, stocktechnical #, speech, avatar # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Stock Technical", stocktechnical.app)
app.add_app("Vietnamese Stocks", home.app)
app.add_app("Gainers / Losers", gainer.app)

app.add_app("Binance Price", binanceprice.app)
app.add_app("Binance Screener", binancescreener.app)
app.add_app("Data Download", datadownload.app)
app.add_app("Coin Market", coinmarket.app)
app.add_app("Crypto Tracker", crypto.app)




# The main app
app.run()