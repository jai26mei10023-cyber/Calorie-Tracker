# ai_service.py
import os
import json
from google import genai
from config import MODEL_NAME

# API Environment
API_KEY = os.environ.get("GEMINI_API_KEY")

# Initialize the new SDK client
client = genai.Client(api_key=API_KEY) if API_KEY else None

def fetch_nutrition(query):
    if not client:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return []
        
    prompt = f"""
    Analyze the following food description and estimate the nutritional content.
    Food description: "{query}"
    
    Return the response strictly as a JSON array of objects (one for each distinct food item). 
    Each object must have these exact keys: 'name' (string), 'calories' (number), 'protein_g' (number), 'fat_total_g' (number), 'sugar_g' (number).
    Provide only the JSON array, with no markdown formatting blocks or extra text.
    """
    
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        text = response.text.strip()
        
        # Clean up markdown formatting if the model includes it
        if text.startswith('```json'):
            text = text[7:-3].strip()
        elif text.startswith('```'):
            text = text[3:-3].strip()
            
        return json.loads(text)
    except Exception as e:
        print(f"AI Generation Error: {e}")
        return []