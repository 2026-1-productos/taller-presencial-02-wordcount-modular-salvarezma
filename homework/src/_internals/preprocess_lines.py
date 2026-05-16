import re


def preprocess_lines(lines):
    """Preprocess lines by normalizing and cleaning text."""
    cleaned_lines = []
    for line in lines:
        lower_line = line.lower()
        # Replace any non-letter character with spaces for consistent tokenization.
        normalized_line = re.sub(r"[^a-z]+", " ", lower_line)
        cleaned_lines.append(normalized_line.strip())
    return cleaned_lines