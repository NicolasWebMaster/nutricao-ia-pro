# 🥗 Nutrição IA Pro

Sistema inteligente de perguntas e respostas em nutrição baseado em Inteligência Artificial, RAG (Retrieval-Augmented Generation) e evidências científicas de organizações internacionais de saúde.

O projeto foi desenvolvido para fornecer respostas nutricionais contextualizadas, educativas e fundamentadas em fontes confiáveis, reduzindo alucinações comuns em modelos generativos e aumentando a precisão das respostas.

---

# 📌 Objetivo do Projeto

Criar um chatbot especializado em nutrição clínica, esportiva e saúde pública capaz de:

* interpretar perguntas em linguagem natural;
* buscar contexto científico relevante;
* gerar respostas fundamentadas;
* utilizar recuperação semântica com embeddings;
* evitar respostas inventadas;
* aumentar confiabilidade utilizando RAG.

---

# 🧠 Tecnologias Utilizadas

## IA e LLM

* LangChain
* Groq API
* Llama 3.3 70B Versatile

## Processamento Semântico

* HuggingFace Embeddings
* all-mpnet-base-v2

## Vetorização e Busca

* FAISS Vector Store

## Processamento de Texto

* RecursiveCharacterTextSplitter

## Fontes Científicas

* OMS (WHO)
* Ministério da Saúde
* FAO
* NIH
* CDC
* Harvard Nutrition Source

---

# 🏗 Arquitetura da Solução

O sistema utiliza arquitetura RAG (Retrieval-Augmented Generation).

Fluxo da aplicação:

1. O usuário envia uma pergunta.
2. O sistema realiza busca semântica na base vetorial.
3. Os documentos mais relevantes são recuperados.
4. O contexto científico é enviado ao modelo LLM.
5. O modelo gera uma resposta baseada apenas nas evidências encontradas.

Isso reduz significativamente:

* alucinações;
* respostas genéricas;
* informações sem fundamento científico.

---

# 🔍 Como Funciona

## 1. Coleta de Dados

O sistema carrega conteúdos científicos de sites oficiais utilizando WebBaseLoader.

## 2. Chunking

Os documentos são divididos em blocos menores para melhorar recuperação contextual.

## 3. Embeddings

Os textos são convertidos em vetores semânticos utilizando sentence-transformers.

## 4. Vetorização

Os embeddings são armazenados utilizando FAISS.

## 5. Retrieval

Quando o usuário faz uma pergunta, o sistema encontra os trechos semanticamente mais relevantes.

## 6. Geração de Resposta

O modelo LLM utiliza:

* histórico da conversa;
* contexto recuperado;
* prompt especializado.

---

# 🚀 Funcionalidades

* Chat nutricional inteligente
* Memória contextual
* Busca semântica
* Respostas baseadas em evidências
* Arquitetura RAG
* Recuperação vetorial
* Contextualização científica
* Redução de hallucinations

---

# ⚙️ Instalação

## Clone o repositório

```bash
git clone https://github.com/seuusuario/nutricao-ia-pro.git
```

## Acesse a pasta

```bash
cd nutricao-ia-pro
```

## Instale as dependências

```bash
pip install -r requirements.txt
```

## Configure a variável de ambiente

Crie um arquivo `.env`

```env
GROQ_API_KEY=sua_chave
```

## Execute o projeto

```bash
python app.py
```

---

# 📁 Estrutura do Projeto

```bash
nutricao-ia-pro/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── prompts/
├── data/
└── docs/
```

---

# ⚠️ Desafios Superados

Durante o desenvolvimento, os principais desafios foram:

* reduzir alucinações do modelo;
* melhorar relevância contextual;
* selecionar fontes científicas confiáveis;
* otimizar recuperação semântica;
* estruturar memória conversacional;
* equilibrar performance e precisão.

A solução foi utilizar:

* embeddings semânticos;
* retrieval vetorial;
* engenharia de prompts;
* arquitetura RAG.

---

# 🔒 Segurança

As chaves de API são armazenadas em variáveis de ambiente utilizando `.env`, evitando exposição sensível no código-fonte.

---

# 📈 Melhorias Futuras

* Interface Web com Streamlit ou Next.js
* Banco vetorial persistente
* Upload de PDFs científicos
* Sistema multiusuário
* Dashboard analítico
* API REST
* Deploy em nuvem
* Avaliação automática de respostas
* Sistema de citações científicas

---

# 👨‍💻 Autor

Nicolas Ribeiro

Desenvolvedor BackEnd em evolução constante, focado em Inteligência Artificial, automações, arquitetura de sistemas e soluções baseadas em IA.

LinkedIn:
https://www.linkedin.com/in/nicolas-ribeiro-0bb906362/

