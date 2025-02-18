import fitz  # PyMuPDF
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import logging

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

logging.basicConfig(level=logging.INFO)

def extract_text_from_pdf(file):
    """Extracts text from a PDF file object."""
    try:
        text = ""
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()

        if not text.strip():
            return "⚠️ No text found in PDF."

        return text.strip()

    except Exception as e:
        logging.error(f"⚠️ PDF Extraction Error: {str(e)}")
        return f"⚠️ PDF extraction error: {str(e)}"

def preprocess_text(text):
    """Tokenizes text and removes stopwords."""
    try:
        words = word_tokenize(text.lower())
        stop_words = set(stopwords.words('english'))
        return [word for word in words if word.isalpha() and word not in stop_words]

    except Exception as e:
        logging.error(f"⚠️ Preprocessing Error: {str(e)}")
        return []
