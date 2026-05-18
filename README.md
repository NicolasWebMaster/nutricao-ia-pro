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

# ⚙️ Instalação e Configuração

Este projeto funciona em:

- Windows
- Linux
- macOS

Antes de começar, você precisa ter instalado:

- Python 3.10 ou superior
- Git
- Uma conta na Groq Cloud

---

# 🐍 1. Instalando o Python

## Windows

1. Acesse:
https://www.python.org/downloads/

2. Baixe a versão mais recente do Python.

3. Durante a instalação:
   marque a opção:

```text
Add Python to PATH
```

4. Clique em:
```text
Install Now
```

5. Após instalar, abra o terminal e teste:

```bash
python --version
```

---

## Linux

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

Teste:

```bash
python3 --version
```

---

## macOS

Instale usando Homebrew:

```bash
brew install python
```

Teste:

```bash
python3 --version
```

---

# 🔧 2. Instalando o Git

## Windows

Baixe:
https://git-scm.com/download/win

Instale normalmente.

Teste:

```bash
git --version
```

---

## Linux

```bash
sudo apt install git
```

---

## macOS

```bash
brew install git
```

---

# 📥 3. Clonando o Projeto

Abra o terminal e execute:

```bash
git clone https://github.com/seuusuario/nutricao-ia-pro.git
```

Depois entre na pasta:

```bash
cd nutricao-ia-pro
```

---

# 🧪 4. Criando Ambiente Virtual

Ambientes virtuais evitam conflitos entre bibliotecas Python.

---

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Se o ambiente estiver ativo, aparecerá algo assim no terminal:

```text
(venv)
```

---

# 📦 5. Instalando Dependências

Execute:

```bash
pip install -r requirements.txt
```

Isso instalará:
- LangChain
- FAISS
- HuggingFace
- Groq SDK
- Embeddings
- Bibliotecas auxiliares

---

# 🔑 6. Criando a Chave da API Groq

O projeto utiliza modelos de IA da Groq.

---

## Passo 1: Acesse o site oficial

https://console.groq.com/

---

## Passo 2: Criar conta

Você pode criar conta usando:

- Google
- GitHub
- E-mail

Clique em:

```text
Sign Up
```

---

## Passo 3: Fazer login

Após criar a conta:

1. Faça login.
2. Você será redirecionado ao painel da Groq Cloud.

---

## Passo 4: Abrir menu de API Keys

No menu lateral esquerdo:

```text
API Keys
```

Clique nessa opção.

---

## Passo 5: Criar nova chave

Clique em:

```text
Create API Key
```

Digite um nome para sua chave.

Exemplo:

```text
nutricao-ia-pro
```

Clique em:

```text
Create
```

---

## Passo 6: Copiar a chave

A Groq mostrará uma chave parecida com:

```text
gsk_xxxxxxxxxxxxxxxxxxxxxxxxx
```

Copie essa chave.

⚠️ Importante:
Nunca compartilhe sua chave publicamente.

---

# 🔐 7. Configurando a API no Projeto

Na raiz do projeto, crie um arquivo chamado:

```text
.env
```

Dentro dele coloque:

```env
GROQ_API_KEY=sua_chave_aqui
```

Exemplo:

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxx
```

---

# ▶️ 8. Executando o Projeto

Agora execute:

## Windows

```bash
python app/main.py
```

---

## Linux/macOS

```bash
python3 app/main.py
```

---

# ✅ Resultado Esperado

Se tudo estiver funcionando corretamente, aparecerá:

```text
======================================================================
🥗 NUTRIÇÃO IA PRO
Digite 'sair' para encerrar
======================================================================
```

Agora basta fazer perguntas normalmente no terminal.

Exemplo:

```text
O que ajuda no emagrecimento saudável?
```

---

# 🛑 Como Encerrar

Digite:

```text
sair
```

---

# ⚠️ Possíveis Erros

## Erro: Python não encontrado

Instale o Python corretamente e reinicie o terminal.

---

## Erro: pip não reconhecido

Use:

```bash
python -m pip install -r requirements.txt
```

---

## Erro: API Key inválida

Verifique:
- se a chave foi copiada corretamente;
- se o arquivo `.env` está na raiz do projeto;
- se não existem espaços extras.

---

# 📌 Observações

O primeiro carregamento pode demorar alguns segundos, pois:
- os documentos científicos são processados;
- os embeddings são gerados;
- a base vetorial é criada.

Após isso, o chatbot estará pronto para responder perguntas com base em evidências científicas.
--

# 👨‍💻 Autor

Nicolas Ribeiro

Desenvolvedor BackEnd em evolução constante, focado em Inteligência Artificial, automações, arquitetura de sistemas e soluções baseadas em IA.

LinkedIn:
https://www.linkedin.com/in/nicolas-ribeiro-0bb906362/

