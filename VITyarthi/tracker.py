# tracker.py
from datetime import date
from config import LOGS_FILE
from storage import load_json, save_json
from ai_service import fetch_nutrition
from analytics import show_daily_summary

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