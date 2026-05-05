from fastapi import FastAPI
from models import QueryRequest
from data_store import DataStore
from ollama_client import generate_response
from utils import build_prompt

app = FastAPI()

store = DataStore()

@app.post("/ask")
def ask_question(request: QueryRequest):
    # Step 1: Search (vectorless)
    context = store.search(request.question)

    # Step 2: Build prompt
    prompt = build_prompt(context, request.question)

    # Step 3: LLM call
    answer = generate_response(prompt)

    return {
        "question": request.question,
        "context_found": context,
        "answer": answer
    }