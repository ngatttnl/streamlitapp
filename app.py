import streamlit as st
from multiapp import MultiApp
from apps import home, data, model#, crypto, sp500, mlapp, themes, modelper, binanceprice #, avatar # import your app modules here

app = MultiApp()

st.markdown("""
# Multi-Page App

This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).

""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Model", model.app)
"""app.add_app("Crypto", crypto.app)
app.add_app("SP500", sp500.app)
app.add_app("Machine Learning App", mlapp.app)
app.add_app("Theme changing", themes.app)
app.add_app("Model Perform", modelper.app)
app.add_app("Binance Price", binanceprice.app)
#app.add_app("Avatar making", avatar.app)
"""

# The main app
app.run()