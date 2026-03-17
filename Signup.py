import base64

import firebase_admin
import streamlit as st
from firebase_admin import auth, credentials, firestore

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("dashboard-explorer-4f089ffb4fcb.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()


# Function to add animated image
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


def show():
    # Add background
    add_bg_from_local("9019808.jpg")

    # --- CSS for buttons ---
    st.markdown(
        """
    <style>
    div.stForm .stFormSubmitButton button,
    div.stButton > button {
        width: 200px !important;
        background-color: white !important;
        color: black !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        padding: 10px !important;
        border: 2px solid #4facfe !important;
        margin-top: 10px;
        margin-left: 60px;
        margin-bottom: 5px;
        transition: 0.3s !important;
    }
    div.stForm .stFormSubmitButton button:hover,
    div.stButton > button:hover {
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
        st.markdown("<div class='signup-container'>", unsafe_allow_html=True)
        st.markdown(
            "<h2 style='text-align:center;'>📝 Signup</h2>", unsafe_allow_html=True
        )

        # --- Signup Form ---
        with st.form("signup_form"):
            username = st.text_input("Username")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")

            # --- Buttons (inside form) ---
            col_btn1, col_btn2 = st.columns([1, 1])
            with col_btn1:
                signup_submitted = st.form_submit_button("Signup")
            with col_btn2:
                login_clicked = st.form_submit_button("Login")

            if signup_submitted:
                if not username or not email or not password:
                    st.error("⚠️ Please fill in all fields")
                elif password != confirm_password:
                    st.error("❌ Passwords do not match!")
                else:
                    try:
                        # Creates user in Firebase Authentication
                        user = auth.create_user(
                            email=email,
                            password=password,
                        )

                        # Save username + email in Firestore
                        db.collection("users").document(username).set(
                            {"username": username, "email": email}
                        )

                        st.success(f"✅ Account created for {username}! Please login.")
                        st.session_state.page = "Login"
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ Error creating account: {e}")

            # --- Handle Login button ---
            if login_clicked:
                st.session_state.page = "Login"
                st.rerun()
