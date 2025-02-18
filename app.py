import streamlit as st
import nltk
import logging
from pdf_preprocessing import extract_text_from_pdf, preprocess_text
from autocomplete_engine import AutocompleteEngine
from llm_integration import LLMIntegration

# Configure logging
logging.basicConfig(level=logging.INFO)

# Download required NLTK datasets
nltk.download('punkt')
nltk.download('stopwords')

# Streamlit UI
st.title("📖 Context-Aware Autocomplete System")
st.write("Upload a PDF document and start typing to get autocomplete suggestions.")

# Upload PDF file
uploaded_file = st.file_uploader("📂 Upload a PDF document", type="pdf")

# Initialize objects
autocomplete_engine = None
llm_integration = LLMIntegration(model_name="distilgpt2")

if uploaded_file:
    try:
        # Extract and preprocess text
        text = extract_text_from_pdf(uploaded_file)
        words = preprocess_text(text)

        # Initialize autocomplete engine with unique words
        autocomplete_engine = AutocompleteEngine(words)

        st.success("✅ PDF processed successfully! Start typing below.")

    except Exception as e:
        st.error(f"⚠️ An error occurred while processing the PDF: {str(e)}")
        logging.error(f"PDF Processing Error: {str(e)}")

# User input field
user_input = st.text_input("✍ Start typing...", key="user_input")

if user_input and autocomplete_engine:
    input_tokens = user_input.lower().split()  # Convert input to lowercase tokens

    # Get autocomplete suggestions based on previous words in input
    suggestions = autocomplete_engine.get_suggestions(input_tokens, top_k=5)

    if suggestions:
        st.write("### 🔍 Autocomplete Suggestions:")
        for i, suggestion in enumerate(suggestions):
            if st.button(suggestion, key=f"suggestion_{i}"):
                autocomplete_engine.update_feedback(suggestion)
                st.success(f"✅ Selected Suggestion: **{suggestion}**")

    else:
        st.warning("⚠️ No autocomplete suggestions available.")

    # Get LLM-based suggestion
    llm_suggestion = llm_integration.generate_suggestions(user_input)
    st.write("### 🤖 LLM-Based Suggestion:")
    st.write(llm_suggestion)
