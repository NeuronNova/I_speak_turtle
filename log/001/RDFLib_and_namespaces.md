# 001 - Representing Things in RDFlib

RDF's whole idea is that everything is a triple: subject, predicate, object.
So essentially we are not storing rows or documents. We are instead storing *statements*.

`Ashrah studies MachineLearning` is a statement. That's a triple.

In rdflib that looks like this:

```python
from rdflib import Graph, URIRef

g = Graph()

g.add((
    URIRef("http://example.org/Ashrah"),
    URIRef("http://example.org/studies"),
    URIRef("http://example.org/MachineLearning")
))
```

Three URIs. One for subject, another for predicate and the third for object. This is an example of graph edge written by hand.

But typing full URIs every time is time-consuming. And this is where most explanations I came accross
just say "use Namespace for convenience" and move on. but Namespace
is not just convenience.

---

# 002 - Why Namespace Is Not Just Shorthand

When you write `http://example.org/studies` you are not just naming something.
You are *identifying* it globally. That URI could, in theory, be dereferenced.
We could look it up and find out what `studies` means, what domain it belongs
to, how it relates to other predicates.

That's the difference between RDF and a Python dict. A dict key `"studies"` means
whatever we  want it to mean in our program. A URI means something that can be
shared, linked, and reasoned over across systems that have never met each other.

So when we write:

```python
from rdflib import Graph, Namespace

EX = Namespace("http://example.org/")

g = Graph()
g.add((EX.Ashrah, EX.studies, EX.KnowledgeGraphs))
```

`EX.studies` is not a string shortcut. It expands to the full URI
`http://example.org/studies`. The Namespace is just making that expansion
readable without losing what it actually is.

This is also why real ontologies use namespaces we don't own, like:

```python
from rdflib.namespace import FOAF, RDF

g.add((EX.Ashrah, RDF.type, FOAF.Person))
```

`FOAF.Person` expands to `http://xmlns.com/foaf/0.1/Person`, a URI defined
by the FOAF ontology that thousands of datasets already use. When we use it,
our graph connects to all of them. When we invent your own, it connects to none as is obvious.
