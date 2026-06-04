from src.services.llm_service import generate_response

print("Testing Ollama connection...")
try:
    response = generate_response("What is 2+2? Answer in one word.")
    print(f"AI Response: {response}")
except Exception as e:
    print(f"Test failed: {e}")