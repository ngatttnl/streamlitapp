import streamlit as st
import streamlit.components.v1 as components
from multiapp import MultiApp
from apps import book, pattern, candlestick, addstock, binancescreener, home, coinmarket, datadownload, crypto, gainer, binanceprice, stocktechnical #, speech, avatar # import your app modules here

app = MultiApp()

# Add all your application here

app.add_app("Learning - Candlestick", candlestick.app)
app.add_app("Learning - Patterns", pattern.app)
app.add_app("VN Stock Screener", home.app)
app.add_app("VN Stock Technical", stocktechnical.app)
app.add_app("VN Stock Gainers / Losers", gainer.app)

app.add_app("Binance Technical", binanceprice.app)
app.add_app("Binance Screener", binancescreener.app)
app.add_app("Add Stock", addstock.app)
app.add_app("Data Download", datadownload.app)
app.add_app("Coin Market", coinmarket.app)
app.add_app("Crypto Tracker", crypto.app)

app.run()


 
    

    
   
    

    