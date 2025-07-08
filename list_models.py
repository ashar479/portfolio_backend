import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.base_url = "https://openrouter.ai/api/v1"

models = openai.Model.list()
print([m.id for m in models["data"]])
