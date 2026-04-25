"""Exploration of ChromaDb

Useful Links:
- https://www.trychroma.com

"""

import os
import chromadb


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


def demo_chroma_db():
    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(name="twenty_docs")
    docs = get_docs()
    # again, slow, not optimal. Going for readability
    for idx, doc in enumerate(docs):
        collection.add(
            ids=[f"id-{idx}"],
            documents=[doc]
        )
    print("GOOD SEARCH")
    result = collection.query(
        query_texts=["Rome Republic"],
        n_results=1
    )
    print(result)

    print("WEAK SEARCH")
    result = collection.query(
        query_texts=["Tell me about Rome"],
        n_results=1
    )
    print(result)


if __name__ == "__main__":
    demo_chroma_db()
