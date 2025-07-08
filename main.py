# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://www.anshsharma.us/", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(msg: Message):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are Ansh's AI twin. Answer questions about his skills, projects, and experience."},
                {"role": "user", "content": msg.question}
            ]
        )
        return {"answer": response.choices[0].message.content}
    except Exception as e:
        return {"answer": f"Error: {str(e)}"}
