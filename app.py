# app.py
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Global Inequality Explorer",
    layout="wide",
    initial_sidebar_state="auto",
)

import About
import Chatbot
import Dashboard
import Feedback
import Help
import Home
import Login
import Profile
import ScenarioLab
import Signup

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    div.stButton > button {
        width: 220px !important;
        background-color: white !important;
        color: black !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        padding: 10px !important;
        border: 2px solid #4facfe !important;
        margin-top: 5px;
        margin-bottom: 5px;
        transition: 0.3s !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #4facfe, #00f2fe) !important;
        color: white !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

if "page" not in st.session_state:
    st.session_state.page = "Login"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    selected = option_menu(
        menu_title=None,
        options=[
            "Home",
            "Dashboard",
            "Chatbot",
            "Scenario Lab",
            "About",
            "Feedback",
            "Help",
            "Profile",
        ],
        icons=[
            "house",
            "bar-chart",
            "robot",
            "activity",
            "info-circle",
            "pencil-square",
            "question-circle",
            "person",
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#f0f0f0"},
            "icon": {"color": "black", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "center",
                "margin": "0px",
                "color": "black",
                "min-width": "140px",
                "white-space": "nowrap",
            },
            "nav-link-selected": {"background-color": "#4facfe", "color": "white"},
        },
    )

    if selected == "Home":
        st.session_state.page = "Home"
    elif selected == "Dashboard":
        st.session_state.page = "Dashboard"
    elif selected == "Chatbot":
        st.session_state.page = "Chatbot"
    elif selected == "Scenario Lab":
        st.session_state.page = "Scenario Lab"
    elif selected == "About":
        st.session_state.page = "About"
    elif selected == "Feedback":
        st.session_state.page = "Feedback"
    elif selected == "Help":
        st.session_state.page = "Help"
    elif selected == "Profile":
        st.session_state.page = "Profile"

if not st.session_state.logged_in:
    if st.session_state.page == "Login":
        Login.show()
    elif st.session_state.page == "Signup":
        Signup.show()
else:
    if st.session_state.page == "Home":
        Home.show()
    elif st.session_state.page == "Dashboard":
        Dashboard.show()
    elif st.session_state.page == "Chatbot":
        Chatbot.show()
    elif st.session_state.page == "Scenario Lab":
        ScenarioLab.show()
    elif st.session_state.page == "About":
        About.show()
    elif st.session_state.page == "Feedback":
        Feedback.show()
    elif st.session_state.page == "Help":
        Help.show()
    elif st.session_state.page == "Profile":
        Profile.show()
