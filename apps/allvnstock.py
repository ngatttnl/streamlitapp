import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from PIL import Image


def app():
    components.html(f"""
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
    <div class="tradingview-widget-container__widget"></div>
    <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/screener/" rel="noopener" target="_blank"><span class="blue-text">Stock Screener</span></a> by TradingView</div>
    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-screener.js" async>
    {{
    "width": 1100,
    "height": 523,
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
    """, height=530)


    