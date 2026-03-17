import streamlit as st

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
        
        </style>
        """,
        unsafe_allow_html=True
)
    
    st.markdown(
    """<h2 style='margin-left: 100px; color: #00b8d9'>📊 Income Inequality Dashboard </h2>
    <p style='margin-left: 200px; color: grey'>Visualizing global disparities interactively</p>""",
    unsafe_allow_html=True
)

    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
            <iframe title="PowerBI" 
                    width="600" height="400" 
                    src="https://app.powerbi.com/view?r=eyJrIjoiZTg1NjBmNTctMjllNy00Y2NiLTkxMmMtNmNhOWI3NDIzOWMwIiwidCI6ImUxNGU3M2ViLTUyNTEtNDM4OC04ZDY3LThmOWYyZTJkNWE0NiIsImMiOjEwfQ%3D%3D&pageName=2bb89e9f31152786e32e"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )

    show_insights()


def show_insights():
    # Divider
    st.markdown("---")


    st.markdown(
    """<h3 style='margin-left: 250px; color: #00b8d9'>🔍 Key Insights </h3>
    """,
    unsafe_allow_html=True
)

    # Reusable CSS for boxes
    box_style = "padding:15px; border-radius:10px; color:white; margin-bottom:15px; min-height:150px;"

    # === First Dashboard (Overall Summary) ===
    st.markdown("### 📌 First Dashboard: Overall Summary")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            <div style="background:#1f77b4; {box_style}">
                🌍 <b>Global Coverage</b><br>
                Dataset includes <b>189 countries</b>.
            </div>
            """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div style="background:#ff7f0e; {box_style}">
                📊 <b>Average Inequality</b><br>
                Global average inequality is <b>0.74</b>.
            </div>
            """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        st.markdown(f"""
            <div style="background:#2ca02c; {box_style}">
                📈 <b>Extremes</b><br>
                Highest: Zambia<br>
                Lowest: Myanmar
            </div>
            """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
            <div style="background:#d62728; {box_style}">
                🌐 <b>Continent Inequality</b><br>
                America & Europe → High<br>
                Oceania → Lowest<br>
                Africa → Relatively high
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # === Second Dashboard (Trends & Breakdown) ===
    st.markdown("### 📌 Second Dashboard: Trends & Deeper Breakdown")
    st.markdown("---")

    col5, col6 = st.columns(2)
    with col5:
        st.markdown(f"""
            <div style="background:#17becf; {box_style}">
                🌍 <b>Regional Inequality</b><br>
                Highest: LAC (0.97)<br>
                East Asia & Pacific (0.91)<br>
                Lowest: Arab States (0.34), South Asia (0.43)
            </div>
            """, unsafe_allow_html=True)
    with col6:
        st.markdown(f"""
            <div style="background:#bcbd22; {box_style}">
                ⏳ <b>Trends 2010–2020</b><br>
                Africa & America → Consistently high<br>
                Europe → Lowest<br>
                Asia → Gradual improvement
            </div>
            """, unsafe_allow_html=True)

    col7, col8 = st.columns(2)
    with col7:
        st.markdown(f"""
            <div style="background:#8c564b; {box_style}">
                🌐 <b>Country Examples</b><br>
                Afghanistan → Low inequality<br>
                Albania → High<br>
                Algeria → High<br>
                Andorra → Low
            </div>
            """, unsafe_allow_html=True)
    with col8:
        st.markdown(f"""
            <div style="background:#e377c2; {box_style}">
                📊 <b>PCA Distribution</b><br>
                Africa & Asia → Diverse patterns<br>
                Europe & Oceania → Clustered tightly
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # === Third Dashboard (Policy & Recommendations) ===
    st.markdown("### 📌 Third Dashboard: Drilldown and Hemisphere Analysis")
    st.markdown("---")

    col9, col10 = st.columns(2)
    with col9:
        st.markdown(f"""
            <div style="background:#7f7f7f; {box_style}">
                📊 <b>Inequality Extremes</b><br>
                Max inequality = 3.66,<br>
                Min inequality = -2.36.
            </div>
            """, unsafe_allow_html=True)
    with col10:
        st.markdown(f"""
            <div style="background:#9467bd; {box_style}">
            🌍 <b>Hemisphere Split</b><br>
            81.4% of countries in the<br>
            Southern Hemisphere, 18.5% in the North.
        </div>
        """, unsafe_allow_html=True)

    col11, col12 = st.columns(2)
    with col11:
        st.markdown(f"""
            <div style="background:#ff9896; {box_style}">
            📈 <b>Hemisphere Inequality</b><br>
            Southern Hemisphere avg index ≈ 0.9<br>
            vs Northern Hemisphere ≈ 0.7.
        </div>
        """, unsafe_allow_html=True)
    with col12:
        st.markdown(f"""
            <div style="background:#98df8a; {box_style}">
            🔎 <b>Country Drilldown</b><br>
            Zambia shows highest inequality (3.66 in 2017).<br>
            Brazil & Lesotho also above average.
        </div>
        """, unsafe_allow_html=True)