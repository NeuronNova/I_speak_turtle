from rdflib import Graph, Namespace, OWL, RDFS

EX1 = Namespace("http://example.org/graph1/")
EX2 = Namespace("http://example.org/graph2/")

align = Graph()
align.bind("ex1", EX1)
align.bind("ex2", EX2)
align.bind("owl", OWL)
align.bind("rdfs", RDFS)

# Entity alignment
align.add((EX1.John, OWL.sameAs, EX2.JohnDoe))

# Property alignment
align.add((EX1.hasName, OWL.equivalentProperty, EX2.fullName))

# Class alignment
align.add((EX2.Employee, RDFS.subClassOf, EX1.Person))

align.serialize("alignment.ttl", format="turtle")

print("alignment.ttl created")