import nltk
from nltk import pos_tag, word_tokenize
from collections import Counter
from typing import Dict
import time

class TextProcessor:
    """Processes text to extract and count proper nouns."""
    
    def __init__(self):
        # Download required NLTK resources
        for resource in ['punkt', 'punkt_tab', 'averaged_perceptron_tagger']:
            nltk.download(resource, quiet=True)
        self.processing_time = 0.0
    
    def extract_proper_nouns(self, text: str) -> Counter:
        """Extracts and counts proper nouns from text."""
        start_time = time.time()
        
        tokens = word_tokenize(text)
        tagged = pos_tag(tokens)
        proper_nouns = [
            word for word, pos in tagged 
            if pos in ['NNP', 'NNPS'] and word.isalpha()
        ]
        
        self.processing_time += time.time() - start_time
        return Counter(proper_nouns)