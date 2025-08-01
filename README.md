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
git clone https://github.com/Billy-Flowers/RAG-LangChain-Project
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
python rag_app/query_rag.py "where was the wizard of Oz from"
```

Example output:

```text
Answer the question based on the above context: What did the Wizard of Oz give the Scarecrow, and why?

Response:  The Great and Terrible (Wizard) promised to grant the Scarecrow a lot of new brains if he killed the Wicked Witch of the West. The reason for this was that by killing her, the Scarecrow hoped to earn these 'great many good brains' which would fulfill his wish and make him as 
wise as any other person in Oz.
Sources: ['src\\data\\source\\the_wonderful_wizard_of_oz.pdf:73:0', 'src\\data\\source\\the_wonderful_wizard_of_oz.pdf:23:3', 'src\\data\\source\\the_wonderful_wizard_of_oz.pdf:47:0', 'src\\data\\source\\the_wonderful_wizard_of_oz.pdf:46:3', 'src\\data\\source\\the_wonderful_wizard_of_oz.pdf:15:3']
```

## Model Configuration
### Current Setup (Ollama - Local)
The project currently uses phi3:mini for optimal speed/performance balance:
```
OLLAMA_MODEL_ID = "phi3:mini"
```

### Ollama Model Options:

- phi3:mini (3.8B) - Current default, good balance
- gemma:2b (2B) - Very fast, smaller model
- codellama:7b (7B) - Better for code-related queries
- llama3:70b (70B) - Best quality, very slow

### Speed Comparison
- Ollama (Local): 5-30 seconds per query
- Cloud APIs: 1-5 seconds per query
- Groq (Free tier eligible)

### OpenAI (Recommended for production)
- Install: pip install langchain-openai
- Set API key: export OPENAI_API_KEY="your-key"
- Replace model initialization:
```
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
```

### Optimization Tips
- Reduce context size: Change k=3 to k=1 in similarity search (recommended only for shorter pdfs 1-8 pages)
- Use smaller models: Switch to phi3:mini or gemma:2b
- Switch to cloud APIs: 10x+ speed improvement
- Cache model initialization: Model is loaded once at module level
