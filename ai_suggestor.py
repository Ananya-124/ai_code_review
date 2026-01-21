from google import genai
import os

def get_ai_suggestion(code_string, previous_suggestions, api_key):
    # Initialize the new Client
    client = genai.Client(api_key=api_key)
    
    prompt = f"""
    Review the following code and give concise suggestions.
    Give DIFFERENT suggestions from these: {previous_suggestions}
    
    Explain the 'why' behind improvements (Performance, PEP8, Logic).
    Score submissions based on style compliance.
    
    Code:
    {code_string}
    """
    
    try:
        # Using the new SDK's generate_content method
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return {"message": response.text}
    except Exception as e:
        return {"message": f"Error getting AI suggestion: {str(e)}"}
