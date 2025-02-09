# Context-Aware Autocomplete System

This application provides context-aware autocomplete suggestions based on the content of a provided PDF document. It uses a small open-source model (DistilGPT-2) for improved suggestions and allows user feedback to refine future suggestions.


     pip install -r requirements.txt
     ```

. Run the Application
 
   - Run the Streamlit app:
   
     streamlit run app.py
    
   - The app will open in your browser automatically. If it doesn’t, copy the URL displayed in the terminal (e.g., `http://localhost:8501`) and paste it into your browser.

Use the Application
   - Upload a PDF document.
   - Start typing in the input box.
   - View autocomplete and LLM-based suggestions.
   - Click on a suggestion to provide feedback.

Features

- PDF text extraction using PyMuPDF.
- Text preprocessing using NLTK.
- Autocomplete suggestions based on the document content.
- Improved suggestions using a small open-source model (DistilGPT-2).
- Real-time typing assistance.
- User feedback to refine future suggestions.

## Requirements

- Python 3.7+
- Streamlit
- PyMuPDF
- NLTK
- Transformers (for DistilGPT-2)