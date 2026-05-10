# Insurance Rules RAG System

AI-powered insurance rule validation system using:

- Node.js
- Express
- PostgreSQL
- pgvector
- OpenRouter embeddings
- RAG architecture
- Semantic similarity search

---

## Features

- Rule validation
- Conflict detection
- Duplicate detection
- Semantic similarity matching
- Vector search with pgvector
- Recommendation engine
- Frontend UI
- REST API

---

## Recommendation Tags

- Exact_Match
- High_Severity_Match
- Duplicated_Add_to_list
- Low_Severity_Match

---

## Technologies

- Express.js
- PostgreSQL
- pgvector
- OpenRouter
- Docker
- HTML/CSS frontend

---

## Run Project

### Install packages

```bash
npm install
```

### Run backend

```bash
node server.js
```

### Open frontend

Open:

```text
index.html
```

with Live Server.

---

## RAG Flow

1. Rules are indexed into pgvector
2. Embeddings are created using OpenRouter
3. Similarity search finds related rules
4. Recommendation engine returns validation tags