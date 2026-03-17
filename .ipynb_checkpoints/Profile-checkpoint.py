import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore, auth
import streamlit.components.v1 as components

# Initialize Firebase (once)
if not firebase_admin._apps:
    cred = credentials.Certificate("dashboard-explorer-4f089ffb4fcb.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

def show():

    st.markdown(
        """
        <style>
        .stApp {
            background-color: #001f3f;  /* Navy blue background */
            color: #D3D3D3;             /* Light grey text */
        }

        header[data-testid="stHeader"] {
            display: none;
        }
        div[data-testid="stToolbar"] {
            display: none;
        }
        
        </style>
        """,
        unsafe_allow_html=True
)
    
    # --- CSS for styling ---
    st.markdown("""
        <style>
        .main-title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-top: 10px;
            margin-bottom: 20px;
            color: #00b8d9;
        }
        .card {
            padding: 20px;
            border-radius: 12px;
            background-color: #fff;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            text-align: center;
            margin-bottom: 20px;
        }
        .emoji {
            font-size: 40px;
        }

        /* Logout button inside form */
        div.stForm .stFormSubmitButton > button {
            width: 220px !important;
            background-color: white !important;
            color: black !important;
            font-weight: bold !important;
            border-radius: 8px !important;
            padding: 10px !important;
            border: 2px solid #ff416c !important;
            margin-top: 20px;
            transition: 0.3s !important;
        }
        div.stForm .stFormSubmitButton > button:hover {
            background: linear-gradient(90deg, #ff416c, #ff4b2b) !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- Profile title card ---
    st.markdown("<div class='main-title'>👤 Profile</div>", unsafe_allow_html=True)

    components.html(
        """
        <div style="
            background-color: white;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            max-width: 600px;
            margin: auto;
        ">
            <script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.8.1/dist/dotlottie-wc.js" type="module"></script>
<dotlottie-wc src="https://lottie.host/11938525-c4d0-46aa-b75e-37a1ed4c7542/abcKuyyrCz.lottie" style="width: 600px;height: 300px" autoplay loop></dotlottie-wc>

        </div>
        """,
        height=400,
    )

    # Check login
    if "username" not in st.session_state:
        st.warning("⚠️ Please login to view your profile")
        return

    username = st.session_state["username"]

    # Fetch user data from Firestore
    user_ref = db.collection("users").document(username).get()
    if user_ref.exists:
        user_data = user_ref.to_dict()
        email_val = user_data.get("email", "")
        bio_val = user_data.get("bio", "")
    else:
        email_val = ""
        bio_val = ""

    # --- Profile form ---
    with st.form("profile_form"):
        name = st.text_input("👤 Username", value=username, disabled=True)
        email = st.text_input("📧 Email", value=email_val, disabled=True)
        bio = st.text_area("✍️ Bio", value=bio_val, placeholder="Write something about yourself...")

        submitted = st.form_submit_button("💾 Save")
        if submitted:
            db.collection("users").document(username).update({"bio": bio})
            st.success(f"✅ Profile updated for {username}!")

    # --- Logout form inside the page ---
    st.markdown("<div style='text-align:center; margin-top:30px;'>", unsafe_allow_html=True)
    with st.form("logout_form"):
        logout_clicked = st.form_submit_button("🚪 Logout")
        if logout_clicked:
            st.session_state.logged_in = False
            st.session_state.page = "Login"
            st.session_state.pop("username", None)
            st.success("✅ Logged out successfully!")
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
