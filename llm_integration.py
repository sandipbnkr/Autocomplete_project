from transformers import pipeline
import logging

logging.basicConfig(level=logging.INFO)

class LLMIntegration:
    """Handles integration with an LLM (e.g., GPT-2) for generating text suggestions."""

    def __init__(self, model_name="distilgpt2"):
        try:
            self.generator = pipeline("text-generation", model=model_name)
            logging.info(f"✅ LLM Model {model_name} loaded successfully.")
        except Exception as e:
            logging.error(f"⚠️ LLM Model Load Failed: {str(e)}")
            self.generator = None

    def generate_suggestions(self, prompt, max_tokens=20):
        """Generates autocomplete suggestions using an LLM."""
        if not self.generator:
            return "⚠️ LLM model unavailable."

        try:
            result = self.generator(prompt, max_length=max_tokens, num_return_sequences=1)
            return result[0]['generated_text'] if result else "⚠️ No suggestion available."
        except Exception as e:
            logging.error(f"⚠️ LLM Error: {str(e)}")
            return "⚠️ Failed to generate suggestions."
