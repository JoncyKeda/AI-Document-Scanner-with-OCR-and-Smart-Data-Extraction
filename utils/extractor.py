import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_fields(text):
    prompt = f"""
    Extract the following fields from the document text:

    - Name
    - Date
    - Total Amount
    - Items (as a list)

    Return ONLY valid JSON format like:
    {{
        "name": "...",
        "date": "...",
        "amount": "...",
        "items": ["...", "..."]
    }}

    Text:
    {text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert data extraction assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    result = response['choices'][0]['message']['content']

    # Try parsing JSON safely
    try:
        return json.loads(result)
    except:
        return {"error": "Failed to parse JSON", "raw_output": result}
