import streamlit as st
from streamlit_option_menu import option_menu
import Home
import Dashboard
import Profile
import Feedback
import Login
import Signup

# --- Inject CSS ---
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Button CSS for sidebar navigation ---
st.markdown("""
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
""", unsafe_allow_html=True)

# --- Initialize session state ---
if "page" not in st.session_state:
    st.session_state.page = "Login"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- Top navigation menu (only after login) ---
if st.session_state.logged_in:
    selected = option_menu(
        menu_title=None,  # no menu title
        options=["Home", "Dashboard", "Feedback", "Profile"],
        icons=["house", "bar-chart", "pencil-square", "person"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#f0f0f0"},
            "icon": {"color": "black", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "color": "black"},
            "nav-link-selected": {"background-color": "#4facfe", "color": "white"},
        }
    )

    # Update current page based on selection
    if selected == "Home":
        st.session_state.page = "Home"
    elif selected == "Dashboard":
        st.session_state.page = "Dashboard"
    elif selected == "Feedback":
        st.session_state.page = "Feedback"
    elif selected == "Profile":
        st.session_state.page = "Profile"

# --- Page routing ---
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
    elif st.session_state.page == "Feedback":
        Feedback.show()
    elif st.session_state.page == "Profile":
        Profile.show()