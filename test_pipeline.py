from src.services.pdf_service import extract_text_from_pdf
from src.services.llm_service import generate_response

def run_integration_pipeline():
    print("1. Extracting text from PDF...")
    # Make sure sample.pdf is in the main project folder
    pdf_text = extract_text_from_pdf("sample.pdf") 
    
    # Check if the PDF extraction failed
    if "Error reading PDF" in pdf_text:
        print(pdf_text)
        return

    print(f"Success! Extracted {len(pdf_text)} characters.")
    
    # We grab just the first 1000 characters so we don't overwhelm your local AI 
    # context window on the very first try.
    text_snippet = pdf_text[:1000] 

    print("\n2. Sending instructions and text to AI (this may take a moment)...")
    prompt = f"Please summarize the following document snippet in exactly one sentence:\n\n{text_snippet}"
    
    response = generate_response(prompt)
    
    print("\n--- AI Response ---")
    print(response)

if __name__ == "__main__":
    run_integration_pipeline()