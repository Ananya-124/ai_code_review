import google import genai

def get_ai_suggestion(code_string, previous_suggestions=None, api_key=None):
    # Configure the API
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
    
    # Handle the previous context to ensure variety
    if previous_suggestions:
        prev_context = f"Previous suggestions given were: {previous_suggestions}"
    else:
        prev_context = "No previous suggestions."

    # The prompt as seen in your project image
    prompt = f"""
    Review the following Python code and give concise, practical suggestions.
    "You are a Senior Software Engineer. Analyze the code and provide feedback in 4 distinct sections.\n"
    "Use these exact tags to separate sections:\n"
    "[ERRORS]: List all logical or syntax bugs here.\n"
    "[SUGGESTIONS]: List style, security, and readability improvements if really necessary for the code also suggesr to remove if any unused variables,imports are there.\n"
    "[COMPLEXITY]: Provide Big-O time and space complexity analysis.\n"
    "[FIXED_CODE]: Provide the full corrected code block here only if it has errors and need optimization."
    
    Code:
    {code_string}
    """
    
    try:
        response = model.generate_content(prompt)
        # Returning as a dictionary to match your UI structure
        return {
            "type": "AISuggestion",
            "message": response.text
        }
    except Exception as e:
        return {
            "type": "Error",
            "message": str(e)
        }
