import streamlit as st
import Dashboard
import streamlit.components.v1 as components

# --- Set wide page layout ---
st.set_page_config(
    page_title="Global Inequality Explorer",
    layout="wide",  # Makes the Streamlit app full width
    initial_sidebar_state="auto"
)

def show():
    # --- Set background color and text color ---
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #001f3f;  /* Navy blue background */
            color: #4facfe;              /* Blue text */
        }
        .stApp * {
            color: #00b8d9 !important;   /* Ensure all text elements are blue */
        }

        header[data-testid="stHeader"] {
            display: none;  /* Show header (Deploy, 3 dots) */
        }
        div[data-testid="stToolbar"] {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- Page Header ---
    st.markdown("""
<div style="
    background-color: rgba(255,255,255,0.1);
    padding: 25px;
    border-radius: 15px;
    text-align:center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    margin-bottom: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
">
    <h1 style="margin:0; padding:0;">🏠 Welcome to Global Inequality Explorer</h1>
</div>
""", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # --- Lottie Animation ---
    components.html(
    """
    <div style="
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        padding: 0;
    ">
        <script
            src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.6.2/dist/dotlottie-wc.js"
            type="module"
        ></script>
        <dotlottie-wc
            src="https://lottie.host/9af34b4f-5ef9-45da-8711-c61b300d044d/KT9y2ORJPF.lottie"
            style="width: 100%; max-width: 900px; height: 400px;"
            speed="1"
            autoplay
            loop
        ></dotlottie-wc>
    </div>
    """,
    height=450,
)

    # --- Subtitle ---
    st.subheader("🌍 Explore Global Income Disparities")

    # --- Description about dashboard ---
    st.write(
        """
        This dashboard provides an in-depth exploration of income inequality across countries over the years. With comprehensive data covering 189 countries, it allows users to analyze trends, identify regions with the highest and lowest inequality, and compare countries on a global scale. By examining disparities across continents and over time, users can gain meaningful insights into patterns of wealth distribution, socio-economic factors, and policy impacts. Whether you are a researcher, policymaker, or curious explorer, this interactive platform offers a clear and engaging way to understand the complexities of global income inequality.
        """
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Key Statistic Cards ---
    col1, col2, col3, col4 = st.columns(4)
    
    # Card 1: Total countries
    with col1:
        st.markdown("""
        <div style="
    background-color: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 12px;
    text-align:center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    min-height: 150px;  /* ensures all cards are same height */
    display: flex;
    flex-direction: column;
    justify-content: center;  /* center content vertically */
">
    <h3>📊 Countries</h3>
    <h2>189</h2>
</div>
        """, unsafe_allow_html=True)

    # Card 2: Highest inequality
    with col2:
        st.markdown("""
        <div style="
    background-color: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 12px;
    text-align:center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    min-height: 178px;
    display: flex;
    flex-direction: column;
    justify-content: center;
">
            <h3>⚠️ Highest Inequality</h3>
            <h4>Zambia (3.66 in 2017)</h4>
        </div>
        """, unsafe_allow_html=True)

    # Card 3: Lowest inequality
    with col3:
        st.markdown("""
        <div style="
    background-color: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 12px;
    text-align:center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    min-height: 178px;
    display: flex;
    flex-direction: column;
    justify-content: center;
">
            <h3>✅ Lowest Inequality</h3>
            <h4>Myanmar</h4>
        </div>
        """, unsafe_allow_html=True)

    # Card 4: Average inequality
    with col4:
        st.markdown("""
        <div style="
    background-color: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 12px;
    text-align:center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    min-height: 178px;
    display: flex;
    flex-direction: column;
    justify-content: center;
">
            <h3>📈 Average Index</h3>
            <h4>0.74</h4>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- Key Features / Dashboard Info ---
    st.markdown("### ✨ Dashboard Features")
    st.markdown("""
    - 📊 **Interactive Dashboard** – Filter by country, year, or inequality level.  
    - 🌐 **Global Coverage** – Analyze disparities across continents and hemispheres.  
    - 📈 **Trends & Comparisons** – Identify high, medium, and low inequality zones.  
    - 🔎 **Drilldown Analysis** – Explore country-level insights in detail.  
    - 🚀 **Visualizations** – Maps, bar charts, line plots, and scatter plots for deep analysis.
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Get Started Prompt ---
    st.write("🚀 **Get Started**")
    st.write("👉 Use the navigation menu at the top to explore the Dashboard.")

    st.markdown('</div>', unsafe_allow_html=True)
