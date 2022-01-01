import streamlit as st
import streamlit.components.v1 as components
from multiapp import MultiApp
from apps import book, addstock, binancescreener, home, coinmarket, datadownload, crypto, gainer, binanceprice, stocktechnical #, speech, avatar # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Learning", book.app)
app.add_app("VN Stock Screener", home.app)
app.add_app("VN Stock Technical", stocktechnical.app)
app.add_app("VN Stock Gainers / Losers", gainer.app)
app.add_app("Add Stock", addstock.app)

app.add_app("Binance Technical", binanceprice.app)
app.add_app("Binance Screener", binancescreener.app)
app.add_app("Data Download", datadownload.app)
app.add_app("Coin Market", coinmarket.app)
app.add_app("Crypto Tracker", crypto.app)


st.set_page_config(layout="wide")
col0, col1= st.columns((4.5, 1))

with col0:
    # The main app
    app.run()
with col1:
    expand_menu = f"""
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
        <div class="container">
            <h2>My projects</h2>
            
            <a href="http://khuonchauthanhphuc.tk" class="btn btn-info" role="button" style="width: 100%">Khuôn chậu Thanh Phúc</a>
            <br><br>
            
            <a href="http://bazancider.tk" class="btn btn-info" role="button" style="width: 100%">Rượu trái cây Bazan</a>
            <br><br>

            <a href="https://www.linguar.com" class="btn btn-info" role="button" style="width: 100%">Học ngoại ngữ</a>
            <br><br>

            <a href="http://thanhnga.tk" class="btn btn-info" role="button" style="width: 100%">My website</a>
            <br><br>
        
        </div>
    """
    #st.markdown(expand_menu, unsafe_allow_html=True)
    components.html(expand_menu, height=500, scrolling=True)
    #tabs = ["Candlestick", "Marubozu_Spinning", "Hammer"]
    #active_tab = st.radio("Select a topic", tabs)
    