from io import StringIO

import pandas as pd
import streamlit as st


def show():
    # --- CSS for background, text, buttons ---
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #001f3f;  /* Navy blue background */
        }
        div.section-box {
    background-color: rgba(255,255,255,0.1);
    padding: 30px;              /* Increased from 20px */
    border-radius: 12px;
    margin-bottom: 30px;        /* Slightly more spacing */
    min-height: 200px;          /* Ensures taller box */
    min-width: 100%;            /* Full width container */
    box-shadow: 0 6px 16px rgba(0,0,0,0.25); /* Slightly bigger shadow */
} 
        /* Apply same style to both regular buttons and download buttons */
    div.stButton > button,
    div.stForm .stFormSubmitButton button,
    div.stDownloadButton > button {
        width: 300px !important;
        background-color: white !important;
        color: black !important;
        font-weight: 900 !important;
        border-radius: 8px !important;
        padding: 10px !important;
        border: 2px solid #4facfe !important;
        margin-top: 5px;
        margin-bottom: 5px;
        margin-left: 150px;
        transition: 0.3s !important;
    }

    div.stButton > button:hover,
    div.stForm .stFormSubmitButton button:hover,
    div.stDownloadButton > button:hover {
        background: linear-gradient(90deg, #4facfe, #00f2fe) !important;
        color: white !important;
    }

header[data-testid="stHeader"] {
            display: none;  /* Show header (Deploy, 3 dots) */
        }
        div[data-testid="stToolbar"] {
            display: none;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- Header ---
    st.markdown(
        """
        <div class="section-box" style="text-align:center;">
            <h1 style='margin: 0;'>🌍 Global Inequality Explorer</h1>
            <p style='margin-top: 10px; font-size:18px;'>Project Overview, Objectives, Methodology, Tools, Data & Author</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- About, Objectives, Methodology, Tools ---
    st.markdown(
        """
        <div class="section-box">
        <h2>📌 About the Project</h2>
        <p style=' font-size:18px;'>This project is a Streamlit-based dashboard to visualize global income inequality.
        It provides interactive visualizations, key insights, and downloadable datasets to help researchers, policymakers, and enthusiasts explore disparities across countries.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="section-box">
        <h2>🎯 Objectives</h2>
        <ul>
            <li style=' font-size:18px;'>Analyze and visualize global income inequality.</li>
            <li style=' font-size:18px;'>Provide interactive dashboards for country-wise comparisons.</li>
            <li style=' font-size:18px;'>Offer AI-generated insights for trends and predictions.</li>
            <li style=' font-size:18px;'>Enable users to access cleaned datasets for further analysis.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="section-box">
        <h2>⚙️ Methodology & Process</h2>
        <ol>
            <li style=' font-size:18px;'>Data Collection from reliable sources (World Bank, UNDP, OECD).</li>
            <li style=' font-size:18px;'>Data Cleaning and preprocessing.</li>
            <li style=' font-size:18px;'>Exploratory Data Analysis (EDA) and visualizations.</li>
            <li style=' font-size:18px;'>AI-assisted insights and trend prediction.</li>
            <li style=' font-size:18px;'>Integration into a Streamlit dashboard with authentication.</li>
        </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="section-box">
        <h2>🛠️ Tools Used</h2>
        <ul>
            <li style=' font-size:18px;'><b>VS Code</b> – Development environment for Python and Streamlit.</li>
            <li style=' font-size:18px;'><b>Jupyter Notebook</b> – Data cleaning, analysis, and EDA.</li>
            <li style=' font-size:18px;'><b>Excel</b> – Data preprocessing and quick analysis.</li>
            <li style=' font-size:18px;'><b>Power BI</b> – Optional for interactive visualizations during exploration.</li>
            <li style=' font-size:18px;'><b>Python Libraries</b> – pandas, numpy, matplotlib, seaborn, plotly, etc.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- Load Dataset ---
    df = pd.read_csv("cleaned_income_inequality.csv")

    # --- Buttons: Explore + Download ---
    col1, col2 = st.columns([1, 1])
    with col1:
        explore_clicked = st.button("👁️ Explore Dataset")
    with col2:
        st.download_button(
            label="📥 Download Cleaned Dataset",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="cleaned_dataset.csv",
            mime="text/csv",
        )

    # --- Show dataset info / preview ---
    if explore_clicked:
        st.subheader("📄 Dataset Preview")
        st.dataframe(df.head(10))

    # --- Author ---
    st.markdown(
        """
        <div class="section-box">
        <h2>👨‍💻 Developer</h2>
        <p><b>Doddi Suresh Kumar</b></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
