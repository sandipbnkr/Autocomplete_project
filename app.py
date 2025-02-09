import streamlit as st
from pdf_preprocessing import extract_text_from_pdf, preprocess_text
from autocomplete_engine import AutocompleteEngine
from llm_integration import LLMIntegration
import nltk
nltk.download()

# Streamlit App
st.title("Context-Aware Autocomplete System")
st.write("Upload a PDF document and start typing to get autocomplete suggestions.")

# Upload PDF#
uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")
#from tabula import read_pdf
#uploaded_file = read_pdf(r'Test-driven development.pdf')

if uploaded_file is not None:
    # Extract and preprocess text
    text = extract_text_from_pdf(uploaded_file)  # Pass the file object
    words = preprocess_text(text)

    # Initialize autocomplete engine
    autocomplete_engine = AutocompleteEngine(words)

    # Initialize LLM integration
    llm_integration = LLMIntegration(model_name="distilgpt2")  # Use DistilGPT-2

    # User input
    user_input = st.text_input("Start typing...", key="user_input")

    if user_input:
        # Get autocomplete suggestions
        prefix = user_input.split()[-1]  # Use the last word as the prefix
        suggestions = autocomplete_engine.get_suggestions(prefix, top_k=5)

        # Display autocomplete suggestions
        st.write("Autocomplete Suggestions:")
        for suggestion in suggestions:
            if st.button(suggestion):
                # Update user feedback
                autocomplete_engine.update_feedback(suggestion)
                st.write(f"You selected: {suggestion}")

        # Get LLM-based suggestions
        llm_suggestion = llm_integration.generate_suggestions(user_input)
        st.write("LLM-Based Suggestion:")
        st.write(llm_suggestion)

        # Real-time typing assistance
        st.write("Real-Time Typing Assistance:")
        st.write(f"Next word suggestions: {suggestions}")