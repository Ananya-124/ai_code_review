import streamlit as st
import os
from dotenv import load_dotenv
from ai_suggestor import get_ai_suggestion
from error_detector import detect_issues
from code_parser import parse_code

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

st.set_page_config(page_title="AI Code Reviewer", layout="wide")
st.title("🔍 AI Code Reviewer")

# Initialize session state
if "ai_response" not in st.session_state:
    st.session_state.ai_response = ""
if "history" not in st.session_state:
    st.session_state.history = []

code_input = st.text_area("Paste your code:", height=250, placeholder="Write or paste your Python code here...")

col1, col2, _ = st.columns([1, 2, 5])
with col1:
    analyze_btn = st.button("Analyze", type="primary")
with col2:
    new_suggestion_btn = st.button("Get New Suggestion")

if analyze_btn or new_suggestion_btn:
    if not code_input.strip():
        st.error("Please paste code first.")
    else:
        # 1. Run Parser and Static Analysis
        tree, syntax_error = parse_code(code_input)
        
        # If syntax is broken, issues will just be empty/default
        if not syntax_error:
            issues = detect_issues(tree)
        else:
            issues = {"unused_variables": [], "unused_imports": []}

        # 2. AI Suggestion Logic (Always runs, even with syntax errors)
        with st.spinner("AI is analyzing your code..."):
            history_context = "\n".join(st.session_state.history[-3:])
            # We pass the syntax error to the AI so it can help fix it
            full_context = f"{code_input}\n\n[System Note: The parser detected this error: {syntax_error}]" if syntax_error else code_input
            
            result = get_ai_suggestion(full_context, history_context, GEMINI_API_KEY)
            st.session_state.ai_response = result["message"]
            st.session_state.history.append(result["message"])

        # 3. User Interface Display
        tab1, tab2 = st.tabs(["📊 Detected Issues", "🤖 AI Suggestions"])
        
        with tab1:
            st.subheader("Static Analysis & Syntax")
            
            if syntax_error:
                st.error(f"**Syntax Error Found:** {syntax_error}")
                st.info("The AI has provided a fix for this error in the next tab.")
            else:
                st.success("✅ Code is syntactically correct.")
                
                # Show unused vars/imports only if syntax is clean
                u_vars = issues.get('unused_variables', [])
                u_imports = issues.get('unused_imports', [])
                
                if u_vars:
                    st.warning(f"**Unused Variables:** {', '.join(u_vars)}")
                if u_imports:
                    st.warning(f"**Unused Imports:** {', '.join(u_imports)}")
                if not u_vars and not u_imports:
                    st.info("No unused variables or imports detected.")

        with tab2:
            st.subheader(f"AI Feedback (Review #{len(st.session_state.history)})")
            st.markdown(st.session_state.ai_response)