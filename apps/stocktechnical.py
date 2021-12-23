import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from PIL import Image



def app():
    
    CHOICES = {  
        "HNX:ART": "ART (HNX)", "HNX:DST": "DST (HNX)", "HNX:KLF": "KLF (HNX)", "HNX:NBC": "NBC (HNX)",
        "UPCOM:ABB": "ABB (UPCOM)", "UPCOM:BSR": "BSR (UPCOM)", "UPCOM:DPS": "DPS (UPCOM)", "UPCOM:SBS": "SBS (UPCOM)", "UPCOM:S12": "S12 (UPCOM)", 
        "HOSE:AAA": "AAA (HOSE)", "HOSE:ACB": "ACB (HOSE)", "HOSE:TCB": "TCB (HOSE)",
        "HOSE:HPG": "HPG (HOSE)", "HOSE:NKG": "NKG (HOSE)", 
        "HOSE:FPT": "FPT (HOSE)", "HOSE:MHC": "MHC (HOSE)",
        "HOSE:AMD": "AMD (HOSE)", "HOSE:HAI": "HAI (HOSE)", "HOSE:ROS": "ROS (HOSE)", "HOSE:TCH": "TCH (HOSE)", "HOSE:TTB": "TTB (HOSE)",
        "HOSE:PVD": "PVD (HOSE)", "HOSE:PVT": "PVT (HOSE)", "HOSE:QBS": "QBS (HOSE)"}
    
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
        #technical
        components.html(f"""
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{newstock}/technicals/" rel="noopener" target="_blank"><span class="blue-text">Technical Analysis for {stock}</span></a> by TradingView</div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
        {{
        "interval": "1D",
        "width": "100%",
        "isTransparent": false,
        "height": "480",
        "symbol": "{stock}",
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
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{newstock}/" rel="noopener" target="_blank"><span class="blue-text">{newstock} Quotes</span></a> by TradingView</div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
        {{
        "symbol": "{stock}",
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
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{newstock}/financials-overview/" rel="noopener" target="_blank"><span class="blue-text">{newstock} Fundamental Data</span></a> by TradingView</div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-financials.js" async>
        {{
        "symbol": "{stock}",
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
    #Technical
    with col21:
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
            """, width=510, height=460)
    with col22:
        #company profile
        company = components.html(f"""
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{newstock}/" rel="noopener" target="_blank"><span class="blue-text">{newstock} Profile</span></a> by TradingView</div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-profile.js" async>
        {{
        "symbol": "{stock}",
        "width": 500,
        "height": 310,
        "colorTheme": "light",
        "isTransparent": false,
        "locale": "{language}"
        }}
        </script>
        </div>
        <!-- TradingView Widget END -->
            """, width=510, height=310)
        
    
   
    
    


    