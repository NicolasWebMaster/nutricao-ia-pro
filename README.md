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

## Fontes Científicas

* OMS (WHO)
* Ministério da Saúde
* FAO
* NIH
* CDC
* Harvard Nutrition Source

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

# ⚙️ Executando o Projeto no Google Colab

Você pode executar o projeto diretamente pelo Google Colab, sem instalar nada no computador.

---

# 🚀 1. Abrir o Google Colab

Acesse:

https://colab.research.google.com/

Faça login com sua conta Google.

---

# 📄 2. Criar um Novo Notebook

Clique em:

```text
Novo notebook
```

ou

```text
New Notebook
```

---

# 📦 3. Instalar as Bibliotecas

Na primeira célula do Colab, cole:

```python
!pip install -q \
langchain \
langchain-community \
langchain-core \
langchain-groq \
langchain-huggingface \
langchain-text-splitters \
faiss-cpu \
sentence-transformers \
huggingface-hub \
beautifulsoup4 \
lxml \
requests
```

Depois clique no botão ▶️ para executar.

A instalação pode demorar alguns minutos.

---

# 🔑 4. Criar a Chave da API Groq

O chatbot utiliza IA da Groq.

---

## Passo 1: Acesse

https://console.groq.com/

---

## Passo 2: Crie uma conta

Você pode entrar usando:
- Google
- GitHub
- E-mail

---

## Passo 3: Faça login

Após entrar, você verá o painel da Groq.

---

## Passo 4: Abrir API Keys

No menu lateral esquerdo:

```text
API Keys
```

Clique nessa opção.

---

## Passo 5: Criar a chave

Clique em:

```text
Create API Key
```

Digite um nome:

```text
nutricao-ia-pro
```

Clique em:

```text
Create
```

---

## Passo 6: Copiar a chave

A chave será parecida com:

```text
gsk_xxxxxxxxxxxxxxxxxxxxx
```

Copie ela.

⚠️ Nunca compartilhe sua chave publicamente.

---

# 🔐 5. Configurar a API no Colab

Crie uma nova célula e cole:

```python
import os

os.environ["GROQ_API_KEY"] = "SUA_CHAVE_AQUI"
```

Substitua:

```python
SUA_CHAVE_AQUI
```

pela sua chave real.

Exemplo:

```python
os.environ["GROQ_API_KEY"] = "gsk_xxxxxxxxxxxxxxxxx"
```

Execute a célula.

---

# 🧠 6. Colocar o Código do Projeto

Crie outra célula e cole todo o código do chatbot.

Depois execute.

---

# ✅ Resultado Esperado

Após carregar:

```text
🥗 NUTRIÇÃO IA PRO
Digite 'sair' para encerrar
```

---

# 💬 Fazendo Perguntas

Digite perguntas como:

```text
O que ajuda no emagrecimento saudável?
```

ou

```text
Quais alimentos possuem mais fibras?
```

---

# ⚠️ Observações Importantes

O primeiro carregamento pode demorar porque:
- os sites científicos são carregados;
- os embeddings são gerados;
- a base vetorial é criada.

Isso é normal.

---

# 🛑 Como Encerrar

Digite:

```text
sair
```

---

# ❌ Erros Comuns

## API Key inválida

Verifique:
- se copiou a chave corretamente;
- se não deixou espaços extras;
- se executou a célula da API antes do chatbot.

---

## Bibliotecas não encontradas

Execute novamente a célula:

```python
!pip install ...
```

---

# 📌 Dica

Se quiser transformar o projeto em algo mais profissional futuramente:
- use Streamlit;
- faça deploy;
- adicione interface web;
- implemente citações científicas;
- utilize banco vetorial persistente.
---

# 👨‍💻 Autor

Nicolas Ribeiro

Desenvolvedor BackEnd em evolução constante, focado em Inteligência Artificial, automações, arquitetura de sistemas e soluções baseadas em IA.

LinkedIn:
https://www.linkedin.com/in/nicolas-ribeiro-0bb906362/

