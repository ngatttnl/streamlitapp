import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from PIL import Image
from multiapp import MultiApp


def app():
    
    CHOICES = {"HNX:KLF": "HNX: KLF", "HOSE:AMD": "HOSE: AMD", "HOSE:MHC": "HOSE: MHC", "HNX:NBC": "HNX: NBC",
        "UPCOM:SBS": "UPCOM: SBS", "HOSE:ROS": "HOSE: ROS", "HOSE:TCH": "HOSE: TCH", "HOSE:TTB": "HOSE: TTB",
        "HOSE:PVT": "HOSE: PVT", "HOSE:QBS": "HOSE: QBS"}
    
    col01, col02 = st.columns(2)
    with col01:
        stock = st.selectbox("Select stock", CHOICES.keys(), format_func=lambda x:CHOICES[ x ])
    
    
    with col02:
        st.write("Click here if the page doesn't refresh")
        btn = st.button("Submit")
    if btn:
        pass

    language = st.session_state.key 
    
    newstock = stock.replace(":", "-")   

    col11, col12 = st.columns(2)
    with col11:
        #Symbol Info
        components.html(f"""
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{newstock}/" rel="noopener" target="_blank"><span class="blue-text">{newstock} Price Today</span></a> by TradingView</div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js" async>
        {{
        "symbol": "{stock}",
        "width": 500,
        "locale": "{language}",
        "colorTheme": "light",
        "isTransparent": false
        }}
        </script>
        </div>
        <!-- TradingView Widget END -->
            """, width=510, height=300)
        
    with col12:
        #Symbol Info
        components.html(f"""
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{newstock}/" rel="noopener" target="_blank"><span class="blue-text">{newstock} Quotes</span></a> by TradingView</div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
        {{
        "symbol": "{stock}",
        "width": 450,
        "height": 270,
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

    col21, col22 = st.columns(2)
    #Technical
    with col21:
        technical = components.html(f"""
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{newstock}/technicals/" rel="noopener" target="_blank"><span class="blue-text">Technical Analysis for {stock}</span></a> by TradingView</div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
        {{
        "interval": "1D",
        "width": "100%",
        "isTransparent": false,
        "height": "500",
        "symbol": "{stock}",
        "showIntervalTabs": true,
        "locale": "{language}",
        "colorTheme": "light"
        }}
        </script>
        </div>
        <!-- TradingView Widget END -->
        """, width=600, height=520)
    with col22:
        #company info
        company = components.html(f"""
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{newstock}/" rel="noopener" target="_blank"><span class="blue-text">{newstock} Profile</span></a> by TradingView</div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-profile.js" async>
        {{
        "symbol": "{stock}",
        "width": 480,
        "height": 500,
        "colorTheme": "light",
        "isTransparent": false,
        "locale": "{language}"
        }}
        </script>
        </div>
        <!-- TradingView Widget END -->
            """, width=500, height=520)
   
    
    


    