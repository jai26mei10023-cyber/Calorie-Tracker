# analytics.py
from config import LOGS_FILE, RDA
from storage import load_json

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