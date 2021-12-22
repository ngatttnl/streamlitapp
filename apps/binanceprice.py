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
        col1_selection = st.selectbox('Crypto', df.symbol, list(df.symbol).index('BTCUSDT') )

    # Custom function for rounding values
    def round_value(input_value):
        if input_value.values > 1:
            a = float(round(input_value, 2))
        else:
            a = float(round(input_value, 8))
        return a

    

    # DataFrame of selected Cryptocurrency
    col1_df = df[df.symbol == col1_selection]

    # Apply a custom function to conditionally round values
    col1_price = round_value(col1_df.weightedAvgPrice)

    # Select the priceChangePercent column
    col1_percent = f'{float(col1_df.priceChangePercent)}%'
    
    # Create a metrics price box
    col1.metric(col1_selection, col1_price, col1_percent)
    
    #chart
    components.html(f"""
    <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
        <div id="tradingview_fe4a9"></div>
        <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{col1_selection}/?exchange=BINANCE" rel="noopener" target="_blank"><span class="blue-text">{col1_selection} Chart</span></a> by TradingView</div>
        <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
        <script type="text/javascript">
        new TradingView.widget(
            {{
            "width": 980,
            "height": 610,
            "symbol": "BINANCE:{col1_selection}",
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
    

    st.header('**All Price**')
    st.dataframe(df)

    