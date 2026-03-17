import pandas as pd
import plotly.express as px
import streamlit as st


def show():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #001f3f;    
        }

        header[data-testid="stHeader"] {
            display: none;
        }
        div[data-testid="stToolbar"] {
            display: none;
        }

        .card {
            background: rgba(255,255,255,0.15);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            transition: transform 0.2s;
            text-align: center;
        }
        .card:hover {
            transform: scale(1.03);
            box-shadow: 0 6px 16px rgba(0,0,0,0.4);
        }
        
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
<div style="
    background-color: rgba(255,255,255,0.1);
    padding: 25px;
    border-radius: 15px;
    text-align:center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    margin-bottom: 20px;
    justify-content: center;
    align-items: center;
    gap: 20px;
    flex-wrap: nowrap;
">
    <h1 style='color: #FFFFFF; margin:0; font-weight:bold;'>📊 Income Inequality Dashboard</h1>
    <p style='color: grey; margin:0;font-size:18px;'>Visualizing global disparities interactively</p>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Power BI Embed
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
            <iframe title="PowerBI" 
                    width="600" height="400" 
                    src="https://app.powerbi.com/view?r=eyJrIjoiZTg1NjBmNTctMjllNy00Y2NiLTkxMmMtNmNhOWI3NDIzOWMwIiwidCI6ImUxNGU3M2ViLTUyNTEtNDM4OC04ZDY3LThmOWYyZTJkNWE0NiIsImMiOjEwfQ%3D%3D&pageName=2bb89e9f31152786e32e"></iframe>
        </div>
        """,
        unsafe_allow_html=True,
    )

    show_insights()


def render_card(title, text, color="#1f77b4"):
    st.markdown(
        f"""
        <div class="card" style="background:{color}; padding:15px; border-radius:10px; min-height:150px; margin-bottom:15px; color:white;">
            <h3 style="font-size:22px; font-weight:bold; margin-bottom:10px;">{title}</h3>
            <p style="font-size:18px; line-height:1.5; font-weight:500;">{text}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_insights():
    st.markdown("---")

    st.markdown(
        """<h2 style='margin-left: 540px; color: #FFFFFF; font-weight: bold; font-size:26px;'>🔍 Key Insights </h2>""",
        unsafe_allow_html=True,
    )

    global_coverage = "Dataset includes 189 countries"
    average_inequality = "Global average inequality is 0.74"
    extremes = "Highest: Zambia, Lowest: Myanmar"
    continent_inequality = (
        "America & Europe → High, Oceania → Lowest, Africa → Relatively high"
    )

    # --- Overview Section ---
    st.subheader("🌍 Overview")
    col1, col2 = st.columns(2)
    with col1:
        render_card("🌍 Global Coverage", global_coverage, color="#1f77b4")
    with col2:
        render_card("📊 Average Inequality", average_inequality, color="#17becf")

    col3, col4 = st.columns(2)
    with col3:
        render_card("📈 Extremes", extremes, color="#2ca02c")
    with col4:
        render_card("🌐 Continent Inequality", continent_inequality, color="#bcbd22")

    st.markdown("---")

    # --- Trends Section ---
    st.subheader("📈 Trends & Breakdown")
    col5, col6 = st.columns(2)
    with col5:
        render_card(
            "🌍 Regional Inequality",
            "Highest: LAC (0.97)\nEast Asia & Pacific (0.91)\nLowest: Arab States (0.34), South Asia (0.43)",
            color="#ff7f0e",
        )
    with col6:
        render_card(
            "⏳ Trends 2010–2020",
            "Africa & America → Consistently high\nEurope → Lowest\nAsia → Gradual improvement",
            color="#9467bd",
        )

    col7, col8 = st.columns(2)
    with col7:
        render_card(
            "🌐 Country Examples",
            "Afghanistan → Low inequality\nAlbania → High\nAlgeria → High\nAndorra → Low",
            color="#8c564b",
        )
    with col8:
        render_card(
            "📊 PCA Distribution",
            "Africa & Asia → Diverse patterns\nEurope & Oceania → Clustered tightly",
            color="#e377c2",
        )

    st.markdown("---")

    # --- Policy & Recommendations ---
    st.subheader("🏛️ Policy & Recommendations")
    col9, col10 = st.columns(2)
    with col9:
        render_card(
            "📊 Inequality Extremes",
            "Max inequality = 3.66\nMin inequality = -2.36",
            color="#7f7f7f",
        )
    with col10:
        render_card(
            "🌍 Hemisphere Split",
            "81.4% of countries in Southern Hemisphere, 18.5% in the North",
            color="#bcbd22",
        )

    col11, col12 = st.columns(2)
    with col11:
        render_card(
            "📈 Hemisphere Inequality",
            "Southern Hemisphere avg index ≈ 0.9 vs Northern Hemisphere ≈ 0.7",
            color="#ff9896",
        )
    with col12:
        render_card(
            "🔎 Country Drilldown",
            "Zambia shows highest inequality (3.66 in 2017)\nBrazil & Lesotho also above average",
            color="#98df8a",
        )
