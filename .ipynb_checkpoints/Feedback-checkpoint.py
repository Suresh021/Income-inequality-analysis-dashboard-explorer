import streamlit as st
import pandas as pd
import datetime

def show():


    st.markdown(
        """
        <style>
        .stApp {
            background-color: #001f3f;  /* Navy blue background */             
        }

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
        margin-left: 220px;
        transition: 0.3s !important;
    }

    div.stButton > button:hover,
    div.stForm .stFormSubmitButton button:hover {
        background: linear-gradient(90deg, #ff416c, #ff4b2b) !important;
        color: white !important;
    }

        
        </style>
        """,
        unsafe_allow_html=True
)
    
    st.markdown(
    "<h1 style='color:#00b8d9;'>📝 Feedback</h1>",
    unsafe_allow_html=True
)
    st.write("We value your feedback! Please share your thoughts about this app or the dashboard.")

    # Feedback form
    with st.form("feedback_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email (optional)")
        rating = st.slider("Rate your experience", 1, 5, 3)
        comments = st.text_area("Your Feedback")

        submitted = st.form_submit_button("Submit Feedback")

        if submitted:
            # Save feedback to CSV (or database)
            feedback_entry = {
                "Name": name,
                "Email": email,
                "Rating": rating,
                "Comments": comments,
                "Timestamp": datetime.datetime.now()
            }

            # Append feedback to a CSV file
            try:
                df = pd.read_csv("feedback.csv")
                df = df.append(feedback_entry, ignore_index=True)
            except FileNotFoundError:
                df = pd.DataFrame([feedback_entry])

            df.to_csv("feedback.csv", index=False)

            st.success("✅ Thank you for your feedback!")
