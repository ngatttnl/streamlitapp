
import streamlit as st
import streamlit.components.v1 as components


def app():
    language = st.session_state.key 
    components.html(f"""
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
    <div class="tradingview-widget-container__widget"></div>
    <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/crypto-screener/" rel="noopener" target="_blank"><span class="blue-text">Crypto Screener</span></a> by TradingView</div>
    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-screener.js" async>
    {{
    "width": 1100,
    "height": 700,
    "defaultColumn": "overview",
    "defaultScreen": "general",
    "market": "crypto",
    "showToolbar": true,
    "colorTheme": "light",
    "locale": "{language}"
    }}
    </script>
    </div>
    <!-- TradingView Widget END -->
    """, height=720)

    
    

    

