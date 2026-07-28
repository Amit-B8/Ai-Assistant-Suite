import json
import re

def parse_quiz_json(raw_text: str):
    """
    Attempts to extract and parse a JSON array of quiz questions from raw LLM text.
    """
    try:
        # Look for the JSON array in the text
        match = re.search(r'\[\s*\{.*\}\s*\]', raw_text, re.DOTALL)
        if match:
            json_str = match.group(0)
            return json.loads(json_str)
        
        # If no regex match, try parsing the whole thing
        return json.loads(raw_text)
    except Exception as e:
        print(f"Error parsing quiz JSON: {e}")
        return None
