from collections import Counter
def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word

def find_most_prevalent_word(text):
    words = text.split()
    word_counts = Counter(words)  # Count occurrences of each word
    most_prevalent_word = word_counts.most_common(1)[0]  # Get the most common word and its count
    return most_prevalent_word
