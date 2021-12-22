import streamlit as st
from multiapp import MultiApp
from apps import home, coinmarket, datadownload, crypto, sp500, mlapp, themes, modelper, binanceprice, stock #, speech, avatar # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("VN Stock Market", stock.app)
app.add_app("Binance Price", binanceprice.app)
app.add_app("Data Download", datadownload.app)
app.add_app("Coin Market", coinmarket.app)
#app.add_app("Speech to Text", speech.app)
app.add_app("Crypto Tracker", crypto.app)

app.add_app("SP500", sp500.app)
app.add_app("Machine Learning App", mlapp.app)
app.add_app("Theme changing", themes.app)
app.add_app("Model Perform", modelper.app)

#app.add_app("Avatar making", avatar.app)


# The main app
app.run()