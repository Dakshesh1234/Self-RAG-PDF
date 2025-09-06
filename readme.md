# RAG Workflow Q&A

This project is a Streamlit application that uses Retrieval-Augmented Generation (RAG) with Self Reflection to answer questions related to a document. The application retrieves relevant information and generates an answer based on the user's input.

## Prerequisites

- Python 3.7 or higher
- An OpenAI API key

## Installation
1. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

2. Replace the placeholder in the `.env` file with your OpenAI API key:

    ```env
    OPENAI_API_KEY = "your-openai-api-key"
    ```

## Usage

1. Run the Streamlit application:

    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter a question related to your document in the input field and click the "Get Answer" button.

## Project Structure

- `app.py`: The main Streamlit application file.
- `document_processing.py`: Contains functions for processing documents.
- `main.py`: Contains the main workflow logic.
- `nodes.py`: Defines the nodes used in the workflow.
- `pdf_utils.py`: Utility functions for handling PDF files.
- `prompts.py`: Contains prompt templates for the RAG workflow.
- `vectorstore.py`: Manages the vector store for document retrieval.
- `workflow.py`: Defines the workflow for the RAG process.
- `.env`: Environment variables file (contains the OpenAI API key).
- `requirements.txt`: List of required Python packages.
- `readme.md`: Project documentation.



