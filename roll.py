"""This is a super simple vector database demonstrating the concepts.

Goal / Challenge
1. write everything from scratch. (notice the imports!). Also write easy to
   read code, expanding out as needed. comprehension is hte goal here!
2. demonstrate the concepts of a vector database with as simple of code
   as possible.
3. Can you improve performance? does the different distance measurements
   help or hurt? What about the embedding model? Tokenizer?

Use
1. make it your own! try writing your own functions, tokenizers, etc.
2. in main uncomment out as needed.
"""

import os


# ----------------------------------------------------------------------
# Building blocks
# ----------------------------------------------------------------------

class SlowWordTokenizer:
    """Totally do not run me on any production system! Hey, I'm demonstrating
    a concept here! This tokenizer doesn't consider white-space, punctionation
    or is overly flexible. I'm trading utility for clarity.

    We just need a way to encode a document.
    """
    def __init__(self, docs: list[str]) -> None:
        self.words: list[str] = []
        # get the words
        for doc in docs:
            doc_words = doc.split()
            for word in doc_words:
                self.words.append(word.lower())
        # lets add our special token
        self.words.append("<UNK>")
        # now make unique
        self.words = list(set(self.words))
        self.unk_token = self.words.index("<UNK>")

    def tokenize(self, text: str) -> list[int]:
        """Tokenizes a text using the trained tokenizer"""
        source_text_words = text.split()
        tokenized_words = []
        # find the index of the word
        for word in source_text_words:
            try:
                idx = self.words.index(word.lower())
                tokenized_words.append(idx)
            except ValueError:
                tokenized_words.append(self.unk_token)
        return tokenized_words

    def decode(self, tokens: list[int]) -> str:
        """Not really used for the VectorDb but showing the way to convert
        back to text.
        """
        words = []
        for token in tokens:
            words.append(self.words[token])
        return " ".join(words)


class SimpleEmbedding:
    """Seriously, don't run this in any production system. This is not
    a great embedding model. again, trading utility for clarity.

    A true embedding model will seek to train a set of weights to transform
    a set of tokens based on the tokens around it. Think sliding window!

    The key here is that it transforms strings of varying length into a
    consistent vector.
    """
    def __init__(self, tokenizer: SlowWordTokenizer) -> None:
        self.tokenizer = tokenizer

    def embed(self, text: str) -> list[float]:
        """Stubs out an embedding model. Lets pretend here that I'm taking
        the tokens and running through a model. I'll reserve embedding for
        a potential future exploration.
        """
        # this has zero reality of a typical embedding model. I'm going
        # with a riff on a bag of words to create an embedding.
        tokens = self.tokenizer.tokenize(text)
        embedding: list[float] = [0.0] * len(self.tokenizer.words)
        for idx in tokens:
            embedding[idx] += 1
        return embedding


def manhattan_distance(
    embedding_a: list[float],
    embedding_b: list[float]
) -> float:
    """A really basic distance measurement"""
    total = 0
    for a, b in zip(embedding_a, embedding_b):
        total += abs(a - b)
    return total


# ----------------------------------------------------------------------
# Here's the database!
# ----------------------------------------------------------------------

class SimpleVectorDatabase:
    """A very simple and basic vector database. Goal is to demonstrate
    the concepts only!
    """
    def __init__(self, docs: list[str]) -> None:
        self.vectors = []
        self.docs = docs
        # train the tokenizer
        self.tokenizer = SlowWordTokenizer(docs)
        self.embedding_model = SimpleEmbedding(self.tokenizer)
        # embed the docs (create the vectors)
        for doc in docs:
            self.vectors.append(self.embedding_model.embed(doc))

    def get_closest_doc(self, text: str) -> str:
        """Putting everything together! Again, this is slow and demonstrates
        the concept.
        """
        closest_dist: float = 10000.0
        closest_idx: int = 0
        search_for = self.embedding_model.embed(text)
        for idx, vec in enumerate(self.vectors):
            dist = manhattan_distance(search_for, vec)
            if closest_dist > dist:
                closest_dist = dist
                closest_idx = idx

        if closest_dist == 10000:
            raise ValueError("No documents found?")
        return self.docs[closest_idx]


# ----------------------------------------------------------------------
# Demoing the building blocks
# ----------------------------------------------------------------------

def get_docs() -> list[str]:
    files = os.listdir("docs")
    docs: list[str] = []
    for file in files:
        file_w_path = os.path.join("docs", file)
        with open(file=file_w_path, mode="r", encoding="utf-8") as infile:
            text = infile.read()
            docs.append(text)
    return docs


def load_database() -> SimpleVectorDatabase:
    # Get the documents from disk
    docs = get_docs()
    # now create the database
    return SimpleVectorDatabase(docs=docs)


# ----------------------------------------------------------------------
# Demos
# ----------------------------------------------------------------------


def demo_tokenizer():
    docs = get_docs()
    tokenizer = SlowWordTokenizer(docs)
    token = tokenizer.tokenize("Rome")
    print(f"The token for Rome is {token}")
    decoded = tokenizer.decode(token)
    print(f"Converted back its {decoded}")


def demo_embedding():
    docs = get_docs()
    tokenizer = SlowWordTokenizer(docs)
    model = SimpleEmbedding(tokenizer)
    embedding = model.embed("Rome")
    print(f"The sum of the embedding is {sum(embedding)}")
    print(f"The length of the embedding is {len(embedding)}")


def demo_distance():
    a = [0.0, 0.0, 0.0]
    b = [1.0, 2.0, 3.0]
    distance = manhattan_distance(a, b)
    print(f"Distance is {distance}")


def demo_db_good():
    print("GOOD SEARCH")
    db = load_database()
    # search for volcanos
    volcano = db.get_closest_doc("Rome Republic")
    print(volcano)


def demo_db_bad():
    print("WEAK SEARCH")
    db = load_database()
    # search for volcanos
    volcano = db.get_closest_doc("Tell me about Rome")
    print(volcano)


if __name__ == "__main__":
    # demo_tokenizer()
    # demo_embedding()
    # demo_distance()
    # demo_db_good()
    demo_db_bad()
