import os

def ensure_directory_exists(directory_path: str):
    """
    Creates the directory if it does not already exist.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def save_to_file(content: str, file_path: str):
    """
    Saves the given content to a file.
    """
    directory = os.path.dirname(file_path)
    if directory:
        ensure_directory_exists(directory)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
