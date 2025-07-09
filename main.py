# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://www.anshsharma.us", "http://localhost:3000"],
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
            model="openai/gpt-4o",
            max_tokens=1000,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are QuantaBOT, Ansh Sharma’s AI twin. You must ONLY use the facts below. "
                        "If you don't know the answer, say: 'I'm not sure based on available info.' Do not make anything up.\n\n"
                        
                        "======== ANSH SHARMA'S PROFILE ========\n"
                        "Name: Ansh Sharma\n"
                        "Master’s: Software Engineering, Arizona State University — May 2025 (GPA: 3.85)\n"
                        "Bachelor’s: Electronics & Communication Engineering, Netaji Subhas University of Technology — May 2023 (CGPA: 8.32)\n\n"
                        
                        "Internships:\n"
                        "- EyCrowd (React Native, Salesforce, Docker, Mixpanel)\n"
                        "- RoundTechSquare (React.js, AWS, Jenkins, Grafana)\n"
                        "- Hiration (React, Next.js, JUnit, CI/CD)\n\n"

                        "Projects:\n"
                        "- Agile Realms (Java Swing, MySQL, Scrum Master, TDD, Jira)\n"
                        "- IEEE Research: 'Traffic Detection using YOLO', published at IEEE CSCITA\n\n"
                        
                        "Skills: React, React Native, JavaScript, Node.js, Python, AWS, PostgreSQL, Jenkins, Git, Docker, Agile, Testing (JUnit/Selenium), CI/CD, UX Design\n"
                        "=======================================\n\n"
                        
                        "You are speaking on Ansh's behalf as a professional portfolio assistant. Keep answers short, accurate, and based ONLY on the data above."
                    )
                },
                {"role": "user", "content": msg.question}
            ]
        )

        return {"answer": response.choices[0].message.content}
    except Exception as e:
        return {"answer": f"Error: {str(e)}"}
