def chunk_text(text, max_length=512):
    """Split text into chunks of max_length tokens."""
    words = text.split()
    chunks = [" ".join(words[i:i + max_length]) for i in range(0, len(words), max_length)]
    return chunks

