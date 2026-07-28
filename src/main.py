import streamlit as st
from src.services.pdf_service import extract_text_from_pdf
from src.core.engine import generate_quiz_from_text
from src.core.coach_engine import get_coaching_feedback
import os

st.set_page_config(page_title="AI Assistant Suite", layout="wide")

st.title("🚀 AI Assistant Suite")

menu = ["PDF Quiz Generator", "Daily Performance Coach"]
choice = st.sidebar.selectbox("Select Feature", menu)

if choice == "PDF Quiz Generator":
    st.header("📝 PDF Quiz Generator")
    st.write("Upload a PDF study guide to generate a practice quiz.")
    
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Save uploaded file temporarily
        temp_path = "temp_upload.pdf"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        if st.button("Generate Quiz"):
            with st.spinner("Extracting text and generating quiz..."):
                text = extract_text_from_pdf(temp_path)
                if "Error" in text:
                    st.error(text)
                else:
                    quiz_data, raw_response = generate_quiz_from_text(text)
                    
                    if quiz_data:
                        st.success("Quiz Generated!")
                        for i, q in enumerate(quiz_data):
                            st.subheader(f"Q{i+1}: {q['question']}")
                            options = q['options']
                            st.radio(f"Options for Q{i+1}", options, key=f"q{i}")
                            with st.expander("See Answer"):
                                st.write(f"Correct Answer: {q['answer']}")
                    else:
                        st.warning("Could not parse structured quiz. Here is the raw response:")
                        st.code(raw_response)
        
        # Cleanup
        if os.path.exists(temp_path):
            os.remove(temp_path)

elif choice == "Daily Performance Coach":
    st.header("🧠 Daily Performance Coach")
    st.write("Reflect on your day to receive actionable advice.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        tasks = st.text_area("What did you do today?", placeholder="List your completed tasks...")
        wins = st.text_area("What went well?", placeholder="Any successes or wins?")
        struggles = st.text_area("What was a struggle?", placeholder="What blocked you or was difficult?")
        
        if st.button("Get Coaching Feedback"):
            if tasks or wins or struggles:
                with st.spinner("Analyzing your day..."):
                    feedback = get_coaching_feedback(tasks, wins, struggles)
                    st.session_state['coach_feedback'] = feedback
            else:
                st.warning("Please enter some reflections first.")
    
    with col2:
        st.subheader("Coach's Feedback")
        if 'coach_feedback' in st.session_state:
            st.markdown(st.session_state['coach_feedback'])
        else:
            st.write("Your feedback will appear here after you submit your reflections.")
