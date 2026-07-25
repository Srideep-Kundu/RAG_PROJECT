# VectorVenger - RAG-Powered Study Assistant 📚🤖

VectorVenger is an intelligent, context-aware study assistant built using a Retrieval-Augmented Generation (RAG) architecture. It allows users to upload massive PDF documents (like textbooks or research papers), ask questions in natural language, and get accurate answers extracted directly from their materials.


---

## 🚀 Tech Stack

- **Language:** Python
- **Framework:** LangChain
- **LLM (Text Generation):** Mistral AI (`ChatMistralAI` - `mistral-small-latest`)
- **Embeddings:** OpenAI (`OpenAIEmbeddings`)
- **Vector Database:** ChromaDB
- **Document Processing:** `PyPDFLoader`, `RecursiveCharacterTextSplitter`
- **User Interface:** Streamlit

---

## 🧠 Core Architecture (How it Works)

The pipeline is divided into two major phases: **Data Ingestion** and **Retrieval & Generation**.

### Phase 1: Data Ingestion (Vector Database Creation)
1. **Document Loading:** The user uploads a PDF. `PyPDFLoader` reads the document and converts it into LangChain document objects.
2. **Text Splitting (Chunking):** Because LLMs have context window limits, the document is broken down into smaller, manageable chunks using `RecursiveCharacterTextSplitter` (e.g., 1000 tokens with a 200-token overlap).
3. **Embedding Generation:** Each chunk is converted into numerical representations (vectors) using OpenAI's Embedding models, capturing semantic meaning.
4. **Vector Storage:** These embeddings are stored locally using **ChromaDB**.

### Phase 2: Retrieval & Generation (Answering Queries)
1. **User Query:** The user asks a question via the Streamlit UI.
2. **Query Embedding:** The question is converted into an embedding using the same OpenAI model.
3. **Similarity Search (Retriever):** ChromaDB compares the query embedding against the stored document embeddings using techniques like **Similarity Search** or **Max Marginal Relevance (MMR)** to fetch the most relevant chunks.
4. **Prompting:** A `ChatPromptTemplate` merges the user's question with the retrieved chunks (context) and defines a system role for the AI.
5. **Generation:** The context-rich prompt is sent to **Mistral AI**, which formulates a precise answer based *only* on the provided PDF data.

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.9+
- [uv](https://github.com/astral-sh/uv) (Package manager used in the course) or `pip`
- API Keys for **OpenAI** (for embeddings) and **Mistral AI** (for chat).

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/course-mate-ai.git
cd course-mate-ai
```

### 2. Create and Activate a Virtual Environment
```bash
uv venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 3. Install Dependencies
Ensure you have your `requirements.txt` ready.
```bash
uv pip install -r requirements.txt
```
*(Key dependencies: `langchain`, `langchain-openai`, `langchain-mistralai`, `langchain-community`, `chromadb`, `pypdf`, `streamlit`, `python-dotenv`)*

### 4. Setup Environment Variables
Create a `.env` file in the root directory and add your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
MISTRAL_API_KEY=your_mistral_api_key_here
```

---

## 🎮 Running the Application

To launch the Streamlit user interface:

```bash
streamlit run app.py
```

1. Open the provided `localhost` URL in your browser.
2. Upload a PDF document using the sidebar/upload widget.
3. Wait for the Vector Database to process and index the document.
4. Start chatting with your study material! 

*(Note: If you upload a new book, the existing `chroma_db` folder will be overwritten/deleted to accommodate the new context).*

---

## 📂 Project Structure

```text
rag-project/
│
├── app.py                # Main Streamlit UI and execution logic
├── create_database.py    # Script to load, chunk, and embed documents into ChromaDB
├── .env                  # Environment variables (API Keys)
├── requirements.txt      # Python dependencies
└── chroma_db/            # Auto-generated local vector database directory
```

---

## 💡 Advanced Retriever Strategies Implemented

While building this, several retrieval strategies were explored:
- **Standard Similarity Search:** Uses Cosine Similarity/Euclidean distance to find the nearest vectors.
- **MMR (Max Marginal Relevance):** Balances relevancy with diversity, ensuring the retrieved chunks aren't just repetitive duplicates of the same idea.
- **MultiQueryRetriever:** Uses an LLM to generate multiple variations of the user's question to overcome poorly worded queries and retrieve a richer set of documents.

---


