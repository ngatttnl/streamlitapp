from os import name
from attr import validate
import streamlit as st
from apps.db import *
import pandas as pd

def app():
    menu = ["List Stocks", "Edit Stock", "Delete Stock"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice=="List Stocks":
        with st.expander("Add Stock"):
            col1, col2, col3 = st.columns(3)
            with col1:
                value = st.selectbox("Exchange: ", ["HNX","HOSE","UPCOM"])
            with col2:
                name=st.text_input("Enter name: ", key = 1, max_chars=50)
            with col3:
                st.write("Press Enter to add a stock!")
                #if st.button("Add"):
                """try:
                    if name!="":
                        add(name.upper(), value)
                        st.success("Stock: {} saved".format(name.upper()))
                    else:
                        st.warning("Name of stock is not empty!")
                except:
                    st.warning("The stock already exists")"""
                
                st.warning("You can't add stocks now!")
                
        st.subheader("Vietnamese Stocks")
        all_stocks = pd.DataFrame(view_all(), columns=["Name", "Exchange"])
        #all_stocks = all_stocks.sort_values(by=['Name']) 
        st.dataframe(all_stocks)
    elif choice=="Edit Stock":
        st.subheader("Edit Stock")
        result = view_all()
        clean_db = pd.DataFrame(result, columns=["Name", "Exchange"])
        st.dataframe(clean_db)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            unique_names = [i[0] for i in view_all()]
            name = st.selectbox("Unique name", unique_names)
        with col2:
            exchange = st.selectbox("Exchange: ", ["HNX","HOSE","UPCOM"])
        

        new_df = clean_db
        st.warning("You can't edit stocks now!")
        
        """if st.button("Edit"):
            edit(name, exchange)
            st.warning("Edited: '{}'".format(name))"""


    elif choice=="Delete Stock":
        st.subheader("Delete Stock")
        result = view_all()
        clean_db = pd.DataFrame(result, columns=["Name", "Exchange"])
        st.dataframe(clean_db)
        
        
        unique_names = [i[0] for i in view_all()]
        name = st.selectbox("Unique name", unique_names)
        
        new_df = clean_db
        st.warning("You can't delete stocks now!")
        """if st.button("Delete"):
            delete(name)
            st.warning("Deleted: '{}'".format(name))"""

        """if st.button("Delete Wrong stocks"):
            #delete_wrong()
            st.warning("Deleted: '{}'")"""
        
        
        

	
