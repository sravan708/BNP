from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from chatbot import ask_ai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "BNP Finance Backend Running"}


@app.post("/chat")
def chat(request: ChatRequest):
    answer = ask_ai(request.message)
    return {"reply": answer}