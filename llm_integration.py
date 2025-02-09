from transformers import pipeline

class LLMIntegration:
    def __init__(self, model_name="distilgpt2"):
        """
        Initializes the LLM integration with a small open-source model.
        """
        self.generator = pipeline("text-generation", model=model_name)

    def generate_suggestions(self, prompt, max_tokens=20):
        """
        Generates suggestions using the small open-source model.
        """
        return self.generator(prompt, max_length=max_tokens, num_return_sequences=1)[0]['generated_text']