import streamlit as st
from binance.client import Client
import pandas as pd
import streamlit.components.v1 as components
from PIL import Image
#from apps import cryptofunc

client = Client()
info = client.get_exchange_info()

def app():
    st.header('**Selected Price**')

   
    # Widget (Cryptocurrency selection box) 
    
    stocklist = {"HOSE:AMD", "HOSE:KLF"}
    CHOICES = {"HOSE:AMD": "HOSE: AMD", "HNX:KLF": "HNX: KLF", "HOSE:ROS": "HOSE: ROS"}
    stock = st.selectbox("Select option", CHOICES.keys(), format_func=lambda x:CHOICES[ x ])
    
    #chart
    html_str = f"""
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
    <div class="tradingview-widget-container__widget"></div>
    <div class="tradingview-widget-copyright"><span class="blue-text">Technical Analysis for {stock}</span> by TradingView</div>
    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
    {{
    "interval": "1D",
    "width": "100%",
    "isTransparent": false,
    "height": "600",
    "symbol": "{stock}",
    "showIntervalTabs": true,
    "locale": "en",
    "colorTheme": "light"
    }}
    </script>
    </div>
    <!-- TradingView Widget END -->
    """
    components.html(html_str, height=620)

    html_str1 = f"""
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
    <div class="tradingview-widget-container__widget"></div>
    <div class="tradingview-widget-copyright"><span class="blue-text">{stock} Price Today</span> by TradingView</div>
    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
    {{
    "symbol": "{stock}",
    "width": "100%",
    "colorTheme": "light",
    "isTransparent": false,
    "locale": "en"
    }}
    </script>
    </div>
    <!-- TradingView Widget END -->
    """

    components.html(html_str1)

    html_str2 = f"""
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
    <div id="tradingview_1934a"></div>
    <div class="tradingview-widget-copyright"><span class="blue-text">{stock} Chart</span> by TradingView</div>
    <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
    <script type="text/javascript">
    new TradingView.MediumWidget(
    {{
    "symbols": [
        [
        "{stock}|12M"
        ]
    ],
    "chartOnly": false,
    "width": 1000,
    "height": 400,
    "locale": "en",
    "colorTheme": "light",
    "gridLineColor": "rgba(240, 243, 250, 0)",
    "fontColor": "#787B86",
    "isTransparent": false,
    "autosize": false,
    "showFloatingTooltip": true,
    "showVolume": false,
    "scalePosition": "no",
    "scaleMode": "Normal",
    "fontFamily": "Trebuchet MS, sans-serif",
    "noTimeScale": false,
    "chartType": "area",
    "lineColor": "#2962FF",
    "bottomColor": "rgba(41, 98, 255, 0)",
    "topColor": "rgba(41, 98, 255, 0.3)",
    "container_id": "tradingview_1934a"
    }}
    );
    </script>
    </div>
    <!-- TradingView Widget END -->
    """

    components.html(html_str2, height=420)#

    