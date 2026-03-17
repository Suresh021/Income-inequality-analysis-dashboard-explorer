# Help.py

import firebase_admin
import streamlit as st
from firebase_admin import credentials, firestore

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("dashboard-explorer-4f089ffb4fcb.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()


def show():
    # --- Page styling ---
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #001f3f;  /* Navy blue background */
        }
        header[data-testid="stHeader"] {
            display: none;  /* Hide header */
        }
        div[data-testid="stToolbar"] {
            display: none;  /* Hide toolbar */
        }

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
        margin-left: 450px;
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

    st.markdown(
        "<h1 style='color:#FFFFFF;'>🆘 Help & Guide</h1>", unsafe_allow_html=True
    )
    st.markdown(
        "<p style='font-size:18px;'>Report any issues, bugs, or get guidance on using the app.</p>",
        unsafe_allow_html=True,
    )

    with st.form("help_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        issue_type = st.selectbox(
            "Issue Type", ["Bug", "Feature Request", "Question / Guidance"]
        )
        description = st.text_area("Describe the issue in detail")
        submit = st.form_submit_button("Submit")

    if submit:
        if not name or not email or not description:
            st.error("Please fill in all required fields.")
        else:
            try:
                db.collection("app_issues").add(
                    {
                        "name": name,
                        "email": email,
                        "issue_type": issue_type,
                        "description": description,
                        "status": "Pending",
                    }
                )
                st.success(
                    "Your issue has been submitted! Our team will get back to you soon."
                )
            except Exception as e:
                st.error(f"Error submitting issue: {e}")
