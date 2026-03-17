import base64
import time

import firebase_admin
import requests
import streamlit as st
from firebase_admin import credentials, firestore

import Signup

# Firebase Initialization
if not firebase_admin._apps:
    cred = credentials.Certificate("dashboard-explorer-4f089ffb4fcb.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Firebase REST API Key
API_KEY = st.secrets["GOOGLE_API_KEY"]


# Helper Functions
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        header[data-testid="stHeader"] {{
            display: none;
        }}
        div[data-testid="stToolbar"] {{
            display: none;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def verify_user_with_password(email, password):
    """Authenticate user with Firebase Auth REST API."""
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
    payload = {"email": email, "password": password, "returnSecureToken": True}
    response = requests.post(url, json=payload)
    return response.json()


# Login Page
def show():
    if st.session_state.get("page") == "Signup":
        Signup.show()
        return

    add_bg_from_local("9019808.jpg")

    # --- CSS for buttons ---
    st.markdown(
        """
    <style>
    div.stButton > button,
    div.stForm .stFormSubmitButton button {
        width: 300px !important;
        background-color: white !important;
        color: black !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        padding: 10px !important;
        border: 2px solid #4facfe !important;
        margin-top: 5px;
        margin-bottom: 5px;
        margin-left: 150px;
        transition: 0.3s !important;
    }

    div.stButton > button:hover,
    div.stForm .stFormSubmitButton button:hover {
        background: linear-gradient(90deg, #4facfe, #00f2fe) !important;
        color: white !important;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    # --- Center layout ---
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='login-container'>", unsafe_allow_html=True)

        st.markdown(
            """
        <div style="
            background-color: rgba(255,255,255,0.15);
            padding: 25px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            margin-bottom: 20px;
            width: 100%;
            max-width: 1000px;
            margin-left: auto;
            margin-right: auto;
        ">
            <h1 style="margin:0; padding:0; white-space: nowrap;">🌍 Global Inequality Explorer</h1>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p style='text-align:center; color:gray;'>Welcome back! Please login to continue.</p>",
            unsafe_allow_html=True,
        )

        # --- Login Form ---
        with st.form("login_form"):
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")

            login_submitted = st.form_submit_button("Login")
            create_clicked = st.form_submit_button("Create an account")

            if login_submitted:
                if not username or not password:
                    st.error("⚠️ Please enter both username and password")
                else:
                    with st.spinner("🔵 Checking credentials..."):
                        time.sleep(1.5)

                        # Check if username exists in Firestore
                        user_doc = db.collection("users").document(username).get()
                        if not user_doc.exists:
                            st.error("❌ Username not found")
                        else:
                            user_data = user_doc.to_dict()
                            email = user_data.get("email")

                            if not email:
                                st.error("⚠️ No email mapped for this username")
                            else:
                                # Authenticate with Firebase using email + password
                                try:
                                    result = verify_user_with_password(email, password)
                                    if "idToken" in result:
                                        st.session_state.logged_in = True
                                        st.session_state.username = username
                                        st.session_state.email = email
                                        st.session_state.id_token = result["idToken"]

                                        st.session_state.page = "🏠 Home"
                                        st.success(f"✅ Welcome {username}!")
                                        st.rerun()
                                    else:
                                        error_message = result.get("error", {}).get(
                                            "message", "❌ Wrong credentials"
                                        )
                                        st.error(f"❌ {error_message}")
                                except Exception as e:
                                    st.error(f"❌ Error logging in: {e}")

            # --- Handle Signup Button ---
            if create_clicked:
                st.session_state.page = "Signup"
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)
