# AI Assistant Suite

A modular AI-powered toolkit featuring an automated Quiz Generator from PDFs and a Daily Performance Coach.

## Features
- **PDF Quiz Generator:** Extracts text from study guides and generates quizzes via local LLM.
- **AI Performance Coach:** Reflects on your daily tasks and suggests actionable improvements.

## Setup
1. Clone the repo.
2. Create virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (or `venv\Scripts\activate`)
4. Install requirements: `pip install -r requirements.txt`
5. Ensure [Ollama](https://ollama.com/) is running locally.

## Usage
Run the Streamlit application:
`streamlit run src/main.py`