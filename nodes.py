from typing import List
from typing_extensions import TypedDict
from langchain.schema import Document
from pprint import pprint

from prompts import (
    retrieval_grader,
    rag_chain,
    hallucination_grader,
    answer_grader,
    question_rewriter,
)

class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        generation: LLM generation
        documents: list of documents 
    """
    question: str
    generation: str
    documents: List[Document]

def retrieve(state, retriever):
    """
    Retrieve documents.

    Args:
        state (dict): The current graph state.
        retriever: The retriever object.

    Returns:
        dict: Updated state with retrieved documents.
    """
    print("---RETRIEVE---")
    question = state["question"]

    # Retrieval
    documents = retriever.get_relevant_documents(question)
    return {"documents": documents, "question": question}

def generate(state):
    """
    Generate an answer.

    Args:
        state (dict): The current graph state.

    Returns:
        dict: Updated state with the generated answer.
    """
    print("---GENERATE---")
    question = state["question"]
    documents = state["documents"]
    
    # Format documents
    formatted_docs = "\n\n".join(doc.page_content for doc in documents)

    # RAG generation
    generation = rag_chain.invoke({"context": formatted_docs, "question": question})
    return {"documents": documents, "question": question, "generation": generation}

def grade_documents(state):
    """
    Determine whether the retrieved documents are relevant to the question.

    Args:
        state (dict): The current graph state.

    Returns:
        dict: Updated state with filtered relevant documents.
    """
    print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
    question = state["question"]
    documents = state["documents"]
    
    # Score each doc
    filtered_docs = []
    for d in documents:
        score = retrieval_grader.invoke({"question": question, "document": d.page_content})
        grade = score.binary_score
        if grade.lower() == "yes":
            print("---GRADE: DOCUMENT RELEVANT---")
            filtered_docs.append(d)
        else:
            print("---GRADE: DOCUMENT NOT RELEVANT---")
            continue
    return {"documents": filtered_docs, "question": question}

def transform_query(state):
    """
    Transform the query to produce a better question.

    Args:
        state (dict): The current graph state.

    Returns:
        dict: Updated state with the rephrased question.
    """
    print("---TRANSFORM QUERY---")
    question = state["question"]
    documents = state["documents"]

    # Re-write question
    better_question = question_rewriter.invoke({"question": question})
    return {"documents": documents, "question": better_question}

def decide_to_generate(state):
    """
    Decide whether to generate an answer or rephrase the question.

    Args:
        state (dict): The current graph state.

    Returns:
        str: Decision for the next node to call.
    """
    print("---ASSESS GRADED DOCUMENTS---")
    filtered_documents = state["documents"]

    if not filtered_documents:
        print("---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---")
        return "transform_query"
    else:
        print("---DECISION: GENERATE---")
        return "generate"

def grade_generation_v_documents_and_question(state):
    """
    Determine whether the generation is grounded in the documents and answers the question.

    Args:
        state (dict): The current graph state.

    Returns:
        str: Decision for the next node to call.
    """
    print("---CHECK HALLUCINATIONS---")
    question = state["question"]
    documents = state["documents"]
    generation = state["generation"]

    # Format documents
    formatted_docs = "\n\n".join(doc.page_content for doc in documents)

    score = hallucination_grader.invoke({"documents": formatted_docs, "generation": generation})
    grade = score.binary_score

    if grade.lower() == "yes":
        print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")
        # Check if generation addresses the question
        print("---GRADE GENERATION VS QUESTION---")
        score = answer_grader.invoke({"question": question, "generation": generation})
        grade = score.binary_score
        if grade.lower() == "yes":
            print("---DECISION: GENERATION ADDRESSES QUESTION---")
            return "useful"
        else:
            print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")
            return "not useful"
    else:
        print("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")
        return "not supported"