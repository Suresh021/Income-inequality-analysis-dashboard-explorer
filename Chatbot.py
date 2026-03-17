import time

import pandas as pd
import streamlit as st
from openai import OpenAI


@st.cache_data
def load_dataset():
    df = pd.read_csv("cleaned_income_inequality.csv")
    return df


df = load_dataset()

# --- OpenAI API Key ---
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
# --- Keywords for dataset relevance ---
dataset_keywords = [
    "inequality",
    "country",
    "countries",
    "iso3",
    "continent",
    "hemisphere",
    "human development groups",
    "undp developing regions",
    "hdi rank",
    "pca",
    "cluster",
    "inequality status",
    "average",
    "mean",
    "sum",
    "total",
    "highest",
    "lowest",
    "max",
    "min",
    "value",
]


def summarize_dataset(df: pd.DataFrame):
    summary = {"columns": list(df.columns), "rows": len(df)}

    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    categorical_cols = df.select_dtypes(exclude=["number"]).columns.tolist()

    numeric_summary = {}
    for col in numeric_cols:
        col_stats = df[col].describe().to_dict()
        max_idx = df[col].idxmax()
        min_idx = df[col].idxmin()
        col_stats["max_row"] = df.loc[max_idx].to_dict()
        col_stats["min_row"] = df.loc[min_idx].to_dict()
        numeric_summary[col] = col_stats

    summary["numeric_summary"] = numeric_summary
    summary["categorical_summary"] = {
        col: df[col].value_counts().head(10).to_dict() for col in categorical_cols
    }

    return summary


dataset_summary = summarize_dataset(df)


# --- GPT with dataset context ---
def ask_gpt_with_dataset(query):
    prompt = f"""
    You are a data analysis assistant.
    The user asked: "{query}"

    Here is a structured summary of the dataset:
    - Number of rows: {dataset_summary["rows"]}
    - Columns: {dataset_summary["columns"]}

    Numeric summary (min, max, mean, std):
    {dataset_summary["numeric_summary"]}

    Categorical summary (top categories):
    {dataset_summary["categorical_summary"]}

    Instructions:
    - If the question is mathematical (average, highest, lowest, min, max, sum, total, value),
      use the numeric summary to give the exact answer.
    - If it is descriptive (hemisphere, continent, clusters, HDI, etc.), use the categorical info.
    - Always ground your answer in the dataset.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI data analyst."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )
    return response.choices[0].message.content.strip()


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
        .chat-input-container {
            display: flex;
            align-items: center;
            border-radius: 25px;
            background-color: #ffffff;
            padding: 5px 10px;
            margin-top: 10px;
            position: fixed;
            bottom: 10px;
            width: 95%;
            max-width: 1200px;
        }
        .chat-input-container input {
            flex: 1;
            border: none;
            outline: none;
            font-size: 16px;
            background-color: transparent;
            color: #001f3f;
            padding: 8px;
            border-radius: 25px;
        }
        .chat-input-container button {
            background-color: #007bff;
            color: #ffffff;
            border: none;
            border-radius: 20px;
            padding: 8px 16px;
            margin-left: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .chat-input-container button:hover {
            background-color: #0056b3;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.title("🤖 AI Data Analyst Chatbot")
    with col2:
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history = []

    st.markdown(
        "<p style='font-size:18px;'>Ask anything about your dataset or general data analysis questions.</p>",
        unsafe_allow_html=True,
    )

    col_input, col_button = st.columns([16, 1])
    with col_input:
        user_input = st.text_input(
            "", key="chat_input", placeholder="Ask a question about the data..."
        )
    with col_button:
        st.markdown(
            """
        <style>
        .send-button {
            margin-top: 30px;  
            width: 40px;     
            height: 40px;     
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 8px;  
            font-size: 20px;
            cursor: pointer;
            text-align: center;
        }
        .send-button:hover {
            background-color: #0056b3;
        }
        </style>
        <button class="send-button" onclick="window.parent.postMessage({isInput:true,value:document.getElementById('chat_input').value}, '*'); document.getElementById('chat_input').value='';">➤</button>
        """,
            unsafe_allow_html=True,
        )

    # --- Process input ---
    if user_input:
        if any(word in user_input.lower() for word in dataset_keywords):
            placeholder = st.empty()
            with placeholder.container():
                with st.spinner("🤖 Thinking..."):
                    gpt_answer = ask_gpt_with_dataset(user_input)
            st.session_state.chat_history.append(
                {"user": user_input, "bot": gpt_answer}
            )
            placeholder.empty()
        else:
            warning_msg = (
                "⚠️ I can only answer questions related to the dataset "
                "(inequality, countries, continents, HDI, PCA, clusters, hemispheres, etc.)."
            )
            st.session_state.chat_history.append(
                {"user": user_input, "bot": warning_msg}
            )

    # --- Display chat history ---
    for chat in st.session_state.chat_history:
        st.markdown(
            f"""
            <div style="
                background-color: rgba(0, 128, 255, 0.2);
                padding: 20px;
                border-radius: 15px;
                margin-bottom: 10px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                display: flex;
                align-items: center;
            ">
                <span style="font-size: 28px; color: #007bff; margin-right: 10px;">👨‍💻:</span>
                <span>{chat["user"]}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            f"""
            <div style="
                display: flex;
                margin-bottom: 10px;
            ">
                <span style="font-size: 28px; color: #007bff; margin-right: 10px;">🤖:</span>
                <span>{chat["bot"]}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
