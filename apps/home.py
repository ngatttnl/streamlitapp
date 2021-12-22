import streamlit as st
from binance.client import Client
import pandas as pd
import streamlit.components.v1 as components
from PIL import Image
#from apps import cryptofunc

client = Client()
info = client.get_exchange_info()

def app():
    
    st.title('Vietnamese stocks')
    components.html(f"""
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
    <div class="tradingview-widget-container__widget"></div>
    <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/screener/" rel="noopener" target="_blank"><span class="blue-text">Stock Screener</span></a> by TradingView</div>
    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-screener.js" async>
    {{
    "width": 1100,
    "height": 700,
    "defaultColumn": "overview",
    "defaultScreen": "most_capitalized",
    "market": "vietnam",
    "showToolbar": true,
    "colorTheme": "light",
    "locale": "en"
    }}
    </script>
    </div>
    <!-- TradingView Widget END -->
    """, height=720)

    image = Image.open('invest.png')   
    st.image(image, width = 500)
    st.title('Loading...')
    placeholder1 = st.empty()
    placeholder1.warning("I am learning to make a system for trading Vietnamese stocks and cryptos on Binance. Please come back later for many more features")
  

    

    