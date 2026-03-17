import streamlit as st
import pandas as pd
import openai
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.schema import Document

# --- Setup API Key ---
openai.api_key = st.secrets["OPENAI_API_KEY"]  # put your key in .streamlit/secrets.toml

# --- Load dataset once ---
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_income_inequality.csv")  # <-- your dataset
    return df

df = load_data()

# --- Build vector store once ---
@st.cache_resource
def build_vectorstore(df):
    # Instead of splitting row by row, we dump the entire dataset as one document
    dataset_text = df.to_csv(index=False)  # convert full dataset to CSV text
    documents = [Document(page_content=dataset_text, metadata={"source": "full_dataset"})]

    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(documents, embeddings)
    return vectorstore

vectorstore = build_vectorstore(df)

# --- Prompt Template ---
prompt_template = """
You are a dataset assistant. Use only the dataset content below to answer.

If the answer is not in the dataset, reply strictly with: "I don’t know."

Dataset content (CSV format):
{context}

Question: {question}
Answer:
"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

# --- LLM ---
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# --- RetrievalQA ---
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 1}),  # only 1 doc (full dataset)
    chain_type="stuff",
    chain_type_kwargs={"prompt": PROMPT},
    return_source_documents=True
)

# --- Streamlit UI ---
st.title("📊 Dataset Q&A Chatbot")
st.markdown("Ask me anything about the dataset. If it's not in the data, I’ll reply *I don’t know.*")

# Session history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_query = st.text_input("💬 Your Question:")

if user_query:
    with st.spinner("Thinking..."):
        result = qa(user_query)
        answer = result["result"]

    # Save history
    st.session_state.chat_history.append((user_query, answer))

# Display chat history
for q, a in st.session_state.chat_history:
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Bot:** {a}")
