# 002 : spaCy separates delimiters unlike naive Python tokenization

One interesting thing I noticed immediately:

spaCy treats punctuation as independent tokens.

```python
import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("This is Muhammed Ashrah. I am going to hit 4, 4 and 6.")

for token in doc:
    print(token)
```

Output:

```text
This
is
Muhammed
Ashrah
.
I
am
going
to
hit
4
,
4
and
6
.
```

What makes this interesting is that a naive tokenizer from scratch usually does something like:

```python
text.split()
```

which would produce:

```text
Ashrah.
4,
```

meaning delimiters stay attached to words/numbers.

spaCy intentionally separates them because punctuation itself carries structural meaning in language.
