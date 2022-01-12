
import streamlit as st
from apps.db import *
import pandas as pd
from streamlit_quill import st_quill
import streamlit.components.v1 as components
from PIL import Image
import re

def app():
    menu = ["List Post", "Add Post", "Edit Post", "Delete Post"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice=="List Post":
        result = view_all_post()
        count = 0
        for i in result:
            count = count + 1
            id = i[0]
            topic = i[1]
            content = i[2]
            if count==1:
                html_content=f"""
                <div>
                    <h2><a title="">{topic}</a></h2>
                    <div>{content}</div>
                </div>                
                """
                st.markdown(html_content, unsafe_allow_html=True)

            else:
                col01, col02 = st.columns([1, 5])
                with col01:
                    img = "stock.png" #str(count) + ".jpg"
                    image = Image.open('images/small/' + img)
                    st.image(image, width=200)
                    
                with col02:
                    html_css = """
                    <style>
                        .blog-meta h4 {
                            padding: 1rem 0 0.5rem;
                            margin: 0;
                            font-size: 21px;
                        }

                        .blog-meta.big-meta h4 {
                            padding: 1rem 0 0.6rem;
                            margin: 0;
                            font-size: 28px;
                        }

                        .blog-meta.big-meta p {
                            margin-bottom: 0.5rem;
                            padding-bottom: 0;
                        }

                        .blog-meta small {
                            font-size: 11px;
                            display: inline-block;
                            margin-bottom: 0;
                            padding-bottom: 0;
                            color: #111111;
                            font-weight: bold;
                            text-transform: uppercase;
                            margin-right: 0.5rem;
                        }

                        .blog-meta small:after {
                            content: "/";
                            padding-left: 1rem;
                        }

                        .blog-meta small:last-child:after {
                            content: ""
                        }
                    </style>
                    """
                    st.markdown(html_css, unsafe_allow_html=True)
                    html_content=f"""
                    <div class="blog-meta big-meta">
                        <h4><a title="">{topic}</a></h4>    
                    </div>
                    """
                    st.markdown(html_content, unsafe_allow_html=True)
                    with st.expander("Click here"):
                        view(content)
                
    elif choice=="Add Post":
        topic = st.text_input("Enter topic name: ", max_chars=100)
        content = st_quill(html=True)  # Spawn a new Quill editor
        st.warning("You can't add posts now!") 
        """if st.button("Add"):
            try:
                if topic!="":
                    add_post(topic, content)
                    st.success("Saved: ".format(topic))
                else:
                    st.warning("Name of topic and content is not empty!")
            except:
                st.warning("Something went wrong!")
            """    
    elif choice=="Edit Post":
        st.subheader("Edit Post")
        
        df = pd.DataFrame(view_all_post(), columns=['ID', 'Topic', 'Content'])
        df = df.sort_values(by=['Topic']) 
        posts = df.set_index(['ID'])['Topic'].to_dict()
        
        idTopic = st.selectbox("Select topic:", options=posts, format_func=lambda x:posts[ x ])

        dfContent = df.loc[df['ID'] == idTopic]
       
        topic = st.text_input("Enter a topic: ", value=dfContent.iloc[0]['Topic'])
        content = st_quill(value= dfContent.iloc[0]['Content'], html=True)  # Spawn a new Quill editor 
        st.warning("You can't edit post now!")
        
        """if st.button("Edit"):
            #newContent = content.replace('"', '###')
            #print(newContent)
            edit_post(content, topic, idTopic)
            st.warning("Edited: '{}'".format(idTopic))
        """
    elif choice=="Delete Post":
        st.subheader("Delete Stock")
        
        st.warning("You can't delete posts now!")
        """if st.button("Delete"):
            delete(name)
            st.warning("Deleted: '{}'".format(name))"""

        """if st.button("Delete Wrong stocks"):
            #delete_wrong()
            st.warning("Deleted: '{}'")"""
    elif choice=="tmp":
        df = pd.DataFrame(view_all_post(), columns=['ID', 'Topic', 'Content'])
        df = df.sort_values(by=['Topic']) 
        posts = df.set_index(['ID'])['Topic'].to_dict()
        
        topic = st.selectbox("Select topic:", options=posts, format_func=lambda x:posts[ x ])

        content = df.loc[df['ID'] == topic]
        for i in range(0, len(df)):
            #print(df.iloc[i]['c1'], df.iloc[i]['c2'])
            col01, col02 = st.columns([1, 5])
            with col01:
                img = str(i+1) + ".jpg"
                image = Image.open('images/small/' + img)
                st.image(image, width=200)
                
            with col02:
                st.subheader(df.iloc[i]['Topic'])
                show_content=df.iloc[i]['Content']
                
                with st.expander("See more..."):
                    components.html(show_content, height=300, scrolling=True)
def view(content):
    html_content2 = f"""
    <div>{content}</div>
    """
    st.markdown(html_content2, unsafe_allow_html=True)
        
        
        

	
