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
    
    st.title('Loading...')
    placeholder1 = st.empty()
    placeholder1.warning("I am learning to make a system for trading Vietnamese stocks and cryptos on Binance. Please come back later for many more features")
  

    

    