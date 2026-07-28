from src.services.llm_service import generate_response
from src.templates.prompts import COACH_PROMPT

def get_coaching_feedback(tasks: str, wins: str, struggles: str):
    """
    Generates coaching feedback based on daily reflections.
    """
    prompt = COACH_PROMPT.format(tasks=tasks, wins=wins, struggles=struggles)
    response = generate_response(prompt)
    return response
