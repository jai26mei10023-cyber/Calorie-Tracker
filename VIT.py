import os
import json
import hashlib
from datetime import date
from google import genai

# API Environment
API_KEY = os.environ.get("GEMINI_API_KEY")

# Initialize the new SDK client
client = genai.Client(api_key=API_KEY) if API_KEY else None

# AI Model
MODEL_NAME = 'gemini-3.6-flash'

USERS_FILE = 'users.json'
LOGS_FILE = 'logs.json'

# Standard Recommended Dietary Allowance (RDA) reference values
RDA = {
    'calories': 2000.0,
    'protein_g': 50.0,
    'fat_total_g': 78.0,
    'sugar_g': 50.0
}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_json(filename):
    if not os.path.exists(filename):
        return {}
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def register():
    users = load_json(USERS_FILE)
    print("\n--- Register ---")
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists.")
        return None
    password = input("Enter a password: ")
    users[username] = hash_password(password)
    save_json(USERS_FILE, users)
    print("Registration successful.")
    return username

def login():
    users = load_json(USERS_FILE)
    print("\n--- Login ---")
    username = input("Enter username: ")
    if username not in users:
        print("User not found.")
        return None
    password = input("Enter password: ")
    if users[username] == hash_password(password):
        print("Login successful.")
        return username
    else:
        print("Incorrect password.")
        return None

def fetch_nutrition(query):
    prompt = f"""
    Analyze the following food description and estimate the nutritional content.
    Food description: "{query}"
    
    Return the response strictly as a JSON array of objects (one for each distinct food item). 
    Each object must have these exact keys: 'name' (string), 'calories' (number), 'protein_g' (number), 'fat_total_g' (number), 'sugar_g' (number).
    Provide only the JSON array, with no markdown formatting blocks or extra text.
    """
    
    try:
        # Updated method call for the google.genai package
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

def log_food(username):
    query = input("\nEnter food description (e.g., '1 cup of milk and 2 eggs'): ")
    print("Analyzing food AI...")
    items = fetch_nutrition(query)
    
    if not items:
        print("No nutritional data could be extracted for that description.")
        return

    daily_totals = {'calories': 0, 'protein_g': 0, 'fat_total_g': 0, 'sugar_g': 0}
    
    print("\nLogged Items:")
    for item in items:
        print(f"- {item.get('name', 'Unknown').capitalize()}: {item.get('calories', 0)} kcal")
        for key in daily_totals:
            daily_totals[key] += item.get(key, 0)

    logs = load_json(LOGS_FILE)
    if username not in logs:
        logs[username] = {}
    
    today = str(date.today())
    if today not in logs[username]:
        logs[username][today] = {'calories': 0, 'protein_g': 0, 'fat_total_g': 0, 'sugar_g': 0}
    
    for key in daily_totals:
        logs[username][today][key] += daily_totals[key]
        
    save_json(LOGS_FILE, logs)
    print("Data saved successfully.")
    show_daily_summary(username, today, logs)

def show_daily_summary(username, today, logs=None):
    if logs is None:
        logs = load_json(LOGS_FILE)
    
    stats = logs.get(username, {}).get(today, {'calories': 0, 'protein_g': 0, 'fat_total_g': 0, 'sugar_g': 0})
    
    print(f"\n=== Daily Summary ({today}) ===")
    print(f"{'Metric':<15} | {'Consumed':<10} | {'RDA':<10} | {'% of RDA':<10}")
    print("-" * 55)
    
    for key, rda_val in RDA.items():
        consumed = stats.get(key, 0)
        pct = (consumed / rda_val) * 100
        metric_name = key.replace('_g', '').replace('_total', '').capitalize()
        print(f"{metric_name:<15} | {consumed:<10.1f} | {rda_val:<10.1f} | {pct:.1f}%")

def main():
    if not client:
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Please set it before running the tracker.")
        return

    current_user = None
    
    while True:
        if not current_user:
            choice = input("\n1. Login\n2. Register\n3. Exit\nSelect option: ")
            if choice == '1':
                current_user = login()
            elif choice == '2':
                current_user = register()
            elif choice == '3':
                break
            else:
                print("Invalid input.")
        else:
            choice = input("\n1. Log Food\n2. View Today's Summary\n3. Logout\nSelect option: ")
            if choice == '1':
                log_food(current_user)
            elif choice == '2':
                show_daily_summary(current_user, str(date.today()))
            elif choice == '3':
                current_user = None
                print("Logged out.")
            else:
                print("Invalid input.")
if __name__ == "__main__":
    main()