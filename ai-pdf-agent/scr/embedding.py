def generate_embeddings(text_chunks, model_name="all-mpnet-base-v2"):
    """Generate embeddings for text chunks."""
    model = SentenceTransformer(model_name)
    embeddings = model.encode(text_chunks)
    return embeddings