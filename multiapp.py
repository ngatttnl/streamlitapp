"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    def __init__(self):
        self.apps = []
        self.language = "en"
    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })
    def get_language(self):
        print("get: " + self.language)
        return self.language
    def run(self):
        st.set_page_config(
        page_title="Investing world",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded")
        st.markdown(
            f"""
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script type="text/javascript" src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
            <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
            <a class="navbar-brand" href="https://thanhnga.herokuapp.com" target="_blank">Thanh Nga</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item active">
                    <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="http://khuonchauthanhphuc.tk" target="_blank">Khuôn chậu Thanh Phúc</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="http://bazancider.tk" target="_blank">Rượu trái cây Bazan</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="http://thanhnga.tk" target="_blank">My Wordpress website</a>
                    </li>
                </ul>
            </div>
        </nav>
            """, unsafe_allow_html=True)
            
        hide_menu_style = """
                <style>
                #MainMenu {visibility: hidden;}

                .sidebar .sidebar-content {{
                        width: 200px;
                    }}
                </style>
                """
        st.markdown(hide_menu_style, unsafe_allow_html=True)
        
        #app = st.selectbox(     
      
        
        app = st.sidebar.radio(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title'])

        languages = {"vi_VN": "Việt Nam", "en": "English", "de_DE": "Deutsch"}
        if 'key' not in st.session_state:
            st.session_state['key'] = 'en'
        st.session_state['key'] = st.sidebar.selectbox("Select language", languages.keys(), format_func=lambda x:languages[ x ])
        
        app['function']()