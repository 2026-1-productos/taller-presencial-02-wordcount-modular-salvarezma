def split_into_words(lines):
    """Split lines into individual words."""
    words = []
    for line in lines:
        tokens = [word for word in line.split() if word]
        words.extend(tokens)
    return words