import openai
import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from .openai_client import generate_flashcards
from .wiki_loader import parse

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with your GitHub Pages domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate_flashcards")
def generate(term: str):
    try:
        text = parse(term)
        flashcards = generate_flashcards(text)
        return {"flashcards": flashcards}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
