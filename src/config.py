import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Ollama Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "llama3")

# Directory Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOURNALS_DIR = os.path.join(BASE_DIR, "journals")
QUIZZES_DIR = os.path.join(BASE_DIR, "quizzes")
