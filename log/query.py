from rdflib import Graph

g = Graph()

# load all TTL files
g.parse("graph1.ttl", format="turtle")
g.parse("graph2.ttl", format="turtle")
g.parse("alignment.ttl", format="turtle")

query = """
PREFIX ex1: <http://example.org/graph1/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?name
WHERE {
    ex1:John owl:sameAs ?other .
    ?other ?p ?name .
}
"""

results = g.query(query)

print("\n--- OUTPUT ---")
for row in results:
    print(str(row.name))