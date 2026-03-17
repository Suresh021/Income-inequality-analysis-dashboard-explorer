# scenario_lab.py
import pandas as pd
import plotly.express as px
import streamlit as st


# --- Load dataset ---
@st.cache_data
def load_dataset():
    df = pd.read_csv("cleaned_income_inequality.csv")
    return df


df = load_dataset()


def show():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #001f3f;
        }
        header[data-testid="stHeader"], div[data-testid="stToolbar"] {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Scenario Simulation / Policy Lab")
    st.markdown(
        """
        <p style='font-size:20px; color:white; font-weight:500;'>
            Adjust values and explore the impact on global inequality metrics in real-time.
        </p>
        """,
        unsafe_allow_html=True,
    )

    country = st.selectbox("Select Country", df["Country"].unique())

    year_columns = [col for col in df.columns if col.startswith("Inequality in income")]
    years = [col.split("(")[1].replace(")", "") for col in year_columns]
    selected_year = st.selectbox("Select Year", years)

    year_col = f"Inequality in income ({selected_year})"
    original_value = float(df.loc[df["Country"] == country, year_col].values[0])

    percent_change = st.slider("Percentage Change", -50, 50, 0, step=1)

    new_value = original_value * (1 + percent_change / 100)

    df_scenario = df.copy()
    df_scenario.loc[df_scenario["Country"] == country, year_col] = new_value

    global_avg_before = df[year_col].mean()
    global_avg_after = df_scenario[year_col].mean()

    st.markdown(
        f"<p style='font-size:18px; color:white; font-weight:bold;'>"
        f"Original value for {country} ({selected_year}): {original_value:.2f}</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='font-size:18px; color:white; font-weight:bold;'>"
        f"New value after {percent_change}% change: {new_value:.2f}</p>",
        unsafe_allow_html=True,
    )

    st.subheader("Country Inequality Before vs After")
    bar_df = pd.DataFrame(
        {
            "Scenario": ["Original", "After Change"],
            "Inequality": [original_value, new_value],
        }
    )
    fig1 = px.bar(
        bar_df, x="Scenario", y="Inequality", color="Scenario", text="Inequality"
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Global Average Inequality Over Years")
    global_avg_over_time = df[year_columns].mean().reset_index()
    global_avg_over_time.columns = ["Year", "Original"]
    global_avg_over_time["Year"] = [
        y.split("(")[1].replace(")", "") for y in year_columns
    ]

    global_avg_over_time_scenario = df_scenario[year_columns].mean().reset_index()
    global_avg_over_time_scenario.columns = ["Year", "Scenario"]
    global_avg_over_time_scenario["Year"] = [
        y.split("(")[1].replace(")", "") for y in year_columns
    ]

    fig2 = px.line()
    fig2.add_scatter(
        x=global_avg_over_time["Year"],
        y=global_avg_over_time["Original"],
        mode="lines+markers",
        name="Original",
    )
    fig2.add_scatter(
        x=global_avg_over_time_scenario["Year"],
        y=global_avg_over_time_scenario["Scenario"],
        mode="lines+markers",
        name="Scenario",
    )
    st.plotly_chart(fig2, use_container_width=True)
