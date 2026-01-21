from google import genai
import os

def get_ai_suggestion(code_string, previous_suggestions, api_key):
    # Initialize the new Client
    client = genai.Client(api_key=api_key)
    
    prompt = f"""
    Review the following code and give concise suggestions.
    Give DIFFERENT suggestions from these: {previous_suggestions}
    
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
        # Using the new SDK's generate_content method
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite", 
            contents=prompt
        )
        return {"message": response.text}
    except Exception as e:
        return {"message": f"Error getting AI suggestion: {str(e)}"}
