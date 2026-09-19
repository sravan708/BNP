import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="BNP Finance Copilot")

st.title("🏦 BNP Finance Copilot")

st.info("""
Try commands:

EMI 1000000 8.5 20
COMPOUND 50000 12 10
USD 100
EUR 50
TAX 900000
""")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Enter command...")

if prompt:

    st.session_state.messages.append(
        {"role":"user","content":prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = requests.post(
        API_URL,
        json={"message":prompt}
    )

    reply = response.json()["reply"]

    st.session_state.messages.append(
        {"role":"assistant","content":reply}
    )

    with st.chat_message("assistant"):
        st.write(reply)