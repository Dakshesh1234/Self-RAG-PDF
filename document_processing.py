from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text_into_documents(text):
    """
    Splits text into smaller chunks for processing.

    Args:
        text (str): The text to split.

    Returns:
        List[Document]: A list of Document objects.
    """
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=250, chunk_overlap=50
    )
    doc_splits = text_splitter.create_documents([text])
    return doc_splits