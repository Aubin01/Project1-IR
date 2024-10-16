import pyterrier as pt
import pandas as pd
import re
import json

# Initialize PyTerrier
if not pt.started():
    pt.init()

def load_answers(file_path):
    """Load answers from a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        answers = json.load(file)
    return answers

def load_topics(file_path):
    """Load topics from a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        topics = json.load(file)
    return topics

def filter_empty_documents(answers):
    """Filter out documents that are empty."""
    return [
        {'docno': str(answer['Id']), 'text': answer['Text']}
        for answer in answers if answer['Text'].strip() != ''
    ]

def build_index(answers, index_path="./index"):
    """
    Build an index using PyTerrier's DFIndexer.

    Args:
        answers (list): List of answers (documents) to index.
        index_path (str): The path where the index will be stored.

    Returns:
        index_ref: Reference to the built index.
    """
    # Filter out empty documents
    filtered_answers = filter_empty_documents(answers)

    # Convert to DataFrame
    docs_df = pd.DataFrame(filtered_answers)

    # Create the index using DFIndexer
    indexer = pt.DFIndexer(index_path, overwrite=True)
    index_ref = indexer.index(docs_df["text"], docs_df["docno"])
    
    return index_ref

def clean_query(query):
    """Clean the query text by removing special characters."""
    return re.sub(r'[^\w\s]', '', query)
