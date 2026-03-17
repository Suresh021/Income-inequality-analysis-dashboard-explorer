import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth, firestore
import base64

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("dashboard-explorer-4f089ffb4fcb.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# ✅ Function to add background image
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
        unsafe_allow_html=True
    )

def show():
    # Add background
    add_bg_from_local("9019808.jpg")

    # --- CSS for buttons inside forms ---
    st.markdown("""
    <style>
    div.stForm .stFormSubmitButton button {
        width: 220px !important;
        background-color: white !important;
        color: black !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        padding: 10px !important;
        border: 2px solid #4facfe !important;
        margin-top: 5px;
        margin-bottom: 5px;
        margin-left: 50px;
        transition: 0.3s !important;
    }
    div.stForm .stFormSubmitButton button:hover {
        background: linear-gradient(90deg, #4facfe, #00f2fe) !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # --- Center layout ---
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='signup-container'>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align:center;'>📝 Signup</h2>", unsafe_allow_html=True)

        # --- Signup Form ---
        with st.form("signup_form"):
            username = st.text_input("Username")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")

            signup_submitted = st.form_submit_button("Signup")

        # --- Handle Signup ---
        if signup_submitted:
            if not username or not email or not password:
                st.error("⚠️ Please fill in all fields")
            elif password != confirm_password:
                st.error("❌ Passwords do not match!")
            else:
                try:
                    # Create user in Firebase Authentication
                    user = auth.create_user(
                        email=email,
                        password=password,
                    )

                    # Save username + email in Firestore
                    db.collection("users").document(username).set({
                        "username": username,
                        "email": email
                    })

                    st.success(f"✅ Account created for {username}! Please login.")
                    st.session_state.page = "Login"
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error creating account: {e}")

        st.markdown("</div>", unsafe_allow_html=True)
