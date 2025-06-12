import spacy
import networkx as nx
from pyvis.network import Network

nlp = spacy.load("en_core_web_sm")

def extract_triples(text):
    doc = nlp(text)
    triples = []
    for sent in doc.sents:
        for token in sent:
            if token.dep_ == "ROOT":
                subject = [w.text for w in token.lefts if w.dep_ in ("nsubj", "nsubjpass")]
                obj = [w.text for w in token.rights if w.dep_ in ("dobj", "pobj")]
                if subject and obj:
                    triples.append((subject[0], token.lemma_, obj[0]))
    return triples

def build_graph(triples):
    G = nx.DiGraph()
    for s, p, o in triples:
        G.add_edge(s, o, label=p)
    return G


def visualize_graph(G):
    net = Network(notebook=True, directed=True)
    for u, v, data in G.edges(data=True):
        net.add_node(u)
        net.add_node(v)
        net.add_edge(u, v, label=data['label'])
    net.show("kg.html")


