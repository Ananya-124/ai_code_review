import google.generativeai as genai

def get_ai_suggestion(code_string, previous_suggestions=None, api_key=None):
    # Configure the API
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    # Handle the previous context to ensure variety
    if previous_suggestions:
        prev_context = f"Previous suggestions given were: {previous_suggestions}"
    else:
        prev_context = "No previous suggestions."

    # The prompt as seen in your project image
    prompt = f"""
    Review the following Python code and give concise, practical suggestions.
    Give DIFFERENT suggestions from these previous ones: {prev_context}
    
    Explain why Suggestions Were Made: for examples-
    Not just: "Remove unused import"
    But: "Unused imports increase memory usage and reduce code readability."
    
    Focused on scalability, time/space complexity, readability, performance, best practices.
    Follow the PEP8 standard coding guidelines for Coding Style Analysis: Highlight issues like improper indentation, naming conventions.
    Score submissions based on style compliance.
    
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