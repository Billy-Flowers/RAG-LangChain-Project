# RAG LangChain Project

A Retrieval-Augmented Generation (RAG) application built with LangChain that allows you to query documents using natural language. The system uses ChromaDB for vector storage and supports multiple LLM providers.

## Features

- Document ingestion and vector storage with ChromaDB
- Natural language querying with source attribution
- Multiple LLM provider support (Ollama, OpenAI, Groq)
- Command-line interface for easy querying

## Getting Started

### Prerequisites

- Python 3.8+
- Ollama installed (for local models)

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd RAG-LangChain-Project
```

### Installing Requirements

```sh
pip install -r requirements.txt
```

### Generate the database

```sh
# Execute from root directory.
python populate_database.py --reset
```

### Running the app

```sh
# Execute from src directory
cd src
python rag_app/query_rag.py "how much does a landing page cost?"
```

Example output:

```text
Answer the question based on the above context: How much does a landing page cost to develop?

Response:  Based on the context provided, the cost for a landing page service offered by Galaxy Design Agency is $4,820. Specifically, under the "Our Services" section, it states "Landing Page for Small Businesses ($4,820)" when describing the landing page service. So the cost listed for a landing page is $4,820.
Sources: ['src/data/source/galaxy-design-client-guide.pdf:1:0', 'src/data/source/galaxy-design-client-guide.pdf:7:0', 'src/data/source/galaxy-design-client-guide.pdf:7:1']
```

## Model Configuration
### Current Setup (Ollama - Local)
The project currently uses phi3:mini for optimal speed/performance balance:
```
OLLAMA_MODEL_ID = "phi3:mini"
```

## Ollama Model Options
### Fast & Lightweight:

- phi3:mini (3.8B) - Current default, good balance
- gemma:2b (2B) - Very fast, smaller model
- codellama:7b (7B) - Better for code-related queries
- llama3:70b (70B) - Best quality, very slow

## Performance Optimization
### Speed Comparison
- Ollama (Local): 5-30 seconds per query
- Cloud APIs: 1-5 seconds per query
- Groq (Free tier eligible)

### Cloud API Options (Faster)
For significantly better speed, switch to cloud APIs:

### OpenAI (Recommended for production)
- Install: pip install langchain-openai
- Set API key: export OPENAI_API_KEY="your-key"
- Replace model initialization:
```
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
```

### Optimization Tips
- Reduce context size: Change k=3 to k=1 in similarity search
- Use smaller models: Switch to phi3:mini or gemma:2b
- Switch to cloud APIs: 10x+ speed improvement
- Cache model initialization: Model is loaded once at module level
