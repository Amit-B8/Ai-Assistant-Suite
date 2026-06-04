# library used to send HTTP requests
import requests
# library used to load environment variables from a .env file
import os
# library used to load environment variables from a .env file
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()
# Get the base URL for the Ollama API and the default model from environment variables, with defaults if not set
OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
MODEL = os.getenv("DEFAULT_MODEL", "llama3")

def generate_response(prompt: str):
    """
    Sends a prompt to the local Ollama instance and returns the text response.
    """
    # 1. THE ENDPOINT
    # Combine the base URL with the specific "route" that Ollama uses to generate text.
    # This results in: http://localhost:11434/api/generate
    url = f"{OLLAMA_URL}/api/generate"
    
    # 2. THE PAYLOAD (The Package)
    # APIs communicate using JSON and this dictionary 
    # perfectly matches the structure the Ollama API expects to receive.
    payload = {
        "model": MODEL,      # Tells Ollama which brain to use (llama3)
        "prompt": prompt,    # The actual question or text we want to send
        "stream": False      # False means "wait until the whole answer is ready before sending it back"
    }
    
    # 3. THE EXECUTION & SAFETY NET
    # If the local AI crashes or isn't running, the whole Python application doesn't instantly crash.
    try:
        # Send an HTTP POST request to the URL, attaching the JSON payload.
        # This is where your code pauses and waits for the AI to think.
        response = requests.post(url, json=payload)
        
        # This line is like a strict bouncer. If Ollama returns an error code (like a 404 or 500),
        # this line forces the code to jump straight to the 'except' block below.
        response.raise_for_status() 
        
        # If the request was successful it takes the JSON response from Ollama,
        # extracts just the text inside the "response" key, and return it to our main program.
        return response.json().get("response", "")
        
    except Exception as e:
        # If anything goes wrong return error message
        return f"Error connecting to Ollama: {e}"