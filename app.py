

import streamlit as st
import os
import re
from dotenv import load_dotenv
from ai_suggestor import get_ai_suggestion
from error_detector import detect_issues
from code_parser import parse_code

# Load environment variables
load_dotenv()
# Check local .env first, then Streamlit Secrets for deployment
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

st.set_page_config(page_title="AI Code Reviewer Pro", layout="wide", page_icon="🚀")

# --- Custom CSS for High Visibility & Modern UI ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    
    /* FIX: Dark background for text area with bright green text for visibility */
    .stTextArea>div>div>textarea { 
        font-family: 'Source Code Pro', monospace; 
        background-color: #1e1e1e !important; 
        color: #00ff00 !important; 
        border: 2px solid #4CAF50;
        padding: 10px;
    }

    /* Button Styling */
    .stButton>button { 
        width: 100%; 
        border-radius: 8px; 
        font-weight: bold;
    }
    
    /* Metrics Styling */
    [data-testid="stMetricValue"] { color: #4CAF50; }
    </style>
    """, unsafe_allow_html=True)

# --- Session State ---
if "ai_response" not in st.session_state: st.session_state.ai_response = ""
if "history" not in st.session_state: st.session_state.history = []

# --- Sidebar ---
with st.sidebar:
    st.title("⚙️ Control Panel")
    selected_lang = st.selectbox("Select Language", ["Python", "JavaScript", "Java", "C++", "HTML/CSS"])
    st.info("Static analysis (AST) is currently active for Python.")
    if st.button("🗑️ Clear Review History"):
        st.session_state.history = []
        st.session_state.ai_response = ""
        st.rerun()

# --- Main UI ---
st.title("🔍 AI Code Reviewer Pro")
st.write("Paste your code below for a comprehensive review by a simulated Senior AI Engineer.")

code_input = st.text_area("Input Code Editor:", height=300, placeholder="Enter your code here...")

col1, col2, _ = st.columns([1.5, 1.5, 4])
with col1:
    analyze_btn = st.button("🚀 Analyze Code", type="primary")
with col2:
    new_suggestion_btn = st.button("🔄 Get New Suggestion")

# --- Analysis Logic ---
if analyze_btn or new_suggestion_btn:
    if not code_input.strip():
        st.error("Text area is empty. Please provide code.")
    elif not GEMINI_API_KEY:
        st.error("API Key not found. Please set GOOGLE_API_KEY in Secrets or .env.")
    else:
        # 1. Static Analysis (Python Only)
        syntax_error = None
        issues = {"unused_variables": [], "unused_imports": []}
        
        if selected_lang == "Python":
            tree, syntax_error = parse_code(code_input)
            if not syntax_error:
                issues = detect_issues(tree)

        # 2. AI Call
        with st.spinner("🤖 AI is reviewing your logic and style..."):
            history_context = "\n".join(st.session_state.history[-2:])
            full_context = f"Language: {selected_lang}\nCode: {code_input}"
            if syntax_error: full_context += f"\nNote: The parser found this syntax error: {syntax_error}"
            
            result = get_ai_suggestion(full_context, history_context, GEMINI_API_KEY)
            st.session_state.ai_response = result["message"]
            st.session_state.history.append(result["message"])

# --- Results Display ---
if st.session_state.ai_response:
    res = st.session_state.ai_response
    
    # Extraction Logic
    def extract_section(tag, text):
        pattern = rf"\[{tag}\](.*?)(?=\[|$)"
        match = re.search(pattern, text, re.DOTALL)
        return match.group(1).strip() if match else "N/A"

    t1, t2, t3, t4 = st.tabs(["📊 Analysis", "💡 Suggestions", "⏱️ Complexity", "🛠️ Fixed Code"])

    with t1:
        if selected_lang == "Python":
            if syntax_error:
                st.error(f"**Syntax Error Detected:** {syntax_error}")
            else:
                st.success("✅ Syntax Check Passed")
                c1, c2 = st.columns(2)
                c1.metric("Unused Variables", len(issues['unused_variables']))
                c2.metric("Unused Imports", len(issues['unused_imports']))
        else:
            st.info(f"Local parsing skipped for {selected_lang}. AI Analysis below.")
        
        st.subheader("Logical Errors (AI Detected)")
        st.warning(extract_section("ERRORS", res))

    with t2:
        st.subheader("Improvement Suggestions")
        st.markdown(extract_section("SUGGESTIONS", res))

    with t3:
        st.subheader("Computational Complexity")
        st.code(extract_section("COMPLEXITY", res))

    with t4:
        st.subheader("Optimized Version")
        fixed = extract_section("FIXED_CODE", res).replace("```python", "").replace("```", "")
        st.code(fixed, language=selected_lang.lower())
