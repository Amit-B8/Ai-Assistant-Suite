from pypdf import PdfReader
def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts all text from a given PDF file.
    """
    # Initialize an empty container
    text = "" 
    try:
        reader = PdfReader(pdf_path) # Open the file
        for page in reader.pages: # Loop through the document
            content = page.extract_text() # Grab the data
            if content:
                text += content + "\n" # Accumulate and format
        return text
    except Exception as e:
        return f"Error reading PDF: {e}" # Safety check