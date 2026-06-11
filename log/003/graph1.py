from rdflib import Graph, Namespace, RDF, Literal

EX1 = Namespace("http://example.org/graph1/")

g1 = Graph()
g1.bind("ex1", EX1)

g1.add((EX1.John, RDF.type, EX1.Person))

# FIX: wrap string in Literal
g1.add((EX1.John, EX1.hasName, Literal("John Smith")))

g1.serialize("graph1.ttl", format="turtle")

print("graph1.ttl created")
