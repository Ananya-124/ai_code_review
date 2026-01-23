AI Code Reviewer 🔍
An end-to-end AI-powered Python code reviewer built with Streamlit that detects errors, finds unused variables/imports, and provides intelligent suggestions for code improvement.

Check it out here -> https://aicodereview-wcjmccmkhjyasxaljjgf9m.streamlit.app/

Features
📝 Code Analysis: Parse and analyze Python code structure
🐛 Error Detection: Identify unused variables and imports
💡 AI Suggestions: Get intelligent recommendations for code improvement
🔄 Code Refactoring: Automatically generate cleaned-up code
📊 Quality Scoring: Receive a code quality score with detailed metrics
Project Structure
ai-code-reviewer/
app.py                 # Main Streamlit application
code_parser.py         # Code parsing and AST analysis
error_detector.py      # Error detection (unused vars/imports)
ai_suggestor.py        # AI-powered suggestions
requirements.txt       # Python dependencies
README.md             # This file

Installation
Local Setup
Clone the repository:
bash
git clone https://github.com/yourusername/ai-code-reviewer.git
cd ai-code-reviewer
Create a virtual environment (optional but recommended):
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:
bash
pip install -r requirements.txt
Run the application:
bash
streamlit run app.py
The app will open in your browser at http://localhost:8501

Deployment to Streamlit Cloud
Step 1: Push to GitHub
Create a new repository on GitHub
Initialize git in your project folder:
bash
git init
git add .
git commit -m "Initial commit: AI Code Reviewer"
git branch -M main
git remote add origin https://github.com/yourusername/ai-code-reviewer.git
git push -u origin main

Step 2: Deploy on Streamlit Cloud
Go to share.streamlit.io
Sign in with your GitHub account
Click "New app"
Fill in the deployment details:
Repository: Select your ai-code-reviewer repository
Branch: main
Main file path: app.py
Click "Deploy"
Your app will be live in a few minutes at: https://yourusername-ai-code-reviewer-app-xxxxx.streamlit.app




Ananya 
Built with ❤️ using Streamlit



