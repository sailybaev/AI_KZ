import streamlit as st
from llama_model import ask_llama
from vector_store import init_vector_store, embed_constitution, search_context

st.title("🇰🇿 Constitution of Kazakhstan AI Assistant")

st.info("Loading Constitution...")
collection = init_vector_store()
embed_constitution(collection)
st.success("Ready!")

query = st.text_input("Ask a question about the Constitution:")
if query:
    st.write("🔍 Searching for relevant context...")
    context = search_context(query, collection)
    st.text_area("Context", context, height=200)

    st.write("🧠 Asking LLaMA...")
    answer = ask_llama(context, query)
    st.markdown(f"**Answer:** {answer}")
