"""""
Week 8 - Simple RAG Application (Streamlit version)

This is the OPTIONAL "basic Streamlit interface" version mentioned in the Week 8 task. 
It does the same thing but shows a small web page instead of a text-based loop.

How to run this file (not a notebook — run it from a terminal):
    streamlit run streamlit_app.py

Before running:
1. Run Week_8_01_Document_Setup.ipynb once, so week8_rag_db has documents in it.
"""

import os
import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
from google import genai
from google.genai.errors import APIError
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# heading at the top of the page.
st.header("Simple RAG Question Answering App")
st.write("Ask a question about the documents you added in Notebook 01.")

if not api_key:
    st.error("No GEMINI_API_KEY found. Please add it to your .env file.")
    st.stop()


# @st.cache_resource means: only load these heavy things ONCE, even if the
# page reruns many times (Streamlit reruns the whole script on every click).
@st.cache_resource
def load_resources():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    gemini_client = genai.Client(api_key=api_key)
    db_client = chromadb.PersistentClient(path="./week8_rag_db")
    collection = db_client.get_or_create_collection(name="week8_documents")
    return model, gemini_client, collection


embedding_model, gemini_client, collection = load_resources()

# Error handling:
if collection.count() == 0:
    st.warning("No documents found yet. Run Week_8_01_Document_Setup.ipynb first to add some.")

# st.text_input shows a text box and returns whatever the user typed.
question = st.text_input("Your question:")

# st.button shows a button and returns True only on the click that pressed it.
if st.button("Ask"):
    if not question.strip():
        st.warning("Please type a question first.")
    else:
        try:
            # --- Retrieval step ---
            question_embedding = embedding_model.encode(question).tolist()
            results = collection.query(query_embeddings=[question_embedding], n_results=3)
            chunks = results["documents"][0]
            distances = results["distances"][0]

            if not chunks or min(distances) > 1.1:
                context = None
                st.info("No relevant information found in your documents.")
            else:
                context = "\n".join(f"Context {i}: {c}" for i, c in enumerate(chunks, start=1))
                with st.expander("Retrieved context (click to view)"):
                    st.write(context)

            # --- Generation step ---
            if context:
                prompt = f"""
Answer the question using the retrieved context when it is relevant.
If the context does not contain the answer, use your general knowledge.

Retrieved context:
{context}

Question:
{question}

Give a concise and accurate answer.
"""
            else:
                prompt = f"""
No relevant information was found in the user's documents for this question.
Answer using your general knowledge, and briefly mention that this answer is
not based on the user's own documents.

Question:
{question}
"""

            response = gemini_client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

            st.subheader("Answer")
            st.write(response.text if response.text else "The model returned an empty answer.")

        except APIError as error:
            st.error(f"Gemini API error: {error}")
        except Exception as error:
            st.error(f"Something went wrong: {error}")
