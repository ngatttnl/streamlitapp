import streamlit as st
from binance.client import Client
import pandas as pd
import streamlit.components.v1 as components
from PIL import Image
#from apps import cryptofunc

client = Client()
info = client.get_exchange_info()

def app():
    image = Image.open('invest.png')
    st.image(image, width = 500)
    st.header('**Selected Price**')

    # Load market data from Binance API
    all_pairs = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')
    relev = all_pairs[all_pairs.symbol.str.contains('USDT')]
    
    df = relev[~((relev.symbol.str.contains('UP')) | (relev.symbol.str.contains('DOWN')) | (relev.symbol.str.contains('BEAR')) | (relev.symbol.str.contains('BULL')))]
    
    # Widget (Cryptocurrency selection box) 
    col1_selection = st.selectbox('Crypto', df.symbol, list(df.symbol).index('BTCUSDT') )

    # Custom function for rounding values
    def round_value(input_value):
        if input_value.values > 1:
            a = float(round(input_value, 2))
        else:
            a = float(round(input_value, 8))
        return a

    col1, col2, col3 = st.columns(3)

    # DataFrame of selected Cryptocurrency
    col1_df = df[df.symbol == col1_selection]

    # Apply a custom function to conditionally round values
    col1_price = round_value(col1_df.weightedAvgPrice)

    # Select the priceChangePercent column
    col1_percent = f'{float(col1_df.priceChangePercent)}%'
    
    # Create a metrics price box
    col1.metric(col1_selection, col1_price, col1_percent)
    
    #chart
    html_str = f"""
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
    <div id="technical-analysis"></div>
    <div class="tradingview-widget-copyright"><a href="https://in.tradingview.com/symbols/{col1_selection}/" rel="noopener" target="_blank"><span class="blue-text">{col1_selection} Chart</span></a> by TradingView</div>
    <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
    <script type="text/javascript">
    new TradingView.widget(
    {{
    "container_id": "technical-analysis",
    "width": "100%",
    "height": 800,
    "symbol": "BINANCE:{col1_selection}",
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
    "locale": "in"
    }}
    );
    </script>
    </div>
    <!-- TradingView Widget END -->
    """
    components.html(html_str, height=820)

    st.header('**All Price**')
    st.dataframe(df)

    