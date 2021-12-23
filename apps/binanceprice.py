import streamlit as st
from binance.client import Client
import pandas as pd
import streamlit.components.v1 as components
from PIL import Image
#from apps import cryptofunc

client = Client()
info = client.get_exchange_info()

def app():
    language = st.session_state.key 
    
    # Load market data from Binance API
    all_pairs = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')
    relev = all_pairs[all_pairs.symbol.str.contains('USDT')]
    
    df = relev[~((relev.symbol.str.contains('UP')) | (relev.symbol.str.contains('DOWN')) | (relev.symbol.str.contains('BEAR')) | (relev.symbol.str.contains('BULL')))]
    
    col0, col1= st.columns(2)
    with col0:
    # Widget (Cryptocurrency selection box) 
        crypto = st.selectbox('Crypto', df.symbol, list(df.symbol).index('BTCUSDT') )
    
    #chart
    components.html(f"""
    <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
        <div id="tradingview_fe4a9"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{crypto}/?exchange=BINANCE" rel="noopener" target="_blank"><span class="blue-text">{crypto} Chart</span></a> by TradingView</div>
        <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
        <script type="text/javascript">
        new TradingView.widget(
            {{
            "width": 980,
            "height": 610,
            "symbol": "BINANCE:{crypto}",
            "interval": "D",
            "timezone": "Etc/UTC",
            "theme": "light",
            "style": "1",
            "locale": "{language}",
            "toolbar_bg": "#f1f3f6",
            "enable_publishing": false,
            "allow_symbol_change": false,
            "container_id": "tradingview_fe4a9"
            }}
        );
        </script>
        </div>
        <!-- TradingView Widget END -->
    """, height=630)
    
    col11, col12 = st.columns(2)
    with col11:
        #technical
        components.html(f"""
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{crypto}/technicals/" rel="noopener" target="_blank"><span class="blue-text">Technical Analysis for {crypto}</span></a> by TradingView</div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
        {{
        "interval": "1D",
        "width": "100%",
        "isTransparent": false,
        "height": "480",
        "symbol": "BINANCE:{crypto}",
        "showIntervalTabs": true,
        "locale": "{language}",
        "colorTheme": "light"
        }}
        </script>
        </div>
        <!-- TradingView Widget END -->
        """, width=510, height=490)
    
        #Symbol Info
        components.html(f"""
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{crypto}/" rel="noopener" target="_blank"><span class="blue-text">{crypto} Quotes</span></a> by TradingView</div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
        {{
        "symbol": "BINANCE:{crypto}",
        "width": 500,
        "height": 290,
        "locale": "{language}",
        "dateRange": "12M",
        "colorTheme": "light",
        "trendLineColor": "rgba(41, 98, 255, 1)",
        "underLineColor": "rgba(41, 98, 255, 0.3)",
        "underLineBottomColor": "rgba(41, 98, 255, 0)",
        "isTransparent": false,
        "autosize": false,
        "largeChartUrl": ""
        }}
        </script>
        </div>
        <!-- TradingView Widget END -->
            """, width=510, height=300)
        
    with col12:
        components.html(f"""
    <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{crypto}/financials-overview/" rel="noopener" target="_blank"><span class="blue-text">{crypto} Fundamental Data</span></a> by TradingView</div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-financials.js" async>
        {{
        "symbol": "BINANCE:{crypto}",
        "colorTheme": "light",
        "isTransparent": false,
        "largeChartUrl": "",
        "displayMode": "regular",
        "width": 500,
        "height": 800,
        "locale": "{language}"
        }}
        </script>
        </div>
        <!-- TradingView Widget END -->
            """, width=510, height=810)
        

    col21, col22 = st.columns(2)
    #Symbol Overview Widget
    company = components.html(f"""
    <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
        <div id="tradingview_a9bd3"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{crypto}/?exchange=BINANCE" rel="noopener" target="_blank"><span class="blue-text">{crypto} Chart</span></a> by TradingView</div>
        <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
        <script type="text/javascript">
        new TradingView.MediumWidget(
        {{
        "symbols": [
            [
            "{crypto}|12M"
            ]
        ],
        "chartOnly": false,
        "width": 1100,
        "height": 400,
        "locale": "{language}",
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
        "container_id": "tradingview_a9bd3"
        }}
        );
        </script>
        </div>
        <!-- TradingView Widget END -->
        """, width=1200, height=400)


    