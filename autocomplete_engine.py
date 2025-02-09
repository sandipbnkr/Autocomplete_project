from collections import defaultdict

class AutocompleteEngine:
    def __init__(self, words):
        """
        Initializes the autocomplete engine with a list of words.
        """
        self.words = words
        self.word_freq = defaultdict(int)
        for word in words:
            self.word_freq[word] += 1
        self.user_feedback = defaultdict(int)  # Store user feedback

    def get_suggestions(self, prefix, top_k=5):
        """
        Returns top-k suggestions for a given prefix.
        """
        suggestions = [word for word in self.words if word.startswith(prefix)]
        # Combine word frequency and user feedback for ranking
        suggestions = sorted(suggestions, key=lambda x: (self.word_freq[x] + self.user_feedback[x]), reverse=True)[:top_k]
        return suggestions

    def update_feedback(self, selected_suggestion):
        """
        Updates user feedback for a selected suggestion.
        """
        self.user_feedback[selected_suggestion] += 1