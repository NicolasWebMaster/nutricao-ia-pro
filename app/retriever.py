from langchain_community.document_loaders import WebBaseLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

from embeddings import get_embeddings


URLS = [
    "https://www.gov.br/saude/pt-br/composicao/saps/promocao-da-saude/guias-alimentares",

    "https://www.who.int/news-room/fact-sheets/detail/healthy-diet",

    "https://www.who.int/health-topics/micronutrients",

    "https://www.fao.org/nutrition/education/food-dietary-guidelines/en/",

    "https://ods.od.nih.gov/factsheets/list-all/",

    "https://www.cdc.gov/nutrition/index.html",

    "https://www.hsph.harvard.edu/nutritionsource/"
]


def build_retriever():

    print("🔄 Carregando documentos...")

    loader = WebBaseLoader(URLS)

    docs = loader.load()


    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=300
    )

    split_docs = splitter.split_documents(docs)


    embeddings = get_embeddings()

    vectorstore = FAISS.from_documents(
        split_docs,
        embeddings
    )

    print("✅ Base vetorial criada!")

    return vectorstore.as_retriever(
        search_kwargs={"k": 6}
    )
