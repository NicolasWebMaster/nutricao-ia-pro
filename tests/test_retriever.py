from app.retriever import build_retriever


def test_retriever():

    retriever = build_retriever()

    assert retriever is not None
