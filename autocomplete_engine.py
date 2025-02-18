from collections import defaultdict
import random

class AutocompleteEngine:
    """Provides intelligent autocomplete suggestions based on document words."""

    def __init__(self, words):
        self.words = list(set(words))  # Remove duplicates
        self.word_freq = defaultdict(int)

        for word in words:
            self.word_freq[word] += 1

        self.user_feedback = defaultdict(int)

    def get_suggestions(self, input_tokens, top_k=5):
        """Returns top-k autocomplete suggestions based on input context."""
        if not input_tokens:
            return []

        # Ensure last_word is a string
        last_word = input_tokens[-1] if isinstance(input_tokens[-1], str) else str(input_tokens[-1])

        # Find words that frequently appear after the last word
        possible_suggestions = [
            word for word in self.words if word.startswith(last_word)
        ]

        if not possible_suggestions:
            return random.sample(self.words, min(top_k, len(self.words)))  # Return random words if no match

        ranked_suggestions = sorted(
            possible_suggestions, key=lambda x: (self.word_freq[x] + self.user_feedback[x]), reverse=True
        )

        return ranked_suggestions[:top_k]

    def update_feedback(self, selected_suggestion):
        """Updates user feedback to improve suggestion rankings."""
        self.user_feedback[selected_suggestion] += 1
