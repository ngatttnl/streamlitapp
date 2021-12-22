import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
#from apps import cryptofunc

def app():
    st.title('Vietnamese stocks')
    language = st.session_state.key 
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
    "locale": "{language}"
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
  

    

    