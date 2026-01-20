AI Code Reviewer 🔍
An end-to-end AI-powered Python code reviewer built with Streamlit that detects errors, finds unused variables/imports, and provides intelligent suggestions for code improvement.

Features
📝 Code Analysis: Parse and analyze Python code structure
🐛 Error Detection: Identify unused variables and imports
💡 AI Suggestions: Get intelligent recommendations for code improvement
🔄 Code Refactoring: Automatically generate cleaned-up code
📊 Quality Scoring: Receive a code quality score with detailed metrics
Project Structure
ai-code-reviewer/
├── app.py                 # Main Streamlit application
├── code_parser.py         # Code parsing and AST analysis
├── error_detector.py      # Error detection (unused vars/imports)
├── ai_suggestor.py        # AI-powered suggestions
├── requirements.txt       # Python dependencies
└── README.md             # This file
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

Usage
Input Code:
Type or paste Python code directly
Or upload a .py file
Analyze:
Click "Analyze Code" to detect errors and issues
Get Suggestions:
Switch to the "AI Suggestions" tab
Click "Get AI Suggestions" for improvement recommendations
Download:
Download the refactored code with improvements applied
Example
Input:

python
import os
import sys

def calculate_sum(a, b):
    unused_var = 10
    result = a + b
    return result
The tool will detect:

Unused import: os
Unused import: sys
Unused variable: unused_var
And provide suggestions for improvement!

Technologies Used
Streamlit: Web interface
Python AST: Code parsing and analysis
Regular Expressions: Pattern matching and code refactoring
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

License
MIT License - feel free to use this project for learning and development.

Author
Built with ❤️ using Streamlit

Note: This tool analyzes Python code statically. For best results, ensure your code is syntactically correct before analysis.

