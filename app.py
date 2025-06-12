import streamlit as st
from kg import *
text = st.text_area("Enter text to convert into KG")
if st.button("Generate KG"):
    triples = extract_triples(text)
    G = build_graph(triples)
    visualize_graph(G)
    st.write("Knowledge Graph saved to kg.html")
    st.components.v1.html(open("kg.html", 'r').read(), height=500)