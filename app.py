import streamlit as st
from main import process_query

# =========================
# 🎨 UI SETUP
# =========================
st.set_page_config(page_title="Chat with Real Estate Data", layout="centered")

st.title("💬 Chat with Pune Real Estate Leads")
st.write("Ask questions about your customer / lead data")

# =========================
# 💬 INPUT BOX
# =========================
user_input = st.text_input("Enter your question:")

# =========================
# 🚀 PROCESS OUTPUT
# =========================
if user_input:
    with st.spinner("Thinking... 🤖"):
        result = process_query(user_input)

    st.subheader("📊 Result")
    st.write(result)