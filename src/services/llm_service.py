import requests
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
MODEL = os.getenv("DEFAULT_MODEL", "llama3")

def generate_response(prompt: str):
    """
    Sends a prompt to the local Ollama instance and returns the text response.
    """
    url = f"{OLLAMA_URL}/api/generate"
    payload = {
        "model": MODEL,
        "prompt": prompt,
         # Set this to True later when we want to show it typing
        "stream": False 
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status() # This will raise an error if the connection fails
        return response.json().get("response", "")
    except Exception as e:
        return f"Error connecting to Ollama: {e}"