from src.services.llm_service import generate_response
from src.templates.prompts import QUIZ_PROMPT
from src.utils.parsers import parse_quiz_json

def generate_quiz_from_text(text: str):
    """
    Generates a structured quiz from the provided text using the LLM.
    """
    # Truncate text if too long for simple local LLM context
    snippet = text[:4000]
    prompt = QUIZ_PROMPT.format(text=snippet)
    
    raw_response = generate_response(prompt)
    quiz_data = parse_quiz_json(raw_response)
    
    return quiz_data, raw_response
