# ⚙️ Ansh Sharma — Portfolio Backend

This is the **backend service** for my personal portfolio website **[anshsharma.us](https://www.anshsharma.us/)**.  
It powers **Quantabot**, my AI assistant, handles API endpoints for portfolio data, and manages **chat logging to AWS S3**.

---

## 📌 Overview

The backend is built with **FastAPI** for high performance and easy API development.  
It integrates with:
- **OpenAI API** — for AI responses in Quantabot
- **AWS S3** — for secure storage of chatbot logs
- **PostgreSQL** — for structured portfolio data
- **RAG (Retrieval-Augmented Generation)** — for accurate, context-aware responses

---

## ✨ Features

- **Quantabot AI Assistant** 🤖 — Answers questions about my skills, projects, education, and achievements
- **Resume Context Injection** — Uses structured resume data for accurate AI responses
- **Chat History Logging** — Uploads logs to AWS S3 bucket `ansh-chat-logs` (`us-west-2` region)
- **REST API Endpoints** — For serving portfolio content to the frontend
- **CORS Configured** — To securely allow frontend requests
- **Lightweight & Fast** — Powered by FastAPI’s async capabilities

---

## 🛠️ Tech Stack

| Component       | Technology |
|-----------------|------------|
| Backend API     | FastAPI (Python) |
| AI Processing   | OpenAI API (gpt‑4o) |
| Data Storage    | PostgreSQL |
| File Storage    | AWS S3 |
| Deployment      | AWS EC2 / Render / Railway |
| Auth & Security | Environment variables via `.env` |

---

## 📂 Folder Structure

portfolio_backend/
│── main.py # FastAPI entrypoint
│── requirements.txt # Python dependencies
│── .env.example # Example environment variables
│── services/
│ ├── chatbot.py # Quantabot logic
│ ├── s3_upload.py # AWS S3 log uploader
│ └── resume_context.py # RAG-based resume context loader
│── routes/
│ ├── chatbot_routes.py # AI chat endpoints
│ ├── projects.py # Projects API
│ └── experience.py # Experience & education API
│── utils/
│ └── formatters.py # Helper functions

yaml
Copy
Edit

---

## 🚀 Running Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/portfolio_backend.git
cd portfolio_backend
2️⃣ Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Configure Environment Variables
Create a .env file:

env
Copy
Edit
OPENAI_API_KEY=your_openai_api_key
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_REGION=us-west-2
S3_BUCKET_NAME=ansh-chat-logs
DATABASE_URL=postgresql://user:password@host:port/dbname
5️⃣ Run the Server
bash
Copy
Edit
uvicorn main:app --reload
Server runs at: http://localhost:8000

📡 API Endpoints
Method	Endpoint	Description
POST	/chat	Send a message to Quantabot
GET	/projects	Get portfolio projects list
GET	/experience	Get work experience & education
GET	/health	Health check

🔒 Security
API keys stored in .env — Never hardcoded

CORS middleware — Only allows requests from anshsharma.us

S3 IAM policy — Restricted to write-only for chat logs

Rate limiting (optional) — Prevents abuse

📚 References
FastAPI Documentation

OpenAI API Reference

AWS S3 Python SDK (boto3)

<p align="center"> Made with ❤️ by <a href="https://www.anshsharma.us/">Ansh Sharma</a> </p> ```
