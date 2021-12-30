from enum import auto
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from PIL import Image
from apps.db import view_all, get_stockname



def app():
    #df = pd.read_csv('vnstocks.csv', delimiter=',', header=None, skiprows=1, names=['value','name'])
    #names = df['exchange'].tolist()
    #print(df)
    #df = df.sort_values(by=['name']) 
    df = pd.DataFrame(get_stockname(), columns=['name', 'exchange'])
    df = df.sort_values(by=['name']) 
    stocks = df.set_index(['exchange'])['name'].to_dict()
    
    col01, col02 = st.columns(2)
    with col01:
        stock = st.selectbox('Select', options=stocks, format_func=lambda x:stocks[ x ])
        
    with col02:
        st.write("Click here if the page doesn't refresh")
        btn = st.button("Submit")
    if btn:
        pass

    language = st.session_state.key 
    
    newstock = stock.replace(":", "-")   
    if "HOSE" in stock:
        new_title = '<p style="font-family:sans-serif; color:red; font-size: 20px;">This stock does not have an advanced chart. Sorry for this inconvenience. We will update later...</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        components.html(f"""
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{newstock}/" rel="noopener" target="_blank"><span class="blue-text">{newstock} Price Today</span></a> by TradingView</div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
        {{
        "symbol": "{stock}",
        "width": 500,
        "colorTheme": "light",
        "isTransparent": false,
        "locale": "{language}"
        }}
        </script>
        </div>
        <!-- TradingView Widget END -->
        """, width=520)
    else:
        #chart
       
        components.html(f"""
            <!-- TradingView Widget BEGIN -->
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
        <div id="technical-analysis"></div>
        <div class="tradingview-widget-copyright"><a href="https://in.tradingview.com/symbols/{newstock}/" rel="noopener" target="_blank"><span class="blue-text">{newstock} Chart</span></a> by TradingView</div>
        <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
        <script type="text/javascript">
        new TradingView.widget(
        {{
        "container_id": "technical-analysis",
        "width": "100%",
        "height": 800,
        "symbol": "{stock}",
        "interval": "D",
        "timezone": "exchange",
        "theme": "light",
        "style": "1",
        "toolbar_bg": "#f1f3f6",
        "withdateranges": true,
        "hide_side_toolbar": false,
        "allow_symbol_change": false,
        "save_image": false,
        "studies": [
            "ROC@tv-basicstudies",
            "StochasticRSI@tv-basicstudies",
            "MASimple@tv-basicstudies"
        ],
        "show_popup_button": true,
        "popup_width": "1000",
        "popup_height": "650",
        "locale": "{language}"
        }}
        );
        </script>
        </div>
        <!-- TradingView Widget END -->
    """, height=820)

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
    
        
    
   
    
    


    