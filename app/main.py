import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from retriever import build_retriever
from memory import ConversationMemory
from prompts import SYSTEM_PROMPT


load_dotenv()

os.environ["USER_AGENT"] = "NutriBotPro/1.0"


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2,
    api_key=os.getenv("GROQ_API_KEY")
)


retriever = build_retriever()

memory = ConversationMemory()


prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),

    ("user",
     """
Histórico:
{historico}

Contexto científico:
{contexto}

Pergunta:
{pergunta}
""")
])

chain = prompt | llm


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


print("=" * 70)
print("🥗 NUTRIÇÃO IA PRO")
print("Digite 'sair' para encerrar")
print("=" * 70)


while True:

    pergunta = input("\n🧑 Você: ")

    if pergunta.lower() == "sair":
        print("\n👋 Encerrando...")
        break


    docs = retriever.invoke(pergunta)

    contexto = format_docs(docs)

    historico = memory.get_history()


    resposta = chain.invoke({
        "historico": historico,
        "contexto": contexto,
        "pergunta": pergunta
    })


    memory.add_user_message(pergunta)
    memory.add_ai_message(resposta.content)


    print("\n🤖 Nutrição IA Pro:\n")
    print(resposta.content)
    print("-" * 70)
