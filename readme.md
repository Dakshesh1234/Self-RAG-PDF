# Self-RAG PDF Q&A

This project is a Retrieval-Augmented Generation (RAG) application that answers questions based on the content of a PDF document. It uses a self-correcting RAG workflow built with LangGraph and a Streamlit interface for user interaction.

## Features

- **Retrieval-Augmented Generation (RAG):** Uses a vector store to retrieve relevant document chunks and an LLM to generate answers.
- **Self-Correction:** Implements a graph-based workflow to grade the relevance of retrieved documents and the generated answers, and to rewrite questions for better retrieval.
- **Streamlit UI:** Provides a simple web interface for users to ask questions and get answers.
- **PDF as a Knowledge Base:** Can use any PDF file as the source of information.
- **ChromaDB Vector Store:** Uses ChromaDB to store and retrieve document embeddings.
- **Groq LLM:** Leverages the Groq API for fast and efficient language model interactions.

## How it Works

The application follows a self-correcting RAG workflow implemented using LangGraph. Here's a high-level overview of the process:

1.  **Retrieve:** Given a user's question, the application retrieves relevant document chunks from the ChromaDB vector store.
2.  **Grade Documents:** The retrieved documents are graded for relevance to the question. Irrelevant documents are discarded.
3.  **Decide to Generate:**
    * If relevant documents are found, the application proceeds to generate an answer.
    * If no relevant documents are found, the original question is transformed into a better-phrased question, and the process goes back to the "Retrieve" step.
4.  **Generate:** The LLM generates an answer based on the relevant documents and the user's question.
5.  **Grade Generation:** The generated answer is graded to check for hallucinations and to ensure it addresses the user's question.
    * If the answer is grounded in the documents and answers the question, it is returned to the user.
    * If the answer is not grounded in the documents (hallucination), the generation step is retried.
    * If the answer does not address the question, the question is transformed, and the process goes back to the "Retrieve" step.

## Getting Started

### Prerequisites

- Python 3.7+
- A Groq API key

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/dakshesh1234/self-rag-pdf.git](https://github.com/dakshesh1234/self-rag-pdf.git)
    cd self-rag-pdf
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your environment variables:**
    Create a `.env` file in the root directory and add your Groq API key:
    ```
    GROQ_API_KEY="YOUR_GROQ_API_KEY"
    ```

## Usage

1.  **Add your PDF:**
    Place the PDF file you want to use as a knowledge base in the root directory of the project and name it `Bio-pesticide.pdf`. You can change the PDF file by editing the `pdf_path` variable in `main.py`.

2.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

3.  **Open the application in your browser:**
    Navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

4.  **Ask a question:**
    Enter your question in the text box and click "Get Answer".

## Project Structure
Markdown

# Self-RAG PDF Q&A

This project is a Retrieval-Augmented Generation (RAG) application that answers questions based on the content of a PDF document. It uses a self-correcting RAG workflow built with LangGraph and a Streamlit interface for user interaction.

## Features

- **Retrieval-Augmented Generation (RAG):** Uses a vector store to retrieve relevant document chunks and an LLM to generate answers.
- **Self-Correction:** Implements a graph-based workflow to grade the relevance of retrieved documents and the generated answers, and to rewrite questions for better retrieval.
- **Streamlit UI:** Provides a simple web interface for users to ask questions and get answers.
- **PDF as a Knowledge Base:** Can use any PDF file as the source of information.
- **ChromaDB Vector Store:** Uses ChromaDB to store and retrieve document embeddings.
- **Groq LLM:** Leverages the Groq API for fast and efficient language model interactions.

## How it Works

The application follows a self-correcting RAG workflow implemented using LangGraph. Here's a high-level overview of the process:

1.  **Retrieve:** Given a user's question, the application retrieves relevant document chunks from the ChromaDB vector store.
2.  **Grade Documents:** The retrieved documents are graded for relevance to the question. Irrelevant documents are discarded.
3.  **Decide to Generate:**
    * If relevant documents are found, the application proceeds to generate an answer.
    * If no relevant documents are found, the original question is transformed into a better-phrased question, and the process goes back to the "Retrieve" step.
4.  **Generate:** The LLM generates an answer based on the relevant documents and the user's question.
5.  **Grade Generation:** The generated answer is graded to check for hallucinations and to ensure it addresses the user's question.
    * If the answer is grounded in the documents and answers the question, it is returned to the user.
    * If the answer is not grounded in the documents (hallucination), the generation step is retried.
    * If the answer does not address the question, the question is transformed, and the process goes back to the "Retrieve" step.

## Getting Started

### Prerequisites

- Python 3.7+
- A Groq API key

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/dakshesh1234/self-rag-pdf.git](https://github.com/dakshesh1234/self-rag-pdf.git)
    cd self-rag-pdf
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your environment variables:**
    Create a `.env` file in the root directory and add your Groq API key:
    ```
    GROQ_API_KEY="YOUR_GROQ_API_KEY"
    ```

## Usage

1.  **Add your PDF:**
    Place the PDF file you want to use as a knowledge base in the root directory of the project and name it `Bio-pesticide.pdf`. You can change the PDF file by editing the `pdf_path` variable in `main.py`.

2.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

3.  **Open the application in your browser:**
    Navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

4.  **Ask a question:**
    Enter your question in the text box and click "Get Answer".

## Project Structure

.
├── .gitignore
├── app.py                  # Streamlit web application
├── document_processing.py  # Text splitting and document creation
├── main.py                 # Main application logic
├── nodes.py                # Nodes for the LangGraph workflow
├── pdf_utils.py            # PDF text extraction
├── prompts.py              # Prompts and grading schemas
├── readme.md               # This file
├── requirements.txt        # Python dependencies
├── vectorstore.py          # ChromaDB vector store setup
└── workflow.py             # LangGraph workflow definition

## Dependencies

The main dependencies are listed in the `requirements.txt` file and include:

-   `streamlit`
-   `langchain`
-   `langgraph`
-   `langchain-groq`
-   `chromadb`
-   `pypdf2`
-   `python-dotenv`

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.
