import streamlit as st
from main import app  # Import the workflow

# Streamlit page setup
st.set_page_config(page_title="RAG Q&A", layout="centered")

# Sidebar instructions
st.sidebar.title("Instructions")
st.sidebar.info(
    """
    - Enter a question related to your document.
    - The app will use RAG (Retrieval-Augmented Generation) with Self Reflection to retrieve and generate an answer.
    """
)
st.sidebar.markdown(
    """
    ---
    ### **Dakshesh Hirwani**
    *21EC39039*
    ---
    """
)

# Main interface
st.title("RAG Workflow Q&A")

# User input
user_question = st.text_input("Your Question:", value="what this document is about")

# Submit button
if st.button("Get Answer") and user_question.strip():
    # Run the RAG workflow
    inputs = {"question": user_question}
    final_generation = None
    
    try:
        spinner_placeholder = st.empty()
        spinner_placeholder.text("Processing...")

        # Display a loading spinner
        iteration = 1
        with st.spinner(""):
            for output in app.stream(inputs, {"recursion_limit": 8}):
                for key, value in output.items():
                    xx = len(value["documents"])
                    if(key == "transform_query"): iteration += 1
                    spinner_placeholder.text(f"Iteration = {iteration}")
                    

        spinner_placeholder.text(f"")
        # Display the final answer
        if value["generation"]:
            st.success("Answer:")
            st.write(value["generation"])
        else:
            st.error("Sorry, I didn't understand your question. Do you want to connect with a live agent?")
    
    except Exception as e:
        spinner_placeholder.text(f"")
        st.error("Sorry, I didn't understand your question. Do you want to connect with a live agent?")
        
        
# streamlit run app.py