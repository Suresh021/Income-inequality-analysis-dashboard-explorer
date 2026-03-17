import streamlit as st
import streamlit.components.v1 as components


def show():
    st.markdown('<a id="top-of-page"></a>', unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .stApp {
            background-color: #001f3f; 
            color: #4facfe; 
        }
        .stApp * {
            color: #FFFFFF !important;
        }
        header[data-testid="stHeader"] {
            display: none;
        }
        div[data-testid="stToolbar"] {
            display: none;
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
            display: flex;
            justify-content: center;
            align-items: center;
        ">
            <h1 style="margin:0; padding:0;">🏠 Welcome to Global Inequality Explorer</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

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
            <script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.6.2/dist/dotlottie-wc.js" type="module"></script>
            <dotlottie-wc src="https://lottie.host/9af34b4f-5ef9-45da-8711-c61b300d044d/KT9y2ORJPF.lottie"
            style="width: 100%; max-width: 900px; height: 400px;" speed="1" autoplay loop>
            </dotlottie-wc>
        </div>
        """,
        height=450,
    )

    st.subheader("🌍 Explore Global Income Disparities")

    st.markdown(
        """
    <div style="font-size:18px; line-height:1.6; text-align:justify;">
        This dashboard provides an in-depth exploration of income inequality 
        across countries over the years. With comprehensive data covering 189 countries, 
        it allows users to analyze trends, identify regions with the highest and lowest inequality, 
        and compare countries on a global scale. By examining disparities across continents and over time, 
        users can gain meaningful insights into patterns of wealth distribution, socio-economic factors, 
        and policy impacts. Whether you are a researcher, policymaker, or curious explorer, this interactive 
        platform offers a clear and engaging way to understand the complexities of global income inequality.
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Key Statistic Cards ---
    col1, col2, col3, col4 = st.columns(4)

    # Card 1: Countries covered
    col1.markdown(
        """
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
        <h3>🌐 Countries Covered</h3>
        <h4>189</h4>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Card 2: Highest inequality
    col2.markdown(
        """
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
        """,
        unsafe_allow_html=True,
    )

    # Card 3: Lowest inequality
    col3.markdown(
        """
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
        """,
        unsafe_allow_html=True,
    )

    # Card 4: Average inequality
    col4.markdown(
        """
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
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- App Features / Key Capabilities ---
    st.markdown("### ✨ Key Capabilities")
    col1, col2 = st.columns(2)

    with col1:
        # Dashboard Page Card
        st.markdown(
            """
            <div style="
                background-color: rgba(255,255,255,0.1);
                padding: 20px;
                border-radius: 12px;
                text-align:center;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                min-height: 180px;
                margin-bottom: 20px;
            ">
    <h3>📊 Data Exploration</h3>
    <p style="font-size:18px; line-height:1.6; text-align:Center;">
        Interactive dashboard for filtering, visualization, and trend analysis.
    </p>
</div>
""",
            unsafe_allow_html=True,
        )

        # Chatbot page card
        st.markdown(
            """
            <div style="
                background-color: rgba(255,255,255,0.1);
                padding: 20px;
                border-radius: 12px;
                text-align:center;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                min-height: 180px;
            ">
                <h3>🤖 Intelligent Assistant</h3>
                <p style="font-size:18px; line-height:1.6; text-align:Center;">
        AI-powered chatbot to answer queries and provide instant insights.
    </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        # Feedback Page card
        st.markdown(
            """
            <div style="
                background-color: rgba(255,255,255,0.1);
                padding: 20px;
                border-radius: 12px;
                text-align:center;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                min-height: 180px;
                margin-bottom: 20px;
            ">
                <h3>📝 User Feedback</h3>
                <p style="font-size:18px; line-height:1.6; text-align:Center;">
        Collect suggestions and evaluations to continuously improve the platform.
    </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Help Page Card
        st.markdown(
            """
            <div style="
                background-color: rgba(255,255,255,0.1);
                padding: 20px;
                border-radius: 12px;
                text-align:center;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                min-height: 180px;
            ">
                <h3>🆘 Support & Assistance</h3>
                <p style="font-size:18px; line-height:1.6; text-align:Center;">
        Dedicated help section for reporting issues and accessing guidance.
    </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # --- Scenario Lab Card ---
        st.markdown(
            """
            <div style="
                background-color: rgba(255,255,255,0.1);
                padding: 20px;
                border-radius: 12px;
                text-align:center;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                min-height: 180px;
                margin-top: 20px;
            ">
                <h3>🧪 Scenario Lab</h3>
                <p style="font-size:18px; line-height:1.6; text-align:Center;">
        Explore “what-if” scenarios by adjusting a country’s inequality values and 
                instantly seeing the impact on global metrics. Analyze trends, simulate policy changes, 
                and visualize outcomes interactively.
    </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)

    # --- Scroll to top button using anchor ---
    st.markdown(
        """
        <div style="text-align:center; margin-top:30px;">
            <a href="#top-of-page">
                <button style="
                background: linear-gradient(135deg, #4facfe, #00f2fe);
                color: white;
                border: none;
                padding: 12px 25px;
                border-radius: 10px;
                font-size: 18px;
                cursor: pointer;
                font-weight: bold;
                ">
                    🚀 Get Started
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<h5 style="text-align: center;"> Use the Navigation Bar at the Top to Navigate to Other Pages</h5>',
        unsafe_allow_html=True,
    )
