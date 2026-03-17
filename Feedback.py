import datetime

import firebase_admin
import streamlit as st
from firebase_admin import credentials, firestore


def show():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #001f3f;

        header[data-testid="stHeader"] {
            display: none;
        }
        div[data-testid="stToolbar"] {
            display: none;
        }
        
        div.stButton > button,
        div.stForm .stFormSubmitButton button {
            width: 220px !important;
            background-color: white !important;
            color: black !important;
            font-weight: bold !important;
            border-radius: 8px !important;
            padding: 10px !important;
            border: 2px solid #ff416c !important;
            margin-top: 5px;
            margin-bottom: 5px;
            margin-left: 540px;
            transition: 0.3s !important;
        }

        div.stButton > button:hover,
        div.stForm .stFormSubmitButton button:hover {
            background: linear-gradient(90deg, #ff416c, #ff4b2b) !important;
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<h1 style='color:#FFFFFF;'>📝 Feedback</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size:18px;'>We value your feedback! Please share your thoughts about this app or the dashboard.</p>",
        unsafe_allow_html=True,
    )
    if not firebase_admin._apps:
        cred = credentials.Certificate("dashboard-explorer-4f089ffb4fcb.json")
        firebase_admin.initialize_app(cred)

    db = firestore.client()

    # --- Feedback form ---
    with st.form("feedback_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email (optional)")
        rating = st.slider("Rate your experience", 1, 5, 3)
        comments = st.text_area("Your Feedback")

        submitted = st.form_submit_button("Submit Feedback")

        if submitted:
            feedback_entry = {
                "Name": name,
                "Email": email,
                "Rating": rating,
                "Comments": comments,
                "Timestamp": datetime.datetime.now().isoformat(),
            }

            try:
                db.collection("feedback").add(feedback_entry)
                st.success("✅ Thank you for your feedback!")
            except Exception as e:
                st.error(f"❌ Failed to save feedback: {e}")
