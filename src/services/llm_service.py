import requests
from src.config import OLLAMA_BASE_URL, DEFAULT_MODEL

def generate_response(prompt: str, model: str = DEFAULT_MODEL):
    """
    Sends a prompt to the local Ollama instance and returns the text response.
    """
    url = f"{OLLAMA_BASE_URL}/api/generate"
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status() 
        return response.json().get("response", "")
        
    except Exception as e:
        return f"Error connecting to Ollama: {e}"
