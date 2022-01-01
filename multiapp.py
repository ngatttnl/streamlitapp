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
        
        languages = {"vi_VN": "Việt Nam", "en": "English", "de_DE": "Deutsch"}
        if 'key' not in st.session_state:
            st.session_state['key'] = 'en'
        st.session_state['key'] = st.sidebar.selectbox("Select language", languages.keys(), format_func=lambda x:languages[ x ])
       
        ex_menu = """
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" integrity="sha512-Fo3rlrZj/k7ujTnHg4CGR2D7kSs0v4LLanw2qksYuRlEzO+tcaEPQogQ0KaoGN26/zrn20ImR1DfuLWnOo7aBA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
            <style>
                .wrapMenuHeader,
                .wrapMenuHeader * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }
                .wrapMenuHeader a {
                    text-decoration: none;
                }

                .wrapMenuHeader {
                    width: 100%;
                    background-color: #3498DB;
                    padding-left: 20px;
                    padding-right: 20px;
                    padding-top: 15px;
                    padding-bottom: 15px;
                    display: flex;
                    align-items: center;
                    position: relative;
                }
                .wrapMenuHeader .wrapLogoMenu {
                    display: flex;
                    align-items: center;
                    gap: 30px;
                    width: 100%;
                }

                .wrapMenuHeader .logoName {
                    font-size:22px;
                    font-weight: 700px;
                    color: white
                }

                .wrapMenuHeader .wrapMenu {
                    list-style: none;
                    display: flex;
                    gap: 20px;
                }

                .wrapMenuHeader .wrapMenu .MenuLink {
                    color: #9ACCED;
                    font-size: 18px;
                    font-weight: 700px;
                }

                .wrapMenuHeader .wrapMenu .MenuLink:hover {
                    color : rgba(255,255,255,.75)
                }

                .wrapMenuHeader .btnBurger {
                    position: absolute;
                    top: 10px;
                    right: 20px;
                    cursor: pointer;
                    width: 40px;
                    height: 40px;
                    border: 2px solid #49A3DF;
                    display: none;
                    justify-content: center;
                    align-items: center;
                    color: #9ACCED;
                    border-radius: 5px;
                    -webkit-border-radius: 5px;
                    -moz-border-radius: 5px;
                    -ms-border-radius: 5px;
                    -o-border-radius: 5px;
                    font-size: 22px
                }

                .wrapMenuHeader .btnBurger:hover {
                    color : rgba(255,255,255,.75)
                }

                input[id="collapseMenuMoile"]:checked ~ .wrapLogoMenu {
                    max-height: 100vh !important;
                    transition: all .5s;
                    -webkit-transition: all .5s;
                    -moz-transition: all .5s;
                    -ms-transition: all .5s;
                    -o-transition: all .5s;
                }

                @media screen and (max-width: 1000px) {
                    .wrapMenuHeader .btnBurger {
                        display: flex;
                    }

                    .wrapMenuHeader .wrapLogoMenu {
                        display: flex;
                        height: auto;
                        align-items: flex-start;
                        gap: 0px;
                        flex-direction: column;
                        max-height: 30px;
                        overflow: hidden;
                        transition: all .2s;
                        -webkit-transition: all .2s;
                        -moz-transition: all .2s;
                        -ms-transition: all .2s;
                        -o-transition: all .2s;
                    }
                    
                    .wrapMenuHeader .wrapMenu {
                        flex-direction:column;
                        gap: 0px;
                        width: 100%;
                        margin-top: 10px;
                    }
                    
                    .wrapMenuHeader .wrapMenu .MenuLink {
                        width: 100%;
                        display: flex;
                        padding-top: 8px;
                        padding-bottom: 8px;
                    }
                }
                </style>
            <div class="wrapMenuHeader">
                <input type="checkbox" hidden id="collapseMenuMoile">
                <div class="wrapLogoMenu">
                    <a href="http://thanhnga.tk" class="logoName">
                        Thanh Nga
                    </a>

                    <ul class="wrapMenu">
                        <li class="menuItem">
                            <a href="http://khuonchauthanhphuc.tk" class="MenuLink">
                                Khuôn chậu Thanh Phúc
                            </a>
                        </li>    
                        <li class="menuItem">
                            <a href="http://bazancider.tk" class="MenuLink">
                                Rượu trái cây Bazan
                            </a>
                        </li>    
                        <li class="menuItem">
                            <a href="https://www.linguar.com" class="MenuLink">
                                Học ngoại ngữ
                            </a>
                        </li>    
                        <li class="menuItem">
                            <a href="http://thanhnga.tk" class="MenuLink">
                                My website
                            </a>
                        </li>            
                    </ul>
                </div>

                <label for="collapseMenuMoile" class="btnBurger">
                    <i class="fas fa-bars"></i>
                </label>
            </div>
        """
        expand_menu = f"""
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
            <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
            <a class="navbar-brand" href="https://thanhnga.herokuapp.com" target="_blank">Thanh Nga</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav" style="scroll-behavior: auto;">
                <ul class="navbar-nav">
                    <li class="nav-item">
                    <a class="nav-link" href="http://khuonchauthanhphuc.tk" target="_blank">Khuôn chậu Thanh Phúc</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="http://bazancider.tk" target="_blank">Rượu trái cây Bazan</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="https://www.linguar.com" target="_blank">Học ngoại ngữ</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="http://thanhnga.tk" target="_blank">My website</a>
                    </li>
                </ul>
            </div>
            </nav>
            """
        #st.markdown(ex_menu, unsafe_allow_html=True)
        components.html(ex_menu, height=120, scrolling=True)
         
        hide_menu_style = """
                <style>
                #MainMenu {visibility: hidden;}

                </style>
                """
        st.markdown(hide_menu_style, unsafe_allow_html=True)
        
        PINNED_NAV_STYLE = """
            <style>
            .reportview-container .sidebar-content {
                padding-top: 0rem;

            }
            .reportview-container .main .block-container {
                padding-top: 0rem;
                padding-right: 3rem;
                padding-left: 3rem;
                padding-bottom: 0rem;
            }
            </style>
        """
        st.markdown(PINNED_NAV_STYLE,unsafe_allow_html=True)
        #app = st.selectbox(     
      
        app = st.sidebar.radio(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()