import streamlit as st
from apps.db import *
import pandas as pd

# Layout Templates
html_temp = """
    <div style="background-color:{};padding:10px;border-radius:10px">
    <h1 style="color:{};text-align:center;">Simple Blog </h1>
    </div>
"""
title_temp ="""
    <div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
    <h4 style="color:white;text-align:center;">{}</h1>
    
    <br/>
    <br/> 
    <p style="text-align:justify">{}</p>
    </div>
"""
article_temp ="""
    <div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
    <h4 style="color:white;text-align:center;">{}</h1>
    <h6>Author:{}</h6> 
    <h6>Post Date: {}</h6>
    <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;width: 50px;height: 50px;border-radius: 50%;" >
    <br/>
    <br/>
    <p style="text-align:justify">{}</p>
    </div>
"""
head_message_temp ="""
    <div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
    <h4 style="color:white;text-align:center;">{}</h1>
    <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
    <h6>Author:{}</h6> 

    </div>
"""
full_message_temp ="""
    <div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
    <p style="text-align:justify;color:black;padding:10px">{}</p>
    </div>
"""

def app():
	st.markdown(html_temp.format('royalblue','white'),unsafe_allow_html=True)

	menu = ["Home","View Stocks","Add Stock","Search","Manage Blog"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		result = view_all()

		for i in result:
			value = i[0]
			name = i[1]
			
			st.markdown(title_temp.format(name, value),unsafe_allow_html=True)

	elif choice == "View Stocks":
		st.subheader("View Articles")
		all_titles = [i[0] for i in view_all()]
		postlist = st.sidebar.selectbox("View Posts",all_titles)
		post_result = get_by_name(postlist)
		for i in post_result:
			value = i[0]
			name = i[1]
			
			st.markdown(head_message_temp.format(name,value),unsafe_allow_html=True)
		
	elif choice == "Add Stock":
		st.subheader("Add Stock")
		create_table()
		name = st.text_input("Enter name", max_chars=50)
		value = st.text_input("Enter value")
        choice1 = "ab"
        choice = st.sidebar.selectbox("Exchanges",["HNX","HOSE","UPCOM"])
		
		if st.button("Add"):
			add_data(name, value)
			st.success("Post:{} saved".format(name))	
	elif choice == "Search":
		st.subheader("Search Articles")
		search_term = st.text_input('Enter Search Term')
		search_choice = st.radio("Field to Search By",("name","author"))
		
		if st.button("Search"):

			if search_choice == "name":
				article_result = get_by_name(search_term)
			elif search_choice == "author":
				article_result = get_by_value(search_term)


			for i in article_result:
				value = i[0]
				name = i[1]
				b_article = i[2]
				b_post_date = i[3]
				
				st.markdown(head_message_temp.format(name,value,b_post_date),unsafe_allow_html=True)
				st.markdown(full_message_temp.format(b_article),unsafe_allow_html=True)

	elif choice == "Manage Blog":
		st.subheader("Manage Articles")

		result = view_all()
		clean_db = pd.DataFrame(result,columns=["Author","name","Articles","Post Date"])
		st.dataframe(clean_db)

		unique_names = [i[0] for i in view_all()]
		delete_blog_by_name = st.selectbox("Unique name",unique_names)
		new_df = clean_db
		if st.button("Delete"):
			delete(delete_blog_by_name)
			st.warning("Deleted: '{}'".format(delete_blog_by_name))


		if st.checkbox("Metrics"):
			
			new_df['Length'] = new_df['Articles'].str.len()
			st.dataframe(new_df)


			st.subheader("Author Stats")
			new_df["Author"].value_counts().plot(kind='bar')
			st.pyplot()

			st.subheader("Author Stats")
			new_df['Author'].value_counts().plot.pie(autopct="%1.1f%%")
			st.pyplot()
