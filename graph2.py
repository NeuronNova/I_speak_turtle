from rdflib import Graph, Namespace, RDF, Literal

EX2 = Namespace("http://example.org/graph2/")

g2 = Graph()
g2.bind("ex2", EX2)

# Employee type
g2.add((EX2.JohnDoe, RDF.type, EX2.Employee))

# FIX: Literal for string
g2.add((EX2.JohnDoe, EX2.fullName, Literal("John Smith")))

g2.serialize("graph2.ttl", format="turtle")

print("graph2.ttl created")