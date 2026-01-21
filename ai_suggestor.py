from google import genai

def get_ai_suggestion(code_string, previous_suggestions=None, api_key=None):
    # 1. Initialize the Client
    client = genai.Client(api_key=api_key)
    
    # Handle context
    prev_context = f"Previous suggestions: {previous_suggestions}" if previous_suggestions else "No previous suggestions."

    prompt = f"""
    {prev_context}
    
    Review the following Python code as a Senior Software Engineer and provide feedback in 4 distinct sections.
    Use these exact tags:
    [ERRORS]: List all logical or syntax bugs here.
    [SUGGESTIONS]: List style, security, and readability improvements.
    [COMPLEXITY]: Provide Big-O time and space complexity analysis.
    [FIXED_CODE]: Provide the full corrected code block here only if it has errors and needs optimization.
    
    Code:
    {code_string}
    """
    
    try:
        # 2. Use the client to generate content
        # Note: 'gemini-2.0-flash' is the stable current version; verify your specific model name.
        response = client.models.generate_content(
            model='gemini-2.5-flash-lite', 
            contents=prompt
        )
        
        return {
            "type": "AISuggestion",
            "message": response.text
        }
    except Exception as e:
        return {
            "type": "Error",
            "message": str(e)
        }
