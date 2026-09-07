# DocMind-AI

An AI-powered document intelligence platform that extracts, understands, and answers questions from PDFs, images, and Word documents using OCR, RAG, and Gemini LLM.

## Folder Structure

```
DocMind-AI/
├── backend/
│   ├── api/          # FastAPI route handlers
│   ├── services/     # Business logic (OCR, RAG, Gemini)
│   └── models/       # Pydantic data models
├── frontend/         # Streamlit UI
├── data/
│   ├── pdfs/         # Uploaded PDF files
│   ├── images/       # Uploaded images
│   └── docs/         # Uploaded Word documents
├── utils/            # Shared utility functions
├── notebooks/        # Jupyter notebooks for experimentation
├── tests/            # Unit and integration tests
├── .vscode/          # VS Code workspace settings
├── .env.example      # Environment variable template
├── .gitignore
├── requirements.txt
└── README.md
```

## Tech Stack

| Layer       | Technology                              |
|-------------|------------------------------------------|
| API         | FastAPI + Uvicorn                        |
| UI          | Streamlit                                |
| OCR         | PyMuPDF, EasyOCR, Pillow                 |
| Embeddings  | Sentence Transformers                    |
| Vector DB   | FAISS                                    |
| LLM         | Google Gemini (`google-generativeai`)    |
| Doc Parsing | python-docx                              |
| Utilities   | NumPy, Pandas, python-dotenv             |

## Setup Instructions

```bash
# 1. Clone the repository
git clone <repo-url>
cd DocMind-AI

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
copy .env.example .env
# Edit .env and add your GEMINI_API_KEY

# 5. Run the backend
uvicorn backend.api.main:app --reload

# 6. Run the frontend (separate terminal)
streamlit run frontend/app.py
```

## Future Features

- [ ] PDF text extraction and chunking
- [ ] OCR for scanned documents and images
- [ ] RAG pipeline with FAISS vector search
- [ ] Gemini-powered Q&A over documents
- [ ] Streamlit chat interface
- [ ] Multi-document support
