from langchain.llms import Cohere, HuggingFaceHub
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

def initialize_llm(provider="openai", api_key=None):
    """Initialize LLM based on provider."""
    if provider == "openai":
        return OpenAI(api_key=api_key)
    elif provider == "cohere":
        return Cohere(cohere_api_key=api_key)
    elif provider == "huggingface":
        return HuggingFaceHub(repo_id="gpt2", huggingfacehub_api_token=api_key)
    else:
        raise ValueError(f"Unsupported provider: {provider}")


def create_retriever(docsearch, llm):
    """Create a retriever with contextual compression."""
    compressor = LLMChainExtractor.from_llm(llm)
    retriever = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=docsearch.as_retriever())
    return retriever