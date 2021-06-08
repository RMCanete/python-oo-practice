"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
    >>> wf = WordFinder("words2.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, file):
        """Reads a file and makes an attribute of a list of those words. Prints out the number of words read"""

        list = open(file)
        self.words = self.get_words(list)

        print(f"{len(self.words)} words read")

    def __repr__(self):
        """Representation"""

        return f"<WordFinder is looking at a list of {len(self.words)} words>"

    def get_words(self, list):
        """Create a list of words"""

        return [word.strip() for word in list]

    def random(self):
        """Get a random word"""

        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Special Word Finder will not return blank lines or comments
    
    >>> swf = SpecialWordFinder("words3.txt")
    4 words read

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    """

    def __repr__(self):
        """Representation"""

        return f"<SpecialWordFinder is looking at a list of {len(self.words)} words>"

    def get_words(self, list):
        """Create a list of words without blank lines or comments"""

        return [word.strip() for word in list if word.strip() and not word.startswith("#")]