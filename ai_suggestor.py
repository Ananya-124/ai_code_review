from google import genai

def get_ai_suggestion(code_string, previous_suggestions, api_key):
    client = genai.Client(api_key=api_key)
    
    prompt = f"""
    Previous Context: {previous_suggestions}
    
    Act as a Senior Engineer. Review the code below and provide feedback using EXACTLY these section tags:
    [ERRORS]: (Bugs or logic issues)
    [SUGGESTIONS]: (Style, PEP8, security)
    [COMPLEXITY]: (Big-O analysis)
    [FIXED_CODE]: (Provide ONLY the full corrected code block here)
    
    Code to review:
    {code_string}
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash-lite',
            contents=prompt
        )
        return {"message": response.text}
    except Exception as e:
        return {"message": f"[ERRORS]: {str(e)}"}
