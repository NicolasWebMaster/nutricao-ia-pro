from app.embeddings import get_embeddings


def test_embeddings():

    embeddings = get_embeddings()

    assert embeddings is not None
