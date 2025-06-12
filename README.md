# Knowledge Graph Generator from Text

This project extracts subject–predicate–object triples from any input text and visualizes them as a Knowledge Graph using Python and Streamlit.

## Features
- Triple extraction with spaCy
- Graph construction with NetworkX
- Visualization via PyVis
- Streamlit web app interface

## How to Run
Install dependencies:

pip install spacy streamlit networkx pyvis

python -m spacy download en_core_web_sm

Run in terminal:
streamlit run app.py
